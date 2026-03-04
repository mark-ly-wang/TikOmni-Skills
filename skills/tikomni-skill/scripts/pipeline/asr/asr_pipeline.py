#!/usr/bin/env python3
"""Shared ASR pipeline helpers for runner scripts."""

import time
from urllib.parse import urlparse, urlunparse
from typing import Any, Dict, List, Optional

from scripts.core.tikomni_common import (
    call_json_api,
    extract_task_id,
    extract_task_status,
    extract_transcript_text,
    is_terminal_status,
)


def submit_u2_asr(
    *,
    base_url: str,
    token: str,
    timeout_ms: int,
    video_url: str,
) -> Dict[str, Any]:
    return call_json_api(
        base_url=base_url,
        path="/api/u2/v1/services/audio/asr/transcription",
        token=token,
        method="POST",
        timeout_ms=timeout_ms,
        body={"input": {"file_urls": [video_url]}},
    )


def is_retriable_submit_failure(response: Dict[str, Any]) -> bool:
    status_code = response.get("status_code")
    if isinstance(status_code, str) and status_code.isdigit():
        status_code = int(status_code)
    if isinstance(status_code, (int, float)) and int(status_code) in {502, 503, 504}:
        return True

    error_reason = str(response.get("error_reason") or "").upper()
    return "UPSTREAM_TIMEOUT" in error_reason or "TIMEOUT" in error_reason


def submit_u2_asr_with_retry(
    *,
    base_url: str,
    token: str,
    timeout_ms: int,
    video_url: str,
    max_retries: int,
    backoff_ms: int,
) -> Dict[str, Any]:
    retries = max(0, int(max_retries))
    base_backoff = max(0, int(backoff_ms))
    max_attempts = 1 + retries

    retry_chain: List[Dict[str, Any]] = []
    final_response: Dict[str, Any] = {}
    final_task_id: Optional[str] = None
    final_submit_status = "failed_unknown"

    for attempt in range(1, max_attempts + 1):
        wait_ms = 0 if attempt == 1 else base_backoff * (2 ** (attempt - 2))
        if wait_ms > 0:
            time.sleep(wait_ms / 1000.0)

        submit_response = submit_u2_asr(
            base_url=base_url,
            token=token,
            timeout_ms=timeout_ms,
            video_url=video_url,
        )
        task_id = extract_task_id(submit_response.get("data"))
        retriable = is_retriable_submit_failure(submit_response)

        retry_chain.append(
            {
                "attempt": attempt,
                "wait_ms": wait_ms,
                "status_code": submit_response.get("status_code"),
                "error_reason": submit_response.get("error_reason"),
                "ok": submit_response.get("ok"),
                "task_id": task_id,
                "retriable": retriable,
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
    }


def clean_transcript_text(raw_text: Any) -> str:
    if raw_text is None:
        return ""
    return str(raw_text).strip()


def poll_u2_task_core(
    *,
    base_url: str,
    token: str,
    timeout_ms: int,
    task_id: str,
    poll_interval_sec: float,
    max_polls: int,
) -> Dict[str, Any]:
    trace = []
    last_request_id = None

    for attempt in range(1, max_polls + 1):
        response = call_json_api(
            base_url=base_url,
            path=f"/api/u2/v1/tasks/{task_id}",
            token=token,
            method="POST",
            timeout_ms=timeout_ms,
        )

        status = extract_task_status(response["data"])
        last_request_id = response.get("request_id") or last_request_id

        trace.append(
            {
                "attempt": attempt,
                "status_code": response.get("status_code"),
                "task_status": status,
                "request_id": response.get("request_id"),
                "error_reason": response.get("error_reason"),
            }
        )

        if not response["ok"]:
            if attempt < max_polls:
                time.sleep(max(poll_interval_sec, 0.2))
                continue
            return {
                "ok": False,
                "task_id": task_id,
                "task_status": status or "UNKNOWN",
                "request_id": last_request_id,
                "error_reason": response.get("error_reason") or "u2_poll_http_error",
                "raw_task": response["data"],
                "trace": trace,
            }

        if is_terminal_status(status):
            transcript = extract_transcript_text(response["data"]) if status == "SUCCEEDED" else ""
            return {
                "ok": status == "SUCCEEDED",
                "task_id": task_id,
                "task_status": status,
                "request_id": last_request_id,
                "error_reason": None if status == "SUCCEEDED" else "u2_task_failed",
                "transcript_text": clean_transcript_text(transcript),
                "raw_task": response["data"],
                "trace": trace,
            }

        time.sleep(max(poll_interval_sec, 0.2))

    return {
        "ok": False,
        "task_id": task_id,
        "task_status": "TIMEOUT",
        "request_id": last_request_id,
        "error_reason": "u2_poll_timeout",
        "raw_task": {},
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
        })

        final_bundle = bundle
        chosen_url = candidate
        if ok:
            break

        if error_reason == "INVALID_SOURCE_URL":
            continue

    final_bundle["candidate_attempts"] = attempts
    final_bundle["chosen_candidate"] = chosen_url
    final_bundle["normalized_candidates"] = normalized_candidates
    return final_bundle


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

    for round_index in range(1, max_rounds + 1):
        submit_bundle = submit_u2_asr_with_retry(
            base_url=base_url,
            token=token,
            timeout_ms=timeout_ms,
            video_url=video_url,
            max_retries=submit_max_retries,
            backoff_ms=submit_backoff_ms,
        )
        submit_response = submit_bundle.get("submit_response", {})
        task_id = submit_bundle.get("task_id")

        poll_result: Dict[str, Any]
        if submit_response.get("ok") and task_id:
            poll_result = poll_u2_task_core(
                base_url=base_url,
                token=token,
                timeout_ms=timeout_ms,
                task_id=str(task_id),
                poll_interval_sec=poll_interval_sec,
                max_polls=max_polls,
            )
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
                },
                "poll": {
                    "task_id": poll_result.get("task_id") or task_id,
                    "task_status": poll_result.get("task_status"),
                    "request_id": poll_result.get("request_id"),
                    "ok": poll_result.get("ok"),
                    "error_reason": poll_result.get("error_reason"),
                    "attempts": len(poll_result.get("trace", [])),
                },
            }
        )

        final_submit_bundle = submit_bundle
        final_poll_result = poll_result

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
    }
