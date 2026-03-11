#!/usr/bin/env python3

if __package__ in {None, ""}:
    import sys
    from pathlib import Path

    _self = Path(__file__).resolve()
    for _parent in _self.parents:
        if (_parent / "scripts" / "core" / "bootstrap_env.py").is_file():
            sys.path.insert(0, str(_parent))
            break

"""Poll Tikomni U2 task until terminal state."""

from scripts.core.bootstrap_env import bootstrap_for_direct_run

bootstrap_for_direct_run(__file__, __package__)

import argparse
from typing import Any, Callable, Dict, Optional

from scripts.core.asr_pipeline import poll_u2_task_core
from scripts.core.tikomni_common import extract_error_reason, resolve_runtime, write_json_stdout


def poll_u2_task(
    *,
    base_url: str,
    token: str,
    timeout_ms: int,
    task_id: str,
    poll_interval_sec: float,
    max_polls: int,
    pending_timeout_sec: Optional[int] = None,
    progress_callback: Optional[Callable[[Dict[str, Any]], None]] = None,
) -> Dict[str, Any]:
    return poll_u2_task_core(
        base_url=base_url,
        token=token,
        timeout_ms=timeout_ms,
        task_id=task_id,
        poll_interval_sec=poll_interval_sec,
        max_polls=max_polls,
        pending_timeout_sec=pending_timeout_sec,
        progress_callback=progress_callback,
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Poll Tikomni U2 task until SUCCEEDED/FAILED")
    parser.add_argument("task_id", help="U2 task id")
    parser.add_argument("--env-file", default=None, help="Optional env file path (e.g. <skill_root>/.env.local)")
    parser.add_argument("--api-key-env", default="TIKOMNI_API_KEY", help="API key env variable name")
    parser.add_argument("--allow-process-env", action="store_true", help="Allow process env to override .env/.env.local")
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
            allow_process_env=args.allow_process_env,
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
