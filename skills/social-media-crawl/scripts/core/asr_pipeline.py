#!/usr/bin/env python3
"""Shared ASR pipeline helpers for runner scripts."""

import json
import re
import threading
import time
import urllib.error
import urllib.request
from urllib.parse import urlparse, urlunparse
from typing import Any, Callable, Dict, List, Optional, Tuple

from scripts.core.tikomni_common import (
    call_json_api,
    deep_find_first,
    extract_task_id,
    extract_task_status,
    extract_transcript_text,
    is_terminal_status,
    normalize_text,
)
from scripts.core.u3_fallback import run_u3_public_url_fallback

U2_BATCH_SUBMIT_HARD_LIMIT = 100
DEFAULT_U2_PENDING_TIMEOUT_SEC = 60
SUMMARY_TEXT_FIELDS = (
    "full_text",
    "transcript_text",
    "transcription_text",
    "result_text",
    "summary_text",
    "transcript",
    "transcription",
    "result",
    "content",
    "text",
)
SEGMENT_CONTAINER_FIELDS = ("sentences", "segments", "paragraphs")
SEGMENT_TEXT_FIELDS = ("text", "sentence", "content", "paragraph", "transcript_text")
CHAR_SPACED_RUN_RE = re.compile(r"(?:[A-Za-z0-9\u4e00-\u9fff]{1,4}\s+){5,}[A-Za-z0-9\u4e00-\u9fff]{1,4}")


def clamp_u2_batch_submit_size(size: int, *, default: int = 50, hard_limit: int = U2_BATCH_SUBMIT_HARD_LIMIT) -> int:
    try:
        parsed = int(size)
    except Exception:
        parsed = int(default)
    parsed = max(1, parsed)
    return min(parsed, max(1, int(hard_limit)))


def submit_u2_asr(
    *,
    base_url: str,
    token: str,
    timeout_ms: int,
    video_url: str,
) -> Dict[str, Any]:
    return submit_u2_asr_batch(
        base_url=base_url,
        token=token,
        timeout_ms=timeout_ms,
        file_urls=[video_url],
    )


def submit_u2_asr_batch(
    *,
    base_url: str,
    token: str,
    timeout_ms: int,
    file_urls: List[str],
) -> Dict[str, Any]:
    normalized_urls = normalize_media_candidates(file_urls)
    limited_urls = normalized_urls[:U2_BATCH_SUBMIT_HARD_LIMIT]
    return call_json_api(
        base_url=base_url,
        path="/api/u2/v1/services/audio/asr/transcription",
        token=token,
        method="POST",
        timeout_ms=timeout_ms,
        body={"input": {"file_urls": limited_urls}},
    )


def is_retriable_submit_failure(response: Dict[str, Any]) -> bool:
    status_code = response.get("status_code")
    if isinstance(status_code, str) and status_code.isdigit():
        status_code = int(status_code)
    if isinstance(status_code, (int, float)) and int(status_code) in {502, 503, 504}:
        return True

    error_reason = str(response.get("error_reason") or "").upper()
    return "UPSTREAM_TIMEOUT" in error_reason or "TIMEOUT" in error_reason


def submit_u2_asr_batch_with_retry(
    *,
    base_url: str,
    token: str,
    timeout_ms: int,
    file_urls: List[str],
    max_retries: int,
    backoff_ms: int,
    progress_callback: Optional[Callable[[Dict[str, Any]], None]] = None,
) -> Dict[str, Any]:
    retries = max(0, int(max_retries))
    base_backoff = max(0, int(backoff_ms))
    max_attempts = 1 + retries

    normalized_urls = normalize_media_candidates(file_urls)
    limited_urls = normalized_urls[:U2_BATCH_SUBMIT_HARD_LIMIT]
    if not limited_urls:
        return {
            "submit_response": {
                "ok": False,
                "status_code": None,
                "error_reason": "no_valid_file_urls",
                "data": {},
                "request_id": None,
            },
            "task_id": None,
            "retry_chain": [],
            "final_submit_status": "failed_no_valid_file_urls",
            "file_urls": [],
        }

    retry_chain: List[Dict[str, Any]] = []
    final_response: Dict[str, Any] = {}
    final_task_id: Optional[str] = None
    final_submit_status = "failed_unknown"

    def _emit_submit_progress(event: Dict[str, Any]) -> None:
        if progress_callback is None:
            return
        try:
            progress_callback(event)
        except Exception:
            pass

    for attempt in range(1, max_attempts + 1):
        wait_ms = 0 if attempt == 1 else base_backoff * (2 ** (attempt - 2))
        if wait_ms > 0:
            time.sleep(wait_ms / 1000.0)

        _emit_submit_progress(
            {
                "phase": "submit",
                "state": "started",
                "attempt": attempt,
                "wait_ms": wait_ms,
                "candidate_count": len(limited_urls),
            }
        )

        heartbeat_stop = threading.Event()

        def _heartbeat() -> None:
            while not heartbeat_stop.wait(5.0):
                _emit_submit_progress(
                    {
                        "phase": "submit",
                        "state": "heartbeat",
                        "attempt": attempt,
                        "wait_ms": wait_ms,
                        "candidate_count": len(limited_urls),
                    }
                )

        heartbeat_thread = threading.Thread(target=_heartbeat, daemon=True)
        heartbeat_thread.start()

        try:
            submit_response = submit_u2_asr_batch(
                base_url=base_url,
                token=token,
                timeout_ms=timeout_ms,
                file_urls=limited_urls,
            )
        finally:
            heartbeat_stop.set()
            heartbeat_thread.join(timeout=0.2)
        task_id = extract_task_id(submit_response.get("data"))
        retriable = is_retriable_submit_failure(submit_response)

        _emit_submit_progress(
            {
                "phase": "submit",
                "state": "finished",
                "attempt": attempt,
                "wait_ms": wait_ms,
                "candidate_count": len(limited_urls),
                "task_id": task_id,
                "status_code": submit_response.get("status_code"),
                "ok": bool(submit_response.get("ok")),
                "error_reason": submit_response.get("error_reason"),
                "request_id": submit_response.get("request_id"),
                "retriable": retriable,
            }
        )

        retry_chain.append(
            {
                "attempt": attempt,
                "wait_ms": wait_ms,
                "status_code": submit_response.get("status_code"),
                "error_reason": submit_response.get("error_reason"),
                "ok": submit_response.get("ok"),
                "task_id": task_id,
                "retriable": retriable,
                "file_url_count": len(limited_urls),
            }
        )

        final_response = submit_response
        final_task_id = task_id

        if submit_response.get("ok") and task_id:
            final_submit_status = "success"
            break

        if submit_response.get("ok") and not task_id:
            final_submit_status = "failed_missing_task_id"
            break

        if retriable and attempt < max_attempts:
            final_submit_status = "retrying"
            continue

        final_submit_status = "failed_retries_exhausted" if retriable else "failed_non_retriable"
        break

    return {
        "submit_response": final_response,
        "task_id": final_task_id,
        "retry_chain": retry_chain,
        "final_submit_status": final_submit_status,
        "file_urls": limited_urls,
    }


def submit_u2_asr_with_retry(
    *,
    base_url: str,
    token: str,
    timeout_ms: int,
    video_url: str,
    max_retries: int,
    backoff_ms: int,
    progress_callback: Optional[Callable[[Dict[str, Any]], None]] = None,
) -> Dict[str, Any]:
    return submit_u2_asr_batch_with_retry(
        base_url=base_url,
        token=token,
        timeout_ms=timeout_ms,
        file_urls=[video_url],
        max_retries=max_retries,
        backoff_ms=backoff_ms,
        progress_callback=progress_callback,
    )


