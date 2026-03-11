#!/usr/bin/env python3
"""Write work fact cards and normalized envelopes."""

from __future__ import annotations

import json
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

from scripts.core.completeness import ensure_request_id, evaluate_work_fact_card, normalize_missing_fields
from scripts.core.config_loader import resolve_storage_paths
from scripts.core.storage_router import (
    build_work_fact_card_paths,
    render_output_filename,
    resolve_card_root,
    resolve_json_filename_pattern,
)

SHANGHAI_TZ = timezone(timedelta(hours=8))


def _safe_text(value: Any) -> str:
    if value is None:
        return ""
    return str(value).strip()


def _safe_int(value: Any) -> int:
    if value is None:
        return 0
    if isinstance(value, bool):
        return int(value)
    if isinstance(value, int):
        return value
    if isinstance(value, float):
        return int(value)
    text = _safe_text(value)
    if not text:
        return 0
    try:
        return int(float(text.replace(",", "")))
    except Exception:
        return 0


def _safe_optional_int(value: Any) -> Optional[int]:
    if value is None:
        return None
    if isinstance(value, bool):
        return int(value)
    if isinstance(value, int):
        return value
    if isinstance(value, float):
        return int(value)
    text = _safe_text(value)
    if not text:
        return None
    try:
        return int(float(text.replace(",", "")))
    except Exception:
        return None


def _source_dict(payload: Dict[str, Any]) -> Dict[str, Any]:
    source = payload.get("source")
    return source if isinstance(source, dict) else {}


def _author_dict(payload: Dict[str, Any]) -> Dict[str, Any]:
    author = payload.get("author")
    return author if isinstance(author, dict) else {}


def _resolve_platform(payload: Dict[str, Any], platform: Optional[str]) -> str:
    return _safe_text(platform or payload.get("platform")) or "unknown"


def _resolve_work_id(payload: Dict[str, Any]) -> str:
    for key in ("platform_work_id", "note_id", "aweme_id", "id"):
        hit = _safe_text(payload.get(key))
        if hit:
            return hit
    source = _source_dict(payload)
    for key in ("note_id", "platform_work_id"):
        hit = _safe_text(source.get(key))
        if hit:
            return hit
    return ""


def _resolve_author_display(payload: Dict[str, Any]) -> str:
    author_raw = payload.get("author")
    author_obj = _author_dict(payload)
    if isinstance(author_raw, str) and _safe_text(author_raw):
        return _safe_text(author_raw)
    for key in ("nickname", "author_handle", "platform_author_id"):
        hit = _safe_text(author_obj.get(key))
        if hit:
            return hit
    for key in ("nickname", "author_handle", "platform_author_id"):
        hit = _safe_text(payload.get(key))
        if hit:
            return hit
    return ""


def _resolve_author_handle(payload: Dict[str, Any]) -> str:
    author_obj = _author_dict(payload)
    source = _source_dict(payload)
    for key in ("author_handle", "short_id", "red_id"):
        for container in (payload, author_obj, source):
            hit = _safe_text(container.get(key))
            if hit:
                return hit
    return _resolve_author_display(payload)


def _resolve_platform_author_id(payload: Dict[str, Any]) -> str:
    author_obj = _author_dict(payload)
    source = _source_dict(payload)
    for key in (
        "platform_author_id",
        "author_platform_id",
        "xhs_user_id",
        "douyin_aweme_author_id",
        "uid",
    ):
        for container in (payload, author_obj, source):
            hit = _safe_text(container.get(key))
            if hit:
                return hit
    return ""


def _resolve_title(payload: Dict[str, Any]) -> str:
    for key in ("title", "display_title", "name"):
        hit = _safe_text(payload.get(key))
        if hit:
            return hit
    caption = _resolve_caption(payload)
    return caption[:60] if caption else ""


def _resolve_caption(payload: Dict[str, Any]) -> str:
    source = _source_dict(payload)
    for key in ("caption_raw", "desc", "content", "raw_content", "summary"):
        for container in (payload, source):
            hit = _safe_text(container.get(key))
            if hit:
                return hit
    return ""


