#!/usr/bin/env python3
"""Douyin single-work fixed pipeline runner (APP first, WEB fallback)."""

from __future__ import annotations

if __package__ in {None, ""}:
    import sys
    from pathlib import Path

    _self = Path(__file__).resolve()
    for _parent in _self.parents:
        if (_parent / "scripts" / "core" / "bootstrap_env.py").is_file():
            sys.path.insert(0, str(_parent))
            break


import argparse

from scripts.core.bootstrap_env import bootstrap_for_direct_run

bootstrap_for_direct_run(__file__, __package__)
import hashlib
import json
import re
import time
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

from scripts.core.config_loader import config_get, load_tikomni_config
from scripts.core.extract_pipeline import resolve_trace_error_context
from scripts.core.progress_report import ProgressReporter, build_progress_reporter
from scripts.pipelines.douyin_video_type_matrix import normalize_douyin_video_type
from scripts.pipelines.douyin_metadata import (
    extract_douyin_author as extract_shared_douyin_author,
    extract_douyin_caption as extract_shared_douyin_caption,
    extract_douyin_metrics as extract_shared_douyin_metrics,
    extract_douyin_title as extract_shared_douyin_title,
)
from scripts.pipelines.input_contracts import normalize_douyin_work_input
from scripts.core.asr_pipeline import derive_asr_clean_text, run_u2_asr_with_timeout_retry
from scripts.pipelines.select_low_quality_video_url import select_low_quality_video_url
from scripts.core.tikomni_common import (
    call_json_api,
    deep_find_all,
    normalize_text,
    resolve_runtime,
    summarize_content,
    write_json_stdout,
)
from scripts.writers.write_work_fact_card import (
    build_work_output_envelope,
    persist_output_envelope,
    write_work_fact_card,
)

APP_ENDPOINT = "/api/u1/v1/douyin/app/v3/fetch_one_video_by_share_url"
WEB_ENDPOINT = "/api/u1/v1/douyin/web/fetch_one_video_by_share_url"
U2_SUBMIT_ENDPOINT = "/api/u2/v1/services/audio/asr/transcription"
U2_REQUEST_TIMEOUT_CAP_MS = 15000


def _format_published_date(value: Any) -> str:
    if value is None:
        return "N/A"
    try:
        timestamp = int(value)
        if timestamp > 1_000_000_000_000:
            timestamp //= 1000
        if timestamp <= 0:
            return "N/A"
        return datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d")
    except Exception:
        return "N/A"




def _safe_slug(value: Optional[str], fallback: str = "unknown") -> str:
    text = normalize_text(value)
    if not text:
        return fallback
    lowered = text.lower()
    slug = re.sub(r"[^a-z0-9_-]+", "-", lowered).strip("-")
    return slug[:64] or fallback


def _traceable_identifier(source_input: Dict[str, Optional[str]], platform_work_id: Optional[str]) -> str:
    if platform_work_id:
        return _safe_slug(platform_work_id)

    share_url = normalize_text(source_input.get("share_url"))
    if not share_url:
        return "missing_input"

    digest = hashlib.sha1(share_url.encode("utf-8")).hexdigest()[:10]
    return f"url-{digest}"


def _resolve_u2_timeout_ms(timeout_ms: Any) -> int:
    try:
        parsed = int(timeout_ms)
    except Exception:
        parsed = U2_REQUEST_TIMEOUT_CAP_MS
    if parsed <= 0:
        return U2_REQUEST_TIMEOUT_CAP_MS
    return max(5000, min(parsed, U2_REQUEST_TIMEOUT_CAP_MS))


def _report_u2_progress(progress: Optional[ProgressReporter], *, stage: str, event: Dict[str, Any], label: str) -> None:
    if progress is None:
        return

    phase = normalize_text(event.get("phase")).lower()
    state = normalize_text(event.get("state")).lower()
    payload = {
        "phase": phase or "poll",
        "state": state or "",
        "task_id": event.get("task_id"),
        "attempt": event.get("attempt"),
        "task_status": event.get("task_status"),
        "platform_task_status": event.get("platform_task_status"),
        "pending_count": event.get("pending_count"),
        "status_code": event.get("status_code"),
        "batch_progress": event.get("batch_progress"),
        "wait_ms": event.get("wait_ms"),
        "candidate_count": event.get("candidate_count"),
        "ok": event.get("ok"),
        "error_reason": event.get("error_reason"),
        "retriable": event.get("retriable"),
        "request_id": event.get("request_id"),
    }
    message = f"{label} u2 {phase or 'poll'} {state or 'progress'}"
    if phase == "submit" and state == "heartbeat":
        progress.heartbeat(stage=stage, message=message, data=payload)
        return
    progress.progress(stage=stage, message=message, data=payload)


def _finalize_result(
    *,
    result: Dict[str, Any],
    source_input: Dict[str, Optional[str]],
    platform_work_id: Optional[str],
    storage_config: Optional[Dict[str, Any]],
    persist_output: bool,
) -> Dict[str, Any]:
    envelope = build_work_output_envelope(result, platform="douyin")
    if "card_write" in result:
        envelope["card_write"] = result.get("card_write")
    if not persist_output:
        envelope["output_persist"] = {"enabled": False, "skipped": True, "reason": "disabled_by_flag"}
        return envelope
    envelope["output_persist"] = persist_output_envelope(
        envelope=envelope,
        storage_config=storage_config,
        platform="douyin",
        fallback_identifier=platform_work_id or _traceable_identifier(source_input, platform_work_id),
    )
    return envelope

def _normalize_input(
    input_value: Optional[str],
    share_url: Optional[str],
) -> Dict[str, Optional[str]]:
    normalized = normalize_douyin_work_input(input_value, share_url)
    return {"share_url": normalize_text(normalized.get("share_url")) or None}


