#!/usr/bin/env python3
"""Structured stderr progress reporting for long-running TikOmni workflows."""

from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from typing import Any, Dict, Optional
from urllib.parse import urlparse


VALID_EVENTS = {"started", "progress", "done", "failed"}
_MASKED_TEXT = "<redacted>"
_MAX_TEXT_PREVIEW = 180
_MAX_LIST_ITEMS = 8
_SENSITIVE_KEYS = {
    "api_key",
    "authorization",
    "cookie",
    "cookies",
    "set_cookie",
    "token",
    "xsec_token",
}
_LONG_TEXT_KEYS = {
    "asr_clean",
    "asr_raw",
    "prompt",
    "prompt_text",
    "raw_content",
    "stderr",
    "stdout",
    "transcript",
    "transcript_text",
}


def _looks_like_url(text: str) -> bool:
    return text.startswith("http://") or text.startswith("https://")


def _mask_key(key: str) -> bool:
    lowered = key.lower()
    if lowered in _SENSITIVE_KEYS:
        return True
    return any(token in lowered for token in ("api_key", "token", "cookie", "authorization"))


def _sanitize_url(text: str) -> str:
    try:
        parsed = urlparse(text)
    except Exception:
        return text[:_MAX_TEXT_PREVIEW]
    if not parsed.scheme or not parsed.netloc:
        return text[:_MAX_TEXT_PREVIEW]
    return f"{parsed.scheme}://{parsed.netloc}{parsed.path}"


def _truncate_text(text: str) -> str:
    if len(text) <= _MAX_TEXT_PREVIEW:
        return text
    return f"{text[:_MAX_TEXT_PREVIEW]}…(len={len(text)})"


def _sanitize_scalar(value: Any, *, key: str = "") -> Any:
    if value is None or isinstance(value, (bool, int, float)):
        return value

    text = str(value)
    if _mask_key(key):
        return _MASKED_TEXT
    if key.lower() in _LONG_TEXT_KEYS:
        return f"<redacted:{key}:len={len(text)}>"
    if _looks_like_url(text):
        return _sanitize_url(text)
    return _truncate_text(text)


def _sanitize_payload(value: Any, *, key: str = "") -> Any:
    if isinstance(value, dict):
        sanitized: Dict[str, Any] = {}
        for child_key, child_value in value.items():
            child_key_text = str(child_key)
            if _mask_key(child_key_text):
                sanitized[child_key_text] = _MASKED_TEXT
                continue
            sanitized[child_key_text] = _sanitize_payload(child_value, key=child_key_text)
        return sanitized

    if isinstance(value, list):
        items = value[:_MAX_LIST_ITEMS]
        sanitized_items = [_sanitize_payload(item, key=key) for item in items]
        if len(value) > _MAX_LIST_ITEMS:
            sanitized_items.append(f"...({len(value) - _MAX_LIST_ITEMS} more)")
        return sanitized_items

    return _sanitize_scalar(value, key=key)


