#!/usr/bin/env python3

if __package__ in {None, ""}:
    import sys
    from pathlib import Path

    _self = Path(__file__).resolve()
    for _parent in _self.parents:
        if (_parent / "scripts" / "core" / "bootstrap_env.py").is_file():
            sys.path.insert(0, str(_parent))
            break

"""Unified URL runner via workflow registry dispatch."""

from scripts.core.bootstrap_env import bootstrap_for_direct_run

bootstrap_for_direct_run(__file__, __package__)

import argparse
import hashlib
import json
import re
from datetime import datetime
from pathlib import Path
from typing import Any, Dict

from scripts.core.config_loader import config_get, load_tikomni_config, resolve_storage_paths
from scripts.core.extract_pipeline import detect_platform_from_input
from scripts.core.tikomni_common import resolve_runtime, write_json_stdout
from scripts.registry.workflow_registry import DEFAULT_WORKFLOW_REGISTRY, normalize_result_envelope


def _build_unsupported_result(*, input_value: str, platform: str, content_kind: str) -> Dict[str, Any]:
    return {
        "platform": platform or "unknown",
        "content_kind": content_kind or "unknown",
        "raw_content": "",
        "summary": "",
        "insights": ["source=runner", "unsupported_workflow"],
        "confidence": "low",
        "error_reason": "unsupported_workflow",
        "missing_fields": [],
        "extract_trace": [
            {
                "step": "workflow_resolve",
                "input": input_value,
                "detected_platform": platform,
                "requested_content_kind": content_kind,
                "registry_hit": False,
            }
        ],
        "fallback_trace": [
            {
                "step": "workflow_resolve",
                "detected_platform": platform,
                "requested_content_kind": content_kind,
                "registry_hit": False,
            }
        ],
        "request_id": None,
    }


def _build_runtime_not_ready_result(*, platform: str, content_kind: str, error_reason: str) -> Dict[str, Any]:
    return {
        "platform": platform,
        "content_kind": content_kind,
        "raw_content": "",
        "summary": "",
        "insights": ["source=runner", "runtime_not_ready"],
        "confidence": "low",
        "error_reason": error_reason,
        "missing_fields": [],
        "extract_trace": [],
        "fallback_trace": [],
        "request_id": None,
    }


def _safe_slug(value: Any, fallback: str = "unknown") -> str:
    text = str(value or "").strip().lower()
    if not text:
        return fallback
    slug = re.sub(r"[^a-z0-9_-]+", "-", text).strip("-")
    return slug[:64] or fallback


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
        target_dir = Path(paths.get("errors_dir", "")) / date_key
    else:
        target_dir = Path(paths.get("runs_dir", "")) / str(paths.get("results_dir", "results")) / date_key

    target_dir.mkdir(parents=True, exist_ok=True)
    file_path = target_dir / f"{timestamp}-{platform}-{identifier}.json"

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


