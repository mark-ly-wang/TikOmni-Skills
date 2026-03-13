#!/usr/bin/env python3
"""Author-home ASR enrichment (batch + checkpoint + idempotent dedupe)."""

from __future__ import annotations

import json
import re
import urllib.request
from typing import Any, Dict, List, Optional, Tuple

from scripts.core.progress_report import ProgressReporter
from scripts.core.tikomni_common import normalize_text
from scripts.core.asr_pipeline import (
    clamp_u2_batch_submit_size,
    derive_asr_clean_text,
    normalize_media_url,
    run_u2_asr_batch_with_timeout_retry,
    run_u2_asr_candidates_with_timeout_retry,
)
from scripts.core.u3_fallback import run_u3_public_url_fallback
from scripts.pipelines.douyin_video_type_matrix import normalize_douyin_video_type

DEFAULT_BATCH_SUBMIT_SIZE = 50
MAX_BATCH_SUBMIT_SIZE = 100
XHS_U3_U2_BATCH_SIZE = 20
U2_GATE_MIN_DURATION_MS = 13000
U2_GATE_MAX_DURATION_MS = 1800000
U2_GATE_RULE = "is_video && 13000<duration_ms<=1800000 && video_download_url_present"


def _to_int_or_none(value: Any) -> Optional[int]:
    try:
        if isinstance(value, bool):
            return int(value)
        if isinstance(value, (int, float)):
            parsed = int(value)
            return parsed if parsed > 0 else None
        text = normalize_text(value)
        if not text:
            return None
        parsed = int(float(text.replace(",", "")))
        return parsed if parsed > 0 else None
    except Exception:
        return None


def _to_bool(value: Any) -> Optional[bool]:
    if isinstance(value, bool):
        return value
    if isinstance(value, (int, float)):
        return bool(int(value))
    text = normalize_text(value).lower()
    if not text:
        return None
    if text in {"1", "true", "yes", "y", "video"}:
        return True
    if text in {"0", "false", "no", "n", "image", "photo", "note"}:
        return False
    return None


def _resolve_is_video(work: Dict[str, Any], *, platform: str) -> bool:
    explicit = _to_bool(work.get("is_video"))
    if explicit is not None:
        return explicit

    work_modality = normalize_text(work.get("work_modality")).lower()
    if work_modality == "video":
        return True
    if work_modality == "text":
        return False

    content_type = normalize_text(work.get("content_type")).lower()
    if content_type in {"video", "mixed", "mix", "video_note", "note_video"}:
        return True
    if content_type in {"image", "photo", "album", "note", "text"}:
        return False

    if platform == "douyin":
        raw_ref = work.get("raw_ref") if isinstance(work.get("raw_ref"), dict) else {}
        raw_item = raw_ref.get("raw_item") if isinstance(raw_ref.get("raw_item"), dict) else {}
        if raw_item:
            return bool(normalize_douyin_video_type(raw_item).get("is_video"))
        return False

    raw_ref = work.get("raw_ref") if isinstance(work.get("raw_ref"), dict) else {}
    xhs_type_hint = normalize_text(raw_ref.get("type") or raw_ref.get("note_type")).lower()
    if xhs_type_hint in {"video", "0", "mixed", "mix", "video_note", "note_video"}:
        return True
    if xhs_type_hint in {"normal", "image", "1", "note", "photo", "text", "album"}:
        return False

    return False


def _evaluate_u2_gate(work: Dict[str, Any], *, platform: str) -> Dict[str, Any]:
    is_video = _resolve_is_video(work, platform=platform)
    duration_ms = _to_int_or_none(work.get("duration_ms"))
    video_download_url = normalize_text(work.get("video_download_url") or work.get("video_down_url"))

    if not is_video:
        gate_reason = "skip:not_video"
    elif duration_ms is None:
        gate_reason = "skip:duration_missing"
    elif duration_ms <= U2_GATE_MIN_DURATION_MS:
        gate_reason = "skip:duration_too_short"
    elif duration_ms > U2_GATE_MAX_DURATION_MS:
        gate_reason = "skip:duration_too_long"
    elif not video_download_url:
        gate_reason = "skip:video_download_url_missing"
    else:
        gate_reason = "pass"

    return {
        "can_u2": gate_reason == "pass",
        "gate_reason": gate_reason,
        "is_video": is_video,
        "duration_ms": duration_ms,
        "video_download_url": video_download_url,
        "video_download_url_present": bool(video_download_url),
    }


def _clean_text(text: Any) -> str:
    if text is None:
        return ""
    lines = [normalize_text(line) for line in str(text).splitlines()]
    lines = [line for line in lines if line]
    return "\n".join(lines).strip()


def _build_transcript_result(
    raw_text: Any,
    *,
    subtitle_source: str,
    asr_source: str,
) -> Dict[str, Any]:
    transcript = _clean_text(raw_text)
    asr_clean = derive_asr_clean_text(transcript)
    primary_text = asr_clean or transcript
    return {
        "subtitle_raw": transcript,
        "subtitle_source": subtitle_source,
        "asr_raw": transcript,
        "asr_clean": asr_clean,
        "primary_text": primary_text,
        "primary_text_source": "asr_clean",
        "analysis_eligibility": "eligible" if transcript else "incomplete",
        "analysis_exclusion_reason": "" if transcript else "video_asr_unavailable",
        "asr_status": "success" if transcript else "failed",
        "asr_error_reason": "",
        "asr_source": asr_source,
    }


