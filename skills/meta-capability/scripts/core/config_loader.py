#!/usr/bin/env python3
"""Minimal config loader for meta-capability runtime."""

from __future__ import annotations

import os
from pathlib import Path
from typing import Any, Dict, Optional, Tuple

from scripts.core.tikomni_common import bootstrap_runtime_env

try:
    import yaml
except Exception:  # pragma: no cover
    yaml = None

SKILL_ROOT = Path(__file__).resolve().parents[2]
REPO_ROOT = SKILL_ROOT.parents[1]
DEFAULT_CONFIG_PATH = SKILL_ROOT / "references" / "config-templates" / "defaults.yaml"

BUILTIN_DEFAULT_CONFIG: Dict[str, Any] = {
    "schema_version": "v1",
    "profile": "default",
    "runtime": {
        "base_url": "https://api.tikomni.com",
        "auth_env_key": "TIKOMNI_API_KEY",
        "timeout_ms": 60000,
    },
}


def _deep_clone(value: Any) -> Any:
    if isinstance(value, dict):
        return {k: _deep_clone(v) for k, v in value.items()}
    if isinstance(value, list):
        return [_deep_clone(item) for item in value]
    return value


def _deep_merge(defaults: Dict[str, Any], override: Dict[str, Any]) -> Dict[str, Any]:
    merged = _deep_clone(defaults)
    for key, value in override.items():
        if isinstance(merged.get(key), dict) and isinstance(value, dict):
            merged[key] = _deep_merge(merged[key], value)
        else:
            merged[key] = _deep_clone(value)
    return merged


def _resolve_repo_anchored_path(path_value: str) -> str:
    candidate = Path(path_value).expanduser()
    if not candidate.is_absolute():
        candidate = REPO_ROOT / candidate
    return str(candidate.resolve())


def resolve_config_path(cli_config_path: Optional[str] = None, env_values: Optional[Dict[str, str]] = None) -> str:
    if cli_config_path and str(cli_config_path).strip():
        return _resolve_repo_anchored_path(str(cli_config_path).strip())

    raw_env_path = ""
    if isinstance(env_values, dict):
        raw_env_path = str(env_values.get("TIKOMNI_CONFIG_FILE", "")).strip()
    if not raw_env_path:
        raw_env_path = os.getenv("TIKOMNI_CONFIG_FILE", "").strip()

    if raw_env_path:
        return _resolve_repo_anchored_path(raw_env_path)

    return str(DEFAULT_CONFIG_PATH)


def _load_yaml(path: str) -> Dict[str, Any]:
    if yaml is None:
        raise RuntimeError("PyYAML unavailable")

    with open(path, "r", encoding="utf-8") as handle:
        payload = yaml.safe_load(handle) or {}
    if not isinstance(payload, dict):
        raise ValueError(f"config_root_must_be_mapping:{path}")
    return payload


def _builtin_defaults() -> Dict[str, Any]:
    return _deep_clone(BUILTIN_DEFAULT_CONFIG)


def _read_env(name: str, env_values: Optional[Dict[str, str]] = None) -> str:
    if isinstance(env_values, dict) and name in env_values:
        return str(env_values.get(name, "") or "").strip()
    return os.getenv(name, "").strip()


def _env_int(name: str, env_values: Optional[Dict[str, str]] = None) -> Optional[int]:
    raw = _read_env(name, env_values=env_values)
    if not raw:
        return None
    try:
        value = int(raw)
    except Exception:
        return None
    return value if value > 0 else None


def _env_text(name: str, env_values: Optional[Dict[str, str]] = None) -> Optional[str]:
    value = _read_env(name, env_values=env_values)
    return value or None


def apply_env_overrides(config: Dict[str, Any], env_values: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
    runtime = config.setdefault("runtime", {}) if isinstance(config.get("runtime"), dict) else {}
    config["runtime"] = runtime

    base_url = _env_text("TIKOMNI_BASE_URL", env_values=env_values)
    if base_url is not None:
        runtime["base_url"] = base_url.rstrip("/")

    timeout_ms = _env_int("TIKOMNI_TIMEOUT_MS", env_values=env_values)
    if timeout_ms is not None:
        runtime["timeout_ms"] = timeout_ms

    auth_env_key = _env_text("TIKOMNI_AUTH_ENV_KEY", env_values=env_values)
    if auth_env_key is not None:
        runtime["auth_env_key"] = auth_env_key

    return config


def load_tikomni_config(
    cli_config_path: Optional[str] = None,
    env_file: Optional[str] = None,
    allow_process_env: bool = False,
) -> Tuple[Dict[str, Any], str]:
    bootstrap = bootstrap_runtime_env(
        primary_env_file=env_file,
        allow_process_env=allow_process_env,
    )
    env_values = bootstrap.get("effective_env", {}) if isinstance(bootstrap, dict) else {}

    explicit_config_requested = bool(
        (cli_config_path and str(cli_config_path).strip())
        or (isinstance(env_values, dict) and str(env_values.get("TIKOMNI_CONFIG_FILE", "")).strip())
    )
    path = resolve_config_path(cli_config_path, env_values=env_values if isinstance(env_values, dict) else None)

    if yaml is None:
        if explicit_config_requested:
            raise RuntimeError(f"config_yaml_unavailable:{path}")
        return apply_env_overrides(_builtin_defaults(), env_values=env_values), "builtin-defaults"

    try:
        loaded = _load_yaml(path)
    except Exception:
        if explicit_config_requested:
            raise
        return apply_env_overrides(_builtin_defaults(), env_values=env_values), "builtin-defaults"

    merged = _deep_merge(_builtin_defaults(), loaded)
    return apply_env_overrides(merged, env_values=env_values), path


def config_get(config: Dict[str, Any], dotted_key: str, default: Any = None) -> Any:
    current: Any = config
    for key in dotted_key.split("."):
        if not isinstance(current, dict) or key not in current:
            return default
        current = current[key]
    return current


def resolve_runtime_settings(
    config: Dict[str, Any],
    cli_base_url: Optional[str] = None,
    cli_timeout_ms: Optional[int] = None,
    cli_api_key_env: Optional[str] = None,
) -> Dict[str, Any]:
    runtime_config = config_get(config, "runtime", {})
    runtime_config = runtime_config if isinstance(runtime_config, dict) else {}

    base_url = str(
        cli_base_url or runtime_config.get("base_url") or BUILTIN_DEFAULT_CONFIG["runtime"]["base_url"]
    ).strip().rstrip("/")

    raw_timeout = (
        cli_timeout_ms
        if cli_timeout_ms is not None
        else runtime_config.get("timeout_ms", BUILTIN_DEFAULT_CONFIG["runtime"]["timeout_ms"])
    )
    try:
        timeout_ms = int(raw_timeout)
    except Exception:
        timeout_ms = int(BUILTIN_DEFAULT_CONFIG["runtime"]["timeout_ms"])

    api_key_env = str(
        cli_api_key_env or runtime_config.get("auth_env_key") or BUILTIN_DEFAULT_CONFIG["runtime"]["auth_env_key"]
    ).strip()
    if not api_key_env:
        api_key_env = str(BUILTIN_DEFAULT_CONFIG["runtime"]["auth_env_key"])

    return {
        "base_url": base_url,
        "timeout_ms": timeout_ms,
        "api_key_env": api_key_env,
    }
