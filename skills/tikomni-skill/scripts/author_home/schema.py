#!/usr/bin/env python3
"""Schema definitions and minimal validators for author-home pipeline."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional


def _to_text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value.strip()
    return str(value).strip()


def _to_int(value: Any, default: int = 0) -> int:
    try:
        if isinstance(value, bool):
            return int(value)
        if isinstance(value, (int, float)):
            return int(value)
        text = _to_text(value).replace(",", "")
        return int(float(text)) if text else default
    except Exception:
        return default


@dataclass
class AuthorProfileNormalized:
    platform: str
    platform_author_id: str
    nickname: str
    ip_location: str
    fans_count: int
    liked_count: int
    collected_count: int
    signature: str
    avatar_url: str
    works_count: int
    verified: bool
    snapshot_at: str


@dataclass
class WorkItemNormalized:
    platform: str
    platform_work_id: str
    platform_author_id: str
    title: str
    desc: str
    publish_time: str
    content_type: str
    duration_ms: int
    tags: List[str] = field(default_factory=list)
    metrics: Dict[str, int] = field(default_factory=dict)
    cover_image: str = ""
    source_url: str = ""
    share_url: str = ""
    raw_ref: Dict[str, Any] = field(default_factory=dict)


def validate_author_profile(payload: Dict[str, Any]) -> List[Dict[str, str]]:
    required_types = {
        "platform": str,
        "platform_author_id": str,
        "nickname": str,
        "ip_location": str,
        "fans_count": int,
        "liked_count": int,
        "collected_count": int,
        "signature": str,
        "avatar_url": str,
        "works_count": int,
        "verified": bool,
        "snapshot_at": str,
    }
    missing: List[Dict[str, str]] = []
    for key, expected in required_types.items():
        if key not in payload:
            missing.append({"field": key, "reason": "missing"})
            continue
        value = payload.get(key)
        if expected is int and not isinstance(value, int):
            missing.append({"field": key, "reason": "type_error:int"})
        elif expected is bool and not isinstance(value, bool):
            missing.append({"field": key, "reason": "type_error:bool"})
        elif expected is str and not isinstance(value, str):
            missing.append({"field": key, "reason": "type_error:str"})

    for key in ("platform", "platform_author_id", "nickname"):
        value = payload.get(key)
        if isinstance(value, str) and not value.strip():
            missing.append({"field": key, "reason": "empty_value"})
    return missing


def validate_work_item(payload: Dict[str, Any]) -> List[Dict[str, str]]:
    required_types = {
        "platform": str,
        "platform_work_id": str,
        "platform_author_id": str,
        "title": str,
        "desc": str,
        "publish_time": str,
        "content_type": str,
        "duration_ms": int,
        "tags": list,
        "metrics": dict,
        "cover_image": str,
        "source_url": str,
        "share_url": str,
        "raw_ref": dict,
    }
    missing: List[Dict[str, str]] = []
    for key, expected in required_types.items():
        if key not in payload:
            missing.append({"field": key, "reason": "missing"})
            continue
        if not isinstance(payload.get(key), expected):
            missing.append({"field": key, "reason": f"type_error:{expected.__name__}"})

    for key in ("platform", "platform_work_id", "platform_author_id", "title"):
        value = payload.get(key)
        if isinstance(value, str) and not value.strip():
            missing.append({"field": key, "reason": "empty_value"})
    return missing


def validate_works_collection(works: Any) -> List[Dict[str, str]]:
    if not isinstance(works, list):
        return [{"field": "works", "reason": "type_error:list"}]
    if not works:
        return [{"field": "works", "reason": "empty_collection"}]
    return []


def build_author_profile(**kwargs: Any) -> Dict[str, Any]:
    profile = AuthorProfileNormalized(
        platform=_to_text(kwargs.get("platform")),
        platform_author_id=_to_text(kwargs.get("platform_author_id")),
        nickname=_to_text(kwargs.get("nickname")),
        ip_location=_to_text(kwargs.get("ip_location")),
        fans_count=_to_int(kwargs.get("fans_count")),
        liked_count=_to_int(kwargs.get("liked_count")),
        collected_count=_to_int(kwargs.get("collected_count")),
        signature=_to_text(kwargs.get("signature")),
        avatar_url=_to_text(kwargs.get("avatar_url")),
        works_count=_to_int(kwargs.get("works_count")),
        verified=bool(kwargs.get("verified", False)),
        snapshot_at=_to_text(kwargs.get("snapshot_at")) or datetime.now().isoformat(timespec="seconds"),
    )
    return asdict(profile)


def build_work_item(**kwargs: Any) -> Dict[str, Any]:
    item = WorkItemNormalized(
        platform=_to_text(kwargs.get("platform")),
        platform_work_id=_to_text(kwargs.get("platform_work_id")),
        platform_author_id=_to_text(kwargs.get("platform_author_id")),
        title=_to_text(kwargs.get("title")),
        desc=_to_text(kwargs.get("desc")),
        publish_time=_to_text(kwargs.get("publish_time")),
        content_type=_to_text(kwargs.get("content_type")) or "video",
        duration_ms=_to_int(kwargs.get("duration_ms")),
        tags=list(kwargs.get("tags") or []),
        metrics=dict(kwargs.get("metrics") or {}),
        cover_image=_to_text(kwargs.get("cover_image")),
        source_url=_to_text(kwargs.get("source_url")),
        share_url=_to_text(kwargs.get("share_url")) or _to_text(kwargs.get("source_url")),
        raw_ref=dict(kwargs.get("raw_ref") or {}),
    )
    return asdict(item)
