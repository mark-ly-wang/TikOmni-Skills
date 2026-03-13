#!/usr/bin/env python3
"""Xiaohongshu creator-home fixed pipeline."""

from __future__ import annotations

if __package__ in {None, ""}:
    import sys
    from pathlib import Path

    _self = Path(__file__).resolve()
    for _parent in _self.parents:
        if (_parent / "scripts" / "core" / "bootstrap_env.py").is_file():
            sys.path.insert(0, str(_parent))
            break

import argparse
from typing import Any, Dict, List, Set

from scripts.core.bootstrap_env import bootstrap_for_direct_run

bootstrap_for_direct_run(__file__, __package__)

from scripts.core.completeness import ensure_request_id, evaluate_collection, normalize_missing_fields
from scripts.core.config_loader import config_get, load_tikomni_config, resolve_storage_paths
from scripts.core.progress_report import build_progress_reporter
from scripts.core.tikomni_common import resolve_runtime, write_json_stdout
from scripts.pipelines.home_asr import enrich_author_home_asr
from scripts.pipelines.homepage_runtime_state import (
    clear_homepage_checkpoint,
    load_homepage_checkpoint,
    persist_homepage_runtime_artifacts,
    resolve_homepage_run_status,
)
from scripts.pipelines.input_contracts import normalize_xhs_creator_input
from scripts.pipelines.schema import build_author_profile
from scripts.pipelines.xiaohongshu_creator_home_helpers import collect_and_adapt
from scripts.writers.write_work_fact_card import build_work_fact_card, persist_output_envelope, write_work_fact_card

DEFAULT_MAX_ITEMS = 200
MAX_ITEMS_HARD_LIMIT = 200


