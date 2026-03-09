#!/usr/bin/env python3
"""Storage routing helpers for single-work card outputs."""

from __future__ import annotations

import os
import re
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple


DEFAULT_CARD_TYPE_ROUTES: Dict[str, Dict[str, Any]] = {
    "work": {
        "prefix": "CBV",
        "parts": ["内容系统", "对标研究", "作品卡"],
    },
}

DEFAULT_CONTENT_KIND_CARD_TYPE: Dict[str, str] = {
    "single_video": "work",
    "note": "work",
    "work": "work",
}

CONTENT_KIND_ALIASES: Dict[str, str] = {
    "single-work": "work",
}

DEFAULT_CARD_FILENAME_PATTERN = "{prefix}-{platform}-{author_slug}-{title_slug}{ext}"
DEFAULT_JSON_FILENAME_PATTERN = "{timestamp}-{platform}-{identifier}{ext}"
_INVALID_FILENAME_CHARS = re.compile(r"[\\\\/:*?\"<>|]+")
_SPACE_RUN = re.compile(r"\s+")


def normalize_card_type(card_type: str) -> str:
    normalized = (card_type or "").strip().lower().replace("-", "_")
    return "work" if normalized == "work" else "work"


def normalize_content_kind(content_kind: Optional[str]) -> str:
    normalized = (content_kind or "").strip().lower().replace("-", "_")
    if not normalized:
        return ""
    return CONTENT_KIND_ALIASES.get(normalized, normalized)


def _storage_routes_cfg(storage_config: Optional[Dict[str, Any]]) -> Dict[str, Any]:
    if not isinstance(storage_config, dict):
        return {}
    routes = storage_config.get("storage_routes")
    return routes if isinstance(routes, dict) else {}


def _configured_content_kind_map(storage_config: Optional[Dict[str, Any]]) -> Dict[str, str]:
    routes = _storage_routes_cfg(storage_config)
    configured = routes.get("content_kind_card_type")
    if not isinstance(configured, dict):
        return dict(DEFAULT_CONTENT_KIND_CARD_TYPE)

    merged = dict(DEFAULT_CONTENT_KIND_CARD_TYPE)
    for key, value in configured.items():
        normalized_key = normalize_content_kind(str(key))
        if normalized_key:
            merged[normalized_key] = normalize_card_type(str(value))
    return merged


def _configured_card_routes(storage_config: Optional[Dict[str, Any]]) -> Dict[str, Dict[str, Any]]:
    routes = _storage_routes_cfg(storage_config)
    configured = routes.get("card_type_routes")
    if not isinstance(configured, dict):
        return {key: dict(value) for key, value in DEFAULT_CARD_TYPE_ROUTES.items()}

    merged = {key: dict(value) for key, value in DEFAULT_CARD_TYPE_ROUTES.items()}
    for key, value in configured.items():
        card_type = normalize_card_type(str(key))
        if card_type != "work" or not isinstance(value, dict):
            continue
        parts = value.get("parts")
        if not isinstance(parts, list) or not all(isinstance(item, str) and item for item in parts):
            continue
        prefix = str(value.get("prefix") or merged["work"]["prefix"])
        merged["work"] = {
            "prefix": prefix,
            "parts": parts,
        }
    return merged


def _sanitize_filename_token(value: Any, fallback: str = "item") -> str:
    text = str(value or "").strip()
    if not text:
        text = fallback
    text = _INVALID_FILENAME_CHARS.sub("-", text)
    text = _SPACE_RUN.sub("-", text)
    text = text.replace("/", "-").replace("\\", "-")
    text = re.sub(r"-{2,}", "-", text).strip(" .-_")
    return text or fallback


def resolve_card_filename_pattern(storage_config: Optional[Dict[str, Any]]) -> str:
    if not isinstance(storage_config, dict):
        return DEFAULT_CARD_FILENAME_PATTERN
    naming_rules = storage_config.get("naming_rules")
    if not isinstance(naming_rules, dict):
        return DEFAULT_CARD_FILENAME_PATTERN
    pattern = str(naming_rules.get("card_filename_pattern") or "").strip()
    return pattern or DEFAULT_CARD_FILENAME_PATTERN


