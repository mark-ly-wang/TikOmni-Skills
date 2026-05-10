#!/usr/bin/env python3
"""Call TikOmni API by catalog endpoint_id."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
import urllib.parse
from typing import Any, Dict, List, Optional, Tuple

SKILL_ROOT = Path(__file__).resolve().parents[2]
if str(SKILL_ROOT) not in sys.path:
    sys.path.insert(0, str(SKILL_ROOT))

from scripts.core.api_catalog import load_operations, operation_by_endpoint_id
from scripts.core.tikomni_common import call_json_api, resolve_runtime

RESERVED_PARAM_KEYS = {"path", "method"}


def _json_stdout(payload: Dict[str, Any]) -> None:
    print(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True))


def _parse_params(raw_params: str) -> Dict[str, Any]:
    if not raw_params:
        return {}
    payload = json.loads(raw_params)
    if not isinstance(payload, dict):
        raise ValueError("params_must_be_json_object")
    return payload


def _schema_type(schema: Dict[str, Any]) -> str:
    raw_type = schema.get("type")
    if isinstance(raw_type, list):
        return "|".join(str(item) for item in raw_type)
    return str(raw_type or "")


def _validate_type(name: str, value: Any, schema: Dict[str, Any]) -> Optional[str]:
    schema_type = _schema_type(schema)
    if not schema_type:
        return None
    allowed = set(schema_type.split("|"))
    if "null" in allowed and value is None:
        return None
    if "string" in allowed and isinstance(value, str):
        return None
    if "integer" in allowed and isinstance(value, int) and not isinstance(value, bool):
        return None
    if "number" in allowed and isinstance(value, (int, float)) and not isinstance(value, bool):
        return None
    if "boolean" in allowed and isinstance(value, bool):
        return None
    if "array" in allowed and isinstance(value, list):
        return None
    if "object" in allowed and isinstance(value, dict):
        return None
    return f"invalid_type:{name}:expected_{schema_type or 'declared'}"


def _parameter_maps(operation: Dict[str, Any]) -> Tuple[Dict[str, Dict[str, Any]], Dict[str, Dict[str, Any]], Dict[str, Dict[str, Any]]]:
    path_params: Dict[str, Dict[str, Any]] = {}
    query_params: Dict[str, Dict[str, Any]] = {}
    header_params: Dict[str, Dict[str, Any]] = {}
    for param in operation.get("parameters") or []:
        if not isinstance(param, dict):
            continue
        name = str(param.get("name") or "")
        location = str(param.get("in") or "query")
        if not name:
            continue
        if location == "path":
            path_params[name] = param
        elif location == "header":
            header_params[name] = param
        else:
            query_params[name] = param
    return path_params, query_params, header_params


def _body_properties(operation: Dict[str, Any]) -> Tuple[Dict[str, Any], bool, bool]:
    body = operation.get("request_body") if isinstance(operation.get("request_body"), dict) else None
    if not body:
        return {}, False, False
    schema = body.get("schema") if isinstance(body.get("schema"), dict) else {}
    props = schema.get("properties") if isinstance(schema.get("properties"), dict) else {}
    return props, bool(body.get("required")), True


def _render_path(path: str, params: Dict[str, Any], path_params: Dict[str, Dict[str, Any]]) -> Tuple[str, List[str]]:
    missing: List[str] = []

    def replace(match: re.Match[str]) -> str:
        name = match.group(1)
        if name not in params or params.get(name) in (None, ""):
            missing.append(name)
            return match.group(0)
        return urllib.parse.quote(str(params[name]), safe="")

    rendered = re.sub(r"\{([^}]+)\}", replace, path)
    for name, param in path_params.items():
        if param.get("required") and (name not in params or params.get(name) in (None, "")):
            missing.append(name)
    return rendered, sorted(set(missing))


def build_request(operation: Dict[str, Any], params: Dict[str, Any]) -> Tuple[Optional[Dict[str, Any]], Optional[Dict[str, Any]]]:
    input_schema = operation.get("input_schema") if isinstance(operation.get("input_schema"), dict) else {}
    properties = input_schema.get("properties") if isinstance(input_schema.get("properties"), dict) else {}
    reserved = sorted(key for key in params.keys() if key in RESERVED_PARAM_KEYS and key not in properties)
    if reserved:
        return None, {"code": "RESERVED_PARAM_KEY", "message": f"Reserved API routing keys are not allowed in params: {', '.join(reserved)}"}

    required = set(str(item) for item in input_schema.get("required") or [])
    missing_required = sorted(name for name in required if name not in params or params.get(name) in (None, ""))
    if missing_required:
        return None, {"code": "MISSING_REQUIRED_PARAMS", "message": f"Missing required params: {', '.join(missing_required)}"}

    unknown = sorted(key for key in params.keys() if key not in properties)
    if unknown:
        return None, {"code": "UNKNOWN_PARAMS", "message": f"Unknown params for endpoint_id={operation.get('endpoint_id')}: {', '.join(unknown)}"}

    for name, value in params.items():
        schema = properties.get(name) if isinstance(properties.get(name), dict) else {}
        error = _validate_type(name, value, schema)
        if error:
            return None, {"code": "INVALID_PARAM_TYPE", "message": error}

    path_params, query_params, header_params = _parameter_maps(operation)
    path, missing_path = _render_path(str(operation.get("path") or ""), params, path_params)
    if missing_path:
        return None, {"code": "MISSING_PATH_PARAMS", "message": f"Missing path params: {', '.join(missing_path)}"}

    query = {name: params[name] for name in query_params.keys() if name in params}
    headers = {name: str(params[name]) for name in header_params.keys() if name in params}
    body_props, body_required, has_body = _body_properties(operation)
    body: Optional[Dict[str, Any]] = None
    if has_body:
        if body_props:
            body = {name: params[name] for name in body_props.keys() if name in params}
        elif "body" in params:
            raw_body = params["body"]
            if not isinstance(raw_body, dict):
                return None, {"code": "INVALID_PARAM_TYPE", "message": "invalid_type:body:expected_object"}
            body = raw_body
        elif body_required:
            return None, {"code": "MISSING_REQUIRED_PARAMS", "message": "Missing required params: body"}
        else:
            body = {}

    return {
        "method": str(operation.get("method") or "GET"),
        "path": path,
        "query": query,
        "headers": headers,
        "body": body,
    }, None


def call_endpoint(
    *,
    endpoint_id: str,
    params: Dict[str, Any],
    env_file: Optional[str] = None,
    base_url: Optional[str] = None,
    timeout_ms: Optional[int] = None,
    allow_process_env: bool = False,
    dry_run: bool = False,
) -> Dict[str, Any]:
    operations = load_operations()
    operation = operation_by_endpoint_id(operations, endpoint_id)
    if not operation:
        return {
            "ok": False,
            "code": "UNKNOWN_ENDPOINT_ID",
            "endpoint_id": endpoint_id,
            "error_reason": f"endpoint_id_not_found:{endpoint_id}",
        }

    request_plan, validation_error = build_request(operation, params)
    if validation_error:
        return {
            "ok": False,
            "code": validation_error["code"],
            "endpoint_id": endpoint_id,
            "platform": operation.get("platform"),
            "capability": operation.get("capability"),
            "variant": operation.get("variant"),
            "error_reason": validation_error["message"],
            "alternatives": operation.get("alternatives") or [],
        }

    if dry_run:
        return {
            "ok": True,
            "dry_run": True,
            "endpoint_id": endpoint_id,
            "platform": operation.get("platform"),
            "capability": operation.get("capability"),
            "variant": operation.get("variant"),
            "alternatives": operation.get("alternatives") or [],
            "request": request_plan,
        }

    runtime = resolve_runtime(
        env_file=env_file,
        api_key_env="TIKOMNI_API_KEY",
        base_url=base_url,
        timeout_ms=timeout_ms,
        allow_process_env=allow_process_env,
    )
    response = call_json_api(
        base_url=str(runtime["base_url"]),
        path=str(request_plan["path"]),
        token=str(runtime["token"]),
        method=str(request_plan["method"]),
        timeout_ms=int(runtime["timeout_ms"]),
        params=request_plan.get("query") if isinstance(request_plan.get("query"), dict) else None,
        body=request_plan.get("body") if isinstance(request_plan.get("body"), dict) else None,
        extra_headers=request_plan.get("headers") if isinstance(request_plan.get("headers"), dict) else None,
    )
    return {
        "ok": bool(response.get("ok")),
        "status_code": response.get("status_code"),
        "request_id": response.get("request_id"),
        "endpoint_id": endpoint_id,
        "platform": operation.get("platform"),
        "capability": operation.get("capability"),
        "variant": operation.get("variant"),
        "alternatives": operation.get("alternatives") or [],
        "error_reason": response.get("error_reason"),
        "data": response.get("data") if response.get("ok") else {},
    }


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Call TikOmni API by endpoint_id.")
    parser.add_argument("--endpoint-id", required=True)
    parser.add_argument("--params", default="{}")
    parser.add_argument("--env-file", default=None)
    parser.add_argument("--base-url", default=None)
    parser.add_argument("--timeout-ms", type=int, default=None)
    parser.add_argument("--allow-process-env", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)
    try:
        params = _parse_params(args.params)
        payload = call_endpoint(
            endpoint_id=args.endpoint_id,
            params=params,
            env_file=args.env_file,
            base_url=args.base_url,
            timeout_ms=args.timeout_ms,
            allow_process_env=bool(args.allow_process_env),
            dry_run=bool(args.dry_run),
        )
    except Exception as exc:
        payload = {"ok": False, "code": "CALLER_EXCEPTION", "error_reason": str(exc)}
    _json_stdout(payload)
    return 0 if payload.get("ok") else 2


if __name__ == "__main__":
    sys.exit(main())