def clean_transcript_text(raw_text: Any) -> str:
    if raw_text is None:
        return ""
    return normalize_text(raw_text)


def _text_signature(text: str) -> str:
    return re.sub(r"[\W_]+", "", clean_transcript_text(text)).lower()


def _is_char_spaced_noise_sequence(text: str) -> bool:
    tokens = [token for token in clean_transcript_text(text).split(" ") if token]
    if len(tokens) < 6:
        return False
    single_char_tokens = sum(1 for token in tokens if len(token) == 1)
    short_tokens = sum(1 for token in tokens if len(token) <= 2)
    cjk_tokens = sum(1 for token in tokens if any("\u4e00" <= char <= "\u9fff" for char in token))
    return (
        single_char_tokens >= 4
        and short_tokens / max(len(tokens), 1) >= 0.75
        and cjk_tokens / max(len(tokens), 1) >= 0.5
    )


def _strip_char_spaced_noise_runs(text: str) -> str:
    def _replace(match: re.Match[str]) -> str:
        chunk = match.group(0)
        return " " if _is_char_spaced_noise_sequence(chunk) else chunk

    cleaned = CHAR_SPACED_RUN_RE.sub(_replace, text)
    return re.sub(r"\s+", " ", cleaned).strip()


def _ensure_sentence_end(text: str) -> str:
    if not text:
        return text
    if text[-1] in "。！？!?" or text.endswith("..."):
        return text
    return f"{text}。"


def derive_asr_clean_text(asr_raw: Any, legacy_clean: Any = None) -> str:
    base = clean_transcript_text(asr_raw) or clean_transcript_text(legacy_clean)
    if not base:
        return ""

    denoised = _strip_char_spaced_noise_runs(base)
    denoised = re.sub(r"\b(嗯|啊|呃|额|那个|这个|然后|就是)\b", " ", denoised)
    denoised = re.sub(r"(嗯+|啊+|呃+)", " ", denoised)
    denoised = re.sub(r"(就是就是|然后然后|这个这个|那个那个)", " ", denoised)
    denoised = re.sub(r"\s+", " ", denoised).strip()

    units = [clean_transcript_text(part) for part in re.split(r"[。！？!?；;\n]+", denoised)]
    sentences: List[str] = []
    signatures: List[str] = []
    for unit in units:
        if not unit or _is_char_spaced_noise_sequence(unit):
            continue
        sentence = _ensure_sentence_end(unit)
        signature = _text_signature(sentence)
        if not signature:
            continue
        duplicate = False
        for existing in signatures:
            if signature == existing:
                duplicate = True
                break
            smaller = signature if len(signature) <= len(existing) else existing
            larger = existing if len(signature) <= len(existing) else signature
            if len(smaller) >= 12 and smaller in larger:
                duplicate = True
                break
        if duplicate:
            continue
        signatures.append(signature)
        sentences.append(sentence)
    if not sentences:
        fallback = _ensure_sentence_end(denoised)
        return fallback if fallback else ""

    paragraphs: List[str] = []
    bucket: List[str] = []
    for sentence in sentences:
        bucket.append(sentence)
        if len(bucket) >= 3:
            paragraphs.append("\n".join(bucket))
            bucket = []

    if bucket:
        if len(bucket) == 1 and paragraphs:
            paragraphs[-1] = f"{paragraphs[-1]}\n{bucket[0]}"
        else:
            paragraphs.append("\n".join(bucket))

    return "\n\n".join(paragraphs)


def _extract_summary_text_from_node(node: Dict[str, Any]) -> Tuple[str, str]:
    for key in SUMMARY_TEXT_FIELDS:
        value = node.get(key)
        if isinstance(value, str):
            cleaned = clean_transcript_text(value)
            if cleaned:
                return cleaned, key
    return "", ""


def _append_segment_lines(node: Any, lines: List[str]) -> None:
    if isinstance(node, str):
        cleaned = clean_transcript_text(node)
        if cleaned:
            lines.append(cleaned)
        return
    if isinstance(node, dict):
        for key in SEGMENT_TEXT_FIELDS:
            value = node.get(key)
            if isinstance(value, str):
                cleaned = clean_transcript_text(value)
                if cleaned:
                    lines.append(cleaned)
                    break
        return
    if isinstance(node, list):
        for item in node:
            _append_segment_lines(item, lines)


def _extract_segment_text_from_node(node: Dict[str, Any]) -> str:
    lines: List[str] = []
    for key in SEGMENT_CONTAINER_FIELDS:
        if key not in node:
            continue
        _append_segment_lines(node.get(key), lines)
        if lines:
            break
    if not lines:
        return ""

    deduped: List[str] = []
    seen = set()
    for line in lines:
        signature = _text_signature(line)
        if not signature or signature in seen or _is_char_spaced_noise_sequence(line):
            continue
        seen.add(signature)
        deduped.append(line)
    return "\n".join(deduped).strip()


def _extract_canonical_transcript_from_node(node: Dict[str, Any]) -> Dict[str, Any]:
    summary_text, summary_field = _extract_summary_text_from_node(node)
    if summary_text:
        return {
            "transcript_text": summary_text,
            "summary_field_used": summary_field,
            "segment_fallback_used": False,
            "canonical_text_source": f"summary:{summary_field}",
        }

    segment_text = _extract_segment_text_from_node(node)
    if segment_text:
        return {
            "transcript_text": segment_text,
            "summary_field_used": "",
            "segment_fallback_used": True,
            "canonical_text_source": "segments",
        }

    fallback_text = clean_transcript_text(extract_transcript_text(node))
    if fallback_text:
        return {
            "transcript_text": fallback_text,
            "summary_field_used": "",
            "segment_fallback_used": True,
            "canonical_text_source": "deep_search_fallback",
        }

    return {
        "transcript_text": "",
        "summary_field_used": "",
        "segment_fallback_used": False,
        "canonical_text_source": "missing",
    }


def extract_u2_task_metrics(payload: Any) -> Dict[str, Any]:
    metrics = deep_find_first(payload, ["task_metrics", "metrics"])
    return metrics if isinstance(metrics, dict) else {}


def _safe_int(value: Any) -> int:
    if isinstance(value, bool):
        return int(value)
    if isinstance(value, (int, float)):
        return int(value)
    if isinstance(value, str):
        text = value.strip()
        if not text:
            return 0
        try:
            return int(float(text))
        except Exception:
            return 0
    return 0


def _status_upper(value: Any) -> str:
    return str(value or "").strip().upper()


def _is_success_status(status: str) -> bool:
    return status in {"SUCCEEDED", "SUCCESS", "COMPLETED", "DONE"}


def _is_failed_status(status: str) -> bool:
    return status in {"FAILED", "FAILURE", "ERROR", "CANCELED", "CANCELLED"}


def extract_platform_task_status(payload: Any) -> str:
    status = deep_find_first(payload, ["platform_task_status"])
    return _status_upper(status)


def extract_pending_count(payload: Any) -> int:
    return max(0, _safe_int(deep_find_first(payload, ["pending_count"])))


