#!/usr/bin/env python3
"""Collectors for author homepage profile + paginated posts."""

from __future__ import annotations

import os
from typing import Any, Dict, List, Optional, Tuple
from urllib.parse import parse_qs, urlparse

from scripts.core.extract_pipeline import (
    build_api_trace,
    build_attempted_route,
    build_route_plan_entry,
    build_stage_status,
)
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


def _pick_raw(payload: Any, keys: List[str]) -> Any:
    ordered_keys = [str(key) for key in keys if str(key).strip()]

    def _walk(node: Any) -> Any:
        if isinstance(node, dict):
            for key in ordered_keys:
                if key in node and node.get(key) is not None:
                    return node.get(key)
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

    return _walk(payload)


def _payload_candidates(payload: Any) -> List[Any]:
    candidates: List[Any] = []
    if payload is not None:
        candidates.append(payload)
    if isinstance(payload, dict):
        nested = payload.get("data")
        if nested is not None:
            candidates.append(nested)
    return candidates


def _pick_raw_from_candidates(payload: Any, keys: List[str]) -> Any:
    for candidate in _payload_candidates(payload):
        hit = _pick_raw(candidate, keys)
        if hit is not None:
            return hit
    return None


def _pick_list_from_candidates(payload: Any, keys: List[str]) -> List[Any]:
    for candidate in _payload_candidates(payload):
        hit = _pick_list(candidate, keys)
        if hit:
            return hit
    return []


def _unwrap_data_layers(payload: Any, *, max_depth: int = 3) -> Any:
    node = payload
    depth = 0
    while depth < max_depth and isinstance(node, dict) and isinstance(node.get("data"), dict):
        node = node.get("data")
        depth += 1
    return node


def _extract_douyin_posts_page(payload: Any) -> Dict[str, Any]:
    node = _unwrap_data_layers(payload)
    if not isinstance(node, dict):
        return {}
    return node


def _extract_douyin_posts_items(payload: Any) -> List[Any]:
    node = _extract_douyin_posts_page(payload)
    items = node.get("aweme_list")
    return items if isinstance(items, list) else []


def _extract_douyin_posts_next_cursor(payload: Any) -> Any:
    node = _extract_douyin_posts_page(payload)
    if not isinstance(node, dict):
        return None
    for key in ("max_cursor", "cursor", "next_cursor"):
        if key in node and node.get(key) is not None:
            return node.get(key)
    return None


def _extract_douyin_posts_has_more(payload: Any) -> Any:
    node = _extract_douyin_posts_page(payload)
    if not isinstance(node, dict):
        return None
    for key in ("has_more", "hasMore"):
        if key in node and node.get(key) is not None:
            return node.get(key)
    return None


def _extract_xhs_posts_page(payload: Any) -> Dict[str, Any]:
    node = _unwrap_data_layers(payload)
    if not isinstance(node, dict):
        return {}
    return node


def _extract_xhs_posts_items(payload: Any) -> List[Any]:
    node = _extract_xhs_posts_page(payload)
    for key in ("notes", "note_list", "noteList", "items", "list"):
        value = node.get(key)
        if isinstance(value, list):
            return value
    return []


def _extract_xhs_response_cursor(payload: Any) -> str:
    node = _extract_xhs_posts_page(payload)
    if not isinstance(node, dict):
        return ""
    for key in ("cursor", "next_cursor", "last_cursor", "last_note_id"):
        value = _to_text(node.get(key))
        if value:
            return value
    return ""


def _extract_xhs_posts_has_more(payload: Any) -> Any:
    node = _extract_xhs_posts_page(payload)
    if not isinstance(node, dict):
        return None
    for key in ("has_more", "hasMore"):
        if key in node and node.get(key) is not None:
            return node.get(key)
    return None


def _normalize_has_more(value: Any) -> Optional[bool]:
    if value is None:
        return None
    if isinstance(value, bool):
        return value
    if isinstance(value, (int, float)):
        return bool(int(value))
    text = _to_text(value).lower()
    if not text:
        return None
    if text in {"1", "true", "yes", "y"}:
        return True
    if text in {"0", "false", "no", "n"}:
        return False
    return None


def _normalize_int_like(value: Any) -> Optional[int]:
    if value is None:
        return None
    try:
        if isinstance(value, bool):
            return int(value)
        if isinstance(value, (int, float)):
            return int(value)
        text = _to_text(value)
        if not text:
            return None
        return int(float(text.replace(",", "")))
    except Exception:
        return None


def _last_xhs_note_id(items: List[Any]) -> str:
    for item in reversed(items):
        if not isinstance(item, dict):
            continue
        note_id = _pick_text(item, ["note_id", "id", "item_id"])
        if note_id:
            return note_id
    return ""


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


def _response_failure_reason(response: Dict[str, Any]) -> str:
    if response.get("timeout_retry_exhausted"):
        return "primary_timeout_retry_exhausted"
    if response.get("error_reason"):
        return "primary_non_timeout_failure"
    return "primary_unknown_failure"


