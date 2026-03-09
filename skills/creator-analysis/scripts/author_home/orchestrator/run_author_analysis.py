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

import hashlib
import json
from datetime import datetime
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional

from scripts.core.config_loader import resolve_storage_paths
from scripts.core.storage_router import render_output_filename, resolve_json_filename_pattern

from scripts.author_home.adapters.platform_adapters import adapt_douyin_author_home, adapt_xhs_author_home
from scripts.author_home.analyzers.author_analysis_v2_support import prepare_author_analysis_bundle
from scripts.author_home.orchestrator.work_analysis_artifacts import orchestrate_work_analysis_artifacts
from scripts.core.progress_report import ProgressReporter
from scripts.author_home.analyzers.prompt_first_analyzers import run_prompt_first_author_analysis
from scripts.author_home.asr.home_asr import enrich_author_home_asr
from scripts.author_home.builders.home_builders import build_author_card, build_work_cards
from scripts.author_home.collectors.homepage_collectors import collect_douyin_author_home_raw, collect_xhs_author_home_raw

CollectorFn = Callable[..., Dict[str, Any]]


def _stage_status(*, status: str, ok_count: int, failed_count: int, degraded_count: int, reason_codes: List[str], failure_kind: str = "") -> Dict[str, Any]:
    return {
        "status": status,
        "ok_count": ok_count,
        "failed_count": failed_count,
        "degraded_count": degraded_count,
        "reason_codes": list(dict.fromkeys([code for code in reason_codes if code])),
        "failure_kind": failure_kind or None,
    }


def _reason_codes_from_failed_items(items: List[Dict[str, Any]]) -> List[str]:
    reason_codes: List[str] = []
    for item in items:
        if not isinstance(item, dict):
            continue
        reason = str(item.get("error_reason") or "").strip()
        if not reason:
            continue
        reason_codes.append(reason.split(":", 1)[0])
    return list(dict.fromkeys(reason_codes))