def extract_u2_batch_result_items(payload: Any) -> List[Dict[str, Any]]:
    found: Dict[str, Dict[str, Any]] = {}

    stack: List[Any] = [payload]
    while stack:
        node = stack.pop(0)
        if isinstance(node, dict):
            raw_file_url = (
                node.get("file_url")
                or node.get("source_url")
                or node.get("media_url")
                or node.get("url")
            )
            file_url = normalize_media_url(str(raw_file_url or ""))
            if file_url:
                canonical = _extract_canonical_transcript_from_node(node)
                transcript = clean_transcript_text(canonical.get("transcript_text"))

                status = _status_upper(node.get("status") or node.get("task_status") or node.get("state"))
                error_reason = str(node.get("error_reason") or node.get("error") or "").strip()
                transcription_url = normalize_text(node.get("transcription_url"))
                ok = _is_success_status(status) or bool(transcript) or bool(transcription_url)

                candidate = {
                    "file_url": file_url,
                    "transcript_text": transcript,
                    "task_status": status,
                    "transcription_url": transcription_url,
                    "error_reason": error_reason,
                    "ok": ok,
                    "summary_field_used": canonical.get("summary_field_used", ""),
                    "segment_fallback_used": bool(canonical.get("segment_fallback_used")),
                    "canonical_text_source": canonical.get("canonical_text_source", "missing"),
                }

                existing = found.get(file_url)
                if existing is None:
                    found[file_url] = candidate
                else:
                    old_score = (
                        1 if existing.get("ok") else 0,
                        1 if not existing.get("segment_fallback_used") else 0,
                        1 if existing.get("summary_field_used") else 0,
                        len(str(existing.get("transcript_text") or "")),
                        1 if existing.get("transcription_url") else 0,
                        1 if not existing.get("error_reason") else 0,
                    )
                    new_score = (
                        1 if candidate.get("ok") else 0,
                        1 if not candidate.get("segment_fallback_used") else 0,
                        1 if candidate.get("summary_field_used") else 0,
                        len(str(candidate.get("transcript_text") or "")),
                        1 if candidate.get("transcription_url") else 0,
                        1 if not candidate.get("error_reason") else 0,
                    )
                    if new_score > old_score:
                        found[file_url] = candidate

            for value in node.values():
                if isinstance(value, (dict, list)):
                    stack.append(value)
        elif isinstance(node, list):
            for item in node:
                if isinstance(item, (dict, list)):
                    stack.append(item)

    return list(found.values())


def map_u2_batch_results_by_file_url(payload: Any) -> Dict[str, Dict[str, Any]]:
    mapped: Dict[str, Dict[str, Any]] = {}
    for item in extract_u2_batch_result_items(payload):
        file_url = normalize_media_url(item.get("file_url"))
        if not file_url:
            continue
        mapped[file_url] = item
    return mapped


def _parse_non_negative_item_index(value: Any) -> Optional[int]:
    if isinstance(value, bool):
        return None
    if isinstance(value, int):
        return value if value >= 0 else None
    if isinstance(value, float):
        if value < 0 or not value.is_integer():
            return None
        return int(value)
    if isinstance(value, str):
        text = value.strip()
        if not text or not text.isdigit():
            return None
        return int(text)
    return None


def map_u2_batch_results_by_item_index(payload: Any) -> Dict[int, Dict[str, Any]]:
    mapped: Dict[int, Dict[str, Any]] = {}
    stack: List[Any] = [payload]

    while stack:
        node = stack.pop(0)
        if isinstance(node, dict):
            item_index_raw = node.get("item_index")
            item_index = _parse_non_negative_item_index(item_index_raw)
            if item_index is not None:
                canonical = _extract_canonical_transcript_from_node(node)
                transcript = clean_transcript_text(canonical.get("transcript_text"))

                status = _status_upper(node.get("task_status") or node.get("status") or node.get("state"))
                error_reason = str(node.get("error_reason") or node.get("error") or "").strip()
                transcription_url = normalize_text(node.get("transcription_url"))
                ok = _is_success_status(status) or bool(transcript) or bool(transcription_url)

                candidate = {
                    "item_index": item_index,
                    "transcript_text": transcript,
                    "task_status": status,
                    "error_reason": error_reason,
                    "transcription_url": transcription_url,
                    "ok": ok,
                    "summary_field_used": canonical.get("summary_field_used", ""),
                    "segment_fallback_used": bool(canonical.get("segment_fallback_used")),
                    "canonical_text_source": canonical.get("canonical_text_source", "missing"),
                }

                existing = mapped.get(item_index)
                if existing is None:
                    mapped[item_index] = candidate
                else:
                    old_score = (
                        1 if existing.get("ok") else 0,
                        1 if not existing.get("segment_fallback_used") else 0,
                        1 if existing.get("summary_field_used") else 0,
                        len(str(existing.get("transcript_text") or "")),
                        1 if existing.get("transcription_url") else 0,
                        1 if not existing.get("error_reason") else 0,
                    )
                    new_score = (
                        1 if candidate.get("ok") else 0,
                        1 if not candidate.get("segment_fallback_used") else 0,
                        1 if candidate.get("summary_field_used") else 0,
                        len(str(candidate.get("transcript_text") or "")),
                        1 if candidate.get("transcription_url") else 0,
                        1 if not candidate.get("error_reason") else 0,
                    )
                    if new_score > old_score:
                        mapped[item_index] = candidate

            for value in node.values():
                if isinstance(value, (dict, list)):
                    stack.append(value)
        elif isinstance(node, list):
            for item in node:
                if isinstance(item, (dict, list)):
                    stack.append(item)

    return mapped


def _extract_transcript_from_transcription_payload(payload: Any) -> str:
    if isinstance(payload, str):
        text = clean_transcript_text(payload)
        if text:
            return text
        try:
            payload = json.loads(payload)
        except Exception:
            return ""

    for key in SUMMARY_TEXT_FIELDS:
        transcript = clean_transcript_text(deep_find_first(payload, [key]))
        if transcript:
            return transcript

    for key in SEGMENT_CONTAINER_FIELDS:
        segments = deep_find_first(payload, [key])
        if segments is None:
            continue
        lines: List[str] = []
        _append_segment_lines(segments, lines)
        deduped: List[str] = []
        seen = set()
        for line in lines:
            signature = _text_signature(line)
            if not signature or signature in seen or _is_char_spaced_noise_sequence(line):
                continue
            seen.add(signature)
            deduped.append(line)
        if deduped:
            return "\n".join(deduped)

    transcript = clean_transcript_text(extract_transcript_text(payload))
    if transcript:
        return transcript

    return ""


def _extract_transcript_bundle_from_transcription_payload(payload: Any) -> Dict[str, Any]:
    if isinstance(payload, str):
        text = clean_transcript_text(payload)
        if text:
            return {
                "transcript_text": text,
                "summary_field_used": "raw_string",
                "segment_fallback_used": False,
                "canonical_text_source": "summary:raw_string",
            }
        try:
            payload = json.loads(payload)
        except Exception:
            return {
                "transcript_text": "",
                "summary_field_used": "",
                "segment_fallback_used": False,
                "canonical_text_source": "missing",
            }

    for key in SUMMARY_TEXT_FIELDS:
        transcript = clean_transcript_text(deep_find_first(payload, [key]))
        if transcript:
            return {
                "transcript_text": transcript,
                "summary_field_used": key,
                "segment_fallback_used": False,
                "canonical_text_source": f"summary:{key}",
            }

    for key in SEGMENT_CONTAINER_FIELDS:
        segments = deep_find_first(payload, [key])
        if segments is None:
            continue
        lines: List[str] = []
        _append_segment_lines(segments, lines)
        deduped: List[str] = []
        seen = set()
        for line in lines:
            signature = _text_signature(line)
            if not signature or signature in seen or _is_char_spaced_noise_sequence(line):
                continue
            seen.add(signature)
            deduped.append(line)
        if deduped:
            return {
                "transcript_text": "\n".join(deduped),
                "summary_field_used": "",
                "segment_fallback_used": True,
                "canonical_text_source": f"segments:{key}",
            }

    transcript = clean_transcript_text(extract_transcript_text(payload))
    if transcript:
        return {
            "transcript_text": transcript,
            "summary_field_used": "",
            "segment_fallback_used": True,
            "canonical_text_source": "deep_search_fallback",
        }

    return {
        "transcript_text": "",
        "summary_field_used": "",
        "segment_fallback_used": False,
        "canonical_text_source": "missing",
    }


