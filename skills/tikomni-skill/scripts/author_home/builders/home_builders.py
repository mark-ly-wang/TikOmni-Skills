#!/usr/bin/env python3
"""Builders for author-home outputs.

Hard rule: single-work cards reuse existing writer implementation.
"""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from scripts.writers.write_benchmark_card import write_benchmark_card


def build_work_cards(
    *,
    platform: str,
    profile: Dict[str, Any],
    works: List[Dict[str, Any]],
    render_payloads: Dict[str, Dict[str, Any]],
    card_root: Optional[str],
    storage_config: Optional[Dict[str, Any]],
    collect_material: bool,
    write_card: bool,
    failed_items: Optional[List[Dict[str, Any]]] = None,
) -> Dict[str, Any]:
    if not write_card:
        return {"enabled": False, "count": 0, "results": []}

    sample_author = str(profile.get("nickname") or profile.get("platform_author_id") or "作者")
    results: List[Dict[str, Any]] = []
    unresolved: List[Dict[str, Any]] = list(failed_items or [])

    for work in works:
        platform_work_id = str(work.get("platform_work_id") or "").strip()
        payload = render_payloads.get(platform_work_id)
        if not isinstance(payload, dict):
            unresolved.append(
                {
                    "platform_work_id": platform_work_id,
                    "error_reason": "missing_work_analysis_artifact",
                }
            )
            continue
        result = write_benchmark_card(
            payload=payload,
            platform=platform,
            card_type="author_sample_work",
            card_root=card_root,
            collect_material=collect_material,
            sample_author=sample_author,
            content_kind="author_home",
            storage_config=storage_config,
        )
        results.append(result)

    return {
        "enabled": True,
        "count": len(results),
        "results": results,
        "failed_items": unresolved,
    }


def build_author_card(
    *,
    platform: str,
    profile: Dict[str, Any],
    analysis_payload: Dict[str, Any],
    card_root: Optional[str],
    storage_config: Optional[Dict[str, Any]],
    collect_material: bool,
    write_card: bool,
) -> Dict[str, Any]:
    if not write_card:
        return {"enabled": False, "skipped": True, "reason": "write_card_disabled"}

    payload = {
        "content_kind": "author_analysis",
        "title": f"{profile.get('nickname') or profile.get('platform_author_id') or '作者'} 主页画像",
        "desc": profile.get("signature") or "",
        "summary": analysis_payload.get("author_portrait", ""),
        "insights": [
            f"business_score={analysis_payload.get('business_score', 0)}",
            f"benchmark_gap_score={analysis_payload.get('benchmark_gap_score', 0)}",
        ],
        "author": {
            "nickname": profile.get("nickname"),
            "author_platform_id": profile.get("author_platform_id") or profile.get("platform_author_id"),
            "author_handle": profile.get("author_handle") or "",
        },
        "author_handle": profile.get("author_handle") or "",
        "author_platform_id": profile.get("author_platform_id") or profile.get("platform_author_id"),
        "digg_count": int(profile.get("liked_count", 0) or 0),
        "collect_count": int(profile.get("collected_count", 0) or 0),
        "play_count": 0,
        "raw_content": analysis_payload.get("business_analysis", ""),
        "platform_work_id": f"author-{profile.get('platform_author_id') or 'unknown'}",
        "analysis_output": analysis_payload,
        "business_score": int(analysis_payload.get("business_score", 0) or 0),
        "benchmark_gap_score": int(analysis_payload.get("benchmark_gap_score", 0) or 0),
        "style_radar": analysis_payload.get("style_radar") if isinstance(analysis_payload.get("style_radar"), dict) else {},
        "core_contradictions": analysis_payload.get("core_contradictions") if isinstance(analysis_payload.get("core_contradictions"), list) else [],
        "recommendations": analysis_payload.get("recommendations") if isinstance(analysis_payload.get("recommendations"), list) else [],
        "business_analysis": analysis_payload.get("business_analysis", ""),
        "benchmark_analysis": analysis_payload.get("benchmark_analysis", ""),
    }

    return write_benchmark_card(
        payload=payload,
        platform=platform,
        card_type="author",
        card_root=card_root,
        collect_material=collect_material,
        sample_author=None,
        content_kind="author_analysis",
        storage_config=storage_config,
    )
