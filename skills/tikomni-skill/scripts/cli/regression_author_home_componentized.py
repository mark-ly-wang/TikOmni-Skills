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

import contextlib
import importlib
import io
import json
import tempfile
from pathlib import Path
from typing import Any, Dict, List

from scripts.author_home.orchestrator.run_author_analysis import run_author_home_analysis
from scripts.cli.run_tikomni_extract import _ensure_output_persist
from scripts.core.progress_report import build_progress_reporter

WORK_ANALYSIS_BUILD_CALLS = {"count": 0}


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


def _mock_douyin_empty_collector(**_: Any) -> Dict[str, Any]:
    return {
        "platform": "douyin",
        "resolved_author_id": "",
        "profile_response": {
            "ok": True,
            "request_id": "mock-empty-request",
            "data": {
                "nickname": "",
                "sec_user_id": "",
                "ip_location": "",
                "follower_count": 0,
                "total_favorited": 0,
                "collect_count": 0,
                "signature": "",
                "avatar_url": "",
                "aweme_count": 0,
                "verified": False,
            },
        },
        "works": [],
        "pagination": {
            "sort": "latest",
            "sort_type": 0,
            "cursor_mode": "max_cursor",
            "pages": [{"page": 1, "cursor_in": 0, "cursor_out": 0, "has_more": 0, "items": 0}],
            "total_collected": 0,
            "max_items": 200,
        },
        "extract_trace": [
            {"step": "mock.douyin.collect.error", "ok": False, "request_id": "mock-empty-request", "error_reason": "resolve_failed"}
        ],
        "request_id": "mock-empty-request",
    }


def _fake_analysis(_: Dict[str, Any], works: List[Dict[str, Any]]):
    return (
        {
            "author_portrait": "mock portrait",
            "business_analysis": "mock business analysis",
            "benchmark_analysis": "mock benchmark analysis",
            "business_score": 78,
            "benchmark_gap_score": 66,
            "style_radar": {"选题": 80, "表达": 77, "结构": 75, "节奏": 74, "人设": 73, "转化": 70, "差异化": 71, "稳定性": 79},
            "core_contradictions": ["mock contradiction"],
            "recommendations": ["mock recommendation"],
        },
        [],
        [{"step": "analysis.mock", "works_used": min(len(works), 30), "ok": True}],
    )


def _fake_work_card_analysis(payload: Dict[str, Any], platform: str, card_type: str) -> Dict[str, Any]:
    WORK_ANALYSIS_BUILD_CALLS["count"] += 1
    title = str(payload.get("title") or "作品标题")
    platform_work_id = str(payload.get("platform_work_id") or "unknown")
    return {
        "fields": {
            "title": title,
            "platform": platform,
            "platform_work_id": platform_work_id,
        },
        "analysis_sections": {
            "modules": {
                "选题": [f"{title} 选题分析"],
                "文风": [f"{title} 文风分析"],
                "Hook": [f"{title} Hook 分析"],
                "结构": [f"{title} 结构分析"],
            },
            "insight": [f"{platform}/{card_type}/{platform_work_id} cached insight"],
        },
    }


def _has_reason(missing_fields: List[Dict[str, Any]], *, reason: str, field: str = "") -> bool:
    for item in missing_fields:
        if not isinstance(item, dict):
            continue
        if item.get("reason") != reason:
            continue
        if field and item.get("field") != field:
            continue
        return True
    return False


def _assert_result(name: str, result: Dict[str, Any], expected_request_id: str) -> Dict[str, Any]:
    works = result.get("works") if isinstance(result.get("works"), list) else []
    checkpoint = result.get("checkpoint") if isinstance(result.get("checkpoint"), dict) else {}
    missing_fields = result.get("missing_fields") if isinstance(result.get("missing_fields"), list) else []
    fallback_trace = result.get("fallback_trace") if isinstance(result.get("fallback_trace"), list) else []
    ok = (
        len(works) == 200
        and int(checkpoint.get("max_items") or 0) == 200
        and result.get("request_id") == expected_request_id
        and not _has_reason(missing_fields, reason="empty_collection", field="works")
        and isinstance(fallback_trace, list)
    )
    return {
        "name": name,
        "ok": ok,
        "works": len(works),
        "max_items": checkpoint.get("max_items"),
        "cursor_mode": checkpoint.get("cursor_mode"),
        "request_id": result.get("request_id"),
        "fallback_steps": len(fallback_trace),
        "summary": result.get("summary"),
    }


