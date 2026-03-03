#!/usr/bin/env python3
"""Lightweight config loader for Tikomni scripts (Phase 1 skeleton)."""

from __future__ import annotations

import os
from pathlib import Path
from typing import Any, Dict, Optional, Tuple

try:
    import yaml
except Exception:  # pragma: no cover - defensive fallback
    yaml = None

DEFAULT_CONFIG_PATH = Path(__file__).resolve().parents[1] / "references" / "config-templates" / "defaults.yaml"

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
            "root_dir": "docs/skill-output",
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


def resolve_config_path(cli_config_path: Optional[str] = None) -> str:
    """Resolve config file path with priority:
    1) --config
    2) TIKOMNI_CONFIG_FILE
    3) references/config-templates/defaults.yaml
    """

    if cli_config_path and str(cli_config_path).strip():
        return str(Path(cli_config_path).expanduser().resolve())

    env_path = os.getenv("TIKOMNI_CONFIG_FILE", "").strip()
    if env_path:
        return str(Path(env_path).expanduser().resolve())

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


def load_tikomni_config(cli_config_path: Optional[str] = None) -> Tuple[Dict[str, Any], str]:
    path = resolve_config_path(cli_config_path)

    if yaml is None:
        return _builtin_defaults(), "builtin-defaults"

    try:
        loaded = _load_yaml(path)
    except Exception:
        return _builtin_defaults(), "builtin-defaults"

    return _deep_merge(_builtin_defaults(), loaded), path


def config_get(config: Dict[str, Any], dotted_key: str, default: Any = None) -> Any:
    current: Any = config
    for key in dotted_key.split("."):
        if not isinstance(current, dict) or key not in current:
            return default
        current = current[key]
    return current
