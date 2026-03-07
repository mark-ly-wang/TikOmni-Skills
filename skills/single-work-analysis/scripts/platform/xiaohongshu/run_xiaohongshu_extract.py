#!/usr/bin/env python3

if __package__ in {None, ""}:
    import sys
    from pathlib import Path

    _self = Path(__file__).resolve()
    for _parent in _self.parents:
        if (_parent / "scripts" / "core" / "bootstrap_env.py").is_file():
            sys.path.insert(0, str(_parent))
            break

"""Xiaohongshu extraction: APP V2 -> APP V1 -> WEB_V2 -> WEB."""

from scripts.core.bootstrap_env import bootstrap_for_direct_run

bootstrap_for_direct_run(__file__, __package__)

import argparse
import hashlib
import json
import re
import urllib.parse
import urllib.request
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from scripts.pipeline.asr.asr_pipeline import run_u2_asr_candidates_with_timeout_retry
from scripts.core.config_loader import config_get, load_tikomni_config, resolve_storage_paths
from scripts.core.progress_report import ProgressReporter
from scripts.core.storage_router import render_output_filename, resolve_json_filename_pattern
from scripts.core.extract_pipeline import build_api_trace, resolve_trace_error_context
from scripts.core.tikomni_common import (
    call_json_api,
    deep_find_all,
    deep_find_first,
    normalize_text,
    resolve_runtime,
    summarize_content,
    write_json_stdout,
)
from scripts.writers.write_benchmark_card import write_benchmark_card

APP_V2_VIDEO_ENDPOINT = "/api/u1/v1/xiaohongshu/app_v2/get_video_note_detail"
APP_V2_IMAGE_ENDPOINT = "/api/u1/v1/xiaohongshu/app_v2/get_image_note_detail"
APP_V2_MIXED_ENDPOINT = "/api/u1/v1/xiaohongshu/app_v2/get_mixed_note_detail"
APP_V1_ENDPOINT = "/api/u1/v1/xiaohongshu/app/get_note_info"
WEB_V2_V2_ENDPOINT = "/api/u1/v1/xiaohongshu/web_v2/fetch_feed_notes_v2"
WEB_V2_V3_ENDPOINT = "/api/u1/v1/xiaohongshu/web_v2/fetch_feed_notes_v3"
WEB_ENDPOINT = "/api/u1/v1/xiaohongshu/web/get_note_info_v7"
U2_GATE_MIN_DURATION_MS = 13000
U2_GATE_MAX_DURATION_MS = 1800000
U2_GATE_RULE = "is_video && 13000<duration_ms<=1800000 && video_download_url_present"


def _format_published_date(value: Any) -> str:
    ts = _to_int_or_none(value)
    if ts is None:
        return "N/A"
    try:
        return datetime.fromtimestamp(ts).strftime("%Y-%m-%d")
    except Exception:
        return "N/A"


def _to_int_or_none(value: Any) -> Optional[int]:
    try:
        if isinstance(value, bool):
            return int(value)
        if isinstance(value, (int, float)):
            parsed = int(value)
            return parsed if parsed > 0 else None
        text = normalize_text(value)
        if not text:
            return None
        parsed = int(float(text.replace(",", "")))
        return parsed if parsed > 0 else None
    except Exception:
        return None


def _evaluate_u2_gate_for_xhs(*, note_content_type: str, duration_ms: Any, video_down_url: Optional[str]) -> Dict[str, Any]:
    content_type = normalize_text(note_content_type).lower()
    is_video = content_type in {"video", "mixed"}
    normalized_duration = _to_int_or_none(duration_ms)
    normalized_video_down_url = normalize_text(video_down_url)

    if not is_video:
        gate_reason = "skip:not_video"
    elif normalized_duration is None:
        gate_reason = "skip:duration_missing"
    elif normalized_duration <= U2_GATE_MIN_DURATION_MS:
        gate_reason = "skip:duration_too_short"
    elif normalized_duration > U2_GATE_MAX_DURATION_MS:
        gate_reason = "skip:duration_too_long"
    elif not normalized_video_down_url:
        gate_reason = "skip:video_download_url_missing"
    else:
        gate_reason = "pass"

    return {
        "can_u2": gate_reason == "pass",
        "gate_reason": gate_reason,
        "is_video": is_video,
        "duration_ms": normalized_duration,
        "video_down_url": normalized_video_down_url,
        "video_download_url": normalized_video_down_url,
        "video_download_url_present": bool(normalized_video_down_url),
    }


def _safe_slug(value: Optional[str], fallback: str = "unknown") -> str:
    text = normalize_text(value)
    if not text:
        return fallback
    slug = re.sub(r"[^a-zA-Z0-9_-]+", "-", text).strip("-").lower()
    return slug[:64] or fallback


def _traceable_identifier(source_input: Dict[str, Optional[str]], note_id: Optional[str]) -> str:
    if note_id:
        return _safe_slug(note_id)
    share = normalize_text(source_input.get("share_text"))
    if not share:
        return "missing_input"
    digest = hashlib.sha1(share.encode("utf-8")).hexdigest()[:10]
    return f"url-{digest}"


def _build_persist_payload(
    *,
    result: Dict[str, Any],
    source_input: Dict[str, Optional[str]],
    note_id: Optional[str],
    status: str,
    written_at: datetime,
) -> Dict[str, Any]:
    summary = {
        "summary": result.get("summary", ""),
        "insights": result.get("insights", []),
        "confidence": result.get("confidence"),
        "error_reason": result.get("error_reason"),
    }
    normalized = {
        "platform": "xiaohongshu",
        "content_kind": result.get("content_kind", "note"),
        "note_id": result.get("note_id") or note_id,
        "note_content_type": result.get("note_content_type"),
        "text_source": result.get("text_source"),
        "request_id": result.get("request_id"),
        "source": source_input,
    }
    return {
        "meta": {
            "written_at": written_at.isoformat(timespec="seconds"),
            "status": status,
            "platform": "xiaohongshu",
            "identifier": _traceable_identifier(source_input, note_id),
        },
        "summary": summary,
        "normalized": normalized,
        "raw": result,
    }


def _persist_output_artifact(
    *,
    result: Dict[str, Any],
    source_input: Dict[str, Optional[str]],
    note_id: Optional[str],
    storage_config: Optional[Dict[str, Any]],
    persist_output: bool,
) -> Dict[str, Any]:
    if not persist_output:
        return {"enabled": False, "skipped": True, "reason": "disabled_by_flag"}

    try:
        paths = resolve_storage_paths(storage_config or {})
    except Exception as error:
        return {"enabled": True, "ok": False, "error": f"resolve_storage_paths_failed:{error}"}

    now = datetime.now()
    date_key = now.strftime("%Y%m%d")
    timestamp = now.strftime("%Y%m%dT%H%M%S")
    identifier = _traceable_identifier(source_input, note_id)
    has_error = bool(result.get("error_reason"))
    status = "error" if has_error else "success"

    if has_error:
        target_dir = Path(paths.get("errors_root", "")) / date_key
    else:
        target_dir = Path(paths.get("results_root", "")) / date_key

    target_dir.mkdir(parents=True, exist_ok=True)
    file_name = render_output_filename(
        pattern=resolve_json_filename_pattern(storage_config),
        context={
            "prefix": status,
            "platform": "xiaohongshu",
            "card_type": "single_work_result",
            "author_slug": identifier,
            "title_slug": identifier,
            "identifier": identifier,
            "timestamp": timestamp,
            "date": date_key,
            "ext": ".json",
        },
        default_filename=f"{timestamp}-xiaohongshu-{identifier}.json",
        default_ext=".json",
    )
    file_path = target_dir / file_name

    payload = _build_persist_payload(
        result=result,
        source_input=source_input,
        note_id=note_id,
        status=status,
        written_at=now,
    )
    file_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    return {
        "enabled": True,
        "ok": True,
        "status": status,
        "path": str(file_path),
    }


def _finalize_result(
    *,
    result: Dict[str, Any],
    source_input: Dict[str, Optional[str]],
    note_id: Optional[str],
    storage_config: Optional[Dict[str, Any]],
    persist_output: bool,
) -> Dict[str, Any]:
    result["output_persist"] = _persist_output_artifact(
        result=result,
        source_input=source_input,
        note_id=note_id,
        storage_config=storage_config,
        persist_output=persist_output,
    )
    return result


def _normalize_input(input_value: Optional[str], share_text: Optional[str], note_id: Optional[str]) -> Dict[str, Optional[str]]:
    normalized_share = normalize_text(share_text) or None
    normalized_note_id = normalize_text(note_id) or None

    if input_value and not normalized_share and not normalized_note_id:
        candidate = input_value.strip()
        if candidate.startswith("http://") or candidate.startswith("https://"):
            normalized_share = candidate
        else:
            normalized_note_id = candidate

    return {
        "share_text": normalized_share,
        "note_id": normalized_note_id,
    }


def _extract_note_id_from_share(share_text: Optional[str]) -> Optional[str]:
    if not share_text:
        return None
    text = share_text.strip()
    patterns = [
        r"/explore/([0-9a-zA-Z]+)",
        r"/discovery/item/([0-9a-zA-Z]+)",
        r"note_id=([0-9a-zA-Z]+)",
    ]
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            return match.group(1)
    return None


