#!/usr/bin/env python3
"""Workflow registry for tikomni extract entrypoint.

Registry only resolves mapping: (platform, content_kind) -> workflow handler.
Routing strategy priority still belongs to capability matrix / routing rules.
"""

from __future__ import annotations

from typing import Any, Callable, Dict, Mapping, MutableMapping, Optional, Tuple, TypedDict

from scripts.platform.douyin.run_douyin_single_video import run_douyin_single_video
from scripts.platform.xiaohongshu.run_xiaohongshu_extract import run_xiaohongshu_extract


class WorkflowContext(TypedDict, total=False):
    input_value: Optional[str]
    resolved_env_file: Optional[str]
    api_key_env: str
    base_url: Optional[str]
    timeout_ms: Optional[int]
    poll_interval_sec: float
    max_polls: int
    u2_submit_max_retries: int
    u2_submit_backoff_ms: int
    douyin_u2_submit_max_retries: int
    douyin_u2_submit_backoff_ms: int
    xhs_u2_submit_max_retries: int
    xhs_u2_submit_backoff_ms: int
    u2_timeout_retry_enabled: bool
    u2_timeout_retry_max_retries: int
    force_u2_fallback: bool
    write_card: bool
    card_type: str
    collect_material: bool
    card_root: Optional[str]
    storage_config: Optional[Dict[str, Any]]
    allow_process_env: bool
    persist_output: bool


class ResultEnvelope(TypedDict, total=False):
    platform: str
    content_kind: str
    raw_content: str
    summary: str
    insights: list
    confidence: str
    error_reason: Optional[str]
    missing_fields: list
    extract_trace: list
    fallback_trace: list
    request_id: Optional[str]
    card_write: Any
    output_persist: Any


WorkflowHandler = Callable[[WorkflowContext], Mapping[str, Any]]


class WorkflowRegistry:
    def __init__(self) -> None:
        self._handlers: MutableMapping[Tuple[str, str], WorkflowHandler] = {}
        self._default_kind: MutableMapping[str, str] = {}

    def register(self, platform: str, content_kind: str, handler: WorkflowHandler, *, default: bool = False) -> None:
        key = (platform.strip().lower(), content_kind.strip().lower())
        self._handlers[key] = handler
        if default:
            self._default_kind[key[0]] = key[1]

    def resolve(self, platform: str, content_kind: str = "auto") -> Tuple[Optional[WorkflowHandler], Optional[str]]:
        platform_key = (platform or "").strip().lower()
        kind_key = (content_kind or "auto").strip().lower()

        if not platform_key:
            return None, None

        if kind_key == "auto":
            kind_key = self._default_kind.get(platform_key, "")

        if kind_key:
            handler = self._handlers.get((platform_key, kind_key))
            if handler is not None:
                return handler, kind_key

        return None, None


def normalize_result_envelope(
    result: Mapping[str, Any],
    *,
    platform: str,
    content_kind: str,
) -> Dict[str, Any]:
    normalized: Dict[str, Any] = dict(result)
    normalized.setdefault("platform", platform)
    normalized.setdefault("content_kind", content_kind)
    normalized.setdefault("raw_content", "")
    normalized.setdefault("summary", "")
    normalized.setdefault("insights", [])
    normalized.setdefault("confidence", "low")
    normalized.setdefault("error_reason", None)
    normalized.setdefault("missing_fields", [])
    normalized.setdefault("extract_trace", [])
    normalized.setdefault("fallback_trace", [])
    normalized.setdefault("request_id", None)
    return normalized


def _run_douyin_single_video_workflow(ctx: WorkflowContext) -> Mapping[str, Any]:
    return run_douyin_single_video(
        input_value=ctx.get("input_value"),
        share_url=None,
        env_file=ctx.get("resolved_env_file"),
        api_key_env=str(ctx.get("api_key_env") or "TIKOMNI_API_KEY"),
        base_url=ctx.get("base_url"),
        timeout_ms=ctx.get("timeout_ms"),
        app_timeout_ms=None,
        web_timeout_ms=None,
        poll_interval_sec=float(ctx.get("poll_interval_sec", 3.0)),
        max_polls=int(ctx.get("max_polls", 30)),
        u2_submit_max_retries=int(
            ctx.get("douyin_u2_submit_max_retries", ctx.get("u2_submit_max_retries", 2))
        ),
        u2_submit_backoff_ms=int(
            ctx.get("douyin_u2_submit_backoff_ms", ctx.get("u2_submit_backoff_ms", 1500))
        ),
        write_card=bool(ctx.get("write_card", True)),
        card_type=str(ctx.get("card_type") or "work"),
        collect_material=bool(ctx.get("collect_material", False)),
        card_root=ctx.get("card_root"),
        content_kind="single_video",
        storage_config=ctx.get("storage_config"),
        allow_process_env=bool(ctx.get("allow_process_env", False)),
        persist_output=bool(ctx.get("persist_output", True)),
    )


def _run_xiaohongshu_note_workflow(ctx: WorkflowContext) -> Mapping[str, Any]:
    return run_xiaohongshu_extract(
        input_value=ctx.get("input_value"),
        share_text=None,
        note_id=None,
        env_file=ctx.get("resolved_env_file"),
        api_key_env=str(ctx.get("api_key_env") or "TIKOMNI_API_KEY"),
        base_url=ctx.get("base_url"),
        timeout_ms=ctx.get("timeout_ms"),
        poll_interval_sec=float(ctx.get("poll_interval_sec", 3.0)),
        max_polls=int(ctx.get("max_polls", 30)),
        u2_submit_max_retries=int(
            ctx.get("xhs_u2_submit_max_retries", ctx.get("u2_submit_max_retries", 0))
        ),
        u2_submit_backoff_ms=int(
            ctx.get("xhs_u2_submit_backoff_ms", ctx.get("u2_submit_backoff_ms", 0))
        ),
        u2_timeout_retry_enabled=bool(ctx.get("u2_timeout_retry_enabled", True)),
        u2_timeout_retry_max_retries=int(ctx.get("u2_timeout_retry_max_retries", 3)),
        force_u2_fallback=bool(ctx.get("force_u2_fallback", False)),
        write_card=bool(ctx.get("write_card", True)),
        card_type=str(ctx.get("card_type") or "work"),
        collect_material=bool(ctx.get("collect_material", False)),
        card_root=ctx.get("card_root"),
        storage_config=ctx.get("storage_config"),
        allow_process_env=bool(ctx.get("allow_process_env", False)),
        persist_output=bool(ctx.get("persist_output", True)),
    )


def build_default_workflow_registry() -> WorkflowRegistry:
    registry = WorkflowRegistry()
    registry.register("douyin", "single_video", _run_douyin_single_video_workflow, default=True)
    registry.register("xiaohongshu", "note", _run_xiaohongshu_note_workflow, default=True)
    # Compatibility alias with existing single_video naming.
    registry.register("xiaohongshu", "single_video", _run_xiaohongshu_note_workflow, default=False)
    return registry


DEFAULT_WORKFLOW_REGISTRY = build_default_workflow_registry()
