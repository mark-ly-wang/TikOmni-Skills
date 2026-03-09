#!/usr/bin/env python3

if __package__ in {None, ""}:
    import sys
    from pathlib import Path

    _self = Path(__file__).resolve()
    for _parent in _self.parents:
        if (_parent / "scripts").is_dir():
            sys.path.insert(0, str(_parent))
            break

"""Write single-work benchmark markdown cards into card root zones."""

import argparse
import datetime as dt
import json
import os
import re
import time
import unicodedata
from pathlib import Path
from typing import Any, Dict, List, Optional

try:
    from zoneinfo import ZoneInfo
except Exception:  # pragma: no cover
    ZoneInfo = None

from scripts.core.analysis_pipeline import (
    DEFAULT_MODULE_SECTIONS,
    build_analysis_sections,
    ensure_analysis_sections_schema,
)
from scripts.core.config_loader import load_tikomni_config
from scripts.core.progress_report import ProgressReporter
from scripts.core.storage_router import build_card_output_path, normalize_card_type, resolve_effective_card_type
from scripts.core.tikomni_common import normalize_text, read_json_file, write_json_stdout
from scripts.pipeline.asr.asr_pipeline import derive_asr_clean_text


CARD_TYPES = ["work"]


def resolve_default_card_root() -> str:
    raw = os.getenv("TIKOMNI_CARD_ROOT", "").strip()
    if not raw:
        raise ValueError("missing_card_root: set --card-root or define TIKOMNI_CARD_ROOT in .env/.env.local")

    candidate = Path(raw).expanduser()
    if not candidate.is_absolute():
        raise ValueError("TIKOMNI_CARD_ROOT must be an absolute path")
    return str(candidate.resolve())


DEFAULT_CARD_ROOT = ""


def _safe_int(value: Any, default: int = 0) -> int:
    if value is None:
        return default
    if isinstance(value, bool):
        return int(value)
    if isinstance(value, int):
        return value
    if isinstance(value, float):
        return int(value)
    text = str(value).strip()
    if not text:
        return default
    try:
        return int(float(text))
    except Exception:
        return default


def _safe_optional_int(value: Any) -> Optional[int]:
    if value is None:
        return None
    if isinstance(value, bool):
        return int(value)
    if isinstance(value, int):
        return value
    if isinstance(value, float):
        return int(value)
    text = str(value).strip()
    if not text:
        return None
    try:
        return int(float(text))
    except Exception:
        return None


def _display_metric(value: Optional[int]) -> str:
    return "N/A" if value is None else str(value)


def _source_dict(payload: Dict[str, Any]) -> Dict[str, Any]:
    source = payload.get("source")
    return source if isinstance(source, dict) else {}


def _pick_text(payload: Dict[str, Any], keys: List[str], source_keys: Optional[List[str]] = None) -> str:
    source = _source_dict(payload)
    for key in keys:
        text = normalize_text(payload.get(key))
        if text:
            return text
    for key in (source_keys or keys):
        text = normalize_text(source.get(key))
        if text:
            return text
    return ""


def _to_unix_sec(value: Any) -> int:
    parsed = _safe_int(value, default=0)
    if parsed <= 0:
        return 0
    if parsed > 1_000_000_000_000:
        parsed //= 1000
    return parsed


def _format_shanghai_datetime(value: Any) -> str:
    ts = _to_unix_sec(value)
    if ts <= 0:
        return ""
    try:
        if ZoneInfo is not None:
            dt_obj = dt.datetime.fromtimestamp(ts, tz=ZoneInfo("Asia/Shanghai"))
        else:
            dt_obj = dt.datetime.fromtimestamp(ts, tz=dt.timezone(dt.timedelta(hours=8)))
        return dt_obj.strftime("%Y-%m-%d %H:%M:%S")
    except Exception:
        return ""


def _resolve_published_date(payload: Dict[str, Any], create_time_sec: int) -> str:
    published_date = normalize_text(payload.get("published_date"))
    if published_date:
        return published_date
    publish_time_text = normalize_text(payload.get("publish_time_text"))
    if publish_time_text:
        return publish_time_text[:10]

    source = _source_dict(payload)
    for key in ("publish_time", "create_time", "time"):
        text = _format_shanghai_datetime(payload.get(key))
        if text:
            return text[:10]
        text = _format_shanghai_datetime(source.get(key))
        if text:
            return text[:10]

    fallback = _format_shanghai_datetime(create_time_sec)
    return fallback[:10] if fallback else "N/A"