def _to_timestamp(value: Any) -> Optional[int]:
    raw = _safe_int(value)
    if raw <= 0:
        return None
    if raw > 1_000_000_000_000:
        raw //= 1000
    return raw if raw > 0 else None


def _resolve_published_date(payload: Dict[str, Any]) -> str:
    for key in ("published_date", "publish_time_text"):
        hit = _safe_text(payload.get(key))
        if hit:
            return hit[:10] if len(hit) >= 10 else hit
    for key in ("publish_time", "create_time_sec", "create_time", "time"):
        ts = _to_timestamp(payload.get(key))
        if ts:
            return datetime.fromtimestamp(ts, tz=SHANGHAI_TZ).strftime("%Y-%m-%d")
    return ""


def _resolve_work_modality(payload: Dict[str, Any]) -> str:
    modality = _safe_text(payload.get("work_modality")).lower()
    if modality:
        return modality
    content_type = _safe_text(payload.get("note_content_type") or payload.get("content_type")).lower()
    if content_type in {"video", "single_video", "video_note"}:
        return "video"
    if content_type in {"image", "photo", "text", "note"}:
        return "text"
    if payload.get("is_video") is True:
        return "video"
    return "video" if _safe_text(payload.get("video_download_url") or payload.get("video_down_url")) else "text"


def _resolve_source_url(payload: Dict[str, Any], platform: str, work_id: str) -> str:
    source = _source_dict(payload)
    for key in ("source_url", "url", "note_url"):
        for container in (payload, source):
            hit = _safe_text(container.get(key))
            if hit:
                return hit
    if platform == "douyin" and work_id:
        return f"https://www.douyin.com/video/{work_id}"
    if platform == "xiaohongshu" and work_id:
        return f"https://www.xiaohongshu.com/explore/{work_id}"
    return ""


def _resolve_share_url(payload: Dict[str, Any], source_url: str) -> str:
    source = _source_dict(payload)
    for key in ("share_url", "share_link", "share_text"):
        for container in (payload, source):
            hit = _safe_text(container.get(key))
            if hit:
                return hit
    return source_url


def _resolve_primary_text(payload: Dict[str, Any], caption_raw: str) -> Dict[str, str]:
    subtitle_raw = _safe_text(payload.get("subtitle_raw"))
    asr_clean = _safe_text(payload.get("asr_clean"))
    asr_raw = _safe_text(payload.get("asr_raw"))
    if subtitle_raw:
        return {"primary_text": subtitle_raw, "primary_text_source": "subtitle_raw"}
    if asr_clean:
        return {"primary_text": asr_clean, "primary_text_source": "asr_clean"}
    if asr_raw:
        return {"primary_text": asr_raw, "primary_text_source": "asr_raw"}
    if caption_raw:
        return {"primary_text": caption_raw, "primary_text_source": "caption_raw"}
    return {"primary_text": "", "primary_text_source": "missing"}


