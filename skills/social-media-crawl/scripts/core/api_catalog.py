#!/usr/bin/env python3
"""Skill-local API catalog helpers."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional

SKILL_ROOT = Path(__file__).resolve().parents[2]
CATALOG_ROOT = SKILL_ROOT / "references" / "api-catalog"


def normalize_key(value: Any) -> str:
    text = str(value or "").strip().lower()
    text = re.sub(r"\s+", " ", text)
    return text


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def load_operations() -> List[Dict[str, Any]]:
    payload = load_json(CATALOG_ROOT / "operations.json")
    if not isinstance(payload, list):
        raise ValueError("api_catalog_operations_must_be_list")
    return [item for item in payload if isinstance(item, dict)]


def load_aliases() -> Dict[str, Any]:
    payload = load_json(CATALOG_ROOT / "aliases.json")
    if not isinstance(payload, dict):
        raise ValueError("api_catalog_aliases_must_be_object")
    return payload


def build_alias_index(alias_map: Dict[str, Iterable[Any]]) -> Dict[str, str]:
    index: Dict[str, str] = {}
    for slug, aliases in alias_map.items():
        index[normalize_key(slug)] = str(slug)
        for alias in aliases or []:
            normalized = normalize_key(alias)
            if normalized:
                index[normalized] = str(slug)
    return index


def resolve_alias(value: Optional[str], alias_map: Dict[str, Iterable[Any]]) -> str:
    if not value:
        return ""
    normalized = normalize_key(value)
    index = build_alias_index(alias_map)
    return index.get(normalized, normalized.replace("-", "_").replace(" ", "_"))


def _has_non_ascii(value: str) -> bool:
    return any(ord(char) > 127 for char in value)


def _alias_in_text(alias: str, normalized_text: str) -> bool:
    if not alias:
        return False
    if _has_non_ascii(alias):
        return alias in normalized_text
    pattern = rf"(?<![a-z0-9_]){re.escape(alias)}(?![a-z0-9_])"
    return re.search(pattern, normalized_text) is not None


def infer_alias_from_text(text: str, alias_map: Dict[str, Iterable[Any]]) -> str:
    normalized_text = normalize_key(text)
    if not normalized_text:
        return ""
    index = build_alias_index(alias_map)
    hits: List[tuple[int, str, str]] = []
    for alias, slug in index.items():
        if not alias:
            continue
        if _alias_in_text(alias, normalized_text):
            hits.append((len(alias), alias, slug))
    if not hits:
        return ""
    hits.sort(reverse=True)
    return hits[0][2]


def operation_by_endpoint_id(operations: Iterable[Dict[str, Any]], endpoint_id: str) -> Optional[Dict[str, Any]]:
    for operation in operations:
        if operation.get("endpoint_id") == endpoint_id:
            return operation
    return None


def sorted_operations(operations: Iterable[Dict[str, Any]]) -> List[Dict[str, Any]]:
    return sorted(
        operations,
        key=lambda item: (
            not bool(item.get("recommended")),
            str(item.get("variant") or ""),
            str(item.get("path") or ""),
        ),
    )