def run_xiaohongshu_creator_home(
    *,
    input_value: str,
    config: Dict[str, Any],
    runtime: Dict[str, Any] | None,
    max_items: int,
    write_card: bool,
    persist_output: bool,
) -> Dict[str, Any]:
    bounded_max_items = max(1, min(int(max_items), MAX_ITEMS_HARD_LIMIT))
    progress = build_progress_reporter(
        workflow="social-media-crawl",
        platform="xiaohongshu",
        content_kind="author_home",
        input_value=input_value,
        scope="workflow",
    )
    progress.started(stage="author_home.workflow", message="xiaohongshu author_home workflow started")
    preflight = normalize_xhs_creator_input(input_value)
    normalized_input_value = str(preflight.get("input_value") or "")
    if preflight.get("error_reason"):
        request_id = ensure_request_id(None, fallback_seed=input_value)
        empty_profile = build_author_profile(platform="xiaohongshu", request_id=request_id)
        extract_trace = [
            {
                "step": "input.preflight",
                "ok": False,
                "input_kind": "creator_url_or_user_id",
                "normalized_input_value": normalized_input_value or None,
                "error_reason": preflight.get("error_reason"),
                "missing_fields": list(preflight.get("missing_fields") or []),
            }
        ]
        envelope = {
            "object_type": "creator",
            "platform": "xiaohongshu",
            "input": input_value,
            "normalized": {
                "creator_profile": {**empty_profile, "request_id": request_id, "extract_trace": extract_trace},
                "work_collection": {
                    "platform": "xiaohongshu",
                    "platform_author_id": "",
                    "count": 0,
                    "items": [],
                    "request_id": request_id,
                    "extract_trace": extract_trace,
                },
            },
            "completeness": evaluate_collection(empty_profile, []),
            "missing_fields": normalize_missing_fields(preflight.get("missing_fields")),
            "error_reason": str(preflight.get("error_reason") or "invalid_creator_input"),
            "extract_trace": extract_trace,
            "request_id": request_id,
            "card_write": {
                "enabled": bool(write_card),
                "ok": False,
                "count": 0,
                "results": [],
                "reason": "skipped_invalid_input",
            },
            "collection_artifacts": {},
            "output_persist": {"enabled": False, "skipped": True, "reason": "invalid_input"},
        }
        progress.done(
            stage="author_home.workflow",
            message="xiaohongshu author_home workflow finished",
            data={"request_id": request_id, "works_count": 0, "error_reason": envelope["error_reason"]},
        )
        return envelope

    if runtime is None:
        raise ValueError("runtime_required_for_valid_input")

    raw, profile, works, missing = collect_and_adapt(
        input_value=normalized_input_value or input_value,
        base_url=runtime["base_url"],
        token=runtime["token"],
        timeout_ms=runtime["timeout_ms"],
        page_size=20,
        pages_max=50,
        max_items=bounded_max_items,
        progress=progress.child(scope="author_home.collect"),
    )

    card_root = resolve_storage_paths(config)["card_root"]
    request_id = ensure_request_id(
        raw.get("request_id") or profile.get("request_id"),
        fallback_seed=normalized_input_value or input_value,
    )
    raw_extract_trace = list(raw.get("extract_trace") or [])
    checkpoint = load_homepage_checkpoint(
        platform="xiaohongshu",
        profile=profile,
        card_root=card_root,
    )
    if checkpoint:
        progress.progress(
            stage="author_home.workflow.resume",
            message="xiaohongshu author_home checkpoint loaded",
            data={
                "completed_work_ids": len(checkpoint.get("completed_work_ids") or []),
                "last_completed_batch_id": checkpoint.get("last_completed_batch_id"),
            },
        )

    asr_strategy = config_get(config, "asr_strategy", {})
    card_results: List[Dict[str, Any]] = []
    written_work_ids: Set[str] = set()

    def _persist_batch(event: Dict[str, Any]) -> None:
        batch_id = str(event.get("batch_id") or "")
        batch_works = event.get("batch_works") if isinstance(event.get("batch_works"), list) else []
        all_works = event.get("works") if isinstance(event.get("works"), list) else []
        batch_trace = raw_extract_trace + list(event.get("trace") or [])

        batch_card_count = 0
        if write_card:
            for work in batch_works:
                if not isinstance(work, dict):
                    continue
                result = write_work_fact_card(
                    payload=work,
                    platform="xiaohongshu",
                    card_root=card_root,
                    storage_config=config,
                )
                card_results.append(result)
                work_id = str(work.get("platform_work_id") or "").strip()
                if work_id:
                    written_work_ids.add(work_id)
                batch_card_count += 1

        persist_homepage_runtime_artifacts(
            platform="xiaohongshu",
            profile=profile,
            works=all_works,
            card_root=card_root,
            extract_trace=batch_trace,
            request_id=request_id,
            checkpoint=event.get("checkpoint") if isinstance(event.get("checkpoint"), dict) else {},
            run_status="in_progress",
            last_completed_batch_id=batch_id,
        )
        progress.progress(
            stage="author_home.persist.batch",
            message="xiaohongshu author_home batch persisted",
            data={
                "batch_id": batch_id,
                "batch_cards": batch_card_count,
                "completed_count": (event.get("checkpoint") if isinstance(event.get("checkpoint"), dict) else {}).get("processed_works"),
                "pending_count": (event.get("checkpoint") if isinstance(event.get("checkpoint"), dict) else {}).get("pending_works"),
            },
        )

    asr_bundle = enrich_author_home_asr(
        platform="xiaohongshu",
        works=works,
        base_url=runtime["base_url"],
        token=runtime["token"],
        timeout_ms=runtime["timeout_ms"],
        poll_interval_sec=float(asr_strategy.get("poll_interval_sec", 3.0)),
        max_polls=int(asr_strategy.get("max_polls", 30)),
        xhs_submit_max_retries=int(config_get(config, "asr_strategy.submit_retry.xiaohongshu_note.max_retries", 0)),
        xhs_submit_backoff_ms=int(config_get(config, "asr_strategy.submit_retry.xiaohongshu_note.backoff_ms", 0)),
        timeout_retry_enabled=bool(config_get(config, "asr_strategy.u2_timeout_retry.enabled", True)),
        timeout_retry_max_retries=int(config_get(config, "asr_strategy.u2_timeout_retry.max_retries", 0)),
        checkpoint=checkpoint,
        request_id=request_id,
        on_batch_complete=_persist_batch,
        progress=progress.child(scope="author_home.asr"),
    )
    works = list(asr_bundle.get("works") or [])

    if write_card:
        for work in works:
            work_id = str(work.get("platform_work_id") or "").strip()
            if work_id and work_id in written_work_ids:
                continue
            card_results.append(
                write_work_fact_card(
                    payload=work,
                    platform="xiaohongshu",
                    card_root=card_root,
                    storage_config=config,
                )
            )

    extract_trace = raw_extract_trace + list(asr_bundle.get("trace") or [])
    checkpoint_out = asr_bundle.get("checkpoint") if isinstance(asr_bundle.get("checkpoint"), dict) else {}
    collection_artifacts = persist_homepage_runtime_artifacts(
        platform="xiaohongshu",
        profile=profile,
        works=works,
        card_root=card_root,
        extract_trace=extract_trace,
        request_id=request_id,
        checkpoint=checkpoint_out,
        run_status=resolve_homepage_run_status(asr_bundle.get("stats")),
        last_completed_batch_id=str(checkpoint_out.get("last_completed_batch_id") or ""),
    )
    if int(checkpoint_out.get("pending_works") or 0) <= 0:
        cleared_checkpoint_path = clear_homepage_checkpoint(platform="xiaohongshu", profile=profile, card_root=card_root)
        if cleared_checkpoint_path:
            collection_artifacts["checkpoint_cleared_path"] = cleared_checkpoint_path

    normalized_profile = dict(profile)
    normalized_profile["request_id"] = request_id
    normalized_profile["extract_trace"] = extract_trace
    normalized_works = [build_work_fact_card(work, platform="xiaohongshu") for work in works]
    stage_status = raw.get("stage_status") if isinstance(raw.get("stage_status"), dict) else {}
    error_reason = raw.get("error_reason")

    envelope = {
        "object_type": "creator",
        "platform": "xiaohongshu",
        "input": input_value,
        "normalized": {
            "creator_profile": normalized_profile,
            "work_collection": {
                "platform": "xiaohongshu",
                "platform_author_id": profile.get("platform_author_id"),
                "count": len(normalized_works),
                "items": normalized_works,
                "request_id": request_id,
                "extract_trace": extract_trace,
            },
        },
        "completeness": evaluate_collection(profile, normalized_works),
        "missing_fields": normalize_missing_fields(missing),
        "error_reason": error_reason,
        "extract_trace": extract_trace,
        "request_id": request_id,
        "card_write": {
            "enabled": bool(write_card),
            "ok": all(item.get("ok") for item in card_results) if card_results else False,
            "count": len(card_results),
            "results": card_results,
        },
        "collection_artifacts": collection_artifacts,
    }
    if stage_status:
        envelope["stage_status"] = stage_status
    envelope["output_persist"] = persist_output_envelope(
        envelope=envelope,
        storage_config=config,
        platform="xiaohongshu",
        fallback_identifier=str(profile.get("platform_author_id") or "author-home"),
    ) if persist_output else {"enabled": False, "skipped": True, "reason": "disabled_by_flag"}

    final_event = progress.failed if envelope.get("error_reason") else progress.done
    final_event(
        stage="author_home.workflow",
        message="xiaohongshu author_home workflow failed" if envelope.get("error_reason") else "xiaohongshu author_home workflow finished",
        data={"request_id": request_id, "works_count": len(normalized_works), "error_reason": envelope.get("error_reason")},
    )
    return envelope


