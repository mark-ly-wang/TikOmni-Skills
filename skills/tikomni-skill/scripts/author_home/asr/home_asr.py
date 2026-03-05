#!/usr/bin/env python3
"""Author-home ASR enrichment (batch + checkpoint + idempotent dedupe)."""

from __future__ import annotations

import json
import re
import urllib.request
from typing import Any, Dict, List, Optional, Tuple

from scripts.core.tikomni_common import normalize_text
from scripts.pipeline.asr.asr_pipeline import run_u2_asr_candidates_with_timeout_retry


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
    video_down_url = normalize_text(work.get("video_down_url"))
    if not video_down_url:
        return {
            "asr_raw": "",
            "asr_clean": "",
            "asr_status": "failed",
            "asr_error_reason": "video_down_url_missing",
            "asr_source": "fallback_none",
        }, {
            "step": "author_home.asr.u2.skip",
            "platform_work_id": work.get("platform_work_id"),
            "ok": False,
            "error_reason": "video_down_url_missing",
        }

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
    batch_size: int = 20,
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

    trace.append(
        {
            "step": "author_home.asr.init",
            "platform": platform,
            "input_count": len(works),
            "deduped_count": len(deduped_works),
            "duplicate_count": duplicate_count,
            "resume_completed": len(completed_ids),
            "batch_size": max(1, int(batch_size or 20)),
        }
    )

    queue: List[Dict[str, Any]] = []
    for work in deduped_works:
        work_id = normalize_text(work.get("platform_work_id"))
        if work_id and work_id in completed_ids:
            continue
        queue.append(work)

    failed_queue: List[Dict[str, Any]] = []
    failed_ids: List[str] = []
    success_count = 0
    fallback_none_count = 0

    effective_batch = max(1, int(batch_size or 20))
    batch_total = (len(queue) + effective_batch - 1) // effective_batch if queue else 0

    for batch_index in range(batch_total):
        batch = queue[batch_index * effective_batch : (batch_index + 1) * effective_batch]
        batch_failed = 0
        batch_success = 0

        for work in batch:
            work_id = normalize_text(work.get("platform_work_id"))
            asr_result: Dict[str, Any] = {}
            asr_trace: Dict[str, Any] = {}

            if platform == "douyin":
                asr_result, asr_trace = _run_u2_for_work(
                    work=work,
                    base_url=base_url,
                    token=token,
                    timeout_ms=timeout_ms,
                    poll_interval_sec=poll_interval_sec,
                    max_polls=max_polls,
                    submit_max_retries=max(0, int(douyin_submit_max_retries)),
                    submit_backoff_ms=max(0, int(douyin_submit_backoff_ms)),
                    timeout_retry_enabled=timeout_retry_enabled,
                    timeout_retry_max_retries=max(0, int(timeout_retry_max_retries)),
                )
            else:
                subtitle_text, subtitle_source, subtitle_urls = _resolve_xhs_subtitle(work, timeout_ms=timeout_ms)
                subtitle_invalid = _invalid_subtitle_reason(subtitle_text)
                if subtitle_invalid is None:
                    asr_result = {
                        "asr_raw": subtitle_text,
                        "asr_clean": subtitle_text,
                        "asr_status": "success",
                        "asr_error_reason": "",
                        "asr_source": "xhs_subtitle",
                    }
                    asr_trace = {
                        "step": "author_home.asr.xhs_subtitle",
                        "platform_work_id": work_id,
                        "ok": True,
                        "subtitle_source": subtitle_source,
                        "subtitle_url_count": len(subtitle_urls),
                    }
                else:
                    asr_trace = {
                        "step": "author_home.asr.xhs_subtitle",
                        "platform_work_id": work_id,
                        "ok": False,
                        "error_reason": subtitle_invalid,
                        "subtitle_source": subtitle_source,
                        "subtitle_url_count": len(subtitle_urls),
                    }
                    fallback_result, u2_trace = _run_u2_for_work(
                        work=work,
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
                    if fallback_result.get("asr_source") == "u2":
                        asr_result = fallback_result
                        u2_trace["fallback_trigger_reason"] = f"xhs_subtitle_invalid:{subtitle_invalid}"
                        trace.append(u2_trace)
                    else:
                        missing_video = not normalize_text(work.get("video_down_url"))
                        asr_result = {
                            "asr_raw": "",
                            "asr_clean": "",
                            "asr_status": "failed",
                            "asr_error_reason": (
                                f"{subtitle_invalid}_and_video_missing"
                                if missing_video
                                else normalize_text(fallback_result.get("asr_error_reason")) or subtitle_invalid
                            ),
                            "asr_source": "fallback_none",
                        }
                        u2_trace["fallback_trigger_reason"] = f"xhs_subtitle_invalid:{subtitle_invalid}"
                        trace.append(u2_trace)

            work.update(asr_result)
            trace.append(asr_trace)

            if work_id:
                completed_ids.add(work_id)

            if asr_result.get("asr_status") == "success":
                success_count += 1
                batch_success += 1
            else:
                fallback_none_count += 1
                batch_failed += 1
                if normalize_text(work.get("video_down_url")):
                    failed_queue.append(work)
                    if work_id:
                        failed_ids.append(work_id)

        trace.append(
            {
                "step": "author_home.asr.batch_done",
                "batch_index": batch_index + 1,
                "batch_total": batch_total,
                "batch_size": len(batch),
                "batch_success": batch_success,
                "batch_failed": batch_failed,
            }
        )

    refill_failed_ids: List[str] = []
    refill_queue = []
    seen_refill = set()
    for item in failed_queue:
        key = normalize_text(item.get("platform_work_id"))
        if not key or key in seen_refill:
            continue
        seen_refill.add(key)
        refill_queue.append(item)

    for work in refill_queue:
        work_id = normalize_text(work.get("platform_work_id"))
        retry_result, retry_trace = _run_u2_for_work(
            work=work,
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
        retry_trace["step"] = "author_home.asr.refill"
        retry_trace["refill_attempt"] = 1
        trace.append(retry_trace)

        if retry_result.get("asr_source") == "u2" and retry_result.get("asr_status") == "success":
            work.update(retry_result)
            continue

        if work_id:
            refill_failed_ids.append(work_id)

    checkpoint_out = {
        "platform": platform,
        "completed_work_ids": sorted(completed_ids),
        "failed_work_ids": sorted(list(dict.fromkeys(refill_failed_ids or failed_ids))),
        "batch_size": effective_batch,
        "batches_total": batch_total,
        "total_works": len(deduped_works),
        "processed_works": len(completed_ids),
        "refill_attempted": len(refill_queue),
    }

    stats = {
        "total": len(deduped_works),
        "success": success_count,
        "fallback_none": fallback_none_count,
        "duplicates_dropped": duplicate_count,
        "refill_attempted": len(refill_queue),
        "refill_failed": len(refill_failed_ids),
    }

    return {
        "works": deduped_works,
        "trace": trace,
        "checkpoint": checkpoint_out,
        "stats": stats,
    }
