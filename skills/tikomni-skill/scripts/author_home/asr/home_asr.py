#!/usr/bin/env python3
"""Author-home ASR enrichment (batch + checkpoint + idempotent dedupe)."""

from __future__ import annotations

import json
import re
import urllib.request
from typing import Any, Dict, List, Optional, Tuple

from scripts.core.tikomni_common import normalize_text
from scripts.pipeline.asr.asr_pipeline import (
    clamp_u2_batch_submit_size,
    normalize_media_url,
    run_u2_asr_batch_with_timeout_retry,
    run_u2_asr_candidates_with_timeout_retry,
)

DEFAULT_BATCH_SUBMIT_SIZE = 50
MAX_BATCH_SUBMIT_SIZE = 100
U2_GATE_MIN_DURATION_MS = 13000
U2_GATE_MAX_DURATION_MS = 1800000
U2_GATE_RULE = "is_video && 13000<duration_ms<=1800000 && video_down_url_present"


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

    content_type = normalize_text(work.get("content_type")).lower()
    if content_type in {"video", "mixed", "mix", "video_note", "note_video"}:
        return True
    if content_type in {"image", "photo", "album", "note", "text"}:
        return False

    if platform == "douyin":
        return True

    raw_ref = work.get("raw_ref") if isinstance(work.get("raw_ref"), dict) else {}
    xhs_type_hint = normalize_text(raw_ref.get("type") or raw_ref.get("note_type")).lower()
    if xhs_type_hint in {"video", "0", "normal", "mixed", "mix"}:
        return True
    if xhs_type_hint in {"image", "1", "note", "photo"}:
        return False

    return False


def _evaluate_u2_gate(work: Dict[str, Any], *, platform: str) -> Dict[str, Any]:
    is_video = _resolve_is_video(work, platform=platform)
    duration_ms = _to_int_or_none(work.get("duration_ms"))
    video_down_url = normalize_text(work.get("video_down_url"))

    if not is_video:
        gate_reason = "skip:not_video"
    elif duration_ms is None:
        gate_reason = "skip:duration_missing"
    elif duration_ms <= U2_GATE_MIN_DURATION_MS:
        gate_reason = "skip:duration_too_short"
    elif duration_ms > U2_GATE_MAX_DURATION_MS:
        gate_reason = "skip:duration_too_long"
    elif not video_down_url:
        gate_reason = "skip:video_down_url_missing"
    else:
        gate_reason = "pass"

    return {
        "can_u2": gate_reason == "pass",
        "gate_reason": gate_reason,
        "is_video": is_video,
        "duration_ms": duration_ms,
        "video_down_url": video_down_url,
        "video_down_url_present": bool(video_down_url),
    }


def _clean_text(text: Any) -> str:
    if text is None:
        return ""
    lines = [normalize_text(line) for line in str(text).splitlines()]
    lines = [line for line in lines if line]
    return "\n".join(lines).strip()


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
        return _fallback_none_result(gate_reason), {
            "step": "author_home.asr.u2_gate",
            "platform_work_id": work.get("platform_work_id"),
            "ok": False,
            "can_u2": False,
            "gate_reason": gate_reason,
            "rule": U2_GATE_RULE,
            "is_video": gate.get("is_video"),
            "duration_ms": gate.get("duration_ms"),
            "video_down_url_present": gate.get("video_down_url_present"),
        }

    video_down_url = normalize_text(gate.get("video_down_url"))

    bundle = run_u2_asr_candidates_with_timeout_retry(
        base_url=base_url,
        token=token,
        timeout_ms=timeout_ms,
        candidates=[video_down_url],
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
        "selected_video_url": bundle.get("chosen_candidate") or video_down_url,
        "rounds": bundle.get("rounds", []),
        "candidate_attempts": bundle.get("candidate_attempts", []),
        "timeout_retry": bundle.get("timeout_retry", {}),
        "gate_reason": "pass",
        "rule": U2_GATE_RULE,
    }

    if transcript:
        return {
            "asr_raw": transcript,
            "asr_clean": transcript,
            "asr_status": "success",
            "asr_error_reason": "",
            "asr_source": "u2",
        }, trace

    return {
        "asr_raw": "",
        "asr_clean": "",
        "asr_status": "failed",
        "asr_error_reason": normalize_text(poll_result.get("error_reason")) or "u2_failed",
        "asr_source": "fallback_none",
    }, trace


