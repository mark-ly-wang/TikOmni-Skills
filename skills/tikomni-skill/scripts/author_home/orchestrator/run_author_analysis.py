#!/usr/bin/env python3

if __package__ in {None, ""}:
    import sys
    from pathlib import Path

    _self = Path(__file__).resolve()
    for _parent in _self.parents:
        if (_parent / "scripts" / "core" / "bootstrap_env.py").is_file():
            sys.path.insert(0, str(_parent))
            break

"""Componentized author-home orchestrator."""

from typing import Any, Callable, Dict, List, Optional

from scripts.author_home.adapters.platform_adapters import adapt_douyin_author_home, adapt_xhs_author_home
from scripts.author_home.analyzers.prompt_first_analyzers import run_prompt_first_author_analysis
from scripts.author_home.asr.home_asr import enrich_author_home_asr
from scripts.author_home.builders.home_builders import build_author_card, build_work_cards
from scripts.author_home.collectors.homepage_collectors import collect_douyin_author_home_raw, collect_xhs_author_home_raw

CollectorFn = Callable[..., Dict[str, Any]]


def _unsupported(platform: str) -> Dict[str, Any]:
    return {
        "platform": platform,
        "content_kind": "author_home",
        "raw_content": "",
        "summary": "",
        "insights": ["source=author_home_orchestrator", "unsupported_platform"],
        "confidence": "low",
        "error_reason": f"unsupported_platform:{platform}",
        "missing_fields": [],
        "extract_trace": [],
        "fallback_trace": [],
        "request_id": None,
    }


