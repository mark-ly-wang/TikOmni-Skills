#!/usr/bin/env python3
"""Shared runtime-state helpers for homepage pipelines."""

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

from scripts.core.storage_router import resolve_author_directory_name


def _safe_text(value: Any) -> str:
    if value is None:
        return ""
    return str(value).strip()


def _now_iso() -> str:
    return datetime.now().isoformat(timespec="seconds")


def resolve_homepage_author_dir(*, platform: str, profile: Dict[str, Any], card_root: str) -> Path:
    author_dir_name = resolve_author_directory_name(
        platform,
        _safe_text(profile.get("author_handle")),
        _safe_text(profile.get("platform_author_id")),
        _safe_text(profile.get("nickname")),
    )
    author_dir = Path(card_root) / "内容系统" / "作品库" / author_dir_name
    author_dir.mkdir(parents=True, exist_ok=True)
    return author_dir


def load_homepage_checkpoint(*, platform: str, profile: Dict[str, Any], card_root: str) -> Dict[str, Any]:
    author_dir = resolve_homepage_author_dir(platform=platform, profile=profile, card_root=card_root)
    checkpoint_path = author_dir / "_homepage_asr_checkpoint.json"
    if not checkpoint_path.is_file():
        return {}
    try:
        payload = json.loads(checkpoint_path.read_text(encoding="utf-8"))
    except Exception:
        return {}
    return payload if isinstance(payload, dict) else {}


def clear_homepage_checkpoint(*, platform: str, profile: Dict[str, Any], card_root: str) -> Optional[str]:
    author_dir = resolve_homepage_author_dir(platform=platform, profile=profile, card_root=card_root)
    checkpoint_path = author_dir / "_homepage_asr_checkpoint.json"
    if not checkpoint_path.exists():
        return None
    checkpoint_path.unlink()
    return str(checkpoint_path)


def persist_homepage_runtime_artifacts(
    *,
    platform: str,
    profile: Dict[str, Any],
    works: List[Dict[str, Any]],
    card_root: str,
    extract_trace: List[Dict[str, Any]],
    request_id: str,
    checkpoint: Optional[Dict[str, Any]],
    run_status: str,
    last_completed_batch_id: str = "",
) -> Dict[str, str]:
    author_dir = resolve_homepage_author_dir(platform=platform, profile=profile, card_root=card_root)
    updated_at = _now_iso()

    checkpoint_payload = checkpoint if isinstance(checkpoint, dict) else {}
    completed_work_ids = sorted({_safe_text(item) for item in (checkpoint_payload.get("completed_work_ids") or []) if _safe_text(item)})
    failed_work_ids = sorted({_safe_text(item) for item in (checkpoint_payload.get("failed_work_ids") or []) if _safe_text(item)})
    completed_id_set = set(completed_work_ids)
    failed_id_set = set(failed_work_ids)

    collection_items: List[Dict[str, Any]] = []
    for work in works:
        if not isinstance(work, dict):
            continue
        work_id = _safe_text(work.get("platform_work_id"))
        processing_status = "pending"
        if work_id in failed_id_set:
            processing_status = "failed"
        elif work_id in completed_id_set:
            processing_status = "completed"
        collection_items.append(
            {
                "platform_work_id": work_id,
                "title": work.get("title"),
                "published_date": work.get("published_date"),
                "processing_status": processing_status,
            }
        )

    completed_count = len(completed_work_ids)
    failed_count = len(failed_work_ids)
    total_count = len(collection_items)
    pending_count = max(0, total_count - completed_count)

    creator_profile = dict(profile)
    creator_profile.update(
        {
            "request_id": request_id,
            "extract_trace": extract_trace,
            "run_status": run_status,
            "completed_count": completed_count,
            "failed_count": failed_count,
            "pending_count": pending_count,
            "updated_at": updated_at,
        }
    )

    work_collection = {
        "platform": platform,
        "platform_author_id": profile.get("platform_author_id"),
        "count": total_count,
        "items": collection_items,
        "request_id": request_id,
        "extract_trace": extract_trace,
        "run_status": run_status,
        "completed_count": completed_count,
        "failed_count": failed_count,
        "pending_count": pending_count,
        "completed_work_ids": completed_work_ids,
        "failed_work_ids": failed_work_ids,
        "batch_size": checkpoint_payload.get("batch_size"),
        "batches_total": checkpoint_payload.get("batches_total"),
        "batches_completed": checkpoint_payload.get("batches_completed"),
        "batch_mapped": checkpoint_payload.get("batch_mapped"),
        "batch_unmapped": checkpoint_payload.get("batch_unmapped"),
        "fallback_singles": checkpoint_payload.get("fallback_singles"),
        "last_completed_batch_id": last_completed_batch_id or _safe_text(checkpoint_payload.get("last_completed_batch_id")),
        "updated_at": updated_at,
    }

    if checkpoint_payload:
        checkpoint_to_write = dict(checkpoint_payload)
        checkpoint_to_write["request_id"] = request_id
        checkpoint_to_write["updated_at"] = updated_at
        checkpoint_to_write["last_completed_batch_id"] = last_completed_batch_id or _safe_text(checkpoint_payload.get("last_completed_batch_id"))
    else:
        checkpoint_to_write = {}

    profile_path = author_dir / "_creator_profile.json"
    collection_path = author_dir / "_work_collection.json"
    checkpoint_path = author_dir / "_homepage_asr_checkpoint.json"
    profile_path.write_text(json.dumps(creator_profile, ensure_ascii=False, indent=2), encoding="utf-8")
    collection_path.write_text(json.dumps(work_collection, ensure_ascii=False, indent=2), encoding="utf-8")
    if checkpoint_to_write:
        checkpoint_path.write_text(json.dumps(checkpoint_to_write, ensure_ascii=False, indent=2), encoding="utf-8")

    return {
        "author_dir": str(author_dir),
        "creator_profile_path": str(profile_path),
        "work_collection_path": str(collection_path),
        "checkpoint_path": str(checkpoint_path),
    }


def resolve_homepage_run_status(stats: Optional[Dict[str, Any]]) -> str:
    payload = stats if isinstance(stats, dict) else {}
    total = int(payload.get("total") or 0)
    success = int(payload.get("success") or 0)
    failed = int(payload.get("fallback_none") or 0)
    if total <= 0:
        return "complete"
    if failed <= 0 and success >= total:
        return "complete"
    if success > 0:
        return "partial"
    return "failed"