def _extract_aweme_detail(payload: Any) -> Optional[Dict[str, Any]]:
    if isinstance(payload, dict):
        direct = payload.get("aweme_detail")
        if isinstance(direct, dict):
            return direct

        for list_key in ("aweme_details", "aweme_list", "item_list", "items"):
            values = payload.get(list_key)
            if isinstance(values, list) and values:
                first = values[0]
                if isinstance(first, dict):
                    return first

        nested_data = payload.get("data")
        if nested_data is not None:
            hit = _extract_aweme_detail(nested_data)
            if hit:
                return hit

        for value in payload.values():
            hit = _extract_aweme_detail(value)
            if hit:
                return hit

    elif isinstance(payload, list):
        for item in payload:
            hit = _extract_aweme_detail(item)
            if hit:
                return hit

    return None


def _safe_int(value: Any) -> Optional[int]:
    if value is None:
        return None
    if isinstance(value, bool):
        return 1 if value else 0
    if isinstance(value, int):
        return value
    if isinstance(value, float):
        return int(value)
    if isinstance(value, str):
        text = value.strip()
        if text.startswith("-"):
            sign = -1
            text = text[1:]
        else:
            sign = 1
        if text.isdigit():
            return sign * int(text)
    return None


def _normalize_duration_ms(item: Dict[str, Any]) -> Optional[int]:
    raw = item.get("duration")
    if raw is None:
        video = item.get("video")
        if isinstance(video, dict):
            raw = video.get("duration")

    value = _safe_int(raw)
    if value is None:
        return None

    # Douyin commonly uses ms; convert obvious second-level durations.
    if 0 < value < 10000:
        return value * 1000
    return value


def _pick_title(item: Dict[str, Any]) -> str:
    return extract_shared_douyin_title(item)


def _pick_desc(item: Dict[str, Any]) -> str:
    return extract_shared_douyin_caption(item)


def _extract_author(item: Dict[str, Any]) -> Dict[str, Optional[str]]:
    return extract_shared_douyin_author(item)


def _extract_metrics(item: Dict[str, Any]) -> Dict[str, Optional[int]]:
    return extract_shared_douyin_metrics(item)


def _extract_platform_work_id(item: Dict[str, Any]) -> Optional[str]:
    for key in ("aweme_id", "item_id", "id"):
        value = item.get(key)
        if value is None:
            continue
        text = normalize_text(value)
        if text:
            return text

    statistics = item.get("statistics")
    if isinstance(statistics, dict):
        value = statistics.get("aweme_id")
        text = normalize_text(value)
        if text:
            return text
    return None


def _extract_create_time_sec(item: Dict[str, Any]) -> Optional[int]:
    for key in ("create_time", "aweme_create_time"):
        value = _safe_int(item.get(key))
        if value is not None and value > 0:
            return value
    return None


def _pick_first_url(value: Any) -> Optional[str]:
    if isinstance(value, str):
        text = value.strip()
        return text or None
    if isinstance(value, list):
        for item in value:
            if isinstance(item, str) and item.strip():
                return item.strip()
    if isinstance(value, dict):
        for key in ("url_list", "url", "uri"):
            hit = _pick_first_url(value.get(key))
            if hit:
                return hit
    return None


def _extract_cover_image(item: Dict[str, Any]) -> Optional[str]:
    # prefer video-level covers
    video = item.get("video") if isinstance(item.get("video"), dict) else {}
    for key in ("cover", "origin_cover", "dynamic_cover"):
        hit = _pick_first_url(video.get(key))
        if hit:
            return hit

    # fallback to item-level covers
    for key in ("cover", "origin_cover", "dynamic_cover"):
        hit = _pick_first_url(item.get(key))
        if hit:
            return hit

    return None


def _clean_tag_text(value: Any) -> str:
    text = normalize_text(value)
    if not text:
        return ""
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
        text = value.strip()
        if not text:
            return
        if text.startswith("{") or text.startswith("["):
            try:
                parsed = json.loads(text)
                _extract_tags_from_container(parsed, output, seen)
                return
            except Exception:
                pass
        for part in re.split(r"[,，\s]+", text):
            _append_tag(part, output, seen)
        return

    if isinstance(value, list):
        for item in value:
            _extract_tags_from_container(item, output, seen)
        return

    if isinstance(value, dict):
        for key in ("hashtag_name", "cha_name", "name", "tag_name", "topic_name", "hashtag"):
            _append_tag(value.get(key), output, seen)


def _extract_douyin_tags(item: Dict[str, Any]) -> List[str]:
    tags: List[str] = []
    seen: set = set()

    for value in deep_find_all(item, ["text_extra"]):
        _extract_tags_from_container(value, tags, seen)

    for value in deep_find_all(item, ["cha_list"]):
        _extract_tags_from_container(value, tags, seen)

    for value in deep_find_all(item, ["hashtag"]):
        _extract_tags_from_container(value, tags, seen)

    for common_flags in deep_find_all(item, ["common_flags"]):
        if not isinstance(common_flags, str):
            continue
        try:
            parsed = json.loads(common_flags)
        except Exception:
            continue
        _extract_tags_from_container(parsed.get("hashtag"), tags, seen)

    for text_field in (normalize_text(item.get("caption")), normalize_text(item.get("desc"))):
        if not text_field:
            continue
        for match in re.findall(r"#([^#\s]+)", text_field):
            _append_tag(match, tags, seen)

    return tags