def fetch_transcription_text_by_url(*, transcription_url: str, timeout_ms: int) -> Dict[str, Any]:
    url = normalize_media_url(transcription_url)
    if not url:
        return {
            "ok": False,
            "transcription_url": "",
            "error_reason": "transcription_url_missing",
            "transcript_text": "",
        }
    if not (url.startswith("http://") or url.startswith("https://")):
        return {
            "ok": False,
            "transcription_url": url,
            "error_reason": "transcription_url_invalid",
            "transcript_text": "",
        }

    request = urllib.request.Request(url=url, method="GET", headers={"Accept": "application/json"})
    try:
        with urllib.request.urlopen(request, timeout=max(timeout_ms / 1000.0, 1.0)) as response:
            raw_text = response.read().decode("utf-8", errors="replace")
    except urllib.error.URLError as error:
        return {
            "ok": False,
            "transcription_url": url,
            "error_reason": f"transcription_fetch_failed:{normalize_text(getattr(error, 'reason', error)) or 'unknown'}",
            "transcript_text": "",
        }
    except Exception as error:
        return {
            "ok": False,
            "transcription_url": url,
            "error_reason": f"transcription_fetch_failed:{normalize_text(error) or 'unknown'}",
            "transcript_text": "",
        }

    payload: Any = raw_text
    try:
        payload = json.loads(raw_text)
    except Exception:
        payload = raw_text

    transcript_bundle = _extract_transcript_bundle_from_transcription_payload(payload)
    transcript = transcript_bundle.get("transcript_text", "")
    if transcript:
        return {
            "ok": True,
            "transcription_url": url,
            "error_reason": "",
            "transcript_text": transcript,
            "summary_field_used": transcript_bundle.get("summary_field_used", ""),
            "segment_fallback_used": bool(transcript_bundle.get("segment_fallback_used")),
            "canonical_text_source": transcript_bundle.get("canonical_text_source", "missing"),
        }

    return {
        "ok": False,
        "transcription_url": url,
        "error_reason": "transcription_payload_empty",
        "transcript_text": "",
        "summary_field_used": "",
        "segment_fallback_used": False,
        "canonical_text_source": "missing",
    }


def hydrate_u2_batch_results_from_transcription_urls(
    *,
    mapped_results: Dict[str, Dict[str, Any]],
    timeout_ms: int,
) -> Dict[str, Dict[str, Any]]:
    hydrated: Dict[str, Dict[str, Any]] = {}
    fetch_timeout_ms = max(1000, min(int(timeout_ms), 15000))

    for file_url, item in mapped_results.items():
        if not isinstance(item, dict):
            continue

        candidate = dict(item)
        status = _status_upper(candidate.get("task_status"))
        transcript = clean_transcript_text(candidate.get("transcript_text"))
        transcription_url = normalize_text(candidate.get("transcription_url"))

        if not transcript and _is_success_status(status) and transcription_url:
            fetch_result = fetch_transcription_text_by_url(
                transcription_url=transcription_url,
                timeout_ms=fetch_timeout_ms,
            )
            fetched_text = clean_transcript_text(fetch_result.get("transcript_text"))
            candidate["transcription_fetch"] = {
                "ok": bool(fetch_result.get("ok")),
                "error_reason": fetch_result.get("error_reason"),
            }
            if fetched_text:
                transcript = fetched_text
                candidate["transcript_text"] = fetched_text
                candidate["summary_field_used"] = fetch_result.get("summary_field_used", "")
                candidate["segment_fallback_used"] = bool(fetch_result.get("segment_fallback_used"))
                candidate["canonical_text_source"] = fetch_result.get("canonical_text_source", "missing")
            elif not candidate.get("error_reason"):
                candidate["error_reason"] = fetch_result.get("error_reason") or "transcription_payload_empty"

        candidate["task_status"] = status
        candidate["transcription_url"] = transcription_url
        candidate["transcript_text"] = transcript
        candidate["ok"] = bool(candidate.get("ok") or transcript)
        hydrated[file_url] = candidate

    return hydrated


def build_u2_batch_progress(*, payload: Any, expected_total: int = 0) -> Dict[str, Any]:
    metrics_raw = extract_u2_task_metrics(payload)
    metrics = {str(key).strip().upper(): value for key, value in metrics_raw.items()} if isinstance(metrics_raw, dict) else {}

    metrics_total = _safe_int(metrics.get("TOTAL") or metrics.get("TASK_TOTAL") or metrics.get("COUNT"))
    metrics_succeeded = _safe_int(metrics.get("SUCCEEDED") or metrics.get("SUCCESS"))
    metrics_failed = (
        _safe_int(metrics.get("FAILED"))
        + _safe_int(metrics.get("FAILURE"))
        + _safe_int(metrics.get("ERROR"))
        + _safe_int(metrics.get("CANCELED"))
        + _safe_int(metrics.get("CANCELLED"))
    )
    metrics_completed = metrics_succeeded + metrics_failed

    provider_total = _safe_int(deep_find_first(payload, ["input_count", "total_count"]))
    provider_succeeded = _safe_int(deep_find_first(payload, ["succeeded_count"]))
    provider_failed = _safe_int(deep_find_first(payload, ["failed_count"]))
    provider_pending = max(0, _safe_int(deep_find_first(payload, ["pending_count"])))
    provider_completed = provider_succeeded + provider_failed
    provider_status = extract_platform_task_status(payload)

    mapped_results = map_u2_batch_results_by_file_url(payload)
    result_total = len(mapped_results)
    result_succeeded = 0
    result_failed = 0

    for item in mapped_results.values():
        status = _status_upper(item.get("task_status"))
        transcript = clean_transcript_text(item.get("transcript_text"))
        if _is_success_status(status) or transcript:
            result_succeeded += 1
        elif _is_failed_status(status):
            result_failed += 1

    result_completed = result_succeeded + result_failed

    target_total = metrics_total if metrics_total > 0 else (provider_total if provider_total > 0 else max(0, int(expected_total or 0)))
    complete_by_metrics = target_total > 0 and metrics_completed >= target_total
    complete_by_provider_counts = target_total > 0 and provider_pending == 0 and provider_completed >= target_total
    complete_by_provider_status = provider_pending == 0 and provider_status in {"SUCCEEDED", "PARTIAL_SUCCEEDED", "FAILED"}
    complete_by_results = target_total > 0 and result_completed >= target_total

    completion_basis = "pending"
    if complete_by_metrics:
        completion_basis = "task_metrics"
    elif complete_by_provider_counts or complete_by_provider_status:
        completion_basis = "platform_status"
    elif complete_by_results:
        completion_basis = "results"

    return {
        "expected_total": max(0, int(expected_total or 0)),
        "target_total": target_total,
        "metrics_total": metrics_total,
        "metrics_succeeded": metrics_succeeded,
        "metrics_failed": metrics_failed,
        "metrics_completed": metrics_completed,
        "provider_total": provider_total,
        "provider_succeeded": provider_succeeded,
        "provider_failed": provider_failed,
        "provider_pending": provider_pending,
        "platform_task_status": provider_status,
        "results_total": result_total,
        "results_succeeded": result_succeeded,
        "results_failed": result_failed,
        "results_completed": result_completed,
        "complete": bool(complete_by_metrics or complete_by_provider_counts or complete_by_provider_status or complete_by_results),
        "completion_basis": completion_basis,
        "metrics": metrics_raw if isinstance(metrics_raw, dict) else {},
    }