def _extract_duration_ms(payload: Dict[str, Any]) -> int:
    source = _source_dict(payload)
    for base in (payload, source):
        for key in ("duration_ms", "duration", "duration_sec"):
            value = _safe_int(base.get(key), default=0)
            if value > 0:
                return value * 1000 if key != "duration_ms" and value < 10000 else value
    return 0


def _extract_author(payload: Dict[str, Any]) -> Dict[str, str]:
    author_raw = payload.get("author")
    author = author_raw if isinstance(author_raw, dict) else {}
    source = _source_dict(payload)
    source_author = source.get("author") if isinstance(source.get("author"), dict) else {}

    nickname = normalize_text(author.get("nickname"))
    if not nickname and isinstance(author_raw, str):
        nickname = normalize_text(author_raw)
    nickname = nickname or normalize_text(source_author.get("nickname"))

    author_handle = (
        normalize_text(payload.get("author_handle"))
        or normalize_text(author.get("author_handle"))
        or normalize_text(source_author.get("author_handle"))
        or nickname
    )
    platform_author_id = (
        normalize_text(payload.get("platform_author_id"))
        or normalize_text(payload.get("author_platform_id"))
        or normalize_text(author.get("platform_author_id"))
        or normalize_text(author.get("author_platform_id"))
        or normalize_text(source_author.get("platform_author_id"))
        or normalize_text(source_author.get("author_platform_id"))
    )
    return {
        "nickname": nickname,
        "author_handle": author_handle,
        "platform_author_id": platform_author_id,
    }


def _is_cjk(char: str) -> bool:
    code = ord(char)
    return 0x4E00 <= code <= 0x9FFF


def _clean_for_filename(text: str) -> str:
    if not text:
        return ""

    normalized = unicodedata.normalize("NFKC", text)
    normalized = re.sub(r"[#＃][^\s#＃]+", " ", normalized)
    normalized = re.sub(r"\[[^\]]+\]", " ", normalized)
    normalized = normalized.replace("\n", " ").replace("\r", " ")

    kept: List[str] = []
    for char in normalized:
        category = unicodedata.category(char)
        if _is_cjk(char) or char.isalnum() or char in {" ", "-", "_"}:
            kept.append(char)
        elif category.startswith("Z"):
            kept.append(" ")

    compact = "".join(kept)
    compact = re.sub(r"\s+", "", compact)
    compact = re.sub(r"[\\/:*?\"<>|]", "", compact)
    return compact.strip("._-")


def _clip_with_min(text: str, min_len: int, max_len: int, fallback: str) -> str:
    candidate = _clean_for_filename(text)
    fallback_clean = _clean_for_filename(fallback)
    if not candidate:
        candidate = fallback_clean
    if len(candidate) < min_len:
        candidate = (candidate + fallback_clean)[:max_len]
    if len(candidate) < min_len:
        candidate = (candidate + "内容速览")[:max_len]
    candidate = candidate[:max_len]
    if len(candidate) < min_len:
        candidate = (candidate + "作品卡")[:max_len]
    return candidate[:max_len] if candidate else fallback_clean[:max_len]


def _extract_platform_work_id(payload: Dict[str, Any]) -> str:
    return _pick_text(
        payload,
        ["platform_work_id", "aweme_id", "note_id", "item_id", "id"],
        ["platform_work_id", "aweme_id", "note_id", "item_id", "id"],
    )


def _pick_author_slug(payload: Dict[str, Any]) -> str:
    author = _extract_author(payload)
    base = author["nickname"] or author["author_handle"] or author["platform_author_id"] or "作者"
    slug = _clip_with_min(base, min_len=2, max_len=18, fallback="作者")
    return slug if len(slug) >= 2 else "作者"


def _pick_title_source(payload: Dict[str, Any]) -> str:
    for key in ("title", "desc", "summary"):
        text = normalize_text(payload.get(key))
        if text:
            return text

    source = _source_dict(payload)
    for key in ("title", "desc"):
        text = normalize_text(source.get(key))
        if text:
            return text

    raw_content = normalize_text(payload.get("raw_content"))
    if raw_content:
        return raw_content[:48]

    platform_work_id = _extract_platform_work_id(payload)
    if platform_work_id:
        return f"作品拆解{platform_work_id[-8:]}"

    return "内容拆解速览"


