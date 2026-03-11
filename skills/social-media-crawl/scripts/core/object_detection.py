#!/usr/bin/env python3
"""Platform and object detection helpers."""

from __future__ import annotations

import urllib.request
from dataclasses import dataclass, asdict
from typing import Dict
from urllib.parse import urlparse


@dataclass
class DetectionResult:
    input_value: str
    resolved_url: str
    platform: str
    object_type: str

    def to_dict(self) -> Dict[str, str]:
        return asdict(self)


def resolve_final_url(input_value: str, timeout_ms: int = 10000) -> str:
    candidate = str(input_value or "").strip()
    if not candidate.startswith(("http://", "https://")):
        return candidate
    try:
        request = urllib.request.Request(candidate, method="GET")
        with urllib.request.urlopen(request, timeout=max(timeout_ms / 1000.0, 1.0)) as response:
            return response.geturl() or candidate
    except Exception:
        return candidate


def detect_target(input_value: str, timeout_ms: int = 10000) -> DetectionResult:
    raw = str(input_value or "").strip()
    resolved = resolve_final_url(raw, timeout_ms=timeout_ms)
    candidate = resolved or raw
    lower = candidate.lower()
    host = urlparse(lower).netloc

    platform = "unknown"
    object_type = "unknown"

    if any(token in host for token in ["douyin.com", "iesdouyin.com"]):
        platform = "douyin"
        if "/video/" in lower:
            object_type = "work"
        elif "/user/" in lower or "sec_uid=" in lower or "sec_user_id=" in lower:
            object_type = "creator"
    elif any(token in host for token in ["xiaohongshu.com", "xhslink.com"]):
        platform = "xiaohongshu"
        if any(token in lower for token in ["/discovery/item/", "/explore/"]):
            object_type = "work"
        elif any(token in lower for token in ["/user/profile/", "/user/", "/profile/"]):
            object_type = "creator"

    return DetectionResult(
        input_value=raw,
        resolved_url=resolved or raw,
        platform=platform,
        object_type=object_type,
    )
