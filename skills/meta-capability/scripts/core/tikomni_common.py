#!/usr/bin/env python3
"""Minimal TikOmni auth and HTTP helpers for meta-capability."""

from __future__ import annotations

import json
import os
import re
import socket
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple

DEFAULT_BASE_URL = "https://api.tikomni.com"
DEFAULT_TIMEOUT_MS = 60000
DEFAULT_USER_AGENT = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
)
DEFAULT_GLOBAL_QPS = 5.0
DEFAULT_TIMEOUT_RETRY_MAX = 3
DEFAULT_TIMEOUT_RETRY_BACKOFF_MS = 300

_RATE_LIMIT_LOCK = threading.Lock()
_NEXT_ALLOWED_TS = 0.0


def _parse_env_file(env_file: Optional[str]) -> Dict[str, str]:
    if not env_file:
        return {}

    path = Path(env_file)
    if not path.exists() or not path.is_file():
        return {}

    parsed: Dict[str, str] = {}
    with path.open("r", encoding="utf-8") as handle:
        for raw_line in handle:
            line = raw_line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            if key:
                parsed[key] = value
    return parsed


def get_skills_root() -> Path:
    script_path = Path(__file__).resolve()
    return script_path.parents[3]


def get_repo_root() -> Path:
    return get_skills_root().parent


def _resolve_env_file_path(env_file: Optional[str]) -> Path:
    skills_root = get_skills_root()
    if not env_file:
        return (skills_root / ".env").resolve()

    candidate = Path(env_file).expanduser()
    if not candidate.is_absolute():
        candidate = skills_root / candidate
    return candidate.resolve()


def _infer_default_env_paths(primary_env_file: Optional[str]) -> Tuple[Path, Path]:
    script_path = Path(__file__).resolve()
    skill_root = script_path.parents[2]

    workspace_env = _resolve_env_file_path(primary_env_file)
    local_env = (skill_root / ".env.local").resolve()
    return workspace_env, local_env


def bootstrap_runtime_env(
    primary_env_file: Optional[str] = None,
    allow_process_env: bool = False,
) -> Dict[str, Any]:
    """Load env values from skills/.env and skill/.env.local."""

    process_env = dict(os.environ)
    workspace_env_path, local_env_path = _infer_default_env_paths(primary_env_file)

    base_values = _parse_env_file(str(workspace_env_path))
    local_values = _parse_env_file(str(local_env_path))

    merged: Dict[str, str] = {}
    merged.update(base_values)
    merged.update(local_values)
    if allow_process_env:
        merged.update(process_env)

    os.environ.update(merged)

    loaded_files: List[str] = []
    if workspace_env_path.exists():
        loaded_files.append(str(workspace_env_path))
    if local_env_path.exists():
        loaded_files.append(str(local_env_path))

    key_source: Dict[str, str] = {}
    priority = [".env.local", ".env"]
    if allow_process_env:
        priority.insert(0, "process_env")

    all_keys = set(base_values.keys()) | set(local_values.keys())
    if allow_process_env:
        all_keys |= set(process_env.keys())

    for key in all_keys:
        if allow_process_env and key in process_env:
            key_source[key] = "process_env"
        elif key in local_values:
            key_source[key] = ".env.local"
        elif key in base_values:
            key_source[key] = ".env"

    return {
        "skills_root": str(get_skills_root()),
        "repo_root": str(get_repo_root()),
        "workspace_env": str(workspace_env_path),
        "local_env": str(local_env_path),
        "loaded_files": loaded_files,
        "key_source": key_source,
        "priority": priority,
        "allow_process_env": bool(allow_process_env),
        "effective_env": merged,
    }


def resolve_runtime(
    env_file: Optional[str],
    api_key_env: str,
    base_url: Optional[str],
    timeout_ms: Optional[int],
    allow_process_env: bool = False,
) -> Dict[str, Any]:
    bootstrap_info = bootstrap_runtime_env(
        primary_env_file=env_file,
        allow_process_env=allow_process_env,
    )
    effective_env = bootstrap_info.get("effective_env", {}) if isinstance(bootstrap_info, dict) else {}

    token = str(effective_env.get(api_key_env, "") or "").strip()
    if not token and allow_process_env:
        token = os.getenv(api_key_env, "").strip()
    if not token:
        raise ValueError(
            f"missing_api_key:{api_key_env} (set in skills/.env or meta-capability/.env.local)"
        )

    resolved_base_url = str(base_url or effective_env.get("TIKOMNI_BASE_URL") or DEFAULT_BASE_URL).strip().rstrip("/")
    timeout_raw = timeout_ms if timeout_ms is not None else effective_env.get("TIKOMNI_TIMEOUT_MS")
    try:
        resolved_timeout_ms = int(timeout_raw or DEFAULT_TIMEOUT_MS)
    except Exception:
        resolved_timeout_ms = DEFAULT_TIMEOUT_MS

    return {
        "token": token,
        "base_url": resolved_base_url,
        "timeout_ms": resolved_timeout_ms,
        "env_bootstrap": {
            "loaded_files": bootstrap_info.get("loaded_files", []),
            "api_key_source": bootstrap_info.get("key_source", {}).get(api_key_env, "unknown"),
            "priority": bootstrap_info.get("priority", [".env.local", ".env"]),
            "allow_process_env": bool(allow_process_env),
        },
    }


