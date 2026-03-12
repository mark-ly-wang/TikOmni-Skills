#!/usr/bin/env python3
"""Shared Douyin metadata extraction helpers."""

from __future__ import annotations

import re
from typing import Any, Dict, Optional

from scripts.core.tikomni_common import normalize_text

INVALID_AUTHOR_HANDLE_VALUES = {"0", "unknown", "none", "null", "nil", "na", "n/a"}
MUSIC_TITLE_PATTERN = re.compile(r"^@?.+?(?:创作的原声|作品使用的原声|的原声)$")


def _safe_int(value: Any) -> Optional[int]:
    if value is None:
        return None
    if isinstance(value, bool):
        return int(value)
    if isinstance(value, int):
        return value
    if isinstance(value, float):
        return int(value)

    text = normalize_text(value)
    if not text:
        return None
    try:
        return int(float(text.replace(",", "")))
    except Exception:
        return None


def normalize_douyin_author_handle(*values: Any) -> str:
    for value in values:
        text = normalize_text(value)
        if not text:
            continue
        if text.lower() in INVALID_AUTHOR_HANDLE_VALUES:
            continue
        return text
    return ""


def looks_like_douyin_music_title(value: Any) -> bool:
    title = normalize_text(value)
    if not title:
        return False
    return bool(MUSIC_TITLE_PATTERN.match(title))


def extract_douyin_caption(item: Dict[str, Any]) -> str:
    if not isinstance(item, dict):
        return ""
    for key in ("desc", "caption", "content", "item_title", "preview_title", "title"):
        text = normalize_text(item.get(key))
        if text:
            return text
    return ""


def title_from_douyin_caption(caption: Any) -> str:
    text = normalize_text(caption)
    if not text:
        return ""

    stripped = re.split(r"\s*#\S+", text, maxsplit=1)[0].strip()
    if stripped:
        return stripped
    return text


def extract_douyin_title(item: Dict[str, Any]) -> str:
    if not isinstance(item, dict):
        return ""

    # Only read title-like fields from the work object itself.
    # Nested `music.title` is an audio title, not the work title.
    caption_title = title_from_douyin_caption(extract_douyin_caption(item))
    for key in ("item_title", "preview_title", "title"):
        candidate = normalize_text(item.get(key))
        if not candidate:
            continue
        if looks_like_douyin_music_title(candidate) and caption_title:
            continue
        return candidate
    return caption_title


def extract_douyin_author(item: Dict[str, Any]) -> Dict[str, Optional[str]]:
    author = item.get("author") if isinstance(item.get("author"), dict) else {}

    author_platform_id = (
        normalize_text(author.get("uid"))
        or normalize_text(author.get("id"))
        or normalize_text(item.get("author_user_id"))
    )
    author_handle = normalize_douyin_author_handle(
        author.get("unique_id"),
        author.get("short_id"),
        author.get("douyin_id"),
        author.get("display_id"),
        author.get("nickname"),
    )
    douyin_sec_uid = normalize_text(author.get("sec_uid"))
    douyin_aweme_author_id = normalize_text(item.get("author_user_id")) or author_platform_id

    return {
        "author_handle": author_handle or None,
        "platform_author_id": author_platform_id or None,
        "author_platform_id": author_platform_id or None,
        "douyin_sec_uid": douyin_sec_uid or None,
        "douyin_aweme_author_id": douyin_aweme_author_id or None,
        "unique_id": normalize_text(author.get("unique_id")) or None,
        "nickname": normalize_text(author.get("nickname")) or None,
        "signature": normalize_text(author.get("signature")) or None,
    }


def extract_douyin_metrics(item: Dict[str, Any]) -> Dict[str, Optional[int]]:
    statistics = item.get("statistics") if isinstance(item.get("statistics"), dict) else {}

    def metric(*keys: str, default: Optional[int] = 0) -> Optional[int]:
        for key in keys:
            value = _safe_int(statistics.get(key))
            if value is not None:
                return value
            value = _safe_int(item.get(key))
            if value is not None:
                return value
        return default

    metrics = {
        "digg_count": metric("digg_count", "like_count"),
        "comment_count": metric("comment_count"),
        "collect_count": metric("collect_count"),
        "share_count": metric("share_count", "forward_count"),
        "play_count": metric("play_count", "view_count", default=None),
    }

    play_count = metrics.get("play_count")
    engagement_floor = max(
        int(metrics.get("digg_count") or 0),
        int(metrics.get("comment_count") or 0),
        int(metrics.get("collect_count") or 0),
        int(metrics.get("share_count") or 0),
    )
    if play_count is not None and int(play_count) <= 0 and engagement_floor > 0:
        metrics["play_count"] = None

    return metrics
