#!/usr/bin/env python3
"""Xiaohongshu extraction: subtitle-first, fallback to U2."""

import argparse
import json
import re
import urllib.request
from typing import Any, Dict, List, Optional

from asr_pipeline import submit_u2_asr
from config_loader import config_get, load_tikomni_config
from extract_pipeline import build_api_trace, request_with_optional_fallback
from poll_u2_task import poll_u2_task
from tikomni_common import (
    deep_find_all,
    deep_find_first,
    extract_task_id,
    normalize_text,
    resolve_runtime,
    summarize_content,
    write_json_stdout,
)
from write_benchmark_card import DEFAULT_WIKI_ROOT, write_benchmark_card


def _normalize_input(input_value: Optional[str], share_text: Optional[str], note_id: Optional[str]) -> Dict[str, Optional[str]]:
    normalized_share = share_text
    normalized_note_id = note_id

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


def _build_result(
    *,
    source_input: Dict[str, Optional[str]],
    raw_content: str,
    confidence: str,
    error_reason: Optional[str],
    extract_trace: List[Dict[str, Any]],
    request_id: Optional[str],
    text_source: str,
    note_id: Optional[str],
    subtitle_hit: bool,
    u2_task_id: Optional[str],
    u2_task_status: Optional[str],
) -> Dict[str, Any]:
    summary_block = summarize_content(raw_content, source=f"xiaohongshu:{text_source}")
    return {
        "platform": "xiaohongshu",
        "source": source_input,
        "note_id": note_id,
        "subtitle_hit": subtitle_hit,
        "text_source": text_source,
        "u2_task_id": u2_task_id,
        "u2_task_status": u2_task_status,
        "raw_content": raw_content,
        "summary": summary_block["summary"],
        "insights": summary_block["insights"],
        "confidence": confidence,
        "error_reason": error_reason,
        "extract_trace": extract_trace,
        "request_id": request_id,
    }


def _fetch_note_info(*, base_url: str, token: str, timeout_ms: int, source_input: Dict[str, Optional[str]]) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if source_input.get("share_text"):
        params["share_text"] = source_input["share_text"]
    if source_input.get("note_id"):
        params["note_id"] = source_input["note_id"]

    # Prefer v7 (best coverage in current catalog), fallback to app V1.
    return request_with_optional_fallback(
        base_url=base_url,
        token=token,
        timeout_ms=timeout_ms,
        method="GET",
        params=params,
        primary_path="/api/u1/v1/xiaohongshu/web/get_note_info_v7",
        fallback_path="/api/u1/v1/xiaohongshu/app/get_note_info",
    )


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

    # JSON subtitle payload
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

    # VTT/SRT style
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


