#!/usr/bin/env python3
"""Storage routing helpers for work fact cards."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any, Dict, List, Optional

DEFAULT_CARD_FILENAME_PATTERN = "{identifier}{ext}"
DEFAULT_JSON_FILENAME_PATTERN = "{timestamp}-{platform}-{identifier}{ext}"
_INVALID_FILENAME_CHARS = re.compile(r"[\\\\/:*?\"<>|]+")
_SPACE_RUN = re.compile(r"\s+")
_INVALID_AUTHOR_SLUGS = {"0", "unknown", "none", "null", "nil", "na", "n-a"}


def slugify_token(value: Any, fallback: str = "unknown") -> str:
    text = str(value or "").strip().lower()
    if not text:
        text = fallback
    text = text.replace(" ", "-")
    text = _INVALID_FILENAME_CHARS.sub("-", text)
    text = re.sub(r"[^a-z0-9_-]+", "-", text)
    text = re.sub(r"-{2,}", "-", text).strip("-_")
    return text or fallback


def resolve_card_filename_pattern(storage_config: Optional[Dict[str, Any]]) -> str:
    if not isinstance(storage_config, dict):
        return DEFAULT_CARD_FILENAME_PATTERN
    naming_rules = storage_config.get("naming_rules")
    if not isinstance(naming_rules, dict):
        return DEFAULT_CARD_FILENAME_PATTERN
    return str(naming_rules.get("card_filename_pattern") or "").strip() or DEFAULT_CARD_FILENAME_PATTERN


def resolve_json_filename_pattern(storage_config: Optional[Dict[str, Any]]) -> str:
    if not isinstance(storage_config, dict):
        return DEFAULT_JSON_FILENAME_PATTERN
    naming_rules = storage_config.get("naming_rules")
    if not isinstance(naming_rules, dict):
        return DEFAULT_JSON_FILENAME_PATTERN
    return str(naming_rules.get("json_filename_pattern") or "").strip() or DEFAULT_JSON_FILENAME_PATTERN


def render_output_filename(
    *,
    pattern: str,
    context: Dict[str, Any],
    default_filename: str,
    default_ext: str,
) -> str:
    safe_context = {key: slugify_token(value, fallback=key) for key, value in context.items()}
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


def _storage_routes_cfg(storage_config: Optional[Dict[str, Any]]) -> Dict[str, Any]:
    if not isinstance(storage_config, dict):
        return {}
    routes = storage_config.get("storage_routes")
    return routes if isinstance(routes, dict) else {}


def resolve_card_root(storage_config: Optional[Dict[str, Any]], explicit_card_root: Optional[str] = None) -> str:
    if explicit_card_root:
        candidate = Path(explicit_card_root).expanduser()
        if not candidate.is_absolute():
            raise ValueError("card_root must be an absolute path")
        return str(candidate.resolve())

    routes = _storage_routes_cfg(storage_config)
    default_route = routes.get("default") if isinstance(routes.get("default"), dict) else {}
    card_root = str(default_route.get("card_root") or "").strip()
    if not card_root:
        raise ValueError("missing_card_root")
    return str(Path(card_root).expanduser().resolve())


def resolve_author_slug(platform: str, author_handle: str, platform_author_id: str) -> str:
    handle_slug = slugify_token(author_handle, fallback="")
    if handle_slug and handle_slug not in _INVALID_AUTHOR_SLUGS:
        return handle_slug
    author_id_slug = slugify_token(platform_author_id, fallback="")
    if author_id_slug:
        return author_id_slug
    return f"{slugify_token(platform)}-unknown"


def resolve_author_directory_name(platform: str, author_handle: str, platform_author_id: str) -> str:
    return f"{slugify_token(platform)}-{resolve_author_slug(platform, author_handle, platform_author_id)}"


def resolve_card_route_parts(
    storage_config: Optional[Dict[str, Any]],
    *,
    platform: str,
    author_slug: str,
) -> List[str]:
    routes = _storage_routes_cfg(storage_config)
    card_type_routes = routes.get("card_type_routes") if isinstance(routes.get("card_type_routes"), dict) else {}
    work_route = card_type_routes.get("work") if isinstance(card_type_routes.get("work"), dict) else {}
    parts = work_route.get("parts") if isinstance(work_route.get("parts"), list) else ["内容系统", "作品库", "{platform}-{author_slug}"]
    rendered: List[str] = []
    context = {"platform": slugify_token(platform), "author_slug": author_slug}
    for part in parts:
        try:
            rendered.append(str(part).format(**context))
        except Exception:
            rendered.append(str(part))
    return rendered


def build_work_fact_card_paths(
    *,
    card_root: str,
    platform: str,
    platform_work_id: str,
    author_handle: str,
    platform_author_id: str,
    storage_config: Optional[Dict[str, Any]],
    fallback_identifier: str,
) -> Dict[str, str]:
    author_slug = resolve_author_slug(platform, author_handle, platform_author_id)
    route_parts = resolve_card_route_parts(storage_config, platform=platform, author_slug=author_slug)
    directory = Path(card_root).joinpath(*route_parts)
    directory.mkdir(parents=True, exist_ok=True)

    identifier = slugify_token(platform_work_id, fallback="") or slugify_token(fallback_identifier, fallback="unknown")
    json_filename = render_output_filename(
        pattern=resolve_card_filename_pattern(storage_config),
        context={"identifier": identifier, "platform": platform, "author_slug": author_slug, "ext": ".json"},
        default_filename=f"{identifier}.json",
        default_ext=".json",
    )
    markdown_filename = render_output_filename(
        pattern=resolve_card_filename_pattern(storage_config),
        context={"identifier": identifier, "platform": platform, "author_slug": author_slug, "ext": ".md"},
        default_filename=f"{identifier}.md",
        default_ext=".md",
    )
    return {
        "identifier": identifier,
        "author_slug": author_slug,
        "directory": str(directory),
        "route": "/".join(route_parts),
        "json_path": str(directory / json_filename),
        "markdown_path": str(directory / markdown_filename),
    }