def _resolve_note_id(payload: Any, source_input: Dict[str, Optional[str]]) -> Optional[str]:
    # Priority 1: explicit source input
    if source_input.get("note_id"):
        return source_input.get("note_id")

    # Priority 2: canonical keys from payload
    for key in ["note_id", "noteid", "item_id", "itemId"]:
        value = deep_find_first(payload, [key])
        text = normalize_text(value)
        if text and len(text) >= 16:
            return text

    # Priority 3: parse from canonical webpage URLs
    for key in ["webpage_url", "share_url", "url"]:
        values = deep_find_all(payload, [key])
        for value in values:
            text = normalize_text(value)
            hit = _extract_note_id_from_share(text)
            if hit:
                return hit

    # Priority 4: parse from source share text
    hit = _extract_note_id_from_share(source_input.get("share_text"))
    if hit:
        return hit

    return None


def _is_short_share_url(share_text: Optional[str]) -> bool:
    if not share_text:
        return False
    try:
        host = urllib.parse.urlparse(share_text).netloc.lower()
    except Exception:
        return False
    return "xhslink.com" in host


def _app_response_has_core_fields(response_data: Any) -> bool:
    subtitle_hit = bool(_extract_subtitle_inline_text(response_data)) or bool(_extract_subtitle_urls(response_data))
    video_hit = bool(_extract_video_candidates(response_data))
    # For APP-first strategy, if app only has weak image frames but no subtitle/video core,
    # continue probing WEB_V2 to improve media fidelity.
    return subtitle_hit or video_hit


def _route_field_completeness(payload: Any, source_input: Dict[str, Optional[str]]) -> Dict[str, Any]:
    note_id_hit = bool(_resolve_note_id(payload, source_input))
    title_hit = bool(
        _pick_text_from_paths(
            payload,
            [["title"], ["desc"], ["content"], ["note", "title"], ["note", "desc"], ["note", "content"]],
        )
    )
    author_hit = bool(
        _pick_text_from_paths(
            payload,
            [
                ["nickname"],
                ["author_nickname"],
                ["user_nickname"],
                ["author", "nickname"],
                ["user", "nickname"],
                ["author", "name"],
                ["user", "name"],
            ],
        )
    )
    media_hit = bool(_extract_video_candidates(payload) or _extract_image_candidates(payload))
    subtitle_hit = bool(_extract_subtitle_inline_text(payload)) or bool(_extract_subtitle_urls(payload))
    metrics_hit = any(
        _pick_int_from_paths(payload, [path], prefer_positive=True) is not None
        for path in (
            ["digg_count"],
            ["liked_count"],
            ["like_count"],
            ["comment_count"],
            ["collect_count"],
            ["share_count"],
            ["view_count"],
            ["play_count"],
        )
    )

    fields = {
        "note_id": note_id_hit,
        "title_or_desc": title_hit,
        "author": author_hit,
        "media": media_hit,
        "subtitle": subtitle_hit,
        "metrics": metrics_hit,
    }
    filled_count = sum(1 for hit in fields.values() if hit)
    missing_core = [key for key in ("note_id", "title_or_desc", "media") if not fields.get(key)]
    return {
        "fields": fields,
        "filled_count": filled_count,
        "total_fields": len(fields),
        "ratio": round(filled_count / max(len(fields), 1), 3),
        "missing_core": missing_core,
        "core_ready": not missing_core,
    }


def _route_success_for_note(response: Dict[str, Any], source_input: Dict[str, Optional[str]]) -> bool:
    if not response.get("ok"):
        return False
    completeness = response.get("_field_completeness")
    if not isinstance(completeness, dict):
        completeness = _route_field_completeness(response.get("data"), source_input)
        response["_field_completeness"] = completeness
    return bool(completeness.get("core_ready"))


def _pick_text_from_paths(payload: Any, paths: List[List[str]]) -> str:
    for path in paths:
        raw = deep_find_first(payload, path)
        if isinstance(raw, (dict, list)):
            continue
        text = normalize_text(raw)
        if text:
            return text
    return ""


def _to_int(value: Any) -> Optional[int]:
    if isinstance(value, bool):
        return int(value)
    if isinstance(value, int):
        return value
    if isinstance(value, float):
        return int(value)
    if isinstance(value, str):
        text = value.strip()
        if text.isdigit() or (text.startswith("-") and text[1:].isdigit()):
            return int(text)
    return None


def _extract_value_by_path(payload: Any, path: List[str]) -> Optional[Any]:
    if not path:
        return None

    def _walk(node: Any, idx: int) -> Optional[Any]:
        if idx >= len(path):
            if node in (None, "", [], {}):
                return None
            return node

        key = path[idx]
        if isinstance(node, dict):
            if key in node:
                hit = _walk(node.get(key), idx + 1)
                if hit is not None:
                    return hit
            for value in node.values():
                hit = _walk(value, idx)
                if hit is not None:
                    return hit
            return None

        if isinstance(node, list):
            for item in node:
                hit = _walk(item, idx)
                if hit is not None:
                    return hit
            return None

        return None

    return _walk(payload, 0)


def _normalize_unix_sec(value: int) -> int:
    # 13-digit timestamps are milliseconds.
    if value > 1_000_000_000_000:
        return value // 1000
    return value


def _pick_int_with_source_from_paths(
    payload: Any,
    paths: List[List[str]],
    *,
    prefer_positive: bool = False,
    normalize_unix_sec: bool = False,
) -> Tuple[Optional[int], str]:
    for path in paths:
        value = _extract_value_by_path(payload, path)
        if value is None:
            value = deep_find_first(payload, path)
        parsed = _to_int(value)
        if parsed is None:
            continue
        if normalize_unix_sec:
            parsed = _normalize_unix_sec(parsed)
        if prefer_positive and parsed <= 0:
            continue
        return parsed, ".".join(path)
    return None, ""


def _pick_int_from_paths(
    payload: Any,
    paths: List[List[str]],
    *,
    prefer_positive: bool = False,
    normalize_unix_sec: bool = False,
) -> Optional[int]:
    value, _ = _pick_int_with_source_from_paths(
        payload,
        paths,
        prefer_positive=prefer_positive,
        normalize_unix_sec=normalize_unix_sec,
    )
    return value


def _dedupe_keep_order(values: List[str]) -> List[str]:
    output: List[str] = []
    seen = set()
    for value in values:
        if value in seen:
            continue
        seen.add(value)
        output.append(value)
    return output


def _clean_tag_text(value: Any) -> str:
    text = normalize_text(value)
    if not text:
        return ""
    text = text.strip().strip("#")
    text = re.sub(r"\[话题\]$", "", text)
    text = text.strip().strip("#")
    return text


def _append_tag(raw: Any, output: List[str], seen: set) -> None:
    tag = _clean_tag_text(raw)
    if not tag or tag in seen:
        return
    seen.add(tag)
    output.append(tag)


def _extract_tags_from_container(value: Any, output: List[str], seen: set) -> None:
    if isinstance(value, str):
        _append_tag(value, output, seen)
        return
    if isinstance(value, list):
        for item in value:
            _extract_tags_from_container(item, output, seen)
        return
    if isinstance(value, dict):
        for key in ("name", "tag_name", "topic_name", "hashtag_name"):
            _append_tag(value.get(key), output, seen)


def _extract_xhs_tags(payload: Any) -> List[str]:
    primary_tags: List[str] = []
    primary_seen: set = set()
    for key in ("tagList", "taglist", "tag_list"):
        for value in deep_find_all(payload, [key]):
            _extract_tags_from_container(value, primary_tags, primary_seen)
    if primary_tags:
        return primary_tags

    tags: List[str] = []
    seen: set = set()
    for key in ("topics", "hash_tag", "hashTag", "head_tags", "foot_tags"):
        for value in deep_find_all(payload, [key]):
            _extract_tags_from_container(value, tags, seen)

    for desc in deep_find_all(payload, ["desc", "content"]):
        if not isinstance(desc, str):
            continue
        for match in re.findall(r"#([^#\n\r]+?)#", desc):
            _append_tag(match, tags, seen)

    return tags


def _build_candidate_merge_sources(*, app_candidates: List[str], enrich_candidates: List[str], app_label: str) -> List[str]:
    sources: List[str] = []
    if app_candidates:
        sources.append(app_label)
    if enrich_candidates:
        sources.append("web_v2_enrich")
    return sources


