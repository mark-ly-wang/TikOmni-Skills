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
        raise RuntimeError("PyYAML is required to load Tikomni config templates")

    with open(path, "r", encoding="utf-8") as handle:
        payload = yaml.safe_load(handle) or {}
    if not isinstance(payload, dict):
        raise ValueError(f"config_root_must_be_mapping:{path}")
    return payload


def load_tikomni_config(cli_config_path: Optional[str] = None) -> Tuple[Dict[str, Any], str]:
    path = resolve_config_path(cli_config_path)
    config = _load_yaml(path)
    return config, path


def config_get(config: Dict[str, Any], dotted_key: str, default: Any = None) -> Any:
    current: Any = config
    for key in dotted_key.split("."):
        if not isinstance(current, dict) or key not in current:
            return default
        current = current[key]
    return current