def resolve_json_filename_pattern(storage_config: Optional[Dict[str, Any]]) -> str:
    if not isinstance(storage_config, dict):
        return DEFAULT_JSON_FILENAME_PATTERN
    naming_rules = storage_config.get("naming_rules")
    if not isinstance(naming_rules, dict):
        return DEFAULT_JSON_FILENAME_PATTERN
    pattern = str(naming_rules.get("json_filename_pattern") or "").strip()
    return pattern or DEFAULT_JSON_FILENAME_PATTERN


def render_output_filename(
    *,
    pattern: str,
    context: Dict[str, Any],
    default_filename: str,
    default_ext: str,
) -> str:
    safe_context = {key: _sanitize_filename_token(value, fallback=key) for key, value in context.items()}
    safe_context["ext"] = default_ext
    try:
        rendered = str(pattern).format(**safe_context).strip()
    except Exception:
        rendered = default_filename
    rendered = _INVALID_FILENAME_CHARS.sub("-", rendered)
    rendered = _SPACE_RUN.sub("-", rendered)
    rendered = rendered.replace("/", "-").replace("\\", "-").strip()
    if not rendered:
        rendered = default_filename
    if not Path(rendered).suffix:
        rendered = f"{rendered}{default_ext}"
    return rendered


def resolve_effective_card_type(
    *,
    card_type: str,
    content_kind: Optional[str],
    storage_config: Optional[Dict[str, Any]],
    force_card_type: bool = False,
) -> str:
    normalized_card_type = normalize_card_type(card_type)
    if force_card_type:
        return normalized_card_type

    normalized_content_kind = normalize_content_kind(content_kind)
    if not normalized_content_kind:
        return normalized_card_type

    mapped = _configured_content_kind_map(storage_config).get(normalized_content_kind)
    return normalize_card_type(str(mapped)) if mapped is not None else normalized_card_type


def render_route_parts(parts: List[str], *, context: Dict[str, str]) -> List[str]:
    rendered: List[str] = []
    for item in parts:
        try:
            rendered.append(item.format(**context))
        except Exception:
            rendered.append(item)
    return rendered


def build_card_output_path(
    *,
    card_root: str,
    platform: str,
    card_type: str,
    author_slug: str,
    title_slug: str,
    year: str,
    year_month: str,
    timestamp: str,
    storage_config: Optional[Dict[str, Any]],
) -> Tuple[str, str]:
    card_routes = _configured_card_routes(storage_config)
    route = card_routes.get(card_type) or DEFAULT_CARD_TYPE_ROUTES["work"]
    parts = route.get("parts") if isinstance(route.get("parts"), list) else DEFAULT_CARD_TYPE_ROUTES["work"]["parts"]
    prefix = str(route.get("prefix") or "CBV")

    route_context = {
        "platform": platform,
        "author_slug": author_slug,
        "title_slug": title_slug,
        "year": year,
        "year_month": year_month,
        "timestamp": timestamp,
    }
    rendered_parts = render_route_parts(parts, context=route_context)
    directory = os.path.join(card_root, *rendered_parts)
    os.makedirs(directory, exist_ok=True)

    default_filename = f"{prefix}-{platform}-{author_slug}-{title_slug}.md"
    filename = render_output_filename(
        pattern=resolve_card_filename_pattern(storage_config),
        context={
            "prefix": prefix,
            "platform": platform,
            "card_type": card_type,
            "author_slug": author_slug,
            "title_slug": title_slug,
            "timestamp": timestamp,
            "date": timestamp.split("-", 1)[0],
            "identifier": f"{platform}-{author_slug}-{title_slug}",
            "ext": ".md",
        },
        default_filename=default_filename,
        default_ext=".md",
    )

    return os.path.join(directory, filename), "/".join(rendered_parts)