def _subtitle_text_from_raw(raw: str) -> str:
    content = (raw or "").strip()
    if not content:
        return ""

    try:
        payload = json.loads(content)
        candidates: List[str] = []
        if isinstance(payload, list):
            for item in payload:
                if isinstance(item, dict):
                    for key in ("text", "content", "sentence", "line"):
                        value = normalize_text(item.get(key))
                        if value:
                            candidates.append(value)
        elif isinstance(payload, dict):
            stack = [payload]
            while stack:
                node = stack.pop(0)
                if isinstance(node, dict):
                    for key, value in node.items():
                        if key in {"text", "content", "sentence", "line"} and isinstance(value, str):
                            cleaned = normalize_text(value)
                            if cleaned:
                                candidates.append(cleaned)
                        elif isinstance(value, (dict, list)):
                            stack.append(value)
                elif isinstance(node, list):
                    stack.extend(node)
        if candidates:
            return "\n".join(list(dict.fromkeys(candidates))).strip()
    except Exception:
        pass

    lines: List[str] = []
    for line in content.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if re.match(r"^\d+$", stripped):
            continue
        if re.match(r"^\d{1,2}:\d{2}(?::\d{2})?(?:[\.,]\d{1,3})?\s*-->\s*\d{1,2}:\d{2}(?::\d{2})?(?:[\.,]\d{1,3})?$", stripped):
            continue
        lines.append(stripped)
    return "\n".join(lines).strip()


def _fetch_subtitle_text(urls: List[str], timeout_ms: int) -> str:
    for url in urls:
        text = normalize_text(url)
        if not text:
            continue
        try:
            req = urllib.request.Request(text, method="GET")
            with urllib.request.urlopen(req, timeout=max(timeout_ms / 1000.0, 1.0)) as response:
                raw = response.read().decode("utf-8", errors="replace")
            parsed = _subtitle_text_from_raw(raw)
            if parsed:
                return parsed
        except Exception:
            continue
    return ""


def _invalid_subtitle_reason(text: str) -> Optional[str]:
    clean = _clean_text(text)
    if not clean:
        return "subtitle_empty"

    if len(clean) < 20:
        return "subtitle_too_short"

    normalized = clean.replace("\n", "")
    total_chars = len(normalized)
    if total_chars <= 0:
        return "subtitle_empty"

    allowed_punct = " ，。！？；：“”‘’（）()《》、,.!?;:-_/\\\"'\t"
    invalid_chars = 0
    for char in normalized:
        if char.isalnum() or "\u4e00" <= char <= "\u9fff" or char in allowed_punct:
            continue
        invalid_chars += 1

    if invalid_chars / max(total_chars, 1) > 0.35:
        return "subtitle_garbled"

    timeline_like_lines = 0
    non_timeline_lines = 0
    for line in clean.splitlines():
        line = line.strip()
        if not line:
            continue
        if re.match(r"^\d{1,2}:\d{2}(?::\d{2})?(?:[\.,]\d{1,3})?\s*-->\s*\d{1,2}:\d{2}(?::\d{2})?(?:[\.,]\d{1,3})?$", line):
            timeline_like_lines += 1
        elif re.match(r"^[\d:\-\.,\s>]+$", line):
            timeline_like_lines += 1
        else:
            non_timeline_lines += 1

    if timeline_like_lines > 0 and non_timeline_lines == 0:
        return "subtitle_timeline_only"

    lines = [line for line in clean.splitlines() if line.strip()]
    if len(lines) >= 4 and len(set(lines)) <= 1:
        return "subtitle_noise_repeated"

    return None


def _run_u2_for_work(
    *,
    platform: str,
    work: Dict[str, Any],
    base_url: str,
    token: str,
    timeout_ms: int,
    poll_interval_sec: float,
    max_polls: int,
    submit_max_retries: int,
    submit_backoff_ms: int,
    timeout_retry_enabled: bool,
    timeout_retry_max_retries: int,
) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    gate = _evaluate_u2_gate(work, platform=platform)
    if not gate.get("can_u2"):
        gate_reason = normalize_text(gate.get("gate_reason")) or "skip:unknown"
        fallback_result = _video_caption_fallback_result(work, gate_reason) if gate.get("is_video") else _fallback_none_result(gate_reason)
        return fallback_result, {
            "step": "author_home.asr.u2_gate",
            "platform_work_id": work.get("platform_work_id"),
            "ok": False,
            "can_u2": False,
            "gate_reason": gate_reason,
            "rule": U2_GATE_RULE,
            "is_video": gate.get("is_video"),
            "duration_ms": gate.get("duration_ms"),
            "video_download_url_present": gate.get("video_download_url_present"),
        }

    video_download_url = normalize_text(gate.get("video_download_url"))

    bundle = run_u2_asr_candidates_with_timeout_retry(
        base_url=base_url,
        token=token,
        timeout_ms=timeout_ms,
        candidates=[video_download_url],
        submit_max_retries=submit_max_retries,
        submit_backoff_ms=submit_backoff_ms,
        poll_interval_sec=poll_interval_sec,
        max_polls=max_polls,
        timeout_retry_enabled=timeout_retry_enabled,
        timeout_retry_max_retries=timeout_retry_max_retries,
    )
    poll_result = bundle.get("poll_result", {}) if isinstance(bundle.get("poll_result"), dict) else {}
    transcript = _clean_text(poll_result.get("transcript_text"))

    trace = {
        "step": "author_home.asr.u2",
        "platform_work_id": work.get("platform_work_id"),
        "ok": bool(poll_result.get("ok") and transcript),
        "task_status": poll_result.get("task_status"),
        "error_reason": poll_result.get("error_reason"),
        "selected_video_url": bundle.get("chosen_candidate") or video_download_url,
        "rounds": bundle.get("rounds", []),
        "candidate_attempts": bundle.get("candidate_attempts", []),
        "timeout_retry": bundle.get("timeout_retry", {}),
        "gate_reason": "pass",
        "rule": U2_GATE_RULE,
    }

    if transcript:
        return _build_transcript_result(
            transcript,
            subtitle_source="external_asr",
            asr_source="external_asr",
        ), trace

    return _video_caption_fallback_result(work, normalize_text(poll_result.get("error_reason")) or "u2_failed"), trace