def _extract_xhs_metadata(
    *,
    payload: Any,
    source_input: Dict[str, Optional[str]],
    selected_video_url: Optional[str],
    selected_image_urls: List[str],
) -> Dict[str, Any]:
    share_from_source = normalize_text(source_input.get("share_text"))

    title = _pick_text_from_paths(payload, [["title"], ["note", "title"], ["desc"], ["content"]])
    author = _pick_text_from_paths(
        payload,
        [
            ["nickname"],
            ["author_nickname"],
            ["user_nickname"],
            ["author", "nickname"],
            ["user", "nickname"],
            ["author", "name"],
            ["user", "name"],
        ],
    )

    create_time_paths = [
        ["create_time_sec"],
        ["create_time"],
        ["publish_time_sec"],
        ["publish_time"],
        ["time"],
        ["timestamp"],
        ["createTime"],
        ["publishTime"],
        ["note", "create_time_sec"],
        ["note", "create_time"],
        ["note", "createTime"],
        ["note", "publish_time_sec"],
        ["note", "publish_time"],
        ["note", "publishTime"],
        ["note", "time"],
        ["note", "timestamp"],
        ["note_list", "create_time_sec"],
        ["note_list", "create_time"],
        ["note_list", "createTime"],
        ["note_list", "publish_time_sec"],
        ["note_list", "publish_time"],
        ["note_list", "publishTime"],
        ["note_list", "time"],
        ["note_list", "timestamp"],
        ["noteList", "create_time_sec"],
        ["noteList", "create_time"],
        ["noteList", "createTime"],
        ["noteList", "publish_time_sec"],
        ["noteList", "publish_time"],
        ["noteList", "publishTime"],
        ["noteList", "time"],
        ["noteList", "timestamp"],
    ]
    create_time_sec, create_time_source = _pick_int_with_source_from_paths(
        payload,
        create_time_paths,
        prefer_positive=True,
        normalize_unix_sec=True,
    )
    duration_ms = _pick_int_from_paths(
        payload,
        [["duration_ms"], ["duration"], ["duration_sec"], ["video", "duration"], ["note", "duration"]],
    )
    if duration_ms is not None and duration_ms > 0 and duration_ms < 10000:
        duration_ms *= 1000

    share_url = _pick_text_from_paths(payload, [["share_url"], ["webpage_url"], ["url"], ["share_link"], ["share_text"]])
    source_url = _pick_text_from_paths(payload, [["source_url"], ["webpage_url"], ["url"], ["share_url"]])
    if not share_url:
        share_url = share_from_source
    if not source_url:
        source_url = share_url or share_from_source

    cover_image = _pick_text_from_paths(payload, [["cover_image"], ["cover_url"], ["cover"], ["image", "url"], ["origin_cover"]])
    if not cover_image and selected_image_urls:
        cover_image = selected_image_urls[0]

    video_down_url = _pick_text_from_paths(
        payload,
        [
            ["video_down_url"],
            ["original_video_url"],
            ["video_url"],
            ["play_url"],
            ["master_url"],
            ["selected_video_url"],
        ],
    )
    if not video_down_url:
        video_down_url = normalize_text(selected_video_url)

    xhs_user_id = _pick_text_from_paths(
        payload,
        [["author", "userid"], ["author", "user_id"], ["user", "userid"], ["user", "user_id"], ["user_id"], ["userid"], ["id"]],
    )
    author_handle = _pick_text_from_paths(
        payload,
        [["author", "red_id"], ["user", "red_id"], ["red_id"], ["author", "nickname"], ["user", "nickname"], ["nickname"]],
    ) or author

    xhs_sec_token = _pick_text_from_paths(
        payload,
        [["xhs_sec_token"], ["xsec_token"], ["xsecToken"], ["note", "xsecToken"], ["user", "xsecToken"], ["user", "xsec_token"]],
    )
    if not xhs_sec_token:
        for url_text in [share_url, source_url, share_from_source]:
            text = normalize_text(url_text)
            if not text:
                continue
            try:
                query = urllib.parse.urlparse(text).query
                xhs_sec_token = urllib.parse.parse_qs(query).get("xsec_token", [""])[0]
            except Exception:
                xhs_sec_token = ""
            if normalize_text(xhs_sec_token):
                break

    return {
        "title": title,
        "caption_raw": _pick_text_from_paths(payload, [["desc"], ["content"], ["note", "desc"], ["note", "content"]]),
        "author": author,
        "author_handle": author_handle,
        "platform_author_id": xhs_user_id,
        "author_platform_id": xhs_user_id,
        "xhs_user_id": xhs_user_id,
        "xhs_sec_token": normalize_text(xhs_sec_token),
        "create_time_sec": create_time_sec,
        "publish_time": create_time_sec,
        "publish_time_source": create_time_source or "unknown",
        "duration_ms": duration_ms,
        "tags": _extract_xhs_tags(payload),
        "digg_count": _pick_int_from_paths(payload, [["digg_count"], ["liked_count"], ["like_count"], ["likes"]]),
        "comment_count": _pick_int_from_paths(payload, [["comment_count"], ["comments_count"], ["comments"]]),
        "collect_count": _pick_int_from_paths(payload, [["collect_count"], ["collected_count"], ["favorite_count"]]),
        "share_count": _pick_int_from_paths(payload, [["share_count"], ["shared_count"]]),
        "share_url": share_url,
        "source_url": source_url,
        "cover_image": cover_image,
        "video_down_url": video_down_url,
        "video_download_url": video_down_url,
    }


def _is_sparse_metadata(metadata_fields: Dict[str, Any]) -> bool:
    if not normalize_text(metadata_fields.get("title")):
        return True
    if not normalize_text(metadata_fields.get("author")):
        return True
    if metadata_fields.get("create_time_sec") is None:
        return True
    metric_keys = ["digg_count", "comment_count", "collect_count", "share_count"]
    return not any(metadata_fields.get(key) is not None for key in metric_keys)


def _append_missing_metadata_fields(missing_fields: List[Dict[str, str]], metadata_fields: Dict[str, Any]) -> None:
    missing_set = {item.get("field") for item in missing_fields if isinstance(item, dict)}

    def _append(field: str) -> None:
        if field in missing_set:
            return
        missing_fields.append({"field": field, "reason": "missing_metadata"})
        missing_set.add(field)

    for key in [
        "title",
        "author",
        "author_handle",
        "platform_author_id",
        "xhs_user_id",
        "xhs_sec_token",
        "share_url",
        "source_url",
        "cover_image",
        "video_down_url",
    ]:
        if not normalize_text(metadata_fields.get(key)):
            _append(key)

    for key in ["create_time_sec", "duration_ms", "digg_count", "comment_count", "collect_count", "share_count"]:
        if metadata_fields.get(key) is None:
            _append(key)


def _fetch_sparse_metadata_enrich(
    *,
    base_url: str,
    token: str,
    timeout_ms: int,
    source_input: Dict[str, Optional[str]],
    note_id: Optional[str],
) -> Dict[str, Any]:
    share_text = source_input.get("share_text")
    resolved_note_id = note_id or source_input.get("note_id") or _extract_note_id_from_share(share_text)

    if _is_short_share_url(share_text) and share_text:
        response = call_json_api(
            base_url=base_url,
            path=WEB_V2_V3_ENDPOINT,
            token=token,
            method="GET",
            timeout_ms=timeout_ms,
            params={"short_url": share_text},
        )
        response["_endpoint"] = WEB_V2_V3_ENDPOINT
        response["_route_label"] = "web_v2_v3_sparse_enrich"
        return response

    if resolved_note_id:
        response = call_json_api(
            base_url=base_url,
            path=WEB_V2_V2_ENDPOINT,
            token=token,
            method="GET",
            timeout_ms=timeout_ms,
            params={"note_id": resolved_note_id},
        )
        response["_endpoint"] = WEB_V2_V2_ENDPOINT
        response["_route_label"] = "web_v2_v2_sparse_enrich"
        return response

    return {
        "ok": False,
        "error": "missing_share_text_and_note_id_for_sparse_enrich",
        "_endpoint": None,
        "_route_label": "web_v2_sparse_enrich_skipped",
    }


def _fetch_note_info(*, base_url: str, token: str, timeout_ms: int, source_input: Dict[str, Optional[str]]) -> Dict[str, Any]:
    attempts: List[Dict[str, Any]] = []

    share_text = source_input.get("share_text")
    note_id = source_input.get("note_id") or _extract_note_id_from_share(share_text)

    def _call(path: str, params: Dict[str, Any], label: str, fallback_reason: Optional[str] = None) -> Dict[str, Any]:
        response = call_json_api(
            base_url=base_url,
            path=path,
            token=token,
            method="GET",
            timeout_ms=timeout_ms,
            params=params,
        )
        response["_endpoint"] = path
        response["_route_label"] = label
        if fallback_reason:
            response["fallback_trigger_reason"] = fallback_reason
        response["_field_completeness"] = _route_field_completeness(response.get("data"), source_input) if response.get("ok") else {
            "fields": {},
            "filled_count": 0,
            "total_fields": 0,
            "ratio": 0.0,
            "missing_core": ["note_id", "title_or_desc", "media"],
            "core_ready": False,
        }
        attempts.append({"label": label, "endpoint": path, "response": response})
        return response

    app_params: Dict[str, Any] = {}
    if share_text:
        app_params["share_text"] = share_text
    if note_id:
        app_params["note_id"] = note_id

    app_v2_attempts = [
        (APP_V2_VIDEO_ENDPOINT, "app_v2_video"),
        (APP_V2_IMAGE_ENDPOINT, "app_v2_image"),
        (APP_V2_MIXED_ENDPOINT, "app_v2_mixed"),
    ]
    next_reason: Optional[str] = None

    for path, label in app_v2_attempts:
        app_v2_response = _call(path, app_params, label, fallback_reason=next_reason)
        if _route_success_for_note(app_v2_response, source_input):
            app_v2_response["_attempts"] = attempts
            return app_v2_response
        if app_v2_response.get("ok"):
            app_v2_response["fallback_trigger_reason"] = "field_completeness_below_threshold"
        next_reason = "field_completeness_below_threshold" if app_v2_response.get("ok") else (
            "primary_timeout_retry_exhausted" if app_v2_response.get("timeout_retry_exhausted") else "primary_non_timeout_failure"
        )

    app_response = _call(APP_V1_ENDPOINT, app_params, "app_v1", fallback_reason=next_reason)
    if _route_success_for_note(app_response, source_input):
        app_response["_attempts"] = attempts
        return app_response
    if app_response.get("ok"):
        app_response["fallback_trigger_reason"] = "field_completeness_below_threshold"

    app_fallback_reason = (
        "field_completeness_below_threshold"
        if app_response.get("ok")
        else ("primary_timeout_retry_exhausted" if app_response.get("timeout_retry_exhausted") else "primary_non_timeout_failure")
    )
    is_short = _is_short_share_url(share_text)

    if is_short and share_text:
        v3_response = _call(
            WEB_V2_V3_ENDPOINT,
            {"short_url": share_text},
            "web_v2_v3_short",
            fallback_reason=app_fallback_reason,
        )
        if v3_response.get("ok"):
            v3_response["_attempts"] = attempts
            return v3_response

    if note_id:
        v2_response = _call(
            WEB_V2_V2_ENDPOINT,
            {"note_id": note_id},
            "web_v2_v2_note_id",
            fallback_reason=app_fallback_reason,
        )
        if v2_response.get("ok"):
            v2_response["_attempts"] = attempts
            return v2_response

    web_params: Dict[str, Any] = {}
    if share_text:
        web_params["share_text"] = share_text
    if note_id:
        web_params["note_id"] = note_id

    web_response = _call(WEB_ENDPOINT, web_params, "web_v7", fallback_reason=app_fallback_reason)
    web_response["_attempts"] = attempts
    return web_response


