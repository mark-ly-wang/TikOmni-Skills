#!/usr/bin/env python3
"""Shared extraction pipeline helpers for runner scripts."""

from typing import Any, Dict, Optional
from urllib.parse import urlparse

from tikomni_common import call_json_api


def build_api_trace(
    *,
    step: str,
    endpoint: Optional[str],
    response: Dict[str, Any],
    extra: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    payload: Dict[str, Any] = {
        "step": step,
        "endpoint": endpoint,
        "status_code": response.get("status_code"),
        "request_id": response.get("request_id"),
        "ok": response.get("ok"),
        "error_reason": response.get("error_reason"),
    }
    if extra:
        payload.update(extra)
    return payload


def request_with_optional_fallback(
    *,
    base_url: str,
    token: str,
    timeout_ms: int,
    method: str,
    params: Optional[Dict[str, Any]],
    primary_path: str,
    fallback_path: Optional[str] = None,
) -> Dict[str, Any]:
    """Call primary endpoint, then fallback endpoint if primary fails."""
    primary = call_json_api(
        base_url=base_url,
        path=primary_path,
        token=token,
        method=method,
        timeout_ms=timeout_ms,
        params=params,
    )
    primary["_endpoint"] = primary_path
    if primary.get("ok") or not fallback_path:
        return primary

    fallback = call_json_api(
        base_url=base_url,
        path=fallback_path,
        token=token,
        method=method,
        timeout_ms=timeout_ms,
        params=params,
    )
    fallback["_endpoint"] = fallback_path
    fallback["_primary_failed"] = primary
    return fallback


def detect_platform_from_input(input_value: str) -> str:
    candidate = (input_value or "").strip().lower()
    if not candidate:
        return "unknown"

    if candidate.startswith("http://") or candidate.startswith("https://"):
        host = urlparse(candidate).netloc.lower()
        if "douyin.com" in host or "iesdouyin.com" in host:
            return "douyin"
        if "xiaohongshu.com" in host or "xhslink.com" in host:
            return "xiaohongshu"

    if "douyin" in candidate:
        return "douyin"
    if "xiaohongshu" in candidate or "xhs" in candidate:
        return "xiaohongshu"
    return "unknown"