def _build_unavailable_attempt(
    *,
    route_label: str,
    endpoint: str,
    reason: str,
    extra: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    return build_attempted_route(
        route_label=route_label,
        endpoint=endpoint,
        accepted=False,
        accept_reason="skipped_param_unavailable",
        fallback_reason=reason,
        param_readiness="unavailable",
        param_reason=reason,
        skipped=True,
        extra=extra,
    )


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
    page_items = _extract_xhs_posts_items(payload)
    first_item = _pick_first_mapping(page_items)
    has_more_flag = _extract_xhs_posts_has_more(payload) is not None
    cursor_hit = bool(_extract_xhs_response_cursor(payload))
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


def _xhs_profile_accept_decision(response: Dict[str, Any], completeness: Dict[str, Any]) -> Dict[str, Any]:
    if not response.get("ok"):
        return {
            "accepted": False,
            "accept_reason": "response_not_ok",
            "fallback_reason": _response_failure_reason(response),
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
            "fallback_reason": _response_failure_reason(response),
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


def _douyin_profile_field_completeness(payload: Any, resolved_author_id: str) -> Dict[str, Any]:
    fields = {
        "platform_author_id": bool(_pick_text(payload, ["sec_user_id", "sec_uid", "uid", "user_id", "id"]) or resolved_author_id),
        "nickname": bool(_pick_text(payload, ["nickname", "name"])),
        "avatar_url": bool(_extract_first_url(_first_url_candidate(payload, ["avatar_larger", "avatar_thumb", "avatar_url", "avatar", "images"]))),
        "fans_count": _pick_int(payload, ["follower_count", "fans_count", "mplatform_followers_count"], default=0) > 0,
        "works_count": _pick_int(payload, ["aweme_count", "works_count", "video_count"], default=0) > 0,
        "unique_id": bool(_pick_text(payload, ["unique_id", "short_id", "douyin_id", "display_id"])),
    }
    return _build_field_completeness(fields, core_keys=["platform_author_id", "nickname"])


def _douyin_posts_field_completeness(payload: Any) -> Dict[str, Any]:
    page_items = _extract_douyin_posts_items(payload)
    first_item = _pick_first_mapping(page_items)
    has_more_flag = _extract_douyin_posts_has_more(payload) is not None
    cursor_hit = _extract_douyin_posts_next_cursor(payload) is not None
    cover_hit = bool(_extract_first_url(_first_url_candidate(first_item, ["cover_url", "cover", "origin_cover", "image", "images"])))
    share_or_source = bool(_pick_text(first_item, ["share_url", "share_link", "url"])) or bool(_pick_text(first_item, ["aweme_id", "item_id", "id"]))
    interaction_values = [
        _pick_int(first_item, ["digg_count"], default=-1),
        _pick_int(first_item, ["comment_count"], default=-1),
        _pick_int(first_item, ["collect_count"], default=-1),
        _pick_int(first_item, ["share_count"], default=-1),
        _pick_int(first_item, ["play_count"], default=-1),
    ]
    fields = {
        "items": len(page_items) > 0,
        "platform_work_id": bool(_pick_text(first_item, ["aweme_id", "item_id", "id"])),
        "title_or_caption": bool(_pick_text(first_item, ["title", "caption", "desc"])),
        "published_date": bool(_pick_text(first_item, ["create_time", "publish_time"])),
        "base_link_fields": cover_hit or share_or_source,
        "interaction_fields": any(value >= 0 for value in interaction_values),
        "cursor": cursor_hit,
        "has_more_flag": has_more_flag,
        "response_shape": len(page_items) > 0 or cursor_hit or has_more_flag,
    }
    return _build_field_completeness(fields, core_keys=["items", "platform_work_id", "title_or_caption", "published_date"])


def _douyin_profile_accept_decision(response: Dict[str, Any], completeness: Dict[str, Any]) -> Dict[str, Any]:
    if not response.get("ok"):
        return {
            "accepted": False,
            "accept_reason": "response_not_ok",
            "fallback_reason": _response_failure_reason(response),
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
        for field_name in ("avatar_url", "fans_count", "works_count", "unique_id")
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


def _douyin_posts_accept_decision(response: Dict[str, Any], completeness: Dict[str, Any]) -> Dict[str, Any]:
    if not response.get("ok"):
        return {
            "accepted": False,
            "accept_reason": "response_not_ok",
            "fallback_reason": _response_failure_reason(response),
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
    return {
        "accepted": True,
        "accept_reason": "posts_contract_fields_ready",
        "fallback_reason": "",
    }


def _douyin_profile_route_plan(*, sec_user_id: str, unique_id: str, uid: str) -> List[Dict[str, Any]]:
    sec_ready = bool(sec_user_id)
    unique_ready = bool(unique_id)
    uid_ready = bool(uid)
    return [
        {
            "step_name": "douyin.profile.app_v3",
            "path": "/api/u1/v1/douyin/app/v3/handler_user_profile",
            "route_label": "app_v3",
            "params": {"sec_user_id": sec_user_id or None},
            "param_readiness": "ready" if sec_ready else "unavailable",
            "param_reason": "" if sec_ready else "missing_sec_user_id",
        },
        {
            "step_name": "douyin.profile.web_v4",
            "path": "/api/u1/v1/douyin/web/handler_user_profile_v4",
            "route_label": "web_v4",
            "params": {"sec_user_id": sec_user_id or None},
            "param_readiness": "ready" if sec_ready else "unavailable",
            "param_reason": "" if sec_ready else "missing_sec_user_id",
        },
        {
            "step_name": "douyin.profile.web",
            "path": "/api/u1/v1/douyin/web/handler_user_profile",
            "route_label": "web",
            "params": {"sec_user_id": sec_user_id or None},
            "param_readiness": "ready" if sec_ready else "unavailable",
            "param_reason": "" if sec_ready else "missing_sec_user_id",
        },
        {
            "step_name": "douyin.profile.web_v2",
            "path": "/api/u1/v1/douyin/web/handler_user_profile_v2",
            "route_label": "web_v2",
            "params": {"unique_id": unique_id or None},
            "param_readiness": "ready" if unique_ready else "unavailable",
            "param_reason": "" if unique_ready else "missing_unique_id",
        },
        {
            "step_name": "douyin.profile.web_v3",
            "path": "/api/u1/v1/douyin/web/handler_user_profile_v3",
            "route_label": "web_v3",
            "params": {"uid": uid or None},
            "param_readiness": "ready" if uid_ready else "unavailable",
            "param_reason": "" if uid_ready else "missing_uid",
        },
    ]


def _douyin_posts_route_plan(*, sec_user_id: str, cursor: int, count: int, cookie: str) -> List[Dict[str, Any]]:
    sec_ready = bool(sec_user_id)
    web_ready = sec_ready and bool(cookie)
    web_reason = ""
    if not sec_ready:
        web_reason = "missing_sec_user_id"
    elif not cookie:
        web_reason = "fallback_requires_cookie"
    return [
        {
            "step_name": "douyin.posts.app_v3",
            "path": "/api/u1/v1/douyin/app/v3/fetch_user_post_videos",
            "route_label": "app_v3",
            "params": {
                "sec_user_id": sec_user_id or None,
                "count": count,
                "max_cursor": cursor,
                "sort_type": 0,
            },
            "param_readiness": "ready" if sec_ready else "unavailable",
            "param_reason": "" if sec_ready else "missing_sec_user_id",
        },
        {
            "step_name": "douyin.posts.web",
            "path": "/api/u1/v1/douyin/web/fetch_user_post_videos",
            "route_label": "web",
            "params": {
                "sec_user_id": sec_user_id or None,
                "count": count,
                "max_cursor": cursor,
                "filter_type": 0,
                "cookie": cookie or None,
            },
            "param_readiness": "ready" if web_ready else "unavailable",
            "param_reason": web_reason,
        },
    ]


def _xhs_route_plan(kind: str, *, user_id: str, input_value: str, cursor: Any = "") -> List[Dict[str, Any]]:
    user_ready = bool(user_id)
    if kind == "profile":
        return [
            {
                "step_name": "xhs.profile.app_v2",
                "path": "/api/u1/v1/xiaohongshu/app_v2/get_user_info",
                "route_label": "app_v2",
                "params": {"user_id": user_id or None, "share_text": input_value or None},
                "param_readiness": "ready" if user_ready else "unavailable",
                "param_reason": "" if user_ready else "missing_user_id",
            },
            {
                "step_name": "xhs.profile.app",
                "path": "/api/u1/v1/xiaohongshu/app/get_user_info",
                "route_label": "app",
                "params": {"user_id": user_id or None},
                "param_readiness": "ready" if user_ready else "unavailable",
                "param_reason": "" if user_ready else "missing_user_id",
            },
            {
                "step_name": "xhs.profile.web_v2_app",
                "path": "/api/u1/v1/xiaohongshu/web_v2/fetch_user_info_app",
                "route_label": "web_v2_app",
                "params": {"user_id": user_id or None},
                "param_readiness": "ready" if user_ready else "unavailable",
                "param_reason": "" if user_ready else "missing_user_id",
            },
            {
                "step_name": "xhs.profile.web_v2",
                "path": "/api/u1/v1/xiaohongshu/web_v2/fetch_user_info",
                "route_label": "web_v2",
                "params": {"user_id": user_id or None},
                "param_readiness": "ready" if user_ready else "unavailable",
                "param_reason": "" if user_ready else "missing_user_id",
            },
            {
                "step_name": "xhs.profile.web_v1_v2",
                "path": "/api/u1/v1/xiaohongshu/web/get_user_info_v2",
                "route_label": "web_v1_v2",
                "params": {"user_id": user_id or None, "share_text": input_value or None},
                "param_readiness": "ready" if user_ready else "unavailable",
                "param_reason": "" if user_ready else "missing_user_id",
            },
            {
                "step_name": "xhs.profile.web_v1",
                "path": "/api/u1/v1/xiaohongshu/web/get_user_info",
                "route_label": "web_v1",
                "params": {"user_id": user_id or None},
                "param_readiness": "ready" if user_ready else "unavailable",
                "param_reason": "" if user_ready else "missing_user_id",
            },
        ]
    if kind == "posts":
        last_cursor = _to_text(cursor)
        return [
            {
                "step_name": "xhs.posts.app_v2",
                "path": "/api/u1/v1/xiaohongshu/app_v2/get_user_posted_notes",
                "route_label": "app_v2",
                "params": {"user_id": user_id or None, "share_text": input_value or None, "cursor": last_cursor or None},
                "param_readiness": "ready" if user_ready else "unavailable",
                "param_reason": "" if user_ready else "missing_user_id",
            },
            {
                "step_name": "xhs.posts.app",
                "path": "/api/u1/v1/xiaohongshu/app/get_user_notes",
                "route_label": "app",
                "params": {"user_id": user_id or None, "cursor": last_cursor or None},
                "param_readiness": "ready" if user_ready else "unavailable",
                "param_reason": "" if user_ready else "missing_user_id",
            },
            {
                "step_name": "xhs.posts.web_v2_app",
                "path": "/api/u1/v1/xiaohongshu/web_v2/fetch_home_notes_app",
                "route_label": "web_v2_app",
                "params": {"user_id": user_id or None, "cursor": last_cursor or None},
                "param_readiness": "ready" if user_ready else "unavailable",
                "param_reason": "" if user_ready else "missing_user_id",
            },
            {
                "step_name": "xhs.posts.web_v2",
                "path": "/api/u1/v1/xiaohongshu/web_v2/fetch_home_notes",
                "route_label": "web_v2",
                "params": {"user_id": user_id or None, "cursor": last_cursor or None},
                "param_readiness": "ready" if user_ready else "unavailable",
                "param_reason": "" if user_ready else "missing_user_id",
            },
            {
                "step_name": "xhs.posts.web_v1_v2",
                "path": "/api/u1/v1/xiaohongshu/web/get_user_notes_v2",
                "route_label": "web_v1_v2",
                "params": {"user_id": user_id or None, "lastCursor": last_cursor or None},
                "param_readiness": "ready" if user_ready else "unavailable",
                "param_reason": "" if user_ready else "missing_user_id",
            },
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
    stage_status: Dict[str, Any] = {}
    if progress is not None:
        progress.started(stage="author_home.collect", message="collecting douyin author homepage")
    sec_user_id = _guess_douyin_sec_user_id(input_value)
    resolve_resp: Optional[Dict[str, Any]] = None
    request_id_candidates: List[Optional[Dict[str, Any]]] = []
    page_limit = min(max(page_size, 1), 20)
    max_pages = max(pages_max, 1)
    resolver_route_plan = [
        build_route_plan_entry(route_label="local_extract", endpoint=None, method="LOCAL"),
        build_route_plan_entry(
            route_label="web",
            endpoint="/api/u1/v1/douyin/web/get_sec_user_id",
            method="GET",
        ),
    ]
    resolver_attempts: List[Dict[str, Any]] = []

    if sec_user_id:
        resolver_attempts.append(
            build_attempted_route(
                route_label="local_extract",
                endpoint=None,
                accepted=True,
                accept_reason="author_id_ready",
                param_readiness="ready",
                extra={"resolved_author_id": sec_user_id},
            )
        )
        trace.append(
            {
                "step": "douyin.resolve_sec_user_id.local",
                "route_label": "local_extract",
                "ok": True,
                "resolved_author_id": sec_user_id,
                "accept_reason": "author_id_ready",
            }
        )
        stage_status["resolver"] = build_stage_status(
            stage="resolver",
            status="succeeded",
            route_plan=resolver_route_plan,
            attempted_routes=resolver_attempts,
            chosen_route="local_extract",
            accept_reason="author_id_ready",
            fallback_reason="",
            error_reason=None,
            all_routes_failed=False,
        )
    else:
        resolve_resp = call_json_api(
            base_url=base_url,
            path="/api/u1/v1/douyin/web/get_sec_user_id",
            token=token,
            method="GET",
            timeout_ms=timeout_ms,
            params={"url": input_value},
        )
        trace.append(build_api_trace(step="douyin.resolve_sec_user_id", endpoint="/api/u1/v1/douyin/web/get_sec_user_id", response=resolve_resp))
        request_id_candidates.append(resolve_resp)
        resolve_data = resolve_resp.get("data")
        sec_user_id = _extract_douyin_sec_user_id(resolve_data)
        resolver_attempts.append(
            build_attempted_route(
                route_label="web",
                endpoint="/api/u1/v1/douyin/web/get_sec_user_id",
                response=resolve_resp,
                accepted=bool(sec_user_id),
                accept_reason="author_id_ready" if sec_user_id else "author_id_unresolved",
                fallback_reason="" if sec_user_id else "resolver_fallback_unavailable",
                extra={"resolved_author_id": sec_user_id},
            )
        )
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
        stage_status["resolver"] = build_stage_status(
            stage="resolver",
            status="succeeded" if sec_user_id else "failed",
            route_plan=resolver_route_plan,
            attempted_routes=resolver_attempts,
            chosen_route="web",
            accept_reason="author_id_ready" if sec_user_id else "author_id_unresolved",
            fallback_reason="" if sec_user_id else "resolver_fallback_unavailable",
            error_reason=None if sec_user_id else "author_id_unresolved",
            all_routes_failed=not bool(sec_user_id),
        )

    trace.append(
        {
            "step": "douyin.resolver.route_decision",
            **stage_status["resolver"],
        }
    )

    web_cookie = os.getenv("TIKOMNI_DOUYIN_WEB_COOKIE", "").strip()
    if not sec_user_id:
        stage_status["profile"] = build_stage_status(
            stage="profile",
            status="skipped",
            route_plan=[
                build_route_plan_entry(
                    route_label=route["route_label"],
                    endpoint=route["path"],
                    method="GET",
                    param_readiness=route["param_readiness"],
                    param_reason=route["param_reason"],
                )
                for route in _douyin_profile_route_plan(sec_user_id="", unique_id="", uid="")
            ],
            attempted_routes=[],
            chosen_route="",
            accept_reason="",
            fallback_reason="author_id_unresolved",
            error_reason="author_id_unresolved",
            all_routes_failed=False,
        )
        stage_status["posts"] = build_stage_status(
            stage="posts",
            status="skipped",
            route_plan=[
                build_route_plan_entry(
                    route_label=route["route_label"],
                    endpoint=route["path"],
                    method="GET",
                    param_readiness=route["param_readiness"],
                    param_reason=route["param_reason"],
                )
                for route in _douyin_posts_route_plan(sec_user_id="", cursor=0, count=page_limit, cookie=web_cookie)
            ],
            attempted_routes=[],
            chosen_route="",
            accept_reason="",
            fallback_reason="author_id_unresolved",
            error_reason="author_id_unresolved",
            all_routes_failed=False,
        )
        trace.append({"step": "douyin.profile.route_decision", **stage_status["profile"]})
        trace.append({"step": "douyin.posts.stage_decision", **stage_status["posts"]})
        request_id = _pick_request_id(request_id_candidates, trace)
        if progress is not None:
            progress.done(
                stage="author_home.collect",
                message="douyin author homepage collected",
                data={"works_count": 0, "pages": 0, "request_id": request_id},
            )
        return {
            "platform": "douyin",
            "resolved_author_id": "",
            "profile_response": {},
            "works": [],
            "pagination": {
                "sort": "latest",
                "sort_type": 0,
                "cursor_mode": "max_cursor",
                "pages": [],
                "total_collected": 0,
                "max_items": max_items,
            },
            "extract_trace": trace,
            "request_id": request_id,
            "stage_status": stage_status,
            "error_reason": "author_id_unresolved",
        }

    profile_resp: Dict[str, Any] = {}
    profile_attempts: List[Dict[str, Any]] = []
    profile_reason: str = ""
    profile_unique_id = ""
    profile_uid = ""
    sec_profile_routes = _douyin_profile_route_plan(sec_user_id=sec_user_id, unique_id="", uid="")[:3]
    extra_profile_routes: List[Dict[str, Any]] = []

    def _run_douyin_profile_route(route: Dict[str, Any], *, fallback_reason: str) -> Tuple[Dict[str, Any], Dict[str, Any]]:
        response = call_json_api(
            base_url=base_url,
            path=str(route["path"]),
            token=token,
            method="GET",
            timeout_ms=timeout_ms,
            params=dict(route.get("params") or {}),
        )
        response["_endpoint"] = route["path"]
        response["_route_label"] = route["route_label"]
        if fallback_reason:
            response["fallback_trigger_reason"] = fallback_reason
        response["_field_completeness"] = _douyin_profile_field_completeness(response.get("data"), sec_user_id) if response.get("ok") else {
            "fields": {},
            "filled_count": 0,
            "total_fields": 0,
            "ratio": 0.0,
            "missing_core": [],
            "core_ready": False,
        }
        decision = _douyin_profile_accept_decision(response, response.get("_field_completeness") or {})
        return response, decision

    for route in sec_profile_routes:
        response, decision = _run_douyin_profile_route(route, fallback_reason=profile_reason)
        profile_resp = response
        request_id_candidates.append(response)
        profile_unique_id = profile_unique_id or _pick_text(response.get("data"), ["unique_id", "short_id", "douyin_id", "display_id"])
        profile_uid = profile_uid or _pick_text(response.get("data"), ["uid", "user_id", "id"])
        profile_attempts.append(
            build_attempted_route(
                route_label=str(route["route_label"]),
                endpoint=str(route["path"]),
                response=response,
                accepted=bool(decision.get("accepted")),
                accept_reason=str(decision.get("accept_reason") or ""),
                fallback_reason=str(decision.get("fallback_reason") or ""),
                extra={"field_completeness": response.get("_field_completeness")},
            )
        )
        trace.append(
            build_api_trace(
                step=str(route["step_name"]),
                endpoint=str(route["path"]),
                response=response,
                extra={
                    "route_label": route["route_label"],
                    "field_completeness": response.get("_field_completeness"),
                    "accept_reason": decision.get("accept_reason"),
                    "route_accepted": bool(decision.get("accepted")),
                },
            )
        )
        if decision.get("accepted"):
            profile_resp["_accept_reason"] = decision.get("accept_reason")
            break
        profile_reason = str(decision.get("fallback_reason") or "field_completeness_below_threshold")
        profile_resp["fallback_trigger_reason"] = profile_reason

    if not profile_resp.get("_accept_reason"):
        extra_profile_routes = _douyin_profile_route_plan(
            sec_user_id=sec_user_id,
            unique_id=profile_unique_id,
            uid=profile_uid,
        )[3:]
        for route in extra_profile_routes:
            if route.get("param_readiness") != "ready":
                profile_attempts.append(
                    _build_unavailable_attempt(
                        route_label=str(route["route_label"]),
                        endpoint=str(route["path"]),
                        reason=str(route.get("param_reason") or "fallback_param_unavailable"),
                    )
                )
                continue
            response, decision = _run_douyin_profile_route(route, fallback_reason=profile_reason)
            profile_resp = response
            request_id_candidates.append(response)
            profile_attempts.append(
                build_attempted_route(
                    route_label=str(route["route_label"]),
                    endpoint=str(route["path"]),
                    response=response,
                    accepted=bool(decision.get("accepted")),
                    accept_reason=str(decision.get("accept_reason") or ""),
                    fallback_reason=str(decision.get("fallback_reason") or ""),
                    extra={"field_completeness": response.get("_field_completeness")},
                )
            )
            trace.append(
                build_api_trace(
                    step=str(route["step_name"]),
                    endpoint=str(route["path"]),
                    response=response,
                    extra={
                        "route_label": route["route_label"],
                        "field_completeness": response.get("_field_completeness"),
                        "accept_reason": decision.get("accept_reason"),
                        "route_accepted": bool(decision.get("accepted")),
                    },
                )
            )
            if decision.get("accepted"):
                profile_resp["_accept_reason"] = decision.get("accept_reason")
                break
            profile_reason = str(decision.get("fallback_reason") or "field_completeness_below_threshold")
            profile_resp["fallback_trigger_reason"] = profile_reason
    else:
        extra_profile_routes = _douyin_profile_route_plan(
            sec_user_id=sec_user_id,
            unique_id=profile_unique_id,
            uid=profile_uid,
        )[3:]
        for route in extra_profile_routes:
            if route.get("param_readiness") != "ready":
                profile_attempts.append(
                    _build_unavailable_attempt(
                        route_label=str(route["route_label"]),
                        endpoint=str(route["path"]),
                        reason=str(route.get("param_reason") or "fallback_param_unavailable"),
                    )
                )

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

    profile_route_plan = [
        build_route_plan_entry(
            route_label=str(route["route_label"]),
            endpoint=str(route["path"]),
            method="GET",
            param_readiness=str(route.get("param_readiness") or "ready"),
            param_reason=str(route.get("param_reason") or ""),
        )
        for route in _douyin_profile_route_plan(sec_user_id=sec_user_id, unique_id=profile_unique_id, uid=profile_uid)
    ]
    profile_has_accepted = any(bool(attempt.get("accepted")) for attempt in profile_attempts)
    profile_has_ok_response = any(bool(attempt.get("ok")) for attempt in profile_attempts if not attempt.get("skipped"))
    profile_error_reason = None
    if not profile_has_accepted:
        profile_error_reason = "profile_contract_incomplete" if profile_has_ok_response else "profile_all_routes_failed"
    stage_status["profile"] = build_stage_status(
        stage="profile",
        status="succeeded" if profile_has_accepted else "failed",
        route_plan=profile_route_plan,
        attempted_routes=profile_attempts,
        chosen_route=str(profile_resp.get("_route_label") or ""),
        accept_reason=str(profile_resp.get("_accept_reason") or ""),
        fallback_reason=profile_reason,
        error_reason=profile_error_reason,
        all_routes_failed=not profile_has_accepted,
    )
    trace.append({"step": "douyin.profile.route_decision", **stage_status["profile"]})

    works: List[Dict[str, Any]] = []
    seen_ids = set()
    cursor = 0
    has_more = True
    page = 0
    pagination_trace: List[Dict[str, Any]] = []
    posts_attempts_all: List[Dict[str, Any]] = []
    posts_accepted_routes: List[str] = []
    posts_error_reason: Optional[str] = None

    while has_more and page < max_pages and len(works) < max_items:
        page += 1
        if progress is not None:
            progress.progress(
                stage="author_home.collect.pagination",
                message="douyin pagination page requested",
                data={"page": page, "cursor_in": cursor},
            )
        posts_routes = _douyin_posts_route_plan(sec_user_id=sec_user_id, cursor=cursor, count=page_limit, cookie=web_cookie)
        page_attempts: List[Dict[str, Any]] = []
        posts_resp: Dict[str, Any] = {}
        page_reason = ""
        for route in posts_routes:
            if route.get("param_readiness") != "ready":
                skipped_attempt = _build_unavailable_attempt(
                    route_label=str(route["route_label"]),
                    endpoint=str(route["path"]),
                    reason=str(route.get("param_reason") or "fallback_param_unavailable"),
                    extra={"page": page, "cursor_in": cursor},
                )
                page_attempts.append(skipped_attempt)
                posts_attempts_all.append(skipped_attempt)
                continue
            posts_resp = call_json_api(
                base_url=base_url,
                path=str(route["path"]),
                token=token,
                method="GET",
                timeout_ms=timeout_ms,
                params=dict(route.get("params") or {}),
            )
            posts_resp["_endpoint"] = route["path"]
            posts_resp["_route_label"] = route["route_label"]
            if page_reason:
                posts_resp["fallback_trigger_reason"] = page_reason
            posts_resp["_field_completeness"] = _douyin_posts_field_completeness(posts_resp.get("data")) if posts_resp.get("ok") else {
                "fields": {},
                "filled_count": 0,
                "total_fields": 0,
                "ratio": 0.0,
                "missing_core": [],
                "core_ready": False,
            }
            posts_decision = _douyin_posts_accept_decision(posts_resp, posts_resp.get("_field_completeness") or {})
            page_attempt = build_attempted_route(
                route_label=str(route["route_label"]),
                endpoint=str(route["path"]),
                response=posts_resp,
                accepted=bool(posts_decision.get("accepted")),
                accept_reason=str(posts_decision.get("accept_reason") or ""),
                fallback_reason=str(posts_decision.get("fallback_reason") or ""),
                extra={
                    "page": page,
                    "cursor_in": cursor,
                    "field_completeness": posts_resp.get("_field_completeness"),
                },
            )
            page_attempts.append(page_attempt)
            posts_attempts_all.append(page_attempt)
            trace.append(
                build_api_trace(
                    step=str(route["step_name"]),
                    endpoint=str(route["path"]),
                    response=posts_resp,
                    extra={
                        "page": page,
                        "cursor": cursor,
                        "route_label": route["route_label"],
                        "field_completeness": posts_resp.get("_field_completeness"),
                        "accept_reason": posts_decision.get("accept_reason"),
                        "route_accepted": bool(posts_decision.get("accepted")),
                    },
                )
            )
            request_id_candidates.append(posts_resp)
            if posts_decision.get("accepted"):
                posts_resp["_accept_reason"] = posts_decision.get("accept_reason")
                posts_accepted_routes.append(str(route["route_label"]))
                break
            page_reason = str(posts_decision.get("fallback_reason") or "field_completeness_below_threshold")
            posts_resp["fallback_trigger_reason"] = page_reason

        page_route_plan = [
            build_route_plan_entry(
                route_label=str(route["route_label"]),
                endpoint=str(route["path"]),
                method="GET",
                param_readiness=str(route.get("param_readiness") or "ready"),
                param_reason=str(route.get("param_reason") or ""),
            )
            for route in posts_routes
        ]
        trace.append(
            {
                "step": "douyin.posts.route_decision",
                "page": page,
                "cursor_in": cursor,
                "route_plan": page_route_plan,
                "chosen_route": posts_resp.get("_route_label"),
                "request_id": posts_resp.get("request_id"),
                "field_completeness": posts_resp.get("_field_completeness"),
                "accept_reason": posts_resp.get("_accept_reason"),
                "fallback_reason": page_reason,
                "attempted_routes": page_attempts,
                "all_routes_failed": not any(bool(attempt.get("accepted")) for attempt in page_attempts),
            }
        )

        if not posts_resp.get("_accept_reason"):
            posts_error_reason = "posts_contract_incomplete" if any(bool(attempt.get("ok")) for attempt in page_attempts if not attempt.get("skipped")) else "posts_all_routes_failed"
            pagination_trace.append(
                {
                    "page": page,
                    "cursor_in": cursor,
                    "cursor_out": None,
                    "has_more_raw": None,
                    "has_more_normalized": None,
                    "items": 0,
                    "stop_reason": posts_error_reason,
                }
            )
            break

        response_payload = posts_resp.get("data")
        page_items = _extract_douyin_posts_items(response_payload)

        next_cursor_raw = _extract_douyin_posts_next_cursor(response_payload)
        has_more_raw = _extract_douyin_posts_has_more(response_payload)
        next_cursor = _normalize_int_like(next_cursor_raw)
        has_more_normalized = _normalize_has_more(has_more_raw)

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

        next_cursor_changed = next_cursor is not None and next_cursor != cursor
        stop_reason = ""
        should_continue = False

        if len(works) >= max_items:
            stop_reason = "max_items_reached"
        elif not page_items:
            stop_reason = "page_empty"
        elif has_more_normalized is False:
            stop_reason = "has_more_false"
        elif next_cursor is not None and next_cursor == cursor:
            stop_reason = "cursor_not_advanced"
        elif has_more_normalized is True and next_cursor is None:
            stop_reason = "pagination_contract_incomplete"
        elif has_more_normalized is True or next_cursor_changed:
            should_continue = True
        else:
            stop_reason = "pagination_contract_incomplete"

        if should_continue and page >= max_pages:
            should_continue = False
            stop_reason = "pages_max_reached"

        pagination_trace.append(
            {
                "page": page,
                "cursor_in": cursor,
                "cursor_out": next_cursor,
                "has_more_raw": has_more_raw,
                "has_more_normalized": has_more_normalized,
                "items": len(page_items),
                "stop_reason": stop_reason,
            }
        )

        has_more = should_continue
        if should_continue and next_cursor is not None:
            cursor = next_cursor

    posts_route_plan = [
        build_route_plan_entry(
            route_label=str(route["route_label"]),
            endpoint=str(route["path"]),
            method="GET",
            param_readiness=str(route.get("param_readiness") or "ready"),
            param_reason=str(route.get("param_reason") or ""),
        )
        for route in _douyin_posts_route_plan(sec_user_id=sec_user_id, cursor=0, count=page_limit, cookie=web_cookie)
    ]
    posts_has_accepted = bool(posts_accepted_routes)
    if not posts_has_accepted and posts_error_reason is None:
        posts_error_reason = "posts_all_routes_failed"
    stage_status["posts"] = build_stage_status(
        stage="posts",
        status="succeeded" if posts_has_accepted else "failed",
        route_plan=posts_route_plan,
        attempted_routes=posts_attempts_all,
        chosen_route=posts_accepted_routes[0] if len(set(posts_accepted_routes)) == 1 and posts_accepted_routes else ("mixed" if posts_accepted_routes else ""),
        accept_reason="posts_pages_collected" if posts_has_accepted else "",
        fallback_reason=posts_error_reason or "",
        error_reason=None if posts_has_accepted else posts_error_reason,
        all_routes_failed=not posts_has_accepted,
    )
    trace.append({"step": "douyin.posts.stage_decision", **stage_status["posts"]})

    request_id = _pick_request_id(request_id_candidates, trace)
    if progress is not None:
        progress.done(
            stage="author_home.collect",
            message="douyin author homepage collected",
            data={"works_count": len(works), "pages": len(pagination_trace), "request_id": request_id},
        )

    collect_error_reason: Optional[str] = None
    if stage_status.get("resolver", {}).get("status") == "failed":
        collect_error_reason = str(stage_status["resolver"].get("error_reason") or "author_id_unresolved")
    elif not works and stage_status.get("posts", {}).get("status") == "failed":
        collect_error_reason = stage_status["posts"].get("error_reason")
    elif stage_status.get("profile", {}).get("status") == "failed":
        collect_error_reason = stage_status["profile"].get("error_reason")

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
        "stage_status": stage_status,
        "error_reason": collect_error_reason,
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
    stage_status: Dict[str, Any] = {}
    if progress is not None:
        progress.started(stage="author_home.collect", message="collecting xiaohongshu author homepage")
    user_id, xsec_token = _guess_xhs_ids(input_value)
    resolve_resp: Optional[Dict[str, Any]] = None
    request_id_candidates: List[Optional[Dict[str, Any]]] = []
    max_pages = max(pages_max, 1)
    page_limit = min(max(page_size, 1), 20)
    resolver_route_plan = [
        build_route_plan_entry(route_label="local_extract", endpoint=None, method="LOCAL"),
        build_route_plan_entry(
            route_label="app",
            endpoint="/api/u1/v1/xiaohongshu/app/get_user_id_and_xsec_token",
            method="GET",
        ),
    ]
    resolver_attempts: List[Dict[str, Any]] = []

    if user_id:
        resolver_attempts.append(
            build_attempted_route(
                route_label="local_extract",
                endpoint=None,
                accepted=True,
                accept_reason="author_id_ready",
                param_readiness="ready",
                extra={"resolved_author_id": user_id},
            )
        )
        trace.append(
            {
                "step": "xhs.resolve_user_id.local",
                "route_label": "local_extract",
                "ok": True,
                "resolved_author_id": user_id,
                "accept_reason": "author_id_ready",
            }
        )
        stage_status["resolver"] = build_stage_status(
            stage="resolver",
            status="succeeded",
            route_plan=resolver_route_plan,
            attempted_routes=resolver_attempts,
            chosen_route="local_extract",
            accept_reason="author_id_ready",
            fallback_reason="",
            error_reason=None,
            all_routes_failed=False,
        )
    else:
        resolve_resp = call_json_api(
            base_url=base_url,
            path="/api/u1/v1/xiaohongshu/app/get_user_id_and_xsec_token",
            token=token,
            method="GET",
            timeout_ms=timeout_ms,
            params={"share_link": input_value},
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
        resolver_attempts.append(
            build_attempted_route(
                route_label="app",
                endpoint="/api/u1/v1/xiaohongshu/app/get_user_id_and_xsec_token",
                response=resolve_resp,
                accepted=bool(user_id),
                accept_reason="author_id_ready" if user_id else "author_id_unresolved",
                fallback_reason="" if user_id else "resolver_fallback_unavailable",
                extra={"resolved_author_id": user_id},
            )
        )
        stage_status["resolver"] = build_stage_status(
            stage="resolver",
            status="succeeded" if user_id else "failed",
            route_plan=resolver_route_plan,
            attempted_routes=resolver_attempts,
            chosen_route="app",
            accept_reason="author_id_ready" if user_id else "author_id_unresolved",
            fallback_reason="" if user_id else "resolver_fallback_unavailable",
            error_reason=None if user_id else "author_id_unresolved",
            all_routes_failed=not bool(user_id),
        )

    trace.append({"step": "xhs.resolver.route_decision", **stage_status["resolver"]})

    if not user_id:
        stage_status["profile"] = build_stage_status(
            stage="profile",
            status="skipped",
            route_plan=[
                build_route_plan_entry(
                    route_label=route["route_label"],
                    endpoint=route["path"],
                    method="GET",
                    param_readiness=route["param_readiness"],
                    param_reason=route["param_reason"],
                )
                for route in _xhs_route_plan("profile", user_id="", input_value=input_value)
            ],
            attempted_routes=[],
            chosen_route="",
            accept_reason="",
            fallback_reason="author_id_unresolved",
            error_reason="author_id_unresolved",
            all_routes_failed=False,
        )
        stage_status["posts"] = build_stage_status(
            stage="posts",
            status="skipped",
            route_plan=[
                build_route_plan_entry(
                    route_label=route["route_label"],
                    endpoint=route["path"],
                    method="GET",
                    param_readiness=route["param_readiness"],
                    param_reason=route["param_reason"],
                )
                for route in _xhs_route_plan("posts", user_id="", input_value=input_value, cursor="")
            ],
            attempted_routes=[],
            chosen_route="",
            accept_reason="",
            fallback_reason="author_id_unresolved",
            error_reason="author_id_unresolved",
            all_routes_failed=False,
        )
        trace.append({"step": "xhs.profile.route_decision", **stage_status["profile"]})
        trace.append({"step": "xhs.posts.stage_decision", **stage_status["posts"]})
        request_id = _pick_request_id(request_id_candidates, trace)
        if progress is not None:
            progress.done(
                stage="author_home.collect",
                message="xiaohongshu author homepage collected",
                data={"works_count": 0, "pages": 0, "request_id": request_id},
            )
        return {
            "platform": "xiaohongshu",
            "resolved_author_id": "",
            "resolved_xsec_token": xsec_token,
            "profile_response": {},
            "works": [],
            "pagination": {
                "sort": "latest",
                "sort_type": "latest",
                "cursor_mode": "cursor",
                "pages": [],
                "total_collected": 0,
                "max_items": max_items,
            },
            "extract_trace": trace,
            "request_id": request_id,
            "stage_status": stage_status,
            "error_reason": "author_id_unresolved",
        }

    profile_routes = _xhs_route_plan("profile", user_id=user_id, input_value=input_value)
    profile_route_plan = [
        build_route_plan_entry(
            route_label=str(route["route_label"]),
            endpoint=str(route["path"]),
            method="GET",
            param_readiness=str(route.get("param_readiness") or "ready"),
            param_reason=str(route.get("param_reason") or ""),
        )
        for route in profile_routes
    ]
    profile_resp: Dict[str, Any] = {}
    profile_reason: Optional[str] = None
    profile_attempts: List[Dict[str, Any]] = []
    for route in profile_routes:
        if route.get("param_readiness") != "ready":
            profile_attempts.append(
                _build_unavailable_attempt(
                    route_label=str(route["route_label"]),
                    endpoint=str(route["path"]),
                    reason=str(route.get("param_reason") or "fallback_param_unavailable"),
                )
            )
            continue
        profile_resp = _call_xhs_route(
            base_url=base_url,
            token=token,
            timeout_ms=timeout_ms,
            path=str(route["path"]),
            route_label=str(route["route_label"]),
            params=dict(route.get("params") or {}),
            fallback_reason=profile_reason,
            completeness_builder=lambda data, resolved_author_id=user_id: _xhs_profile_field_completeness(data, resolved_author_id),
        )
        profile_decision = _xhs_profile_accept_decision(profile_resp, profile_resp.get("_field_completeness") or {})
        profile_attempts.append(
            build_attempted_route(
                route_label=str(route["route_label"]),
                endpoint=str(route["path"]),
                response=profile_resp,
                accepted=bool(profile_decision.get("accepted")),
                accept_reason=str(profile_decision.get("accept_reason") or ""),
                fallback_reason=str(profile_decision.get("fallback_reason") or ""),
                extra={"field_completeness": profile_resp.get("_field_completeness")},
            )
        )
        trace.append(
            build_api_trace(
                step=str(route["step_name"]),
                endpoint=str(route["path"]),
                response=profile_resp,
                extra={
                    "route_label": route["route_label"],
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
            "route_plan": profile_route_plan,
            "chosen_route": profile_resp.get("_route_label"),
            "request_id": profile_resp.get("request_id"),
            "field_completeness": profile_resp.get("_field_completeness"),
            "accept_reason": profile_resp.get("_accept_reason"),
            "fallback_reason": profile_reason,
            "attempted_routes": profile_attempts,
            "all_routes_failed": not any(bool(attempt.get("accepted")) for attempt in profile_attempts),
        }
    )
    profile_has_accepted = any(bool(attempt.get("accepted")) for attempt in profile_attempts)
    profile_has_ok_response = any(bool(attempt.get("ok")) for attempt in profile_attempts if not attempt.get("skipped"))
    profile_error_reason = None
    if not profile_has_accepted:
        profile_error_reason = "profile_contract_incomplete" if profile_has_ok_response else "profile_all_routes_failed"
    stage_status["profile"] = build_stage_status(
        stage="profile",
        status="succeeded" if profile_has_accepted else "failed",
        route_plan=profile_route_plan,
        attempted_routes=profile_attempts,
        chosen_route=str(profile_resp.get("_route_label") or ""),
        accept_reason=str(profile_resp.get("_accept_reason") or ""),
        fallback_reason=str(profile_reason or ""),
        error_reason=profile_error_reason,
        all_routes_failed=not profile_has_accepted,
    )

    works: List[Dict[str, Any]] = []
    seen_ids = set()
    cursor: Any = ""
    has_more = True
    page = 0
    pagination_trace: List[Dict[str, Any]] = []
    posts_attempts_all: List[Dict[str, Any]] = []
    posts_accepted_routes: List[str] = []
    posts_error_reason: Optional[str] = None

    while has_more and page < max_pages and len(works) < max_items:
        page += 1
        if progress is not None:
            progress.progress(
                stage="author_home.collect.pagination",
                message="xiaohongshu pagination page requested",
                data={"page": page, "cursor_in": cursor},
            )
        posts_routes = _xhs_route_plan("posts", user_id=user_id, input_value=input_value, cursor=cursor)
        posts_resp: Dict[str, Any] = {}
        posts_reason: Optional[str] = None
        posts_attempts: List[Dict[str, Any]] = []
        page_route_plan = [
            build_route_plan_entry(
                route_label=str(route["route_label"]),
                endpoint=str(route["path"]),
                method="GET",
                param_readiness=str(route.get("param_readiness") or "ready"),
                param_reason=str(route.get("param_reason") or ""),
            )
            for route in posts_routes
        ]
        for route in posts_routes:
            if route.get("param_readiness") != "ready":
                skipped_attempt = _build_unavailable_attempt(
                    route_label=str(route["route_label"]),
                    endpoint=str(route["path"]),
                    reason=str(route.get("param_reason") or "fallback_param_unavailable"),
                    extra={"page": page, "cursor_in": cursor},
                )
                posts_attempts.append(skipped_attempt)
                posts_attempts_all.append(skipped_attempt)
                continue
            posts_resp = _call_xhs_route(
                base_url=base_url,
                token=token,
                timeout_ms=timeout_ms,
                path=str(route["path"]),
                route_label=str(route["route_label"]),
                params=dict(route.get("params") or {}),
                fallback_reason=posts_reason,
                completeness_builder=_xhs_posts_field_completeness,
            )
            posts_decision = _xhs_posts_accept_decision(posts_resp, posts_resp.get("_field_completeness") or {})
            posts_attempt = build_attempted_route(
                route_label=str(route["route_label"]),
                endpoint=str(route["path"]),
                response=posts_resp,
                accepted=bool(posts_decision.get("accepted")),
                accept_reason=str(posts_decision.get("accept_reason") or ""),
                fallback_reason=str(posts_decision.get("fallback_reason") or ""),
                extra={
                    "page": page,
                    "cursor_in": cursor,
                    "field_completeness": posts_resp.get("_field_completeness"),
                },
            )
            posts_attempts.append(posts_attempt)
            posts_attempts_all.append(posts_attempt)
            trace.append(
                build_api_trace(
                    step=str(route["step_name"]),
                    endpoint=str(route["path"]),
                    response=posts_resp,
                    extra={
                        "page": page,
                        "cursor": cursor,
                        "route_label": route["route_label"],
                        "field_completeness": posts_resp.get("_field_completeness"),
                        "accept_reason": posts_decision.get("accept_reason"),
                        "route_accepted": bool(posts_decision.get("accepted")),
                    },
                )
            )
            request_id_candidates.append(posts_resp)
            if posts_decision.get("accepted"):
                posts_resp["_accept_reason"] = posts_decision.get("accept_reason")
                posts_accepted_routes.append(str(route["route_label"]))
                break
            posts_reason = str(posts_decision.get("fallback_reason") or "field_completeness_below_threshold")
            posts_resp["fallback_trigger_reason"] = posts_reason

        trace.append(
            {
                "step": "xhs.posts.route_decision",
                "page": page,
                "cursor_in": cursor,
                "route_plan": page_route_plan,
                "chosen_route": posts_resp.get("_route_label"),
                "request_id": posts_resp.get("request_id"),
                "field_completeness": posts_resp.get("_field_completeness"),
                "accept_reason": posts_resp.get("_accept_reason"),
                "fallback_reason": posts_reason,
                "attempted_routes": posts_attempts,
                "all_routes_failed": not any(bool(attempt.get("accepted")) for attempt in posts_attempts),
            }
        )

        if not posts_resp.get("_accept_reason"):
            posts_error_reason = "posts_contract_incomplete" if any(bool(attempt.get("ok")) for attempt in posts_attempts if not attempt.get("skipped")) else "posts_all_routes_failed"
            pagination_trace.append(
                {
                    "page": page,
                    "cursor_in": cursor,
                    "cursor_out": "",
                    "cursor_source": "missing",
                    "has_more_raw": None,
                    "has_more_normalized": None,
                    "items": 0,
                    "route_label": posts_resp.get("_route_label"),
                    "request_id": posts_resp.get("request_id"),
                    "stop_reason": posts_error_reason,
                }
            )
            break

        data = posts_resp.get("data")
        page_items = _extract_xhs_posts_items(data)
        next_cursor_raw = _extract_xhs_response_cursor(data)
        has_more_raw = _extract_xhs_posts_has_more(data)
        has_more_normalized = _normalize_has_more(has_more_raw)
        fallback_cursor = _last_xhs_note_id(page_items)
        explicit_cursor = _to_text(next_cursor_raw)
        cursor_source = "response_cursor" if explicit_cursor else ("last_note_id_fallback" if fallback_cursor else "missing")
        next_cursor = explicit_cursor or fallback_cursor

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

        next_cursor_changed = bool(next_cursor and str(next_cursor) != str(cursor))
        stop_reason = ""
        should_continue = False

        if len(works) >= max_items:
            stop_reason = "max_items_reached"
        elif not page_items:
            stop_reason = "page_empty"
        elif has_more_normalized is False:
            stop_reason = "has_more_false"
        elif next_cursor and str(next_cursor) == str(cursor):
            stop_reason = "cursor_not_advanced"
        elif has_more_normalized is True and not next_cursor:
            stop_reason = "pagination_contract_incomplete"
        elif has_more_normalized is True or next_cursor_changed:
            should_continue = True
        else:
            stop_reason = "pagination_contract_incomplete"

        if should_continue and page >= max_pages:
            should_continue = False
            stop_reason = "pages_max_reached"

        pagination_trace.append(
            {
                "page": page,
                "cursor_in": cursor,
                "cursor_out": next_cursor,
                "cursor_source": cursor_source,
                "has_more_raw": has_more_raw,
                "has_more_normalized": has_more_normalized,
                "items": len(page_items),
                "route_label": posts_resp.get("_route_label"),
                "request_id": posts_resp.get("request_id"),
                "stop_reason": stop_reason,
            }
        )

        has_more = should_continue
        if should_continue and next_cursor:
            cursor = next_cursor

    posts_route_plan = [
        build_route_plan_entry(
            route_label=str(route["route_label"]),
            endpoint=str(route["path"]),
            method="GET",
            param_readiness=str(route.get("param_readiness") or "ready"),
            param_reason=str(route.get("param_reason") or ""),
        )
        for route in _xhs_route_plan("posts", user_id=user_id, input_value=input_value, cursor="")
    ]
    posts_has_accepted = bool(posts_accepted_routes)
    if not posts_has_accepted and posts_error_reason is None:
        posts_error_reason = "posts_all_routes_failed"
    stage_status["posts"] = build_stage_status(
        stage="posts",
        status="succeeded" if posts_has_accepted else "failed",
        route_plan=posts_route_plan,
        attempted_routes=posts_attempts_all,
        chosen_route=posts_accepted_routes[0] if len(set(posts_accepted_routes)) == 1 and posts_accepted_routes else ("mixed" if posts_accepted_routes else ""),
        accept_reason="posts_pages_collected" if posts_has_accepted else "",
        fallback_reason=str(posts_error_reason or ""),
        error_reason=None if posts_has_accepted else posts_error_reason,
        all_routes_failed=not posts_has_accepted,
    )
    trace.append({"step": "xhs.posts.stage_decision", **stage_status["posts"]})

    request_id = _pick_request_id(request_id_candidates, trace)
    if progress is not None:
        progress.done(
            stage="author_home.collect",
            message="xiaohongshu author homepage collected",
            data={"works_count": len(works), "pages": len(pagination_trace), "request_id": request_id},
        )

    collect_error_reason: Optional[str] = None
    if stage_status.get("resolver", {}).get("status") == "failed":
        collect_error_reason = str(stage_status["resolver"].get("error_reason") or "author_id_unresolved")
    elif not works and stage_status.get("posts", {}).get("status") == "failed":
        collect_error_reason = stage_status["posts"].get("error_reason")
    elif stage_status.get("profile", {}).get("status") == "failed":
        collect_error_reason = stage_status["profile"].get("error_reason")

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
        "stage_status": stage_status,
        "error_reason": collect_error_reason,
    }