def _resolve_xhs_subtitle(work: Dict[str, Any], timeout_ms: int) -> Tuple[str, str, List[str]]:
    raw_ref = work.get("raw_ref") if isinstance(work.get("raw_ref"), dict) else {}
    inline_text = _clean_text(work.get("asr_raw") or raw_ref.get("subtitle_inline"))

    subtitle_urls = raw_ref.get("subtitle_urls") if isinstance(raw_ref.get("subtitle_urls"), list) else []
    subtitle_urls = [normalize_text(item) for item in subtitle_urls if normalize_text(item)]

    if inline_text:
        return inline_text, "inline", subtitle_urls

    fetched = _fetch_subtitle_text(subtitle_urls, timeout_ms=timeout_ms)
    return _clean_text(fetched), "url", subtitle_urls


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
        "asr_raw": "",
        "asr_clean": "",
        "asr_status": "failed",
        "asr_error_reason": normalize_text(reason) or "asr_failed",
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
        normalized_url = normalize_media_url(entry.get("video_down_url"))
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

    trace: List[Dict[str, Any]] = [
        {
            "step": "author_home.asr.batch.submitted",
            "batch_id": batch_id,
            "ok": bool(submit_response.get("ok") and submit_bundle.get("task_id")),
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
                    {
                        "asr_raw": transcript,
                        "asr_clean": transcript,
                        "asr_status": "success",
                        "asr_error_reason": "",
                        "asr_source": "u2",
                    }
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
        "submitted": True,
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

        batch_u2_entries: List[Dict[str, Any]] = []

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
                        "video_down_url_present": gate.get("video_down_url_present"),
                    }
                )

                if not gate.get("can_u2"):
                    work.update(_fallback_none_result(str(gate.get("gate_reason") or "skip:unknown")))
                else:
                    batch_u2_entries.append(
                        {
                            "work": work,
                            "work_id": work_id,
                            "video_down_url": gate.get("video_down_url"),
                            "fallback_reason": "batch_result_unmapped",
                        }
                    )
                continue

            subtitle_text, subtitle_source, subtitle_urls = _resolve_xhs_subtitle(work, timeout_ms=timeout_ms)
            subtitle_invalid = _invalid_subtitle_reason(subtitle_text)
            if subtitle_invalid is None:
                work.update(
                    {
                        "asr_raw": subtitle_text,
                        "asr_clean": subtitle_text,
                        "asr_status": "success",
                        "asr_error_reason": "",
                        "asr_source": "xhs_subtitle",
                    }
                )
                trace.append(
                    {
                        "step": "author_home.asr.xhs_subtitle",
                        "batch_id": batch_id,
                        "platform_work_id": work_id,
                        "ok": True,
                        "subtitle_source": subtitle_source,
                        "subtitle_url_count": len(subtitle_urls),
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
                        "subtitle_url_count": len(subtitle_urls),
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
                        "video_down_url_present": gate.get("video_down_url_present"),
                        "subtitle_invalid": subtitle_invalid,
                    }
                )

                if not gate.get("can_u2"):
                    work.update(_fallback_none_result(str(gate.get("gate_reason") or "skip:unknown")))
                else:
                    batch_u2_entries.append(
                        {
                            "work": work,
                            "work_id": work_id,
                            "video_down_url": gate.get("video_down_url"),
                            "fallback_reason": f"xhs_subtitle_invalid:{subtitle_invalid}",
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

            if work.get("asr_status") == "success":
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

    failed_work_ids = sorted(
        list(
            {
                normalize_text(work.get("platform_work_id"))
                for work in deduped_works
                if isinstance(work, dict)
                and normalize_text(work.get("platform_work_id"))
                and str(work.get("asr_status") or "") != "success"
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

    return {
        "works": deduped_works,
        "trace": trace,
        "checkpoint": checkpoint_out,
        "stats": stats,
    }
