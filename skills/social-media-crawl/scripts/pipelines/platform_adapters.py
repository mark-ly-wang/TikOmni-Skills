#!/usr/bin/env python3
"""Platform adapters: raw homepage payload -> normalized schema."""

from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List, Tuple

from scripts.pipelines.schema import (
    build_author_profile,
    build_work_item,
    validate_author_profile,
    validate_work_item,
    validate_works_collection,
)
from scripts.core.tikomni_common import deep_find_all, deep_find_first
from scripts.pipelines.select_low_quality_video_url import select_low_quality_video_url


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


def _extract_first_url(value: Any) -> str:
    if isinstance(value, str):
        text = value.strip()
        return text if text.startswith("http://") or text.startswith("https://") else ""
    if isinstance(value, list):
        for item in value:
            url = _extract_first_url(item)
            if url:
                return url
        return ""
    if isinstance(value, dict):
        for key in ("url_list", "url", "uri", "avatar_url", "cover_url", "src"):
            if key in value:
                url = _extract_first_url(value.get(key))
                if url:
                    return url
        return ""
    return ""


def _normalize_douyin_tags(value: Any) -> List[str]:
    if not isinstance(value, list):
        return []
    tags: List[str] = []
    for item in value:
        if isinstance(item, str):
            text = item.strip().lstrip("#")
            if text:
                tags.append(text)
            continue
        if not isinstance(item, dict):
            continue
        for key in ("hashtag_name", "search_text", "tag_name", "name", "text"):
            text = _t(item.get(key)).lstrip("#")
            if text:
                tags.append(text)
                break
    return list(dict.fromkeys(tags))


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


def _normalize_text_list(value: Any) -> List[str]:
    values: List[str] = []
    if isinstance(value, list):
        items = value
    else:
        items = [value]
    for item in items:
        if isinstance(item, str):
            text = item.strip().lstrip("#")
            if text:
                values.append(text)
            continue
        if not isinstance(item, dict):
            continue
        for key in ("name", "tag_name", "tag", "text", "display_text", "title"):
            text = _t(item.get(key)).lstrip("#")
            if text:
                values.append(text)
                break
    return list(dict.fromkeys(values))


def _extract_xhs_subtitle_inline(item: Dict[str, Any]) -> str:
    lines: List[str] = []
    for container in deep_find_all(
        item,
        [
            "subtitles",
            "subtitle_list",
            "subtitleList",
            "subtitle",
            "subtitle_text",
            "caption_text",
            "transcript",
            "transcript_text",
            "subtitle_content",
            "subtitle_inline",
        ],
    ):
        if isinstance(container, str):
            value = _t(container)
            if value:
                lines.append(value)
            continue
        if isinstance(container, list):
            for entry in container:
                if isinstance(entry, dict):
                    for key in ["text", "content", "sentence", "line", "subtitle_text", "caption_text"]:
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
    return _pick_http_urls(
        item,
        [
            "subtitle_url",
            "subtitleUrl",
            "srt_url",
            "srtUrl",
            "vtt_url",
            "vttUrl",
            "caption_url",
            "captionUrl",
            "subtitle_urls",
            "subtitleUrls",
        ],
    )


def _extract_xhs_work_modality(item: Dict[str, Any], *, video_download_url: str, subtitle_inline: str) -> str:
    content_type_raw = _t(_first(item, ["type", "note_type", "model_type"])).lower()
    if content_type_raw in {"video", "0", "normal", "mixed", "mix", "video_note", "note_video"}:
        return "video"
    if content_type_raw in {"image", "1", "photo", "album", "note", "text"}:
        return "text"
    if video_download_url or subtitle_inline:
        return "video"
    return "text"


def _extract_xhs_avatar_url(payload: Any) -> str:
    return (
        _extract_first_url(_first(payload, ["image"], ""))
        or _extract_first_url(_first(payload, ["avatar"], ""))
        or _extract_first_url(_first(payload, ["avatar_url"], ""))
        or _extract_first_url(_first(payload, ["images"], ""))
        or _extract_first_url(_first(payload, ["avatar_info"], ""))
    )


def _extract_xhs_cover_image(item: Dict[str, Any]) -> str:
    return (
        _extract_first_url(_first(item, ["cover"], ""))
        or _extract_first_url(_first(item, ["cover_url"], ""))
        or _extract_first_url(_first(item, ["cover_image"], ""))
        or _extract_first_url(_first(item, ["image"], ""))
        or _extract_first_url(_first(item, ["image_url"], ""))
        or _extract_first_url(_first(item, ["images"], ""))
    )