def _assert_standard_run_contract(name: str, result: Dict[str, Any], progress_events: List[Dict[str, Any]]) -> Dict[str, Any]:
    card_write = result.get("card_write") if isinstance(result.get("card_write"), dict) else {}
    author_card = card_write.get("author") if isinstance(card_write.get("author"), dict) else {}
    works_card = card_write.get("works") if isinstance(card_write.get("works"), dict) else {}
    output_persist = result.get("output_persist") if isinstance(result.get("output_persist"), dict) else {}
    required_fields_present = all(key in result for key in ("missing_fields", "fallback_trace", "request_id", "card_write", "output_persist"))
    event_kinds = {str(item.get("event") or "") for item in progress_events if isinstance(item, dict)}
    ok = (
        bool(author_card.get("ok"))
        and int(works_card.get("count") or 0) > 0
        and bool(output_persist.get("ok"))
        and required_fields_present
        and {"started", "progress", "done"}.issubset(event_kinds)
    )
    return {
        "name": name,
        "ok": ok,
        "author_card_ok": bool(author_card.get("ok")),
        "work_cards_count": int(works_card.get("count") or 0),
        "output_persist_ok": bool(output_persist.get("ok")),
        "required_fields_present": required_fields_present,
        "progress_events": sorted(event_kinds),
    }


def _assert_work_analysis_cache_reuse(
    name: str,
    first_result: Dict[str, Any],
    second_result: Dict[str, Any],
    build_calls_before_second: int,
    build_calls_after_second: int,
) -> Dict[str, Any]:
    first_bundle = first_result.get("work_analysis") if isinstance(first_result.get("work_analysis"), dict) else {}
    second_bundle = second_result.get("work_analysis") if isinstance(second_result.get("work_analysis"), dict) else {}
    first_stats = first_bundle.get("stats") if isinstance(first_bundle.get("stats"), dict) else {}
    second_stats = second_bundle.get("stats") if isinstance(second_bundle.get("stats"), dict) else {}
    ok = (
        int(first_stats.get("queued_count") or 0) > 0
        and int(first_stats.get("cache_hit_count") or 0) == 0
        and int(second_stats.get("cache_hit_count") or 0) > 0
        and int(second_stats.get("queued_count") or 0) == 0
        and build_calls_before_second == build_calls_after_second
    )
    return {
        "name": name,
        "ok": ok,
        "first_queued": first_stats.get("queued_count"),
        "first_cache_hit": first_stats.get("cache_hit_count"),
        "second_queued": second_stats.get("queued_count"),
        "second_cache_hit": second_stats.get("cache_hit_count"),
        "build_calls_before_second": build_calls_before_second,
        "build_calls_after_second": build_calls_after_second,
    }


def _assert_semantic_empty_result(name: str, result: Dict[str, Any], expected_request_id: str) -> Dict[str, Any]:
    works = result.get("works") if isinstance(result.get("works"), list) else []
    missing_fields = result.get("missing_fields") if isinstance(result.get("missing_fields"), list) else []
    fallback_trace = result.get("fallback_trace") if isinstance(result.get("fallback_trace"), list) else []
    has_empty_collection = _has_reason(missing_fields, reason="empty_collection", field="works")
    has_empty_author_id = _has_reason(missing_fields, reason="empty_value", field="platform_author_id")
    has_empty_nickname = _has_reason(missing_fields, reason="empty_value", field="nickname")
    fallback_has_failure = any(isinstance(step, dict) and not step.get("ok", True) for step in fallback_trace)
    ok = (
        len(works) == 0
        and has_empty_collection
        and has_empty_author_id
        and has_empty_nickname
        and fallback_has_failure
        and result.get("request_id") == expected_request_id
    )
    return {
        "name": name,
        "ok": ok,
        "works": len(works),
        "request_id": result.get("request_id"),
        "fallback_steps": len(fallback_trace),
        "has_empty_collection": has_empty_collection,
        "has_empty_author_id": has_empty_author_id,
        "has_empty_nickname": has_empty_nickname,
    }


