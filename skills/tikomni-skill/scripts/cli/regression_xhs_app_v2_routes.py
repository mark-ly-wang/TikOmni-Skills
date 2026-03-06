#!/usr/bin/env python3

if __package__ in {None, ""}:
    import sys
    from pathlib import Path

    _self = Path(__file__).resolve()
    for _parent in _self.parents:
        if (_parent / "scripts" / "core" / "bootstrap_env.py").is_file():
            sys.path.insert(0, str(_parent))
            break

"""Regression checks for Xiaohongshu APP V2 route priority."""

import importlib
import json
from typing import Any, Dict, List


def _note_success_response(note_id: str, *, request_id: str) -> Dict[str, Any]:
    return {
        "ok": True,
        "status_code": 200,
        "request_id": request_id,
        "data": {
            "note_id": note_id,
            "title": "APP V2 标题",
            "desc": "APP V2 正文",
            "user": {"nickname": "作者A"},
            "video": {"master_url": "https://example.com/video.mp4"},
            "liked_count": 123,
            "comment_count": 45,
        },
    }


def _note_sparse_response(note_id: str, *, request_id: str) -> Dict[str, Any]:
    return {
        "ok": True,
        "status_code": 200,
        "request_id": request_id,
        "data": {
            "note_id": note_id,
        },
    }


def _response(*, request_id: str, data: Any, ok: bool = True, error_reason: str = "") -> Dict[str, Any]:
    return {
        "ok": ok,
        "status_code": 200 if ok else 500,
        "request_id": request_id,
        "error_reason": error_reason or None,
        "data": data,
    }


def _check_note_prefers_app_v2(note_module) -> Dict[str, Any]:
    calls: List[str] = []

    def _fake_call_json_api(**kwargs: Any) -> Dict[str, Any]:
        path = kwargs.get("path")
        calls.append(str(path))
        if path == note_module.APP_V2_VIDEO_ENDPOINT:
            return _note_success_response("note_app_v2_ok", request_id="req-note-app-v2")
        raise AssertionError(f"unexpected endpoint:{path}")

    original = note_module.call_json_api
    note_module.call_json_api = _fake_call_json_api
    try:
        result = note_module._fetch_note_info(
            base_url="https://api.tikomni.com",
            token="mock-token",
            timeout_ms=1000,
            source_input={"share_text": "https://www.xiaohongshu.com/explore/note_app_v2_ok", "note_id": "note_app_v2_ok"},
        )
    finally:
        note_module.call_json_api = original

    completeness = result.get("_field_completeness") if isinstance(result.get("_field_completeness"), dict) else {}
    ok = (
        result.get("_route_label") == "app_v2_video"
        and len(calls) == 1
        and bool(completeness.get("core_ready"))
    )
    return {
        "name": "note_prefers_app_v2",
        "ok": ok,
        "calls": calls,
        "chosen_route": result.get("_route_label"),
        "core_ready": completeness.get("core_ready"),
    }


def _check_note_falls_back_to_app_v1(note_module) -> Dict[str, Any]:
    calls: List[str] = []

    def _fake_call_json_api(**kwargs: Any) -> Dict[str, Any]:
        path = kwargs.get("path")
        calls.append(str(path))
        if path in {
            note_module.APP_V2_VIDEO_ENDPOINT,
            note_module.APP_V2_IMAGE_ENDPOINT,
            note_module.APP_V2_MIXED_ENDPOINT,
        }:
            return _note_sparse_response("note_need_app_v1", request_id=f"req-{path.split('/')[-1]}")
        if path == note_module.APP_V1_ENDPOINT:
            return _note_success_response("note_need_app_v1", request_id="req-note-app-v1")
        raise AssertionError(f"unexpected endpoint:{path}")

    original = note_module.call_json_api
    note_module.call_json_api = _fake_call_json_api
    try:
        result = note_module._fetch_note_info(
            base_url="https://api.tikomni.com",
            token="mock-token",
            timeout_ms=1000,
            source_input={"share_text": "https://www.xiaohongshu.com/explore/note_need_app_v1", "note_id": "note_need_app_v1"},
        )
    finally:
        note_module.call_json_api = original

    attempts = result.get("_attempts") if isinstance(result.get("_attempts"), list) else []
    ok = (
        result.get("_route_label") == "app_v1"
        and len(attempts) == 4
        and all(
            isinstance(item, dict) and isinstance((item.get("response") or {}).get("_field_completeness"), dict)
            for item in attempts
        )
    )
    return {
        "name": "note_falls_back_to_app_v1",
        "ok": ok,
        "attempt_labels": [item.get("label") for item in attempts if isinstance(item, dict)],
        "chosen_route": result.get("_route_label"),
    }