def safe_json_loads(text: str) -> Any:
    try:
        return json.loads(text)
    except Exception:
        return {"_raw": text}


def normalize_text(value: Any) -> str:
    if value is None:
        return ""
    text = str(value)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def deep_find_first(payload: Any, keys: Iterable[str]) -> Optional[Any]:
    key_set = {str(key) for key in keys}

    def _walk(node: Any) -> Optional[Any]:
        if isinstance(node, dict):
            for key, value in node.items():
                if key in key_set and value not in (None, "", [], {}):
                    return value
            for value in node.values():
                hit = _walk(value)
                if hit not in (None, "", [], {}):
                    return hit
        elif isinstance(node, list):
            for item in node:
                hit = _walk(item)
                if hit not in (None, "", [], {}):
                    return hit
        return None

    return _walk(payload)


def extract_request_id(payload: Any) -> Optional[str]:
    value = deep_find_first(payload, ["request_id"])
    if value is None:
        return None
    return str(value)


def extract_error_reason(payload: Any, status_code: Optional[int] = None) -> str:
    if isinstance(payload, dict):
        error = payload.get("error")
        if isinstance(error, dict):
            code = error.get("code")
            message = error.get("message")
            if code:
                return str(code)
            if message:
                return normalize_text(str(message)) or "unknown_error"

        code = payload.get("code")
        if code not in (None, 0, 200, "0", "200", "SUCCESS", "success"):
            return str(code)

        message = payload.get("message")
        if isinstance(message, str) and message.strip() and message.strip().lower() not in {"ok", "success"}:
            return normalize_text(message)

    if status_code is not None:
        return f"http_{status_code}"
    return "unknown_error"


def _build_url(base_url: str, path: str, params: Optional[Dict[str, Any]]) -> str:
    normalized_path = str(path or "").strip()
    if not normalized_path.startswith("/"):
        normalized_path = f"/{normalized_path}"

    url = f"{base_url}{normalized_path}"
    if params:
        normalized: Dict[str, Any] = {}
        for key, value in params.items():
            if value is None:
                continue
            normalized[key] = value
        if normalized:
            url = f"{url}?{urllib.parse.urlencode(normalized, doseq=True)}"
    return url


def _resolve_global_qps() -> float:
    raw = str(os.getenv("TIKOMNI_GLOBAL_QPS", DEFAULT_GLOBAL_QPS)).strip()
    try:
        qps = float(raw)
    except Exception:
        qps = DEFAULT_GLOBAL_QPS
    return max(0.1, qps)


def _resolve_timeout_retry_max() -> int:
    raw = str(os.getenv("TIKOMNI_TIMEOUT_RETRY_MAX", DEFAULT_TIMEOUT_RETRY_MAX)).strip()
    try:
        retries = int(raw)
    except Exception:
        retries = DEFAULT_TIMEOUT_RETRY_MAX
    return max(0, min(retries, 8))


def _resolve_timeout_retry_backoff_ms() -> int:
    raw = str(os.getenv("TIKOMNI_TIMEOUT_RETRY_BACKOFF_MS", DEFAULT_TIMEOUT_RETRY_BACKOFF_MS)).strip()
    try:
        backoff = int(raw)
    except Exception:
        backoff = DEFAULT_TIMEOUT_RETRY_BACKOFF_MS
    return max(0, min(backoff, 5000))


def _wait_rate_limit_slot(qps: float) -> int:
    global _NEXT_ALLOWED_TS
    interval_sec = 1.0 / max(qps, 0.1)
    now = time.monotonic()
    with _RATE_LIMIT_LOCK:
        scheduled = max(now, _NEXT_ALLOWED_TS)
        wait_sec = max(0.0, scheduled - now)
        _NEXT_ALLOWED_TS = scheduled + interval_sec

    if wait_sec > 0:
        time.sleep(wait_sec)
    return int(wait_sec * 1000)


