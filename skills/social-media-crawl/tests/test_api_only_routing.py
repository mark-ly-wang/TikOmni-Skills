#!/usr/bin/env python3

from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parents[1]
if str(SKILL_ROOT) not in sys.path:
    sys.path.insert(0, str(SKILL_ROOT))

from scripts.core.call_tikomni_api import call_endpoint
from scripts.core.resolve_api_endpoint import resolve_endpoint


class ApiOnlyRoutingTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.operations = json.loads(
            (SKILL_ROOT / "references" / "api-catalog" / "operations.json").read_text(encoding="utf-8")
        )

    def test_error_report_paths_are_not_in_catalog(self) -> None:
        paths = {str(operation["path"]) for operation in self.operations}
        wrong_paths = {
            "/api/u1/v1/health",
            "/api/u1/v1/douyin/hot_search_list",
            "/api/u1/v1/Douyin/douyin_hot_search_list",
            "/api/u1/v1/wechat/article",
            "/api/u1/v1/wechat/fetch_article",
            "/api/u1/v1/account/info",
            "/api/u1/v1/quote/list",
            "/api/u1/v1/demo/wechat/article",
        }
        self.assertTrue(wrong_paths.isdisjoint(paths))
        self.assertIn("/api/u1/v1/demo/douyin/web/fetch_one_video", paths)

    def test_douyin_hot_search_resolves_real_endpoint(self) -> None:
        resolved = resolve_endpoint(platform="douyin", capability="hot_search")
        self.assertTrue(resolved["ok"])
        self.assertEqual(
            resolved["recommended"]["endpoint_id"],
            "douyin.hot_search.app_v3.fetch_hot_search_list",
        )
        self.assertEqual(
            resolved["recommended"]["path"],
            "/api/u1/v1/douyin/app/v3/fetch_hot_search_list",
        )
        self.assertTrue(resolved["alternatives"])

    def test_wechat_mp_and_channels_are_split(self) -> None:
        mp = resolve_endpoint(platform="wechat_mp", capability="article_detail")
        self.assertTrue(mp["ok"])
        self.assertEqual(mp["platform"], "wechat_mp")
        self.assertEqual(mp["recommended"]["path"], "/api/u1/v1/wechat_mp/web/fetch_mp_article_detail_json")

        channels = resolve_endpoint(platform="wechat_channels", capability="video_detail")
        self.assertTrue(channels["ok"])
        self.assertEqual(channels["platform"], "wechat_channels")
        self.assertEqual(channels["recommended"]["path"], "/api/u1/v1/wechat_channels/fetch_video_detail")

    def test_ambiguous_wechat_returns_suggestions_not_guess(self) -> None:
        resolved = resolve_endpoint(platform="wechat", capability="article_detail")
        self.assertFalse(resolved["ok"])
        self.assertEqual(resolved["code"], "ENDPOINT_NOT_RESOLVED")
        self.assertIn({"platform": "wechat_mp", "capability": "article_detail"}, resolved["suggestions"])

    def test_caller_rejects_arbitrary_routing_params(self) -> None:
        result = call_endpoint(
            endpoint_id="douyin.hot_search.app_v3.fetch_hot_search_list",
            params={"path": "/api/u1/v1/douyin/hot_search_list"},
            dry_run=True,
        )
        self.assertFalse(result["ok"])
        self.assertEqual(result["code"], "RESERVED_PARAM_KEY")

        result = call_endpoint(
            endpoint_id="douyin.hot_search.app_v3.fetch_hot_search_list",
            params={"method": "POST"},
            dry_run=True,
        )
        self.assertFalse(result["ok"])
        self.assertEqual(result["code"], "RESERVED_PARAM_KEY")

    def test_caller_allows_declared_path_payload_field(self) -> None:
        result = call_endpoint(
            endpoint_id="xiaohongshu.search.web.sign",
            params={
                "path": "/api/sns/web/v1/search/notes",
                "cookie": "web_session=test",
                "data": {"keyword": "test"},
            },
            dry_run=True,
        )
        self.assertTrue(result["ok"])
        self.assertEqual(result["request"]["path"], "/api/u1/v1/xiaohongshu/web/sign")
        self.assertEqual(result["request"]["body"]["path"], "/api/sns/web/v1/search/notes")

    def test_caller_rejects_unknown_endpoint_id(self) -> None:
        result = call_endpoint(
            endpoint_id="douyin.hot_search.app_v3.not_real",
            params={},
            dry_run=True,
        )
        self.assertFalse(result["ok"])
        self.assertEqual(result["code"], "UNKNOWN_ENDPOINT_ID")

    def test_u2_u3_stay_in_same_catalog(self) -> None:
        endpoint_ids = {str(operation["endpoint_id"]) for operation in self.operations}
        self.assertIn("u2.transcription.service.transcription", endpoint_ids)
        self.assertIn("u3.media_upload.service.uploads", endpoint_ids)

    def test_plain_english_intent_does_not_match_single_letter_x_alias(self) -> None:
        resolved = resolve_endpoint(intent="extract comments from this post")
        self.assertFalse(resolved["ok"])
        self.assertEqual(resolved["capability"], "comments")
        self.assertEqual(resolved["platform"], "")

    def test_search_operations_are_not_classified_as_comments(self) -> None:
        by_id = {str(operation["endpoint_id"]): operation for operation in self.operations}
        for endpoint_id in {
            "xiaohongshu.search.app_v2.search_notes",
            "xiaohongshu.search.app.search_notes",
            "xiaohongshu.search.web.search_notes",
            "xiaohongshu.search.web.search_notes_v3",
        }:
            self.assertIn(endpoint_id, by_id)
            self.assertEqual(by_id[endpoint_id]["capability"], "search")