def _extract_xhs_share_url(item: Dict[str, Any], note_id: str) -> str:
    return (
        _t(_first(item, ["share_url", "share_link", "url", "note_url", "short_url"]))
        or (f"https://www.xiaohongshu.com/explore/{note_id}" if note_id else "")
    )


def _extract_xhs_source_url(item: Dict[str, Any], note_id: str) -> str:
    return (
        _t(_first(item, ["source_url", "note_url", "url", "share_url", "share_link"]))
        or (f"https://www.xiaohongshu.com/explore/{note_id}" if note_id else "")
    )


def _extract_xhs_title(item: Dict[str, Any]) -> str:
    return _t(_first(item, ["title", "display_title", "note_title", "name"]))


def _extract_xhs_caption(item: Dict[str, Any]) -> str:
    return _t(_first(item, ["desc", "content", "note_desc", "description", "text"]))


def _extract_xhs_tags(item: Dict[str, Any]) -> List[str]:
    for key in ("tag_list", "tags", "hashtags", "topics"):
        value = _first(item, [key], [])
        tags = _normalize_text_list(value)
        if tags:
            return tags
    return []


def _extract_xhs_profile_payload(raw: Dict[str, Any]) -> Any:
    profile_response = raw.get("profile_response") if isinstance(raw.get("profile_response"), dict) else {}
    profile_data = profile_response.get("data")
    if isinstance(profile_data, dict):
        return profile_data
    return profile_response


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
        author_handle=author_handle,
        nickname=_t(_first(profile_data, ["nickname", "name"])),
        ip_location=_t(_first(profile_data, ["ip_location", "ip_label", "ipLocation"])),
        fans_count=_i(_first(profile_data, ["follower_count", "fans_count", "mplatform_followers_count"])),
        liked_count=_i(_first(profile_data, ["total_favorited", "liked_count", "favoriting_count"])),
        collected_count=_i(_first(profile_data, ["collect_count", "collected_count", "total_collected_count"])),
        signature=_t(_first(profile_data, ["signature", "desc"])),
        avatar_url=(
            _extract_first_url(_first(profile_data, ["avatar_larger"], ""))
            or _extract_first_url(_first(profile_data, ["avatar_thumb"], ""))
            or _extract_first_url(_first(profile_data, ["avatar_url", "avatar"], ""))
        ),
        works_count=_i(_first(profile_data, ["aweme_count", "works_count", "video_count"])),
        verified=bool(_first(profile_data, ["verification_type", "verified"], 0) not in (0, None, "", "false", False)),
        snapshot_at=datetime.now().isoformat(timespec="seconds"),
        author_platform_id=stable_author_id or author_id,
        platform_native_refs={
            "douyin_sec_uid": internal_author_id,
            "douyin_author_platform_id": stable_author_id,
        },
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
        video_down_url = _extract_douyin_video_down_url(item)
        tags = _normalize_douyin_tags(_first(item, ["hashtags", "tags", "text_extra"], []))
        work = build_work_item(
            platform="douyin",
            platform_work_id=aweme_id,
            platform_author_id=author_id,
            author_handle=author_handle,
            author_platform_id=stable_author_id or author_id,
            title=_t(_first(item, ["title"])),
            caption_raw=_t(_first(item, ["desc"])),
            subtitle_raw="",
            subtitle_source="missing",
            publish_time=_t(_first(item, ["create_time", "publish_time"])),
            work_modality="video",
            content_type="video",
            duration_ms=_i(_first(item, ["duration_ms", "duration"], 0)),
            tags=tags,
            metrics=metrics,
            cover_image=(
                _extract_first_url(_first(item, ["cover_url"], ""))
                or _extract_first_url(_first(item, ["cover"], ""))
                or _extract_first_url(_first(item, ["origin_cover"], ""))
            ),
            source_url=f"https://www.douyin.com/video/{aweme_id}" if aweme_id else "",
            share_url=_t(_first(item, ["share_url", "share_link"])),
            video_download_url=video_down_url,
            asr_status="pending",
            asr_error_reason="",
            asr_source="fallback_none",
            platform_native_refs={
                "douyin_sec_uid": internal_author_id,
                "douyin_aweme_author_id": stable_author_id or author_id,
            },
            raw_ref={"aweme_id": aweme_id, "raw_item": item},
        )
        work.update(
            {
                "digg_count": metrics["like"],
                "comment_count": metrics["comment"],
                "collect_count": metrics["collect"],
                "share_count": metrics["share"],
                "play_count": metrics["play"],
            }
        )

        missing.extend(validate_work_item(work))
        works.append(work)

    missing.extend(validate_works_collection(works))
    return profile, works, missing


