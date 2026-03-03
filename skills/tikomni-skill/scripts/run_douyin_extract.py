#!/usr/bin/env python3
"""Douyin single-video extraction chain: u1 -> u2 submit -> poll."""

import argparse
import time
from typing import Any, Dict, List, Optional

from config_loader import config_get, load_tikomni_config
from poll_u2_task import poll_u2_task
from tikomni_common import (
    call_json_api,
    deep_find_first,
    extract_task_id,
    resolve_runtime,
    summarize_content,
    write_json_stdout,
)
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

    primary = call_json_api(
        base_url=base_url,
        path="/api/u1/v1/douyin/app/v3/fetch_video_high_quality_play_url",
        token=token,
        method="GET",
        timeout_ms=timeout_ms,
        params=params,
    )
    primary["_endpoint"] = "/api/u1/v1/douyin/app/v3/fetch_video_high_quality_play_url"
    if primary["ok"]:
        return primary

    fallback = call_json_api(
        base_url=base_url,
        path="/api/u1/v1/douyin/web/fetch_video_high_quality_play_url",
        token=token,
        method="GET",
        timeout_ms=timeout_ms,
        params=params,
    )
    fallback["_endpoint"] = "/api/u1/v1/douyin/web/fetch_video_high_quality_play_url"
    fallback["_primary_failed"] = primary
    return fallback


def _u2_submit(
    *,
    base_url: str,
    token: str,
    timeout_ms: int,
    original_video_url: str,
    idempotency_key: Optional[str],
) -> Dict[str, Any]:
    extra_headers = {}
    if idempotency_key:
        extra_headers["idempotency-key"] = idempotency_key

    return call_json_api(
        base_url=base_url,
        path="/api/u2/v1/services/audio/asr/transcription",
        token=token,
        method="POST",
        timeout_ms=timeout_ms,
        body={"input": {"file_urls": [original_video_url]}},
        extra_headers=extra_headers,
    )


def _is_retriable_submit_failure(response: Dict[str, Any]) -> bool:
    status_code = response.get("status_code")
    if isinstance(status_code, str) and status_code.isdigit():
        status_code = int(status_code)
    if isinstance(status_code, (int, float)) and int(status_code) in {502, 503, 504}:
        return True

    error_reason = str(response.get("error_reason") or "").upper()
    return "UPSTREAM_TIMEOUT" in error_reason or "TIMEOUT" in error_reason


