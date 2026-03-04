#!/usr/bin/env python3
"""Douyin single-video low-quality runner (APP first, WEB fallback)."""

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
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

from scripts.core.config_loader import config_get, load_tikomni_config, resolve_storage_paths
from scripts.core.extract_pipeline import resolve_trace_error_context
from scripts.platform.douyin.douyin_video_type_matrix import normalize_douyin_video_type
from scripts.pipeline.asr.asr_pipeline import submit_u2_asr_with_retry
from scripts.pipeline.asr.poll_u2_task import poll_u2_task
from scripts.platform.douyin.select_low_quality_video_url import select_low_quality_video_url
from scripts.core.tikomni_common import (
    call_json_api,
    normalize_text,
    resolve_runtime,
    summarize_content,
    write_json_stdout,
)
from scripts.writers.write_benchmark_card import write_benchmark_card

APP_ENDPOINT = "/api/u1/v1/douyin/app/v3/fetch_one_video_by_share_url"
WEB_ENDPOINT = "/api/u1/v1/douyin/web/fetch_one_video_by_share_url"
U2_SUBMIT_ENDPOINT = "/api/u2/v1/services/audio/asr/transcription"




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


def _build_persist_payload(
    *,
    result: Dict[str, Any],
    source_input: Dict[str, Optional[str]],
    platform_work_id: Optional[str],
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
        "platform": result.get("platform", "douyin"),
        "content_kind": result.get("content_kind", "single_video"),
        "platform_work_id": result.get("platform_work_id"),
        "title": result.get("title"),
        "duration_ms": result.get("duration_ms"),
        "is_video": result.get("is_video"),
        "u2_task_id": result.get("u2_task_id"),
        "u2_task_status": result.get("u2_task_status"),
        "request_id": result.get("request_id"),
        "source": source_input,
    }
    return {
        "meta": {
            "written_at": written_at.isoformat(timespec="seconds"),
            "status": status,
            "platform": "douyin",
            "identifier": _traceable_identifier(source_input, platform_work_id),
        },
        "summary": summary,
        "normalized": normalized,
        "raw": result,
    }


def _persist_output_artifact(
    *,
    result: Dict[str, Any],
    source_input: Dict[str, Optional[str]],
    platform_work_id: Optional[str],
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
    identifier = _traceable_identifier(source_input, platform_work_id)
    has_error = bool(result.get("error_reason"))
    status = "error" if has_error else "success"

    if has_error:
        target_dir = Path(paths.get("errors_dir", "")) / date_key
    else:
        target_dir = Path(paths.get("runs_dir", "")) / str(paths.get("results_dir", "results")) / date_key

    target_dir.mkdir(parents=True, exist_ok=True)
    file_path = target_dir / f"{timestamp}-douyin-{identifier}.json"

    payload = _build_persist_payload(
        result=result,
        source_input=source_input,
        platform_work_id=platform_work_id,
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
    platform_work_id: Optional[str],
    storage_config: Optional[Dict[str, Any]],
    persist_output: bool,
) -> Dict[str, Any]:
    result["output_persist"] = _persist_output_artifact(
        result=result,
        source_input=source_input,
        platform_work_id=platform_work_id,
        storage_config=storage_config,
        persist_output=persist_output,
    )
    return result

def _normalize_input(
    input_value: Optional[str],
    share_url: Optional[str],
) -> Dict[str, Optional[str]]:
    normalized_share = (share_url or "").strip() or None

    if input_value and not normalized_share:
        candidate = input_value.strip()
        if candidate.startswith("http://") or candidate.startswith("https://"):
            normalized_share = candidate

    return {"share_url": normalized_share}


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
    for key in ("item_title", "title", "desc", "preview_title"):
        value = item.get(key)
        text = normalize_text(value)
        if text:
            return text
    return ""


def _pick_desc(item: Dict[str, Any]) -> str:
    for key in ("desc", "item_title", "title", "preview_title"):
        value = item.get(key)
        text = normalize_text(value)
        if text:
            return text
    return ""


def _extract_author(item: Dict[str, Any]) -> Dict[str, Optional[str]]:
    author = item.get("author")
    if not isinstance(author, dict):
        author = {}

    return {
        "sec_uid": normalize_text(author.get("sec_uid")) or None,
        "unique_id": normalize_text(author.get("unique_id")) or None,
        "nickname": normalize_text(author.get("nickname")) or None,
        "signature": normalize_text(author.get("signature")) or None,
    }


def _extract_metrics(item: Dict[str, Any]) -> Dict[str, int]:
    statistics = item.get("statistics")
    if not isinstance(statistics, dict):
        statistics = {}

    def metric(*keys: str) -> int:
        for key in keys:
            value = _safe_int(statistics.get(key))
            if value is not None:
                return value
            value = _safe_int(item.get(key))
            if value is not None:
                return value
        return 0

    return {
        "digg_count": metric("digg_count"),
        "comment_count": metric("comment_count"),
        "collect_count": metric("collect_count"),
        "share_count": metric("share_count", "forward_count"),
        "play_count": metric("play_count"),
    }


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
            }
        )
    if extra:
        payload.update(extra)
    return payload


