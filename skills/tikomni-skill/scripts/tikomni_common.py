#!/usr/bin/env python3
"""Common helpers for local Tikomni Track A scripts."""

import json
import os
import re
import socket
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

TERMINAL_TASK_STATUS = {"SUCCEEDED", "FAILED", "CANCELED", "CANCELLED"}


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


def _infer_default_env_paths(primary_env_file: Optional[str]) -> Tuple[Path, Path]:
    script_path = Path(__file__).resolve()
    skill_root = script_path.parents[1]

    workspace_env = Path(primary_env_file).expanduser().resolve() if primary_env_file else (Path.cwd() / ".env").resolve()
    local_env = (skill_root / ".env.local").resolve()
    return workspace_env, local_env


def bootstrap_runtime_env(primary_env_file: Optional[str] = None) -> Dict[str, Any]:
    """Load env values from .env + .env.local with deterministic priority.

    Priority (highest -> lowest): process env > .env.local > .env
    """

    process_env = dict(os.environ)
    workspace_env_path, local_env_path = _infer_default_env_paths(primary_env_file)

    base_values = _parse_env_file(str(workspace_env_path))
    local_values = _parse_env_file(str(local_env_path))

    merged: Dict[str, str] = {}
    merged.update(base_values)
    merged.update(local_values)
    merged.update(process_env)

    os.environ.update(merged)

    loaded_files: List[str] = []
    if workspace_env_path.exists():
        loaded_files.append(str(workspace_env_path))
    if local_env_path.exists():
        loaded_files.append(str(local_env_path))

    key_source: Dict[str, str] = {}
    for key in set(base_values.keys()) | set(local_values.keys()) | set(process_env.keys()):
        if key in process_env:
            key_source[key] = "process_env"
        elif key in local_values:
            key_source[key] = ".env.local"
        elif key in base_values:
            key_source[key] = ".env"

    return {
        "workspace_env": str(workspace_env_path),
        "local_env": str(local_env_path),
        "loaded_files": loaded_files,
        "key_source": key_source,
        "priority": ["process_env", ".env.local", ".env"],
    }


def load_env_file(env_file: Optional[str]) -> None:
    """Backward-compatible wrapper. Prefer bootstrap_runtime_env."""
    bootstrap_runtime_env(primary_env_file=env_file)


def resolve_runtime(
    env_file: Optional[str],
    api_key_env: str,
    base_url: Optional[str],
    timeout_ms: Optional[int],
) -> Dict[str, Any]:
    bootstrap_info = bootstrap_runtime_env(primary_env_file=env_file)

    token = os.getenv(api_key_env, "").strip()
    if not token:
        raise ValueError(f"missing_api_key:{api_key_env}")

    resolved_base_url = (base_url or os.getenv("TIKOMNI_BASE_URL") or DEFAULT_BASE_URL).strip().rstrip("/")
    resolved_timeout_ms = int(timeout_ms or os.getenv("TIKOMNI_TIMEOUT_MS") or DEFAULT_TIMEOUT_MS)

    return {
        "token": token,
        "base_url": resolved_base_url,
        "timeout_ms": resolved_timeout_ms,
        "env_bootstrap": {
            "loaded_files": bootstrap_info.get("loaded_files", []),
            "api_key_source": bootstrap_info.get("key_source", {}).get(api_key_env, "unknown"),
            "priority": bootstrap_info.get("priority", ["process_env", ".env.local", ".env"]),
        },
    }


def safe_json_loads(text: str) -> Any:
    try:
        return json.loads(text)
    except Exception:
        return {"_raw": text}


def _build_url(base_url: str, path: str, params: Optional[Dict[str, Any]]) -> str:
    url = f"{base_url}{path}"
    if params:
        normalized = {}
        for key, value in params.items():
            if value is None:
                continue
            normalized[key] = value
        if normalized:
            url = f"{url}?{urllib.parse.urlencode(normalized)}"
    return url