def _pick_title_slug(payload: Dict[str, Any]) -> str:
    title_source = _pick_title_source(payload)
    platform_work_id = _extract_platform_work_id(payload)
    fallback = f"内容拆解{platform_work_id[-8:]}" if platform_work_id else "内容拆解速览"
    slug = _clip_with_min(title_source, min_len=8, max_len=28, fallback=fallback)
    return slug if slug else "内容拆解速览"


def _extract_tags(payload: Dict[str, Any]) -> List[str]:
    for key in ("tags", "tag_list", "hashtags"):
        value = payload.get(key)
        if isinstance(value, list):
            tags = [normalize_text(item).lstrip("#") for item in value if normalize_text(item)]
            if tags:
                return list(dict.fromkeys(tags))
        if isinstance(value, str) and normalize_text(value):
            parts = re.split(r"[,，\s]+", normalize_text(value))
            tags = [part.lstrip("#") for part in parts if part]
            if tags:
                return list(dict.fromkeys(tags))

    source = _source_dict(payload)
    for key in ("tags", "tag_list", "hashtags"):
        value = source.get(key)
        if isinstance(value, list):
            tags = [normalize_text(item).lstrip("#") for item in value if normalize_text(item)]
            if tags:
                return list(dict.fromkeys(tags))
    return []


def _format_duration(duration_ms: int) -> str:
    if duration_ms <= 0:
        return "未知"
    total_sec = duration_ms // 1000
    minute, second = divmod(total_sec, 60)
    if minute:
        return f"{minute}分{second:02d}秒"
    return f"{second}秒"


def _analysis_status_from_sections(analysis_sections: Dict[str, Any]) -> Dict[str, Any]:
    meta = analysis_sections.get("meta") if isinstance(analysis_sections.get("meta"), dict) else {}
    reason = normalize_text(meta.get("reason"))
    if meta.get("llm_used"):
        status = "completed"
    elif not reason or reason == "analysis_mode_local":
        status = "skipped"
    elif "timeout" in reason:
        status = "timeout"
    elif "unavailable" in reason:
        status = "unavailable"
    else:
        status = "failed"
    return {
        "status": status,
        "provider": normalize_text(analysis_sections.get("provider")) or "local",
        "reason": reason or None,
        "duration_ms": _safe_int(meta.get("duration_ms"), default=0),
        "llm_used": bool(meta.get("llm_used")),
        "degraded": bool(meta.get("degraded")),
    }


def _has_meaningful_analysis_sections(value: Any) -> bool:
    if not isinstance(value, dict):
        return False
    modules = value.get("modules")
    if not isinstance(modules, dict):
        return False
    return any(bool(normalize_text(item)) for items in modules.values() if isinstance(items, list) for item in items)


