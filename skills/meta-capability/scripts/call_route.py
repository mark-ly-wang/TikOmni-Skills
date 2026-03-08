#!/usr/bin/env python3

if __package__ in {None, ""}:
    import sys
    from pathlib import Path

    _self = Path(__file__).resolve()
    for _parent in _self.parents:
        if (_parent / "scripts" / "core" / "bootstrap_env.py").is_file():
            sys.path.insert(0, str(_parent))
            break

"""Call any TikOmni route with Authorization for meta-capability."""

from scripts.core.bootstrap_env import bootstrap_for_direct_run

bootstrap_for_direct_run(__file__, __package__)

import argparse
import json
from typing import Any, Dict, Optional

from scripts.core.config_loader import load_tikomni_config, resolve_runtime_settings
from scripts.core.tikomni_common import call_json_api, resolve_runtime, write_json_stdout


def _parse_json_arg(name: str, raw_value: Optional[str]) -> Optional[Any]:
    if raw_value is None or not str(raw_value).strip():
        return None
    try:
        return json.loads(raw_value)
    except Exception as error:
        raise ValueError(f"invalid_json:{name}") from error


def _require_mapping(name: str, payload: Optional[Any]) -> Optional[Dict[str, Any]]:
    if payload is None:
        return None
    if not isinstance(payload, dict):
        raise ValueError(f"{name}_must_be_json_object")
    return payload


def _normalize_headers(payload: Optional[Any]) -> Optional[Dict[str, str]]:
    mapping = _require_mapping("headers", payload)
    if mapping is None:
        return None
    normalized: Dict[str, str] = {}
    for key, value in mapping.items():
        normalized[str(key)] = str(value)
    return normalized


def main() -> None:
    parser = argparse.ArgumentParser(description="Call a TikOmni route with meta-capability auth")
    parser.add_argument("method", help="HTTP method, for example GET or POST")
    parser.add_argument("path", help="Route path, for example /api/u1/v1/health/check")
    parser.add_argument("--params-json", default=None, help='JSON object for query params, for example {"id":"123"}')
    parser.add_argument("--body-json", default=None, help='JSON payload for request body')
    parser.add_argument(
        "--headers-json",
        default=None,
        help='Optional extra headers JSON, for example {"X-Debug":"1"}',
    )
    parser.add_argument("--config", default=None, help="Optional YAML config path")
    parser.add_argument("--env-file", default=None, help="Optional env file path under skills root")
    parser.add_argument("--api-key-env", default=None, help="Optional API key env variable name override")
    parser.add_argument("--base-url", default=None, help="Optional TikOmni API base URL override")
    parser.add_argument("--timeout-ms", type=int, default=None, help="Optional timeout override in milliseconds")
    parser.add_argument("--allow-process-env", action="store_true", help="Allow process env to override env files")
    args = parser.parse_args()

    try:
        params = _require_mapping("params", _parse_json_arg("params", args.params_json))
        body = _parse_json_arg("body", args.body_json)
        extra_headers = _normalize_headers(_parse_json_arg("headers", args.headers_json))

        config, config_path = load_tikomni_config(
            cli_config_path=args.config,
            env_file=args.env_file,
            allow_process_env=args.allow_process_env,
        )
        runtime_settings = resolve_runtime_settings(
            config=config,
            cli_base_url=args.base_url,
            cli_timeout_ms=args.timeout_ms,
            cli_api_key_env=args.api_key_env,
        )
        runtime = resolve_runtime(
            env_file=args.env_file,
            api_key_env=runtime_settings["api_key_env"],
            base_url=runtime_settings["base_url"],
            timeout_ms=runtime_settings["timeout_ms"],
            allow_process_env=args.allow_process_env,
        )
    except Exception as error:
        write_json_stdout(
            {
                "ok": False,
                "method": args.method.upper(),
                "path": args.path,
                "error_reason": str(error),
                "request_id": None,
            }
        )
        raise SystemExit(2) from error

    result = call_json_api(
        base_url=runtime["base_url"],
        path=args.path,
        token=runtime["token"],
        method=args.method.upper(),
        timeout_ms=runtime["timeout_ms"],
        params=params,
        body=body,
        extra_headers=extra_headers,
    )

    write_json_stdout(
        {
            "ok": result["ok"],
            "method": args.method.upper(),
            "path": args.path,
            "base_url": runtime["base_url"],
            "params": params,
            "body": body,
            "extra_headers": extra_headers,
            "status_code": result.get("status_code"),
            "request_id": result.get("request_id"),
            "error_reason": result.get("error_reason"),
            "auth_env_key": runtime_settings["api_key_env"],
            "config_path": config_path,
            "env_bootstrap": runtime.get("env_bootstrap", {}),
            "data": result.get("data", {}),
        }
    )
    raise SystemExit(0 if result["ok"] else 1)


if __name__ == "__main__":
    main()
