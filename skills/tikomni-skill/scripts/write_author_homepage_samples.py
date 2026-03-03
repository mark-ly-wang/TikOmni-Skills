#!/usr/bin/env python3
"""Batch writer for author-homepage sampled work cards."""

import argparse
import json
import os
from typing import Any, Dict, List

from tikomni_common import normalize_text, read_json_file, write_json_stdout
from write_benchmark_card import DEFAULT_WIKI_ROOT, write_benchmark_card


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
        for key in ("nickname", "unique_id", "sec_uid"):
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
    parser.add_argument("--input-json", default="-", help="JSON list/dict path or '-' for stdin")
    parser.add_argument("--wiki-root", default=DEFAULT_WIKI_ROOT, help="WIKI root")
    parser.add_argument("--sample-author", default="", help="Override author folder name")
    parser.add_argument("--collect-material", action="store_true", help="Also write CMAT cards")
    args = parser.parse_args()

    data = _read_input(args.input_json)
    payloads = _items(data)

    results: List[Dict[str, Any]] = []
    for payload in payloads:
        result = write_benchmark_card(
            payload=payload,
            platform=args.platform,
            card_type="author_sample_work",
            wiki_root=args.wiki_root,
            collect_material=args.collect_material,
            sample_author=_author_hint(payload, args.sample_author),
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
