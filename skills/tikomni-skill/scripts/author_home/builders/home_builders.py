#!/usr/bin/env python3
"""Builders for author-home outputs.

Hard rule: single-work cards reuse existing writer implementation.
"""

from __future__ import annotations

from typing import Any, Dict, List, Optional


def _coerce_unix_sec(value: Any) -> int:
    try:
        if value is None:
            return 0
        if isinstance(value, (int, float)):
            parsed = int(value)
        else:
            text = str(value).strip()
            if not text:
                return 0
            parsed = int(float(text))
        if parsed > 1_000_000_000_000:
            parsed //= 1000
        return parsed if parsed > 0 else 0
    except Exception:
        return 0

from scripts.writers.write_benchmark_card import write_benchmark_card


def _work_payload(work: Dict[str, Any], profile: Dict[str, Any], analysis_text: str) -> Dict[str, Any]:
    metrics = work.get("metrics") if isinstance(work.get("metrics"), dict) else {}
    author = {
        "nickname": profile.get("nickname"),
        "author_platform_id": profile.get("author_platform_id") or profile.get("platform_author_id"),
        "author_handle": profile.get("author_handle") or "",
    }
    publish_time = work.get("publish_time")
    create_time_sec = _coerce_unix_sec(publish_time)
    return {
        "content_kind": "author_home",
        "platform_work_id": work.get("platform_work_id"),
        "title": work.get("title") or work.get("desc"),
        "desc": work.get("desc") or work.get("title"),
        "source_url": work.get("source_url"),
        "share_url": work.get("share_url"),
        "cover_image": work.get("cover_image"),
        "author": author,
        "author_handle": author.get("author_handle"),
        "author_platform_id": author.get("author_platform_id"),
        "publish_time": publish_time,
        "publish_time_source": "author_home.work.publish_time",
        "create_time_sec": create_time_sec,
        "digg_count": int(metrics.get("like", 0) or 0),
        "comment_count": int(metrics.get("comment", 0) or 0),
        "collect_count": int(metrics.get("collect", 0) or 0),
        "share_count": int(metrics.get("share", 0) or 0),
        "play_count": int(metrics.get("play", 0) or 0),
        "summary": analysis_text or "",
        "insights": ["source=author_home_componentized", "work_card_reused_writer"],
        "raw_content": work.get("desc") or "",
    }


def build_work_cards(
    *,
    platform: str,
    profile: Dict[str, Any],
    works: List[Dict[str, Any]],
    analysis_text: str,
    card_root: Optional[str],
    storage_config: Optional[Dict[str, Any]],
    collect_material: bool,
    write_card: bool,
) -> Dict[str, Any]:
    if not write_card:
        return {"enabled": False, "count": 0, "results": []}

    sample_author = str(profile.get("nickname") or profile.get("platform_author_id") or "作者")
    results: List[Dict[str, Any]] = []

    for work in works:
        payload = _work_payload(work, profile, analysis_text)
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

    return {"enabled": True, "count": len(results), "results": results}


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
