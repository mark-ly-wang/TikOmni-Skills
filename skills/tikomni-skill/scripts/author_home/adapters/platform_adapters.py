#!/usr/bin/env python3
"""Platform adapters: raw homepage payload -> normalized schema."""

from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List, Tuple

from scripts.author_home.schema import build_author_profile, build_work_item, validate_author_profile, validate_work_item, validate_works_collection
from scripts.core.tikomni_common import deep_find_all, deep_find_first
from scripts.platform.douyin.select_low_quality_video_url import select_low_quality_video_url


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


def _pick_http_urls(payload: Any, keys: List[str]) -> List[str]:
    urls: List[str] = []
    for key in keys:
        for value in deep_find_all(payload, [key]):
            if isinstance(value, str):
                text = value.strip()
                if text.startswith("http://") or text.startswith("https://"):
                    urls.append(text)
            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, str):
                        text = item.strip()
                        if text.startswith("http://") or text.startswith("https://"):
                            urls.append(text)

    deduped: List[str] = []
    seen = set()
    for url in urls:
        if url in seen:
            continue
        deduped.append(url)
        seen.add(url)
    return deduped


def _is_probable_video_url(url: str) -> bool:
    lower = (url or "").lower()
    if not (lower.startswith("http://") or lower.startswith("https://")):
        return False
    if any(token in lower for token in [".jpg", ".jpeg", ".png", ".webp", "image", "img"]):
        return False
    return any(token in lower for token in [".mp4", ".m3u8", ".m4a", "video", "stream", "play"])


def _extract_douyin_video_down_url(item: Dict[str, Any]) -> str:
    video = item.get("video") if isinstance(item.get("video"), dict) else {}
    selected = select_low_quality_video_url(video)
    return _t(selected.get("video_down_url"))


def _extract_xhs_video_down_url(item: Dict[str, Any]) -> str:
    urls = _pick_http_urls(
        item,
        [
            "master_url",
            "masterUrl",
            "play_url",
            "playUrl",
            "url",
            "video_url",
            "videoUrl",
            "origin_video_url",
        ],
    )
    for url in urls:
        if _is_probable_video_url(url):
            return url
    return ""


def _extract_xhs_subtitle_inline(item: Dict[str, Any]) -> str:
    lines: List[str] = []
    for container in deep_find_all(item, ["subtitles", "subtitle_list", "subtitleList"]):
        if isinstance(container, list):
            for entry in container:
                if isinstance(entry, dict):
                    for key in ["text", "content", "sentence", "line"]:
                        value = _t(entry.get(key))
                        if value:
                            lines.append(value)
                elif isinstance(entry, str):
                    value = _t(entry)
                    if value:
                        lines.append(value)
        elif isinstance(container, dict):
            for key in ["text", "content"]:
                value = _t(container.get(key))
                if value:
                    lines.append(value)

    deduped = list(dict.fromkeys(lines))
    return "\n".join(deduped).strip()


def _extract_xhs_subtitle_urls(item: Dict[str, Any]) -> List[str]:
    return _pick_http_urls(item, ["subtitle_url", "subtitleUrl", "srt_url", "srtUrl", "vtt_url", "vttUrl"])