def build_work_fact_card(payload: Dict[str, Any], platform: Optional[str] = None) -> Dict[str, Any]:
    platform_name = _resolve_platform(payload, platform)
    work_id = _resolve_work_id(payload)
    caption_raw = _resolve_caption(payload)
    source_url = _resolve_source_url(payload, platform_name, work_id)
    share_url = _resolve_share_url(payload, source_url)
    author_handle = _resolve_author_handle(payload)
    platform_author_id = _resolve_platform_author_id(payload)
    primary_text_bundle = _resolve_primary_text(payload, caption_raw)

    card: Dict[str, Any] = {
        "platform": platform_name,
        "platform_work_id": work_id,
        "platform_author_id": platform_author_id,
        "author_handle": author_handle,
        "author": _resolve_author_display(payload),
        "title": _resolve_title(payload),
        "caption_raw": caption_raw,
        "subtitle_raw": _safe_text(payload.get("subtitle_raw")),
        "work_modality": _resolve_work_modality(payload),
        "publish_time": payload.get("publish_time"),
        "create_time_sec": payload.get("create_time_sec"),
        "publish_time_source": _safe_text(payload.get("publish_time_source")),
        "published_date": _resolve_published_date(payload),
        "digg_count": _safe_int(payload.get("digg_count")),
        "comment_count": _safe_int(payload.get("comment_count")),
        "collect_count": _safe_int(payload.get("collect_count")),
        "share_count": _safe_int(payload.get("share_count")),
        "play_count": _safe_optional_int(payload.get("play_count")),
        "cover_image": _safe_text(payload.get("cover_image")),
        "source_url": source_url,
        "share_url": share_url,
        "video_download_url": _safe_text(payload.get("video_download_url") or payload.get("video_down_url")),
        "primary_text": primary_text_bundle["primary_text"],
        "primary_text_source": primary_text_bundle["primary_text_source"],
        "asr_raw": _safe_text(payload.get("asr_raw")),
        "asr_clean": _safe_text(payload.get("asr_clean")),
        "request_id": ensure_request_id(_safe_text(payload.get("request_id")), fallback_seed=share_url or work_id or caption_raw),
        "missing_fields": normalize_missing_fields(payload.get("missing_fields")),
        "error_reason": _safe_text(payload.get("error_reason")) or None,
        "extract_trace": payload.get("extract_trace") if isinstance(payload.get("extract_trace"), list) else [],
    }
    existing_missing = {(entry.get("field"), entry.get("reason")) for entry in card["missing_fields"]}
    if (
        card["work_modality"] == "video"
        and not card["asr_clean"]
        and not card["asr_raw"]
        and not card["subtitle_raw"]
        and ("asr_clean", "caption_fallback") not in existing_missing
    ):
        card["missing_fields"].append({"field": "asr_clean", "reason": "caption_fallback"})
    evaluation = evaluate_work_fact_card(card)
    card["completeness"] = evaluation["completeness"]
    card["missing_fields"] = evaluation["missing_fields"]
    return card


def build_work_output_envelope(payload: Dict[str, Any], platform: Optional[str] = None) -> Dict[str, Any]:
    card = build_work_fact_card(payload, platform=platform)
    source = _source_dict(payload)
    input_value = source.get("share_url") or source.get("share_text") or source.get("source_url") or source
    return {
        "object_type": "work",
        "platform": card["platform"],
        "input": input_value,
        "normalized": card,
        "completeness": card["completeness"],
        "missing_fields": card["missing_fields"],
        "error_reason": card.get("error_reason"),
        "extract_trace": card.get("extract_trace", []),
        "request_id": card["request_id"],
    }