def _ensure_output_persist(*, result: Dict[str, Any], input_value: str, storage_config: Dict[str, Any], persist_output: bool) -> Dict[str, Any]:
    existing = result.get("output_persist")
    if isinstance(existing, dict):
        if existing.get("ok") is True:
            return result
        if existing.get("skipped") is True and not persist_output:
            return result

    result["output_persist"] = _persist_output_artifact(
        result=result,
        input_value=input_value,
        storage_config=storage_config,
        persist_output=persist_output,
    )
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description="Run tikomni local extractor by URL")
    parser.add_argument("input", help="URL or platform-specific ID")
    parser.add_argument("--platform", choices=["auto", "douyin", "xiaohongshu"], default="auto")
    parser.add_argument(
        "--content-kind",
        choices=["auto", "single_video", "note", "author_home"],
        default="auto",
        help="Workflow content kind. auto resolves by platform default mapping.",
    )
    parser.add_argument("--config", default=None, help="Runtime config YAML path")
    parser.add_argument("--env-file", default=None, help="Optional env file path")
    parser.add_argument("--allow-process-env", action="store_true", help="Allow process env to override .env/.env.local")
    parser.add_argument("--api-key-env", default=None, help="API key env variable name")
    parser.add_argument("--base-url", default=None, help="Tikomni API base URL")
    parser.add_argument("--timeout-ms", type=int, default=None, help="Request timeout ms")
    parser.add_argument("--poll-interval-sec", type=float, default=None, help="U2 poll interval")
    parser.add_argument("--max-polls", type=int, default=None, help="Max U2 poll attempts")
    parser.add_argument("--u2-submit-max-retries", type=int, default=None, help="Douyin U2 submit max retries")
    parser.add_argument("--u2-submit-backoff-ms", type=int, default=None, help="Douyin U2 submit base backoff ms")
    parser.add_argument("--u2-timeout-retry-enabled", type=str, choices=["true", "false"], default=None, help="Enable timeout-only retry")
    parser.add_argument("--u2-timeout-retry-max-retries", type=int, default=None, help="Timeout-only retry max retries")
    parser.add_argument("--xhs-u2-submit-max-retries", type=int, default=None, help="Xiaohongshu U2 submit max retries")
    parser.add_argument("--xhs-u2-submit-backoff-ms", type=int, default=None, help="Xiaohongshu U2 submit base backoff ms")
    parser.add_argument("--force-u2-fallback", action="store_true", help="XHS only: force subtitle miss for fallback test")
    parser.add_argument("--write-card", dest="write_card", action="store_true", help="Write markdown card (default on)")
    parser.add_argument("--no-write-card", dest="write_card", action="store_false", help="Disable markdown card writing")
    parser.set_defaults(write_card=True)
    parser.add_argument("--card-type", choices=["work", "author", "author_sample_work"], default="work", help="Primary card type")
    parser.add_argument("--collect-material", action="store_true", help="Write CMAT only when explicit")
    parser.add_argument("--card-root", default=None, help="Card root (absolute); falls back to TIKOMNI_CARD_ROOT when writing cards")
    parser.add_argument("--page-size", type=int, default=20, help="Homepage fetch page size (capped to 20)")
    parser.add_argument("--pages-max", type=int, default=50, help="Homepage max pagination rounds")
    parser.add_argument("--max-items", type=int, default=200, help="Homepage total item cap (hard max 200)")
    parser.add_argument("--persist-output", dest="persist_output", action="store_true", help="Persist workflow JSON artifact to TIKOMNI_OUTPUT_ROOT (default on)")
    parser.add_argument("--no-persist-output", dest="persist_output", action="store_false", help="Disable workflow artifact persistence globally")
    parser.set_defaults(persist_output=True)
    args = parser.parse_args()

    config, _ = load_tikomni_config(
        args.config,
        env_file=args.env_file,
        allow_process_env=args.allow_process_env,
    )

    resolved_env_file = args.env_file or config_get(config, "runtime.env_file", None)
    api_key_env = args.api_key_env or config_get(config, "runtime.auth_env_key", "TIKOMNI_API_KEY")
    base_url = args.base_url or config_get(config, "runtime.base_url", None)
    timeout_ms = args.timeout_ms if args.timeout_ms is not None else config_get(config, "runtime.timeout_ms", None)
    poll_interval_sec = (
        args.poll_interval_sec
        if args.poll_interval_sec is not None
        else config_get(config, "asr_strategy.poll_interval_sec", 3.0)
    )
    max_polls = args.max_polls if args.max_polls is not None else config_get(config, "asr_strategy.max_polls", 30)
    douyin_u2_submit_max_retries = (
        args.u2_submit_max_retries
        if args.u2_submit_max_retries is not None
        else config_get(config, "asr_strategy.submit_retry.douyin_video.max_retries", 2)
    )
    douyin_u2_submit_backoff_ms = (
        args.u2_submit_backoff_ms
        if args.u2_submit_backoff_ms is not None
        else config_get(config, "asr_strategy.submit_retry.douyin_video.backoff_ms", 1500)
    )
    u2_timeout_retry_enabled = (
        (str(args.u2_timeout_retry_enabled).lower() == "true")
        if args.u2_timeout_retry_enabled is not None
        else bool(config_get(config, "asr_strategy.u2_timeout_retry.enabled", True))
    )
    u2_timeout_retry_max_retries = (
        args.u2_timeout_retry_max_retries
        if args.u2_timeout_retry_max_retries is not None
        else config_get(config, "asr_strategy.u2_timeout_retry.max_retries", 3)
    )
    xhs_u2_submit_max_retries = (
        args.xhs_u2_submit_max_retries
        if args.xhs_u2_submit_max_retries is not None
        else config_get(config, "asr_strategy.submit_retry.xiaohongshu_note.max_retries", 0)
    )
    xhs_u2_submit_backoff_ms = (
        args.xhs_u2_submit_backoff_ms
        if args.xhs_u2_submit_backoff_ms is not None
        else config_get(config, "asr_strategy.submit_retry.xiaohongshu_note.backoff_ms", 0)
    )

    platform = args.platform
    if platform == "auto":
        platform = detect_platform_from_input(args.input)

    requested_content_kind = args.content_kind

    runtime = resolve_runtime(
        env_file=resolved_env_file,
        api_key_env=api_key_env,
        base_url=base_url,
        timeout_ms=timeout_ms,
        allow_process_env=args.allow_process_env,
    )

    workflow_ctx = {
        "input_value": args.input,
        "resolved_env_file": resolved_env_file,
        "api_key_env": api_key_env,
        "token": runtime.get("token"),
        "base_url": runtime.get("base_url"),
        "timeout_ms": int(runtime.get("timeout_ms") or 60000),
        "poll_interval_sec": float(poll_interval_sec),
        "max_polls": int(max_polls),
        "douyin_u2_submit_max_retries": int(douyin_u2_submit_max_retries),
        "douyin_u2_submit_backoff_ms": int(douyin_u2_submit_backoff_ms),
        "xhs_u2_submit_max_retries": int(xhs_u2_submit_max_retries),
        "xhs_u2_submit_backoff_ms": int(xhs_u2_submit_backoff_ms),
        "u2_timeout_retry_enabled": bool(u2_timeout_retry_enabled),
        "u2_timeout_retry_max_retries": int(u2_timeout_retry_max_retries),
        "force_u2_fallback": args.force_u2_fallback,
        "write_card": args.write_card,
        "card_type": args.card_type,
        "collect_material": args.collect_material,
        "card_root": args.card_root,
        "storage_config": config,
        "allow_process_env": args.allow_process_env,
        "persist_output": args.persist_output,
        "page_size": int(args.page_size),
        "pages_max": int(args.pages_max),
        "max_items": int(args.max_items),
    }

    resolved_content_kind = None

    try:
        handler, resolved_content_kind = DEFAULT_WORKFLOW_REGISTRY.resolve(
            platform=platform,
            content_kind=requested_content_kind,
        )

        if handler is None or not resolved_content_kind:
            result = _build_unsupported_result(
                input_value=args.input,
                platform=platform,
                content_kind=requested_content_kind,
            )
        else:
            raw_result = handler(workflow_ctx)
            result = normalize_result_envelope(
                raw_result,
                platform=platform,
                content_kind=resolved_content_kind,
            )
    except ValueError as error:
        fallback_content_kind = (
            resolved_content_kind
            or (requested_content_kind if requested_content_kind != "auto" else "unknown")
        )
        result = _build_runtime_not_ready_result(
            platform=platform,
            content_kind=fallback_content_kind,
            error_reason=str(error),
        )

    result = _ensure_output_persist(
        result=result,
        input_value=args.input,
        storage_config=config,
        persist_output=bool(args.persist_output),
    )

    write_json_stdout(result)
    raise SystemExit(0 if not result.get("error_reason") else 1)


if __name__ == "__main__":
    main()
