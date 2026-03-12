#!/usr/bin/env python3
"""Collectors for author homepage profile + paginated posts."""

from __future__ import annotations

from typing import Any, Dict, List, Optional, Tuple
from urllib.parse import parse_qs, urlparse

from scripts.core.extract_pipeline import build_api_trace
from scripts.core.progress_report import ProgressReporter
from scripts.core.tikomni_common import call_json_api, deep_find_all, deep_find_first
from scripts.pipelines.input_contracts import extract_douyin_sec_uid, extract_xhs_user_id, looks_like_xhs_user_id


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


def _extract_first_url(value: Any) -> str:
    if isinstance(value, str):
        text = value.strip()
        return text if text.startswith("http://") or text.startswith("https://") else ""
    if isinstance(value, list):
        for item in value:
            url = _extract_first_url(item)
            if url:
                return url
        return ""
    if isinstance(value, dict):
        for key in ("url_list", "url", "src", "avatar_url", "cover_url", "image", "images", "default"):
            if key in value:
                url = _extract_first_url(value.get(key))
                if url:
                    return url
        for nested in value.values():
            url = _extract_first_url(nested)
            if url:
                return url
        return ""
    return ""


def _build_field_completeness(fields: Dict[str, bool], *, core_keys: List[str]) -> Dict[str, Any]:
    filled_count = sum(1 for value in fields.values() if value)
    missing_core = [key for key in core_keys if not fields.get(key)]
    return {
        "fields": fields,
        "filled_count": filled_count,
        "total_fields": len(fields),
        "ratio": round(filled_count / max(len(fields), 1), 3),
        "missing_core": missing_core,
        "core_ready": not missing_core,
    }


def _xhs_profile_field_completeness(payload: Any, resolved_author_id: str) -> Dict[str, Any]:
    fields = {
        "platform_author_id": bool(_pick_text(payload, ["user_id", "userid", "uid", "id"]) or resolved_author_id),
        "nickname": bool(_pick_text(payload, ["nickname", "name"])),
        "avatar_url": bool(_extract_first_url(_first_url_candidate(payload, ["image", "avatar", "avatar_url", "images"]))),
        "fans_count": _pick_int(payload, ["fans", "fans_count", "follower_count"], default=0) > 0,
        "works_count": _pick_int(payload, ["notes", "note_count", "works_count"], default=0) > 0,
    }
    return _build_field_completeness(fields, core_keys=["platform_author_id", "nickname"])


def _first_url_candidate(payload: Any, keys: List[str]) -> Any:
    for key in keys:
        for value in deep_find_all(payload, [key]):
            url = _extract_first_url(value)
            if url:
                return value
    return ""


def _pick_first_mapping(items: List[Any]) -> Dict[str, Any]:
    for item in items:
        if isinstance(item, dict):
            return item
    return {}


def _xhs_posts_field_completeness(payload: Any) -> Dict[str, Any]:
    page_items = _pick_list(payload, ["notes", "note_list", "noteList", "items", "list"])
    first_item = _pick_first_mapping(page_items)
    has_more_flag = _pick_int(payload, ["has_more", "hasMore"], default=-1) >= 0
    cursor_hit = bool(_pick_text(payload, ["cursor", "next_cursor", "last_cursor", "last_note_id"]))
    cover_hit = bool(_extract_first_url(_first_url_candidate(first_item, ["cover", "cover_url", "cover_image", "image", "image_url"])))
    share_or_source = bool(_pick_text(first_item, ["share_url", "share_link", "url", "note_url"])) or bool(_pick_text(first_item, ["note_id", "id", "item_id"]))
    interaction_values = [
        _pick_int(first_item, ["liked_count", "like_count", "digg_count"], default=-1),
        _pick_int(first_item, ["comment_count"], default=-1),
        _pick_int(first_item, ["collected_count", "collect_count"], default=-1),
        _pick_int(first_item, ["share_count"], default=-1),
        _pick_int(first_item, ["view_count", "play_count"], default=-1),
    ]
    fields = {
        "items": len(page_items) > 0,
        "platform_work_id": bool(_pick_text(first_item, ["note_id", "id", "item_id"])),
        "title_or_caption": bool(_pick_text(first_item, ["title", "display_title", "desc", "content"])),
        "published_date": bool(_pick_text(first_item, ["publish_time", "time", "create_time"])),
        "base_link_fields": cover_hit or share_or_source,
        "interaction_fields": any(value >= 0 for value in interaction_values),
        "cursor": cursor_hit,
        "has_more_flag": has_more_flag,
        "response_shape": len(page_items) > 0 or cursor_hit or has_more_flag,
    }
    return _build_field_completeness(fields, core_keys=["items", "platform_work_id", "title_or_caption", "published_date"])


