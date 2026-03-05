#!/usr/bin/env python3
"""Collectors for author homepage profile + paginated posts."""

from __future__ import annotations

from typing import Any, Dict, List, Optional, Tuple
from urllib.parse import parse_qs, urlparse

from scripts.core.extract_pipeline import build_api_trace
from scripts.core.tikomni_common import call_json_api, deep_find_first


def _pick_text(payload: Any, keys: List[str]) -> str:
    hit = deep_find_first(payload, keys)
    if hit is None:
        return ""
    if isinstance(hit, str):
        return hit.strip()
    return str(hit).strip()


def _pick_int(payload: Any, keys: List[str], default: int = 0) -> int:
    hit = deep_find_first(payload, keys)
    if hit is None:
        return default
    try:
        if isinstance(hit, (int, float)):
            return int(hit)
        return int(float(str(hit).replace(",", "")))
    except Exception:
        return default


def _pick_list(payload: Any, keys: List[str]) -> List[Any]:
    hit = deep_find_first(payload, keys)
    if isinstance(hit, list):
        return hit
    return []


def _guess_douyin_sec_user_id(input_value: str) -> str:
    value = (input_value or "").strip()
    if not value:
        return ""
    if "sec_uid=" in value:
        query = parse_qs(urlparse(value).query)
        sec = query.get("sec_uid") or query.get("sec_user_id")
        if sec and sec[0]:
            return sec[0]
    if value.startswith("MS4wLjAB") or value.startswith("MS4wLjA"):
        return value
    return ""


def _guess_xhs_ids(input_value: str) -> Tuple[str, str]:
    value = (input_value or "").strip()
    if not value:
        return "", ""
    parsed = urlparse(value)
    if parsed.query:
        query = parse_qs(parsed.query)
        uid = (query.get("user_id") or query.get("userid") or [""])[0]
        xsec = (query.get("xsec_token") or [""])[0]
        if uid:
            return uid, xsec
    if "/user/profile/" in value:
        tail = value.split("/user/profile/", 1)[-1].split("?", 1)[0].split("/", 1)[0].strip()
        if tail:
            return tail, ""
    return "", ""


def collect_douyin_author_home_raw(
    *,
    input_value: str,
    base_url: str,
    token: str,
    timeout_ms: int,
    page_size: int,
    pages_max: int,
    max_items: int,
) -> Dict[str, Any]:
    trace: List[Dict[str, Any]] = []
    sec_user_id = _guess_douyin_sec_user_id(input_value)
    resolve_resp: Optional[Dict[str, Any]] = None

    if not sec_user_id:
        resolve_resp = call_json_api(
            base_url=base_url,
            path="/api/u1/v1/douyin/web/get_sec_user_id",
            token=token,
            method="GET",
            timeout_ms=timeout_ms,
            params={"url": input_value, "share_url": input_value},
        )
        trace.append(build_api_trace(step="douyin.resolve_sec_user_id", endpoint="/api/u1/v1/douyin/web/get_sec_user_id", response=resolve_resp))
        sec_user_id = _pick_text(resolve_resp.get("data"), ["sec_user_id", "sec_uid", "secUserId"])

    profile_resp = call_json_api(
        base_url=base_url,
        path="/api/u1/v1/douyin/app/v3/handler_user_profile",
        token=token,
        method="GET",
        timeout_ms=timeout_ms,
        params={"sec_user_id": sec_user_id},
    )
    trace.append(build_api_trace(step="douyin.profile", endpoint="/api/u1/v1/douyin/app/v3/handler_user_profile", response=profile_resp))

    works: List[Dict[str, Any]] = []
    seen_ids = set()
    cursor = 0
    has_more = True
    page = 0
    pagination_trace: List[Dict[str, Any]] = []

    while has_more and page < max(pages_max, 1) and len(works) < max_items:
        page += 1
        posts_resp = call_json_api(
            base_url=base_url,
            path="/api/u1/v1/douyin/app/v3/fetch_user_post_videos",
            token=token,
            method="GET",
            timeout_ms=timeout_ms,
            params={
                "sec_user_id": sec_user_id,
                "count": min(max(page_size, 1), 20),
                "max_cursor": cursor,
                "sort_type": 0,
            },
        )
        trace.append(
            build_api_trace(
                step="douyin.posts_page",
                endpoint="/api/u1/v1/douyin/app/v3/fetch_user_post_videos",
                response=posts_resp,
                extra={"page": page, "cursor": cursor, "sort_type": 0},
            )
        )
        data = posts_resp.get("data")
        page_items = _pick_list(data, ["aweme_list", "items", "list", "data"])
        next_cursor = _pick_int(data, ["max_cursor", "cursor", "next_cursor"], default=0)
        has_more_flag = _pick_int(data, ["has_more", "hasMore"], default=0)
        pagination_trace.append(
            {
                "page": page,
                "cursor_in": cursor,
                "cursor_out": next_cursor,
                "has_more": has_more_flag,
                "items": len(page_items),
            }
        )

        for item in page_items:
            if not isinstance(item, dict):
                continue
            work_id = _pick_text(item, ["aweme_id", "item_id", "id"])
            dedupe_key = work_id or f"p{page}-i{len(works)}"
            if dedupe_key in seen_ids:
                continue
            seen_ids.add(dedupe_key)
            works.append(item)
            if len(works) >= max_items:
                break

        has_more = bool(has_more_flag == 1 and next_cursor != cursor)
        cursor = next_cursor

    request_id = None
    for resp in [resolve_resp, profile_resp]:
        if isinstance(resp, dict) and resp.get("request_id"):
            request_id = resp.get("request_id")
            break

    return {
        "platform": "douyin",
        "resolved_author_id": sec_user_id,
        "profile_response": profile_resp,
        "works": works,
        "pagination": {
            "sort": "latest",
            "sort_type": 0,
            "cursor_mode": "max_cursor",
            "pages": pagination_trace,
            "total_collected": len(works),
            "max_items": max_items,
        },
        "extract_trace": trace,
        "request_id": request_id,
    }


