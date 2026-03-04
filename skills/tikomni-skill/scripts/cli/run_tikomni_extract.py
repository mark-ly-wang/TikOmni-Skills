#!/usr/bin/env python3

if __package__ in {None, ""}:
    import sys
    from pathlib import Path

    _self = Path(__file__).resolve()
    for _parent in _self.parents:
        if (_parent / "scripts").is_dir():
            sys.path.insert(0, str(_parent))
            break

"""Unified URL runner for douyin/xiaohongshu local adaptation."""

import argparse

from scripts.core.config_loader import config_get, load_tikomni_config
from scripts.core.extract_pipeline import detect_platform_from_input
from scripts.platform.douyin.run_douyin_single_video import run_douyin_single_video
from scripts.platform.xiaohongshu.run_xiaohongshu_extract import run_xiaohongshu_extract
from scripts.core.tikomni_common import write_json_stdout


def main() -> None:
    parser = argparse.ArgumentParser(description="Run tikomni local extractor by URL")
    parser.add_argument("input", help="URL or platform-specific ID")
    parser.add_argument("--platform", choices=["auto", "douyin", "xiaohongshu"], default="auto")
    parser.add_argument("--config", default=None, help="Runtime config YAML path")
    parser.add_argument("--env-file", default=None, help="Optional env file path")
    parser.add_argument("--allow-process-env", action="store_true", help="Allow process env to override .env/.env.local")
    parser.add_argument("--api-key-env", default=None, help="API key env variable name")
    parser.add_argument("--base-url", default=None, help="Tikomni API base URL")
    parser.add_argument("--timeout-ms", type=int, default=None, help="Request timeout ms")
    parser.add_argument("--poll-interval-sec", type=float, default=None, help="U2 poll interval")
    parser.add_argument("--max-polls", type=int, default=None, help="Max U2 poll attempts")
    parser.add_argument("--u2-submit-max-retries", type=int, default=None, help="Douyin U2 submit max retries")
    parser.add_argument("--u2-submit-backoff-ms", type=int, default=None, help="Douyin U2 submit base backoff ms")
    parser.add_argument("--u2-timeout-retry-enabled", type=str, choices=["true", "false"], default=None, help="Enable timeout-only retry")
    parser.add_argument("--u2-timeout-retry-max-retries", type=int, default=None, help="Timeout-only retry max retries")
    parser.add_argument("--xhs-u2-submit-max-retries", type=int, default=None, help="Xiaohongshu U2 submit max retries")
    parser.add_argument("--xhs-u2-submit-backoff-ms", type=int, default=None, help="Xiaohongshu U2 submit base backoff ms")
    parser.add_argument("--force-u2-fallback", action="store_true", help="XHS only: force subtitle miss for fallback test")
    parser.add_argument("--write-card", dest="write_card", action="store_true", help="Write markdown card (default on)")
    parser.add_argument("--no-write-card", dest="write_card", action="store_false", help="Disable markdown card writing")
    parser.set_defaults(write_card=True)
    parser.add_argument("--card-type", choices=["work", "author", "author_sample_work"], default="work", help="Primary card type")
    parser.add_argument("--collect-material", action="store_true", help="Write CMAT only when explicit")
    parser.add_argument("--card-root", default=None, help="Card root (absolute); falls back to TIKOMNI_CARD_ROOT when writing cards")
    parser.add_argument("--persist-output", dest="persist_output", action="store_true", help="Persist douyin JSON artifact to TIKOMNI_OUTPUT_ROOT (default on)")
    parser.add_argument("--no-persist-output", dest="persist_output", action="store_false", help="Disable douyin artifact persistence")
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
    xhs_u2_submit_max_retries = (
        args.xhs_u2_submit_max_retries
        if args.xhs_u2_submit_max_retries is not None
        else config_get(config, "asr_strategy.submit_retry.xiaohongshu_note.max_retries", 0)
    )
    xhs_u2_submit_backoff_ms = (
        args.xhs_u2_submit_backoff_ms
        if args.xhs_u2_submit_backoff_ms is not None
        else config_get(config, "asr_strategy.submit_retry.xiaohongshu_note.backoff_ms", 0)
    )

    platform = args.platform
    if platform == "auto":
        platform = detect_platform_from_input(args.input)

    try:
        if platform == "douyin":
            douyin_app_timeout_ms = config_get(config, "runtime.douyin.app_timeout_ms", None)
            douyin_web_timeout_ms = config_get(config, "runtime.douyin.web_timeout_ms", None)
            result = run_douyin_single_video(
                input_value=args.input,
                share_url=None,
                env_file=resolved_env_file,
                api_key_env=api_key_env,
                base_url=base_url,
                timeout_ms=timeout_ms,
                app_timeout_ms=douyin_app_timeout_ms,
                web_timeout_ms=douyin_web_timeout_ms,
                poll_interval_sec=float(poll_interval_sec),
                max_polls=int(max_polls),
                u2_submit_max_retries=int(u2_submit_max_retries),
                u2_submit_backoff_ms=int(u2_submit_backoff_ms),
                write_card=args.write_card,
                card_type=args.card_type,
                collect_material=args.collect_material,
                card_root=args.card_root,
                content_kind="single_video",
                storage_config=config,
                allow_process_env=args.allow_process_env,
                persist_output=args.persist_output,
            )
        elif platform == "xiaohongshu":
            result = run_xiaohongshu_extract(
                input_value=args.input,
                share_text=None,
                note_id=None,
                env_file=resolved_env_file,
                api_key_env=api_key_env,
                base_url=base_url,
                timeout_ms=timeout_ms,
                poll_interval_sec=float(poll_interval_sec),
                max_polls=int(max_polls),
                u2_submit_max_retries=int(xhs_u2_submit_max_retries),
                u2_submit_backoff_ms=int(xhs_u2_submit_backoff_ms),
                u2_timeout_retry_enabled=bool(u2_timeout_retry_enabled),
                u2_timeout_retry_max_retries=int(u2_timeout_retry_max_retries),
                force_u2_fallback=args.force_u2_fallback,
                write_card=args.write_card,
                card_type=args.card_type,
                collect_material=args.collect_material,
                card_root=args.card_root,
                storage_config=config,
                allow_process_env=args.allow_process_env,
            )
        else:
            result = {
                "platform": "unknown",
                "raw_content": "",
                "summary": "",
                "insights": ["source=runner", "unsupported_platform"],
                "confidence": "low",
                "error_reason": "unsupported_platform",
                "extract_trace": [
                    {
                        "step": "platform_detect",
                        "input": args.input,
                        "detected": platform,
                    }
                ],
                "request_id": None,
            }
    except ValueError as error:
        result = {
            "platform": platform,
            "raw_content": "",
            "summary": "",
            "insights": ["source=runner", "runtime_not_ready"],
            "confidence": "low",
            "error_reason": str(error),
            "extract_trace": [],
            "request_id": None,
        }

    write_json_stdout(result)
    raise SystemExit(0 if not result.get("error_reason") else 1)


if __name__ == "__main__":
    main()
