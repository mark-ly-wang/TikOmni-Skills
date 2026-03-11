#!/usr/bin/env python3
"""Config loader for social-media-crawl."""

from __future__ import annotations

import os
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

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
        "mcp_url": "https://mcp.tikomni.com/mcp",
        "auth_env_key": "TIKOMNI_API_KEY",
        "timeout_ms": 60000,
        "u2_pending_timeout_sec": 60,
    },
    "storage_routes": {
        "default": {
            "root_dir": "",
            "card_root": "",
            "runs_dir": "_runs",
            "results_dir": "results",
            "errors_dir": "_errors",
        },
        "content_kind_card_type": {
            "single_video": "work",
            "note": "work",
            "work": "work",
            "author_home": "work",
            "work_collection": "work",
        },
        "card_type_routes": {
            "work": {
                "prefix": "CBV",
                "parts": ["内容系统", "作品库", "{platform}-{author_slug}"],
            }
        },
    },
    "naming_rules": {
        "card_filename_pattern": "{identifier}{ext}",
        "json_filename_pattern": "{timestamp}-{platform}-{identifier}{ext}",
    },
    "asr_strategy": {
        "poll_interval_sec": 3.0,
        "max_polls": 30,
        "submit_retry": {
            "douyin_video": {"max_retries": 2, "backoff_ms": 1500},
            "xiaohongshu_note": {"max_retries": 0, "backoff_ms": 0},
        },
        "u2_timeout_retry": {
            "enabled": True,
            "max_retries": 0,
        },
    },
}

LOCALE_ROUTE_PRESETS: Dict[str, Dict[str, Dict[str, Any]]] = {
    "zh": {
        "work": {
            "prefix": "CBV",
            "parts": ["内容系统", "作品库", "{platform}-{author_slug}"],
        }
    },
    "en": {
        "work": {
            "prefix": "CBV",
            "parts": ["content-system", "work-library", "{platform}-{author_slug}"],
        }
    },
}

CARD_ROUTE_ENV_KEYS: Dict[str, List[str]] = {
    "work": ["TIKOMNI_CARD_ROUTE_WORK", "TIKOMNI_CARD_ROUTE_AUTHOR_SAMPLE_WORK"],
}

CARD_PREFIX_ENV_KEYS: Dict[str, List[str]] = {
    "work": ["TIKOMNI_CARD_PREFIX_WORK", "TIKOMNI_CARD_PREFIX_AUTHOR_SAMPLE_WORK"],
}


def _deep_clone(value: Any) -> Any:
    if isinstance(value, dict):
        return {key: _deep_clone(item) for key, item in value.items()}
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


def _builtin_defaults() -> Dict[str, Any]:
    return _deep_clone(BUILTIN_DEFAULT_CONFIG)


def _resolve_repo_anchored_path(path_value: str) -> str:
    candidate = Path(path_value).expanduser()
    if not candidate.is_absolute():
        candidate = REPO_ROOT / candidate
    return str(candidate.resolve())


def _load_yaml(path: str) -> Dict[str, Any]:
    if yaml is None:
        raise RuntimeError("PyYAML unavailable")
    with open(path, "r", encoding="utf-8") as handle:
        payload = yaml.safe_load(handle) or {}
    if not isinstance(payload, dict):
        raise ValueError(f"config_root_must_be_mapping:{path}")
    return payload


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


def _read_env(name: str, env_values: Optional[Dict[str, str]] = None) -> str:
    if isinstance(env_values, dict) and name in env_values:
        return str(env_values.get(name, "") or "").strip()
    return os.getenv(name, "").strip()


def _env_text(name: str, env_values: Optional[Dict[str, str]] = None) -> Optional[str]:
    value = _read_env(name, env_values=env_values)
    return value or None


def _env_int(name: str, env_values: Optional[Dict[str, str]] = None) -> Optional[int]:
    raw = _read_env(name, env_values=env_values)
    if not raw:
        return None
    try:
        value = int(raw)
    except Exception:
        return None
    return value


def _require_absolute_path(path_value: str, env_key: str) -> str:
    candidate = Path(path_value).expanduser()
    if not candidate.is_absolute():
        raise ValueError(f"{env_key} must be an absolute path")
    return str(candidate.resolve())


def _require_absolute_env(name: str, env_values: Optional[Dict[str, str]] = None) -> str:
    value = _env_text(name, env_values=env_values)
    if value is None:
        raise ValueError(f"{name} is required and must be an absolute path")
    return _require_absolute_path(value, name)


def _route_from_env(value: str) -> Optional[List[str]]:
    parts = [item.strip() for item in value.split("|")]
    cleaned = [item for item in parts if item]
    return cleaned if cleaned else None


def _normalize_path_locale(raw_value: Optional[str]) -> str:
    value = (raw_value or "").strip().lower()
    if value in LOCALE_ROUTE_PRESETS:
        return value
    return "zh"


def resolve_storage_paths(config: Dict[str, Any]) -> Dict[str, str]:
    default_route = config_get(config, "storage_routes.default", {})
    default_route = default_route if isinstance(default_route, dict) else {}

    root_dir = Path(_require_absolute_path(str(default_route.get("root_dir") or ""), "TIKOMNI_OUTPUT_ROOT"))
    card_root = Path(_require_absolute_path(str(default_route.get("card_root") or ""), "TIKOMNI_CARD_ROOT"))

    resolved: Dict[str, str] = {
        "root_dir": str(root_dir),
        "card_root": str(card_root),
    }

    for key in ("runs_dir", "results_dir", "errors_dir"):
        raw_value = str(default_route.get(key) or "").strip() or {
            "runs_dir": "_runs",
            "results_dir": "results",
            "errors_dir": "_errors",
        }[key]
        part = Path(raw_value).expanduser()
        resolved[key] = str(part.resolve()) if part.is_absolute() else str((root_dir / part).resolve())

    resolved["runs_root"] = resolved["runs_dir"]
    resolved["results_root"] = resolved["results_dir"]
    resolved["errors_root"] = resolved["errors_dir"]
    return resolved