def _yaml_scalar(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        return str(value)
    text = _safe_text(value)
    if not text:
        return ""
    return json.dumps(text, ensure_ascii=False)


def _frontmatter_lines(card: Dict[str, Any]) -> List[str]:
    fields = [
        ("card_type", "work"),
        ("platform", card.get("platform")),
        ("platform_work_id", card.get("platform_work_id")),
        ("platform_author_id", card.get("platform_author_id")),
        ("author_handle", card.get("author_handle")),
        ("author", card.get("author")),
        ("title", card.get("title")),
        ("published_date", card.get("published_date")),
        ("work_modality", card.get("work_modality")),
        ("digg_count", card.get("digg_count")),
        ("comment_count", card.get("comment_count")),
        ("collect_count", card.get("collect_count")),
        ("share_count", card.get("share_count")),
        ("play_count", card.get("play_count")),
        ("cover_image", card.get("cover_image")),
        ("source_url", card.get("source_url")),
        ("share_url", card.get("share_url")),
        ("video_download_url", card.get("video_download_url")),
        ("primary_text_source", card.get("primary_text_source")),
        ("completeness", card.get("completeness")),
        ("request_id", card.get("request_id")),
        ("error_reason", card.get("error_reason")),
    ]
    lines = ["---"]
    for key, value in fields:
        rendered = _yaml_scalar(value)
        lines.append(f"{key}: {rendered}" if rendered else f"{key}:")
    lines.append("---")
    return lines


def _markdown_lines(card: Dict[str, Any]) -> List[str]:
    lines = _frontmatter_lines(card)
    primary_text = _safe_text(card.get("primary_text"))
    caption_raw = _safe_text(card.get("caption_raw"))
    subtitle_raw = _safe_text(card.get("subtitle_raw"))
    asr_raw = _safe_text(card.get("asr_raw"))

    lines.extend(["", "## 主文本", primary_text or ""])
    if caption_raw and caption_raw != primary_text:
        lines.extend(["", "## 原始文案", caption_raw])
    if subtitle_raw and subtitle_raw != primary_text:
        lines.extend(["", "## 原始字幕", subtitle_raw])
    if asr_raw and asr_raw not in {primary_text, subtitle_raw}:
        lines.extend(["", "## 原始转写", asr_raw])
    if card.get("missing_fields"):
        lines.extend(["", "## 缺失字段"])
        for entry in card["missing_fields"]:
            lines.append(f"- {entry.get('field')}: {entry.get('reason')}")
    return lines


def write_work_fact_card(
    *,
    payload: Dict[str, Any],
    platform: Optional[str] = None,
    card_root: Optional[str] = None,
    storage_config: Optional[Dict[str, Any]] = None,
    **_: Any,
) -> Dict[str, Any]:
    card = build_work_fact_card(payload, platform=platform)
    published_date = card["published_date"] or _resolve_published_date(payload)
    resolved_card_root = resolve_card_root(storage_config, explicit_card_root=card_root)
    fallback_identifier = card["share_url"] or card["source_url"] or card["title"] or card["request_id"]
    paths = build_work_fact_card_paths(
        card_root=resolved_card_root,
        platform=card["platform"],
        platform_work_id=card["platform_work_id"],
        author_handle=card["author_handle"],
        platform_author_id=card["platform_author_id"],
        author_name=card["author"],
        title=card["title"],
        published_date=published_date,
        storage_config=storage_config,
        fallback_identifier=fallback_identifier,
    )

    Path(paths["markdown_path"]).write_text(
        "\n".join(_markdown_lines(card)).strip() + "\n",
        encoding="utf-8",
    )

    return {
        "enabled": True,
        "ok": True,
        "count": 1,
        "path": paths["markdown_path"],
        "json_path": None,
        "markdown_path": paths["markdown_path"],
        "route": paths["route"],
        "identifier": paths["identifier"],
        "card": card,
    }


def persist_output_envelope(
    *,
    envelope: Dict[str, Any],
    storage_config: Optional[Dict[str, Any]],
    platform: str,
    fallback_identifier: str,
) -> Dict[str, Any]:
    try:
        paths = resolve_storage_paths(storage_config or {})
    except Exception as error:
        return {"enabled": True, "ok": False, "error": f"resolve_storage_paths_failed:{error}"}

    now = datetime.now()
    date_key = now.strftime("%Y%m%d")
    timestamp = now.strftime("%Y%m%dT%H%M%S")
    identifier = _safe_text(envelope.get("normalized", {}).get("platform_work_id")) or fallback_identifier
    status = "error" if envelope.get("error_reason") else "success"

    target_root = Path(paths["errors_root"] if status == "error" else paths["results_root"]) / date_key
    target_root.mkdir(parents=True, exist_ok=True)
    file_name = render_output_filename(
        pattern=resolve_json_filename_pattern(storage_config),
        context={
            "platform": platform,
            "identifier": identifier,
            "timestamp": timestamp,
            "date": date_key,
            "ext": ".json",
        },
        default_filename=f"{timestamp}-{platform}-{identifier}.json",
        default_ext=".json",
    )
    file_path = target_root / file_name
    file_path.write_text(json.dumps(envelope, ensure_ascii=False, indent=2), encoding="utf-8")
    return {"enabled": True, "ok": True, "status": status, "path": str(file_path)}
