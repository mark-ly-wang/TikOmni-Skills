#!/usr/bin/env python3
"""Collectors for author homepage profile + paginated posts."""

from __future__ import annotations

from typing import Any, Dict, List, Optional, Tuple
from urllib.parse import parse_qs, urlparse

from scripts.core.extract_pipeline import build_api_trace
from scripts.core.tikomni_common import call_json_api, deep_find_first


def _to_text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value.strip()
    return str(value).strip()


def _pick_text(payload: Any, keys: List[str]) -> str:
    hit = deep_find_first(payload, keys)
    if hit is None:
        return ""
    return _to_text(hit)


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
    if isinstance(payload, list):
        return payload

    ordered_keys = [str(key) for key in keys if str(key).strip()]

    def _walk(node: Any) -> Optional[List[Any]]:
        if isinstance(node, dict):
            for key in ordered_keys:
                if key not in node:
                    continue
                value = node.get(key)
                if isinstance(value, list):
                    return value
                if isinstance(value, dict):
                    hit = _walk(value)
                    if hit is not None:
                        return hit
            for value in node.values():
                hit = _walk(value)
                if hit is not None:
                    return hit
        elif isinstance(node, list):
            for item in node:
                hit = _walk(item)
                if hit is not None:
                    return hit
        return None

    hit = _walk(payload)
    return hit if isinstance(hit, list) else []


def _looks_like_douyin_sec_user_id(value: str) -> bool:
    return value.startswith("MS4wLjA")


def _extract_douyin_sec_user_id(payload: Any) -> str:
    sec_user_keys = ["sec_user_id", "sec_uid", "secUserId", "secuid"]

    def _walk(node: Any, depth: int = 0) -> str:
        if depth > 8:
            return ""
        if isinstance(node, dict):
            for key in sec_user_keys:
                if key not in node:
                    continue
                candidate = _to_text(node.get(key))
                if candidate:
                    return candidate

            if "data" in node:
                data_node = node.get("data")
                if isinstance(data_node, str):
                    text = _to_text(data_node)
                    if text and _looks_like_douyin_sec_user_id(text):
                        return text
                nested = _walk(data_node, depth + 1)
                if nested:
                    return nested

            for value in node.values():
                nested = _walk(value, depth + 1)
                if nested:
                    return nested
            return ""

        if isinstance(node, list):
            for item in node:
                nested = _walk(item, depth + 1)
                if nested:
                    return nested
            return ""

        if isinstance(node, str):
            text = _to_text(node)
            if text and _looks_like_douyin_sec_user_id(text):
                return text
        return ""

    return _walk(payload, 0)


def _preview(value: Any, max_len: int = 160) -> str:
    text = _to_text(value)
    if not text:
        return ""
    text = " ".join(text.split())
    return text[:max_len]


def _pick_request_id(responses: List[Optional[Dict[str, Any]]], trace: Optional[List[Dict[str, Any]]] = None) -> Optional[str]:
    for response in responses:
        if isinstance(response, dict) and response.get("request_id"):
            return str(response.get("request_id"))

    for step in trace or []:
        if isinstance(step, dict) and step.get("request_id"):
            return str(step.get("request_id"))
    return None


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
    request_id_candidates: List[Optional[Dict[str, Any]]] = []

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
        request_id_candidates.append(resolve_resp)
        resolve_data = resolve_resp.get("data")
        sec_user_id = _extract_douyin_sec_user_id(resolve_data)
        if not sec_user_id:
            trace.append(
                {
                    "step": "douyin.resolve_sec_user_id.unresolved",
                    "endpoint": "/api/u1/v1/douyin/web/get_sec_user_id",
                    "ok": False,
                    "status_code": resolve_resp.get("status_code"),
                    "request_id": resolve_resp.get("request_id"),
                    "error_reason": resolve_resp.get("error_reason"),
                    "resolve_data_type": type(resolve_data).__name__,
                    "resolve_data_keys": list(resolve_data.keys())[:8] if isinstance(resolve_data, dict) else [],
                    "resolve_data_preview": _preview(resolve_data),
                    "input_hint": _preview(input_value, max_len=120),
                }
            )

    profile_resp = call_json_api(
        base_url=base_url,
        path="/api/u1/v1/douyin/app/v3/handler_user_profile",
        token=token,
        method="GET",
        timeout_ms=timeout_ms,
        params={"sec_user_id": sec_user_id},
    )
    trace.append(build_api_trace(step="douyin.profile", endpoint="/api/u1/v1/douyin/app/v3/handler_user_profile", response=profile_resp))
    request_id_candidates.append(profile_resp)

    profile_author_id = _pick_text(profile_resp.get("data"), ["sec_user_id", "sec_uid", "secUserId", "uid", "user_id"])
    resolved_author_id = sec_user_id or profile_author_id
    if not resolved_author_id:
        trace.append(
            {
                "step": "douyin.author_id.unresolved",
                "endpoint": "/api/u1/v1/douyin/app/v3/handler_user_profile",
                "ok": False,
                "status_code": profile_resp.get("status_code"),
                "request_id": profile_resp.get("request_id"),
                "error_reason": profile_resp.get("error_reason"),
                "profile_data_type": type(profile_resp.get("data")).__name__,
                "profile_data_keys": list(profile_resp.get("data").keys())[:8] if isinstance(profile_resp.get("data"), dict) else [],
                "profile_data_preview": _preview(profile_resp.get("data")),
            }
        )

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
        request_id_candidates.append(posts_resp)
        response_payload = posts_resp.get("data")
        page_items = _pick_list(response_payload, ["aweme_list", "items", "list"])
        if not page_items and isinstance(response_payload, dict):
            page_items = _pick_list(response_payload.get("data"), ["aweme_list", "items", "list"])

        data = response_payload
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

    request_id = _pick_request_id(request_id_candidates, trace)

    return {
        "platform": "douyin",
        "resolved_author_id": resolved_author_id,
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
    request_id_candidates: List[Optional[Dict[str, Any]]] = []

    if not user_id:
        resolve_resp = call_json_api(
            base_url=base_url,
            path="/api/u1/v1/xiaohongshu/app/get_user_id_and_xsec_token",
            token=token,
            method="GET",
            timeout_ms=timeout_ms,
            params={"share_link": input_value, "share_url": input_value, "url": input_value},
        )
        trace.append(
            build_api_trace(
                step="xhs.resolve_user_id",
                endpoint="/api/u1/v1/xiaohongshu/app/get_user_id_and_xsec_token",
                response=resolve_resp,
            )
        )
        request_id_candidates.append(resolve_resp)
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
    request_id_candidates.append(profile_resp)

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
        request_id_candidates.append(fallback_profile)

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
        request_id_candidates.append(posts_resp)

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
            request_id_candidates.append(fallback_posts)

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

    request_id = _pick_request_id(request_id_candidates, trace)

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