def poll_u2_task_core(
    *,
    base_url: str,
    token: str,
    timeout_ms: int,
    task_id: str,
    poll_interval_sec: float,
    max_polls: int,
    require_batch_complete: bool = False,
    expected_total: int = 0,
    pending_timeout_sec: Optional[int] = None,
    progress_callback: Optional[Callable[[Dict[str, Any]], None]] = None,
) -> Dict[str, Any]:
    trace = []
    last_request_id = None
    started_at = time.perf_counter()

    last_status = "UNKNOWN"
    last_payload: Any = {}
    last_batch_results: Dict[str, Dict[str, Any]] = {}
    last_metrics: Dict[str, Any] = {}
    last_progress: Dict[str, Any] = {
        "expected_total": max(0, int(expected_total or 0)),
        "target_total": 0,
        "complete": False,
        "completion_basis": "pending",
    }

    for attempt in range(1, max_polls + 1):
        response = call_json_api(
            base_url=base_url,
            path=f"/api/u2/v1/tasks/{task_id}",
            token=token,
            method="POST",
            timeout_ms=timeout_ms,
        )

        payload = response.get("data")
        status = extract_task_status(payload)
        platform_status = extract_platform_task_status(payload)
        pending_count = extract_pending_count(payload)
        last_request_id = response.get("request_id") or last_request_id

        metrics = extract_u2_task_metrics(payload)
        batch_results = map_u2_batch_results_by_file_url(payload)
        batch_progress = build_u2_batch_progress(payload=payload, expected_total=expected_total)

        effective_status = platform_status or status
        last_status = effective_status or last_status
        last_payload = payload
        last_batch_results = batch_results
        last_metrics = metrics if isinstance(metrics, dict) else {}
        last_progress = batch_progress

        trace.append(
            {
                "attempt": attempt,
                "elapsed_ms": int((time.perf_counter() - started_at) * 1000),
                "status_code": response.get("status_code"),
                "task_status": status,
                "platform_task_status": platform_status,
                "pending_count": pending_count,
                "request_id": response.get("request_id"),
                "error_reason": response.get("error_reason"),
                "batch_progress": batch_progress,
            }
        )

        if progress_callback is not None:
            try:
                progress_callback(
                    {
                        "attempt": attempt,
                        "elapsed_ms": int((time.perf_counter() - started_at) * 1000),
                        "task_id": task_id,
                        "task_status": status or "UNKNOWN",
                        "platform_task_status": platform_status or "UNKNOWN",
                        "pending_count": pending_count,
                        "request_id": response.get("request_id"),
                        "status_code": response.get("status_code"),
                        "ok": bool(response.get("ok")),
                        "error_reason": response.get("error_reason"),
                        "batch_progress": batch_progress,
                    }
                )
            except Exception:
                pass

        if not response.get("ok"):
            if attempt < max_polls:
                time.sleep(max(poll_interval_sec, 0.2))
                continue
            return {
                "ok": False,
                "task_id": task_id,
                "task_status": status or "UNKNOWN",
                "request_id": last_request_id,
                "error_reason": response.get("error_reason") or "u2_poll_http_error",
                "raw_task": payload,
                "task_metrics": last_metrics,
                "batch_results": batch_results,
                "batch_progress": batch_progress,
                "batch_complete": bool(batch_progress.get("complete")),
                "trace": trace,
            }

        status_terminal = is_terminal_status(status)
        platform_terminal = pending_count == 0 and platform_status in {"SUCCEEDED", "PARTIAL_SUCCEEDED", "FAILED"}
        task_complete = status_terminal or platform_terminal
        batch_complete = bool(batch_progress.get("complete")) if require_batch_complete else task_complete

        elapsed_sec = time.perf_counter() - started_at
        if pending_timeout_sec and elapsed_sec >= max(float(pending_timeout_sec), 1.0):
            timeout_reason = "u2_batch_pending_timeout" if require_batch_complete else "u2_pending_timeout"
            return {
                "ok": False,
                "task_id": task_id,
                "task_status": effective_status or last_status or "PENDING",
                "platform_task_status": platform_status,
                "pending_count": pending_count,
                "request_id": last_request_id,
                "error_reason": timeout_reason,
                "transcript_text": "",
                "raw_task": payload,
                "task_metrics": last_metrics,
                "batch_results": batch_results,
                "batch_progress": batch_progress,
                "batch_complete": bool(batch_complete),
                "trace": trace,
            }

        if require_batch_complete and not batch_complete:
            if attempt < max_polls:
                time.sleep(max(poll_interval_sec, 0.2))
                continue
            return {
                "ok": False,
                "task_id": task_id,
                "task_status": effective_status or "UNKNOWN",
                "request_id": last_request_id,
                "error_reason": "u2_batch_incomplete_timeout",
                "raw_task": payload,
                "task_metrics": last_metrics,
                "batch_results": batch_results,
                "batch_progress": batch_progress,
                "batch_complete": False,
                "trace": trace,
            }

        if task_complete or batch_complete:
            success_signal = (
                platform_status == "SUCCEEDED" and pending_count == 0
            ) or _is_success_status(status)
            transcript = extract_transcript_text(payload) if success_signal else ""
            return {
                "ok": bool(success_signal),
                "task_id": task_id,
                "task_status": effective_status or status,
                "platform_task_status": platform_status,
                "pending_count": pending_count,
                "request_id": last_request_id,
                "error_reason": None if success_signal else (None if batch_complete and require_batch_complete else "u2_task_failed"),
                "transcript_text": clean_transcript_text(transcript),
                "raw_task": payload,
                "task_metrics": last_metrics,
                "batch_results": batch_results,
                "batch_progress": batch_progress,
                "batch_complete": bool(batch_complete),
                "trace": trace,
            }

        time.sleep(max(poll_interval_sec, 0.2))

    timeout_reason = "u2_batch_incomplete_timeout" if require_batch_complete else "u2_poll_timeout"
    return {
        "ok": False,
        "task_id": task_id,
        "task_status": last_status or "TIMEOUT",
        "request_id": last_request_id,
        "error_reason": timeout_reason,
        "raw_task": last_payload,
        "task_metrics": last_metrics,
        "batch_results": last_batch_results,
        "batch_progress": last_progress,
        "batch_complete": bool(last_progress.get("complete")) if require_batch_complete else False,
        "trace": trace,
    }


def normalize_media_url(url: str) -> str:
    text = str(url or "").strip()
    if not text:
        return ""
    try:
        parsed = urlparse(text)
    except Exception:
        return text

    scheme = (parsed.scheme or "").lower()
    if scheme == "http":
        parsed = parsed._replace(scheme="https")
    return urlunparse(parsed)


def is_valid_u2_media_candidate(url: str) -> bool:
    lower = str(url or "").lower()
    if not (lower.startswith("http://") or lower.startswith("https://")):
        return False
    image_tokens = [".jpg", ".jpeg", ".png", ".webp", "imageview2", "imagemogr2", "redimage", "frame/"]
    if any(token in lower for token in image_tokens):
        return False
    media_tokens = [".mp4", ".m3u8", ".m4a", ".mp3", "video", "stream", "audio", "vod"]
    return any(token in lower for token in media_tokens)


def normalize_media_candidates(candidates: List[str]) -> List[str]:
    normalized: List[str] = []
    seen = set()
    for raw in candidates or []:
        url = normalize_media_url(raw)
        if not url or url in seen:
            continue
        seen.add(url)
        normalized.append(url)
    return normalized


