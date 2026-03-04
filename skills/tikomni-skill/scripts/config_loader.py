#!/usr/bin/env python3
"""Lightweight config loader for Tikomni scripts (Phase 1 skeleton)."""

from __future__ import annotations

import os
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

try:
    import yaml
except Exception:  # pragma: no cover - defensive fallback
    yaml = None

SKILL_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = SKILL_ROOT.parents[1]
DEFAULT_OUTPUT_ROOT_NAME = "tikomni-output"
DEFAULT_CONFIG_PATH = SKILL_ROOT / "references" / "config-templates" / "defaults.yaml"

BUILTIN_DEFAULT_CONFIG: Dict[str, Any] = {
    "schema_version": "v1",
    "profile": "default",
    "runtime": {
        "base_url": "https://api.tikomni.com",
        "auth_env_key": "TIKOMNI_API_KEY",
        "timeout_ms": 60000,
    },
    "storage_routes": {
        "default": {
            "root_dir": DEFAULT_OUTPUT_ROOT_NAME,
            "runs_dir": "_runs",
            "results_dir": "results",
            "errors_dir": "_errors",
        },
        "content_kind_card_type": {
            "single_video": "work",
            "work": "work",
            "author_home": "author_sample_work",
            "author_sample_work": "author_sample_work",
            "author_analysis": "author",
        },
        "card_type_routes": {
            "work": {
                "prefix": "CBV",
                "parts": ["10-内容系统", "15-对标研究", "01-作品对标卡"],
            },
            "author": {
                "prefix": "CBA",
                "parts": ["10-内容系统", "15-对标研究", "03-作者对标卡"],
            },
            "author_sample_work": {
                "prefix": "CBV",
                "parts": ["10-内容系统", "15-对标研究", "02-作者样本集", "{platform}-{author_slug}"],
            },
            "material": {
                "prefix": "CMAT",
                "parts": ["10-内容系统", "12-素材库", "素材卡", "{year}", "{year_month}"],
            },
        },
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
            "max_retries": 3,
        },
    },
}

LOCALE_ROUTE_PRESETS: Dict[str, Dict[str, Dict[str, Any]]] = {
    "zh": {
        "work": {
            "prefix": "CBV",
            "parts": ["10-内容系统", "15-对标研究", "01-作品对标卡"],
        },
        "author": {
            "prefix": "CBA",
            "parts": ["10-内容系统", "15-对标研究", "03-作者对标卡"],
        },
        "author_sample_work": {
            "prefix": "CBV",
            "parts": ["10-内容系统", "15-对标研究", "02-作者样本集", "{platform}-{author_slug}"],
        },
        "material": {
            "prefix": "CMAT",
            "parts": ["10-内容系统", "12-素材库", "素材卡", "{year}", "{year_month}"],
        },
    },
    "en": {
        "work": {
            "prefix": "CBV",
            "parts": ["10-content-system", "15-benchmark-research", "01-work-benchmark-cards"],
        },
        "author": {
            "prefix": "CBA",
            "parts": ["10-content-system", "15-benchmark-research", "03-author-benchmark-cards"],
        },
        "author_sample_work": {
            "prefix": "CBV",
            "parts": [
                "10-content-system",
                "15-benchmark-research",
                "02-author-sample-works",
                "{platform}-{author_slug}",
            ],
        },
        "material": {
            "prefix": "CMAT",
            "parts": ["10-content-system", "12-material-library", "material-cards", "{year}", "{year_month}"],
        },
    },
}

