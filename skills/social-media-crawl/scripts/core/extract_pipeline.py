#!/usr/bin/env python3
"""Shared extraction pipeline helpers for runner scripts."""

from typing import Any, Dict, List, Optional
from urllib.parse import urlparse

from scripts.core.tikomni_common import call_json_api


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
        "rate_limit_wait_ms": response.get("rate_limit_wait_ms", 0),
        "retry_attempt": response.get("retry_attempt", 0),
        "fallback_trigger_reason": response.get("fallback_trigger_reason"),
    }
    if extra:
        payload.update(extra)
    return payload


def build_route_plan_entry(
    *,
    route_label: str,
    endpoint: Optional[str],
    method: str = "GET",
    param_readiness: str = "ready",
    param_reason: str = "",
) -> Dict[str, Any]:
    return {
        "route_label": route_label,
        "endpoint": endpoint,
        "method": method.upper(),
        "param_readiness": param_readiness,
        "param_reason": param_reason,
    }


def build_attempted_route(
    *,
    route_label: str,
    endpoint: Optional[str],
    response: Optional[Dict[str, Any]] = None,
    accepted: bool = False,
    accept_reason: str = "",
    fallback_reason: str = "",
    param_readiness: str = "ready",
    param_reason: str = "",
    skipped: bool = False,
    extra: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    attempt: Dict[str, Any] = {
        "route_label": route_label,
        "endpoint": endpoint,
        "accepted": bool(accepted),
        "accept_reason": accept_reason,
        "fallback_reason": fallback_reason,
        "param_readiness": param_readiness,
        "param_reason": param_reason,
        "skipped": bool(skipped),
    }
    if isinstance(response, dict):
        attempt.update(
            {
                "ok": response.get("ok"),
                "status_code": response.get("status_code"),
                "request_id": response.get("request_id"),
                "error_reason": response.get("error_reason"),
                "retry_attempt": response.get("retry_attempt", 0),
                "rate_limit_wait_ms": response.get("rate_limit_wait_ms", 0),
            }
        )
    else:
        attempt.update(
            {
                "ok": None,
                "status_code": None,
                "request_id": None,
                "error_reason": None,
                "retry_attempt": 0,
                "rate_limit_wait_ms": 0,
            }
        )
    if extra:
        attempt.update(extra)
    return attempt


def build_stage_status(
    *,
    stage: str,
    status: str,
    route_plan: Optional[List[Dict[str, Any]]] = None,
    attempted_routes: Optional[List[Dict[str, Any]]] = None,
    chosen_route: Optional[str] = None,
    accept_reason: str = "",
    fallback_reason: str = "",
    error_reason: Optional[str] = None,
    all_routes_failed: bool = False,
) -> Dict[str, Any]:
    return {
        "stage": stage,
        "status": status,
        "route_plan": list(route_plan or []),
        "attempted_routes": list(attempted_routes or []),
        "chosen_route": chosen_route or "",
        "accept_reason": accept_reason,
        "fallback_reason": fallback_reason,
        "error_reason": error_reason,
        "all_routes_failed": bool(all_routes_failed),
    }


def build_fallback_trace_from_extract_trace(extract_trace: Optional[List[Dict[str, Any]]]) -> List[Dict[str, Any]]:
    """Build a compact fallback trace from runner extract trace."""
    if not extract_trace:
        return []

    trace: List[Dict[str, Any]] = []
    include_tokens = ("primary", "effective", "fallback", "gate", "retry", "attempt", "route_decision")

    for step in extract_trace:
        if not isinstance(step, dict):
            continue

        step_name = str(step.get("step") or "")
        if not step_name:
            continue

        has_fallback_signal = any(token in step_name for token in include_tokens)
        if not has_fallback_signal:
            continue

        compact: Dict[str, Any] = {"step": step_name}
        for key in (
            "endpoint",
            "ok",
            "status_code",
            "request_id",
            "error_reason",
            "gate_reason",
            "final_submit_status",
            "subtitle_hit",
            "force_u2_fallback",
            "rate_limit_wait_ms",
            "retry_attempt",
            "fallback_trigger_reason",
        ):
            if key in step:
                compact[key] = step.get(key)
        trace.append(compact)

    return trace


def resolve_trace_error_context(
    *,
    responses: Optional[List[Optional[Dict[str, Any]]]] = None,
    extract_trace: Optional[List[Dict[str, Any]]] = None,
    explicit_error_reason: Optional[str] = None,
    default_error_reason: Optional[str] = None,
    explicit_request_id: Optional[str] = None,
) -> Dict[str, Any]:
    """Resolve consistent error/request/fallback fields for result envelopes."""
    chain = [item for item in (responses or []) if isinstance(item, dict)]

    request_id = explicit_request_id
    if not request_id:
        for response in chain:
            candidate = response.get("request_id")
            if candidate:
                request_id = str(candidate)
                break

    error_reason = explicit_error_reason
    if not error_reason:
        for response in chain:
            candidate = response.get("error_reason")
            if candidate:
                error_reason = str(candidate)
                break
    if not error_reason:
        error_reason = default_error_reason

    return {
        "request_id": request_id,
        "error_reason": error_reason,
        "fallback_trace": build_fallback_trace_from_extract_trace(extract_trace),
    }


def _resolve_fallback_trigger_reason(primary: Dict[str, Any]) -> str:
    if primary.get("timeout_retry_exhausted"):
        return "primary_timeout_retry_exhausted"
    if primary.get("error_reason"):
        return "primary_non_timeout_failure"
    return "primary_unknown_failure"


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

    fallback_reason = _resolve_fallback_trigger_reason(primary)
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
    fallback["fallback_trigger_reason"] = fallback_reason
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