def adapt_douyin_author_home(raw: Dict[str, Any]) -> Tuple[Dict[str, Any], List[Dict[str, Any]], List[Dict[str, str]]]:
    missing: List[Dict[str, str]] = []
    profile_data = raw.get("profile_response", {}).get("data")

    internal_author_id = _t(_first(profile_data, ["sec_user_id", "sec_uid"], raw.get("resolved_author_id")))
    stable_author_id = _t(_first(profile_data, ["uid", "user_id", "id"]))
    author_handle = _t(_first(profile_data, ["short_id", "unique_id", "douyin_id", "display_id"]))

    author_id = internal_author_id or stable_author_id
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
    profile["author_platform_id"] = stable_author_id or author_id
    profile["author_handle"] = author_handle

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
        video_down_url = _extract_douyin_video_down_url(item)
        work = build_work_item(
            platform="douyin",
            platform_work_id=aweme_id,
            platform_author_id=author_id,
            title=_t(_first(item, ["desc", "title"])),
            desc=_t(_first(item, ["desc", "title"])),
            publish_time=_t(_first(item, ["create_time", "publish_time"])),
            content_type="video",
            duration_ms=_i(_first(item, ["duration_ms", "duration"], 0)),
            tags=list(_first(item, ["hashtags", "tags", "text_extra"], [])) if isinstance(_first(item, ["hashtags", "tags", "text_extra"], []), list) else [],
            metrics=metrics,
            cover_image=_t(_first(item, ["cover_url", "cover", "origin_cover"], "")),
            source_url=f"https://www.douyin.com/video/{aweme_id}" if aweme_id else "",
            share_url=_t(_first(item, ["share_url", "share_link"])),
            video_down_url=video_down_url,
            asr_raw="",
            asr_clean="",
            asr_status="pending",
            asr_error_reason="",
            asr_source="fallback_none",
            raw_ref={"aweme_id": aweme_id, "raw_item": item},
        )
        work["author_platform_id"] = stable_author_id or author_id
        work["author_handle"] = author_handle

        missing.extend(validate_work_item(work))
        works.append(work)

    missing.extend(validate_works_collection(works))
    return profile, works, missing


def adapt_xhs_author_home(raw: Dict[str, Any]) -> Tuple[Dict[str, Any], List[Dict[str, Any]], List[Dict[str, str]]]:
    missing: List[Dict[str, str]] = []
    profile_data = raw.get("profile_response", {}).get("data")

    author_id = _t(_first(profile_data, ["user_id", "userid", "id"], raw.get("resolved_author_id")))
    author_handle = _t(_first(profile_data, ["red_id", "redid", "display_id", "username"]))
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
    profile["author_platform_id"] = author_id
    profile["author_handle"] = author_handle

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
        subtitle_inline = _extract_xhs_subtitle_inline(item)
        subtitle_urls = _extract_xhs_subtitle_urls(item)
        video_down_url = _extract_xhs_video_down_url(item)
        content_type_raw = _t(_first(item, ["type", "note_type"]))
        content_type = "video" if content_type_raw in {"video", "0", "normal"} else (content_type_raw or "note")

        work = build_work_item(
            platform="xiaohongshu",
            platform_work_id=note_id,
            platform_author_id=author_id,
            title=_t(_first(item, ["title", "desc"])),
            desc=_t(_first(item, ["desc", "title"])),
            publish_time=_t(_first(item, ["publish_time", "time", "create_time"])),
            content_type=content_type,
            duration_ms=_i(_first(item, ["duration_ms", "duration", "video_duration"], 0)),
            tags=list(_first(item, ["tag_list", "tags", "hashtags"], [])) if isinstance(_first(item, ["tag_list", "tags", "hashtags"], []), list) else [],
            metrics=metrics,
            cover_image=_t(_first(item, ["cover", "cover_url", "image"], "")),
            source_url=f"https://www.xiaohongshu.com/explore/{note_id}" if note_id else "",
            share_url=_t(_first(item, ["share_url", "url"])),
            video_down_url=video_down_url,
            asr_raw=subtitle_inline,
            asr_clean=subtitle_inline,
            asr_status="subtitle_ready" if subtitle_inline else "pending",
            asr_error_reason="",
            asr_source="xhs_subtitle" if subtitle_inline else "fallback_none",
            raw_ref={
                "note_id": note_id,
                "raw_item": item,
                "subtitle_inline": subtitle_inline,
                "subtitle_urls": subtitle_urls,
            },
        )
        work["author_platform_id"] = author_id
        work["author_handle"] = author_handle

        missing.extend(validate_work_item(work))
        works.append(work)

    missing.extend(validate_works_collection(works))
    return profile, works, missing