def _check_home_prefers_app_v2(collector_module) -> Dict[str, Any]:
    calls: List[str] = []

    def _fake_call_json_api(**kwargs: Any) -> Dict[str, Any]:
        path = str(kwargs.get("path"))
        calls.append(path)
        if path.endswith("app_v2/get_user_info"):
            return _response(
                request_id="req-home-profile-app-v2",
                data={"user_id": "mock_uid", "nickname": "作者主页", "fans": 12, "note_count": 1},
            )
        if path.endswith("app_v2/get_user_posted_notes"):
            return _response(
                request_id="req-home-posts-app-v2",
                data={"notes": [{"note_id": "n1", "title": "作品1"}], "cursor": "c1", "has_more": 0},
            )
        raise AssertionError(f"unexpected endpoint:{path}")

    original = collector_module.call_json_api
    collector_module.call_json_api = _fake_call_json_api
    try:
        result = collector_module.collect_xhs_author_home_raw(
            input_value="https://www.xiaohongshu.com/user/profile/mock_uid",
            base_url="https://api.tikomni.com",
            token="mock-token",
            timeout_ms=1000,
            page_size=20,
            pages_max=1,
            max_items=20,
            progress=None,
        )
    finally:
        collector_module.call_json_api = original

    extract_trace = result.get("extract_trace") if isinstance(result.get("extract_trace"), list) else []
    profile_route = next((item for item in extract_trace if isinstance(item, dict) and item.get("step") == "xhs.profile.route_decision"), {})
    posts_route = next((item for item in extract_trace if isinstance(item, dict) and item.get("step") == "xhs.posts.route_decision"), {})
    ok = (
        profile_route.get("chosen_route") == "app_v2_primary"
        and posts_route.get("chosen_route") == "app_v2_primary"
        and ((result.get("pagination") or {}).get("pages") or [{}])[0].get("route_label") == "app_v2_primary"
    )
    return {
        "name": "home_prefers_app_v2",
        "ok": ok,
        "calls": calls,
        "profile_route": profile_route.get("chosen_route"),
        "posts_route": posts_route.get("chosen_route"),
    }


def _check_home_falls_back_to_web_v2(collector_module) -> Dict[str, Any]:
    calls: List[str] = []

    def _fake_call_json_api(**kwargs: Any) -> Dict[str, Any]:
        path = str(kwargs.get("path"))
        calls.append(path)
        if path.endswith("app_v2/get_user_info"):
            return _response(request_id="req-profile-app-v2-fail", data={}, ok=False, error_reason="app_v2_failed")
        if path.endswith("web_v2/fetch_user_info_app"):
            return _response(
                request_id="req-profile-web-v2",
                data={"user_id": "mock_uid", "nickname": "作者主页", "fans": 12, "note_count": 1},
            )
        if path.endswith("app_v2/get_user_posted_notes"):
            return _response(request_id="req-posts-app-v2-fail", data={}, ok=False, error_reason="app_v2_failed")
        if path.endswith("web_v2/fetch_home_notes_app"):
            return _response(
                request_id="req-posts-web-v2",
                data={"notes": [{"note_id": "n1", "title": "作品1"}], "cursor": "c1", "has_more": 0},
            )
        raise AssertionError(f"unexpected endpoint:{path}")

    original = collector_module.call_json_api
    collector_module.call_json_api = _fake_call_json_api
    try:
        result = collector_module.collect_xhs_author_home_raw(
            input_value="https://www.xiaohongshu.com/user/profile/mock_uid",
            base_url="https://api.tikomni.com",
            token="mock-token",
            timeout_ms=1000,
            page_size=20,
            pages_max=1,
            max_items=20,
            progress=None,
        )
    finally:
        collector_module.call_json_api = original

    extract_trace = result.get("extract_trace") if isinstance(result.get("extract_trace"), list) else []
    profile_route = next((item for item in extract_trace if isinstance(item, dict) and item.get("step") == "xhs.profile.route_decision"), {})
    posts_route = next((item for item in extract_trace if isinstance(item, dict) and item.get("step") == "xhs.posts.route_decision"), {})
    fallback_steps = [
        item for item in extract_trace
        if isinstance(item, dict) and str(item.get("fallback_trigger_reason") or "").strip()
    ]
    ok = (
        profile_route.get("chosen_route") == "web_v2_secondary"
        and posts_route.get("chosen_route") == "web_v2_secondary"
        and len(fallback_steps) >= 2
    )
    return {
        "name": "home_falls_back_to_web_v2",
        "ok": ok,
        "calls": calls,
        "profile_route": profile_route.get("chosen_route"),
        "posts_route": posts_route.get("chosen_route"),
        "fallback_steps": len(fallback_steps),
    }


def main() -> None:
    note_module = importlib.import_module("scripts.platform.xiaohongshu.run_xiaohongshu_extract")
    collector_module = importlib.import_module("scripts.author_home.collectors.homepage_collectors")
    checks = [
        _check_note_prefers_app_v2(note_module),
        _check_note_falls_back_to_app_v1(note_module),
        _check_home_prefers_app_v2(collector_module),
        _check_home_falls_back_to_web_v2(collector_module),
    ]
    output = {
        "ok": all(item.get("ok") for item in checks),
        "checks": checks,
    }
    print(json.dumps(output, ensure_ascii=False, indent=2))
    raise SystemExit(0 if output.get("ok") else 1)


if __name__ == "__main__":
    main()