def _extract_required_fields(payload: Dict[str, Any], platform: str) -> Dict[str, Any]:
    author = _extract_author(payload)
    title = _pick_text(payload, ["title", "desc"], ["title", "desc"])
    caption_raw = normalize_text(payload.get("caption_raw") or payload.get("desc"))
    platform_work_id = _extract_platform_work_id(payload)
    source_url = _pick_text(payload, ["source_url", "share_url", "url"], ["source_url", "share_url", "url"])
    share_url = _pick_text(payload, ["share_url", "canonical_share_url"], ["share_url", "canonical_share_url", "url"]) or source_url
    cover_image = _pick_text(payload, ["cover_image", "cover_url", "cover"], ["cover_image", "cover_url", "cover"])
    selected_images = payload.get("selected_image_urls")
    if not cover_image and isinstance(selected_images, list) and selected_images:
        cover_image = normalize_text(selected_images[0])
    video_download_url = _pick_text(
        payload,
        ["video_download_url", "video_down_url", "selected_video_url", "original_video_url", "video_url", "download_url"],
        ["video_download_url", "video_down_url", "selected_video_url", "original_video_url", "video_url", "download_url"],
    )

    create_time_sec = _to_unix_sec(payload.get("create_time_sec"))
    if create_time_sec <= 0:
        create_time_sec = _to_unix_sec(payload.get("create_time"))
    if create_time_sec <= 0:
        create_time_sec = _to_unix_sec(_source_dict(payload).get("create_time"))

    raw_content = normalize_text(payload.get("asr_raw") or payload.get("raw_content"))
    provided_asr_clean = normalize_text(payload.get("asr_clean"))
    asr_clean = derive_asr_clean_text(raw_content, provided_asr_clean)

    work_modality = normalize_text(payload.get("work_modality"))
    if not work_modality:
        work_modality = "video" if video_download_url or raw_content else "text"

    primary_text_source = normalize_text(payload.get("primary_text_source"))
    if primary_text_source not in {"asr_clean", "caption_raw"}:
        primary_text_source = "asr_clean" if work_modality == "video" else "caption_raw"
    primary_text = normalize_text(payload.get("primary_text"))
    if not primary_text:
        primary_text = asr_clean if primary_text_source == "asr_clean" else (caption_raw or raw_content)

    analysis_sections = ensure_analysis_sections_schema(
        payload.get("analysis_sections") if isinstance(payload.get("analysis_sections"), dict) else {},
        provider="local",
        llm_used=False,
    )

    return {
        "title": title,
        "platform": platform,
        "platform_work_id": platform_work_id,
        "author": author.get("nickname") or "",
        "author_handle": author.get("author_handle") or "",
        "platform_author_id": author.get("platform_author_id") or "",
        "caption_raw": caption_raw,
        "share_url": share_url,
        "source_url": source_url,
        "cover_image": cover_image,
        "video_download_url": video_download_url,
        "published_date": _resolve_published_date(payload, create_time_sec),
        "duration_ms": _extract_duration_ms(payload),
        "digg_count": _safe_int(payload.get("digg_count"), default=0),
        "comment_count": _safe_int(payload.get("comment_count"), default=0),
        "collect_count": _safe_int(payload.get("collect_count"), default=0),
        "share_count": _safe_int(payload.get("share_count"), default=0),
        "play_count": _safe_optional_int(payload.get("play_count")),
        "tags": _extract_tags(payload),
        "work_modality": work_modality,
        "category": normalize_text(payload.get("category")) or "观点",
        "content_kind": normalize_text(payload.get("content_kind")),
        "summary": normalize_text(payload.get("summary")),
        "raw_content": raw_content,
        "asr_raw": raw_content,
        "asr_clean": asr_clean,
        "primary_text": primary_text,
        "primary_text_source": primary_text_source,
        "request_id": payload.get("request_id"),
        "confidence": normalize_text(payload.get("confidence")) or "low",
        "error_reason": payload.get("error_reason"),
        "extract_trace": payload.get("extract_trace", []),
        "analysis_sections": analysis_sections,
    }


def build_card_analysis_artifact(
    *,
    payload: Dict[str, Any],
    platform: str,
    card_type: str,
    analysis_mode: str = "auto",
    storage_config: Optional[Dict[str, Any]] = None,
    progress: Optional[ProgressReporter] = None,
) -> Dict[str, Any]:
    fields = _extract_required_fields(payload, platform=platform)
    if _has_meaningful_analysis_sections(payload.get("analysis_sections")):
        existing = payload.get("analysis_sections")
        meta = existing.get("meta") if isinstance(existing, dict) and isinstance(existing.get("meta"), dict) else {}
        analysis_sections = ensure_analysis_sections_schema(
            existing,
            provider=normalize_text(existing.get("provider")) or "local",
            llm_used=bool(meta.get("llm_used")),
            degraded=bool(meta.get("degraded")),
            reason=normalize_text(meta.get("reason")),
            duration_ms=_safe_int(meta.get("duration_ms"), default=0),
        )
    else:
        analysis_sections = build_analysis_sections(
            fields,
            analysis_mode=analysis_mode,
            analysis_config=storage_config.get("analysis") if isinstance(storage_config, dict) else None,
            progress=progress,
        )
    fields["analysis_sections"] = analysis_sections
    return {
        "fields": fields,
        "analysis_sections": analysis_sections,
        "card_type": normalize_card_type(card_type),
    }


def _build_output_path(
    *,
    card_root: str,
    platform: str,
    card_type: str,
    payload: Dict[str, Any],
    now: dt.datetime,
    storage_config: Optional[Dict[str, Any]],
) -> Dict[str, str]:
    author_slug = _pick_author_slug(payload)
    title_slug = _pick_title_slug(payload)
    path, route_parts = build_card_output_path(
        card_root=card_root,
        platform=platform,
        card_type=card_type,
        author_slug=author_slug,
        title_slug=title_slug,
        year=now.strftime("%Y"),
        year_month=now.strftime("%Y-%m"),
        timestamp=now.strftime("%Y%m%d-%H%M%S"),
        storage_config=storage_config,
    )
    return {
        "path": path,
        "route_parts": route_parts,
    }