def run_u2_asr_candidates_with_timeout_retry(
    *,
    base_url: str,
    token: str,
    timeout_ms: int,
    candidates: List[str],
    submit_max_retries: int,
    submit_backoff_ms: int,
    poll_interval_sec: float,
    max_polls: int,
    timeout_retry_enabled: bool = True,
    timeout_retry_max_retries: int = 3,
    pending_timeout_sec: int = DEFAULT_U2_PENDING_TIMEOUT_SEC,
    progress_callback: Optional[Callable[[Dict[str, Any]], None]] = None,
) -> Dict[str, Any]:
    normalized_candidates = normalize_media_candidates(candidates)
    attempts: List[Dict[str, Any]] = []

    final_bundle: Dict[str, Any] = {
        "submit_bundle": {},
        "poll_result": {"ok": False, "task_status": "UNKNOWN", "error_reason": "no_candidates"},
        "rounds": [],
        "timeout_retry": {"enabled": bool(timeout_retry_enabled), "configured_max_retries": max(0, min(3, int(timeout_retry_max_retries))), "triggered": False, "result": "not_triggered"},
    }
    chosen_url: Optional[str] = None

    for index, candidate in enumerate(normalized_candidates, start=1):
        valid = is_valid_u2_media_candidate(candidate)
        if not valid:
            attempts.append({
                "index": index,
                "candidate": candidate,
                "valid": False,
                "result": "skipped_non_media_candidate",
            })
            continue

        bundle = run_u2_asr_with_timeout_retry(
            base_url=base_url,
            token=token,
            timeout_ms=timeout_ms,
            video_url=candidate,
            submit_max_retries=submit_max_retries,
            submit_backoff_ms=submit_backoff_ms,
            poll_interval_sec=poll_interval_sec,
            max_polls=max_polls,
            timeout_retry_enabled=timeout_retry_enabled,
            timeout_retry_max_retries=timeout_retry_max_retries,
            pending_timeout_sec=pending_timeout_sec,
            progress_callback=progress_callback,
        )
        poll_result = bundle.get("poll_result", {})
        error_reason = str(poll_result.get("error_reason") or "")
        ok = bool(poll_result.get("ok"))

        attempts.append({
            "index": index,
            "candidate": candidate,
            "valid": True,
            "ok": ok,
            "error_reason": error_reason,
            "task_status": poll_result.get("task_status"),
            "u3_fallback": bundle.get("u3_fallback", {}),
        })

        final_bundle = bundle
        chosen_url = candidate
        if ok:
            break

        if (bundle.get("u3_fallback") or {}).get("triggered"):
            break

        if error_reason == "INVALID_SOURCE_URL":
            continue

    final_bundle["candidate_attempts"] = attempts
    final_bundle["chosen_candidate"] = chosen_url
    final_bundle["normalized_candidates"] = normalized_candidates
    return final_bundle


def run_u3_then_u2_asr_candidates_with_timeout_retry(
    *,
    base_url: str,
    token: str,
    timeout_ms: int,
    candidates: List[str],
    submit_max_retries: int,
    submit_backoff_ms: int,
    poll_interval_sec: float,
    max_polls: int,
    timeout_retry_enabled: bool = True,
    timeout_retry_max_retries: int = 3,
    pending_timeout_sec: int = DEFAULT_U2_PENDING_TIMEOUT_SEC,
    progress_callback: Optional[Callable[[Dict[str, Any]], None]] = None,
) -> Dict[str, Any]:
    normalized_candidates = normalize_media_candidates(candidates)
    attempts: List[Dict[str, Any]] = []

    final_bundle: Dict[str, Any] = {
        "submit_bundle": {},
        "poll_result": {"ok": False, "task_status": "UNKNOWN", "error_reason": "no_candidates"},
        "rounds": [],
        "timeout_retry": {
            "enabled": bool(timeout_retry_enabled),
            "configured_max_retries": max(0, min(3, int(timeout_retry_max_retries))),
            "triggered": False,
            "result": "not_triggered",
        },
        "u3_fallback": {
            "enabled": False,
            "triggered": False,
            "ok": False,
            "result": "not_triggered",
            "public_url": "",
            "trace": [],
        },
    }
    chosen_url: Optional[str] = None
    chosen_public_url: Optional[str] = None

    for index, candidate in enumerate(normalized_candidates, start=1):
        valid = is_valid_u2_media_candidate(candidate)
        if not valid:
            attempts.append(
                {
                    "index": index,
                    "candidate": candidate,
                    "valid": False,
                    "result": "skipped_non_media_candidate",
                }
            )
            continue

        u3_result = run_u3_public_url_fallback(
            base_url=base_url,
            token=token,
            timeout_ms=timeout_ms,
            source_url=candidate,
        )
        u3_bundle = {
            "enabled": True,
            "triggered": True,
            "ok": bool(u3_result.get("ok")),
            "result": "u3_completed" if u3_result.get("ok") else "u3_failed",
            "public_url": normalize_media_url(u3_result.get("public_url")),
            "request_id": u3_result.get("request_id"),
            "error_reason": u3_result.get("error_reason"),
            "trace": u3_result.get("trace", []),
        }

        attempts.append(
            {
                "index": index,
                "candidate": candidate,
                "valid": True,
                "u3_bridge": u3_bundle,
            }
        )

        if not u3_bundle.get("ok") or not u3_bundle.get("public_url"):
            final_bundle = {
                "submit_bundle": {},
                "poll_result": {
                    "ok": False,
                    "task_status": "UNKNOWN",
                    "error_reason": u3_bundle.get("error_reason") or "u3_bridge_failed",
                    "request_id": u3_bundle.get("request_id"),
                    "trace": list(u3_bundle.get("trace", [])),
                },
                "rounds": [],
                "timeout_retry": {
                    "enabled": bool(timeout_retry_enabled),
                    "configured_max_retries": max(0, min(3, int(timeout_retry_max_retries))),
                    "triggered": False,
                    "result": "not_triggered",
                },
                "u3_fallback": {
                    "enabled": False,
                    "triggered": False,
                    "ok": False,
                    "result": "not_triggered",
                    "public_url": "",
                    "trace": [],
                },
                "u3_bridge": u3_bundle,
            }
            continue

        bundle = run_u2_asr_with_timeout_retry(
            base_url=base_url,
            token=token,
            timeout_ms=timeout_ms,
            video_url=str(u3_bundle.get("public_url")),
            submit_max_retries=submit_max_retries,
            submit_backoff_ms=submit_backoff_ms,
            poll_interval_sec=poll_interval_sec,
            max_polls=max_polls,
            timeout_retry_enabled=timeout_retry_enabled,
            timeout_retry_max_retries=timeout_retry_max_retries,
            pending_timeout_sec=pending_timeout_sec,
            u3_fallback_enabled=False,
            progress_callback=progress_callback,
        )
        poll_result = bundle.get("poll_result", {})
        error_reason = str(poll_result.get("error_reason") or "")
        ok = bool(poll_result.get("ok"))

        attempts[-1].update(
            {
                "ok": ok,
                "error_reason": error_reason,
                "task_status": poll_result.get("task_status"),
                "u2_public_url": u3_bundle.get("public_url"),
            }
        )

        final_bundle = dict(bundle)
        final_bundle["u3_bridge"] = u3_bundle
        chosen_url = candidate
        chosen_public_url = str(u3_bundle.get("public_url") or "")
        if ok:
            break
        if error_reason == "INVALID_SOURCE_URL":
            continue
        break

    final_bundle["candidate_attempts"] = attempts
    final_bundle["chosen_candidate"] = chosen_url
    final_bundle["chosen_public_url"] = chosen_public_url
    final_bundle["normalized_candidates"] = normalized_candidates
    return final_bundle