def _u2_submit_with_retry(
    *,
    base_url: str,
    token: str,
    timeout_ms: int,
    original_video_url: str,
    idempotency_key: Optional[str],
    max_retries: int,
    backoff_ms: int,
) -> Dict[str, Any]:
    retries = max(0, int(max_retries))
    base_backoff = max(0, int(backoff_ms))
    max_attempts = 1 + retries

    retry_chain: List[Dict[str, Any]] = []
    final_response: Dict[str, Any] = {}
    final_task_id: Optional[str] = None
    final_submit_status = "failed_unknown"

    for attempt in range(1, max_attempts + 1):
        wait_ms = 0 if attempt == 1 else base_backoff * (2 ** (attempt - 2))
        if wait_ms > 0:
            time.sleep(wait_ms / 1000.0)

        submit_response = _u2_submit(
            base_url=base_url,
            token=token,
            timeout_ms=timeout_ms,
            original_video_url=original_video_url,
            idempotency_key=idempotency_key,
        )
        task_id = extract_task_id(submit_response.get("data"))
        retriable = _is_retriable_submit_failure(submit_response)

        retry_chain.append(
            {
                "attempt": attempt,
                "wait_ms": wait_ms,
                "status_code": submit_response.get("status_code"),
                "error_reason": submit_response.get("error_reason"),
                "ok": submit_response.get("ok"),
                "task_id": task_id,
                "retriable": retriable,
            }
        )

        final_response = submit_response
        final_task_id = task_id

        if submit_response.get("ok") and task_id:
            final_submit_status = "success"
            break

        if submit_response.get("ok") and not task_id:
            final_submit_status = "failed_missing_task_id"
            break

        if retriable and attempt < max_attempts:
            final_submit_status = "retrying"
            continue

        final_submit_status = "failed_retries_exhausted" if retriable else "failed_non_retriable"
        break

    return {
        "submit_response": final_response,
        "task_id": final_task_id,
        "retry_chain": retry_chain,
        "final_submit_status": final_submit_status,
    }


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
    idempotency_key: Optional[str],
    u2_submit_max_retries: int,
    u2_submit_backoff_ms: int,
    write_card: bool,
    card_type: str,
    collect_material: bool,
    wiki_root: str,
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
            {
                "step": "u1_fetch_video_high_quality_play_url_primary",
                "endpoint": "/api/u1/v1/douyin/app/v3/fetch_video_high_quality_play_url",
                "status_code": primary_failed.get("status_code"),
                "request_id": primary_failed.get("request_id"),
                "ok": primary_failed.get("ok"),
                "error_reason": primary_failed.get("error_reason"),
            }
        )

    trace.append(
        {
            "step": "u1_fetch_video_high_quality_play_url_effective",
            "endpoint": play_url_response.get("_endpoint"),
            "status_code": play_url_response.get("status_code"),
            "request_id": play_url_response.get("request_id"),
            "ok": play_url_response.get("ok"),
            "error_reason": play_url_response.get("error_reason"),
        }
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
            )
        return result

    submit_bundle = _u2_submit_with_retry(
        base_url=runtime["base_url"],
        token=runtime["token"],
        timeout_ms=runtime["timeout_ms"],
        original_video_url=original_video_url,
        idempotency_key=idempotency_key,
        max_retries=u2_submit_max_retries,
        backoff_ms=u2_submit_backoff_ms,
    )
    submit_response = submit_bundle["submit_response"]
    task_id = submit_bundle.get("task_id")

    trace.append(
        {
            "step": "u2_submit_transcription",
            "endpoint": "/api/u2/v1/services/audio/asr/transcription",
            "status_code": submit_response.get("status_code"),
            "request_id": submit_response.get("request_id"),
            "ok": submit_response.get("ok"),
            "error_reason": submit_response.get("error_reason"),
            "task_id": task_id,
            "idempotency_key_sent": bool(idempotency_key),
            "final_submit_status": submit_bundle.get("final_submit_status"),
        }
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

    if not submit_response["ok"] or not task_id:
        result = _build_result(
            source_input=normalized_input,
            raw_content="",
            confidence="low",
            error_reason=submit_response.get("error_reason") or "u2_submit_failed_or_missing_task_id",
            extract_trace=trace,
            request_id=submit_response.get("request_id") or play_url_response.get("request_id"),
            original_video_url=original_video_url,
            u2_task_id=task_id,
            u2_task_status="UNKNOWN",
        )
        if write_card:
            result["card_write"] = write_benchmark_card(
                payload=result,
                platform="douyin",
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
        source_input=normalized_input,
        raw_content=raw_content,
        confidence="high" if poll_result.get("ok") and raw_content else "low",
        error_reason=poll_result.get("error_reason"),
        extract_trace=trace,
        request_id=poll_result.get("request_id") or submit_response.get("request_id") or play_url_response.get("request_id"),
        original_video_url=original_video_url,
        u2_task_id=task_id,
        u2_task_status=poll_result.get("task_status"),
    )

    if write_card:
        result["card_write"] = write_benchmark_card(
            payload=result,
            platform="douyin",
            card_type=card_type,
            wiki_root=wiki_root,
            collect_material=collect_material,
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
        "--idempotency-key",
        default=None,
        help="Optional idempotency key (not sent by default)",
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
            idempotency_key=args.idempotency_key,
            u2_submit_max_retries=int(u2_submit_max_retries),
            u2_submit_backoff_ms=int(u2_submit_backoff_ms),
            write_card=args.write_card,
            card_type=args.card_type,
            collect_material=args.collect_material,
            wiki_root=args.wiki_root,
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
