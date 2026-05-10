#!/usr/bin/env python3
"""Minimal one-shot TikOmni API task runner."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

SKILL_ROOT = Path(__file__).resolve().parents[1]
if str(SKILL_ROOT) not in sys.path:
    sys.path.insert(0, str(SKILL_ROOT))

from scripts.core.call_tikomni_api import call_endpoint
from scripts.core.resolve_api_endpoint import resolve_endpoint


def _json_stdout(payload: Dict[str, Any]) -> None:
    print(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True))


def _parse_params(raw_params: str) -> Dict[str, Any]:
    if not raw_params:
        return {}
    payload = json.loads(raw_params)
    if not isinstance(payload, dict):
        raise ValueError("params_must_be_json_object")
    return payload


def run_task(
    *,
    intent: str,
    params: Dict[str, Any],
    platform: str = "",
    capability: str = "",
    dry_run: bool = False,
    allow_process_env: bool = False,
) -> Dict[str, Any]:
    resolved = resolve_endpoint(
        platform=platform,
        capability=capability,
        intent=intent,
        context=params,
    )
    if not resolved.get("ok"):
        return resolved

    recommended = resolved.get("recommended") if isinstance(resolved.get("recommended"), dict) else {}
    endpoint_id = str(recommended.get("endpoint_id") or "")
    if not endpoint_id:
        return {
            "ok": False,
            "code": "ENDPOINT_NOT_RESOLVED",
            "error_reason": "resolver_returned_empty_endpoint_id",
            "resolution": resolved,
        }

    response = call_endpoint(
        endpoint_id=endpoint_id,
        params=params,
        allow_process_env=allow_process_env,
        dry_run=dry_run,
    )
    response["resolution"] = resolved
    return response


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Run a deterministic TikOmni API task.")
    parser.add_argument("--intent", default="")
    parser.add_argument("--platform", default="")
    parser.add_argument("--capability", default="")
    parser.add_argument("--params", default="{}")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--allow-process-env", action="store_true")
    args = parser.parse_args(argv)
    try:
        payload = run_task(
            intent=args.intent,
            params=_parse_params(args.params),
            platform=args.platform,
            capability=args.capability,
            dry_run=bool(args.dry_run),
            allow_process_env=bool(args.allow_process_env),
        )
    except Exception as exc:
        payload = {"ok": False, "code": "RUNNER_EXCEPTION", "error_reason": str(exc)}
    _json_stdout(payload)
    return 0 if payload.get("ok") else 2


if __name__ == "__main__":
    sys.exit(main())