def run_u2_asr_batch_with_timeout_retry(
    *,
    base_url: str,
    token: str,
    timeout_ms: int,
    file_urls: List[str],
    submit_max_retries: int,
    submit_backoff_ms: int,
    poll_interval_sec: float,
    max_polls: int,
    timeout_retry_enabled: bool = True,
    timeout_retry_max_retries: int = 3,
    pending_timeout_sec: int = DEFAULT_U2_PENDING_TIMEOUT_SEC,
    progress_callback: Optional[Callable[[Dict[str, Any]], None]] = None,
) -> Dict[str, Any]:
    normalized_urls = normalize_media_candidates(file_urls)
    limited_urls = normalized_urls[:U2_BATCH_SUBMIT_HARD_LIMIT]

    conservative_retries = max(0, min(3, int(timeout_retry_max_retries)))
    retries = conservative_retries if timeout_retry_enabled else 0
    max_rounds = 1 + retries

    rounds: List[Dict[str, Any]] = []
    final_submit_bundle: Dict[str, Any] = {}
    final_poll_result: Dict[str, Any] = {
        "ok": False,
        "task_status": "UNKNOWN",
        "error_reason": "u2_submit_failed_or_missing_task_id",
        "task_metrics": {},
        "batch_results": {},
    }
    timeout_retry_triggered = False
    timeout_retry_result = "not_triggered"

    if not limited_urls:
        return {
            "submit_bundle": {
                "submit_response": {"ok": False, "error_reason": "no_valid_file_urls"},
                "task_id": None,
                "retry_chain": [],
                "final_submit_status": "failed_no_valid_file_urls",
                "file_urls": [],
            },
            "poll_result": {
                "ok": False,
                "task_status": "UNKNOWN",
                "error_reason": "no_valid_file_urls",
                "task_metrics": {},
                "batch_results": {},
            },
            "rounds": [],
            "timeout_retry": {
                "enabled": bool(timeout_retry_enabled),
                "configured_max_retries": conservative_retries,
                "triggered": False,
                "result": "not_triggered",
            },
            "normalized_file_urls": [],
            "mapped_results": {},
            "result_items": [],
            "task_metrics": {},
        }

    for round_index in range(1, max_rounds + 1):
        submit_started_at = time.perf_counter()
        submit_bundle = submit_u2_asr_batch_with_retry(
            base_url=base_url,
            token=token,
            timeout_ms=timeout_ms,
            file_urls=limited_urls,
            max_retries=submit_max_retries,
            backoff_ms=submit_backoff_ms,
            progress_callback=progress_callback,
        )
        submit_duration_ms = int((time.perf_counter() - submit_started_at) * 1000)
        submit_response = submit_bundle.get("submit_response", {})
        task_id = submit_bundle.get("task_id")

        poll_result: Dict[str, Any]
        poll_duration_ms = 0
        if submit_response.get("ok") and task_id:
            poll_started_at = time.perf_counter()
            poll_result = poll_u2_task_core(
                base_url=base_url,
                token=token,
                timeout_ms=timeout_ms,
                task_id=str(task_id),
                poll_interval_sec=poll_interval_sec,
                max_polls=max_polls,
                require_batch_complete=True,
                expected_total=len(limited_urls),
                pending_timeout_sec=pending_timeout_sec,
                progress_callback=progress_callback,
            )
            poll_duration_ms = int((time.perf_counter() - poll_started_at) * 1000)
        else:
            poll_result = {
                "ok": False,
                "task_id": task_id,
                "task_status": "UNKNOWN",
                "request_id": submit_response.get("request_id"),
                "error_reason": submit_response.get("error_reason") or "u2_submit_failed_or_missing_task_id",
                "task_metrics": {},
                "batch_results": {},
                "batch_progress": {
                    "expected_total": len(limited_urls),
                    "target_total": len(limited_urls),
                    "complete": False,
                    "completion_basis": "pending",
                },
                "batch_complete": False,
                "trace": [],
            }

        rounds.append(
            {
                "round": round_index,
                "submit": {
                    "task_id": task_id,
                    "final_submit_status": submit_bundle.get("final_submit_status"),
                    "request_id": submit_response.get("request_id"),
                    "status_code": submit_response.get("status_code"),
                    "ok": submit_response.get("ok"),
                    "error_reason": submit_response.get("error_reason"),
                    "retry_chain": submit_bundle.get("retry_chain", []),
                    "file_url_count": len(limited_urls),
                    "duration_ms": submit_duration_ms,
                },
                "poll": {
                    "task_id": poll_result.get("task_id") or task_id,
                    "task_status": poll_result.get("task_status"),
                    "request_id": poll_result.get("request_id"),
                    "ok": poll_result.get("ok"),
                    "error_reason": poll_result.get("error_reason"),
                    "attempts": len(poll_result.get("trace", [])),
                    "task_metrics": poll_result.get("task_metrics", {}),
                    "batch_complete": bool(poll_result.get("batch_complete")),
                    "batch_progress": poll_result.get("batch_progress", {}),
                    "duration_ms": poll_duration_ms,
                },
            }
        )

        final_submit_bundle = submit_bundle
        final_poll_result = poll_result

        if poll_result.get("error_reason") in {"u2_poll_timeout", "u2_batch_incomplete_timeout", "u2_batch_pending_timeout"} and round_index < max_rounds:
            timeout_retry_triggered = True
            timeout_retry_result = "retrying"
            continue

        break

    if final_poll_result.get("ok"):
        timeout_retry_result = "retry_succeeded" if timeout_retry_triggered else "not_needed"
    elif final_poll_result.get("error_reason") in {"u2_poll_timeout", "u2_batch_incomplete_timeout", "u2_batch_pending_timeout"}:
        timeout_retry_result = "retry_timeout_exhausted" if timeout_retry_triggered else "timeout_no_retry"
    elif timeout_retry_triggered:
        timeout_retry_result = "retry_failed_non_timeout"
    else:
        timeout_retry_result = "not_triggered"

    raw_task_payload = final_poll_result.get("raw_task")
    mapped_results = map_u2_batch_results_by_file_url(raw_task_payload)

    index_mapped = map_u2_batch_results_by_item_index(raw_task_payload)
    for item_index, item in index_mapped.items():
        if item_index < 0 or item_index >= len(limited_urls):
            continue
        file_url = normalize_media_url(limited_urls[item_index])
        if not file_url:
            continue

        candidate = {
            "file_url": file_url,
            "transcript_text": clean_transcript_text(item.get("transcript_text")),
            "task_status": _status_upper(item.get("task_status")),
            "error_reason": str(item.get("error_reason") or "").strip(),
            "transcription_url": normalize_text(item.get("transcription_url")),
            "ok": bool(item.get("ok")),
        }

        existing = mapped_results.get(file_url)
        if existing is None:
            mapped_results[file_url] = candidate
        # When the provider returns file_url, treat it as the source of truth.
        # item_index remains a fallback only for older payloads without file_url.

    mapped_results = hydrate_u2_batch_results_from_transcription_urls(
        mapped_results=mapped_results,
        timeout_ms=timeout_ms,
    )
    result_items = list(mapped_results.values())

    return {
        "submit_bundle": final_submit_bundle,
        "poll_result": final_poll_result,
        "rounds": rounds,
        "timeout_retry": {
            "enabled": bool(timeout_retry_enabled),
            "configured_max_retries": conservative_retries,
            "triggered": timeout_retry_triggered,
            "result": timeout_retry_result,
        },
        "normalized_file_urls": limited_urls,
        "mapped_results": mapped_results,
        "result_items": result_items,
        "task_metrics": final_poll_result.get("task_metrics") if isinstance(final_poll_result.get("task_metrics"), dict) else extract_u2_task_metrics(raw_task_payload),
        "batch_progress": final_poll_result.get("batch_progress") if isinstance(final_poll_result.get("batch_progress"), dict) else build_u2_batch_progress(payload=raw_task_payload, expected_total=len(limited_urls)),
        "batch_complete": bool(final_poll_result.get("batch_complete")),
        "submit_duration_ms": _safe_int((rounds[-1].get("submit") if rounds else {}).get("duration_ms")),
        "poll_duration_ms": _safe_int((rounds[-1].get("poll") if rounds else {}).get("duration_ms")),
    }