def _u1_fetch_one_video(
    *,
    base_url: str,
    token: str,
    share_url: str,
    app_timeout_ms: int,
    web_timeout_ms: int,
) -> Dict[str, Any]:
    app_response = call_json_api(
        base_url=base_url,
        path=APP_ENDPOINT,
        token=token,
        method="GET",
        timeout_ms=app_timeout_ms,
        params={"share_url": share_url},
    )
    app_response["_endpoint"] = APP_ENDPOINT
    if app_response.get("ok"):
        return app_response

    app_response["fallback_trigger_reason"] = (
        "primary_timeout_retry_exhausted" if app_response.get("timeout_retry_exhausted") else "primary_non_timeout_failure"
    )
    web_response = call_json_api(
        base_url=base_url,
        path=WEB_ENDPOINT,
        token=token,
        method="GET",
        timeout_ms=web_timeout_ms,
        params={"share_url": share_url},
    )
    web_response["_endpoint"] = WEB_ENDPOINT
    web_response["_app_failed"] = app_response
    web_response["fallback_trigger_reason"] = app_response.get("fallback_trigger_reason")
    return web_response


def _trace_step(
    *,
    step: str,
    endpoint: Optional[str] = None,
    response: Optional[Dict[str, Any]] = None,
    extra: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    payload: Dict[str, Any] = {"step": step}
    if endpoint:
        payload["endpoint"] = endpoint
    if response is not None:
        payload.update(
            {
                "ok": response.get("ok"),
                "status_code": response.get("status_code"),
                "request_id": response.get("request_id"),
                "error_reason": response.get("error_reason"),
                "rate_limit_wait_ms": response.get("rate_limit_wait_ms", 0),
                "retry_attempt": response.get("retry_attempt", 0),
                "fallback_trigger_reason": response.get("fallback_trigger_reason"),
            }
        )
    if extra:
        payload.update(extra)
    return payload


def _empty_metrics() -> Dict[str, Optional[int]]:
    return {
        "digg_count": 0,
        "comment_count": 0,
        "collect_count": 0,
        "share_count": 0,
        "play_count": None,
    }


def _empty_timings() -> Dict[str, int]:
    return {
        "url_parse_ms": 0,
        "u1_total_ms": 0,
        "u2_submit_ms": 0,
        "u2_poll_ms": 0,
        "card_write_ms": 0,
        "llm_analysis_ms": 0,
        "total_ms": 0,
    }


def _elapsed_ms(started_at: float) -> int:
    return int((time.perf_counter() - started_at) * 1000)


def _u1_response_summary(response: Dict[str, Any]) -> Dict[str, Any]:
    payload = response.get("data")
    item = _extract_aweme_detail(payload)
    return {
        "platform_work_id": _extract_platform_work_id(item or {}) if isinstance(item, dict) else None,
        "title_hit": bool(_pick_title(item or {})) if isinstance(item, dict) else False,
        "desc_hit": bool(_pick_desc(item or {})) if isinstance(item, dict) else False,
        "video_url_present": bool(normalize_text((item or {}).get("video_down_url"))) if isinstance(item, dict) else False,
    }


def _emit_http_progress(
    progress: Optional[ProgressReporter],
    *,
    stage: str,
    response: Dict[str, Any],
    route_label: str,
) -> None:
    if progress is None:
        return
    progress.http_event(
        stage=stage,
        endpoint=str(response.get("_endpoint") or route_label),
        response=response,
        route_label=route_label,
        summary=_u1_response_summary(response),
    )


def _update_pipeline_status(result: Dict[str, Any]) -> None:
    card_write = result.get("card_write") if isinstance(result.get("card_write"), dict) else {}
    deep_analysis = result.get("deep_analysis") if isinstance(result.get("deep_analysis"), dict) else {}
    result["pipeline_status"] = {
        "facts_ready": True,
        "card_ready": bool(card_write.get("ok")),
        "deep_analysis": deep_analysis.get("status") or "skipped",
    }


def _build_missing_fields(
    *,
    title: str,
    desc: str,
    platform_work_id: Optional[str],
    video_down_url: Optional[str],
    author: Dict[str, Optional[str]],
) -> List[Dict[str, str]]:
    missing: List[Dict[str, str]] = []

    def _append(field: str) -> None:
        missing.append({"field": field, "reason": "missing_metadata"})

    if not normalize_text(title):
        _append("title")
    if not normalize_text(desc):
        _append("desc")
    if not normalize_text(platform_work_id):
        _append("platform_work_id")
    if not normalize_text(video_down_url):
        _append("video_down_url")

    author_key_map = {
        "author_handle": ("author_handle",),
        "platform_author_id": ("platform_author_id", "author_platform_id"),
        "douyin_sec_uid": ("douyin_sec_uid",),
        "douyin_aweme_author_id": ("douyin_aweme_author_id",),
    }
    for field, aliases in author_key_map.items():
        if not any(normalize_text(author.get(alias)) for alias in aliases):
            _append(field)

    return missing


def _build_result(
    *,
    source_input: Dict[str, Optional[str]],
    platform_work_id: Optional[str],
    title: str,
    desc: str,
    duration_ms: Optional[int],
    video_down_url: Optional[str],
    author: Dict[str, Optional[str]],
    metrics: Dict[str, Optional[int]],
    tags: List[str],
    is_video: bool,
    video_type_reason: str,
    raw_content: str,
    confidence: str,
    error_reason: Optional[str],
    extract_trace: List[Dict[str, Any]],
    fallback_trace: List[Dict[str, Any]],
    request_id: Optional[str],
    u2_task_id: Optional[str],
    u2_task_status: str,
    u2_gate_reason: str,
    analysis_mode: str,
    create_time_sec: Optional[int] = None,
    cover_image: Optional[str] = None,
    asr_source: str = "fallback_none",
    timings: Optional[Dict[str, int]] = None,
    missing_fields: Optional[List[Dict[str, str]]] = None,
) -> Dict[str, Any]:
    summary_block = summarize_content(raw_content, source="douyin:single-video-low-quality")
    insights = list(summary_block.get("insights", []))
    insights.extend(
        [
            f"platform_work_id={platform_work_id or ''}",
            f"is_video={is_video}",
            f"video_type_reason={video_type_reason}",
            f"u2_gate_reason={u2_gate_reason}",
        ]
    )

    endpoint_list = [
        step.get("endpoint")
        for step in extract_trace
        if isinstance(step, dict) and isinstance(step.get("endpoint"), str)
    ]
    asr_clean = derive_asr_clean_text(raw_content)
    primary_text = asr_clean or raw_content
    analysis_eligibility = "eligible" if raw_content else "incomplete"
    analysis_exclusion_reason = "" if raw_content else "video_asr_unavailable"

    payload: Dict[str, Any] = {
        "platform": "douyin",
        "content_kind": "single_video",
        "analysis_mode": analysis_mode,
        "source": source_input,
        "platform_work_id": platform_work_id,
        "title": title,
        "caption_raw": desc,
        "desc": desc,
        "duration_ms": duration_ms,
        "create_time_sec": create_time_sec,
        "published_date": _format_published_date(create_time_sec),
        "cover_image": cover_image,
        "video_down_url": video_down_url,
        "video_download_url": video_down_url,
        "work_modality": "video",
        "author": author,
        "author_handle": author.get("author_handle"),
        "platform_author_id": author.get("platform_author_id") or author.get("author_platform_id"),
        "douyin_sec_uid": author.get("douyin_sec_uid"),
        "douyin_aweme_author_id": author.get("douyin_aweme_author_id"),
        "digg_count": metrics.get("digg_count", 0),
        "comment_count": metrics.get("comment_count", 0),
        "collect_count": metrics.get("collect_count", 0),
        "share_count": metrics.get("share_count", 0),
        "play_count": metrics.get("play_count"),
        "tags": tags or [],
        "is_video": is_video,
        "video_type_reason": video_type_reason,
        "u2_task_id": u2_task_id,
        "u2_task_status": u2_task_status,
        "raw_content": raw_content,
        "asr_raw": raw_content,
        "asr_clean": asr_clean,
        "primary_text": primary_text,
        "primary_text_source": "asr_clean",
        "analysis_eligibility": analysis_eligibility,
        "analysis_exclusion_reason": analysis_exclusion_reason,
        "asr_source": asr_source,
        "summary": summary_block.get("summary", ""),
        "insights": insights,
        "confidence": confidence,
        "error_reason": error_reason,
        "missing_fields": list(missing_fields or _build_missing_fields(
            title=title,
            desc=desc,
            platform_work_id=platform_work_id,
            video_down_url=video_down_url,
            author=author,
        )),
        "extract_trace": extract_trace,
        "fallback_trace": fallback_trace,
        "request_id": request_id,
        "endpoint_list": endpoint_list,
        "timings": dict(timings or {}),
    }
    return payload


def run_douyin_single_video(
    *,
    input_value: Optional[str],
    share_url: Optional[str],
    env_file: Optional[str],
    api_key_env: str,
    base_url: Optional[str],
    timeout_ms: Optional[int],
    app_timeout_ms: Optional[int],
    web_timeout_ms: Optional[int],
    poll_interval_sec: float,
    max_polls: int,
    u2_submit_max_retries: int,
    u2_submit_backoff_ms: int,
    write_card: bool,
    analysis_mode: str,
    card_type: str,
    card_root: Optional[str],
    content_kind: str = "single_video",
    storage_config: Optional[Dict[str, Any]] = None,
    allow_process_env: bool = False,
    persist_output: bool = True,
    progress: Optional[ProgressReporter] = None,
) -> Dict[str, Any]:
    workflow_started_at = time.perf_counter()
    timings = _empty_timings()
    parse_started_at = time.perf_counter()
    preflight = normalize_douyin_work_input(input_value, share_url)
    source_input = {"share_url": normalize_text(preflight.get("share_url")) or None}
    timings["url_parse_ms"] = _elapsed_ms(parse_started_at)
    if progress is not None:
        progress.started(
            stage="single_video.workflow",
            message="douyin single_video workflow started",
            data={"analysis_mode": analysis_mode, "write_card": bool(write_card), "persist_output": bool(persist_output)},
        )
    preflight_trace = [
        {
            "step": "input.preflight",
            "ok": preflight.get("error_reason") is None,
            "input_kind": "share_url",
            "normalized_share_url": source_input.get("share_url"),
            "error_reason": preflight.get("error_reason"),
            "missing_fields": list(preflight.get("missing_fields") or []),
        }
    ]
    if preflight.get("error_reason"):
        result = _build_result(
            source_input=source_input,
            platform_work_id=None,
            title="",
            desc="",
            duration_ms=None,
            video_down_url=None,
            author={"author_handle": None, "author_platform_id": None, "douyin_sec_uid": None, "douyin_aweme_author_id": None, "nickname": None, "signature": None},
            metrics=_empty_metrics(),
            tags=[],
            is_video=False,
            video_type_reason="invalid_input",
            raw_content="",
            confidence="low",
            error_reason=str(preflight.get("error_reason") or "invalid_share_url"),
            extract_trace=preflight_trace,
            fallback_trace=[],
            request_id=None,
            u2_task_id=None,
            u2_task_status="UNKNOWN",
            u2_gate_reason="invalid_input",
            analysis_mode=analysis_mode,
            timings=timings,
            missing_fields=list(preflight.get("missing_fields") or []),
        )
        if write_card:
            card_started_at = time.perf_counter()
            result["card_write"] = write_work_fact_card(
                payload=result,
                platform="douyin",
                card_type=card_type,
                card_root=card_root,
                content_kind=content_kind,
                storage_config=storage_config,
                analysis_mode=analysis_mode,
                progress=progress.child(scope="card_write") if progress is not None else None,
            )
            timings["card_write_ms"] = _elapsed_ms(card_started_at)
            timings["llm_analysis_ms"] = _safe_int((result.get("card_write") or {}).get("llm_analysis_ms"))
        timings["total_ms"] = _elapsed_ms(workflow_started_at)
        result["timings"] = dict(timings)
        _update_pipeline_status(result)
        return _finalize_result(
            result=result,
            source_input=source_input,
            platform_work_id=None,
            storage_config=storage_config,
            persist_output=persist_output,
        )
    if not source_input.get("share_url"):
        result = _build_result(
            source_input=source_input,
            platform_work_id=None,
            title="",
            desc="",
            duration_ms=None,
            video_down_url=None,
            author={"author_handle": None, "author_platform_id": None, "douyin_sec_uid": None, "douyin_aweme_author_id": None, "nickname": None, "signature": None},
            metrics=_empty_metrics(),
            tags=[],
            is_video=False,
            video_type_reason="missing_share_url",
            raw_content="",
            confidence="low",
            error_reason="missing_share_url",
            extract_trace=preflight_trace,
            fallback_trace=[],
            request_id=None,
            u2_task_id=None,
            u2_task_status="UNKNOWN",
            u2_gate_reason="not_started",
            analysis_mode=analysis_mode,
            timings=timings,
        )
        if write_card:
            card_started_at = time.perf_counter()
            result["card_write"] = write_work_fact_card(
                payload=result,
                platform="douyin",
                card_type=card_type,
                card_root=card_root,
                content_kind=content_kind,
                storage_config=storage_config,
                analysis_mode=analysis_mode,
                progress=progress.child(scope="card_write") if progress is not None else None,
            )
            timings["card_write_ms"] = _elapsed_ms(card_started_at)
            timings["llm_analysis_ms"] = _safe_int((result.get("card_write") or {}).get("llm_analysis_ms"))
        timings["total_ms"] = _elapsed_ms(workflow_started_at)
        result["timings"] = dict(timings)
        _update_pipeline_status(result)
        return _finalize_result(
            result=result,
            source_input=source_input,
            platform_work_id=None,
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

    app_timeout = int(app_timeout_ms or runtime["timeout_ms"])
    web_timeout = int(web_timeout_ms or runtime["timeout_ms"])

    trace: List[Dict[str, Any]] = []

    u1_started_at = time.perf_counter()
    if progress is not None:
        progress.progress(stage="single_video.fetch", message="fetching douyin single_video payload")
    one_video_response = _u1_fetch_one_video(
        base_url=runtime["base_url"],
        token=runtime["token"],
        share_url=source_input["share_url"] or "",
        app_timeout_ms=app_timeout,
        web_timeout_ms=web_timeout,
    )
    timings["u1_total_ms"] = _elapsed_ms(u1_started_at)

    app_failed = one_video_response.get("_app_failed")
    if app_failed:
        _emit_http_progress(progress, stage="single_video.fetch", response=app_failed, route_label="app_primary")
        trace.append(
            _trace_step(
                step="u1_fetch_one_video_primary",
                endpoint=APP_ENDPOINT,
                response=app_failed,
                extra={"timeout_ms": app_timeout},
            )
        )

    _emit_http_progress(
        progress,
        stage="single_video.fetch",
        response=one_video_response,
        route_label="effective_route",
    )
    trace.append(
        _trace_step(
            step="u1_fetch_one_video_effective",
            endpoint=one_video_response.get("_endpoint"),
            response=one_video_response,
            extra={
                "app_timeout_ms": app_timeout,
                "web_timeout_ms": web_timeout,
            },
        )
    )

    if not one_video_response.get("ok"):
        error_ctx = resolve_trace_error_context(
            responses=[one_video_response],
            extract_trace=trace,
            default_error_reason="u1_fetch_one_video_failed",
        )
        result = _build_result(
            source_input=source_input,
            platform_work_id=None,
            title="",
            desc="",
            duration_ms=None,
            video_down_url=None,
            author={"author_handle": None, "author_platform_id": None, "douyin_sec_uid": None, "douyin_aweme_author_id": None, "nickname": None, "signature": None},
            metrics=_empty_metrics(),
            tags=[],
            is_video=False,
            video_type_reason="u1_failed",
            raw_content="",
            confidence="low",
            error_reason=error_ctx.get("error_reason"),
            extract_trace=trace,
            fallback_trace=error_ctx.get("fallback_trace", []),
            request_id=error_ctx.get("request_id"),
            u2_task_id=None,
            u2_task_status="UNKNOWN",
            u2_gate_reason="u1_failed",
            analysis_mode=analysis_mode,
            timings=timings,
        )
        if write_card:
            card_started_at = time.perf_counter()
            result["card_write"] = write_work_fact_card(
                payload=result,
                platform="douyin",
                card_type=card_type,
                card_root=card_root,
                content_kind=content_kind,
                storage_config=storage_config,
                analysis_mode=analysis_mode,
                progress=progress.child(scope="card_write") if progress is not None else None,
            )
            timings["card_write_ms"] = _elapsed_ms(card_started_at)
            timings["llm_analysis_ms"] = _safe_int((result.get("card_write") or {}).get("llm_analysis_ms"))
        timings["total_ms"] = _elapsed_ms(workflow_started_at)
        result["timings"] = dict(timings)
        _update_pipeline_status(result)
        return _finalize_result(
            result=result,
            source_input=source_input,
            platform_work_id=None,
            storage_config=storage_config,
            persist_output=persist_output,
        )

    aweme_detail = _extract_aweme_detail(one_video_response.get("data"))
    if not aweme_detail:
        error_ctx = resolve_trace_error_context(
            responses=[one_video_response],
            extract_trace=trace,
            default_error_reason="aweme_detail_missing",
        )
        result = _build_result(
            source_input=source_input,
            platform_work_id=None,
            title="",
            desc="",
            duration_ms=None,
            video_down_url=None,
            author={"author_handle": None, "author_platform_id": None, "douyin_sec_uid": None, "douyin_aweme_author_id": None, "nickname": None, "signature": None},
            metrics=_empty_metrics(),
            tags=[],
            is_video=False,
            video_type_reason="aweme_detail_missing",
            raw_content="",
            confidence="low",
            error_reason=error_ctx.get("error_reason"),
            extract_trace=trace,
            fallback_trace=error_ctx.get("fallback_trace", []),
            request_id=error_ctx.get("request_id"),
            u2_task_id=None,
            u2_task_status="UNKNOWN",
            u2_gate_reason="aweme_detail_missing",
            analysis_mode=analysis_mode,
            timings=timings,
        )
        if write_card:
            card_started_at = time.perf_counter()
            result["card_write"] = write_work_fact_card(
                payload=result,
                platform="douyin",
                card_type=card_type,
                card_root=card_root,
                content_kind=content_kind,
                storage_config=storage_config,
                analysis_mode=analysis_mode,
                progress=progress.child(scope="card_write") if progress is not None else None,
            )
            timings["card_write_ms"] = _elapsed_ms(card_started_at)
            timings["llm_analysis_ms"] = _safe_int((result.get("card_write") or {}).get("llm_analysis_ms"))
        timings["total_ms"] = _elapsed_ms(workflow_started_at)
        result["timings"] = dict(timings)
        _update_pipeline_status(result)
        return _finalize_result(
            result=result,
            source_input=source_input,
            platform_work_id=None,
            storage_config=storage_config,
            persist_output=persist_output,
        )

    video_type_info = normalize_douyin_video_type(aweme_detail)
    duration_ms = _normalize_duration_ms(aweme_detail)
    platform_work_id = _extract_platform_work_id(aweme_detail)
    title = _pick_title(aweme_detail)
    desc = _pick_desc(aweme_detail)
    author = _extract_author(aweme_detail)
    metrics = _extract_metrics(aweme_detail)
    tags = _extract_douyin_tags(aweme_detail)
    create_time_sec = _extract_create_time_sec(aweme_detail)
    cover_image = _extract_cover_image(aweme_detail)

    video_obj = aweme_detail.get("video") if isinstance(aweme_detail.get("video"), dict) else {}
    down_url_selection = select_low_quality_video_url(video_obj)
    video_down_url = down_url_selection.get("video_down_url")

    trace.append(
        {
            "step": "video_type_normalization",
            "is_video": video_type_info.get("is_video"),
            "video_type_reason": video_type_info.get("video_type_reason"),
            "matched_field": video_type_info.get("matched_field"),
            "duration_ms": duration_ms,
        }
    )

    trace.append(
        {
            "step": "select_low_quality_video_url",
            "selection_reason": down_url_selection.get("selection_reason"),
            "selected_from": down_url_selection.get("selected_from"),
            "video_down_url": video_down_url,
            "min_bit_rate": down_url_selection.get("min_bit_rate"),
            "download_url_count": down_url_selection.get("download_url_count"),
            "bit_rate_count": down_url_selection.get("bit_rate_count"),
        }
    )

    can_u2 = bool(video_type_info.get("is_video")) and bool(duration_ms and duration_ms > 13000 and duration_ms <= 1800000)
    can_u2 = can_u2 and bool(video_down_url)

    if not video_type_info.get("is_video"):
        gate_reason = "skip:not_video"
    elif not duration_ms:
        gate_reason = "skip:duration_missing"
    elif duration_ms <= 13000:
        gate_reason = "skip:duration_too_short"
    elif duration_ms > 1800000:
        gate_reason = "skip:duration_too_long"
    elif not video_down_url:
        gate_reason = "skip:video_down_url_missing"
    else:
        gate_reason = "pass"

    trace.append(
        {
            "step": "u2_gate",
            "can_u2": can_u2,
            "gate_reason": gate_reason,
            "rule": "is_video && 13000<duration_ms<=1800000 && video_down_url_present",
            "is_video": bool(video_type_info.get("is_video")),
            "video_type_reason": video_type_info.get("video_type_reason"),
            "duration_ms": duration_ms,
            "video_down_url_present": bool(video_down_url),
        }
    )

    raw_content = ""
    error_reason: Optional[str] = None
    u2_task_id: Optional[str] = None
    u2_task_status = "SKIPPED"
    submit_response: Dict[str, Any] = {}
    poll_result: Dict[str, Any] = {}

    if can_u2 and video_down_url:
        u2_timeout_ms = _resolve_u2_timeout_ms(runtime["timeout_ms"])
        if progress is not None:
            progress.progress(
                stage="single_video.u2",
                message="starting douyin u2 submit",
                data={"video_down_url_present": True, "timeout_ms": u2_timeout_ms},
            )
        submit_started_at = time.perf_counter()
        submit_bundle = run_u2_asr_with_timeout_retry(
            base_url=runtime["base_url"],
            token=runtime["token"],
            timeout_ms=u2_timeout_ms,
            video_url=video_down_url,
            submit_max_retries=u2_submit_max_retries,
            submit_backoff_ms=u2_submit_backoff_ms,
            poll_interval_sec=poll_interval_sec,
            max_polls=max_polls,
            pending_timeout_sec=int(config_get(storage_config or {}, "runtime.u2_pending_timeout_sec", 60) or 60),
            progress_callback=(
                lambda event: _report_u2_progress(progress, stage="single_video.u2", event=event, label="douyin")
            ) if progress is not None else None,
        )
        timings["u2_submit_ms"] = _safe_int(submit_bundle.get("submit_duration_ms")) or _elapsed_ms(submit_started_at)
        submit_response = (submit_bundle.get("submit_bundle") or {}).get("submit_response", {})
        u2_task_id = (submit_bundle.get("submit_bundle") or {}).get("task_id")
        if progress is not None:
            progress.http_event(
                stage="single_video.u2",
                endpoint=U2_SUBMIT_ENDPOINT,
                response=submit_response,
                route_label="u2_submit",
                summary={
                    "task_id": u2_task_id,
                    "final_submit_status": (submit_bundle.get("submit_bundle") or {}).get("final_submit_status"),
                    "retry_count": len(((submit_bundle.get("submit_bundle") or {}).get("retry_chain") or [])),
                },
            )

        trace.append(
            _trace_step(
                step="u2_submit_transcription",
                endpoint=U2_SUBMIT_ENDPOINT,
                response=submit_response,
                extra={
                    "task_id": u2_task_id,
                    "video_down_url": video_down_url,
                    "final_submit_status": (submit_bundle.get("submit_bundle") or {}).get("final_submit_status"),
                },
            )
        )

        trace.append(
            {
                "step": "u2_submit_retry_chain",
                "final_submit_status": submit_bundle.get("final_submit_status"),
                "retries_config": {
                    "u2_submit_max_retries": max(0, int(u2_submit_max_retries)),
                    "u2_submit_backoff_ms": max(0, int(u2_submit_backoff_ms)),
                },
                "attempts": ((submit_bundle.get("submit_bundle") or {}).get("retry_chain") or []),
            }
        )

        if not submit_response.get("ok") or not u2_task_id:
            if progress is not None:
                progress.failed(
                    stage="single_video.u2",
                    message="douyin u2 submit failed",
                    data={"error_reason": submit_response.get("error_reason") or "u2_submit_failed_or_missing_task_id"},
                )
            error_reason = submit_response.get("error_reason") or "u2_submit_failed_or_missing_task_id"
            u2_task_status = "UNKNOWN"
        else:
            poll_result = submit_bundle.get("poll_result", {})
            timings["u2_poll_ms"] = _safe_int(submit_bundle.get("poll_duration_ms"))
            u2_task_status = poll_result.get("task_status") or "UNKNOWN"
            raw_content = poll_result.get("transcript_text", "") if poll_result.get("ok") else ""
            error_reason = poll_result.get("error_reason")

            trace.append(
                {
                    "step": "u2_poll_task",
                    "endpoint": "/api/u2/v1/tasks/{task_id}",
                    "task_id": u2_task_id,
                    "ok": poll_result.get("ok"),
                    "task_status": u2_task_status,
                    "request_id": poll_result.get("request_id"),
                    "error_reason": poll_result.get("error_reason"),
                    "attempts": len(poll_result.get("trace", [])),
                    "timeout_retry": submit_bundle.get("timeout_retry", {}),
                    "u3_fallback": submit_bundle.get("u3_fallback", {}),
                }
            )
            if submit_bundle.get("u3_fallback", {}).get("triggered"):
                trace.append(
                    {
                        "step": "u3_fallback",
                        "triggered": True,
                        "ok": submit_bundle.get("u3_fallback", {}).get("ok"),
                        "result": submit_bundle.get("u3_fallback", {}).get("result"),
                        "public_url": submit_bundle.get("u3_fallback", {}).get("public_url"),
                        "error_reason": submit_bundle.get("u3_fallback", {}).get("error_reason"),
                        "trace": submit_bundle.get("u3_fallback", {}).get("trace", []),
                    }
                )
            if progress is not None:
                (progress.done if poll_result.get("ok") else progress.failed)(
                    stage="single_video.u2",
                    message="douyin u2 polling finished" if poll_result.get("ok") else "douyin u2 polling failed",
                    data={"task_id": u2_task_id, "task_status": u2_task_status, "attempts": len(poll_result.get("trace", []))},
                )

    error_ctx = resolve_trace_error_context(
        responses=[poll_result, submit_response, one_video_response],
        extract_trace=trace,
        explicit_error_reason=error_reason,
        explicit_request_id=poll_result.get("request_id") or submit_response.get("request_id") or one_video_response.get("request_id"),
    )
    error_reason = error_ctx.get("error_reason")

    if error_reason:
        confidence = "low"
    elif can_u2 and raw_content:
        confidence = "high"
    elif can_u2 and not raw_content:
        confidence = "medium"
    else:
        confidence = "medium"

    result = _build_result(
        source_input=source_input,
        platform_work_id=platform_work_id,
        title=title,
        desc=desc,
        duration_ms=duration_ms,
        create_time_sec=create_time_sec,
        cover_image=cover_image,
        video_down_url=video_down_url,
        author=author,
        metrics=metrics,
        tags=tags,
        is_video=bool(video_type_info.get("is_video")),
        video_type_reason=str(video_type_info.get("video_type_reason") or ""),
        raw_content=raw_content,
        confidence=confidence,
        error_reason=error_reason,
        extract_trace=trace,
        fallback_trace=error_ctx.get("fallback_trace", []),
        request_id=error_ctx.get("request_id"),
        u2_task_id=u2_task_id,
        u2_task_status=u2_task_status,
        u2_gate_reason=gate_reason,
        analysis_mode=analysis_mode,
        asr_source="u2" if raw_content else "fallback_none",
        timings=timings,
    )

    if write_card:
        if progress is not None:
            progress.progress(stage="single_video.card_write", message="writing douyin single_video card")
        card_started_at = time.perf_counter()
        result["card_write"] = write_work_fact_card(
            payload=result,
            platform="douyin",
            card_type=card_type,
            card_root=card_root,
            content_kind=content_kind,
            storage_config=storage_config,
            analysis_mode=analysis_mode,
            progress=progress.child(scope="card_write") if progress is not None else None,
        )
        timings["card_write_ms"] = _elapsed_ms(card_started_at)
        timings["llm_analysis_ms"] = _safe_int((result.get("card_write") or {}).get("llm_analysis_ms"))

    timings["total_ms"] = _elapsed_ms(workflow_started_at)
    result["timings"] = dict(timings)
    _update_pipeline_status(result)

    finalized = _finalize_result(
        result=result,
        source_input=source_input,
        platform_work_id=platform_work_id,
        storage_config=storage_config,
        persist_output=persist_output,
    )
    if progress is not None:
        final_event = progress.failed if finalized.get("error_reason") else progress.done
        final_event(
            stage="single_video.workflow",
            message="douyin single_video workflow finished" if not finalized.get("error_reason") else "douyin single_video workflow failed",
            data={
                "request_id": finalized.get("request_id"),
                "card_write_ok": bool((finalized.get("card_write") or {}).get("ok")),
                "output_persist_ok": bool((finalized.get("output_persist") or {}).get("ok")),
                "deep_analysis_status": ((finalized.get("deep_analysis") or {}).get("status")),
            },
        )
    return finalized


def main() -> None:
    parser = argparse.ArgumentParser(description="Run Douyin single-work fixed pipeline")
    parser.add_argument("input", nargs="?", default=None, help="Douyin share URL")
    parser.add_argument("--share-url", default=None, help="Douyin share URL")
    parser.add_argument("--config", default=None, help="Runtime config YAML path")
    parser.add_argument("--env-file", default=None, help="Optional env file path")
    parser.add_argument("--allow-process-env", action="store_true", help="Allow process env to override .env/.env.local")
    parser.add_argument("--api-key-env", default=None, help="API key env variable name")
    parser.add_argument("--base-url", default=None, help="Tikomni base URL")
    parser.add_argument("--timeout-ms", type=int, default=None, help="Global timeout ms")
    parser.add_argument("--app-timeout-ms", type=int, default=None, help="APP endpoint timeout ms (optional)")
    parser.add_argument("--web-timeout-ms", type=int, default=None, help="WEB endpoint timeout ms (optional)")
    parser.add_argument("--poll-interval-sec", type=float, default=3.0, help="U2 poll interval seconds")
    parser.add_argument("--max-polls", type=int, default=30, help="Max U2 polls")
    parser.add_argument(
        "--u2-submit-max-retries",
        type=int,
        default=2,
        help="Max retries for retriable U2 submit failures",
    )
    parser.add_argument(
        "--u2-submit-backoff-ms",
        type=int,
        default=1500,
        help="Base backoff ms for retriable U2 submit failures (exponential)",
    )
    parser.add_argument("--card-type", choices=["work"], default="work", help="Primary card type")
    parser.add_argument("--content-kind", default="single_video", help="Routing kind, e.g. single_video/work")
    parser.add_argument("--card-mode", dest="analysis_mode", choices=["standard", "auto", "local"], default="standard", help="Fact-card mode")
    parser.add_argument("--analysis-mode", dest="analysis_mode", choices=["standard", "auto", "local"], help=argparse.SUPPRESS)
    parser.set_defaults(write_card=True, persist_output=True)
    parser.add_argument("--write-card", dest="write_card", action="store_true", help="Write final work card")
    parser.add_argument("--no-write-card", dest="write_card", action="store_false", help="Skip card writing")
    parser.add_argument("--persist-output", dest="persist_output", action="store_true", help="Persist result JSON")
    parser.add_argument("--no-persist-output", dest="persist_output", action="store_false", help="Skip result JSON persist")
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

    progress = build_progress_reporter(
        workflow="social-media-crawl",
        platform="douyin",
        content_kind=args.content_kind,
        input_value=args.share_url or args.input,
    )

    try:
        result = run_douyin_single_video(
            input_value=args.input,
            share_url=args.share_url,
            env_file=resolved_env_file,
            api_key_env=api_key_env,
            base_url=base_url,
            timeout_ms=timeout_ms,
            app_timeout_ms=args.app_timeout_ms,
            web_timeout_ms=args.web_timeout_ms,
            poll_interval_sec=args.poll_interval_sec,
            max_polls=args.max_polls,
            u2_submit_max_retries=args.u2_submit_max_retries,
            u2_submit_backoff_ms=args.u2_submit_backoff_ms,
            write_card=bool(args.write_card),
            analysis_mode=args.analysis_mode,
            card_type=args.card_type,
            card_root=args.card_root,
            content_kind=args.content_kind,
            storage_config=config,
            allow_process_env=args.allow_process_env,
            persist_output=bool(args.persist_output),
            progress=progress,
        )
    except ValueError as error:
        result = {
            "platform": "douyin",
            "raw_content": "",
            "summary": "",
            "insights": ["source=douyin:single-video-low-quality", "runtime_not_ready"],
            "confidence": "low",
            "error_reason": str(error),
            "missing_fields": [],
            "extract_trace": [],
            "fallback_trace": [],
            "request_id": None,
            "endpoint_list": [],
        }

    write_json_stdout(result)
    raise SystemExit(0 if not result.get("error_reason") else 1)


if __name__ == "__main__":
    main()
