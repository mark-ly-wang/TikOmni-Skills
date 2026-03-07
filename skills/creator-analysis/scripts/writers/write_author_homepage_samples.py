#!/usr/bin/env python3

if __package__ in {None, ""}:
    import sys
    from pathlib import Path

    _self = Path(__file__).resolve()
    for _parent in _self.parents:
        if (_parent / "scripts").is_dir():
            sys.path.insert(0, str(_parent))
            break

"""Batch writer for author-homepage sampled work cards."""

import argparse
import json
import os
from typing import Any, Dict, List

from scripts.core.config_loader import load_tikomni_config
from scripts.core.tikomni_common import normalize_text, read_json_file, write_json_stdout
from scripts.writers.write_benchmark_card import write_benchmark_card


def _read_input(path: str) -> Any:
    if path == "-":
        raw = os.read(0, 2 * 1024 * 1024).decode("utf-8", errors="replace").strip()
        return json.loads(raw) if raw else {}
    return read_json_file(path)


def _author_hint(payload: Dict[str, Any], fallback: str) -> str:
    if fallback:
        return fallback
    author = payload.get("author")
    if isinstance(author, dict):
        for key in (
            "nickname",
            "author_handle",
            "platform_author_id",
            "author_platform_id",
            "xhs_user_id",
            "douyin_aweme_author_id",
            "douyin_sec_uid",
        ):
            text = normalize_text(author.get(key))
            if text:
                return text
    return "作者"


def _items(data: Any) -> List[Dict[str, Any]]:
    if isinstance(data, list):
        return [item for item in data if isinstance(item, dict)]
    if isinstance(data, dict):
        if isinstance(data.get("items"), list):
            return [item for item in data["items"] if isinstance(item, dict)]
        return [data]
    return []


def main() -> None:
    parser = argparse.ArgumentParser(description="Write homepage sampled works to author sample directory")
    parser.add_argument("--platform", required=True, help="Platform name, e.g. douyin/xiaohongshu")
    parser.add_argument("--config", default=None, help="Runtime config YAML path")
    parser.add_argument("--input-json", default="-", help="JSON list/dict path or '-' for stdin")
    parser.add_argument("--allow-process-env", action="store_true", help="Allow process env to override .env/.env.local")
    parser.add_argument("--card-root", default=None, help="Card root (absolute); falls back to TIKOMNI_CARD_ROOT when writing cards")
    parser.add_argument("--sample-author", default="", help="Override author folder name")
    args = parser.parse_args()

    config, _ = load_tikomni_config(
        args.config,
        allow_process_env=args.allow_process_env,
    )

    data = _read_input(args.input_json)
    payloads = _items(data)

    results: List[Dict[str, Any]] = []
    for payload in payloads:
        payload_with_kind = dict(payload)
        payload_with_kind.setdefault("content_kind", "author_home")
        result = write_benchmark_card(
            payload=payload_with_kind,
            platform=args.platform,
            card_type="author_sample_work",
            card_root=args.card_root,
            sample_author=_author_hint(payload, args.sample_author),
            content_kind="author_home",
            storage_config=config,
        )
        results.append(result)

    write_json_stdout(
        {
            "ok": True,
            "platform": args.platform,
            "count": len(results),
            "results": results,
        }
    )


if __name__ == "__main__":
    main()