def run_u2_asr_with_timeout_retry(
    *,
    base_url: str,
    token: str,
    timeout_ms: int,
    video_url: str,
    submit_max_retries: int,
    submit_backoff_ms: int,
    poll_interval_sec: float,
    max_polls: int,
    timeout_retry_enabled: bool = True,
    timeout_retry_max_retries: int = 3,
    pending_timeout_sec: int = DEFAULT_U2_PENDING_TIMEOUT_SEC,
    u3_fallback_enabled: bool = True,
    progress_callback: Optional[Callable[[Dict[str, Any]], None]] = None,
) -> Dict[str, Any]:
    video_url = normalize_media_url(video_url)
    conservative_retries = max(0, min(3, int(timeout_retry_max_retries)))
    retries = conservative_retries if timeout_retry_enabled else 0
    max_rounds = 1 + retries

    rounds: List[Dict[str, Any]] = []
    final_submit_bundle: Dict[str, Any] = {}
    final_poll_result: Dict[str, Any] = {
        "ok": False,
        "task_status": "UNKNOWN",
        "error_reason": "u2_submit_failed_or_missing_task_id",
    }
    timeout_retry_triggered = False
    timeout_retry_result = "not_triggered"
    u3_fallback_bundle: Dict[str, Any] = {
        "enabled": bool(u3_fallback_enabled),
        "triggered": False,
        "ok": False,
        "result": "not_triggered",
        "public_url": "",
        "trace": [],
    }

    for round_index in range(1, max_rounds + 1):
        submit_started_at = time.perf_counter()
        submit_bundle = submit_u2_asr_with_retry(
            base_url=base_url,
            token=token,
            timeout_ms=timeout_ms,
            video_url=video_url,
            max_retries=submit_max_retries,
            backoff_ms=submit_backoff_ms,
            progress_callback=progress_callback,
        )
        submit_duration_ms = int((time.perf_counter() - submit_started_at) * 1000)
        submit_response = submit_bundle.get("submit_response", {})
        task_id = submit_bundle.get("task_id")

        poll_result: Dict[str, Any]
        poll_duration_ms = 0
        if submit_response.get("ok") and task_id:
            poll_started_at = time.perf_counter()
            poll_result = poll_u2_task_core(
                base_url=base_url,
                token=token,
                timeout_ms=timeout_ms,
                task_id=str(task_id),
                poll_interval_sec=poll_interval_sec,
                max_polls=max_polls,
                pending_timeout_sec=pending_timeout_sec,
                progress_callback=progress_callback,
            )
            poll_duration_ms = int((time.perf_counter() - poll_started_at) * 1000)
        else:
            poll_result = {
                "ok": False,
                "task_id": task_id,
                "task_status": "UNKNOWN",
                "request_id": submit_response.get("request_id"),
                "error_reason": submit_response.get("error_reason") or "u2_submit_failed_or_missing_task_id",
                "trace": [],
            }

        rounds.append(
            {
                "round": round_index,
                "submit": {
                    "task_id": task_id,
                    "final_submit_status": submit_bundle.get("final_submit_status"),
                    "request_id": submit_response.get("request_id"),
                    "status_code": submit_response.get("status_code"),
                    "ok": submit_response.get("ok"),
                    "error_reason": submit_response.get("error_reason"),
                    "retry_chain": submit_bundle.get("retry_chain", []),
                    "duration_ms": submit_duration_ms,
                },
                "poll": {
                    "task_id": poll_result.get("task_id") or task_id,
                    "task_status": poll_result.get("task_status"),
                    "request_id": poll_result.get("request_id"),
                    "ok": poll_result.get("ok"),
                    "error_reason": poll_result.get("error_reason"),
                    "attempts": len(poll_result.get("trace", [])),
                    "duration_ms": poll_duration_ms,
                },
            }
        )

        final_submit_bundle = submit_bundle
        final_poll_result = poll_result

        if (
            u3_fallback_enabled
            and poll_result.get("error_reason") in {"u2_pending_timeout", "u2_poll_timeout"}
        ):
            u3_fallback_bundle["triggered"] = True
            u3_result = run_u3_public_url_fallback(
                base_url=base_url,
                token=token,
                timeout_ms=timeout_ms,
                source_url=video_url,
            )
            u3_fallback_bundle.update(
                {
                    "ok": bool(u3_result.get("ok")),
                    "result": "u3_completed" if u3_result.get("ok") else "u3_failed",
                    "public_url": u3_result.get("public_url") or "",
                    "request_id": u3_result.get("request_id"),
                    "error_reason": u3_result.get("error_reason"),
                    "trace": u3_result.get("trace", []),
                }
            )
            if u3_result.get("ok") and u3_result.get("public_url"):
                retry_bundle = run_u2_asr_with_timeout_retry(
                    base_url=base_url,
                    token=token,
                    timeout_ms=timeout_ms,
                    video_url=str(u3_result.get("public_url")),
                    submit_max_retries=submit_max_retries,
                    submit_backoff_ms=submit_backoff_ms,
                    poll_interval_sec=poll_interval_sec,
                    max_polls=max_polls,
                    timeout_retry_enabled=timeout_retry_enabled,
                    timeout_retry_max_retries=timeout_retry_max_retries,
                    pending_timeout_sec=pending_timeout_sec,
                    u3_fallback_enabled=False,
                    progress_callback=progress_callback,
                )
                retry_bundle["u3_fallback"] = u3_fallback_bundle
                retry_bundle["original_source_url"] = video_url
                return retry_bundle
            final_poll_result = {
                "ok": False,
                "task_id": poll_result.get("task_id") or task_id,
                "task_status": poll_result.get("task_status") or "UNKNOWN",
                "request_id": u3_result.get("request_id") or poll_result.get("request_id"),
                "error_reason": u3_result.get("error_reason") or "u3_fallback_failed",
                "trace": list(poll_result.get("trace", [])) + list(u3_result.get("trace", [])),
            }
            break

        if poll_result.get("error_reason") == "u2_poll_timeout" and round_index < max_rounds:
            timeout_retry_triggered = True
            timeout_retry_result = "retrying"
            continue

        break

    if final_poll_result.get("ok"):
        timeout_retry_result = "retry_succeeded" if timeout_retry_triggered else "not_needed"
    elif final_poll_result.get("error_reason") == "u2_poll_timeout":
        timeout_retry_result = "retry_timeout_exhausted" if timeout_retry_triggered else "timeout_no_retry"
    elif timeout_retry_triggered:
        timeout_retry_result = "retry_failed_non_timeout"
    else:
        timeout_retry_result = "not_triggered"

    return {
        "submit_bundle": final_submit_bundle,
        "poll_result": final_poll_result,
        "rounds": rounds,
        "timeout_retry": {
            "enabled": bool(timeout_retry_enabled),
            "configured_max_retries": conservative_retries,
            "triggered": timeout_retry_triggered,
            "result": timeout_retry_result,
        },
        "u3_fallback": u3_fallback_bundle,
        "submit_duration_ms": _safe_int((rounds[-1].get("submit") if rounds else {}).get("duration_ms")),
        "poll_duration_ms": _safe_int((rounds[-1].get("poll") if rounds else {}).get("duration_ms")),
    }