CARD_ROUTE_ENV_KEYS: Dict[str, str] = {
    "work": "TIKOMNI_CARD_ROUTE_WORK",
    "author": "TIKOMNI_CARD_ROUTE_AUTHOR",
    "author_sample_work": "TIKOMNI_CARD_ROUTE_AUTHOR_SAMPLE_WORK",
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


def resolve_config_path(cli_config_path: Optional[str] = None) -> str:
    """Resolve config file path with priority:
    1) --config
    2) TIKOMNI_CONFIG_FILE
    3) references/config-templates/defaults.yaml

    Relative paths are always anchored at repository root (not current CWD).
    """

    if cli_config_path and str(cli_config_path).strip():
        return _resolve_repo_anchored_path(str(cli_config_path).strip())

    env_path = os.getenv("TIKOMNI_CONFIG_FILE", "").strip()
    if env_path:
        return _resolve_repo_anchored_path(env_path)

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


def _env_int(name: str) -> Optional[int]:
    raw = os.getenv(name, "").strip()
    if not raw:
        return None
    try:
        value = int(raw)
    except Exception:
        return None
    return value if value > 0 else None


def _env_text(name: str) -> Optional[str]:
    value = os.getenv(name, "").strip()
    return value or None


def _route_from_env(value: str) -> Optional[List[str]]:
    parts = [item.strip() for item in value.split("|")]
    normalized = [item for item in parts if item]
    return normalized if normalized else None


def _normalize_path_locale(raw_value: Optional[str]) -> str:
    value = (raw_value or "").strip().lower()
    if value in LOCALE_ROUTE_PRESETS:
        return value
    return "zh"


def _resolve_from_repo_root(path_value: Optional[str]) -> Path:
    raw = (path_value or "").strip()
    if not raw:
        raw = DEFAULT_OUTPUT_ROOT_NAME

    candidate = Path(raw).expanduser()
    if not candidate.is_absolute():
        candidate = REPO_ROOT / candidate
    return candidate.resolve()


def resolve_storage_paths(config: Dict[str, Any]) -> Dict[str, str]:
    """Resolve storage directories deterministically from repo root (never CWD)."""

    default_route = config_get(config, "storage_routes.default", {})
    default_route = default_route if isinstance(default_route, dict) else {}

    root_dir = _resolve_from_repo_root(str(default_route.get("root_dir") or DEFAULT_OUTPUT_ROOT_NAME))

    resolved: Dict[str, str] = {
        "root_dir": str(root_dir),
    }
    for key in ("runs_dir", "results_dir", "errors_dir"):
        raw_value = str(default_route.get(key) or "").strip()
        if not raw_value:
            raw_value = {
                "runs_dir": "_runs",
                "results_dir": "results",
                "errors_dir": "_errors",
            }[key]

        part = Path(raw_value).expanduser()
        if part.is_absolute():
            resolved[key] = str(part.resolve())
        else:
            resolved[key] = str((root_dir / part).resolve())

    return resolved


def apply_env_overrides(config: Dict[str, Any]) -> Dict[str, Any]:
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

    timeout_ms = _env_int("TIKOMNI_TIMEOUT_MS")
    if timeout_ms is not None:
        runtime["timeout_ms"] = timeout_ms

    for env_key, config_key in {
        "TIKOMNI_OUTPUT_ROOT": "root_dir",
        "TIKOMNI_OUTPUT_RUNS_DIR": "runs_dir",
        "TIKOMNI_OUTPUT_RESULTS_DIR": "results_dir",
        "TIKOMNI_OUTPUT_ERRORS_DIR": "errors_dir",
    }.items():
        value = _env_text(env_key)
        if value is not None:
            default_route[config_key] = value

    filename_pattern = _env_text("TIKOMNI_FILENAME_PATTERN")
    if filename_pattern is not None:
        naming_rules["filename_pattern"] = filename_pattern

    path_locale = _normalize_path_locale(os.getenv("TIKOMNI_PATH_LOCALE", "zh"))
    locale_routes = LOCALE_ROUTE_PRESETS.get(path_locale, LOCALE_ROUTE_PRESETS["zh"])

    for route_key, route_value in locale_routes.items():
        existing = card_type_routes.get(route_key)
        prefix = route_value.get("prefix")
        if isinstance(existing, dict) and isinstance(existing.get("prefix"), str) and existing.get("prefix").strip():
            prefix = existing.get("prefix")
        card_type_routes[route_key] = {
            "prefix": prefix,
            "parts": _deep_clone(route_value.get("parts", [])),
        }

    for route_key, env_name in CARD_ROUTE_ENV_KEYS.items():
        raw_value = _env_text(env_name)
        if raw_value is None:
            continue

        env_parts = _route_from_env(raw_value)
        if not env_parts:
            continue

        current = card_type_routes.get(route_key)
        prefix = ""
        if isinstance(current, dict) and isinstance(current.get("prefix"), str):
            prefix = current.get("prefix") or ""
        if not prefix:
            prefix = LOCALE_ROUTE_PRESETS["zh"].get(route_key, {}).get("prefix", "")

        card_type_routes[route_key] = {
            "prefix": prefix,
            "parts": env_parts,
        }

    resolved_storage = resolve_storage_paths(config)
    for key, value in resolved_storage.items():
        default_route[key] = value

    return config


def load_tikomni_config(cli_config_path: Optional[str] = None) -> Tuple[Dict[str, Any], str]:
    path = resolve_config_path(cli_config_path)

    if yaml is None:
        return apply_env_overrides(_builtin_defaults()), "builtin-defaults"

    try:
        loaded = _load_yaml(path)
    except Exception:
        return apply_env_overrides(_builtin_defaults()), "builtin-defaults"

    merged = _deep_merge(_builtin_defaults(), loaded)
    return apply_env_overrides(merged), path


def config_get(config: Dict[str, Any], dotted_key: str, default: Any = None) -> Any:
    current: Any = config
    for key in dotted_key.split("."):
        if not isinstance(current, dict) or key not in current:
            return default
        current = current[key]
    return current