def _merge_normalized_works(*, works: List[Dict[str, Any]], normalized_works: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    normalized_map = {
        str(item.get("platform_work_id") or "").strip(): item
        for item in normalized_works
        if isinstance(item, dict) and str(item.get("platform_work_id") or "").strip()
    }
    merged: List[Dict[str, Any]] = []
    for work in works:
        if not isinstance(work, dict):
            continue
        platform_work_id = str(work.get("platform_work_id") or "").strip()
        normalized = normalized_map.get(platform_work_id)
        if not isinstance(normalized, dict):
            merged.append(work)
            continue
        merged_work = dict(work)
        for field in (
            "primary_text",
            "primary_text_source",
            "digg_count",
            "comment_count",
            "collect_count",
            "share_count",
            "play_count",
            "performance_score",
            "performance_score_norm",
            "bucket",
            "hook_type",
            "structure_type",
            "cta_type",
            "content_form",
            "style_markers",
            "analysis_eligibility",
            "analysis_exclusion_reason",
            "published_date",
            "publish_time",
        ):
            if field in normalized:
                merged_work[field] = normalized.get(field)
        merged.append(merged_work)
    return merged


def _build_card_stage_status(*, expected_count: int, results: Dict[str, Any], failure_kind: str = "runtime") -> Dict[str, Any]:
    if not isinstance(results, dict) or not results.get("enabled", True):
        return _stage_status(status="skipped", ok_count=0, failed_count=0, degraded_count=0, reason_codes=["write_card_disabled"])
    ok_count = int(results.get("count") or len(results.get("results") or []))
    failed_items = results.get("failed_items") if isinstance(results.get("failed_items"), list) else []
    degraded_count = len(failed_items) if ok_count > 0 else 0
    failed_count = len(failed_items) if ok_count == 0 and expected_count > 0 else 0
    if failed_count > 0:
        return _stage_status(
            status="failed",
            ok_count=ok_count,
            failed_count=failed_count,
            degraded_count=0,
            reason_codes=_reason_codes_from_failed_items(failed_items) or ["card_write_failed"],
            failure_kind=failure_kind,
        )
    if degraded_count > 0:
        return _stage_status(
            status="degraded",
            ok_count=ok_count,
            failed_count=0,
            degraded_count=degraded_count,
            reason_codes=_reason_codes_from_failed_items(failed_items) or ["card_write_degraded"],
            failure_kind=failure_kind,
        )
    return _stage_status(status="full", ok_count=ok_count, failed_count=0, degraded_count=0, reason_codes=[])


def _build_overall_status(stage_status: Dict[str, Dict[str, Any]]) -> Dict[str, Any]:
    ordered = [
        "fetch",
        "asr",
        "sampled_explanations",
        "author_analysis",
        "author_sample_card",
        "sample_work_card",
        "author_card",
    ]
    stages = [stage_status.get(key) if isinstance(stage_status.get(key), dict) else {} for key in ordered]
    if any(stage.get("failure_kind") == "configuration" or stage.get("status") == "failed" and stage.get("failure_kind") == "configuration" for stage in stages):
        reason_codes: List[str] = []
        for stage in stages:
            if stage.get("failure_kind") == "configuration":
                reason_codes.extend(stage.get("reason_codes") or [])
        return _stage_status(status="failed", ok_count=0, failed_count=1, degraded_count=0, reason_codes=reason_codes or ["configuration_failed"], failure_kind="configuration")
    author_analysis = stage_status.get("author_analysis") if isinstance(stage_status.get("author_analysis"), dict) else {}
    author_card = stage_status.get("author_card") if isinstance(stage_status.get("author_card"), dict) else {}
    if author_analysis.get("status") == "fallback" and author_card.get("status") in {"full", "degraded", "fallback"}:
        return _stage_status(status="fallback", ok_count=0, failed_count=0, degraded_count=0, reason_codes=author_analysis.get("reason_codes") or ["author_analysis_fallback"], failure_kind=author_analysis.get("failure_kind") or "runtime")
    if any((stage.get("failed_count") or 0) > 0 or (stage.get("degraded_count") or 0) > 0 or stage.get("status") in {"degraded", "failed"} for stage in stages):
        reason_codes = []
        for stage in stages:
            reason_codes.extend(stage.get("reason_codes") or [])
        return _stage_status(status="degraded", ok_count=0, failed_count=0, degraded_count=1, reason_codes=reason_codes or ["stage_degraded"])
    return _stage_status(status="full", ok_count=1, failed_count=0, degraded_count=0, reason_codes=[])


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
        "stage_status": {
            "fetch": _stage_status(status="failed", ok_count=0, failed_count=1, degraded_count=0, reason_codes=["unsupported_platform"]),
            "asr": _stage_status(status="skipped", ok_count=0, failed_count=0, degraded_count=0, reason_codes=["unsupported_platform"]),
            "author_sample_card": _stage_status(status="skipped", ok_count=0, failed_count=0, degraded_count=0, reason_codes=["unsupported_platform"]),
            "sample_work_card": _stage_status(status="skipped", ok_count=0, failed_count=0, degraded_count=0, reason_codes=["unsupported_platform"]),
            "sampled_explanations": _stage_status(status="skipped", ok_count=0, failed_count=0, degraded_count=0, reason_codes=["unsupported_platform"]),
            "author_analysis": _stage_status(status="skipped", ok_count=0, failed_count=0, degraded_count=0, reason_codes=["unsupported_platform"]),
            "author_card": _stage_status(status="skipped", ok_count=0, failed_count=0, degraded_count=0, reason_codes=["unsupported_platform"]),
            "overall": _stage_status(status="failed", ok_count=0, failed_count=1, degraded_count=0, reason_codes=["unsupported_platform"]),
        },
        "quality_tier": "failed",
        "request_id": None,
    }