def _render_markdown(
    *,
    card_id: str,
    card_type: str,
    fields: Dict[str, Any],
    generated_at: str,
) -> str:
    author_name = fields.get("author") or fields.get("author_handle") or fields.get("platform_author_id") or "未知作者"
    title = fields.get("title") or "（标题缺失）"
    analysis_sections = ensure_analysis_sections_schema(fields.get("analysis_sections"), provider="local", llm_used=False)
    creative_modules = analysis_sections.get("modules", {})
    insight_lines = analysis_sections.get("insight", ["数据不足"])
    extract_trace_json = json.dumps(fields.get("extract_trace", []), ensure_ascii=False, indent=2)

    fm = {
        "card_id": card_id,
        "card_type": card_type,
        "platform": fields.get("platform"),
        "generated_at": generated_at,
        "updated_at": generated_at,
        "title": fields.get("title"),
        "platform_work_id": fields.get("platform_work_id"),
        "author": fields.get("author"),
        "author_handle": fields.get("author_handle"),
        "platform_author_id": fields.get("platform_author_id"),
        "caption_raw": fields.get("caption_raw"),
        "share_url": fields.get("share_url"),
        "source_url": fields.get("source_url"),
        "cover_image": fields.get("cover_image"),
        "video_download_url": fields.get("video_download_url"),
        "published_date": fields.get("published_date"),
        "duration_ms": fields.get("duration_ms"),
        "digg_count": fields.get("digg_count"),
        "comment_count": fields.get("comment_count"),
        "collect_count": fields.get("collect_count"),
        "share_count": fields.get("share_count"),
        "play_count": fields.get("play_count"),
        "tags": fields.get("tags", []),
        "work_modality": fields.get("work_modality"),
    }

    frontmatter = ["---"]
    for key, value in fm.items():
        frontmatter.append(f"{key}: {json.dumps(value, ensure_ascii=False)}")
    frontmatter.append("---")

    lines = [
        *frontmatter,
        "",
    ]

    for heading in DEFAULT_MODULE_SECTIONS:
        lines.append("")
        lines.append(f"## {heading}")
        for item in creative_modules.get(heading, ["数据不足"]):
            lines.append(item)

    lines.append("")
    lines.append("## 洞察分析")
    for item in insight_lines:
        lines.append(item)

    lines.extend(
        [
            "",
            "## 主文本",
            fields.get("primary_text") or "（无可用主文本）",
            "",
            "## 附录",
            "### ASR_RAW",
            fields.get("asr_raw") or "（无可用 ASR 原文）",
            "",
            "### trace",
            f"- request_id: {fields.get('request_id')}",
            f"- confidence: {fields.get('confidence')}",
            f"- error_reason: {fields.get('error_reason')}",
            "",
            "<details>",
            "<summary>extract_trace（点击展开）</summary>",
            "",
            "```json",
            extract_trace_json,
            "```",
            "",
            "</details>",
            "",
        ]
    )
    return "\n".join(lines)


def _write_file(path: str, content: str) -> None:
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(content)


def _resolve_card_root(card_root: Optional[str]) -> str:
    raw = (card_root or "").strip()
    if not raw:
        return resolve_default_card_root()
    candidate = Path(raw).expanduser()
    if not candidate.is_absolute():
        raise ValueError("card_root must be an absolute path")
    return str(candidate.resolve())


def _read_payload_from_input(input_json: str) -> Dict[str, Any]:
    if input_json == "-":
        raw = os.read(0, 1024 * 1024).decode("utf-8", errors="replace").strip()
        if not raw:
            return {}
        return json.loads(raw)
    return read_json_file(input_json)