def _is_timeout_like_failure(status_code: Optional[int], error_reason: Optional[str]) -> bool:
    if isinstance(status_code, (int, float)) and int(status_code) in {408, 429, 502, 503, 504}:
        return True

    reason = str(error_reason or "").strip().upper()
    if not reason:
        return False
    timeout_tokens = ["TIMEOUT", "TIMED_OUT", "UPSTREAM_TIMEOUT", "DEADLINE_EXCEEDED"]
    return any(token in reason for token in timeout_tokens)


def _execute_json_request(request: urllib.request.Request, timeout_ms: int, url: str) -> Tuple[Dict[str, Any], bool]:
    status_code: Optional[int] = None
    raw_text = ""
    payload: Any = {}

    try:
        with urllib.request.urlopen(request, timeout=max(timeout_ms / 1000.0, 1.0)) as response:
            status_code = response.getcode()
            raw_text = response.read().decode("utf-8", errors="replace")
            payload = safe_json_loads(raw_text)
    except urllib.error.HTTPError as error:
        status_code = error.code
        raw_text = error.read().decode("utf-8", errors="replace")
        payload = safe_json_loads(raw_text)
    except urllib.error.URLError as error:
        reason_obj = getattr(error, "reason", error)
        reason_text = normalize_text(reason_obj)
        timeout_like = isinstance(reason_obj, socket.timeout) or "timeout" in reason_text.lower()
        error_reason = "network_error:timeout" if timeout_like else f"network_error:{reason_text or 'unknown'}"
        return {
            "ok": False,
            "status_code": None,
            "data": {},
            "request_id": None,
            "error_reason": error_reason,
            "raw_text": str(error),
            "url": url,
        }, timeout_like
    except (TimeoutError, socket.timeout) as error:
        return {
            "ok": False,
            "status_code": None,
            "data": {},
            "request_id": None,
            "error_reason": "network_error:timeout",
            "raw_text": str(error),
            "url": url,
        }, True

    request_id = extract_request_id(payload)
    ok = bool(status_code is not None and 200 <= status_code < 300)
    error_reason = None if ok else extract_error_reason(payload, status_code)
    timeout_like = _is_timeout_like_failure(status_code, error_reason)

    return {
        "ok": ok,
        "status_code": status_code,
        "data": payload,
        "request_id": request_id,
        "error_reason": error_reason,
        "raw_text": raw_text,
        "url": url,
    }, timeout_like


def call_json_api(
    *,
    base_url: str,
    path: str,
    token: str,
    method: str,
    timeout_ms: int,
    params: Optional[Dict[str, Any]] = None,
    body: Optional[Any] = None,
    extra_headers: Optional[Dict[str, str]] = None,
) -> Dict[str, Any]:
    url = _build_url(base_url, path, params)
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
        "Content-Type": "application/json",
        "User-Agent": os.getenv("TIKOMNI_HTTP_USER_AGENT", DEFAULT_USER_AGENT),
        "Accept-Language": os.getenv("TIKOMNI_HTTP_ACCEPT_LANGUAGE", "zh-CN,zh;q=0.9,en;q=0.8"),
    }
    if extra_headers:
        headers.update(extra_headers)

    data: Optional[bytes] = None
    if body is not None:
        data = json.dumps(body, ensure_ascii=False).encode("utf-8")

    request = urllib.request.Request(url=url, data=data, headers=headers, method=method.upper())

    qps = _resolve_global_qps()
    timeout_retry_max = _resolve_timeout_retry_max()
    retry_backoff_ms = _resolve_timeout_retry_backoff_ms()

    cumulative_wait_ms = 0
    last_result: Dict[str, Any] = {
        "ok": False,
        "status_code": None,
        "data": {},
        "request_id": None,
        "error_reason": "unknown_error",
        "raw_text": "",
        "url": url,
    }

    max_attempts = 1 + timeout_retry_max
    for attempt in range(1, max_attempts + 1):
        if attempt > 1 and retry_backoff_ms > 0:
            sleep_ms = retry_backoff_ms * (2 ** (attempt - 2))
            time.sleep(sleep_ms / 1000.0)

        cumulative_wait_ms += _wait_rate_limit_slot(qps)
        response, timeout_like = _execute_json_request(request=request, timeout_ms=timeout_ms, url=url)
        response["rate_limit_wait_ms"] = cumulative_wait_ms
        response["retry_attempt"] = max(0, attempt - 1)
        response["timeout_retry_max"] = timeout_retry_max

        if response.get("ok"):
            response["timeout_retry_exhausted"] = False
            return response

        last_result = response
        if timeout_like and attempt < max_attempts:
            continue

        response["timeout_retry_exhausted"] = bool(timeout_like and attempt >= max_attempts)
        return response

    last_result["timeout_retry_exhausted"] = True
    return last_result


def write_json_stdout(payload: Dict[str, Any]) -> None:
    print(json.dumps(payload, ensure_ascii=False, indent=2))