def adapt_xhs_author_home(raw: Dict[str, Any]) -> Tuple[Dict[str, Any], List[Dict[str, Any]], List[Dict[str, str]]]:
    missing: List[Dict[str, str]] = []
    profile_data = _extract_xhs_profile_payload(raw)

    author_id = _t(_first(profile_data, ["user_id", "userid", "id"], raw.get("resolved_author_id")))
    author_handle = _t(_first(profile_data, ["red_id", "redid", "display_id", "username"]))
    profile = build_author_profile(
        platform="xiaohongshu",
        platform_author_id=author_id,
        author_handle=author_handle,
        nickname=_t(_first(profile_data, ["nickname", "name"])),
        ip_location=_t(_first(profile_data, ["ip_location", "ip_location_desc", "ipLocation"])),
        fans_count=_i(_first(profile_data, ["fans", "fans_count", "follower_count", "followers"])),
        liked_count=_i(_first(profile_data, ["liked_count", "likes", "total_liked", "like_count"])),
        collected_count=_i(_first(profile_data, ["collected_count", "collect_count", "total_collected", "favorite_count"])),
        signature=_t(_first(profile_data, ["desc", "signature", "bio", "introduction"])),
        avatar_url=_extract_xhs_avatar_url(profile_data),
        works_count=_i(_first(profile_data, ["notes", "note_count", "works_count", "post_count"])),
        verified=bool(_first(profile_data, ["official_verified", "verified"], False)),
        snapshot_at=datetime.now().isoformat(timespec="seconds"),
        author_platform_id=author_id,
        platform_native_refs={"xhs_user_id": author_id, "xhs_red_id": author_handle},
    )

    missing.extend(validate_author_profile(profile))

    works: List[Dict[str, Any]] = []
    for item in raw.get("works", []):
        if not isinstance(item, dict):
            continue
        note_id = _t(_first(item, ["note_id", "id", "item_id"]))
        metrics = {
            "like": _i(_first(item, ["liked_count", "like_count", "digg_count"], 0)),
            "comment": _i(_first(item, ["comment_count"], 0)),
            "collect": _i(_first(item, ["collected_count", "collect_count"], 0)),
            "share": _i(_first(item, ["share_count"], 0)),
            "play": _i(_first(item, ["view_count", "play_count"], 0)),
        }
        subtitle_inline = _extract_xhs_subtitle_inline(item)
        subtitle_urls = _extract_xhs_subtitle_urls(item)
        video_down_url = _extract_xhs_video_down_url(item)
        content_type_raw = _t(_first(item, ["type", "note_type", "model_type"]))
        work_modality = _extract_xhs_work_modality(item, video_download_url=video_down_url, subtitle_inline=subtitle_inline)
        content_type = "video" if work_modality == "video" else (content_type_raw or "text")
        cover_image = _extract_xhs_cover_image(item)
        source_url = _extract_xhs_source_url(item, note_id)
        share_url = _extract_xhs_share_url(item, note_id)

        work = build_work_item(
            platform="xiaohongshu",
            platform_work_id=note_id,
            platform_author_id=author_id,
            author_handle=author_handle,
            author_platform_id=author_id,
            title=_extract_xhs_title(item),
            caption_raw=_extract_xhs_caption(item),
            subtitle_raw=subtitle_inline,
            subtitle_source="native_subtitle" if subtitle_inline else "missing",
            publish_time=_t(_first(item, ["publish_time", "time", "create_time", "publishTime", "created_at"])),
            work_modality=work_modality,
            content_type=content_type,
            duration_ms=_i(_first(item, ["duration_ms", "duration", "video_duration"], 0)),
            tags=_extract_xhs_tags(item),
            metrics=metrics,
            cover_image=cover_image,
            source_url=source_url,
            share_url=share_url,
            video_download_url=video_down_url,
            asr_status="subtitle_ready" if subtitle_inline else "pending",
            asr_error_reason="",
            asr_source="native_subtitle" if subtitle_inline else "fallback_none",
            platform_native_refs={"xhs_user_id": author_id, "xhs_red_id": author_handle},
            raw_ref={
                "note_id": note_id,
                "raw_item": item,
                "subtitle_inline": subtitle_inline,
                "subtitle_urls": subtitle_urls,
            },
        )
        work.update(
            {
                "digg_count": metrics["like"],
                "comment_count": metrics["comment"],
                "collect_count": metrics["collect"],
                "share_count": metrics["share"],
                "play_count": metrics["play"],
            }
        )

        missing.extend(validate_work_item(work))
        works.append(work)

    missing.extend(validate_works_collection(works))
    return profile, works, missing