def _extract_video_candidates(payload: Any) -> List[str]:
    candidates: List[str] = []
    key_priority = [
        "original_video_url",
        "video_url",
        "play_url",
        "master_url",
        "masterUrl",
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

    # Keep URLs that look like media first.
    media = [u for u in candidates if any(x in u.lower() for x in [".mp4", "video", "play", "stream"])]
    ordered = media + candidates

    unique: List[str] = []
    seen = set()
    for url in ordered:
        if url not in seen:
            unique.append(url)
            seen.add(url)
    return unique


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
    idempotency_key: Optional[str],
    force_u2_fallback: bool,
    write_card: bool,
    card_type: str,
    collect_material: bool,
    wiki_root: str,
) -> Dict[str, Any]:
    source_input = _normalize_input(input_value, share_text, note_id)
    if not source_input["share_text"] and not source_input["note_id"]:
        return _build_result(
            source_input=source_input,
            raw_content="",
            confidence="low",
            error_reason="missing_share_text_or_note_id",
            extract_trace=[],
            request_id=None,
            text_source="none",
            note_id=None,
            subtitle_hit=False,
            u2_task_id=None,
            u2_task_status="UNKNOWN",
        )

    runtime = resolve_runtime(
        env_file=env_file,
        api_key_env=api_key_env,
        base_url=base_url,
        timeout_ms=timeout_ms,
    )

    trace: List[Dict[str, Any]] = []

    note_response = _fetch_note_info(
        base_url=runtime["base_url"],
        token=runtime["token"],
        timeout_ms=runtime["timeout_ms"],
        source_input=source_input,
    )
    primary_failed = note_response.get("_primary_failed")
    if primary_failed:
        trace.append(
            build_api_trace(
                step="u1_get_note_info_primary",
                endpoint="/api/u1/v1/xiaohongshu/web/get_note_info_v7",
                response=primary_failed,
            )
        )

    trace.append(
        build_api_trace(
            step="u1_get_note_info_effective",
            endpoint=note_response.get("_endpoint"),
            response=note_response,
        )
    )

    if not note_response["ok"]:
        result = _build_result(
            source_input=source_input,
            raw_content="",
            confidence="low",
            error_reason=note_response.get("error_reason") or "u1_get_note_info_failed",
            extract_trace=trace,
            request_id=note_response.get("request_id"),
            text_source="none",
            note_id=source_input.get("note_id"),
            subtitle_hit=False,
            u2_task_id=None,
            u2_task_status="UNKNOWN",
        )
        if write_card:
            result["card_write"] = write_benchmark_card(
                payload=result,
                platform="xiaohongshu",
                card_type=card_type,
                wiki_root=wiki_root,
                collect_material=collect_material,
            )
        return result

    resolved_note_id = deep_find_first(note_response["data"], ["note_id", "id"])

    subtitle_inline_text = "" if force_u2_fallback else _extract_subtitle_inline_text(note_response["data"])
    subtitle_urls = [] if force_u2_fallback else _extract_subtitle_urls(note_response["data"])
    subtitle_url_text = "" if force_u2_fallback else _fetch_subtitle_text(subtitle_urls, runtime["timeout_ms"])

    subtitle_text = subtitle_inline_text or subtitle_url_text
    trace.append(
        {
            "step": "subtitle_probe",
            "subtitle_hit": bool(subtitle_text),
            "subtitle_url_count": len(subtitle_urls),
            "force_u2_fallback": force_u2_fallback,
        }
    )

    if subtitle_text:
        result = _build_result(
            source_input=source_input,
            raw_content=subtitle_text,
            confidence="high",
            error_reason=None,
            extract_trace=trace,
            request_id=note_response.get("request_id"),
            text_source="subtitle",
            note_id=str(resolved_note_id) if resolved_note_id else source_input.get("note_id"),
            subtitle_hit=True,
            u2_task_id=None,
            u2_task_status="SKIPPED",
        )
        if write_card:
            result["card_write"] = write_benchmark_card(
                payload=result,
                platform="xiaohongshu",
                card_type=card_type,
                wiki_root=wiki_root,
                collect_material=collect_material,
            )
        return result

    video_candidates = _extract_video_candidates(note_response["data"])
    selected_video_url = video_candidates[0] if video_candidates else None

    if not selected_video_url:
        result = _build_result(
            source_input=source_input,
            raw_content="",
            confidence="low",
            error_reason="subtitle_missing_and_no_video_url_for_u2",
            extract_trace=trace,
            request_id=note_response.get("request_id"),
            text_source="none",
            note_id=str(resolved_note_id) if resolved_note_id else source_input.get("note_id"),
            subtitle_hit=False,
            u2_task_id=None,
            u2_task_status="UNKNOWN",
        )
        if write_card:
            result["card_write"] = write_benchmark_card(
                payload=result,
                platform="xiaohongshu",
                card_type=card_type,
                wiki_root=wiki_root,
                collect_material=collect_material,
            )
        return result

    submit_response = submit_u2_asr(
        base_url=runtime["base_url"],
        token=runtime["token"],
        timeout_ms=runtime["timeout_ms"],
        video_url=selected_video_url,
        idempotency_key=idempotency_key,
    )
    task_id = extract_task_id(submit_response["data"])

    trace.append(
        build_api_trace(
            step="u2_submit_transcription",
            endpoint="/api/u2/v1/services/audio/asr/transcription",
            response=submit_response,
            extra={
                "task_id": task_id,
                "selected_video_url": selected_video_url,
                "idempotency_key_sent": bool(idempotency_key),
            },
        )
    )

    if not submit_response["ok"] or not task_id:
        result = _build_result(
            source_input=source_input,
            raw_content="",
            confidence="low",
            error_reason=submit_response.get("error_reason") or "u2_submit_failed_or_missing_task_id",
            extract_trace=trace,
            request_id=submit_response.get("request_id") or note_response.get("request_id"),
            text_source="u2",
            note_id=str(resolved_note_id) if resolved_note_id else source_input.get("note_id"),
            subtitle_hit=False,
            u2_task_id=task_id,
            u2_task_status="UNKNOWN",
        )
        if write_card:
            result["card_write"] = write_benchmark_card(
                payload=result,
                platform="xiaohongshu",
                card_type=card_type,
                wiki_root=wiki_root,
                collect_material=collect_material,
            )
        return result

    poll_result = poll_u2_task(
        base_url=runtime["base_url"],
        token=runtime["token"],
        timeout_ms=runtime["timeout_ms"],
        task_id=task_id,
        poll_interval_sec=poll_interval_sec,
        max_polls=max_polls,
    )
    trace.append(
        {
            "step": "u2_poll_task",
            "endpoint": "/api/u2/v1/tasks/{task_id}",
            "task_id": task_id,
            "task_status": poll_result.get("task_status"),
            "request_id": poll_result.get("request_id"),
            "ok": poll_result.get("ok"),
            "error_reason": poll_result.get("error_reason"),
            "attempts": len(poll_result.get("trace", [])),
        }
    )

    raw_content = poll_result.get("transcript_text", "") if poll_result.get("ok") else ""
    result = _build_result(
        source_input=source_input,
        raw_content=raw_content,
        confidence="high" if poll_result.get("ok") and raw_content else "low",
        error_reason=poll_result.get("error_reason"),
        extract_trace=trace,
        request_id=poll_result.get("request_id") or submit_response.get("request_id") or note_response.get("request_id"),
        text_source="u2",
        note_id=str(resolved_note_id) if resolved_note_id else source_input.get("note_id"),
        subtitle_hit=False,
        u2_task_id=task_id,
        u2_task_status=poll_result.get("task_status"),
    )

    if write_card:
        result["card_write"] = write_benchmark_card(
            payload=result,
            platform="xiaohongshu",
            card_type=card_type,
            wiki_root=wiki_root,
            collect_material=collect_material,
        )

    return result