def _iter_xhs_interface_text_candidates(work: Dict[str, Any]) -> List[Tuple[str, str]]:
    raw_ref = work.get("raw_ref") if isinstance(work.get("raw_ref"), dict) else {}
    raw_item = raw_ref.get("raw_item") if isinstance(raw_ref.get("raw_item"), dict) else {}

    candidates: List[Tuple[str, str]] = []

    def _append(source: str, value: Any) -> None:
        clean = _clean_text(value)
        if clean:
            candidates.append((source, clean))

    # Strict subtitle separation: only subtitle/transcript-like fields are allowed here.
    _append("work.subtitle_raw", work.get("subtitle_raw"))
    _append("work.asr_raw", work.get("asr_raw"))
    _append("raw_ref.subtitle_inline", raw_ref.get("subtitle_inline"))

    for key in (
        "subtitle_text",
        "subtitle",
        "subtitles",
        "captions",
        "caption_text",
        "transcript",
        "transcript_text",
        "subtitle_content",
        "subtitle_list",
        "subtitleList",
        "srt",
        "vtt",
    ):
        _append(f"raw_item.{key}", raw_item.get(key))

    deduped: List[Tuple[str, str]] = []
    seen = set()
    for source, text in candidates:
        if text in seen:
            continue
        seen.add(text)
        deduped.append((source, text))
    return deduped


def _classify_xhs_subtitle_failure(*, work: Dict[str, Any], interface_candidates: List[Tuple[str, str]], subtitle_urls: List[str], invalid_reason: str) -> str:
    raw_ref = work.get("raw_ref") if isinstance(work.get("raw_ref"), dict) else {}
    has_subtitle_signal = any(
        normalize_text(raw_ref.get(key))
        for key in (
            "subtitle_inline",
            "subtitle_text",
            "subtitle_raw",
            "caption_text",
            "transcript_text",
        )
    )
    if interface_candidates:
        return "subtitle_content_invalid"
    if subtitle_urls:
        return "subtitle_url_unavailable"
    if has_subtitle_signal:
        return "subtitle_structure_unrecognized"
    if invalid_reason == "subtitle_empty":
        return "subtitle_missing"
    return "subtitle_content_invalid"


def _resolve_xhs_subtitle(work: Dict[str, Any], timeout_ms: int) -> Dict[str, Any]:
    raw_ref = work.get("raw_ref") if isinstance(work.get("raw_ref"), dict) else {}
    subtitle_urls = raw_ref.get("subtitle_urls") if isinstance(raw_ref.get("subtitle_urls"), list) else []
    subtitle_urls = [normalize_text(item) for item in subtitle_urls if normalize_text(item)]
    interface_candidates = _iter_xhs_interface_text_candidates(work)
    invalid_reasons: List[Dict[str, str]] = []

    for source, candidate in interface_candidates:
        invalid_reason = _invalid_subtitle_reason(candidate)
        if invalid_reason is None:
            return {
                "text": candidate,
                "subtitle_source": "interface",
                "subtitle_field": source,
                "subtitle_urls": subtitle_urls,
                "invalid_reasons": invalid_reasons,
                "failure_category": "",
            }
        invalid_reasons.append({"field": source, "reason": invalid_reason})

    subtitle_text = _fetch_subtitle_text(subtitle_urls, timeout_ms)
    if subtitle_text:
        invalid_reason = _invalid_subtitle_reason(subtitle_text)
        if invalid_reason is None:
            return {
                "text": subtitle_text,
                "subtitle_source": "subtitle_url",
                "subtitle_field": "raw_ref.subtitle_urls",
                "subtitle_urls": subtitle_urls,
                "invalid_reasons": invalid_reasons,
                "failure_category": "",
            }
        invalid_reasons.append({"field": "raw_ref.subtitle_urls", "reason": invalid_reason})

    return {
        "text": "",
        "subtitle_source": "missing",
        "subtitle_field": "",
        "subtitle_urls": subtitle_urls,
        "invalid_reasons": invalid_reasons,
        "failure_category": _classify_xhs_subtitle_failure(
            work=work,
            interface_candidates=interface_candidates,
            subtitle_urls=subtitle_urls,
            invalid_reason="subtitle_empty",
        ),
    }


