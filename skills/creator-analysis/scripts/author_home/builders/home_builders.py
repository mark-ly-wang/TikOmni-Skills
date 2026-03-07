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
    write_card: bool,
) -> Dict[str, Any]:
    if not write_card:
        return {"enabled": False, "skipped": True, "reason": "write_card_disabled"}

    author_analysis_v2 = analysis_payload.get("author_analysis_v2") if isinstance(analysis_payload.get("author_analysis_v2"), dict) else {}
    positioning = author_analysis_v2.get("author_positioning") if isinstance(author_analysis_v2.get("author_positioning"), dict) else {}
    trust_model = author_analysis_v2.get("trust_model") if isinstance(author_analysis_v2.get("trust_model"), dict) else {}
    content_mechanism = author_analysis_v2.get("content_mechanism") if isinstance(author_analysis_v2.get("content_mechanism"), dict) else {}
    commercial_bridge = author_analysis_v2.get("commercial_bridge") if isinstance(author_analysis_v2.get("commercial_bridge"), dict) else {}
    core_tensions = author_analysis_v2.get("core_tensions") if isinstance(author_analysis_v2.get("core_tensions"), dict) else {}
    clone_guidance = author_analysis_v2.get("clone_guidance") if isinstance(author_analysis_v2.get("clone_guidance"), dict) else {}

    winning_structures = list(content_mechanism.get("winning_content_structures") or [])[:3] if isinstance(content_mechanism.get("winning_content_structures"), list) else []
    likely_products = list(commercial_bridge.get("likely_products") or [])[:3] if isinstance(commercial_bridge.get("likely_products"), list) else []
    author_card_highlights = {
        "one_liner": positioning.get("one_liner") or analysis_payload.get("author_portrait", ""),
        "core_value_proposition": positioning.get("core_value_proposition") or "",
        "primary_trust_source": trust_model.get("primary_trust_source") or "",
        "winning_content_structures": winning_structures,
        "likely_products": likely_products,
        "most_important_tension": core_tensions.get("most_important_tension") or "",
        "if_only_learn_one_thing": clone_guidance.get("if_only_learn_one_thing") or "",
    }

    payload = {
        "content_kind": "author_analysis",
        "title": f"{profile.get('nickname') or profile.get('platform_author_id') or '作者'} 主页画像",
        "desc": profile.get("signature") or "",
        "summary": author_card_highlights.get("one_liner") or analysis_payload.get("author_portrait", ""),
        "insights": [
            f"business_score={analysis_payload.get('business_score', 0)}",
            f"benchmark_gap_score={analysis_payload.get('benchmark_gap_score', 0)}",
            f"trust_source={author_card_highlights.get('primary_trust_source') or 'unknown'}",
        ],
        "author": {
            "nickname": profile.get("nickname"),
            "author_platform_id": profile.get("author_platform_id") or profile.get("platform_author_id"),
            "author_handle": profile.get("author_handle") or "",
        },
        "author_handle": profile.get("author_handle") or "",
        "author_platform_id": profile.get("author_platform_id") or profile.get("platform_author_id"),
        "nickname": profile.get("nickname") or "",
        "ip_location": profile.get("ip_location") or "",
        "signature": profile.get("signature") or "",
        "avatar_url": profile.get("avatar_url") or "",
        "fans_count": int(profile.get("fans_count", 0) or 0),
        "liked_count": int(profile.get("liked_count", 0) or 0),
        "collected_count": int(profile.get("collected_count", 0) or 0),
        "works_count": int(profile.get("works_count", 0) or 0),
        "verified": bool(profile.get("verified", False)),
        "snapshot_at": profile.get("snapshot_at") or "",
        "digg_count": int(profile.get("liked_count", 0) or 0),
        "collect_count": int(profile.get("collected_count", 0) or 0),
        "play_count": 0,
        "raw_content": analysis_payload.get("business_analysis", ""),
        "platform_work_id": f"author-{profile.get('platform_author_id') or 'unknown'}",
        "analysis_output": analysis_payload,
        "author_analysis_v2": author_analysis_v2,
        "author_analysis_input_v1": analysis_payload.get("author_analysis_input_v1") if isinstance(analysis_payload.get("author_analysis_input_v1"), dict) else {},
        "sampled_work_explanations": analysis_payload.get("sampled_work_explanations") if isinstance(analysis_payload.get("sampled_work_explanations"), dict) else {},
        "author_card_highlights": author_card_highlights,
        "business_score": int(analysis_payload.get("business_score", 0) or 0),
        "benchmark_gap_score": int(analysis_payload.get("benchmark_gap_score", 0) or 0),
        "style_radar": analysis_payload.get("style_radar") if isinstance(analysis_payload.get("style_radar"), dict) else {},
        "core_contradictions": analysis_payload.get("core_contradictions") if isinstance(analysis_payload.get("core_contradictions"), list) else [],
        "recommendations": analysis_payload.get("recommendations") if isinstance(analysis_payload.get("recommendations"), list) else [],
        "business_analysis": analysis_payload.get("business_analysis", ""),
        "benchmark_analysis": analysis_payload.get("benchmark_analysis", ""),
        "validation": analysis_payload.get("validation") if isinstance(analysis_payload.get("validation"), dict) else {},
    }

    return write_benchmark_card(
        payload=payload,
        platform=platform,
        card_type="author",
        card_root=card_root,
        sample_author=None,
        content_kind="author_analysis",
        storage_config=storage_config,
    )