def main() -> None:
    parser = argparse.ArgumentParser(description="Run Xiaohongshu creator-home fixed pipeline")
    parser.add_argument("input", help="Xiaohongshu creator homepage or share URL")
    parser.add_argument("--config", default=None, help="Runtime config YAML path")
    parser.add_argument("--env-file", default=None, help="Explicit .env path")
    parser.add_argument("--allow-process-env", action="store_true", help="Allow process env overrides")
    parser.add_argument("--base-url", default=None, help="Override Tikomni base URL")
    parser.add_argument("--timeout-ms", type=int, default=None, help="Override timeout in ms")
    parser.add_argument(
        "--max-items",
        type=int,
        default=DEFAULT_MAX_ITEMS,
        help=f"Max works to collect from homepage (default full crawl, capped at {MAX_ITEMS_HARD_LIMIT})",
    )
    parser.set_defaults(write_card=True, persist_output=True)
    parser.add_argument("--write-card", dest="write_card", action="store_true", help="Write work fact cards")
    parser.add_argument("--no-write-card", dest="write_card", action="store_false", help="Skip card writing")
    parser.add_argument("--persist-output", dest="persist_output", action="store_true", help="Persist output JSON")
    parser.add_argument("--no-persist-output", dest="persist_output", action="store_false", help="Skip output JSON persist")
    args = parser.parse_args()

    config, _ = load_tikomni_config(args.config, env_file=args.env_file, allow_process_env=args.allow_process_env)
    preflight = normalize_xhs_creator_input(args.input)
    if preflight.get("error_reason"):
        write_json_stdout(
            run_xiaohongshu_creator_home(
                input_value=args.input,
                config=config,
                runtime=None,
                max_items=int(args.max_items),
                write_card=bool(args.write_card),
                persist_output=bool(args.persist_output),
            )
        )
        return
    runtime = resolve_runtime(
        env_file=args.env_file,
        api_key_env=str(config_get(config, "runtime.auth_env_key", "TIKOMNI_API_KEY")),
        base_url=args.base_url or config_get(config, "runtime.base_url", None),
        timeout_ms=args.timeout_ms or config_get(config, "runtime.timeout_ms", None),
        allow_process_env=args.allow_process_env,
    )
    write_json_stdout(
        run_xiaohongshu_creator_home(
            input_value=str(preflight.get("input_value") or args.input),
            config=config,
            runtime=runtime,
            max_items=int(args.max_items),
            write_card=bool(args.write_card),
            persist_output=bool(args.persist_output),
        )
    )


if __name__ == "__main__":
    main()
