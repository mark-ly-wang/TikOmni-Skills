#!/usr/bin/env python3
"""Completeness evaluation helpers."""

from __future__ import annotations

import hashlib
import time
from typing import Any, Dict, List, Optional


def normalize_missing_fields(items: Any) -> List[Dict[str, str]]:
    normalized: List[Dict[str, str]] = []
    seen = set()
    if not isinstance(items, list):
        return normalized
    for item in items:
        if isinstance(item, dict):
            field = str(item.get("field") or "").strip()
            reason = str(item.get("reason") or "").strip() or "missing"
        else:
            field = str(item or "").strip()
            reason = "missing"
        if not field:
            continue
        key = (field, reason)
        if key in seen:
            continue
        seen.add(key)
        normalized.append({"field": field, "reason": reason})
    return normalized


def ensure_request_id(value: Optional[str], fallback_seed: str = "") -> str:
    text = str(value or "").strip()
    if text:
        return text
    digest = hashlib.sha1(fallback_seed.encode("utf-8")).hexdigest()[:8] if fallback_seed else "unknown"
    return f"local-{int(time.time())}-{digest}"


def evaluate_work_fact_card(card: Dict[str, Any]) -> Dict[str, Any]:
    missing = normalize_missing_fields(card.get("missing_fields"))
    existing_fields = {entry["field"] for entry in missing}

    required_pairs = [
        ("platform", bool(str(card.get("platform") or "").strip())),
        ("platform_work_id", bool(str(card.get("platform_work_id") or "").strip())),
        ("platform_author_id", bool(str(card.get("platform_author_id") or "").strip())),
        ("author_handle", bool(str(card.get("author_handle") or "").strip())),
        ("title", bool(str(card.get("title") or "").strip())),
        ("source_url", bool(str(card.get("source_url") or "").strip())),
        ("share_url", bool(str(card.get("share_url") or "").strip())),
    ]
    for field, ok in required_pairs:
        if ok or field in existing_fields:
            continue
        missing.append({"field": field, "reason": "missing_required"})
        existing_fields.add(field)

    primary_text = str(card.get("primary_text") or "").strip()
    if not primary_text and "primary_text" not in existing_fields:
        missing.append({"field": "primary_text", "reason": "missing_primary_text"})

    required_missing = [entry for entry in missing if entry["reason"] == "missing_required"]
    if required_missing:
        completeness = "incomplete"
    elif primary_text:
        completeness = "complete"
    else:
        completeness = "partial"

    return {
        "completeness": completeness,
        "missing_fields": missing,
    }


def evaluate_collection(profile: Dict[str, Any], works: List[Dict[str, Any]]) -> str:
    if not str(profile.get("platform_author_id") or "").strip():
        return "incomplete"
    if works:
        return "complete"
    return "partial"
