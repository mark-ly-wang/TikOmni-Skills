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
import json
from pathlib import Path
from typing import Any, Dict, List

from scripts.core.bootstrap_env import bootstrap_for_direct_run

bootstrap_for_direct_run(__file__, __package__)

from scripts.core.completeness import ensure_request_id, evaluate_collection, normalize_missing_fields
from scripts.core.config_loader import config_get, load_tikomni_config, resolve_storage_paths
from scripts.core.progress_report import build_progress_reporter
from scripts.core.storage_router import resolve_author_directory_name
from scripts.core.tikomni_common import resolve_runtime, write_json_stdout
from scripts.pipelines.home_asr import enrich_author_home_asr
from scripts.pipelines.input_contracts import normalize_xhs_creator_input
from scripts.pipelines.schema import build_author_profile
from scripts.pipelines.xiaohongshu_creator_home_helpers import collect_and_adapt
from scripts.writers.write_work_fact_card import build_work_fact_card, persist_output_envelope, write_work_fact_card

DEFAULT_MAX_ITEMS = 200
MAX_ITEMS_HARD_LIMIT = 200


def _write_collection_artifacts(
    *,
    profile: Dict[str, Any],
    works: List[Dict[str, Any]],
    card_root: str,
    extract_trace: List[Dict[str, Any]],
    request_id: str,
) -> Dict[str, str]:
    author_dir_name = resolve_author_directory_name(
        "xiaohongshu",
        str(profile.get("author_handle") or ""),
        str(profile.get("platform_author_id") or ""),
        str(profile.get("nickname") or ""),
    )
    author_dir = Path(card_root) / "内容系统" / "作品库" / author_dir_name
    author_dir.mkdir(parents=True, exist_ok=True)

    creator_profile = dict(profile)
    creator_profile["request_id"] = request_id
    creator_profile["extract_trace"] = extract_trace

    work_collection = {
        "platform": "xiaohongshu",
        "platform_author_id": profile.get("platform_author_id"),
        "count": len(works),
        "items": [
            {
                "platform_work_id": item.get("platform_work_id"),
                "title": item.get("title"),
                "published_date": item.get("published_date"),
            }
            for item in works
            if isinstance(item, dict)
        ],
        "request_id": request_id,
        "extract_trace": extract_trace,
    }

    profile_path = author_dir / "_creator_profile.json"
    collection_path = author_dir / "_work_collection.json"
    profile_path.write_text(json.dumps(creator_profile, ensure_ascii=False, indent=2), encoding="utf-8")
    collection_path.write_text(json.dumps(work_collection, ensure_ascii=False, indent=2), encoding="utf-8")
    return {"creator_profile_path": str(profile_path), "work_collection_path": str(collection_path)}


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

    asr_strategy = config_get(config, "asr_strategy", {})
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
        progress=progress.child(scope="author_home.asr"),
    )
    works = list(asr_bundle.get("works") or [])

    card_root = resolve_storage_paths(config)["card_root"]
    card_results: List[Dict[str, Any]] = []
    if write_card:
        for work in works:
            card_results.append(
                write_work_fact_card(
                    payload=work,
                    platform="xiaohongshu",
                    card_root=card_root,
                    storage_config=config,
                )
            )

    request_id = ensure_request_id(
        raw.get("request_id") or profile.get("request_id"),
        fallback_seed=normalized_input_value or input_value,
    )
    extract_trace = list(raw.get("extract_trace") or []) + list(asr_bundle.get("trace") or [])

    collection_artifacts = _write_collection_artifacts(
        profile=profile,
        works=works,
        card_root=card_root,
        extract_trace=extract_trace,
        request_id=request_id,
    )

    normalized_profile = dict(profile)
    normalized_profile["request_id"] = request_id
    normalized_profile["extract_trace"] = extract_trace
    normalized_works = [build_work_fact_card(work, platform="xiaohongshu") for work in works]

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
        "error_reason": None,
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
    envelope["output_persist"] = persist_output_envelope(
        envelope=envelope,
        storage_config=config,
        platform="xiaohongshu",
        fallback_identifier=str(profile.get("platform_author_id") or "author-home"),
    ) if persist_output else {"enabled": False, "skipped": True, "reason": "disabled_by_flag"}

    progress.done(
        stage="author_home.workflow",
        message="xiaohongshu author_home workflow finished",
        data={"request_id": request_id, "works_count": len(normalized_works)},
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
