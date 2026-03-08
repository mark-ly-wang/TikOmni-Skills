#!/usr/bin/env python3
"""Structured stderr progress reporting for long-running TikOmni workflows.

Design goals:
- emit machine-readable progress events to stderr only
- keep final JSON stdout contract untouched
- offer a tiny shared helper so handlers do not duplicate logging logic
"""

from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from typing import Any, Dict, Optional


VALID_EVENTS = {"started", "progress", "done", "failed"}


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
        self.defaults = dict(defaults or {})

    def child(self, *, scope: str, defaults: Optional[Dict[str, Any]] = None) -> "ProgressReporter":
        merged = dict(self.defaults)
        if defaults:
            merged.update(defaults)
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
            payload["message"] = str(message)
        if self.defaults:
            payload["data"] = dict(self.defaults)
        if isinstance(data, dict) and data:
            merged = dict(payload.get("data") or {})
            merged.update(data)
            payload["data"] = merged
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
        defaults={"input_value": str(input_value or "")[:240]},
    )