def _enforce_fixed_pipeline_persistence(*, platform: str, content_kind: str, write_card: bool, persist_output: bool) -> None:
    if write_card and persist_output:
        return
    raise ValueError(
        f"fixed_pipeline_requires_full_persistence:{platform}:{content_kind}:write_card={bool(write_card)}:persist_output={bool(persist_output)}"
    )


def _safe_slug(value: Any, fallback: str = "unknown") -> str:
    text = str(value or "").strip().lower()
    if not text:
        return fallback
    filtered = "".join(ch if ch.isalnum() or ch in {"-", "_"} else "-" for ch in text).strip("-")
    return filtered[:64] or fallback


def _resolve_identifier(input_value: str, result: Dict[str, Any]) -> str:
    for key in ("platform_work_id", "note_id", "request_id"):
        hit = _safe_slug(result.get(key), fallback="")
        if hit:
            return hit

    source = result.get("source")
    if isinstance(source, dict):
        for key in ("share_url", "share_text", "note_id"):
            candidate = str(source.get(key) or "").strip()
            if candidate:
                return f"url-{hashlib.sha1(candidate.encode('utf-8')).hexdigest()[:10]}"

    fallback = str(input_value or "").strip()
    if fallback:
        return f"url-{hashlib.sha1(fallback.encode('utf-8')).hexdigest()[:10]}"
    return "missing_input"


def _build_persist_payload(*, result: Dict[str, Any], status: str, written_at: datetime, identifier: str) -> Dict[str, Any]:
    platform = str(result.get("platform") or "unknown")
    content_kind = str(result.get("content_kind") or "unknown")
    summary = {
        "summary": result.get("summary", ""),
        "insights": result.get("insights", []),
        "confidence": result.get("confidence"),
        "error_reason": result.get("error_reason"),
    }
    normalized = {
        "platform": platform,
        "content_kind": content_kind,
        "platform_work_id": result.get("platform_work_id") or result.get("note_id"),
        "request_id": result.get("request_id"),
        "source": result.get("source") if isinstance(result.get("source"), dict) else {},
    }
    return {
        "meta": {
            "written_at": written_at.isoformat(timespec="seconds"),
            "status": status,
            "platform": platform,
            "identifier": identifier,
        },
        "summary": summary,
        "normalized": normalized,
        "raw": result,
    }