def apply_env_overrides(config: Dict[str, Any], env_values: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
    runtime = config.setdefault("runtime", {}) if isinstance(config.get("runtime"), dict) else {}
    config["runtime"] = runtime

    storage_routes = config.setdefault("storage_routes", {}) if isinstance(config.get("storage_routes"), dict) else {}
    config["storage_routes"] = storage_routes
    default_route = storage_routes.setdefault("default", {}) if isinstance(storage_routes.get("default"), dict) else {}
    storage_routes["default"] = default_route
    card_type_routes = (
        storage_routes.setdefault("card_type_routes", {}) if isinstance(storage_routes.get("card_type_routes"), dict) else {}
    )
    storage_routes["card_type_routes"] = card_type_routes

    naming_rules = config.setdefault("naming_rules", {}) if isinstance(config.get("naming_rules"), dict) else {}
    config["naming_rules"] = naming_rules
    asr_strategy = config.setdefault("asr_strategy", {}) if isinstance(config.get("asr_strategy"), dict) else {}
    config["asr_strategy"] = asr_strategy

    auth_env_key = _env_text("TIKOMNI_AUTH_ENV_KEY", env_values=env_values)
    if auth_env_key is not None:
        runtime["auth_env_key"] = auth_env_key

    for env_key, config_key in {
        "TIKOMNI_BASE_URL": "base_url",
        "TIKOMNI_MCP_URL": "mcp_url",
    }.items():
        value = _env_text(env_key, env_values=env_values)
        if value is not None:
            runtime[config_key] = value.rstrip("/")

    timeout_ms = _env_int("TIKOMNI_TIMEOUT_MS", env_values=env_values)
    if timeout_ms is not None:
        runtime["timeout_ms"] = timeout_ms

    pending_timeout_sec = _env_int("TIKOMNI_U2_PENDING_TIMEOUT_SEC", env_values=env_values)
    if pending_timeout_sec is not None and pending_timeout_sec > 0:
        runtime["u2_pending_timeout_sec"] = pending_timeout_sec

    default_route["root_dir"] = _require_absolute_env("TIKOMNI_OUTPUT_ROOT", env_values=env_values)
    default_route["card_root"] = _require_absolute_env("TIKOMNI_CARD_ROOT", env_values=env_values)

    for env_key, config_key in {
        "TIKOMNI_OUTPUT_RUNS_DIR": "runs_dir",
        "TIKOMNI_OUTPUT_RESULTS_DIR": "results_dir",
        "TIKOMNI_OUTPUT_ERRORS_DIR": "errors_dir",
    }.items():
        value = _env_text(env_key, env_values=env_values)
        if value is not None:
            default_route[config_key] = value

    card_filename_pattern = _env_text("TIKOMNI_FILENAME_PATTERN_CARD", env_values=env_values)
    json_filename_pattern = _env_text("TIKOMNI_FILENAME_PATTERN_JSON", env_values=env_values)
    if card_filename_pattern is not None:
        naming_rules["card_filename_pattern"] = card_filename_pattern
    if json_filename_pattern is not None:
        naming_rules["json_filename_pattern"] = json_filename_pattern

    poll_interval_sec = _env_int("TIKOMNI_POLL_INTERVAL_SEC", env_values=env_values)
    if poll_interval_sec is not None and poll_interval_sec > 0:
        asr_strategy["poll_interval_sec"] = float(poll_interval_sec)

    path_locale = _normalize_path_locale(_read_env("TIKOMNI_PATH_LOCALE", env_values=env_values) or "zh")
    locale_routes = LOCALE_ROUTE_PRESETS.get(path_locale, LOCALE_ROUTE_PRESETS["zh"])
    for route_key, route_value in locale_routes.items():
        card_type_routes[route_key] = {
            "prefix": str(route_value.get("prefix") or "CBV"),
            "parts": list(route_value.get("parts") or []),
        }

    for route_key, env_names in CARD_ROUTE_ENV_KEYS.items():
        for env_name in env_names:
            raw_value = _env_text(env_name, env_values=env_values)
            if raw_value is None:
                continue
            env_parts = _route_from_env(raw_value)
            if not env_parts:
                continue
            current = card_type_routes.get(route_key) if isinstance(card_type_routes.get(route_key), dict) else {}
            prefix = str(current.get("prefix") or LOCALE_ROUTE_PRESETS["zh"][route_key]["prefix"])
            card_type_routes[route_key] = {"prefix": prefix, "parts": env_parts}
            break

    for route_key, env_names in CARD_PREFIX_ENV_KEYS.items():
        for env_name in env_names:
            prefix_value = _env_text(env_name, env_values=env_values)
            if prefix_value is None:
                continue
            current = card_type_routes.get(route_key) if isinstance(card_type_routes.get(route_key), dict) else {}
            parts = current.get("parts") if isinstance(current.get("parts"), list) else list(LOCALE_ROUTE_PRESETS["zh"][route_key]["parts"])
            card_type_routes[route_key] = {"prefix": prefix_value, "parts": parts}
            break

    resolved_storage = resolve_storage_paths(config)
    for key, value in resolved_storage.items():
        default_route[key] = value
    return config


def load_tikomni_config(
    cli_config_path: Optional[str] = None,
    env_file: Optional[str] = None,
    allow_process_env: bool = False,
) -> Tuple[Dict[str, Any], str]:
    bootstrap = bootstrap_runtime_env(primary_env_file=env_file, allow_process_env=allow_process_env)
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