def _extract_subtitle_urls(payload: Any) -> List[str]:
    urls: List[str] = []
    for key in ["subtitle_url", "subtitleUrl", "srt_url", "srtUrl", "vtt_url", "vttUrl"]:
        for value in deep_find_all(payload, [key]):
            if isinstance(value, str):
                text = value.strip()
                if text.startswith("http://") or text.startswith("https://"):
                    urls.append(text)

    unique: List[str] = []
    seen = set()
    for url in urls:
        if url not in seen:
            unique.append(url)
            seen.add(url)
    return unique


def _extract_subtitle_inline_text(payload: Any) -> str:
    lines: List[str] = []
    subtitle_containers = deep_find_all(payload, ["subtitles", "subtitle_list", "subtitleList"])

    for container in subtitle_containers:
        if isinstance(container, list):
            for item in container:
                if isinstance(item, dict):
                    for key in ["text", "content", "sentence", "line"]:
                        val = item.get(key)
                        if isinstance(val, str) and normalize_text(val):
                            lines.append(normalize_text(val))
                elif isinstance(item, str) and normalize_text(item):
                    lines.append(normalize_text(item))
        elif isinstance(container, dict):
            for key in ["text", "content"]:
                val = container.get(key)
                if isinstance(val, str) and normalize_text(val):
                    lines.append(normalize_text(val))

    deduped = list(dict.fromkeys(lines))
    return "\n".join(deduped).strip()


def _subtitle_text_from_raw(raw: str) -> str:
    if not raw:
        return ""

    raw = raw.strip()
    if not raw:
        return ""

    if raw.startswith("{") or raw.startswith("["):
        try:
            data = json.loads(raw)
            texts: List[str] = []
            if isinstance(data, dict):
                for key in ["segments", "subtitles", "data", "result", "body"]:
                    val = data.get(key)
                    if isinstance(val, list):
                        for item in val:
                            if isinstance(item, dict):
                                t = item.get("text") or item.get("content") or item.get("sentence")
                                if isinstance(t, str) and normalize_text(t):
                                    texts.append(normalize_text(t))
            elif isinstance(data, list):
                for item in data:
                    if isinstance(item, dict):
                        t = item.get("text") or item.get("content") or item.get("sentence")
                        if isinstance(t, str) and normalize_text(t):
                            texts.append(normalize_text(t))
            return "\n".join(dict.fromkeys(texts)).strip()
        except Exception:
            pass

    lines = []
    for line in raw.splitlines():
        t = line.strip()
        if not t:
            continue
        if t.upper() == "WEBVTT":
            continue
        if re.match(r"^\d+$", t):
            continue
        if "-->" in t:
            continue
        if t.startswith("NOTE"):
            continue
        cleaned = normalize_text(t)
        if cleaned:
            lines.append(cleaned)

    return "\n".join(dict.fromkeys(lines)).strip()


def _fetch_subtitle_text(urls: List[str], timeout_ms: int) -> str:
    for url in urls:
        try:
            req = urllib.request.Request(url=url, method="GET")
            with urllib.request.urlopen(req, timeout=max(timeout_ms / 1000.0, 1.0)) as response:
                raw = response.read().decode("utf-8", errors="replace")
            text = _subtitle_text_from_raw(raw)
            if text:
                return text
        except Exception:
            continue
    return ""


def _url_likely_image(url: str) -> bool:
    lower = url.lower()
    image_tokens = [
        ".jpg",
        ".jpeg",
        ".png",
        ".webp",
        "_jpg_",
        "_png_",
        "imageview2",
        "imagemogr2",
        "redimage",
        "frame/",
        "sns-img",
        "sns-webpic",
        "notes_pre_post",
    ]
    return any(token in lower for token in image_tokens)


def _url_likely_video(url: str) -> bool:
    lower = url.lower()
    video_tokens = [
        ".mp4",
        ".m3u8",
        ".m4a",
        ".mp3",
        "video",
        "play",
        "stream",
        "master",
        "sns-video",
        "redvideo",
        "vod",
        "/audio/",
    ]
    if _url_likely_image(url):
        return False
    return any(token in lower for token in video_tokens)


def _video_quality_hint(url: str) -> int:
    lower = url.lower()
    score = 9999

    query = urllib.parse.parse_qs(urllib.parse.urlparse(url).query)
    for key in ("w", "width", "ratio", "quality", "qn"):
        values = query.get(key)
        if not values:
            continue
        value = str(values[0]).lower()
        m = re.search(r"(\d{3,4})", value)
        if m:
            score = min(score, int(m.group(1)))

    for token, value in (("240p", 240), ("360p", 360), ("480p", 480), ("540p", 540), ("576p", 576), ("720p", 720), ("1080p", 1080), ("2k", 2000), ("4k", 4000)):
        if token in lower:
            score = min(score, value)

    return score


def _extract_video_candidates(payload: Any) -> List[str]:
    candidates: List[str] = []
    key_priority = [
        "master_url",
        "masterUrl",
        "video_url",
        "play_url",
        "origin_video_key",
        "origin_video_url",
        "video_play_url",
        "audio_url",
        "note_sound_info",
        "url",
    ]

    for key in key_priority:
        values = deep_find_all(payload, [key])
        for value in values:
            if isinstance(value, str):
                v = value.strip()
                if v.startswith("http://") or v.startswith("https://"):
                    candidates.append(v)
            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, str):
                        v = item.strip()
                        if v.startswith("http://") or v.startswith("https://"):
                            candidates.append(v)
            elif isinstance(value, dict):
                nested = value.get("url") or value.get("play_url")
                if isinstance(nested, str):
                    v = nested.strip()
                    if v.startswith("http://") or v.startswith("https://"):
                        candidates.append(v)

    unique: List[str] = []
    seen = set()
    for url in candidates:
        if url not in seen:
            unique.append(url)
            seen.add(url)

    video_only = [u for u in unique if _url_likely_video(u)]
    if not video_only:
        return []

    scored = sorted(video_only, key=lambda u: (_video_quality_hint(u), video_only.index(u)))
    return scored


def _collect_urls(value: Any) -> List[str]:
    out: List[str] = []
    if isinstance(value, str):
        v = value.strip()
        if v.startswith("http://") or v.startswith("https://"):
            out.append(v)
    elif isinstance(value, list):
        for item in value:
            out.extend(_collect_urls(item))
    elif isinstance(value, dict):
        for key in ("url", "urlDefault", "url_default", "urlPre", "url_pre", "original"):
            if key in value:
                out.extend(_collect_urls(value.get(key)))
    return out


def _dedupe_image_urls(urls: List[str]) -> List[str]:
    unique: List[str] = []
    seen = set()
    for url in urls:
        if url in seen:
            continue
        seen.add(url)
        if _url_likely_image(url):
            unique.append(url)
    return unique