def call_json_api(
    *,
    base_url: str,
    path: str,
    token: str,
    method: str,
    timeout_ms: int,
    params: Optional[Dict[str, Any]] = None,
    body: Optional[Dict[str, Any]] = None,
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
        return {
            "ok": False,
            "status_code": None,
            "data": {},
            "request_id": None,
            "error_reason": f"network_error:{error.reason}",
            "raw_text": str(error),
            "url": url,
        }
    except (TimeoutError, socket.timeout) as error:
        return {
            "ok": False,
            "status_code": None,
            "data": {},
            "request_id": None,
            "error_reason": "network_error:timeout",
            "raw_text": str(error),
            "url": url,
        }

    request_id = extract_request_id(payload)
    ok = bool(status_code is not None and 200 <= status_code < 300)
    error_reason = None if ok else extract_error_reason(payload, status_code)

    return {
        "ok": ok,
        "status_code": status_code,
        "data": payload,
        "request_id": request_id,
        "error_reason": error_reason,
        "raw_text": raw_text,
        "url": url,
    }


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


def deep_find_all(payload: Any, keys: Iterable[str]) -> List[Any]:
    key_set = {str(key) for key in keys}
    results: List[Any] = []

    def _walk(node: Any) -> None:
        if isinstance(node, dict):
            for key, value in node.items():
                if key in key_set and value not in (None, "", [], {}):
                    results.append(value)
                _walk(value)
        elif isinstance(node, list):
            for item in node:
                _walk(item)

    _walk(payload)
    return results


def deep_collect_strings(payload: Any, max_items: int = 20) -> List[str]:
    results: List[str] = []

    def _walk(node: Any) -> None:
        if len(results) >= max_items:
            return
        if isinstance(node, str):
            text = normalize_text(node)
            if text:
                results.append(text)
        elif isinstance(node, dict):
            for value in node.values():
                _walk(value)
        elif isinstance(node, list):
            for item in node:
                _walk(item)

    _walk(payload)
    return results


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


def normalize_text(value: Any) -> str:
    if value is None:
        return ""
    text = str(value)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def extract_task_id(payload: Any) -> Optional[str]:
    task_id = deep_find_first(payload, ["task_id", "id"])
    if task_id is None:
        return None
    return str(task_id)


def extract_task_status(payload: Any) -> str:
    status = deep_find_first(payload, ["status", "task_status", "state"])
    if status is None:
        return ""
    return normalize_text(status).upper()


def is_terminal_status(status: str) -> bool:
    return status.upper() in TERMINAL_TASK_STATUS


def extract_transcript_text(payload: Any) -> str:
    candidates = deep_find_all(
        payload,
        [
            "text",
            "transcript",
            "transcription",
            "content",
            "raw_content",
            "result",
            "sentence",
            "paragraph",
        ],
    )

    texts: List[str] = []
    for candidate in candidates:
        if isinstance(candidate, str):
            cleaned = normalize_text(candidate)
            if cleaned:
                texts.append(cleaned)
        elif isinstance(candidate, list):
            for item in candidate:
                if isinstance(item, str):
                    cleaned = normalize_text(item)
                    if cleaned:
                        texts.append(cleaned)
                elif isinstance(item, dict):
                    maybe = deep_find_first(item, ["text", "sentence", "content"])
                    if isinstance(maybe, str):
                        cleaned = normalize_text(maybe)
                        if cleaned:
                            texts.append(cleaned)

    merged = "\n".join(dict.fromkeys(texts))
    return merged.strip()


def summarize_content(raw_content: str, source: str) -> Dict[str, Any]:
    clean = normalize_text(raw_content)
    if not clean:
        return {
            "summary": "",
            "insights": [
                f"source={source}",
                "no_text_extracted",
            ],
        }

    clipped = clean[:180]
    if len(clean) > 180:
        clipped = f"{clipped}..."

    insights = [
        f"source={source}",
        f"char_len={len(clean)}",
    ]
    return {
        "summary": clipped,
        "insights": insights,
    }


def read_json_file(path: str) -> Dict[str, Any]:
    with open(path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def write_json_stdout(payload: Dict[str, Any]) -> None:
    print(json.dumps(payload, ensure_ascii=False, indent=2))
