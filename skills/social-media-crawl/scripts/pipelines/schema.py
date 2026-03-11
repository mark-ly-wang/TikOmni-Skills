#!/usr/bin/env python3
"""Schema definitions and minimal validators for social-media-crawl."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import datetime, timedelta, timezone
from typing import Any, Dict, List, Optional


DISPLAY_TIMEZONE = timezone(timedelta(hours=8))
SUBTITLE_SOURCE_ENUM = {"native_subtitle", "external_asr", "missing"}
ASR_SOURCE_ENUM = {"native_subtitle", "external_asr", "fallback_none"}
WORK_MODALITY_ENUM = {"video", "text"}
PRIMARY_TEXT_SOURCE_ENUM = {"asr_clean", "caption_raw"}
ANALYSIS_ELIGIBILITY_ENUM = {"eligible", "incomplete"}


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


def _to_bool(value: Any, default: bool = False) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, (int, float)):
        return bool(int(value))
    text = _to_text(value).lower()
    if not text:
        return default
    if text in {"1", "true", "yes", "y", "video"}:
        return True
    if text in {"0", "false", "no", "n", "text", "image", "photo", "note"}:
        return False
    return default


def _normalize_timestamp(value: Any) -> Optional[datetime]:
    if value is None:
        return None
    if isinstance(value, datetime):
        dt = value
        if dt.tzinfo is None:
            return dt.replace(tzinfo=DISPLAY_TIMEZONE)
        return dt.astimezone(DISPLAY_TIMEZONE)

    if isinstance(value, (int, float)):
        timestamp = float(value)
    else:
        text = _to_text(value)
        if not text:
            return None
        try:
            timestamp = float(text)
        except Exception:
            normalized = text.replace("Z", "+00:00")
            try:
                dt = datetime.fromisoformat(normalized)
            except Exception:
                for fmt in ("%Y-%m-%d", "%Y/%m/%d", "%Y-%m-%d %H:%M:%S", "%Y/%m/%d %H:%M:%S"):
                    try:
                        dt = datetime.strptime(text, fmt)
                        break
                    except Exception:
                        dt = None
                if dt is None:
                    return None
                return dt.replace(tzinfo=DISPLAY_TIMEZONE)

            if dt.tzinfo is None:
                return dt.replace(tzinfo=DISPLAY_TIMEZONE)
            return dt.astimezone(DISPLAY_TIMEZONE)

    if abs(timestamp) >= 1_000_000_000_000:
        timestamp /= 1000.0
    if timestamp <= 0:
        return None
    return datetime.fromtimestamp(timestamp, tz=timezone.utc).astimezone(DISPLAY_TIMEZONE)


def _format_published_date(value: Any) -> str:
    dt = _normalize_timestamp(value)
    return dt.strftime("%Y-%m-%d") if dt else "N/A"


def _infer_work_modality(*, work_modality: str, is_video: Any, content_type: str, subtitle_raw: str, video_download_url: str) -> str:
    modality = _to_text(work_modality).lower()
    if modality in WORK_MODALITY_ENUM:
        return modality

    if _to_bool(is_video, default=False):
        return "video"

    content_type_value = _to_text(content_type).lower()
    if content_type_value in {"video", "mixed", "mix", "video_note", "note_video", "normal", "0"}:
        return "video"
    if content_type_value in {"text", "note", "image", "photo", "album", "1"}:
        return "text"

    if subtitle_raw or video_download_url:
        return "video"
    return "text"


def _infer_primary_text(*, work_modality: str, caption_raw: str, asr_clean: str) -> str:
    if work_modality == "video":
        return asr_clean
    return caption_raw


def _infer_primary_text_source(*, work_modality: str, caption_raw: str, asr_clean: str) -> str:
    if work_modality == "video":
        return "asr_clean"
    return "caption_raw"


def _infer_analysis_state(*, work_modality: str, caption_raw: str, asr_raw: str, video_download_url: str) -> Dict[str, str]:
    if work_modality == "video":
        if asr_raw:
            return {"analysis_eligibility": "eligible", "analysis_exclusion_reason": ""}
        return {
            "analysis_eligibility": "incomplete",
            "analysis_exclusion_reason": "video_asr_unavailable",
        }

    if caption_raw:
        return {"analysis_eligibility": "eligible", "analysis_exclusion_reason": ""}
    return {
        "analysis_eligibility": "incomplete",
        "analysis_exclusion_reason": "caption_raw_missing",
    }


@dataclass
class AuthorProfileNormalized:
    platform: str
    platform_author_id: str
    author_handle: str
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
    author_platform_id: str = ""
    platform_native_refs: Dict[str, Any] = field(default_factory=dict)


@dataclass
class WorkItemNormalized:
    platform: str
    platform_work_id: str
    platform_author_id: str
    author_handle: str
    title: str
    caption_raw: str
    work_modality: str
    published_date: str
    duration_ms: int
    tags: List[str] = field(default_factory=list)
    metrics: Dict[str, int] = field(default_factory=dict)
    cover_image: str = ""
    source_url: str = ""
    share_url: str = ""
    video_download_url: str = ""
    primary_text: str = ""
    primary_text_source: str = "caption_raw"
    analysis_eligibility: str = "eligible"
    analysis_exclusion_reason: str = ""
    platform_native_refs: Dict[str, Any] = field(default_factory=dict)
    raw_ref: Dict[str, Any] = field(default_factory=dict)
    author_platform_id: str = ""
    subtitle_raw: str = ""
    subtitle_source: str = "missing"
    publish_time: str = ""
    create_time_sec: int = 0
    content_type: str = ""
    video_down_url: str = ""
    asr_raw: str = ""
    asr_clean: str = ""
    asr_status: str = "pending"
    asr_error_reason: str = ""
    asr_source: str = "fallback_none"
    is_video: bool = False


def validate_author_profile(payload: Dict[str, Any]) -> List[Dict[str, str]]:
    required_types = {
        "platform": str,
        "platform_author_id": str,
        "author_handle": str,
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
        "author_handle": str,
        "title": str,
        "caption_raw": str,
        "work_modality": str,
        "published_date": str,
        "duration_ms": int,
        "tags": list,
        "metrics": dict,
        "cover_image": str,
        "source_url": str,
        "share_url": str,
        "video_download_url": str,
        "primary_text": str,
        "primary_text_source": str,
        "analysis_eligibility": str,
        "analysis_exclusion_reason": str,
        "platform_native_refs": dict,
        "raw_ref": dict,
        "subtitle_raw": str,
        "subtitle_source": str,
        "publish_time": str,
        "content_type": str,
        "video_down_url": str,
        "asr_raw": str,
        "asr_clean": str,
        "asr_status": str,
        "asr_error_reason": str,
        "asr_source": str,
    }
    missing: List[Dict[str, str]] = []
    for key, expected in required_types.items():
        if key not in payload:
            missing.append({"field": key, "reason": "missing"})
            continue
        if not isinstance(payload.get(key), expected):
            missing.append({"field": key, "reason": f"type_error:{expected.__name__}"})

    for key in ("platform", "platform_work_id", "platform_author_id"):
        value = payload.get(key)
        if isinstance(value, str) and not value.strip():
            missing.append({"field": key, "reason": "empty_value"})

    if not any(_to_text(payload.get(key)) for key in ("title", "caption_raw", "asr_raw")):
        missing.append({"field": "title|caption_raw|asr_raw", "reason": "all_empty"})

    if _to_text(payload.get("work_modality")) not in WORK_MODALITY_ENUM:
        missing.append({"field": "work_modality", "reason": "invalid_enum"})

    if _to_text(payload.get("primary_text_source")) not in PRIMARY_TEXT_SOURCE_ENUM:
        missing.append({"field": "primary_text_source", "reason": "invalid_enum"})

    if _to_text(payload.get("analysis_eligibility")) not in ANALYSIS_ELIGIBILITY_ENUM:
        missing.append({"field": "analysis_eligibility", "reason": "invalid_enum"})

    subtitle_source = payload.get("subtitle_source")
    if isinstance(subtitle_source, str) and subtitle_source not in SUBTITLE_SOURCE_ENUM:
        missing.append({"field": "subtitle_source", "reason": "invalid_enum"})

    asr_source = payload.get("asr_source")
    if isinstance(asr_source, str) and asr_source not in ASR_SOURCE_ENUM:
        missing.append({"field": "asr_source", "reason": "invalid_enum"})
    return missing


def validate_works_collection(works: Any) -> List[Dict[str, str]]:
    if not isinstance(works, list):
        return [{"field": "works", "reason": "type_error:list"}]
    if not works:
        return [{"field": "works", "reason": "empty_collection"}]
    return []


def build_author_profile(**kwargs: Any) -> Dict[str, Any]:
    platform_author_id = _to_text(kwargs.get("platform_author_id"))
    profile = AuthorProfileNormalized(
        platform=_to_text(kwargs.get("platform")),
        platform_author_id=platform_author_id,
        author_handle=_to_text(kwargs.get("author_handle")),
        nickname=_to_text(kwargs.get("nickname")),
        ip_location=_to_text(kwargs.get("ip_location")),
        fans_count=_to_int(kwargs.get("fans_count")),
        liked_count=_to_int(kwargs.get("liked_count")),
        collected_count=_to_int(kwargs.get("collected_count")),
        signature=_to_text(kwargs.get("signature")),
        avatar_url=_to_text(kwargs.get("avatar_url")),
        works_count=_to_int(kwargs.get("works_count")),
        verified=bool(kwargs.get("verified", False)),
        snapshot_at=_to_text(kwargs.get("snapshot_at")) or datetime.now(tz=DISPLAY_TIMEZONE).isoformat(timespec="seconds"),
        author_platform_id=_to_text(kwargs.get("author_platform_id")) or platform_author_id,
        platform_native_refs=dict(kwargs.get("platform_native_refs") or {}),
    )
    return asdict(profile)


def build_work_item(**kwargs: Any) -> Dict[str, Any]:
    caption_raw = _to_text(kwargs.get("caption_raw") if kwargs.get("caption_raw") is not None else kwargs.get("desc"))
    subtitle_raw = _to_text(kwargs.get("subtitle_raw"))
    subtitle_source = _to_text(kwargs.get("subtitle_source")) or ("native_subtitle" if subtitle_raw else "missing")
    asr_raw = _to_text(kwargs.get("asr_raw")) or subtitle_raw
    asr_clean = _to_text(kwargs.get("asr_clean")) or asr_raw
    video_download_url = _to_text(kwargs.get("video_download_url") if kwargs.get("video_download_url") is not None else kwargs.get("video_down_url"))
    work_modality = _infer_work_modality(
        work_modality=_to_text(kwargs.get("work_modality")),
        is_video=kwargs.get("is_video"),
        content_type=_to_text(kwargs.get("content_type")),
        subtitle_raw=subtitle_raw,
        video_download_url=video_download_url,
    )
    primary_text = _to_text(kwargs.get("primary_text")) or _infer_primary_text(
        work_modality=work_modality,
        caption_raw=caption_raw,
        asr_clean=asr_clean,
    )
    primary_text_source_raw = _to_text(kwargs.get("primary_text_source"))
    primary_text_source = (
        primary_text_source_raw
        if primary_text_source_raw in PRIMARY_TEXT_SOURCE_ENUM
        else _infer_primary_text_source(
            work_modality=work_modality,
            caption_raw=caption_raw,
            asr_clean=asr_clean,
        )
    )
    analysis_state = _infer_analysis_state(
        work_modality=work_modality,
        caption_raw=caption_raw,
        asr_raw=asr_raw,
        video_download_url=video_download_url,
    )
    item = WorkItemNormalized(
        platform=_to_text(kwargs.get("platform")),
        platform_work_id=_to_text(kwargs.get("platform_work_id")),
        platform_author_id=_to_text(kwargs.get("platform_author_id")),
        author_handle=_to_text(kwargs.get("author_handle")),
        title=_to_text(kwargs.get("title")),
        caption_raw=caption_raw,
        work_modality=work_modality,
        published_date=_to_text(kwargs.get("published_date")) or _format_published_date(kwargs.get("publish_time")),
        duration_ms=_to_int(kwargs.get("duration_ms")),
        tags=list(kwargs.get("tags") or []),
        metrics=dict(kwargs.get("metrics") or {}),
        cover_image=_to_text(kwargs.get("cover_image")),
        source_url=_to_text(kwargs.get("source_url")),
        share_url=_to_text(kwargs.get("share_url")) or _to_text(kwargs.get("source_url")),
        video_download_url=video_download_url,
        primary_text=primary_text,
        primary_text_source=primary_text_source,
        analysis_eligibility=_to_text(kwargs.get("analysis_eligibility")) or analysis_state["analysis_eligibility"],
        analysis_exclusion_reason=_to_text(kwargs.get("analysis_exclusion_reason")) or analysis_state["analysis_exclusion_reason"],
        platform_native_refs=dict(kwargs.get("platform_native_refs") or {}),
        raw_ref=dict(kwargs.get("raw_ref") or {}),
        author_platform_id=_to_text(kwargs.get("author_platform_id")) or _to_text(kwargs.get("platform_author_id")),
        subtitle_raw=subtitle_raw,
        subtitle_source=subtitle_source,
        publish_time=_to_text(kwargs.get("publish_time")),
        create_time_sec=_to_int(kwargs.get("create_time_sec")),
        content_type=_to_text(kwargs.get("content_type")),
        video_down_url=video_download_url,
        asr_raw=asr_raw,
        asr_clean=asr_clean,
        asr_status=_to_text(kwargs.get("asr_status")) or ("success" if asr_raw else "pending"),
        asr_error_reason=_to_text(kwargs.get("asr_error_reason")),
        asr_source=_to_text(kwargs.get("asr_source")) or (
            "native_subtitle"
            if subtitle_source == "native_subtitle" and subtitle_raw
            else ("external_asr" if subtitle_source == "external_asr" and asr_raw else "fallback_none")
        ),
        is_video=work_modality == "video",
    )
    return asdict(item)