def write_benchmark_card(
    *,
    payload: Dict[str, Any],
    platform: str,
    card_type: str,
    card_root: Optional[str],
    content_kind: Optional[str] = None,
    storage_config: Optional[Dict[str, Any]] = None,
    force_card_type: bool = False,
    analysis_mode: str = "auto",
    progress: Optional[ProgressReporter] = None,
) -> Dict[str, Any]:
    started_at = time.perf_counter()
    now = dt.datetime.now()
    generated_at = now.isoformat(timespec="seconds")

    payload_content_kind = normalize_text(payload.get("content_kind"))
    resolved_content_kind = normalize_text(content_kind) or payload_content_kind
    normalized_card_type = normalize_card_type(card_type)
    effective_card_type = resolve_effective_card_type(
        card_type=normalized_card_type,
        content_kind=resolved_content_kind,
        storage_config=storage_config,
        force_card_type=force_card_type,
    )
    if effective_card_type != "work":
        effective_card_type = "work"

    fields = _extract_required_fields(payload, platform=platform)
    if progress is not None:
        progress.progress(stage="card.analysis", message="building card analysis")
    if _has_meaningful_analysis_sections(payload.get("analysis_sections")):
        existing = payload.get("analysis_sections")
        meta = existing.get("meta") if isinstance(existing, dict) and isinstance(existing.get("meta"), dict) else {}
        analysis_sections = ensure_analysis_sections_schema(
            existing,
            provider=normalize_text(existing.get("provider")) or "local",
            llm_used=bool(meta.get("llm_used")),
            degraded=bool(meta.get("degraded")),
            reason=normalize_text(meta.get("reason")),
            duration_ms=_safe_int(meta.get("duration_ms"), default=0),
        )
    else:
        analysis_sections = build_analysis_sections(
            fields,
            analysis_mode=analysis_mode,
            analysis_config=storage_config.get("analysis") if isinstance(storage_config, dict) else None,
            progress=progress.child(scope="card.analysis") if progress is not None else None,
        )
    fields["analysis_sections"] = analysis_sections

    payload["analysis_sections"] = analysis_sections
    payload["asr_raw"] = fields.get("asr_raw")
    payload["asr_clean"] = fields.get("asr_clean")
    payload["primary_text"] = fields.get("primary_text")
    payload["primary_text_source"] = fields.get("primary_text_source")
    deep_analysis = _analysis_status_from_sections(analysis_sections)
    payload["deep_analysis"] = deep_analysis

    resolved_card_root = _resolve_card_root(card_root)
    primary_target = _build_output_path(
        card_root=resolved_card_root,
        platform=platform,
        card_type=effective_card_type,
        payload=payload,
        now=now,
        storage_config=storage_config,
    )
    primary_path = primary_target["path"]
    primary_card_id = os.path.basename(primary_path).replace(".md", "")

    markdown = _render_markdown(
        card_id=primary_card_id,
        card_type=effective_card_type,
        fields=fields,
        generated_at=generated_at,
    )
    _write_file(primary_path, markdown)

    duration_ms = int((time.perf_counter() - started_at) * 1000)
    return {
        "ok": True,
        "platform": platform,
        "card_type": effective_card_type,
        "requested_card_type": normalized_card_type,
        "force_card_type": bool(force_card_type),
        "content_kind": resolved_content_kind or None,
        "primary_card_path": primary_path,
        "routing": {
            "primary_route_parts": primary_target["route_parts"],
            "storage_routes_configured": bool(isinstance(storage_config, dict) and isinstance(storage_config.get("storage_routes"), dict)),
        },
        "required_fields": fields,
        "analysis_sections": analysis_sections,
        "analysis_status": deep_analysis,
        "duration_ms": duration_ms,
        "llm_analysis_ms": _safe_int(analysis_sections.get("meta", {}).get("duration_ms"), default=0),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Write single-work benchmark card markdown to card root")
    parser.add_argument("--platform", required=True, help="Platform name, e.g. douyin or xiaohongshu")
    parser.add_argument("--card-type", choices=CARD_TYPES, default="work", help="Primary card type")
    parser.add_argument("--analysis-mode", choices=["auto", "local"], default="auto", help="Card analysis mode")
    parser.add_argument("--config", default=None, help="Runtime config YAML path")
    parser.add_argument("--env-file", default=None, help="Shared env file path; defaults to <skills_root>/.env")
    parser.add_argument("--allow-process-env", action="store_true", help="Allow process env to override .env/.env.local")
    parser.add_argument("--content-kind", default=None, help="Optional workflow kind, e.g. single_video/note/work")
    parser.add_argument("--force-card-type", action="store_true", help="Force manual --card-type to override content_kind mapping")
    parser.add_argument("--card-root", default=None, help="Card root path (absolute); falls back to TIKOMNI_CARD_ROOT when omitted")
    parser.add_argument("--input-json", default="-", help="Input JSON path or '-' to read from stdin")
    args = parser.parse_args()

    config, _ = load_tikomni_config(
        args.config,
        env_file=args.env_file,
        allow_process_env=args.allow_process_env,
    )
    payload = _read_payload_from_input(args.input_json)
    result = write_benchmark_card(
        payload=payload,
        platform=args.platform,
        card_type=args.card_type,
        card_root=args.card_root,
        content_kind=args.content_kind,
        storage_config=config,
        force_card_type=args.force_card_type,
        analysis_mode=args.analysis_mode,
        progress=None,
    )
    write_json_stdout(result)


if __name__ == "__main__":
    main()
