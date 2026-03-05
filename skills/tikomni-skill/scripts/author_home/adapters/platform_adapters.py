#!/usr/bin/env python3
"""Platform adapters: raw homepage payload -> normalized schema."""

from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List, Tuple

from scripts.author_home.schema import build_author_profile, build_work_item, validate_author_profile, validate_work_item, validate_works_collection
from scripts.core.tikomni_common import deep_find_first


def _t(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value.strip()
    return str(value).strip()


def _i(value: Any, default: int = 0) -> int:
    try:
        if isinstance(value, (int, float)):
            return int(value)
        return int(float(_t(value).replace(",", ""))) if _t(value) else default
    except Exception:
        return default


def _first(payload: Any, keys: List[str], default: Any = "") -> Any:
    hit = deep_find_first(payload, keys)
    return default if hit is None else hit


def adapt_douyin_author_home(raw: Dict[str, Any]) -> Tuple[Dict[str, Any], List[Dict[str, Any]], List[Dict[str, str]]]:
    missing: List[Dict[str, str]] = []
    profile_data = raw.get("profile_response", {}).get("data")

    author_id = _t(_first(profile_data, ["sec_user_id", "sec_uid", "uid", "user_id"], raw.get("resolved_author_id")))
    profile = build_author_profile(
        platform="douyin",
        platform_author_id=author_id,
        nickname=_t(_first(profile_data, ["nickname", "name"])),
        ip_location=_t(_first(profile_data, ["ip_location", "ip_label", "ipLocation"])),
        fans_count=_i(_first(profile_data, ["follower_count", "fans_count", "mplatform_followers_count"])),
        liked_count=_i(_first(profile_data, ["total_favorited", "liked_count", "favoriting_count"])),
        collected_count=_i(_first(profile_data, ["collect_count", "collected_count", "total_collected_count"])),
        signature=_t(_first(profile_data, ["signature", "desc"])),
        avatar_url=_t(_first(profile_data, ["avatar_larger", "avatar_thumb", "avatar_url", "avatar"])),
        works_count=_i(_first(profile_data, ["aweme_count", "works_count", "video_count"])),
        verified=bool(_first(profile_data, ["verification_type", "verified"], 0) not in (0, None, "", "false", False)),
        snapshot_at=datetime.now().isoformat(timespec="seconds"),
    )
    missing.extend(validate_author_profile(profile))

    works: List[Dict[str, Any]] = []
    for item in raw.get("works", []):
        if not isinstance(item, dict):
            continue
        aweme_id = _t(_first(item, ["aweme_id", "item_id", "id"]))
        metrics = {
            "like": _i(_first(item, ["digg_count", "like_count"], 0)),
            "comment": _i(_first(item, ["comment_count"], 0)),
            "collect": _i(_first(item, ["collect_count"], 0)),
            "share": _i(_first(item, ["share_count"], 0)),
            "play": _i(_first(item, ["play_count", "view_count"], 0)),
        }
        work = build_work_item(
            platform="douyin",
            platform_work_id=aweme_id,
            platform_author_id=author_id,
            title=_t(_first(item, ["desc", "title"])),
            desc=_t(_first(item, ["desc", "title"])),
            publish_time=_t(_first(item, ["create_time", "publish_time"])),
            content_type="video",
            duration_ms=_i(_first(item, ["duration", "duration_ms"], 0)),
            tags=list(_first(item, ["hashtags", "tags", "text_extra"], [])) if isinstance(_first(item, ["hashtags", "tags", "text_extra"], []), list) else [],
            metrics=metrics,
            cover_image=_t(_first(item, ["cover", "cover_url", "origin_cover"], "")),
            source_url=f"https://www.douyin.com/video/{aweme_id}" if aweme_id else "",
            share_url=_t(_first(item, ["share_url", "share_link"])),
            raw_ref={"aweme_id": aweme_id},
        )
        missing.extend(validate_work_item(work))
        works.append(work)

    missing.extend(validate_works_collection(works))
    return profile, works, missing


def adapt_xhs_author_home(raw: Dict[str, Any]) -> Tuple[Dict[str, Any], List[Dict[str, Any]], List[Dict[str, str]]]:
    missing: List[Dict[str, str]] = []
    profile_data = raw.get("profile_response", {}).get("data")

    author_id = _t(_first(profile_data, ["user_id", "userid", "id"], raw.get("resolved_author_id")))
    profile = build_author_profile(
        platform="xiaohongshu",
        platform_author_id=author_id,
        nickname=_t(_first(profile_data, ["nickname", "name"])),
        ip_location=_t(_first(profile_data, ["ip_location", "ip_location_desc", "ipLocation"])),
        fans_count=_i(_first(profile_data, ["fans", "fans_count", "follower_count"])),
        liked_count=_i(_first(profile_data, ["liked_count", "likes", "total_liked"])),
        collected_count=_i(_first(profile_data, ["collected_count", "collect_count", "total_collected"])),
        signature=_t(_first(profile_data, ["desc", "signature", "bio"])),
        avatar_url=_t(_first(profile_data, ["image", "avatar", "avatar_url"])),
        works_count=_i(_first(profile_data, ["notes", "note_count", "works_count"])),
        verified=bool(_first(profile_data, ["official_verified", "verified"], False)),
        snapshot_at=datetime.now().isoformat(timespec="seconds"),
    )
    missing.extend(validate_author_profile(profile))

    works: List[Dict[str, Any]] = []
    for item in raw.get("works", []):
        if not isinstance(item, dict):
            continue
        note_id = _t(_first(item, ["note_id", "id", "item_id"]))
        interact = _first(item, ["interact_info", "statistics"], {})
        metrics = {
            "like": _i(_first(interact, ["liked_count", "like_count", "digg_count"], 0)),
            "comment": _i(_first(interact, ["comment_count"], 0)),
            "collect": _i(_first(interact, ["collected_count", "collect_count"], 0)),
            "share": _i(_first(interact, ["share_count"], 0)),
            "play": _i(_first(interact, ["view_count", "play_count"], 0)),
        }
        work = build_work_item(
            platform="xiaohongshu",
            platform_work_id=note_id,
            platform_author_id=author_id,
            title=_t(_first(item, ["title", "desc"])),
            desc=_t(_first(item, ["desc", "title"])),
            publish_time=_t(_first(item, ["time", "publish_time", "create_time"])),
            content_type="video" if _t(_first(item, ["type", "note_type"])) in {"video", "0", "normal"} else _t(_first(item, ["type", "note_type"])) or "note",
            duration_ms=_i(_first(item, ["video", "duration", "duration_ms"], 0)),
            tags=list(_first(item, ["tag_list", "tags", "hashtags"], [])) if isinstance(_first(item, ["tag_list", "tags", "hashtags"], []), list) else [],
            metrics=metrics,
            cover_image=_t(_first(item, ["cover", "image", "image_list", "0", "url"], "")),
            source_url=f"https://www.xiaohongshu.com/explore/{note_id}" if note_id else "",
            share_url=_t(_first(item, ["share_url", "url"])),
            raw_ref={"note_id": note_id},
        )
        missing.extend(validate_work_item(work))
        works.append(work)

    missing.extend(validate_works_collection(works))
    return profile, works, missing