def main() -> None:
    parser = argparse.ArgumentParser(description="Run xiaohongshu extraction chain")
    parser.add_argument("input", nargs="?", default=None, help="Share URL or note_id")
    parser.add_argument("--share-text", default=None, help="Xiaohongshu share URL/text")
    parser.add_argument("--note-id", default=None, help="Xiaohongshu note_id")
    parser.add_argument("--config", default=None, help="Runtime config YAML path")
    parser.add_argument("--env-file", default=None, help="Optional env file path")
    parser.add_argument("--api-key-env", default=None, help="API key env variable name")
    parser.add_argument("--base-url", default=None, help="Tikomni base URL")
    parser.add_argument("--timeout-ms", type=int, default=None, help="Request timeout ms")
    parser.add_argument("--poll-interval-sec", type=float, default=None, help="U2 polling interval seconds")
    parser.add_argument("--max-polls", type=int, default=None, help="Max U2 polls")
    parser.add_argument("--idempotency-key", default=None, help="Optional idempotency key (not sent by default)")
    parser.add_argument("--force-u2-fallback", action="store_true", help="Skip subtitle usage and force U2 fallback (test)")
    parser.add_argument("--write-card", action="store_true", help="Write benchmark card to WIKI")
    parser.add_argument("--card-type", choices=["work", "author", "author_sample_work"], default="work", help="Primary card type")
    parser.add_argument("--collect-material", action="store_true", help="Write extra CMAT card")
    parser.add_argument("--wiki-root", default=DEFAULT_WIKI_ROOT, help="WIKI root")
    args = parser.parse_args()

    config, _ = load_tikomni_config(args.config)

    api_key_env = args.api_key_env or config_get(config, "runtime.auth_env_key", "TIKOMNI_API_KEY")
    base_url = args.base_url or config_get(config, "runtime.base_url", None)
    timeout_ms = args.timeout_ms if args.timeout_ms is not None else config_get(config, "runtime.timeout_ms", None)
    poll_interval_sec = (
        args.poll_interval_sec
        if args.poll_interval_sec is not None
        else config_get(config, "asr_strategy.poll_interval_sec", 3.0)
    )
    max_polls = args.max_polls if args.max_polls is not None else config_get(config, "asr_strategy.max_polls", 30)

    try:
        result = run_xiaohongshu_extract(
            input_value=args.input,
            share_text=args.share_text,
            note_id=args.note_id,
            env_file=args.env_file,
            api_key_env=api_key_env,
            base_url=base_url,
            timeout_ms=timeout_ms,
            poll_interval_sec=float(poll_interval_sec),
            max_polls=int(max_polls),
            idempotency_key=args.idempotency_key,
            force_u2_fallback=args.force_u2_fallback,
            write_card=args.write_card,
            card_type=args.card_type,
            collect_material=args.collect_material,
            wiki_root=args.wiki_root,
        )
    except ValueError as error:
        result = {
            "platform": "xiaohongshu",
            "raw_content": "",
            "summary": "",
            "insights": ["source=xiaohongshu:runtime", "runtime_not_ready"],
            "confidence": "low",
            "error_reason": str(error),
            "extract_trace": [],
            "request_id": None,
        }

    write_json_stdout(result)
    raise SystemExit(0 if not result.get("error_reason") else 1)


if __name__ == "__main__":
    main()