def _extract_image_candidates_with_strategy(payload: Any) -> Tuple[List[str], str]:
    # Priority 1: original image set
    originals = _dedupe_image_urls(deep_find_all(payload, ["original"]))
    if originals:
        return originals, "original"

    # Priority 2: WEB_V2 infoList with WB_DFT scene
    dft_urls: List[str] = []
    for key in ("imageList", "images_list"):
        image_lists = deep_find_all(payload, [key])
        for image_list in image_lists:
            if not isinstance(image_list, list):
                continue
            for item in image_list:
                if not isinstance(item, dict):
                    continue
                info_list = item.get("infoList") or item.get("info_list")
                if isinstance(info_list, list):
                    for info in info_list:
                        if not isinstance(info, dict):
                            continue
                        scene = str(info.get("imageScene") or info.get("image_scene") or "").upper()
                        if scene == "WB_DFT":
                            dft_urls.extend(_collect_urls(info.get("url")))
    dft_urls = _dedupe_image_urls(dft_urls)
    if dft_urls:
        return dft_urls, "wb_dft"

    # Priority 3: default representative image URLs
    default_urls: List[str] = []
    for key in ("urlDefault", "url_default", "urlPre", "url_pre"):
        default_urls.extend(_collect_urls(deep_find_all(payload, [key])))
    default_urls = _dedupe_image_urls(default_urls)
    if default_urls:
        return default_urls, "default"

    # Priority 4: generic fallback (single quality group intended)
    generic: List[str] = []
    for key in ("url", "url_list", "origin_image", "origin_image_url", "cover", "thumb", "image_url"):
        generic.extend(_collect_urls(deep_find_all(payload, [key])))
    generic = _dedupe_image_urls(generic)
    return generic, "fallback"


def _extract_image_candidates(payload: Any) -> List[str]:
    urls, _ = _extract_image_candidates_with_strategy(payload)
    return urls


def _extract_note_type_field(payload: Any) -> str:
    # WEB_V2 schema: note.type
    for note_obj in deep_find_all(payload, ["note"]):
        if isinstance(note_obj, dict):
            note_type = normalize_text(note_obj.get("type")).lower()
            if note_type:
                return note_type

    # APP schema: note_list[].type
    for key in ("note_list", "noteList"):
        for note_list in deep_find_all(payload, [key]):
            if not isinstance(note_list, list):
                continue
            for item in note_list:
                if not isinstance(item, dict):
                    continue
                note_type = normalize_text(item.get("type")).lower()
                if note_type:
                    return note_type

    # Strict fallback: only accept expected scalar values.
    for value in deep_find_all(payload, ["type"]):
        note_type = normalize_text(value).lower()
        if note_type in {"video", "normal", "image"}:
            return note_type

    return ""


def _detect_note_content_type(payload: Any, video_candidates: List[str], image_candidates: List[str]) -> str:
    note_type_value = _extract_note_type_field(payload)
    if note_type_value == "video":
        return "video"
    if note_type_value == "normal":
        return "image"
    if "video" in note_type_value:
        return "video"
    if "image" in note_type_value:
        return "image"

    note_sound_url = normalize_text(deep_find_first(payload, ["note_sound_info", "url"])).lower()
    has_note_audio = bool(note_sound_url and any(token in note_sound_url for token in [".m4a", ".mp3", "/audio/"]))

    has_video = bool(video_candidates) or has_note_audio
    has_image = bool(image_candidates)
    if has_video and has_image:
        return "mixed"
    if has_video:
        return "video"
    if has_image:
        return "image"
    return "unknown"


def _guess_ext_from_url(url: str) -> str:
    parsed = urllib.parse.urlparse(url)
    path = parsed.path.lower()
    for ext in [".jpg", ".jpeg", ".png", ".webp", ".gif"]:
        if path.endswith(ext):
            return ext
    return ".jpg"


def _download_images(
    *,
    urls: List[str],
    timeout_ms: int,
    source_input: Dict[str, Optional[str]],
    note_id: Optional[str],
    storage_config: Optional[Dict[str, Any]],
) -> List[Dict[str, Any]]:
    if not urls:
        return []

    try:
        paths = resolve_storage_paths(storage_config or {})
        base_dir = Path(paths.get("runs_root", "")) / "assets" / datetime.now().strftime("%Y%m%d") / _traceable_identifier(source_input, note_id)
    except Exception:
        base_dir = Path("./tikomni-output/_runs/assets") / datetime.now().strftime("%Y%m%d") / _traceable_identifier(source_input, note_id)

    base_dir.mkdir(parents=True, exist_ok=True)
    results: List[Dict[str, Any]] = []

    for idx, url in enumerate(urls[:30], start=1):
        ext = _guess_ext_from_url(url)
        path = base_dir / f"image-{idx:02d}{ext}"
        try:
            req = urllib.request.Request(url=url, method="GET")
            with urllib.request.urlopen(req, timeout=max(timeout_ms / 1000.0, 1.0)) as response:
                content = response.read()
            path.write_bytes(content)
            results.append({"index": idx, "url": url, "path": str(path), "ok": True})
        except Exception as error:
            results.append({"index": idx, "url": url, "path": str(path), "ok": False, "error": str(error)})

    return results


def _build_result(
    *,
    source_input: Dict[str, Optional[str]],
    raw_content: str,
    confidence: str,
    error_reason: Optional[str],
    extract_trace: List[Dict[str, Any]],
    fallback_trace: List[Dict[str, Any]],
    request_id: Optional[str],
    text_source: str,
    note_id: Optional[str],
    subtitle_hit: bool,
    u2_task_id: Optional[str],
    u2_task_status: Optional[str],
    note_content_type: str,
    analysis_mode: str,
    selected_video_url: Optional[str],
    selected_video_candidates: List[str],
    selected_image_urls: List[str],
    downloaded_assets: List[Dict[str, Any]],
    missing_fields: Optional[List[Dict[str, str]]] = None,
    metadata_fields: Optional[Dict[str, Any]] = None,
    asr_source: Optional[str] = None,
) -> Dict[str, Any]:
    metadata = metadata_fields or {}
    summary_block = summarize_content(raw_content, source=f"xiaohongshu:{text_source}")
    insights = list(summary_block.get("insights", []))
    insights.extend([
        f"note_content_type={note_content_type}",
        f"analysis_mode={analysis_mode}",
        f"selected_image_count={len(selected_image_urls)}",
    ])

    resolved_asr_source = normalize_text(asr_source)
    if not resolved_asr_source:
        if text_source == "subtitle":
            resolved_asr_source = "native_subtitle"
        elif text_source == "u2":
            resolved_asr_source = "external_asr"
        else:
            resolved_asr_source = "fallback_none"

    work_modality = "video" if normalize_text(note_content_type).lower() in {"video", "mixed"} else "text"
    caption_raw = normalize_text(metadata.get("caption_raw"))
    primary_text = raw_content if work_modality == "video" else (caption_raw or raw_content)
    primary_text_source = "asr_clean" if work_modality == "video" else "caption_raw"
    analysis_eligibility = "eligible" if primary_text else "incomplete"
    analysis_exclusion_reason = "" if analysis_eligibility == "eligible" else ("video_asr_unavailable" if work_modality == "video" else "caption_raw_missing")

    return {
        "platform": "xiaohongshu",
        "content_kind": "note",
        "source": source_input,
        "note_id": note_id,
        "note_content_type": note_content_type,
        "analysis_mode": analysis_mode,
        "subtitle_hit": subtitle_hit,
        "text_source": text_source,
        "asr_source": resolved_asr_source,
        "u2_task_id": u2_task_id,
        "u2_task_status": u2_task_status,
        "selected_video_url": selected_video_url,
        "selected_video_candidates": selected_video_candidates,
        "selected_image_urls": selected_image_urls,
        "title": metadata.get("title"),
        "caption_raw": caption_raw,
        "author": metadata.get("author"),
        "create_time_sec": metadata.get("create_time_sec"),
        "publish_time": metadata.get("publish_time"),
        "published_date": _format_published_date(metadata.get("publish_time")),
        "publish_time_source": metadata.get("publish_time_source"),
        "duration_ms": metadata.get("duration_ms"),
        "tags": metadata.get("tags", []),
        "digg_count": metadata.get("digg_count"),
        "comment_count": metadata.get("comment_count"),
        "collect_count": metadata.get("collect_count"),
        "share_count": metadata.get("share_count"),
        "share_url": metadata.get("share_url"),
        "source_url": metadata.get("source_url"),
        "cover_image": metadata.get("cover_image"),
        "video_down_url": metadata.get("video_down_url"),
        "video_download_url": metadata.get("video_download_url") or metadata.get("video_down_url"),
        "work_modality": work_modality,
        "author_handle": metadata.get("author_handle"),
        "platform_author_id": metadata.get("platform_author_id") or metadata.get("author_platform_id"),
        "xhs_user_id": metadata.get("xhs_user_id"),
        "xhs_sec_token": metadata.get("xhs_sec_token"),
        "downloaded_assets": downloaded_assets,
        "raw_content": raw_content,
        "primary_text": primary_text,
        "primary_text_source": primary_text_source,
        "analysis_eligibility": analysis_eligibility,
        "analysis_exclusion_reason": analysis_exclusion_reason,
        "summary": summary_block["summary"],
        "insights": insights,
        "confidence": confidence,
        "error_reason": error_reason,
        "missing_fields": missing_fields or [],
        "extract_trace": extract_trace,
        "fallback_trace": fallback_trace,
        "request_id": request_id,
    }