def _xhs_route_failure_reason(response: Dict[str, Any]) -> str:
    if response.get("timeout_retry_exhausted"):
        return "primary_timeout_retry_exhausted"
    if response.get("error_reason"):
        return "primary_non_timeout_failure"
    return "primary_unknown_failure"


def _xhs_profile_accept_decision(response: Dict[str, Any], completeness: Dict[str, Any]) -> Dict[str, Any]:
    if not response.get("ok"):
        return {
            "accepted": False,
            "accept_reason": "response_not_ok",
            "fallback_reason": _xhs_route_failure_reason(response),
        }

    missing_core = list(completeness.get("missing_core") or [])
    if missing_core:
        return {
            "accepted": False,
            "accept_reason": "profile_missing_core_fields",
            "fallback_reason": f"profile_missing_core:{','.join(missing_core)}",
        }

    fields = completeness.get("fields") if isinstance(completeness.get("fields"), dict) else {}
    optional_missing = [
        field_name
        for field_name in ("avatar_url", "fans_count", "works_count")
        if not fields.get(field_name)
    ]
    accept_reason = "profile_core_fields_ready"
    if optional_missing:
        accept_reason = f"profile_core_fields_ready_optional_missing:{','.join(optional_missing)}"
    return {
        "accepted": True,
        "accept_reason": accept_reason,
        "fallback_reason": "",
    }


def _xhs_posts_accept_decision(response: Dict[str, Any], completeness: Dict[str, Any]) -> Dict[str, Any]:
    if not response.get("ok"):
        return {
            "accepted": False,
            "accept_reason": "response_not_ok",
            "fallback_reason": _xhs_route_failure_reason(response),
        }

    missing_core = list(completeness.get("missing_core") or [])
    if missing_core:
        return {
            "accepted": False,
            "accept_reason": "posts_missing_core_fields",
            "fallback_reason": f"posts_missing_core:{','.join(missing_core)}",
        }

    fields = completeness.get("fields") if isinstance(completeness.get("fields"), dict) else {}
    if not fields.get("base_link_fields"):
        return {
            "accepted": False,
            "accept_reason": "posts_missing_base_link_fields",
            "fallback_reason": "posts_missing_base_link_fields",
        }
    if not fields.get("interaction_fields"):
        return {
            "accepted": False,
            "accept_reason": "posts_missing_interaction_fields",
            "fallback_reason": "posts_missing_interaction_fields",
        }
    return {
        "accepted": True,
        "accept_reason": "posts_contract_fields_ready",
        "fallback_reason": "",
    }


def _xhs_route_plan(kind: str) -> List[Tuple[str, str, str]]:
    if kind == "profile":
        return [
            ("xhs.profile.app_v2", "/api/u1/v1/xiaohongshu/app_v2/get_user_info", "app_v2"),
            ("xhs.profile.app", "/api/u1/v1/xiaohongshu/app/get_user_info", "app"),
            ("xhs.profile.web_v2", "/api/u1/v1/xiaohongshu/web_v2/fetch_user_info_app", "web_v2"),
        ]
    if kind == "posts":
        return [
            ("xhs.posts.app_v2", "/api/u1/v1/xiaohongshu/app_v2/get_user_posted_notes", "app_v2"),
            ("xhs.posts.app", "/api/u1/v1/xiaohongshu/app/get_user_notes", "app"),
            ("xhs.posts.web_v2", "/api/u1/v1/xiaohongshu/web_v2/fetch_home_notes_app", "web_v2"),
        ]
    raise ValueError(f"unsupported_xhs_route_kind:{kind}")


