#!/usr/bin/env python3
"""Poll Tikomni U2 task until terminal state."""

import argparse
import time
from typing import Any, Dict

from tikomni_common import (
    call_json_api,
    extract_error_reason,
    extract_task_status,
    extract_transcript_text,
    is_terminal_status,
    resolve_runtime,
    write_json_stdout,
)


def poll_u2_task(
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
                "transcript_text": transcript,
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


def main() -> None:
    parser = argparse.ArgumentParser(description="Poll Tikomni U2 task until SUCCEEDED/FAILED")
    parser.add_argument("task_id", help="U2 task id")
    parser.add_argument("--env-file", default=None, help="Optional env file path (e.g. skills/tikomni-skill/.env.local)")
    parser.add_argument("--api-key-env", default="TIKOMNI_API_KEY", help="API key env variable name")
    parser.add_argument("--base-url", default=None, help="Tikomni API base url")
    parser.add_argument("--timeout-ms", type=int, default=None, help="Request timeout in milliseconds")
    parser.add_argument("--poll-interval-sec", type=float, default=3.0, help="Polling interval in seconds")
    parser.add_argument("--max-polls", type=int, default=30, help="Max polling attempts")
    args = parser.parse_args()

    try:
        runtime = resolve_runtime(
            env_file=args.env_file,
            api_key_env=args.api_key_env,
            base_url=args.base_url,
            timeout_ms=args.timeout_ms,
        )
    except ValueError as error:
        write_json_stdout(
            {
                "ok": False,
                "task_id": args.task_id,
                "task_status": "UNKNOWN",
                "error_reason": str(error),
                "request_id": None,
                "trace": [],
            }
        )
        raise SystemExit(2) from error

    result = poll_u2_task(
        base_url=runtime["base_url"],
        token=runtime["token"],
        timeout_ms=runtime["timeout_ms"],
        task_id=args.task_id,
        poll_interval_sec=args.poll_interval_sec,
        max_polls=args.max_polls,
    )

    if not result["ok"] and not result.get("error_reason"):
        result["error_reason"] = extract_error_reason(result.get("raw_task", {}))

    write_json_stdout(result)
    raise SystemExit(0 if result["ok"] else 1)


if __name__ == "__main__":
    main()