def run_xiaohongshu_extract(
    *,
    input_value: Optional[str],
    share_text: Optional[str],
    note_id: Optional[str],
    env_file: Optional[str],
    api_key_env: str,
    base_url: Optional[str],
    timeout_ms: Optional[int],
    poll_interval_sec: float,
    max_polls: int,
    u2_submit_max_retries: int,
    u2_submit_backoff_ms: int,
    u2_timeout_retry_enabled: bool,
    u2_timeout_retry_max_retries: int,
    force_u2_fallback: bool,
    write_card: bool,
    card_type: str,
    card_root: Optional[str],
    storage_config: Optional[Dict[str, Any]] = None,
    allow_process_env: bool = False,
    persist_output: bool = True,
    progress: Optional[ProgressReporter] = None,
) -> Dict[str, Any]:
    if not write_card or not persist_output:
        raise ValueError(
            f"fixed_pipeline_requires_full_persistence:xiaohongshu:note:write_card={bool(write_card)}:persist_output={bool(persist_output)}"
        )

    source_input = _normalize_input(input_value, share_text, note_id)
    if progress is not None:
        progress.started(stage="note.workflow", message="xiaohongshu note workflow started")
    metadata_fields: Dict[str, Any] = {}
    if not source_input["share_text"] and not source_input["note_id"]:
        result = _build_result(
            source_input=source_input,
            raw_content="",
            confidence="low",
            error_reason="missing_share_text_or_note_id",
            extract_trace=[],
            fallback_trace=[],
            request_id=None,
            text_source="none",
            note_id=None,
            subtitle_hit=False,
            u2_task_id=None,
            u2_task_status="UNKNOWN",
            note_content_type="unknown",
            analysis_mode="none",
            selected_video_url=None,
            selected_video_candidates=[],
            selected_image_urls=[],
            downloaded_assets=[],
            missing_fields=[{"field": "share_text_or_note_id", "reason": "missing_input"}],
            metadata_fields=metadata_fields,
        )
        if write_card:
            result["card_write"] = write_benchmark_card(
                payload=result,
                platform="xiaohongshu",
                card_type=card_type,
                card_root=card_root,
                content_kind="note",
                storage_config=storage_config,
            )
        return _finalize_result(
            result=result,
            source_input=source_input,
            note_id=None,
            storage_config=storage_config,
            persist_output=persist_output,
        )

    runtime = resolve_runtime(
        env_file=env_file,
        api_key_env=api_key_env,
        base_url=base_url,
        timeout_ms=timeout_ms,
        allow_process_env=allow_process_env,
    )

    trace: List[Dict[str, Any]] = []

    if progress is not None:
        progress.progress(stage="note.fetch", message="fetching xiaohongshu note payload")
    note_response = _fetch_note_info(
        base_url=runtime["base_url"],
        token=runtime["token"],
        timeout_ms=runtime["timeout_ms"],
        source_input=source_input,
    )

    attempts = note_response.get("_attempts") or []
    for index, attempt in enumerate(attempts, start=1):
        response = attempt.get("response") if isinstance(attempt, dict) else None
        endpoint = attempt.get("endpoint") if isinstance(attempt, dict) else None
        label = attempt.get("label") if isinstance(attempt, dict) else None
        if not isinstance(response, dict):
            continue
        step = "u1_get_note_info_effective" if index == len(attempts) else f"u1_get_note_info_attempt_{index}"
        trace.append(
            build_api_trace(
                step=step,
                endpoint=endpoint,
                response=response,
                extra={
                    "route_label": label,
                    "attempt": index,
                    "chosen_route": note_response.get("_route_label"),
                    "field_completeness": response.get("_field_completeness"),
                },
            )
        )

    trace.append(
        {
            "step": "u1_get_note_info_route_decision",
            "chosen_route": note_response.get("_route_label"),
            "request_id": note_response.get("request_id"),
            "field_completeness": note_response.get("_field_completeness"),
            "attempt_count": len(attempts),
        }
    )

    if not note_response.get("ok"):
        error_ctx = resolve_trace_error_context(
            responses=[note_response],
            extract_trace=trace,
            default_error_reason="u1_get_note_info_failed",
        )
        result = _build_result(
            source_input=source_input,
            raw_content="",
            confidence="low",
            error_reason=error_ctx.get("error_reason"),
            extract_trace=trace,
            fallback_trace=error_ctx.get("fallback_trace", []),
            request_id=error_ctx.get("request_id"),
            text_source="none",
            note_id=source_input.get("note_id"),
            subtitle_hit=False,
            u2_task_id=None,
            u2_task_status="UNKNOWN",
            note_content_type="unknown",
            analysis_mode="none",
            selected_video_url=None,
            selected_video_candidates=[],
            selected_image_urls=[],
            downloaded_assets=[],
            missing_fields=[{"field": "u1_note_info", "reason": "all_routes_failed"}],
            metadata_fields=metadata_fields,
        )
        if write_card:
            result["card_write"] = write_benchmark_card(
                payload=result,
                platform="xiaohongshu",
                card_type=card_type,
                card_root=card_root,
                content_kind="note",
                storage_config=storage_config,
            )
        return _finalize_result(
            result=result,
            source_input=source_input,
            note_id=source_input.get("note_id"),
            storage_config=storage_config,
            persist_output=persist_output,
        )

    effective_payload = note_response.get("data")
    app_route_success = str(note_response.get("_route_label") or "").startswith("app")
    metadata_enrich_on_sparse = bool(config_get(storage_config or {}, "xhs.metadata_enrich_on_sparse", True))

    initial_metadata = _extract_xhs_metadata(
        payload=effective_payload,
        source_input=source_input,
        selected_video_url=None,
        selected_image_urls=[],
    )
    sparse_metadata_detected = bool(app_route_success and metadata_enrich_on_sparse and _is_sparse_metadata(initial_metadata))
    metadata_enrich_hit = False
    enrich_response: Optional[Dict[str, Any]] = None
    enrich_payload: Any = None

    if sparse_metadata_detected:
        enrich_response = _fetch_sparse_metadata_enrich(
            base_url=runtime["base_url"],
            token=runtime["token"],
            timeout_ms=runtime["timeout_ms"],
            source_input=source_input,
            note_id=source_input.get("note_id"),
        )
        trace.append(
            build_api_trace(
                step="u1_sparse_metadata_enrich",
                endpoint=enrich_response.get("_endpoint"),
                response=enrich_response,
                extra={"route_label": enrich_response.get("_route_label")},
            )
        )
        if enrich_response.get("ok"):
            metadata_enrich_hit = True
            enrich_payload = enrich_response.get("data")
            effective_payload = {"app": note_response.get("data"), "web_v2_enrich": enrich_payload}

    resolved_note_id = _resolve_note_id(effective_payload, source_input)

    title = normalize_text(deep_find_first(effective_payload, ["title"]))
    desc = normalize_text(deep_find_first(effective_payload, ["desc", "content"]))
    caption_text = "\n".join([t for t in [title, desc] if t]).strip()

    subtitle_inline_text = "" if force_u2_fallback else _extract_subtitle_inline_text(effective_payload)
    subtitle_urls = [] if force_u2_fallback else _extract_subtitle_urls(effective_payload)
    subtitle_url_text = "" if force_u2_fallback else _fetch_subtitle_text(subtitle_urls, runtime["timeout_ms"])
    subtitle_text = subtitle_inline_text or subtitle_url_text

    app_video_candidates = _extract_video_candidates(note_response.get("data"))
    app_image_candidates, image_quality_strategy = _extract_image_candidates_with_strategy(note_response.get("data"))
    enrich_video_candidates = _extract_video_candidates(enrich_payload) if metadata_enrich_hit else []
    enrich_image_candidates = _extract_image_candidates(enrich_payload) if metadata_enrich_hit else []

    video_candidates = _dedupe_keep_order(app_video_candidates + enrich_video_candidates)
    image_candidates = _dedupe_keep_order(app_image_candidates + enrich_image_candidates)

    selected_video_url = video_candidates[0] if video_candidates else None
    type_field_value = _extract_note_type_field(effective_payload)
    note_content_type = _detect_note_content_type(effective_payload, video_candidates, image_candidates)

    metadata_fields = _extract_xhs_metadata(
        payload=effective_payload,
        source_input=source_input,
        selected_video_url=selected_video_url,
        selected_image_urls=image_candidates,
    )

    missing_fields: List[Dict[str, str]] = []
    _append_missing_metadata_fields(missing_fields, metadata_fields)

    trace.append(
        {
            "step": "media_probe",
            "type_field_value": type_field_value,
            "note_content_type": note_content_type,
            "video_candidate_count": len(video_candidates),
            "image_candidate_count": len(image_candidates),
            "image_quality_strategy": image_quality_strategy,
            "subtitle_hit": bool(subtitle_text),
            "subtitle_url_count": len(subtitle_urls),
            "force_u2_fallback": force_u2_fallback,
            "sparse_metadata_detected": sparse_metadata_detected,
            "metadata_enrich_hit": metadata_enrich_hit,
            "candidate_merge_sources": {
                "video": _build_candidate_merge_sources(
                    app_candidates=app_video_candidates,
                    enrich_candidates=enrich_video_candidates,
                    app_label="app",
                ),
                "image": _build_candidate_merge_sources(
                    app_candidates=app_image_candidates,
                    enrich_candidates=enrich_image_candidates,
                    app_label="app",
                ),
            },
        }
    )

    u2_gate = _evaluate_u2_gate_for_xhs(
        note_content_type=note_content_type,
        duration_ms=metadata_fields.get("duration_ms"),
        video_down_url=metadata_fields.get("video_down_url") or selected_video_url,
    )
    trace.append(
        {
            "step": "u2_gate",
            "can_u2": bool(u2_gate.get("can_u2")),
            "gate_reason": u2_gate.get("gate_reason"),
            "rule": U2_GATE_RULE,
            "is_video": u2_gate.get("is_video"),
            "duration_ms": u2_gate.get("duration_ms"),
            "video_download_url_present": u2_gate.get("video_download_url_present"),
        }
    )

    # Video-note path: aligned with douyin single-video pipeline (subtitle-first difference retained).
    if note_content_type in {"video", "mixed"}:
        if subtitle_text:
            success_ctx = resolve_trace_error_context(
                responses=[note_response],
                extract_trace=trace,
                explicit_error_reason=None,
                explicit_request_id=note_response.get("request_id"),
            )
            result = _build_result(
                source_input=source_input,
                raw_content=subtitle_text,
                confidence="high",
                error_reason=None,
                extract_trace=trace,
                fallback_trace=success_ctx.get("fallback_trace", []),
                request_id=success_ctx.get("request_id"),
                text_source="subtitle",
                note_id=str(resolved_note_id) if resolved_note_id else source_input.get("note_id"),
                subtitle_hit=True,
                u2_task_id=None,
                u2_task_status="SKIPPED",
                note_content_type=note_content_type,
                analysis_mode="video_full",
                selected_video_url=selected_video_url,
                selected_video_candidates=video_candidates,
                selected_image_urls=image_candidates,
                downloaded_assets=[],
                missing_fields=missing_fields,
                metadata_fields=metadata_fields,
            )
            if write_card:
                result["card_write"] = write_benchmark_card(
                    payload=result,
                    platform="xiaohongshu",
                    card_type=card_type,
                    card_root=card_root,
                    content_kind="single_video",
                    storage_config=storage_config,
                )
            return _finalize_result(
                result=result,
                source_input=source_input,
                note_id=str(resolved_note_id) if resolved_note_id else source_input.get("note_id"),
                storage_config=storage_config,
                persist_output=persist_output,
            )

        if not u2_gate.get("can_u2"):
            gate_reason = normalize_text(u2_gate.get("gate_reason")) or "skip:unknown"
            if gate_reason == "skip:duration_missing":
                missing_fields.append({"field": "duration_ms", "reason": gate_reason})
            elif gate_reason in {"skip:duration_too_short", "skip:duration_too_long"}:
                missing_fields.append({"field": "duration_ms", "reason": gate_reason})
            elif gate_reason == "skip:video_download_url_missing":
                missing_fields.append({"field": "video_download_url", "reason": gate_reason})
            elif gate_reason == "skip:not_video":
                missing_fields.append({"field": "note_content_type", "reason": gate_reason})

            error_ctx = resolve_trace_error_context(
                responses=[note_response],
                extract_trace=trace,
                default_error_reason=gate_reason,
            )
            fallback_text = caption_text
            result = _build_result(
                source_input=source_input,
                raw_content=fallback_text,
                confidence="medium" if fallback_text else "low",
                error_reason=None if fallback_text else error_ctx.get("error_reason"),
                extract_trace=trace,
                fallback_trace=error_ctx.get("fallback_trace", []),
                request_id=error_ctx.get("request_id"),
                text_source="caption_fallback" if fallback_text else "none",
                note_id=str(resolved_note_id) if resolved_note_id else source_input.get("note_id"),
                subtitle_hit=False,
                u2_task_id=None,
                u2_task_status="SKIPPED",
                note_content_type=note_content_type,
                analysis_mode="video_full",
                selected_video_url=u2_gate.get("video_down_url") or selected_video_url,
                selected_video_candidates=video_candidates,
                selected_image_urls=image_candidates,
                downloaded_assets=[],
                missing_fields=missing_fields,
                metadata_fields=metadata_fields,
            )
            if write_card:
                result["card_write"] = write_benchmark_card(
                    payload=result,
                    platform="xiaohongshu",
                    card_type=card_type,
                    card_root=card_root,
                    content_kind="single_video",
                    storage_config=storage_config,
                )
            return _finalize_result(
                result=result,
                source_input=source_input,
                note_id=str(resolved_note_id) if resolved_note_id else source_input.get("note_id"),
                storage_config=storage_config,
                persist_output=persist_output,
            )

        u2_candidates = _dedupe_keep_order([u2_gate.get("video_down_url")] + list(video_candidates))
        if progress is not None:
            progress.progress(
                stage="note.u2",
                message="starting xiaohongshu u2 flow",
                data={"candidate_count": len(u2_candidates)},
            )
        u2_bundle = run_u2_asr_candidates_with_timeout_retry(
            base_url=runtime["base_url"],
            token=runtime["token"],
            timeout_ms=runtime["timeout_ms"],
            candidates=u2_candidates,
            submit_max_retries=u2_submit_max_retries,
            submit_backoff_ms=u2_submit_backoff_ms,
            poll_interval_sec=poll_interval_sec,
            max_polls=max_polls,
            timeout_retry_enabled=u2_timeout_retry_enabled,
            timeout_retry_max_retries=u2_timeout_retry_max_retries,
        )
        submit_bundle = u2_bundle.get("submit_bundle", {})
        submit_response = submit_bundle.get("submit_response", {})
        task_id = submit_bundle.get("task_id")
        poll_result = u2_bundle.get("poll_result", {})
        selected_video_url = u2_bundle.get("chosen_candidate") or selected_video_url
        if selected_video_url and not normalize_text(metadata_fields.get("video_down_url")):
            metadata_fields["video_down_url"] = selected_video_url

        trace.append(
            {
                "step": "u2_asr_timeout_retry",
                "endpoint": "/api/u2/v1/services/audio/asr/transcription + /api/u2/v1/tasks/{task_id}",
                "selected_video_url": selected_video_url,
                "selected_video_candidates": u2_candidates,
                "candidate_attempts": u2_bundle.get("candidate_attempts", []),
                "submit_retries_config": {
                    "u2_submit_max_retries": max(0, int(u2_submit_max_retries)),
                    "u2_submit_backoff_ms": max(0, int(u2_submit_backoff_ms)),
                },
                "timeout_retry": u2_bundle.get("timeout_retry", {}),
                "rounds": u2_bundle.get("rounds", []),
                "final_task_id": poll_result.get("task_id") or task_id,
                "final_task_status": poll_result.get("task_status"),
                "final_error_reason": poll_result.get("error_reason"),
            }
        )
        if progress is not None:
            (progress.done if poll_result.get("ok") else progress.failed)(
                stage="note.u2",
                message="xiaohongshu u2 flow finished" if poll_result.get("ok") else "xiaohongshu u2 flow failed",
                data={
                    "task_id": poll_result.get("task_id") or task_id,
                    "task_status": poll_result.get("task_status"),
                    "error_reason": poll_result.get("error_reason"),
                },
            )

        if not poll_result.get("ok") and (
            not submit_response.get("ok") or not (poll_result.get("task_id") or task_id)
        ):
            error_ctx = resolve_trace_error_context(
                responses=[poll_result, submit_response, note_response],
                extract_trace=trace,
                default_error_reason="u2_submit_failed_or_missing_task_id",
                explicit_request_id=(
                    poll_result.get("request_id")
                    or submit_response.get("request_id")
                    or note_response.get("request_id")
                ),
            )
            fallback_text = caption_text
            if fallback_text:
                missing_fields.append({"field": "asr_transcript", "reason": f"u2_failed:{error_ctx.get('error_reason')}"})
            else:
                missing_fields.append({"field": "raw_content", "reason": "u2_failed_and_caption_missing"})
            result = _build_result(
                source_input=source_input,
                raw_content=fallback_text,
                confidence="medium" if fallback_text else "low",
                error_reason=None if fallback_text else error_ctx.get("error_reason"),
                extract_trace=trace,
                fallback_trace=error_ctx.get("fallback_trace", []),
                request_id=error_ctx.get("request_id"),
                text_source="caption_fallback" if fallback_text else "u2",
                note_id=str(resolved_note_id) if resolved_note_id else source_input.get("note_id"),
                subtitle_hit=False,
                u2_task_id=poll_result.get("task_id") or task_id,
                u2_task_status=poll_result.get("task_status") or "UNKNOWN",
                note_content_type=note_content_type,
                analysis_mode="video_full",
                selected_video_url=selected_video_url,
                selected_video_candidates=u2_candidates,
                selected_image_urls=image_candidates,
                downloaded_assets=[],
                missing_fields=missing_fields,
                metadata_fields=metadata_fields,
            )
            if write_card:
                result["card_write"] = write_benchmark_card(
                    payload=result,
                    platform="xiaohongshu",
                    card_type=card_type,
                    card_root=card_root,
                    content_kind="single_video",
                    storage_config=storage_config,
                )
            return _finalize_result(
                result=result,
                source_input=source_input,
                note_id=str(resolved_note_id) if resolved_note_id else source_input.get("note_id"),
                storage_config=storage_config,
                persist_output=persist_output,
            )

        raw_content = poll_result.get("transcript_text", "") if poll_result.get("ok") else ""
        final_ctx = resolve_trace_error_context(
            responses=[poll_result, submit_response, note_response],
            extract_trace=trace,
            explicit_error_reason=poll_result.get("error_reason"),
            explicit_request_id=poll_result.get("request_id") or submit_response.get("request_id") or note_response.get("request_id"),
        )
        result = _build_result(
            source_input=source_input,
            raw_content=raw_content,
            confidence="high" if poll_result.get("ok") and raw_content else "low",
            error_reason=final_ctx.get("error_reason"),
            extract_trace=trace,
            fallback_trace=final_ctx.get("fallback_trace", []),
            request_id=final_ctx.get("request_id"),
            text_source="u2",
            note_id=str(resolved_note_id) if resolved_note_id else source_input.get("note_id"),
            subtitle_hit=False,
            u2_task_id=poll_result.get("task_id") or task_id,
            u2_task_status=poll_result.get("task_status"),
            note_content_type=note_content_type,
            analysis_mode="video_full",
            selected_video_url=selected_video_url,
            selected_video_candidates=u2_candidates,
            selected_image_urls=image_candidates,
            downloaded_assets=[],
            missing_fields=missing_fields,
            metadata_fields=metadata_fields,
        )

        if write_card:
            result["card_write"] = write_benchmark_card(
                payload=result,
                platform="xiaohongshu",
                card_type=card_type,
                card_root=card_root,
                content_kind="single_video",
                storage_config=storage_config,
            )

        return _finalize_result(
            result=result,
            source_input=source_input,
            note_id=str(resolved_note_id) if resolved_note_id else source_input.get("note_id"),
            storage_config=storage_config,
            persist_output=persist_output,
        )

    # Image-note path, strategy B: download images + light text analysis + write card.
    raw_content = caption_text

    downloaded_assets = _download_images(
        urls=image_candidates,
        timeout_ms=runtime["timeout_ms"],
        source_input=source_input,
        note_id=str(resolved_note_id) if resolved_note_id else source_input.get("note_id"),
        storage_config=storage_config,
    )

    if not image_candidates:
        missing_fields.append({"field": "selected_image_urls", "reason": "image_note_but_no_image_url"})
    if not raw_content:
        missing_fields.append({"field": "raw_content", "reason": "title_and_desc_missing"})

    success_ctx = resolve_trace_error_context(
        responses=[note_response],
        extract_trace=trace,
        explicit_error_reason=None,
        explicit_request_id=note_response.get("request_id"),
    )

    result = _build_result(
        source_input=source_input,
        raw_content=raw_content,
        confidence="high" if raw_content else "medium",
        error_reason=None,
        extract_trace=trace,
        fallback_trace=success_ctx.get("fallback_trace", []),
        request_id=success_ctx.get("request_id"),
        text_source="caption",
        note_id=str(resolved_note_id) if resolved_note_id else source_input.get("note_id"),
        subtitle_hit=False,
        u2_task_id=None,
        u2_task_status="SKIPPED",
        note_content_type="image" if note_content_type == "unknown" else note_content_type,
        analysis_mode="image_light_analysis",
        selected_video_url=None,
        selected_video_candidates=video_candidates,
        selected_image_urls=image_candidates,
        downloaded_assets=downloaded_assets,
        missing_fields=missing_fields,
        metadata_fields=metadata_fields,
    )

    if write_card:
        result["card_write"] = write_benchmark_card(
            payload=result,
            platform="xiaohongshu",
            card_type=card_type,
            card_root=card_root,
            content_kind="note",
            storage_config=storage_config,
        )

    finalized = _finalize_result(
        result=result,
        source_input=source_input,
        note_id=str(resolved_note_id) if resolved_note_id else source_input.get("note_id"),
        storage_config=storage_config,
        persist_output=persist_output,
    )
    if progress is not None:
        final_event = progress.failed if finalized.get("error_reason") else progress.done
        final_event(
            stage="note.workflow",
            message="xiaohongshu note workflow finished" if not finalized.get("error_reason") else "xiaohongshu note workflow failed",
            data={
                "request_id": finalized.get("request_id"),
                "card_write_ok": bool((finalized.get("card_write") or {}).get("ok")),
                "output_persist_ok": bool((finalized.get("output_persist") or {}).get("ok")),
                "text_source": finalized.get("text_source"),
            },
        )
    return finalized


