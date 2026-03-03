#!/usr/bin/env python3
"""Unified URL runner for douyin/xiaohongshu local adaptation."""

import argparse
from urllib.parse import urlparse

from run_douyin_extract import run_douyin_extract
from run_xiaohongshu_extract import run_xiaohongshu_extract
from tikomni_common import write_json_stdout
from write_benchmark_card import DEFAULT_WIKI_ROOT


def detect_platform(input_value: str) -> str:
    candidate = (input_value or "").strip().lower()
    if not candidate:
        return "unknown"

    if candidate.startswith("http://") or candidate.startswith("https://"):
        host = urlparse(candidate).netloc.lower()
        if "douyin.com" in host or "iesdouyin.com" in host:
            return "douyin"
        if "xiaohongshu.com" in host or "xhslink.com" in host:
            return "xiaohongshu"

    if "douyin" in candidate:
        return "douyin"
    if "xiaohongshu" in candidate or "xhs" in candidate:
        return "xiaohongshu"
    return "unknown"


def main() -> None:
    parser = argparse.ArgumentParser(description="Run tikomni local extractor by URL")
    parser.add_argument("input", help="URL or platform-specific ID")
    parser.add_argument("--platform", choices=["auto", "douyin", "xiaohongshu"], default="auto")
    parser.add_argument("--env-file", default=None, help="Optional env file path")
    parser.add_argument("--api-key-env", default="TIKOMNI_API_KEY", help="API key env variable name")
    parser.add_argument("--base-url", default=None, help="Tikomni API base URL")
    parser.add_argument("--timeout-ms", type=int, default=None, help="Request timeout ms")
    parser.add_argument("--poll-interval-sec", type=float, default=3.0, help="U2 poll interval")
    parser.add_argument("--max-polls", type=int, default=30, help="Max U2 poll attempts")
    parser.add_argument("--idempotency-key", default=None, help="Optional idempotency key (default omitted)")
    parser.add_argument("--force-u2-fallback", action="store_true", help="XHS only: force subtitle miss for fallback test")
    parser.add_argument("--write-card", action="store_true", help="Write markdown card")
    parser.add_argument("--card-type", choices=["work", "author", "author_sample_work"], default="work", help="Primary card type")
    parser.add_argument("--collect-material", action="store_true", help="Write CMAT only when explicit")
    parser.add_argument("--wiki-root", default=DEFAULT_WIKI_ROOT, help="WIKI root")
    args = parser.parse_args()

    platform = args.platform
    if platform == "auto":
        platform = detect_platform(args.input)

    if platform == "douyin":
        result = run_douyin_extract(
            input_value=args.input,
            share_url=None,
            aweme_id=None,
            env_file=args.env_file,
            api_key_env=args.api_key_env,
            base_url=args.base_url,
            timeout_ms=args.timeout_ms,
            poll_interval_sec=args.poll_interval_sec,
            max_polls=args.max_polls,
            idempotency_key=args.idempotency_key,
            write_card=args.write_card,
            card_type=args.card_type,
            collect_material=args.collect_material,
            wiki_root=args.wiki_root,
        )
    elif platform == "xiaohongshu":
        result = run_xiaohongshu_extract(
            input_value=args.input,
            share_text=None,
            note_id=None,
            env_file=args.env_file,
            api_key_env=args.api_key_env,
            base_url=args.base_url,
            timeout_ms=args.timeout_ms,
            poll_interval_sec=args.poll_interval_sec,
            max_polls=args.max_polls,
            idempotency_key=args.idempotency_key,
            force_u2_fallback=args.force_u2_fallback,
            write_card=args.write_card,
            card_type=args.card_type,
            collect_material=args.collect_material,
            wiki_root=args.wiki_root,
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

    write_json_stdout(result)
    raise SystemExit(0 if not result.get("error_reason") else 1)


if __name__ == "__main__":
    main()