def _dedupe_works_by_platform_id(works: List[Dict[str, Any]]) -> Tuple[List[Dict[str, Any]], int]:
    deduped: List[Dict[str, Any]] = []
    seen = set()
    duplicates = 0

    for work in works:
        if not isinstance(work, dict):
            continue
        platform_work_id = normalize_text(work.get("platform_work_id"))
        dedupe_key = platform_work_id or f"anonymous-{len(deduped)}"
        if dedupe_key in seen:
            duplicates += 1
            continue
        seen.add(dedupe_key)
        deduped.append(work)

    return deduped, duplicates


def _fallback_none_result(reason: str) -> Dict[str, Any]:
    return {
        "subtitle_raw": "",
        "subtitle_source": "missing",
        "asr_raw": "",
        "asr_clean": "",
        "primary_text": "",
        "primary_text_source": "asr_clean",
        "analysis_eligibility": "incomplete",
        "analysis_exclusion_reason": normalize_text(reason) or "video_asr_unavailable",
        "asr_status": "failed",
        "asr_error_reason": normalize_text(reason) or "asr_failed",
        "asr_source": "fallback_none",
    }


def _video_caption_fallback_result(work: Dict[str, Any], reason: str) -> Dict[str, Any]:
    caption_raw = normalize_text(work.get("caption_raw"))
    return {
        "subtitle_raw": "",
        "subtitle_source": "missing",
        "asr_raw": "",
        "asr_clean": "",
        "primary_text": caption_raw,
        "primary_text_source": "caption_raw" if caption_raw else "missing",
        "analysis_eligibility": "eligible" if caption_raw else "incomplete",
        "analysis_exclusion_reason": "" if caption_raw else (normalize_text(reason) or "video_asr_unavailable"),
        "asr_status": "failed",
        "asr_error_reason": normalize_text(reason) or "asr_failed",
        "asr_source": "fallback_none",
    }


def _run_xhs_u3_then_u2_batch_for_entries(
    *,
    batch_id: str,
    entries: List[Dict[str, Any]],
    base_url: str,
    token: str,
    timeout_ms: int,
    poll_interval_sec: float,
    max_polls: int,
    submit_max_retries: int,
    submit_backoff_ms: int,
    timeout_retry_enabled: bool,
    timeout_retry_max_retries: int,
) -> Dict[str, Any]:
    trace: List[Dict[str, Any]] = []
    u2_entries: List[Dict[str, Any]] = []
    u3_failed_count = 0

    for entry in entries:
        work = entry.get("work")
        if not isinstance(work, dict):
            continue

        source_url = normalize_media_url(entry.get("video_download_url") or work.get("video_download_url") or work.get("video_down_url"))
        work_id = normalize_text(entry.get("work_id") or work.get("platform_work_id"))
        subtitle_invalid = normalize_text(entry.get("subtitle_invalid")) or "subtitle_missing"

        if not source_url:
            work.update(_video_caption_fallback_result(work, "skip:video_download_url_missing"))
            trace.append(
                {
                    "step": "author_home.asr.xhs_u3",
                    "batch_id": batch_id,
                    "platform_work_id": work_id,
                    "ok": False,
                    "error_reason": "skip:video_download_url_missing",
                    "subtitle_invalid": subtitle_invalid,
                    "public_url_present": False,
                }
            )
            u3_failed_count += 1
            continue

        u3_result = run_u3_public_url_fallback(
            base_url=base_url,
            token=token,
            timeout_ms=timeout_ms,
            source_url=source_url,
        )
        public_url = normalize_media_url(u3_result.get("public_url"))
        trace.append(
            {
                "step": "author_home.asr.xhs_u3",
                "batch_id": batch_id,
                "platform_work_id": work_id,
                "ok": bool(u3_result.get("ok") and public_url),
                "error_reason": u3_result.get("error_reason"),
                "subtitle_invalid": subtitle_invalid,
                "source_url": source_url,
                "public_url_present": bool(public_url),
                "u3_trace": u3_result.get("trace", []),
            }
        )

        if not u3_result.get("ok") or not public_url:
            work.update(_video_caption_fallback_result(work, normalize_text(u3_result.get("error_reason")) or "u3_bridge_failed"))
            u3_failed_count += 1
            continue

        u2_entries.append(
            {
                "work": work,
                "work_id": work_id,
                "video_download_url": public_url,
                "fallback_reason": f"xhs_u3_then_u2_failed:{subtitle_invalid}",
                "u3_public_url": public_url,
            }
        )

    batch_bundle = {
        "trace": [],
        "submitted": False,
        "completed": False,
        "mapped_count": 0,
        "unmapped_entries": [],
        "batch_progress": {},
    }
    if u2_entries:
        batch_bundle = _run_u2_batch_for_entries(
            batch_id=batch_id,
            entries=u2_entries,
            base_url=base_url,
            token=token,
            timeout_ms=timeout_ms,
            poll_interval_sec=poll_interval_sec,
            max_polls=max_polls,
            submit_max_retries=submit_max_retries,
            submit_backoff_ms=submit_backoff_ms,
            timeout_retry_enabled=timeout_retry_enabled,
            timeout_retry_max_retries=timeout_retry_max_retries,
        )
        trace.extend(batch_bundle.get("trace") if isinstance(batch_bundle.get("trace"), list) else [])

    unmapped_entries = list(batch_bundle.get("unmapped_entries") or [])
    for entry in unmapped_entries:
        work = entry.get("work")
        if not isinstance(work, dict):
            continue
        work.update(_video_caption_fallback_result(work, normalize_text(entry.get("fallback_reason")) or "xhs_u3_then_u2_failed"))

    return {
        "trace": trace,
        "submitted": bool(batch_bundle.get("submitted")),
        "completed": bool(batch_bundle.get("completed")),
        "mapped_count": int(batch_bundle.get("mapped_count") or 0),
        "unmapped_count": len(unmapped_entries),
        "u3_ready_count": len(u2_entries),
        "u3_failed_count": u3_failed_count,
    }