def _build_result(
    *,
    source_input: Dict[str, Optional[str]],
    platform_work_id: Optional[str],
    title: str,
    desc: str,
    duration_ms: Optional[int],
    video_down_url: Optional[str],
    author: Dict[str, Optional[str]],
    metrics: Dict[str, int],
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
    create_time_sec: Optional[int] = None,
    cover_image: Optional[str] = None,
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

    payload: Dict[str, Any] = {
        "platform": "douyin",
        "content_kind": "single_video",
        "source": source_input,
        "platform_work_id": platform_work_id,
        "title": title,
        "desc": desc,
        "duration_ms": duration_ms,
        "create_time_sec": create_time_sec,
        "cover_image": cover_image,
        "video_down_url": video_down_url,
        "author": author,
        "digg_count": metrics.get("digg_count", 0),
        "comment_count": metrics.get("comment_count", 0),
        "collect_count": metrics.get("collect_count", 0),
        "share_count": metrics.get("share_count", 0),
        "play_count": metrics.get("play_count", 0),
        "is_video": is_video,
        "video_type_reason": video_type_reason,
        "u2_task_id": u2_task_id,
        "u2_task_status": u2_task_status,
        "raw_content": raw_content,
        "summary": summary_block.get("summary", ""),
        "insights": insights,
        "confidence": confidence,
        "error_reason": error_reason,
        "missing_fields": [],
        "extract_trace": extract_trace,
        "fallback_trace": fallback_trace,
        "request_id": request_id,
        "endpoint_list": endpoint_list,
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
    card_type: str,
    collect_material: bool,
    card_root: Optional[str],
    content_kind: str = "single_video",
    storage_config: Optional[Dict[str, Any]] = None,
    allow_process_env: bool = False,
    persist_output: bool = True,
) -> Dict[str, Any]:
    source_input = _normalize_input(input_value, share_url)
    if not source_input.get("share_url"):
        result = _build_result(
            source_input=source_input,
            platform_work_id=None,
            title="",
            desc="",
            duration_ms=None,
            video_down_url=None,
            author={"sec_uid": None, "unique_id": None, "nickname": None, "signature": None},
            metrics={
                "digg_count": 0,
                "comment_count": 0,
                "collect_count": 0,
                "share_count": 0,
                "play_count": 0,
            },
            is_video=False,
            video_type_reason="missing_share_url",
            raw_content="",
            confidence="low",
            error_reason="missing_share_url",
            extract_trace=[],
            fallback_trace=[],
            request_id=None,
            u2_task_id=None,
            u2_task_status="UNKNOWN",
            u2_gate_reason="not_started",
        )
        if write_card:
            result["card_write"] = write_benchmark_card(
                payload=result,
                platform="douyin",
                card_type=card_type,
                card_root=card_root,
                collect_material=collect_material,
                content_kind=content_kind,
                storage_config=storage_config,
            )
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

    one_video_response = _u1_fetch_one_video(
        base_url=runtime["base_url"],
        token=runtime["token"],
        share_url=source_input["share_url"] or "",
        app_timeout_ms=app_timeout,
        web_timeout_ms=web_timeout,
    )

    app_failed = one_video_response.get("_app_failed")
    if app_failed:
        trace.append(
            _trace_step(
                step="u1_fetch_one_video_primary",
                endpoint=APP_ENDPOINT,
                response=app_failed,
                extra={"timeout_ms": app_timeout},
            )
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
            author={"sec_uid": None, "unique_id": None, "nickname": None, "signature": None},
            metrics={
                "digg_count": 0,
                "comment_count": 0,
                "collect_count": 0,
                "share_count": 0,
                "play_count": 0,
            },
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
        )
        if write_card:
            result["card_write"] = write_benchmark_card(
                payload=result,
                platform="douyin",
                card_type=card_type,
                card_root=card_root,
                collect_material=collect_material,
                content_kind=content_kind,
                storage_config=storage_config,
            )
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
            author={"sec_uid": None, "unique_id": None, "nickname": None, "signature": None},
            metrics={
                "digg_count": 0,
                "comment_count": 0,
                "collect_count": 0,
                "share_count": 0,
                "play_count": 0,
            },
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
        )
        if write_card:
            result["card_write"] = write_benchmark_card(
                payload=result,
                platform="douyin",
                card_type=card_type,
                card_root=card_root,
                collect_material=collect_material,
                content_kind=content_kind,
                storage_config=storage_config,
            )
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
        gate_reason = f"skip:not_video({video_type_info.get('video_type_reason')})"
    elif not duration_ms:
        gate_reason = "skip:duration_missing"
    elif duration_ms <= 13000:
        gate_reason = f"skip:duration_too_short({duration_ms})"
    elif duration_ms > 1800000:
        gate_reason = f"skip:duration_too_long({duration_ms})"
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
        }
    )

    raw_content = ""
    error_reason: Optional[str] = None
    u2_task_id: Optional[str] = None
    u2_task_status = "SKIPPED"
    submit_response: Dict[str, Any] = {}
    poll_result: Dict[str, Any] = {}

    if can_u2 and video_down_url:
        submit_bundle = submit_u2_asr_with_retry(
            base_url=runtime["base_url"],
            token=runtime["token"],
            timeout_ms=runtime["timeout_ms"],
            video_url=video_down_url,
            max_retries=u2_submit_max_retries,
            backoff_ms=u2_submit_backoff_ms,
        )
        submit_response = submit_bundle["submit_response"]
        u2_task_id = submit_bundle.get("task_id")

        trace.append(
            _trace_step(
                step="u2_submit_transcription",
                endpoint=U2_SUBMIT_ENDPOINT,
                response=submit_response,
                extra={
                    "task_id": u2_task_id,
                    "video_down_url": video_down_url,
                    "final_submit_status": submit_bundle.get("final_submit_status"),
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
                "attempts": submit_bundle.get("retry_chain", []),
            }
        )

        if not submit_response.get("ok") or not u2_task_id:
            error_reason = submit_response.get("error_reason") or "u2_submit_failed_or_missing_task_id"
            u2_task_status = "UNKNOWN"
        else:
            poll_result = poll_u2_task(
                base_url=runtime["base_url"],
                token=runtime["token"],
                timeout_ms=runtime["timeout_ms"],
                task_id=u2_task_id,
                poll_interval_sec=poll_interval_sec,
                max_polls=max_polls,
            )
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
                }
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
    )

    if write_card:
        result["card_write"] = write_benchmark_card(
            payload=result,
            platform="douyin",
            card_type=card_type,
            card_root=card_root,
            collect_material=collect_material,
            content_kind=content_kind,
            storage_config=storage_config,
        )

    return _finalize_result(
        result=result,
        source_input=source_input,
        platform_work_id=platform_work_id,
        storage_config=storage_config,
        persist_output=persist_output,
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Run Douyin single-video low-quality extraction")
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
    parser.add_argument("--write-card", dest="write_card", action="store_true", help="Write benchmark card to card root (default on)")
    parser.add_argument("--no-write-card", dest="write_card", action="store_false", help="Disable benchmark card writing")
    parser.set_defaults(write_card=True)
    parser.add_argument("--card-type", choices=["work", "author", "author_sample_work"], default="work", help="Primary card type")
    parser.add_argument("--content-kind", default="single_video", help="Routing kind, e.g. single_video/author_home/author_analysis")
    parser.add_argument("--collect-material", action="store_true", help="Write extra CMAT card")
    parser.add_argument("--card-root", default=None, help="Card root (absolute); falls back to TIKOMNI_CARD_ROOT when writing cards")
    parser.add_argument("--persist-output", dest="persist_output", action="store_true", help="Persist JSON artifact to TIKOMNI_OUTPUT_ROOT (default on)")
    parser.add_argument("--no-persist-output", dest="persist_output", action="store_false", help="Disable output artifact persistence")
    parser.set_defaults(persist_output=True)
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
            write_card=args.write_card,
            card_type=args.card_type,
            collect_material=args.collect_material,
            card_root=args.card_root,
            content_kind=args.content_kind,
            storage_config=config,
            allow_process_env=args.allow_process_env,
            persist_output=args.persist_output,
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
