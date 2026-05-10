#!/usr/bin/env python3
"""Resolve a TikOmni API endpoint_id from platform and capability."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

SKILL_ROOT = Path(__file__).resolve().parents[2]
if str(SKILL_ROOT) not in sys.path:
    sys.path.insert(0, str(SKILL_ROOT))

from scripts.core.api_catalog import (
    infer_alias_from_text,
    load_aliases,
    load_operations,
    resolve_alias,
    sorted_operations,
)


def _json_stdout(payload: Dict[str, Any]) -> None:
    print(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True))


def _load_context(raw_json: Optional[str]) -> Dict[str, Any]:
    if not raw_json:
        return {}
    try:
        payload = json.loads(raw_json)
    except Exception:
        return {"_raw": raw_json}
    return payload if isinstance(payload, dict) else {"value": payload}


def _suggestions(platform: str, capability: str, operations: List[Dict[str, Any]]) -> List[Dict[str, str]]:
    suggestions: List[Dict[str, str]] = []
    if platform == "wechat" and capability.startswith("article"):
        suggestions.append({"platform": "wechat_mp", "capability": capability})
    if platform == "wechat" and capability in {"video_detail", "comments", "search", "hot_search"}:
        suggestions.append({"platform": "wechat_channels", "capability": capability})

    for operation in operations:
        if capability and operation.get("capability") != capability:
            continue
        item = {
            "platform": str(operation.get("platform") or ""),
            "capability": str(operation.get("capability") or ""),
        }
        if item["platform"] and item not in suggestions:
            suggestions.append(item)
        if len(suggestions) >= 8:
            break
    return suggestions


def resolve_endpoint(
    *,
    platform: str = "",
    capability: str = "",
    intent: str = "",
    url: str = "",
    context: Optional[Dict[str, Any]] = None,
    include_demo: bool = False,
) -> Dict[str, Any]:
    aliases = load_aliases()
    operations = load_operations()
    context = context or {}

    platform_aliases = aliases.get("platforms") if isinstance(aliases.get("platforms"), dict) else {}
    capability_aliases = aliases.get("capabilities") if isinstance(aliases.get("capabilities"), dict) else {}
    text = " ".join(
        str(value)
        for value in [
            intent,
            url,
            context.get("intent"),
            context.get("url"),
            context.get("share_url"),
            context.get("input"),
        ]
        if value
    )

    resolved_platform = resolve_alias(platform, platform_aliases)
    if not resolved_platform:
        resolved_platform = infer_alias_from_text(text, platform_aliases)

    resolved_capability = resolve_alias(capability, capability_aliases)
    if not resolved_capability:
        resolved_capability = infer_alias_from_text(text, capability_aliases)

    if not resolved_platform or not resolved_capability:
        return {
            "ok": False,
            "code": "ENDPOINT_NOT_RESOLVED",
            "message": "platform and capability are required for deterministic API endpoint resolution.",
            "platform": resolved_platform,
            "capability": resolved_capability,
            "suggestions": _suggestions(resolved_platform, resolved_capability, operations),
        }

    candidates = [
        operation
        for operation in operations
        if operation.get("platform") == resolved_platform
        and operation.get("capability") == resolved_capability
        and (include_demo or not operation.get("demo"))
    ]
    if not candidates:
        return {
            "ok": False,
            "code": "ENDPOINT_NOT_RESOLVED",
            "message": (
                "No TikOmni public API endpoint matches "
                f"platform={resolved_platform} capability={resolved_capability}."
            ),
            "platform": resolved_platform,
            "capability": resolved_capability,
            "suggestions": _suggestions(resolved_platform, resolved_capability, operations),
        }

    ordered = sorted_operations(candidates)
    recommended = ordered[0]
    alternatives = [
        {
            "endpoint_id": str(operation.get("endpoint_id") or ""),
            "variant": str(operation.get("variant") or ""),
            "method": str(operation.get("method") or ""),
            "path": str(operation.get("path") or ""),
            "summary": str(operation.get("summary") or ""),
        }
        for operation in ordered[1:]
    ]
    return {
        "ok": True,
        "platform": resolved_platform,
        "capability": resolved_capability,
        "recommended": {
            "endpoint_id": str(recommended.get("endpoint_id") or ""),
            "method": str(recommended.get("method") or ""),
            "path": str(recommended.get("path") or ""),
            "variant": str(recommended.get("variant") or ""),
            "summary": str(recommended.get("summary") or ""),
        },
        "alternatives": alternatives,
        "reason": "catalog_recommended_or_variant_priority",
    }


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Resolve a TikOmni API endpoint_id.")
    parser.add_argument("--platform", default="")
    parser.add_argument("--capability", default="")
    parser.add_argument("--intent", default="")
    parser.add_argument("--url", default="")
    parser.add_argument("--json", default="", help="Optional JSON context.")
    parser.add_argument("--include-demo", action="store_true")
    args = parser.parse_args(argv)
    payload = resolve_endpoint(
        platform=args.platform,
        capability=args.capability,
        intent=args.intent,
        url=args.url,
        context=_load_context(args.json),
        include_demo=bool(args.include_demo),
    )
    _json_stdout(payload)
    return 0 if payload.get("ok") else 2


if __name__ == "__main__":
    sys.exit(main())