def main() -> None:
    author_analysis_module = importlib.import_module("scripts.author_home.orchestrator.run_author_analysis")
    work_artifact_module = importlib.import_module("scripts.author_home.orchestrator.work_analysis_artifacts")
    original_analysis = author_analysis_module.run_prompt_first_author_analysis
    original_work_builder = work_artifact_module.build_card_analysis_artifact
    author_analysis_module.run_prompt_first_author_analysis = _fake_analysis
    work_artifact_module.build_card_analysis_artifact = _fake_work_card_analysis
    WORK_ANALYSIS_BUILD_CALLS["count"] = 0
    try:
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
        dy_empty = run_author_home_analysis(
            platform="douyin",
            input_value="mock://douyin-empty",
            base_url="https://api.tikomni.com",
            token="mock-token",
            timeout_ms=1000,
            write_card=False,
            collector_override=_mock_douyin_empty_collector,
        )

        with tempfile.TemporaryDirectory(prefix="tikomni-author-home-") as tmp:
            tmp_path = Path(tmp)
            card_root = tmp_path / "cards"
            output_root = tmp_path / "output"
            card_root.mkdir(parents=True, exist_ok=True)
            output_root.mkdir(parents=True, exist_ok=True)
            storage_config = {
                "storage_routes": {
                    "default": {
                        "root_dir": str(output_root),
                        "runs_dir": "_runs",
                        "results_dir": "results",
                        "errors_dir": "_errors",
                    }
                }
            }
            reporter = build_progress_reporter(
                workflow="regression_author_home_componentized",
                platform="douyin",
                content_kind="author_home",
                input_value="mock://douyin-standard",
            )
            stderr_buffer = io.StringIO()
            with contextlib.redirect_stderr(stderr_buffer):
                standard = run_author_home_analysis(
                    platform="douyin",
                    input_value="mock://douyin-standard",
                    base_url="https://api.tikomni.com",
                    token="mock-token",
                    timeout_ms=1000,
                    write_card=True,
                    card_root=str(card_root),
                    storage_config=storage_config,
                    collector_override=_mock_douyin_collector,
                    progress=reporter,
                    max_items=5,
                    asr_batch_size=5,
                )
                standard = _ensure_output_persist(
                    result=standard,
                    input_value="mock://douyin-standard",
                    storage_config=storage_config,
                    persist_output=True,
                )
                build_calls_before_second = WORK_ANALYSIS_BUILD_CALLS["count"]
                standard_cached = run_author_home_analysis(
                    platform="douyin",
                    input_value="mock://douyin-standard",
                    base_url="https://api.tikomni.com",
                    token="mock-token",
                    timeout_ms=1000,
                    write_card=True,
                    card_root=str(card_root),
                    storage_config=storage_config,
                    collector_override=_mock_douyin_collector,
                    progress=reporter,
                    max_items=5,
                    asr_batch_size=5,
                )
                build_calls_after_second = WORK_ANALYSIS_BUILD_CALLS["count"]
            progress_events = []
            for line in stderr_buffer.getvalue().splitlines():
                line = line.strip()
                if not line:
                    continue
                try:
                    payload = json.loads(line)
                except Exception:
                    continue
                if payload.get("channel") == "tikomni_progress":
                    progress_events.append(payload)

        checks = [
            _assert_result("douyin", dy, "mock-dy-request"),
            _assert_result("xiaohongshu", xhs, "mock-xhs-request"),
            _assert_semantic_empty_result("douyin-empty", dy_empty, "mock-empty-request"),
            _assert_standard_run_contract("douyin-standard", standard, progress_events),
            _assert_work_analysis_cache_reuse(
                "douyin-standard-cache",
                standard,
                standard_cached,
                build_calls_before_second,
                build_calls_after_second,
            ),
        ]
        output = {
            "ok": all(item.get("ok") for item in checks),
            "checks": checks,
        }
    finally:
        author_analysis_module.run_prompt_first_author_analysis = original_analysis
        work_artifact_module.build_card_analysis_artifact = original_work_builder

    print(json.dumps(output, ensure_ascii=False, indent=2))
    raise SystemExit(0 if output["ok"] else 1)


if __name__ == "__main__":
    main()