class ProgressReporter:
    def __init__(
        self,
        *,
        workflow: str,
        platform: str,
        content_kind: str,
        run_id: Optional[str] = None,
        scope: str = "workflow",
        enabled: bool = True,
        defaults: Optional[Dict[str, Any]] = None,
    ) -> None:
        self.workflow = str(workflow or "unknown")
        self.platform = str(platform or "unknown")
        self.content_kind = str(content_kind or "unknown")
        self.run_id = str(run_id or f"{self.platform}.{self.content_kind}")
        self.scope = str(scope or "workflow")
        self.enabled = bool(enabled)
        self.defaults = _sanitize_payload(dict(defaults or {}))

    def child(self, *, scope: str, defaults: Optional[Dict[str, Any]] = None) -> "ProgressReporter":
        merged = dict(self.defaults)
        if defaults:
            merged.update(_sanitize_payload(defaults))
        return ProgressReporter(
            workflow=self.workflow,
            platform=self.platform,
            content_kind=self.content_kind,
            run_id=self.run_id,
            scope=scope,
            enabled=self.enabled,
            defaults=merged,
        )

    def emit(self, event: str, *, stage: str, message: str = "", data: Optional[Dict[str, Any]] = None) -> None:
        if not self.enabled:
            return
        normalized_event = str(event or "progress").strip().lower()
        if normalized_event not in VALID_EVENTS:
            normalized_event = "progress"
        payload: Dict[str, Any] = {
            "channel": "tikomni_progress",
            "ts": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "workflow": self.workflow,
            "platform": self.platform,
            "content_kind": self.content_kind,
            "run_id": self.run_id,
            "scope": self.scope,
            "event": normalized_event,
            "stage": str(stage or "unknown"),
        }
        if message:
            payload["message"] = _truncate_text(str(message))
        merged_data = dict(self.defaults)
        if isinstance(data, dict) and data:
            merged_data.update(_sanitize_payload(data))
        if merged_data:
            payload["data"] = merged_data
        sys.stderr.write(json.dumps(payload, ensure_ascii=False) + "\n")
        sys.stderr.flush()

    def started(self, *, stage: str, message: str = "", data: Optional[Dict[str, Any]] = None) -> None:
        self.emit("started", stage=stage, message=message, data=data)

    def progress(self, *, stage: str, message: str = "", data: Optional[Dict[str, Any]] = None) -> None:
        self.emit("progress", stage=stage, message=message, data=data)

    def done(self, *, stage: str, message: str = "", data: Optional[Dict[str, Any]] = None) -> None:
        self.emit("done", stage=stage, message=message, data=data)

    def failed(self, *, stage: str, message: str = "", data: Optional[Dict[str, Any]] = None) -> None:
        self.emit("failed", stage=stage, message=message, data=data)

    def heartbeat(self, *, stage: str, message: str = "", data: Optional[Dict[str, Any]] = None) -> None:
        heartbeat_data = dict(data or {})
        heartbeat_data["heartbeat"] = True
        self.progress(stage=stage, message=message or "heartbeat", data=heartbeat_data)

    def http_event(
        self,
        *,
        stage: str,
        endpoint: str,
        response: Optional[Dict[str, Any]],
        summary: Optional[Dict[str, Any]] = None,
        route_label: Optional[str] = None,
    ) -> None:
        payload: Dict[str, Any] = {
            "kind": "http",
            "endpoint": endpoint,
        }
        if route_label:
            payload["route_label"] = route_label
        if isinstance(response, dict):
            payload.update(
                {
                    "ok": bool(response.get("ok")),
                    "status_code": response.get("status_code"),
                    "request_id": response.get("request_id"),
                    "attempt": int(response.get("retry_attempt", 0)) + 1,
                    "fallback_trigger_reason": response.get("fallback_trigger_reason"),
                    "timeout_retry_exhausted": bool(response.get("timeout_retry_exhausted")),
                }
            )
        if isinstance(summary, dict) and summary:
            payload["summary"] = summary
        event_fn = self.done if isinstance(response, dict) and response.get("ok") else self.failed
        event_fn(stage=stage, message="http request finished", data=payload)

    def subprocess_event(
        self,
        *,
        stage: str,
        provider: str,
        operation: str,
        event: str,
        duration_ms: Optional[int] = None,
        exit_code: Optional[int] = None,
        summary: Optional[Dict[str, Any]] = None,
    ) -> None:
        payload: Dict[str, Any] = {
            "kind": "subprocess",
            "provider": provider,
            "operation": operation,
        }
        if duration_ms is not None:
            payload["duration_ms"] = int(duration_ms)
        if exit_code is not None:
            payload["exit_code"] = int(exit_code)
        if isinstance(summary, dict) and summary:
            payload["summary"] = summary

        if event == "started":
            self.started(stage=stage, message="subprocess started", data=payload)
        elif event == "done":
            self.done(stage=stage, message="subprocess finished", data=payload)
        elif event == "failed":
            self.failed(stage=stage, message="subprocess failed", data=payload)
        else:
            self.progress(stage=stage, message="subprocess progress", data=payload)


def build_progress_reporter(
    *,
    workflow: str,
    platform: str,
    content_kind: str,
    input_value: Optional[str] = None,
    enabled: bool = True,
) -> ProgressReporter:
    return ProgressReporter(
        workflow=workflow,
        platform=platform,
        content_kind=content_kind,
        run_id=f"{platform}.{content_kind}",
        enabled=enabled,
        defaults={"input_value": _sanitize_scalar(str(input_value or ""), key="input_value")},
    )