def run_author_home_analysis(
    *,
    platform: str,
    input_value: str,
    base_url: str,
    token: str,
    timeout_ms: int,
    page_size: int = 20,
    pages_max: int = 50,
    max_items: int = 200,
    poll_interval_sec: float = 3.0,
    max_polls: int = 30,
    douyin_u2_submit_max_retries: int = 2,
    douyin_u2_submit_backoff_ms: int = 1500,
    xhs_u2_submit_max_retries: int = 0,
    xhs_u2_submit_backoff_ms: int = 0,
    u2_timeout_retry_enabled: bool = True,
    u2_timeout_retry_max_retries: int = 3,
    asr_batch_size: int = 20,
    checkpoint: Optional[Dict[str, Any]] = None,
    write_card: bool = True,
    collect_material: bool = False,
    card_root: Optional[str] = None,
    storage_config: Optional[Dict[str, Any]] = None,
    collector_override: Optional[CollectorFn] = None,
) -> Dict[str, Any]:
    # hard default policy: latest + cursor loop + max 200 across all platforms
    capped_max_items = min(max(max_items, 1), 200)
    capped_page_size = min(max(page_size, 1), 20)

    if platform == "douyin":
        collector = collector_override or collect_douyin_author_home_raw
        raw = collector(
            input_value=input_value,
            base_url=base_url,
            token=token,
            timeout_ms=timeout_ms,
            page_size=capped_page_size,
            pages_max=max(pages_max, 1),
            max_items=capped_max_items,
        )
        profile, works, adapter_missing = adapt_douyin_author_home(raw)
    elif platform == "xiaohongshu":
        collector = collector_override or collect_xhs_author_home_raw
        raw = collector(
            input_value=input_value,
            base_url=base_url,
            token=token,
            timeout_ms=timeout_ms,
            page_size=capped_page_size,
            pages_max=max(pages_max, 1),
            max_items=capped_max_items,
        )
        profile, works, adapter_missing = adapt_xhs_author_home(raw)
    else:
        return _unsupported(platform)

    # Defensive cap enforcement at orchestrator layer.
    works = works[:capped_max_items]

    asr_bundle = enrich_author_home_asr(
        platform=platform,
        works=works,
        base_url=base_url,
        token=token,
        timeout_ms=timeout_ms,
        poll_interval_sec=poll_interval_sec,
        max_polls=max_polls,
        douyin_submit_max_retries=douyin_u2_submit_max_retries,
        douyin_submit_backoff_ms=douyin_u2_submit_backoff_ms,
        xhs_submit_max_retries=xhs_u2_submit_max_retries,
        xhs_submit_backoff_ms=xhs_u2_submit_backoff_ms,
        timeout_retry_enabled=u2_timeout_retry_enabled,
        timeout_retry_max_retries=u2_timeout_retry_max_retries,
        batch_size=asr_batch_size,
        checkpoint=checkpoint,
    )
    works = list(asr_bundle.get("works") or [])[:capped_max_items]

    analysis, analysis_missing, analysis_trace = run_prompt_first_author_analysis(profile, works)

    work_card_write = build_work_cards(
        platform=platform,
        profile=profile,
        works=works,
        analysis_text=analysis.get("author_portrait", ""),
        card_root=card_root,
        storage_config=storage_config,
        collect_material=collect_material,
        write_card=write_card,
    )
    author_card_write = build_author_card(
        platform=platform,
        profile=profile,
        analysis_payload=analysis,
        card_root=card_root,
        storage_config=storage_config,
        collect_material=collect_material,
        write_card=write_card,
    )

    asr_trace = list(asr_bundle.get("trace") or [])
    all_extract_trace = list(raw.get("extract_trace") or []) + asr_trace + analysis_trace

    fallback_trace: List[Dict[str, Any]] = []
    for step in all_extract_trace:
        if not isinstance(step, dict):
            continue
        name = str(step.get("step") or "")
        try:
            has_retry = int(step.get("retry_attempt") or 0) > 0
        except Exception:
            has_retry = False
        if "fallback" in name or not step.get("ok", True) or step.get("fallback_trigger_reason") or has_retry:
            fallback_trace.append(step)

    asr_missing: List[Dict[str, str]] = []
    for item in works:
        if not isinstance(item, dict):
            continue
        if str(item.get("asr_status") or "") == "success":
            continue
        asr_missing.append(
            {
                "field": f"works[{item.get('platform_work_id') or 'unknown'}].asr",
                "reason": str(item.get("asr_error_reason") or "asr_failed"),
            }
        )

    asr_stats = asr_bundle.get("stats") if isinstance(asr_bundle.get("stats"), dict) else {}
    asr_checkpoint = asr_bundle.get("checkpoint") if isinstance(asr_bundle.get("checkpoint"), dict) else {}

    result = {
        "platform": platform,
        "content_kind": "author_home",
        "raw_content": "",
        "summary": analysis.get("author_portrait", ""),
        "insights": [
            "source=author_home_componentized",
            f"works_count={len(works)}",
            f"business_score={analysis.get('business_score', 0)}",
            f"benchmark_gap_score={analysis.get('benchmark_gap_score', 0)}",
            f"asr_success={asr_stats.get('success', 0)}",
            "analysis_strategy=prompt_first",
        ],
        "confidence": "medium" if not analysis_missing else "low",
        "error_reason": None,
        "missing_fields": adapter_missing + analysis_missing + asr_missing,
        "extract_trace": all_extract_trace,
        "fallback_trace": fallback_trace,
        "request_id": raw.get("request_id"),
        "author_profile": profile,
        "works": works,
        "pagination": {
            **(raw.get("pagination") or {}),
            "total_collected": len(works),
            "max_items": capped_max_items,
        },
        "analysis_output": analysis,
        "asr_stats": asr_stats,
        "card_write": {
            "author": author_card_write,
            "works": work_card_write,
        },
        "checkpoint": {
            "last_cursor": ((raw.get("pagination") or {}).get("pages") or [{}])[-1].get("cursor_out") if isinstance((raw.get("pagination") or {}).get("pages"), list) and (raw.get("pagination") or {}).get("pages") else "",
            "pages": len((raw.get("pagination") or {}).get("pages") or []),
            "total_collected": len(works),
            "max_items": capped_max_items,
            "sort": "latest",
            "cursor_mode": (raw.get("pagination") or {}).get("cursor_mode", "cursor"),
            "asr": asr_checkpoint,
        },
    }
    return result