def main() -> None:
    parser = argparse.ArgumentParser(description="Run xiaohongshu extraction chain")
    parser.add_argument("input", nargs="?", default=None, help="Share URL or note_id")
    parser.add_argument("--share-text", default=None, help="Xiaohongshu share URL/text")
    parser.add_argument("--note-id", default=None, help="Xiaohongshu note_id")
    parser.add_argument("--config", default=None, help="Runtime config YAML path")
    parser.add_argument("--env-file", default=None, help="Optional env file path")
    parser.add_argument("--allow-process-env", action="store_true", help="Allow process env to override .env/.env.local")
    parser.add_argument("--api-key-env", default=None, help="API key env variable name")
    parser.add_argument("--base-url", default=None, help="Tikomni base URL")
    parser.add_argument("--timeout-ms", type=int, default=None, help="Request timeout ms")
    parser.add_argument("--poll-interval-sec", type=float, default=None, help="U2 polling interval seconds")
    parser.add_argument("--max-polls", type=int, default=None, help="Max U2 polls")
    parser.add_argument(
        "--u2-submit-max-retries",
        type=int,
        default=None,
        help="Max retries for retriable U2 submit failures",
    )
    parser.add_argument(
        "--u2-submit-backoff-ms",
        type=int,
        default=None,
        help="Base backoff ms for retriable U2 submit failures (exponential)",
    )
    parser.add_argument(
        "--u2-timeout-retry-enabled",
        type=str,
        choices=["true", "false"],
        default=None,
        help="Enable conservative retry only when U2 polling times out",
    )
    parser.add_argument(
        "--u2-timeout-retry-max-retries",
        type=int,
        default=None,
        help="Conservative max retries for U2 timeout-only retry (0~3)",
    )
    parser.add_argument("--force-u2-fallback", action="store_true", help="Skip subtitle usage and force U2 fallback (test)")
    parser.add_argument("--card-type", choices=["work", "author", "author_sample_work"], default="work", help="Primary card type")
    parser.add_argument("--card-root", default=None, help="Card root (absolute); falls back to TIKOMNI_CARD_ROOT when writing cards")
    args = parser.parse_args()

    config, _ = load_tikomni_config(
        args.config,
        env_file=args.env_file,
        allow_process_env=args.allow_process_env,
    )

    resolved_env_file = args.env_file or config_get(config, "runtime.env_file", None)
    api_key_env = args.api_key_env or config_get(config, "runtime.auth_env_key", "TIKOMNI_API_KEY")
    base_url = args.base_url or config_get(config, "runtime.base_url", None)
    timeout_ms = args.timeout_ms if args.timeout_ms is not None else config_get(config, "runtime.timeout_ms", None)
    poll_interval_sec = (
        args.poll_interval_sec
        if args.poll_interval_sec is not None
        else config_get(config, "asr_strategy.poll_interval_sec", 3.0)
    )
    max_polls = args.max_polls if args.max_polls is not None else config_get(config, "asr_strategy.max_polls", 30)
    u2_submit_max_retries = (
        args.u2_submit_max_retries
        if args.u2_submit_max_retries is not None
        else config_get(config, "asr_strategy.submit_retry.xiaohongshu_note.max_retries", 0)
    )
    u2_submit_backoff_ms = (
        args.u2_submit_backoff_ms
        if args.u2_submit_backoff_ms is not None
        else config_get(config, "asr_strategy.submit_retry.xiaohongshu_note.backoff_ms", 0)
    )
    u2_timeout_retry_enabled = (
        (str(args.u2_timeout_retry_enabled).lower() == "true")
        if args.u2_timeout_retry_enabled is not None
        else bool(config_get(config, "asr_strategy.u2_timeout_retry.enabled", True))
    )
    u2_timeout_retry_max_retries = (
        args.u2_timeout_retry_max_retries
        if args.u2_timeout_retry_max_retries is not None
        else config_get(config, "asr_strategy.u2_timeout_retry.max_retries", 3)
    )

    try:
        result = run_xiaohongshu_extract(
            input_value=args.input,
            share_text=args.share_text,
            note_id=args.note_id,
            env_file=resolved_env_file,
            api_key_env=api_key_env,
            base_url=base_url,
            timeout_ms=timeout_ms,
            poll_interval_sec=float(poll_interval_sec),
            max_polls=int(max_polls),
            u2_submit_max_retries=int(u2_submit_max_retries),
            u2_submit_backoff_ms=int(u2_submit_backoff_ms),
            u2_timeout_retry_enabled=bool(u2_timeout_retry_enabled),
            u2_timeout_retry_max_retries=int(u2_timeout_retry_max_retries),
            force_u2_fallback=args.force_u2_fallback,
            write_card=True,
            card_type=args.card_type,
            card_root=args.card_root,
            storage_config=config,
            allow_process_env=args.allow_process_env,
            persist_output=True,
        )
    except ValueError as error:
        result = {
            "platform": "xiaohongshu",
            "content_kind": "note",
            "raw_content": "",
            "summary": "",
            "insights": ["source=xiaohongshu:runtime", "runtime_not_ready"],
            "confidence": "low",
            "error_reason": str(error),
            "missing_fields": [],
            "extract_trace": [],
            "fallback_trace": [],
            "request_id": None,
        }

    write_json_stdout(result)
    raise SystemExit(0 if not result.get("error_reason") else 1)


if __name__ == "__main__":
    main()
