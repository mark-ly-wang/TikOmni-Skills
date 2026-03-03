#!/usr/bin/env python3
"""Douyin single-video extraction chain: u1 -> u2 submit -> poll."""

import argparse
from typing import Any, Dict, Optional

from asr_pipeline import run_u2_asr_with_timeout_retry
from config_loader import config_get, load_tikomni_config
from extract_pipeline import build_api_trace, request_with_optional_fallback
from tikomni_common import deep_find_first, resolve_runtime, summarize_content, write_json_stdout
from write_benchmark_card import DEFAULT_WIKI_ROOT, write_benchmark_card


def _normalize_input(input_value: Optional[str], share_url: Optional[str], aweme_id: Optional[str]) -> Dict[str, Optional[str]]:
    normalized_share = share_url
    normalized_aweme = aweme_id

    if input_value and not normalized_share and not normalized_aweme:
        candidate = input_value.strip()
        if candidate.startswith("http://") or candidate.startswith("https://"):
            normalized_share = candidate
        else:
            normalized_aweme = candidate

    return {
        "share_url": normalized_share,
        "aweme_id": normalized_aweme,
    }


def _u1_fetch_play_url(
    *,
    base_url: str,
    token: str,
    timeout_ms: int,
    share_url: Optional[str],
    aweme_id: Optional[str],
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if share_url:
        params["share_url"] = share_url
    if aweme_id:
        params["aweme_id"] = aweme_id

    return request_with_optional_fallback(
        base_url=base_url,
        token=token,
        timeout_ms=timeout_ms,
        method="GET",
        params=params,
        primary_path="/api/u1/v1/douyin/app/v3/fetch_video_high_quality_play_url",
        fallback_path="/api/u1/v1/douyin/web/fetch_video_high_quality_play_url",
    )


def _build_result(
    *,
    source_input: Dict[str, Optional[str]],
    raw_content: str,
    confidence: str,
    error_reason: Optional[str],
    extract_trace: Any,
    request_id: Optional[str],
    original_video_url: Optional[str],
    u2_task_id: Optional[str],
    u2_task_status: Optional[str],
) -> Dict[str, Any]:
    summary_block = summarize_content(raw_content, source="douyin:u1->u2")
    return {
        "platform": "douyin",
        "content_kind": "single_video",
        "source": source_input,
        "original_video_url": original_video_url,
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


def run_douyin_extract(
    *,
    input_value: Optional[str],
    share_url: Optional[str],
    aweme_id: Optional[str],
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
    write_card: bool,
    card_type: str,
    collect_material: bool,
    wiki_root: str,
    storage_config: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    normalized_input = _normalize_input(input_value, share_url, aweme_id)
    if not normalized_input["share_url"] and not normalized_input["aweme_id"]:
        result = _build_result(
            source_input=normalized_input,
            raw_content="",
            confidence="low",
            error_reason="missing_share_url_or_aweme_id",
            extract_trace=[],
            request_id=None,
            original_video_url=None,
            u2_task_id=None,
            u2_task_status="UNKNOWN",
        )
        if write_card:
            result["card_write"] = write_benchmark_card(
                payload=result,
                platform="douyin",
                card_type=card_type,
                wiki_root=wiki_root,
                collect_material=collect_material,
                content_kind="single_video",
                storage_config=storage_config,
            )
        return result

    runtime = resolve_runtime(
        env_file=env_file,
        api_key_env=api_key_env,
        base_url=base_url,
        timeout_ms=timeout_ms,
    )

    trace = []

    play_url_response = _u1_fetch_play_url(
        base_url=runtime["base_url"],
        token=runtime["token"],
        timeout_ms=runtime["timeout_ms"],
        share_url=normalized_input["share_url"],
        aweme_id=normalized_input["aweme_id"],
    )

    primary_failed = play_url_response.get("_primary_failed")
    if primary_failed:
        trace.append(
            build_api_trace(
                step="u1_fetch_video_high_quality_play_url_primary",
                endpoint="/api/u1/v1/douyin/app/v3/fetch_video_high_quality_play_url",
                response=primary_failed,
            )
        )

    trace.append(
        build_api_trace(
            step="u1_fetch_video_high_quality_play_url_effective",
            endpoint=play_url_response.get("_endpoint"),
            response=play_url_response,
        )
    )

    if not play_url_response["ok"]:
        result = _build_result(
            source_input=normalized_input,
            raw_content="",
            confidence="low",
            error_reason=play_url_response.get("error_reason") or "u1_fetch_failed",
            extract_trace=trace,
            request_id=play_url_response.get("request_id"),
            original_video_url=None,
            u2_task_id=None,
            u2_task_status="UNKNOWN",
        )
        if write_card:
            result["card_write"] = write_benchmark_card(
                payload=result,
                platform="douyin",
                card_type=card_type,
                wiki_root=wiki_root,
                collect_material=collect_material,
                content_kind="single_video",
                storage_config=storage_config,
            )
        return result

    original_video_url_value = deep_find_first(play_url_response["data"], ["original_video_url"])
    original_video_url = str(original_video_url_value).strip() if original_video_url_value else ""

    if not original_video_url:
        result = _build_result(
            source_input=normalized_input,
            raw_content="",
            confidence="low",
            error_reason="missing_original_video_url",
            extract_trace=trace,
            request_id=play_url_response.get("request_id"),
            original_video_url=None,
            u2_task_id=None,
            u2_task_status="UNKNOWN",
        )
        if write_card:
            result["card_write"] = write_benchmark_card(
                payload=result,
                platform="douyin",
                card_type=card_type,
                wiki_root=wiki_root,
                collect_material=collect_material,
                content_kind="single_video",
                storage_config=storage_config,
            )
        return result

    u2_bundle = run_u2_asr_with_timeout_retry(
        base_url=runtime["base_url"],
        token=runtime["token"],
        timeout_ms=runtime["timeout_ms"],
        video_url=original_video_url,
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

    trace.append(
        {
            "step": "u2_asr_timeout_retry",
            "endpoint": "/api/u2/v1/services/audio/asr/transcription + /api/u2/v1/tasks/{task_id}",
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

    if not poll_result.get("ok") and (
        not submit_response.get("ok") or not (poll_result.get("task_id") or task_id)
    ):
        result = _build_result(
            source_input=normalized_input,
            raw_content="",
            confidence="low",
            error_reason=poll_result.get("error_reason") or submit_response.get("error_reason") or "u2_submit_failed_or_missing_task_id",
            extract_trace=trace,
            request_id=(
                poll_result.get("request_id")
                or submit_response.get("request_id")
                or play_url_response.get("request_id")
            ),
            original_video_url=original_video_url,
            u2_task_id=poll_result.get("task_id") or task_id,
            u2_task_status=poll_result.get("task_status") or "UNKNOWN",
        )
        if write_card:
            result["card_write"] = write_benchmark_card(
                payload=result,
                platform="douyin",
                card_type=card_type,
                wiki_root=wiki_root,
                collect_material=collect_material,
                content_kind="single_video",
                storage_config=storage_config,
            )
        return result

    raw_content = poll_result.get("transcript_text", "") if poll_result.get("ok") else ""
    result = _build_result(
        source_input=normalized_input,
        raw_content=raw_content,
        confidence="high" if poll_result.get("ok") and raw_content else "low",
        error_reason=poll_result.get("error_reason"),
        extract_trace=trace,
        request_id=poll_result.get("request_id") or submit_response.get("request_id") or play_url_response.get("request_id"),
        original_video_url=original_video_url,
        u2_task_id=poll_result.get("task_id") or task_id,
        u2_task_status=poll_result.get("task_status"),
    )

    if write_card:
        result["card_write"] = write_benchmark_card(
            payload=result,
            platform="douyin",
            card_type=card_type,
            wiki_root=wiki_root,
            collect_material=collect_material,
            content_kind="single_video",
            storage_config=storage_config,
        )

    return result


def main() -> None:
    parser = argparse.ArgumentParser(description="Run douyin single-video extraction chain")
    parser.add_argument("input", nargs="?", default=None, help="Share URL or aweme_id")
    parser.add_argument("--share-url", default=None, help="Douyin share URL")
    parser.add_argument("--aweme-id", default=None, help="Douyin aweme_id")
    parser.add_argument("--config", default=None, help="Runtime config YAML path")
    parser.add_argument("--env-file", default=None, help="Optional env file path")
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
    u2_submit_max_retries = (
        args.u2_submit_max_retries
        if args.u2_submit_max_retries is not None
        else config_get(config, "asr_strategy.submit_retry.douyin_video.max_retries", 2)
    )
    u2_submit_backoff_ms = (
        args.u2_submit_backoff_ms
        if args.u2_submit_backoff_ms is not None
        else config_get(config, "asr_strategy.submit_retry.douyin_video.backoff_ms", 1500)
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
        result = run_douyin_extract(
            input_value=args.input,
            share_url=args.share_url,
            aweme_id=args.aweme_id,
            env_file=args.env_file,
            api_key_env=api_key_env,
            base_url=base_url,
            timeout_ms=timeout_ms,
            poll_interval_sec=float(poll_interval_sec),
            max_polls=int(max_polls),
            u2_submit_max_retries=int(u2_submit_max_retries),
            u2_submit_backoff_ms=int(u2_submit_backoff_ms),
            u2_timeout_retry_enabled=bool(u2_timeout_retry_enabled),
            u2_timeout_retry_max_retries=int(u2_timeout_retry_max_retries),
            write_card=args.write_card,
            card_type=args.card_type,
            collect_material=args.collect_material,
            wiki_root=args.wiki_root,
            storage_config=config,
        )
    except ValueError as error:
        result = {
            "platform": "douyin",
            "raw_content": "",
            "summary": "",
            "insights": ["source=douyin:u1->u2", "runtime_not_ready"],
            "confidence": "low",
            "error_reason": str(error),
            "extract_trace": [],
            "request_id": None,
        }

    write_json_stdout(result)
    raise SystemExit(0 if not result.get("error_reason") else 1)


if __name__ == "__main__":
    main()