def _mark_text_work_ready(work: Dict[str, Any]) -> Dict[str, Any]:
    caption_raw = normalize_text(work.get("caption_raw"))
    return {
        "primary_text": caption_raw,
        "primary_text_source": "caption_raw",
        "analysis_eligibility": "eligible" if caption_raw else "incomplete",
        "analysis_exclusion_reason": "" if caption_raw else "caption_raw_missing",
        "asr_status": "not_applicable",
        "asr_error_reason": "",
        "asr_source": "fallback_none",
    }


def _run_u2_batch_for_entries(
    *,
    batch_id: str,
    entries: List[Dict[str, Any]],
    base_url: str,
    token: str,
    timeout_ms: int,
    poll_interval_sec: float,
    max_polls: int,
    submit_max_retries: int,
    submit_backoff_ms: int,
    timeout_retry_enabled: bool,
    timeout_retry_max_retries: int,
) -> Dict[str, Any]:
    url_to_entries: Dict[str, List[Dict[str, Any]]] = {}
    unique_urls: List[str] = []

    for entry in entries:
        normalized_url = normalize_media_url(entry.get("video_download_url") or entry.get("video_down_url"))
        if not normalized_url:
            continue
        entry["normalized_video_url"] = normalized_url
        if normalized_url not in url_to_entries:
            url_to_entries[normalized_url] = []
            unique_urls.append(normalized_url)
        url_to_entries[normalized_url].append(entry)

    if not unique_urls:
        return {
            "trace": [
                {
                    "step": "author_home.asr.batch.submitted",
                    "batch_id": batch_id,
                    "ok": False,
                    "error_reason": "batch_no_valid_urls",
                    "batch_size": len(entries),
                }
            ],
            "unmapped_entries": list(entries),
            "mapped_count": 0,
            "task_metrics": {},
            "submitted": False,
            "completed": False,
        }

    bundle = run_u2_asr_batch_with_timeout_retry(
        base_url=base_url,
        token=token,
        timeout_ms=timeout_ms,
        file_urls=unique_urls,
        submit_max_retries=submit_max_retries,
        submit_backoff_ms=submit_backoff_ms,
        poll_interval_sec=poll_interval_sec,
        max_polls=max_polls,
        timeout_retry_enabled=timeout_retry_enabled,
        timeout_retry_max_retries=timeout_retry_max_retries,
    )

    submit_bundle = bundle.get("submit_bundle") if isinstance(bundle.get("submit_bundle"), dict) else {}
    submit_response = submit_bundle.get("submit_response") if isinstance(submit_bundle.get("submit_response"), dict) else {}
    poll_result = bundle.get("poll_result") if isinstance(bundle.get("poll_result"), dict) else {}
    task_metrics = bundle.get("task_metrics") if isinstance(bundle.get("task_metrics"), dict) else {}
    submit_accepted = bool(submit_response.get("ok") and submit_bundle.get("task_id"))

    trace: List[Dict[str, Any]] = [
        {
            "step": "author_home.asr.batch.submitted",
            "batch_id": batch_id,
            "ok": submit_accepted,
            "batch_size": len(entries),
            "batch_unique_urls": len(unique_urls),
            "task_id": submit_bundle.get("task_id"),
            "submit_status": submit_bundle.get("final_submit_status"),
            "error_reason": submit_response.get("error_reason"),
        }
    ]

    batch_progress = bundle.get("batch_progress") if isinstance(bundle.get("batch_progress"), dict) else {}
    batch_complete = bool(bundle.get("batch_complete") or poll_result.get("batch_complete"))

    trace.append(
        {
            "step": "author_home.asr.batch.completed",
            "batch_id": batch_id,
            "ok": batch_complete,
            "task_status": poll_result.get("task_status"),
            "error_reason": poll_result.get("error_reason"),
            "task_metrics": task_metrics,
            "batch_progress": batch_progress,
            "batch_complete": batch_complete,
        }
    )

    mapped_results = bundle.get("mapped_results") if isinstance(bundle.get("mapped_results"), dict) else {}
    mapped_count = 0
    unmapped_entries: List[Dict[str, Any]] = []

    batch_error = normalize_text(poll_result.get("error_reason")) or "batch_result_unmapped"

    for normalized_url, grouped_entries in url_to_entries.items():
        mapped_item = mapped_results.get(normalized_url) if isinstance(mapped_results, dict) else None
        transcript = _clean_text(mapped_item.get("transcript_text")) if isinstance(mapped_item, dict) else ""
        mapped_status = normalize_text(mapped_item.get("task_status") if isinstance(mapped_item, dict) else "").upper()
        mapped_error = normalize_text(mapped_item.get("error_reason") if isinstance(mapped_item, dict) else "")
        mapped_ok = bool(mapped_item.get("ok")) if isinstance(mapped_item, dict) else False

        if (mapped_ok or mapped_status in {"SUCCEEDED", "SUCCESS", "COMPLETED", "DONE"}) and transcript:
            for entry in grouped_entries:
                entry["work"].update(
                    _build_transcript_result(
                        transcript,
                        subtitle_source="external_asr",
                        asr_source="external_asr",
                    )
                )
                mapped_count += 1
        else:
            fallback_reason = mapped_error or batch_error or ("u2_batch_incomplete" if not batch_complete else "batch_result_unmapped")
            for entry in grouped_entries:
                entry["fallback_reason"] = fallback_reason
                unmapped_entries.append(entry)

    trace.append(
        {
            "step": "author_home.asr.batch.mapped",
            "batch_id": batch_id,
            "mapped_count": mapped_count,
            "mapped_urls": len([key for key in url_to_entries.keys() if isinstance(mapped_results.get(key), dict)]),
        }
    )

    if unmapped_entries:
        trace.append(
            {
                "step": "author_home.asr.batch.unmapped",
                "batch_id": batch_id,
                "unmapped_count": len(unmapped_entries),
                "reason": normalize_text(unmapped_entries[0].get("fallback_reason")) if unmapped_entries else "batch_result_unmapped",
            }
        )

    return {
        "trace": trace,
        "unmapped_entries": unmapped_entries,
        "mapped_count": mapped_count,
        "task_metrics": task_metrics,
        "batch_progress": batch_progress,
        "batch_complete": batch_complete,
        "submitted": submit_accepted,
        "completed": batch_complete,
    }


