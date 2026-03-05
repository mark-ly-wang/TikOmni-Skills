#!/usr/bin/env python3

if __package__ in {None, ""}:
    import sys
    from pathlib import Path

    _self = Path(__file__).resolve()
    for _parent in _self.parents:
        if (_parent / "scripts" / "core" / "bootstrap_env.py").is_file():
            sys.path.insert(0, str(_parent))
            break

"""Regression checks for componentized author-home workflow.

Uses mock collectors to validate cursor loop + hard cap 200 logic for both platforms.
"""

import json
from typing import Any, Dict, List

from scripts.author_home.orchestrator.run_author_analysis import run_author_home_analysis


def _mock_douyin_collector(**_: Any) -> Dict[str, Any]:
    works: List[Dict[str, Any]] = []
    for idx in range(260):
        works.append(
            {
                "aweme_id": f"dy_{idx}",
                "desc": f"douyin sample {idx}",
                "create_time": 1700000000 + idx,
                "duration": 18000,
                "statistics": {
                    "digg_count": idx,
                    "comment_count": idx // 2,
                    "collect_count": idx // 3,
                    "share_count": idx // 4,
                    "play_count": idx * 10,
                },
            }
        )
    return {
        "platform": "douyin",
        "resolved_author_id": "MS4wLjABAAAA-mock",
        "profile_response": {
            "ok": True,
            "data": {
                "nickname": "抖音样本作者",
                "sec_user_id": "MS4wLjABAAAA-mock",
                "ip_location": "上海",
                "follower_count": 123456,
                "total_favorited": 987654,
                "collect_count": 2222,
                "signature": "douyin profile mock",
                "avatar_url": "https://example.com/dy.jpg",
                "aweme_count": 260,
                "verified": True,
            },
        },
        "works": works,
        "pagination": {
            "sort": "latest",
            "sort_type": 0,
            "cursor_mode": "max_cursor",
            "pages": [
                {"page": 1, "cursor_in": 0, "cursor_out": 20, "has_more": 1, "items": 20},
                {"page": 2, "cursor_in": 20, "cursor_out": 40, "has_more": 1, "items": 20},
            ],
            "total_collected": 260,
            "max_items": 200,
        },
        "extract_trace": [{"step": "mock.douyin.collect", "ok": True}],
        "request_id": "mock-dy-request",
    }


def _mock_xhs_collector(**_: Any) -> Dict[str, Any]:
    works: List[Dict[str, Any]] = []
    for idx in range(235):
        works.append(
            {
                "note_id": f"xhs_{idx}",
                "title": f"xhs sample {idx}",
                "desc": f"xhs desc {idx}",
                "time": 1700100000 + idx,
                "interact_info": {
                    "liked_count": idx,
                    "comment_count": idx // 2,
                    "collected_count": idx // 3,
                    "share_count": idx // 4,
                    "view_count": idx * 8,
                },
            }
        )
    return {
        "platform": "xiaohongshu",
        "resolved_author_id": "xhs_mock_uid",
        "profile_response": {
            "ok": True,
            "data": {
                "nickname": "小红书样本作者",
                "user_id": "xhs_mock_uid",
                "ip_location": "杭州",
                "fans": 54321,
                "liked_count": 200000,
                "collected_count": 3333,
                "desc": "xhs profile mock",
                "image": "https://example.com/xhs.jpg",
                "note_count": 235,
                "verified": False,
            },
        },
        "works": works,
        "pagination": {
            "sort": "latest",
            "sort_type": "latest",
            "cursor_mode": "cursor",
            "pages": [
                {"page": 1, "cursor_in": "", "cursor_out": "a1", "has_more": 1, "items": 20},
                {"page": 2, "cursor_in": "a1", "cursor_out": "a2", "has_more": 1, "items": 20},
            ],
            "total_collected": 235,
            "max_items": 200,
        },
        "extract_trace": [{"step": "mock.xhs.collect", "ok": True}],
        "request_id": "mock-xhs-request",
    }


def _assert_result(name: str, result: Dict[str, Any]) -> Dict[str, Any]:
    works = result.get("works") if isinstance(result.get("works"), list) else []
    checkpoint = result.get("checkpoint") if isinstance(result.get("checkpoint"), dict) else {}
    ok = len(works) == 200 and int(checkpoint.get("max_items") or 0) == 200
    return {
        "name": name,
        "ok": ok,
        "works": len(works),
        "max_items": checkpoint.get("max_items"),
        "cursor_mode": checkpoint.get("cursor_mode"),
        "summary": result.get("summary"),
    }


def main() -> None:
    dy = run_author_home_analysis(
        platform="douyin",
        input_value="mock://douyin",
        base_url="https://api.tikomni.com",
        token="mock-token",
        timeout_ms=1000,
        write_card=False,
        collector_override=_mock_douyin_collector,
    )
    xhs = run_author_home_analysis(
        platform="xiaohongshu",
        input_value="mock://xhs",
        base_url="https://api.tikomni.com",
        token="mock-token",
        timeout_ms=1000,
        write_card=False,
        collector_override=_mock_xhs_collector,
    )

    checks = [_assert_result("douyin", dy), _assert_result("xiaohongshu", xhs)]
    output = {
        "ok": all(item.get("ok") for item in checks),
        "checks": checks,
    }
    print(json.dumps(output, ensure_ascii=False, indent=2))
    raise SystemExit(0 if output["ok"] else 1)


if __name__ == "__main__":
    main()