def collect_xhs_author_home_raw(
    *,
    input_value: str,
    base_url: str,
    token: str,
    timeout_ms: int,
    page_size: int,
    pages_max: int,
    max_items: int,
) -> Dict[str, Any]:
    trace: List[Dict[str, Any]] = []
    user_id, xsec_token = _guess_xhs_ids(input_value)
    resolve_resp: Optional[Dict[str, Any]] = None

    if not user_id:
        resolve_resp = call_json_api(
            base_url=base_url,
            path="/api/u1/v1/xiaohongshu/app/get_user_id_and_xsec_token",
            token=token,
            method="GET",
            timeout_ms=timeout_ms,
            params={"share_url": input_value, "url": input_value},
        )
        trace.append(
            build_api_trace(
                step="xhs.resolve_user_id",
                endpoint="/api/u1/v1/xiaohongshu/app/get_user_id_and_xsec_token",
                response=resolve_resp,
            )
        )
        data = resolve_resp.get("data")
        user_id = _pick_text(data, ["user_id", "userid", "uid"])
        if not xsec_token:
            xsec_token = _pick_text(data, ["xsec_token", "xsecToken"])

    profile_resp = call_json_api(
        base_url=base_url,
        path="/api/u1/v1/xiaohongshu/web_v2/fetch_user_info_app",
        token=token,
        method="GET",
        timeout_ms=timeout_ms,
        params={"user_id": user_id, "xsec_token": xsec_token or None},
    )
    trace.append(build_api_trace(step="xhs.profile.primary", endpoint="/api/u1/v1/xiaohongshu/web_v2/fetch_user_info_app", response=profile_resp))

    if not profile_resp.get("ok"):
        fallback_profile = call_json_api(
            base_url=base_url,
            path="/api/u1/v1/xiaohongshu/app/get_user_info",
            token=token,
            method="GET",
            timeout_ms=timeout_ms,
            params={"user_id": user_id},
        )
        trace.append(build_api_trace(step="xhs.profile.fallback", endpoint="/api/u1/v1/xiaohongshu/app/get_user_info", response=fallback_profile))
        profile_resp = fallback_profile

    works: List[Dict[str, Any]] = []
    seen_ids = set()
    cursor: Any = ""
    has_more = True
    page = 0
    pagination_trace: List[Dict[str, Any]] = []

    while has_more and page < max(pages_max, 1) and len(works) < max_items:
        page += 1
        posts_resp = call_json_api(
            base_url=base_url,
            path="/api/u1/v1/xiaohongshu/web_v2/fetch_home_notes_app",
            token=token,
            method="GET",
            timeout_ms=timeout_ms,
            params={
                "user_id": user_id,
                "cursor": cursor or None,
                "num": min(max(page_size, 1), 20),
                "xsec_token": xsec_token or None,
            },
        )
        trace.append(build_api_trace(step="xhs.posts.primary", endpoint="/api/u1/v1/xiaohongshu/web_v2/fetch_home_notes_app", response=posts_resp, extra={"page": page, "cursor": cursor}))

        if not posts_resp.get("ok"):
            fallback_posts = call_json_api(
                base_url=base_url,
                path="/api/u1/v1/xiaohongshu/app/get_user_notes",
                token=token,
                method="GET",
                timeout_ms=timeout_ms,
                params={"user_id": user_id, "cursor": cursor or None, "num": min(max(page_size, 1), 20)},
            )
            trace.append(build_api_trace(step="xhs.posts.fallback", endpoint="/api/u1/v1/xiaohongshu/app/get_user_notes", response=fallback_posts, extra={"page": page, "cursor": cursor}))
            posts_resp = fallback_posts

        data = posts_resp.get("data")
        page_items = _pick_list(data, ["notes", "note_list", "items", "list"])
        next_cursor = _pick_text(data, ["cursor", "next_cursor", "last_cursor", "last_note_id"])
        has_more_flag = _pick_int(data, ["has_more", "hasMore"], default=0)
        pagination_trace.append(
            {
                "page": page,
                "cursor_in": cursor,
                "cursor_out": next_cursor,
                "has_more": has_more_flag,
                "items": len(page_items),
            }
        )

        for item in page_items:
            if not isinstance(item, dict):
                continue
            work_id = _pick_text(item, ["note_id", "id", "item_id"])
            dedupe_key = work_id or f"p{page}-i{len(works)}"
            if dedupe_key in seen_ids:
                continue
            seen_ids.add(dedupe_key)
            works.append(item)
            if len(works) >= max_items:
                break

        has_more = bool(has_more_flag == 1 and next_cursor and str(next_cursor) != str(cursor))
        cursor = next_cursor

    request_id = None
    for resp in [resolve_resp, profile_resp]:
        if isinstance(resp, dict) and resp.get("request_id"):
            request_id = resp.get("request_id")
            break

    return {
        "platform": "xiaohongshu",
        "resolved_author_id": user_id,
        "resolved_xsec_token": xsec_token,
        "profile_response": profile_resp,
        "works": works,
        "pagination": {
            "sort": "latest",
            "sort_type": "latest",
            "cursor_mode": "cursor",
            "pages": pagination_trace,
            "total_collected": len(works),
            "max_items": max_items,
        },
        "extract_trace": trace,
        "request_id": request_id,
    }
