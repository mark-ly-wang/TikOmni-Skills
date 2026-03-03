#!/usr/bin/env python3
"""Shared ASR pipeline helpers for runner scripts."""

import time
from typing import Any, Dict, List, Optional

from tikomni_common import (
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
    idempotency_key: Optional[str],
) -> Dict[str, Any]:
    extra_headers = {}
    if idempotency_key:
        extra_headers["idempotency-key"] = idempotency_key

    return call_json_api(
        base_url=base_url,
        path="/api/u2/v1/services/audio/asr/transcription",
        token=token,
        method="POST",
        timeout_ms=timeout_ms,
        body={"input": {"file_urls": [video_url]}},
        extra_headers=extra_headers,
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
    idempotency_key: Optional[str],
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
            idempotency_key=idempotency_key,
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


def run_u2_asr_with_timeout_retry(
    *,
    base_url: str,
    token: str,
    timeout_ms: int,
    video_url: str,
    idempotency_key: Optional[str],
    submit_max_retries: int,
    submit_backoff_ms: int,
    poll_interval_sec: float,
    max_polls: int,
    timeout_retry_enabled: bool = True,
    timeout_retry_max_retries: int = 1,
) -> Dict[str, Any]:
    conservative_retries = 1 if int(timeout_retry_max_retries) > 0 else 0
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
            idempotency_key=idempotency_key,
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
