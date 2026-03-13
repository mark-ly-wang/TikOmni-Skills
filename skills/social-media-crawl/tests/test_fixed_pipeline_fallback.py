#!/usr/bin/env python3

from __future__ import annotations

import os
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

SKILL_ROOT = Path(__file__).resolve().parents[1]
if str(SKILL_ROOT) not in sys.path:
    sys.path.insert(0, str(SKILL_ROOT))

from scripts.pipelines import homepage_collectors
from scripts.pipelines import run_xiaohongshu_single_work


class FixedPipelineFallbackTest(unittest.TestCase):
    def test_xhs_single_route_plan_respects_version_priority_and_cookie_gate(self) -> None:
        source_input = {
            "share_text": (
                "https://www.xiaohongshu.com/discovery/item/"
                "6995700a000000000a02ef2d?xsec_token=token123"
            ),
            "note_id": "6995700a000000000a02ef2d",
        }
        with patch.dict(os.environ, {}, clear=False):
            routes = run_xiaohongshu_single_work._build_note_fetch_routes(source_input)

        self.assertEqual(
            [route["route_label"] for route in routes],
            [
                "app_v2_video",
                "app_v2_image",
                "app_v2_mixed",
                "app_v1_v2",
                "app_v1",
                "web_v2_v3",
                "web_v2_v2",
                "web_v1_v7",
                "web_v1_v5",
                "web_v1_v4",
                "web_v1_v2",
            ],
        )
        self.assertEqual(routes[3]["endpoint"], run_xiaohongshu_single_work.APP_V1_V2_ENDPOINT)
        self.assertEqual(routes[7]["endpoint"], run_xiaohongshu_single_work.WEB_V1_V7_ENDPOINT)
        self.assertEqual(routes[8]["method"], "POST")
        self.assertEqual(routes[8]["param_readiness"], "unavailable")
        self.assertEqual(routes[8]["param_reason"], "fallback_requires_cookie")
        self.assertEqual(routes[5]["param_readiness"], "unavailable")
        self.assertEqual(routes[5]["param_reason"], "missing_short_share_url")

    def test_douyin_creator_home_fails_fast_when_author_id_unresolved(self) -> None:
        def fake_call_json_api(*, path: str, **_: object) -> dict:
            self.assertEqual(path, "/api/u1/v1/douyin/web/get_sec_user_id")
            return {
                "ok": False,
                "status_code": 502,
                "request_id": "req-dy-resolver",
                "error_reason": "resolver_failed",
                "data": {},
            }

        with patch.object(homepage_collectors, "call_json_api", side_effect=fake_call_json_api):
            raw = homepage_collectors.collect_douyin_author_home_raw(
                input_value="https://v.douyin.com/test-resolver/",
                base_url="https://api.tikomni.com",
                token="test-token",
                timeout_ms=1000,
                page_size=20,
                pages_max=1,
                max_items=5,
                progress=None,
            )

        self.assertEqual(raw.get("error_reason"), "author_id_unresolved")
        self.assertEqual(raw["stage_status"]["resolver"]["status"], "failed")
        self.assertEqual(raw["stage_status"]["profile"]["status"], "skipped")
        self.assertEqual(raw["stage_status"]["posts"]["status"], "skipped")

    def test_xhs_creator_home_fails_fast_when_author_id_unresolved(self) -> None:
        def fake_call_json_api(*, path: str, **_: object) -> dict:
            self.assertEqual(path, "/api/u1/v1/xiaohongshu/app/get_user_id_and_xsec_token")
            return {
                "ok": False,
                "status_code": 502,
                "request_id": "req-xhs-resolver",
                "error_reason": "resolver_failed",
                "data": {},
            }

        with patch.object(homepage_collectors, "call_json_api", side_effect=fake_call_json_api):
            raw = homepage_collectors.collect_xhs_author_home_raw(
                input_value="https://xhslink.com/m/test-resolver",
                base_url="https://api.tikomni.com",
                token="test-token",
                timeout_ms=1000,
                page_size=20,
                pages_max=1,
                max_items=5,
                progress=None,
            )

        self.assertEqual(raw.get("error_reason"), "author_id_unresolved")
        self.assertEqual(raw["stage_status"]["resolver"]["status"], "failed")
        self.assertEqual(raw["stage_status"]["profile"]["status"], "skipped")
        self.assertEqual(raw["stage_status"]["posts"]["status"], "skipped")

    def test_douyin_posts_records_cookie_required_skip(self) -> None:
        def fake_call_json_api(*, path: str, params: dict | None = None, **_: object) -> dict:
            if path == "/api/u1/v1/douyin/web/get_sec_user_id":
                return {
                    "ok": True,
                    "status_code": 200,
                    "request_id": "req-resolve",
                    "error_reason": None,
                    "data": {"sec_user_id": "MS4wLjABAAAA-test-sec"},
                }
            if path == "/api/u1/v1/douyin/app/v3/handler_user_profile":
                return {
                    "ok": True,
                    "status_code": 200,
                    "request_id": "req-profile",
                    "error_reason": None,
                    "data": {
                        "sec_user_id": "MS4wLjABAAAA-test-sec",
                        "nickname": "tester",
                    },
                }
            if path == "/api/u1/v1/douyin/app/v3/fetch_user_post_videos":
                self.assertEqual(params or {}, {
                    "sec_user_id": "MS4wLjABAAAA-test-sec",
                    "count": 20,
                    "max_cursor": 0,
                    "sort_type": 0,
                })
                return {
                    "ok": False,
                    "status_code": 502,
                    "request_id": "req-posts",
                    "error_reason": "posts_failed",
                    "data": {},
                }
            raise AssertionError(f"unexpected path: {path}")

        with patch.dict(os.environ, {"TIKOMNI_DOUYIN_WEB_COOKIE": ""}, clear=False):
            with patch.object(homepage_collectors, "call_json_api", side_effect=fake_call_json_api):
                raw = homepage_collectors.collect_douyin_author_home_raw(
                    input_value="https://v.douyin.com/test-posts/",
                    base_url="https://api.tikomni.com",
                    token="test-token",
                    timeout_ms=1000,
                    page_size=20,
                    pages_max=1,
                    max_items=5,
                    progress=None,
                )

        attempted_routes = raw["stage_status"]["posts"]["attempted_routes"]
        web_attempt = next(attempt for attempt in attempted_routes if attempt.get("route_label") == "web")
        self.assertTrue(web_attempt.get("skipped"))
        self.assertEqual(web_attempt.get("param_reason"), "fallback_requires_cookie")
        self.assertEqual(raw.get("error_reason"), "posts_all_routes_failed")


if __name__ == "__main__":
    unittest.main()