def enrich_author_home_asr(
    *,
    platform: str,
    works: List[Dict[str, Any]],
    base_url: str,
    token: str,
    timeout_ms: int,
    poll_interval_sec: float = 3.0,
    max_polls: int = 30,
    douyin_submit_max_retries: int = 2,
    douyin_submit_backoff_ms: int = 1500,
    xhs_submit_max_retries: int = 0,
    xhs_submit_backoff_ms: int = 0,
    timeout_retry_enabled: bool = True,
    timeout_retry_max_retries: int = 3,
    batch_size: int = DEFAULT_BATCH_SUBMIT_SIZE,
    checkpoint: Optional[Dict[str, Any]] = None,
    progress: Optional[ProgressReporter] = None,
) -> Dict[str, Any]:
    trace: List[Dict[str, Any]] = []
    deduped_works, duplicate_count = _dedupe_works_by_platform_id(works)

    checkpoint_in = checkpoint if isinstance(checkpoint, dict) else {}
    completed_ids = {
        normalize_text(item)
        for item in (checkpoint_in.get("completed_work_ids") or [])
        if normalize_text(item)
    }

    requested_batch = int(batch_size or DEFAULT_BATCH_SUBMIT_SIZE)
    effective_batch = clamp_u2_batch_submit_size(
        requested_batch,
        default=DEFAULT_BATCH_SUBMIT_SIZE,
        hard_limit=MAX_BATCH_SUBMIT_SIZE,
    )
    if platform == "xiaohongshu":
        effective_batch = min(effective_batch, XHS_U3_U2_BATCH_SIZE)

    trace.append(
        {
            "step": "author_home.asr.init",
            "platform": platform,
            "input_count": len(works),
            "deduped_count": len(deduped_works),
            "duplicate_count": duplicate_count,
            "resume_completed": len(completed_ids),
            "requested_batch_size": requested_batch,
            "batch_size": effective_batch,
            "batch_size_clamped": requested_batch != effective_batch,
            "batch_submit_hard_limit": MAX_BATCH_SUBMIT_SIZE,
        }
    )
    if progress is not None:
        progress.started(
            stage="author_home.asr",
            message="author_home asr enrichment started",
            data={
                "input_count": len(works),
                "deduped_count": len(deduped_works),
                "resume_completed": len(completed_ids),
                "batch_size": effective_batch,
            },
        )

    queue: List[Dict[str, Any]] = []
    for work in deduped_works:
        work_id = normalize_text(work.get("platform_work_id"))
        if work_id and work_id in completed_ids:
            continue
        queue.append(work)

    trace.append(
        {
            "step": "author_home.asr.collected_works",
            "platform": platform,
            "queued_count": len(queue),
        }
    )

    batch_total = (len(queue) + effective_batch - 1) // effective_batch if queue else 0
    if progress is not None:
        progress.progress(
            stage="author_home.asr.queue",
            message="author_home asr queue prepared",
            data={"queued_count": len(queue), "batch_total": batch_total},
        )

    success_count = 0
    fallback_none_count = 0
    submitted_batches = 0
    completed_batches = 0
    batch_mapped_count = 0
    batch_unmapped_count = 0
    fallback_single_count = 0

    for batch_index in range(batch_total):
        batch = queue[batch_index * effective_batch : (batch_index + 1) * effective_batch]
        batch_id = f"batch-{batch_index + 1:03d}"
        if progress is not None:
            progress.progress(
                stage="author_home.asr.batch",
                message="processing author_home asr batch",
                data={"batch_id": batch_id, "batch_index": batch_index + 1, "batch_total": batch_total, "batch_size": len(batch)},
            )

        batch_u2_entries: List[Dict[str, Any]] = []
        batch_xhs_u3_entries: List[Dict[str, Any]] = []

        for work in batch:
            work_id = normalize_text(work.get("platform_work_id"))

            if platform == "douyin":
                gate = _evaluate_u2_gate(work, platform=platform)
                trace.append(
                    {
                        "step": "author_home.asr.u2_gate",
                        "batch_id": batch_id,
                        "platform_work_id": work_id,
                        "ok": bool(gate.get("can_u2")),
                        "can_u2": bool(gate.get("can_u2")),
                        "gate_reason": gate.get("gate_reason"),
                        "rule": U2_GATE_RULE,
                        "is_video": gate.get("is_video"),
                        "duration_ms": gate.get("duration_ms"),
                        "video_download_url_present": gate.get("video_download_url_present"),
                    }
                )

                if not gate.get("can_u2"):
                    if gate.get("is_video"):
                        work.update(_video_caption_fallback_result(work, str(gate.get("gate_reason") or "skip:unknown")))
                    else:
                        work.update(_mark_text_work_ready(work))
                else:
                    batch_u2_entries.append(
                        {
                            "work": work,
                            "work_id": work_id,
                            "video_download_url": gate.get("video_download_url"),
                            "fallback_reason": "batch_result_unmapped",
                        }
                    )
                continue

            if not _resolve_is_video(work, platform=platform):
                work.update(_mark_text_work_ready(work))
                trace.append(
                    {
                        "step": "author_home.asr.skip",
                        "batch_id": batch_id,
                        "platform_work_id": work_id,
                        "ok": True,
                        "reason": "text_work_no_asr_required",
                    }
                )
                continue

            subtitle_probe = _resolve_xhs_subtitle(work, timeout_ms=timeout_ms)
            subtitle_text = normalize_text(subtitle_probe.get("text"))
            subtitle_source = normalize_text(subtitle_probe.get("subtitle_source"))
            subtitle_urls = subtitle_probe.get("subtitle_urls") if isinstance(subtitle_probe.get("subtitle_urls"), list) else []
            subtitle_field = normalize_text(subtitle_probe.get("subtitle_field"))
            subtitle_invalid = _invalid_subtitle_reason(subtitle_text)
            if subtitle_invalid is None:
                work.update(
                    _build_transcript_result(
                        subtitle_text,
                        subtitle_source="native_subtitle",
                        asr_source="native_subtitle",
                    )
                )
                trace.append(
                    {
                        "step": "author_home.asr.xhs_subtitle",
                        "batch_id": batch_id,
                        "platform_work_id": work_id,
                        "ok": True,
                        "subtitle_source": subtitle_source,
                        "subtitle_field": subtitle_field,
                        "subtitle_url_count": len(subtitle_urls),
                        "failure_category": "",
                    }
                )
            else:
                trace.append(
                    {
                        "step": "author_home.asr.xhs_subtitle",
                        "batch_id": batch_id,
                        "platform_work_id": work_id,
                        "ok": False,
                        "error_reason": subtitle_invalid,
                        "subtitle_source": subtitle_source,
                        "subtitle_field": subtitle_field,
                        "subtitle_url_count": len(subtitle_urls),
                        "failure_category": subtitle_probe.get("failure_category"),
                        "invalid_reasons": subtitle_probe.get("invalid_reasons"),
                    }
                )
                gate = _evaluate_u2_gate(work, platform=platform)
                trace.append(
                    {
                        "step": "author_home.asr.u2_gate",
                        "batch_id": batch_id,
                        "platform_work_id": work_id,
                        "ok": bool(gate.get("can_u2")),
                        "can_u2": bool(gate.get("can_u2")),
                        "gate_reason": gate.get("gate_reason"),
                        "rule": U2_GATE_RULE,
                        "is_video": gate.get("is_video"),
                        "duration_ms": gate.get("duration_ms"),
                        "video_download_url_present": gate.get("video_download_url_present"),
                    }
                )
                if not gate.get("can_u2"):
                    work.update(_video_caption_fallback_result(work, str(gate.get("gate_reason") or "skip:unknown")))
                else:
                    batch_xhs_u3_entries.append(
                        {
                            "work": work,
                            "work_id": work_id,
                            "video_download_url": gate.get("video_download_url"),
                            "subtitle_invalid": subtitle_invalid,
                        }
                    )

        fallback_entries: List[Dict[str, Any]] = []
        if batch_u2_entries:
            batch_bundle = _run_u2_batch_for_entries(
                batch_id=batch_id,
                entries=batch_u2_entries,
                base_url=base_url,
                token=token,
                timeout_ms=timeout_ms,
                poll_interval_sec=poll_interval_sec,
                max_polls=max_polls,
                submit_max_retries=max(0, int(douyin_submit_max_retries if platform == "douyin" else xhs_submit_max_retries)),
                submit_backoff_ms=max(0, int(douyin_submit_backoff_ms if platform == "douyin" else xhs_submit_backoff_ms)),
                timeout_retry_enabled=timeout_retry_enabled,
                timeout_retry_max_retries=max(0, int(timeout_retry_max_retries)),
            )
            trace.extend(batch_bundle.get("trace") if isinstance(batch_bundle.get("trace"), list) else [])

            if batch_bundle.get("submitted"):
                submitted_batches += 1
            if batch_bundle.get("completed"):
                completed_batches += 1

            batch_mapped_count += int(batch_bundle.get("mapped_count") or 0)
            fallback_entries = list(batch_bundle.get("unmapped_entries") or [])
            batch_unmapped_count += len(fallback_entries)

        if batch_xhs_u3_entries:
            xhs_batch_bundle = _run_xhs_u3_then_u2_batch_for_entries(
                batch_id=batch_id,
                entries=batch_xhs_u3_entries,
                base_url=base_url,
                token=token,
                timeout_ms=timeout_ms,
                poll_interval_sec=poll_interval_sec,
                max_polls=max_polls,
                submit_max_retries=max(0, int(xhs_submit_max_retries)),
                submit_backoff_ms=max(0, int(xhs_submit_backoff_ms)),
                timeout_retry_enabled=timeout_retry_enabled,
                timeout_retry_max_retries=max(0, int(timeout_retry_max_retries)),
            )
            trace.extend(xhs_batch_bundle.get("trace") if isinstance(xhs_batch_bundle.get("trace"), list) else [])
            if xhs_batch_bundle.get("submitted"):
                submitted_batches += 1
            if xhs_batch_bundle.get("completed"):
                completed_batches += 1
            batch_mapped_count += int(xhs_batch_bundle.get("mapped_count") or 0)
            batch_unmapped_count += int(xhs_batch_bundle.get("unmapped_count") or 0)

        for fallback_entry in fallback_entries:
            fallback_work = fallback_entry.get("work")
            if not isinstance(fallback_work, dict):
                continue

            retry_result, retry_trace = _run_u2_for_work(
                platform=platform,
                work=fallback_work,
                base_url=base_url,
                token=token,
                timeout_ms=timeout_ms,
                poll_interval_sec=poll_interval_sec,
                max_polls=max_polls,
                submit_max_retries=max(0, int(douyin_submit_max_retries if platform == "douyin" else xhs_submit_max_retries)),
                submit_backoff_ms=max(0, int(douyin_submit_backoff_ms if platform == "douyin" else xhs_submit_backoff_ms)),
                timeout_retry_enabled=timeout_retry_enabled,
                timeout_retry_max_retries=max(0, int(timeout_retry_max_retries)),
            )
            retry_trace["step"] = "author_home.asr.batch.fallback"
            retry_trace["batch_id"] = batch_id
            retry_trace["fallback_trigger_reason"] = fallback_entry.get("fallback_reason")
            trace.append(retry_trace)
            fallback_single_count += 1
            fallback_work.update(retry_result)

        batch_success = 0
        batch_failed = 0
        for work in batch:
            work_id = normalize_text(work.get("platform_work_id"))
            if work_id:
                completed_ids.add(work_id)

            if str(work.get("analysis_eligibility") or "") == "eligible":
                success_count += 1
                batch_success += 1
            else:
                fallback_none_count += 1
                batch_failed += 1

        trace.append(
            {
                "step": "author_home.asr.batch_done",
                "batch_id": batch_id,
                "batch_index": batch_index + 1,
                "batch_total": batch_total,
                "batch_size": len(batch),
                "batch_success": batch_success,
                "batch_failed": batch_failed,
                "fallback_singles": fallback_single_count,
            }
        )
        if progress is not None:
            progress.progress(
                stage="author_home.asr.batch",
                message="author_home asr batch finished",
                data={
                    "batch_id": batch_id,
                    "batch_index": batch_index + 1,
                    "batch_total": batch_total,
                    "batch_success": batch_success,
                    "batch_failed": batch_failed,
                },
            )

    failed_work_ids = sorted(
        list(
            {
                normalize_text(work.get("platform_work_id"))
                for work in deduped_works
                if isinstance(work, dict)
                and normalize_text(work.get("platform_work_id"))
                and str(work.get("analysis_eligibility") or "") != "eligible"
            }
        )
    )

    checkpoint_out = {
        "platform": platform,
        "completed_work_ids": sorted(completed_ids),
        "failed_work_ids": failed_work_ids,
        "batch_size": effective_batch,
        "batches_total": batch_total,
        "batches_submitted": submitted_batches,
        "batches_completed": completed_batches,
        "batch_mapped": batch_mapped_count,
        "batch_unmapped": batch_unmapped_count,
        "fallback_singles": fallback_single_count,
        "total_works": len(deduped_works),
        "processed_works": len(completed_ids),
        # backward-compatible checkpoint fields
        "refill_attempted": fallback_single_count,
    }

    stats = {
        "total": len(deduped_works),
        "success": success_count,
        "fallback_none": fallback_none_count,
        "duplicates_dropped": duplicate_count,
        "submitted_batches": submitted_batches,
        "completed_batches": completed_batches,
        "batch_mapped": batch_mapped_count,
        "batch_unmapped": batch_unmapped_count,
        "fallback_singles": fallback_single_count,
        # backward-compatible stats fields
        "refill_attempted": fallback_single_count,
        "refill_failed": len(failed_work_ids),
    }

    if progress is not None:
        progress.done(
            stage="author_home.asr",
            message="author_home asr enrichment finished",
            data={
                "total": len(deduped_works),
                "success": success_count,
                "fallback_none": fallback_none_count,
                "submitted_batches": submitted_batches,
                "completed_batches": completed_batches,
            },
        )

    return {
        "works": deduped_works,
        "trace": trace,
        "checkpoint": checkpoint_out,
        "stats": stats,
    }