def _persist_output_artifact(*, result: Dict[str, Any], input_value: str, storage_config: Dict[str, Any], persist_output: bool) -> Dict[str, Any]:
    if not persist_output:
        return {"enabled": False, "skipped": True, "reason": "disabled_by_flag"}

    try:
        paths = resolve_storage_paths(storage_config or {})
    except Exception as error:
        return {"enabled": True, "ok": False, "error": f"resolve_storage_paths_failed:{error}"}

    now = datetime.now()
    date_key = now.strftime("%Y%m%d")
    timestamp = now.strftime("%Y%m%dT%H%M%S")
    platform = _safe_slug(result.get("platform"), fallback="unknown")
    identifier = _resolve_identifier(input_value, result)
    has_error = bool(result.get("error_reason"))
    status = "error" if has_error else "success"

    if has_error:
        target_dir = Path(paths.get("errors_root", "")) / date_key
    else:
        target_dir = Path(paths.get("results_root", "")) / date_key

    target_dir.mkdir(parents=True, exist_ok=True)
    file_name = render_output_filename(
        pattern=resolve_json_filename_pattern(storage_config),
        context={
            "prefix": status,
            "platform": platform,
            "card_type": "author_home_result",
            "author_slug": identifier,
            "title_slug": identifier,
            "identifier": identifier,
            "timestamp": timestamp,
            "date": date_key,
            "ext": ".json",
        },
        default_filename=f"{timestamp}-{platform}-{identifier}.json",
        default_ext=".json",
    )
    file_path = target_dir / file_name
    payload = _build_persist_payload(
        result=result,
        status=status,
        written_at=now,
        identifier=identifier,
    )
    file_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    return {
        "enabled": True,
        "ok": True,
        "status": status,
        "path": str(file_path),
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
    persist_output: bool = True,
    card_root: Optional[str] = None,
    storage_config: Optional[Dict[str, Any]] = None,
    collector_override: Optional[CollectorFn] = None,
    progress: Optional[ProgressReporter] = None,
) -> Dict[str, Any]:
    _enforce_fixed_pipeline_persistence(
        platform=platform,
        content_kind="author_home",
        write_card=bool(write_card),
        persist_output=bool(persist_output),
    )

    # hard default policy: latest + cursor loop + max 200 across all platforms
    capped_max_items = min(max(max_items, 1), 200)
    capped_page_size = min(max(page_size, 1), 20)
    if progress is not None:
        progress.started(
            stage="author_home.workflow",
            message="author_home workflow started",
            data={"page_size": capped_page_size, "max_items": capped_max_items},
        )

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
            progress=progress.child(scope="author_home.collect") if progress is not None else None,
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
            progress=progress.child(scope="author_home.collect") if progress is not None else None,
        )
        profile, works, adapter_missing = adapt_xhs_author_home(raw)
    else:
        return _unsupported(platform)

    # Defensive cap enforcement at orchestrator layer.
    works = works[:capped_max_items]
    if progress is not None:
        progress.progress(
            stage="author_home.adapt",
            message="author_home raw payload adapted",
            data={"works_count": len(works), "missing_fields": len(adapter_missing)},
        )

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
        progress=progress.child(scope="author_home.asr") if progress is not None else None,
    )
    works = list(asr_bundle.get("works") or [])[:capped_max_items]
    prepared_analysis_bundle = prepare_author_analysis_bundle(
        profile=profile,
        works=works,
        platform=platform,
    )
    works = _merge_normalized_works(
        works=works,
        normalized_works=prepared_analysis_bundle.get("normalized_works") if isinstance(prepared_analysis_bundle.get("normalized_works"), list) else [],
    )
    prepared_analysis_bundle = prepare_author_analysis_bundle(
        profile=profile,
        works=works,
        platform=platform,
    )
    sampled_work_ids = prepared_analysis_bundle.get("sampled_work_ids") if isinstance(prepared_analysis_bundle.get("sampled_work_ids"), list) else []

    if write_card:
        work_analysis_bundle = orchestrate_work_analysis_artifacts(
            platform=platform,
            profile=profile,
            works=works,
            storage_config=storage_config,
            progress=progress.child(scope="author_home.work_analysis") if progress is not None else None,
        )
    else:
        work_analysis_bundle = {
            "render_payloads": {},
            "artifact_manifest": {},
            "stats": {
                "total_count": len(works),
                "cache_hit_count": 0,
                "queued_count": 0,
                "running_workers": 0,
                "running_workers_peak": 0,
                "finished_count": 0,
                "failed_count": 0,
                "max_workers": 0,
            },
            "failed_items": [],
            "trace": [],
            "artifact_root": None,
            "analysis_logic_version": None,
            "prompt_contract_hash": None,
            "normalization_version": None,
        }
    work_analysis_stats = work_analysis_bundle.get("stats") if isinstance(work_analysis_bundle.get("stats"), dict) else {}
    work_analysis_failed = work_analysis_bundle.get("failed_items") if isinstance(work_analysis_bundle.get("failed_items"), list) else []
    work_analysis_trace = list(work_analysis_bundle.get("trace") or [])
    artifact_manifest = work_analysis_bundle.get("artifact_manifest") if isinstance(work_analysis_bundle.get("artifact_manifest"), dict) else {}
    render_payloads = work_analysis_bundle.get("render_payloads") if isinstance(work_analysis_bundle.get("render_payloads"), dict) else {}
    failed_work_ids = {str(item.get("platform_work_id") or "").strip() for item in work_analysis_failed if isinstance(item, dict)}
    for work in works:
        if not isinstance(work, dict):
            continue
        platform_work_id = str(work.get("platform_work_id") or "").strip()
        manifest = artifact_manifest.get(platform_work_id) if platform_work_id else None
        if isinstance(manifest, dict):
            work["analysis_artifact_status"] = "cache_hit" if manifest.get("from_cache") else "generated"
            work["analysis_artifact_path"] = manifest.get("artifact_path")
        elif platform_work_id in failed_work_ids:
            work["analysis_artifact_status"] = "failed"
            work["analysis_artifact_path"] = None

    if progress is not None:
        progress.progress(stage="author_home.analysis", message="running author analysis")
    analysis, analysis_missing, analysis_trace = run_prompt_first_author_analysis(
        profile,
        works,
        analysis_bundle=prepared_analysis_bundle,
    )
    if progress is not None:
        progress.done(
            stage="author_home.analysis",
            message="author analysis finished",
            data={"missing_fields": len(analysis_missing)},
        )

    if progress is not None:
        progress.progress(
            stage="author_home.card_write",
            message="writing author and work cards",
            data={"write_card": bool(write_card)},
        )
    work_card_write = build_work_cards(
        platform=platform,
        profile=profile,
        works=works,
        render_payloads=render_payloads,
        sampled_work_ids=sampled_work_ids,
        sampled_work_explanations=(
            analysis.get("sampled_work_explanations", {}).get("sampled_work_explanations")
            if isinstance(analysis.get("sampled_work_explanations"), dict)
            else {}
        ),
        card_root=card_root,
        storage_config=storage_config,
        write_card=write_card,
        failed_items=work_analysis_failed,
    )

    asr_trace = list(asr_bundle.get("trace") or [])
    all_extract_trace = list(raw.get("extract_trace") or []) + asr_trace + work_analysis_trace + analysis_trace

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
        if str(item.get("analysis_eligibility") or "") == "eligible":
            continue
        asr_missing.append(
            {
                "field": f"works[{item.get('platform_work_id') or 'unknown'}].asr",
                "reason": str(item.get("analysis_exclusion_reason") or item.get("asr_error_reason") or "asr_failed"),
            }
        )

    asr_stats = asr_bundle.get("stats") if isinstance(asr_bundle.get("stats"), dict) else {}
    asr_checkpoint = asr_bundle.get("checkpoint") if isinstance(asr_bundle.get("checkpoint"), dict) else {}
    author_sample_cards = work_card_write.get("author_sample_cards") if isinstance(work_card_write.get("author_sample_cards"), dict) else {}
    sample_work_cards = work_card_write.get("sample_work_cards") if isinstance(work_card_write.get("sample_work_cards"), dict) else {}

    eligible_count = len([item for item in works if isinstance(item, dict) and str(item.get("analysis_eligibility") or "") == "eligible"])
    incomplete_count = len([item for item in works if isinstance(item, dict) and str(item.get("analysis_eligibility") or "") != "eligible"])
    if works and eligible_count == 0:
        asr_stage = _stage_status(
            status="failed",
            ok_count=0,
            failed_count=incomplete_count or len(works),
            degraded_count=0,
            reason_codes=["asr_unavailable_for_all_works"],
            failure_kind="runtime",
        )
    elif incomplete_count > 0:
        asr_stage = _stage_status(
            status="degraded",
            ok_count=eligible_count,
            failed_count=0,
            degraded_count=incomplete_count,
            reason_codes=["partial_asr_unavailable"],
            failure_kind="runtime",
        )
    else:
        asr_stage = _stage_status(
            status="full",
            ok_count=eligible_count,
            failed_count=0,
            degraded_count=0,
            reason_codes=[],
        )

    stage_status: Dict[str, Dict[str, Any]] = {
        "fetch": _stage_status(
            status="full",
            ok_count=len(works),
            failed_count=0,
            degraded_count=0,
            reason_codes=[],
        ),
        "asr": asr_stage,
        "author_sample_card": _build_card_stage_status(
            expected_count=len(works),
            results=author_sample_cards,
        ),
        "sample_work_card": _build_card_stage_status(
            expected_count=len(sampled_work_ids),
            results=sample_work_cards,
        ),
        "sampled_explanations": analysis.get("sampled_explanations_status") if isinstance(analysis.get("sampled_explanations_status"), dict) else _stage_status(
            status="failed",
            ok_count=0,
            failed_count=1,
            degraded_count=0,
            reason_codes=["missing_sampled_explanations_status"],
        ),
        "author_analysis": analysis.get("author_analysis_status") if isinstance(analysis.get("author_analysis_status"), dict) else _stage_status(
            status="failed",
            ok_count=0,
            failed_count=1,
            degraded_count=0,
            reason_codes=["missing_author_analysis_status"],
        ),
        "author_card": _stage_status(
            status="skipped",
            ok_count=0,
            failed_count=0,
            degraded_count=0,
            reason_codes=["pending"],
        ),
    }

    author_analysis_payload = dict(analysis)
    author_analysis_payload["stage_status"] = stage_status
    author_analysis_payload["quality_tier"] = analysis.get("quality_tier")
    author_analysis_payload["sampled_work_ids"] = sampled_work_ids

    try:
        author_card_write = build_author_card(
            platform=platform,
            profile=profile,
            analysis_payload=author_analysis_payload,
            card_root=card_root,
            storage_config=storage_config,
            write_card=write_card,
        )
    except Exception as error:
        author_card_write = {
            "ok": False,
            "card_type": "author",
            "card_role": "author_card",
            "error_reason": f"author_card_write_failed:{type(error).__name__}:{error}",
            "routing": {
                "card_role": "author_card",
                "route_key": "author",
                "primary_route_parts": "",
                "explicit_override": False,
                "storage_routes_configured": bool(isinstance(storage_config, dict) and isinstance(storage_config.get("storage_routes"), dict)),
            },
        }

    stage_status["author_card"] = (
        _stage_status(status="full", ok_count=1, failed_count=0, degraded_count=0, reason_codes=[])
        if author_card_write.get("ok")
        else _stage_status(
            status="failed",
            ok_count=0,
            failed_count=1,
            degraded_count=0,
            reason_codes=[str(author_card_write.get("error_reason") or "author_card_write_failed").split(":", 1)[0]],
            failure_kind="runtime",
        )
    )
    stage_status["overall"] = _build_overall_status(stage_status)
    if author_card_write.get("ok"):
        author_analysis_payload["stage_status"] = stage_status
        try:
            author_card_write = build_author_card(
                platform=platform,
                profile=profile,
                analysis_payload=author_analysis_payload,
                card_root=card_root,
                storage_config=storage_config,
                write_card=write_card,
            )
        except Exception:
            pass

    if progress is not None:
        progress.done(
            stage="author_home.card_write",
            message="author_home card writing finished",
            data={
                "author_card_ok": bool(author_card_write.get("ok")),
                "author_sample_cards_count": int(author_sample_cards.get("count") or 0),
                "sample_work_cards_count": int(sample_work_cards.get("count") or 0),
            },
        )

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
            f"work_cache_hit={work_analysis_stats.get('cache_hit_count', 0)}",
            f"work_queued={work_analysis_stats.get('queued_count', 0)}",
            f"work_failed={work_analysis_stats.get('failed_count', 0)}",
        ],
        "confidence": (
            "low"
            if analysis.get("quality_tier") in {"fallback", "failed"} or analysis_missing
            else "medium"
        ),
        "error_reason": (
            ((stage_status.get("overall") or {}).get("reason_codes") or [None])[0]
            if (stage_status.get("overall") or {}).get("status") == "failed"
            else None
        ),
        "missing_fields": adapter_missing + analysis_missing + asr_missing,
        "extract_trace": all_extract_trace,
        "fallback_trace": fallback_trace,
        "request_id": raw.get("request_id"),
        "author_profile": profile,
        "works": works,
        "sampled_work_ids": sampled_work_ids,
        "pagination": {
            **(raw.get("pagination") or {}),
            "total_collected": len(works),
            "max_items": capped_max_items,
        },
        "analysis_output": analysis,
        "author_analysis_v2": analysis.get("author_analysis_v2") if isinstance(analysis.get("author_analysis_v2"), dict) else {},
        "author_analysis_input_v1": analysis.get("author_analysis_input_v1") if isinstance(analysis.get("author_analysis_input_v1"), dict) else {},
        "analysis_validation": analysis.get("validation") if isinstance(analysis.get("validation"), dict) else {},
        "stage_status": stage_status,
        "quality_tier": analysis.get("quality_tier"),
        "asr_stats": asr_stats,
        "work_analysis": {
            "stats": work_analysis_stats,
            "failed_items": work_analysis_failed,
            "artifact_root": work_analysis_bundle.get("artifact_root"),
            "analysis_logic_version": work_analysis_bundle.get("analysis_logic_version"),
            "prompt_contract_hash": work_analysis_bundle.get("prompt_contract_hash"),
            "normalization_version": work_analysis_bundle.get("normalization_version"),
        },
        "card_write": {
            "author": author_card_write,
            "author_sample_cards": author_sample_cards,
            "sample_work_cards": sample_work_cards,
            "works": {
                **author_sample_cards,
                "legacy_alias_of": "author_sample_cards",
            },
        },
        "checkpoint": {
            "last_cursor": ((raw.get("pagination") or {}).get("pages") or [{}])[-1].get("cursor_out") if isinstance((raw.get("pagination") or {}).get("pages"), list) and (raw.get("pagination") or {}).get("pages") else "",
            "pages": len((raw.get("pagination") or {}).get("pages") or []),
            "total_collected": len(works),
            "max_items": capped_max_items,
            "sort": "latest",
            "cursor_mode": (raw.get("pagination") or {}).get("cursor_mode", "cursor"),
            "asr": asr_checkpoint,
            "work_analysis": {
                "cache_hit_count": work_analysis_stats.get("cache_hit_count", 0),
                "queued_count": work_analysis_stats.get("queued_count", 0),
                "finished_count": work_analysis_stats.get("finished_count", 0),
                "failed_count": work_analysis_stats.get("failed_count", 0),
                "artifact_root": work_analysis_bundle.get("artifact_root"),
                "failed_items": work_analysis_failed,
            },
        },
    }
    result["output_persist"] = _persist_output_artifact(
        result=result,
        input_value=input_value,
        storage_config=storage_config or {},
        persist_output=bool(persist_output),
    )
    if progress is not None:
        final_event = progress.failed if result.get("error_reason") else progress.done
        final_event(
            stage="author_home.workflow",
            message="author_home workflow finished" if not result.get("error_reason") else "author_home workflow failed",
            data={
                "works_count": len(works),
                "request_id": result.get("request_id"),
                "author_card_ok": bool((result.get("card_write") or {}).get("author", {}).get("ok")),
                "author_sample_cards_count": int(((result.get("card_write") or {}).get("author_sample_cards") or {}).get("count") or 0),
                "sample_work_cards_count": int(((result.get("card_write") or {}).get("sample_work_cards") or {}).get("count") or 0),
                "cache_hit_count": work_analysis_stats.get("cache_hit_count", 0),
                "queued_count": work_analysis_stats.get("queued_count", 0),
                "failed_count": work_analysis_stats.get("failed_count", 0),
                "output_persist_ok": bool((result.get("output_persist") or {}).get("ok")),
            },
        )
    return result