def _call_xhs_route(
    *,
    base_url: str,
    token: str,
    timeout_ms: int,
    path: str,
    route_label: str,
    params: Dict[str, Any],
    fallback_reason: Optional[str],
    completeness_builder,
) -> Dict[str, Any]:
    response = call_json_api(
        base_url=base_url,
        path=path,
        token=token,
        method="GET",
        timeout_ms=timeout_ms,
        params=params,
    )
    response["_endpoint"] = path
    response["_route_label"] = route_label
    if fallback_reason:
        response["fallback_trigger_reason"] = fallback_reason
    response["_field_completeness"] = completeness_builder(response.get("data")) if response.get("ok") else {
        "fields": {},
        "filled_count": 0,
        "total_fields": 0,
        "ratio": 0.0,
        "missing_core": [],
        "core_ready": False,
    }
    return response


def _guess_douyin_sec_user_id(input_value: str) -> str:
    return str(extract_douyin_sec_uid(input_value) or "")


def _guess_xhs_ids(input_value: str) -> Tuple[str, str]:
    value = (input_value or "").strip()
    if not value:
        return "", ""
    direct_user_id = str(extract_xhs_user_id(value) or "")
    if direct_user_id and looks_like_xhs_user_id(direct_user_id) and not value.startswith(("http://", "https://")):
        return direct_user_id, ""
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
    progress: Optional[ProgressReporter] = None,
) -> Dict[str, Any]:
    trace: List[Dict[str, Any]] = []
    if progress is not None:
        progress.started(stage="author_home.collect", message="collecting douyin author homepage")
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
        if progress is not None:
            progress.progress(
                stage="author_home.collect.pagination",
                message="douyin pagination page requested",
                data={"page": page, "cursor_in": cursor},
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
    if progress is not None:
        progress.done(
            stage="author_home.collect",
            message="douyin author homepage collected",
            data={"works_count": len(works), "pages": len(pagination_trace), "request_id": request_id},
        )

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
    progress: Optional[ProgressReporter] = None,
) -> Dict[str, Any]:
    trace: List[Dict[str, Any]] = []
    if progress is not None:
        progress.started(stage="author_home.collect", message="collecting xiaohongshu author homepage")
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

    profile_routes = _xhs_route_plan("profile")
    profile_resp: Dict[str, Any] = {}
    profile_reason: Optional[str] = None
    profile_attempts: List[Dict[str, Any]] = []
    for step_name, path, route_label in profile_routes:
        profile_resp = _call_xhs_route(
            base_url=base_url,
            token=token,
            timeout_ms=timeout_ms,
            path=path,
            route_label=route_label,
            params={"user_id": user_id, "share_text": input_value, "xsec_token": xsec_token or None},
            fallback_reason=profile_reason,
            completeness_builder=lambda data, resolved_author_id=user_id: _xhs_profile_field_completeness(data, resolved_author_id),
        )
        profile_decision = _xhs_profile_accept_decision(profile_resp, profile_resp.get("_field_completeness") or {})
        profile_attempts.append(
            {
                "route_label": route_label,
                "endpoint": path,
                "accepted": bool(profile_decision.get("accepted")),
                "accept_reason": profile_decision.get("accept_reason"),
                "fallback_reason": profile_decision.get("fallback_reason"),
                "field_completeness": profile_resp.get("_field_completeness"),
                "request_id": profile_resp.get("request_id"),
            }
        )
        trace.append(
            build_api_trace(
                step=step_name,
                endpoint=path,
                response=profile_resp,
                extra={
                    "route_label": route_label,
                    "field_completeness": profile_resp.get("_field_completeness"),
                    "accept_reason": profile_decision.get("accept_reason"),
                    "route_accepted": bool(profile_decision.get("accepted")),
                },
            )
        )
        request_id_candidates.append(profile_resp)
        if profile_decision.get("accepted"):
            profile_resp["_accept_reason"] = profile_decision.get("accept_reason")
            break
        profile_reason = str(profile_decision.get("fallback_reason") or "field_completeness_below_threshold")
        profile_resp["fallback_trigger_reason"] = profile_reason

    trace.append(
        {
            "step": "xhs.profile.route_decision",
            "chosen_route": profile_resp.get("_route_label"),
            "request_id": profile_resp.get("request_id"),
            "field_completeness": profile_resp.get("_field_completeness"),
            "accept_reason": profile_resp.get("_accept_reason"),
            "fallback_reason": profile_reason,
            "attempted_routes": profile_attempts,
        }
    )

    works: List[Dict[str, Any]] = []
    seen_ids = set()
    cursor: Any = ""
    has_more = True
    page = 0
    pagination_trace: List[Dict[str, Any]] = []

    while has_more and page < max(pages_max, 1) and len(works) < max_items:
        page += 1
        if progress is not None:
            progress.progress(
                stage="author_home.collect.pagination",
                message="xiaohongshu pagination page requested",
                data={"page": page, "cursor_in": cursor},
            )
        posts_routes = _xhs_route_plan("posts")
        posts_resp: Dict[str, Any] = {}
        posts_reason: Optional[str] = None
        posts_attempts: List[Dict[str, Any]] = []
        for step_name, path, route_label in posts_routes:
            posts_resp = _call_xhs_route(
                base_url=base_url,
                token=token,
                timeout_ms=timeout_ms,
                path=path,
                route_label=route_label,
                params={
                    "user_id": user_id,
                    "share_text": input_value,
                    "cursor": cursor or None,
                    "num": min(max(page_size, 1), 20),
                    "xsec_token": xsec_token or None,
                },
                fallback_reason=posts_reason,
                completeness_builder=_xhs_posts_field_completeness,
            )
            posts_decision = _xhs_posts_accept_decision(posts_resp, posts_resp.get("_field_completeness") or {})
            posts_attempts.append(
                {
                    "route_label": route_label,
                    "endpoint": path,
                    "accepted": bool(posts_decision.get("accepted")),
                    "accept_reason": posts_decision.get("accept_reason"),
                    "fallback_reason": posts_decision.get("fallback_reason"),
                    "field_completeness": posts_resp.get("_field_completeness"),
                    "request_id": posts_resp.get("request_id"),
                }
            )
            trace.append(
                build_api_trace(
                    step=step_name,
                    endpoint=path,
                    response=posts_resp,
                    extra={
                        "page": page,
                        "cursor": cursor,
                        "route_label": route_label,
                        "field_completeness": posts_resp.get("_field_completeness"),
                        "accept_reason": posts_decision.get("accept_reason"),
                        "route_accepted": bool(posts_decision.get("accepted")),
                    },
                )
            )
            request_id_candidates.append(posts_resp)
            if posts_decision.get("accepted"):
                posts_resp["_accept_reason"] = posts_decision.get("accept_reason")
                break
            posts_reason = str(posts_decision.get("fallback_reason") or "field_completeness_below_threshold")
            posts_resp["fallback_trigger_reason"] = posts_reason

        trace.append(
            {
                "step": "xhs.posts.route_decision",
                "page": page,
                "cursor_in": cursor,
                "chosen_route": posts_resp.get("_route_label"),
                "request_id": posts_resp.get("request_id"),
                "field_completeness": posts_resp.get("_field_completeness"),
                "accept_reason": posts_resp.get("_accept_reason"),
                "fallback_reason": posts_reason,
                "attempted_routes": posts_attempts,
            }
        )

        data = posts_resp.get("data")
        page_items = _pick_list(data, ["notes", "note_list", "noteList", "items", "list"])
        next_cursor = _pick_text(data, ["cursor", "next_cursor", "last_cursor", "last_note_id"])
        has_more_flag = _pick_int(data, ["has_more", "hasMore"], default=0)
        pagination_trace.append(
            {
                "page": page,
                "cursor_in": cursor,
                "cursor_out": next_cursor,
                "has_more": has_more_flag,
                "items": len(page_items),
                "route_label": posts_resp.get("_route_label"),
                "request_id": posts_resp.get("request_id"),
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
    if progress is not None:
        progress.done(
            stage="author_home.collect",
            message="xiaohongshu author homepage collected",
            data={"works_count": len(works), "pages": len(pagination_trace), "request_id": request_id},
        )

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
