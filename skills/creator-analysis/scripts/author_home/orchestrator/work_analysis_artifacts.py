#!/usr/bin/env python3
"""Author-home work analysis artifact cache + worker orchestration."""

from __future__ import annotations

import hashlib
import json
from concurrent.futures import ThreadPoolExecutor, as_completed
from copy import deepcopy
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
import re

from scripts.core.analysis_pipeline import DEFAULT_INSIGHT_SECTION, DEFAULT_MODULE_SECTIONS, PROMPT_CONTRACT_FILES, contracts_dir
from scripts.core.config_loader import config_get, resolve_storage_paths
from scripts.core.progress_report import ProgressReporter
from scripts.writers.write_benchmark_card import build_card_analysis_artifact

WORK_ANALYSIS_ARTIFACT_VERSION = "creator_analysis.work_analysis_artifact@v4"
AUTHOR_HOME_TIMING_VERSION = "creator_analysis.author_home_timing@v2"
AUTHOR_HOME_CARD_CONTRACT_VERSION = "creator_analysis.author_sample_card@v2"
DOUYIN_NORMALIZATION_VERSION = "douyin_author_home_normalization@v2"
XHS_NORMALIZATION_VERSION = "xiaohongshu_author_home_normalization@v1"
DEFAULT_MAX_WORKERS = 3
MAX_MAX_WORKERS = 5
PERF_FIELDS = ("digg_count", "comment_count", "collect_count", "share_count", "play_count")


def _safe_text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value.strip()
    return str(value).strip()


def _safe_int(value: Any, default: int = 0) -> int:
    try:
        if value is None:
            return default
        if isinstance(value, bool):
            return int(value)
        if isinstance(value, (int, float)):
            return int(value)
        text = _safe_text(value).replace(",", "")
        return int(float(text)) if text else default
    except Exception:
        return default


def _safe_text_list(value: Any) -> List[str]:
    if not isinstance(value, list):
        return []
    result: List[str] = []
    for item in value:
        if isinstance(item, dict):
            for key in ("name", "value", "label", "hashtag_name", "search_text", "tag_name", "text"):
                text = _safe_text(item.get(key))
                if text:
                    result.append(text)
                    break
            continue
        text = _safe_text(item)
        if text:
            result.append(text)
    return list(dict.fromkeys(result))


def _normalization_version(platform: str) -> str:
    return DOUYIN_NORMALIZATION_VERSION if platform == "douyin" else XHS_NORMALIZATION_VERSION


def _coerce_unix_sec(value: Any) -> int:
    parsed = _safe_int(value, default=0)
    if parsed > 1_000_000_000_000:
        parsed //= 1000
    return parsed if parsed > 0 else 0


def _prompt_contract_hash() -> str:
    directory = Path(contracts_dir())
    sections = list(DEFAULT_MODULE_SECTIONS) + [DEFAULT_INSIGHT_SECTION]
    filenames = [PROMPT_CONTRACT_FILES.get(section, "") for section in sections if PROMPT_CONTRACT_FILES.get(section, "")]
    digest = hashlib.sha1()
    for filename in filenames:
        path = directory / filename
        digest.update(filename.encode("utf-8"))
        try:
            digest.update(path.read_text(encoding="utf-8").encode("utf-8"))
        except Exception:
            digest.update(b"missing")
    return digest.hexdigest()[:16]


PROMPT_CONTRACT_HASH = _prompt_contract_hash()


def _first_sentence(text: Any) -> str:
    clean = _safe_text(text)
    if not clean:
        return ""
    for chunk in clean.replace("\r", "\n").split("\n"):
        row = _safe_text(chunk)
        if row:
            return row
    units = [part.strip() for part in re.split(r"[。！？!?；;]+", clean) if part.strip()]
    return units[0] if units else clean[:80]


def _format_metric_summary(work: Dict[str, Any]) -> str:
    metrics = _metrics_from_work(work)
    return (
        f"赞 {metrics['digg_count']} / 评 {metrics['comment_count']} / 藏 {metrics['collect_count']} / "
        f"转 {metrics['share_count']} / 播 {metrics['play_count']}"
    )


def _author_home_structural_sections(work: Dict[str, Any]) -> Dict[str, Any]:
    tags = _safe_text_list(work.get("tags"))
    style_markers = _safe_text_list(work.get("style_markers"))
    first_sentence = _first_sentence(work.get("primary_text") or work.get("asr_raw") or work.get("caption_raw") or work.get("title"))
    bucket = _safe_text(work.get("bucket")) or "unknown"
    all_time_rank = work.get("all_time_score_rank")
    recent_rank = work.get("recent_30d_score_rank")
    recent_rank_text = recent_rank if recent_rank is not None else "NA"
    work_modality = _safe_text(work.get("work_modality")) or "unknown"
    primary_text_source = _safe_text(work.get("primary_text_source"))
    if primary_text_source not in {"asr_clean", "caption_raw"}:
        primary_text_source = "asr_clean" if work_modality == "video" else "caption_raw"
    primary_text_label = "视频口播清洗文本" if primary_text_source == "asr_clean" else "作者原始文案"
    has_primary_text = bool(_safe_text(work.get("primary_text")))
    modules = {
        "选题": [
            f"- 原始 tags：{'、'.join(tags[:6]) if tags else '无'}。",
            f"- 分桶/排名：bucket={bucket} / all_time_rank={all_time_rank or 'NA'} / recent_30d_rank={recent_rank_text}。",
            f"- 主文本载体：{primary_text_label}。",
        ],
        "文风": [
            f"- 内容形态：work_modality={work_modality} / content_form={_safe_text(work.get('content_form')) or 'unknown'}。",
            f"- 表达标记：{'、'.join(style_markers[:6]) if style_markers else '未命中显著 style_markers'}。",
            f"- 数据状态：{'主文本已就绪' if has_primary_text else '主文本缺失，仅保留事实字段'}。",
        ],
        "Hook": [
            f"- hook_type：{_safe_text(work.get('hook_type')) or 'unknown'}。",
            f"- 开头原句：{first_sentence or '无可用主文本'}",
        ],
        "结构": [
            f"- structure_type：{_safe_text(work.get('structure_type')) or 'unknown'}。",
            f"- cta_type：{_safe_text(work.get('cta_type')) or 'unknown'}。",
            f"- performance_score_norm：{work.get('performance_score_norm') if work.get('performance_score_norm') is not None else 'NA'}。",
        ],
    }
    insight = [
        f"- 表现摘要：{_format_metric_summary(work)}。",
        f"- 样本定位：这是作者主页样本卡，只保留事实字段与结构标签；不做逐条 rigid 语义赛道分类。",
        f"- 可复用观察：优先参考 bucket / hook_type / structure_type / cta_type / content_form 的组合，而不是把单条作品硬归为某个固定 topic。",
    ]
    return {"modules": modules, "insight": insight}


def _metrics_from_work(work: Dict[str, Any]) -> Dict[str, int]:
    metrics = work.get("metrics") if isinstance(work.get("metrics"), dict) else {}
    return {
        "digg_count": _safe_int(work.get("digg_count"), default=_safe_int(metrics.get("like"), default=0)),
        "comment_count": _safe_int(work.get("comment_count"), default=_safe_int(metrics.get("comment"), default=0)),
        "collect_count": _safe_int(work.get("collect_count"), default=_safe_int(metrics.get("collect"), default=0)),
        "share_count": _safe_int(work.get("share_count"), default=_safe_int(metrics.get("share"), default=0)),
        "play_count": _safe_int(work.get("play_count"), default=_safe_int(metrics.get("play"), default=0)),
    }


def build_single_work_payload(
    *,
    platform: str,
    profile: Dict[str, Any],
    work: Dict[str, Any],
) -> Dict[str, Any]:
    author_platform_id = _safe_text(profile.get("author_platform_id") or profile.get("platform_author_id"))
    author_handle = _safe_text(profile.get("author_handle"))
    author = {
        "nickname": profile.get("nickname"),
        "platform_author_id": author_platform_id,
        "author_handle": author_handle,
    }
    payload: Dict[str, Any] = {
        "content_kind": "author_home",
        "platform_work_id": work.get("platform_work_id"),
        "title": work.get("title") or work.get("desc"),
        "caption_raw": work.get("caption_raw") or work.get("desc") or "",
        "desc": work.get("caption_raw") or work.get("desc") or work.get("title"),
        "source_url": work.get("source_url"),
        "share_url": work.get("share_url"),
        "cover_image": work.get("cover_image"),
        "video_download_url": work.get("video_download_url") or work.get("video_down_url"),
        "author": author,
        "author_handle": author_handle,
        "platform_author_id": author_platform_id,
        "publish_time": work.get("publish_time"),
        "published_date": work.get("published_date"),
        "duration_ms": _safe_int(work.get("duration_ms"), default=0),
        "summary": _safe_text(work.get("summary")),
        "insights": ["source=author_home_work_analysis_artifact", "analysis_strategy=structural_sample_card"],
        "raw_content": _safe_text(work.get("asr_raw")),
        "primary_text": _safe_text(work.get("primary_text")),
        "primary_text_source": _safe_text(work.get("primary_text_source")),
        "asr_clean": _safe_text(work.get("asr_clean")),
        "tags": list(work.get("tags") or []) if isinstance(work.get("tags"), list) else [],
        "work_modality": _safe_text(work.get("work_modality")) or ("video" if platform == "douyin" else "text"),
        "analysis_eligibility": _safe_text(work.get("analysis_eligibility")) or "eligible",
        "analysis_exclusion_reason": _safe_text(work.get("analysis_exclusion_reason")),
        "performance_score": work.get("performance_score"),
        "performance_score_norm": work.get("performance_score_norm"),
        "bucket": _safe_text(work.get("bucket")),
        "hook_type": _safe_text(work.get("hook_type")),
        "structure_type": _safe_text(work.get("structure_type")),
        "cta_type": _safe_text(work.get("cta_type")),
        "content_form": _safe_text(work.get("content_form")),
        "style_markers": _safe_text_list(work.get("style_markers")),
        "platform_native_refs": dict(work.get("platform_native_refs") or {}),
        "request_id": work.get("request_id"),
        "confidence": "medium" if _safe_text(work.get("primary_text") or work.get("title") or work.get("caption_raw")) else "low",
        "error_reason": None,
        "extract_trace": [],
    }
    payload.update(_metrics_from_work(work))
    payload["analysis_sections"] = _author_home_structural_sections(work)
    return payload


def _artifact_cache_key(*, platform: str, content_kind: str, platform_work_id: str) -> str:
    raw = "|".join(
        [
            platform,
            content_kind,
            platform_work_id,
            WORK_ANALYSIS_ARTIFACT_VERSION,
            PROMPT_CONTRACT_HASH,
            AUTHOR_HOME_TIMING_VERSION,
            AUTHOR_HOME_CARD_CONTRACT_VERSION,
        ]
    )
    return hashlib.sha1(raw.encode("utf-8")).hexdigest()[:20]


def _resolve_artifact_root(storage_config: Optional[Dict[str, Any]]) -> Optional[Path]:
    try:
        paths = resolve_storage_paths(storage_config or {})
    except Exception:
        return None
    runs_root = Path(str(paths.get("runs_root") or "").strip())
    if not str(runs_root):
        return None
    return runs_root / "author_home_work_analysis_artifacts"


def _artifact_path(*, artifact_root: Optional[Path], platform: str, platform_work_id: str, content_kind: str) -> Tuple[Optional[Path], Optional[str]]:
    if artifact_root is None or not platform_work_id:
        return None, None
    cache_key = _artifact_cache_key(platform=platform, content_kind=content_kind, platform_work_id=platform_work_id)
    safe_work_id = hashlib.sha1(platform_work_id.encode("utf-8")).hexdigest()[:12]
    return artifact_root / platform / f"{safe_work_id}-{cache_key}.json", cache_key


def _load_cached_artifact(
    *,
    artifact_root: Optional[Path],
    platform: str,
    content_kind: str,
    platform_work_id: str,
) -> Optional[Dict[str, Any]]:
    path, cache_key = _artifact_path(
        artifact_root=artifact_root,
        platform=platform,
        platform_work_id=platform_work_id,
        content_kind=content_kind,
    )
    if path is None or cache_key is None or not path.is_file():
        return None
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return None
    meta = payload.get("meta") if isinstance(payload.get("meta"), dict) else {}
    if meta.get("cache_key") != cache_key:
        return None
    if meta.get("analysis_logic_version") != WORK_ANALYSIS_ARTIFACT_VERSION:
        return None
    if meta.get("prompt_contract_hash") != PROMPT_CONTRACT_HASH:
        return None
    if meta.get("author_home_timing_version") != AUTHOR_HOME_TIMING_VERSION:
        return None
    if meta.get("author_sample_card_contract_version") != AUTHOR_HOME_CARD_CONTRACT_VERSION:
        return None
    if meta.get("normalization_version") != _normalization_version(platform):
        return None
    return payload if isinstance(payload, dict) else None


def _write_cached_artifact(
    *,
    artifact_root: Optional[Path],
    artifact: Dict[str, Any],
) -> Optional[str]:
    meta = artifact.get("meta") if isinstance(artifact.get("meta"), dict) else {}
    path, _ = _artifact_path(
        artifact_root=artifact_root,
        platform=_safe_text(meta.get("platform")),
        platform_work_id=_safe_text(meta.get("platform_work_id")),
        content_kind=_safe_text(meta.get("content_kind")),
    )
    if path is None:
        return None
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(artifact, ensure_ascii=False, indent=2), encoding="utf-8")
    return str(path)


def _refresh_cached_payload(
    *,
    artifact: Dict[str, Any],
    profile: Dict[str, Any],
    work: Dict[str, Any],
    from_cache: bool,
    artifact_path: Optional[str],
) -> Dict[str, Any]:
    payload = deepcopy(artifact.get("payload") if isinstance(artifact.get("payload"), dict) else {})
    payload["analysis_sections"] = deepcopy(
        artifact.get("analysis_sections") if isinstance(artifact.get("analysis_sections"), dict) else {}
    )
    payload["extract_trace"] = list(payload.get("extract_trace") or [])
    payload["extract_trace"].append(
        {
            "step": "author_home.work_analysis.cache_hit" if from_cache else "author_home.work_analysis.generated",
            "platform_work_id": work.get("platform_work_id"),
            "ok": True,
            "artifact_cache_key": ((artifact.get("meta") or {}).get("cache_key") if isinstance(artifact.get("meta"), dict) else None),
            "artifact_path": artifact_path,
            "from_cache": from_cache,
            "artifact_version": ((artifact.get("meta") or {}).get("analysis_logic_version") if isinstance(artifact.get("meta"), dict) else None),
            "normalization_version": ((artifact.get("meta") or {}).get("normalization_version") if isinstance(artifact.get("meta"), dict) else None),
        }
    )
    payload["request_id"] = work.get("request_id") or payload.get("request_id")
    payload["author"] = {
        "nickname": profile.get("nickname"),
        "platform_author_id": profile.get("author_platform_id") or profile.get("platform_author_id"),
        "author_handle": profile.get("author_handle") or "",
    }
    payload["author_handle"] = profile.get("author_handle") or ""
    payload["platform_author_id"] = profile.get("author_platform_id") or profile.get("platform_author_id")
    for field, value in _metrics_from_work(work).items():
        payload[field] = value
    return payload


def _build_artifact(
    *,
    platform: str,
    profile: Dict[str, Any],
    work: Dict[str, Any],
) -> Dict[str, Any]:
    payload = build_single_work_payload(platform=platform, profile=profile, work=work)
    analysis_artifact = build_card_analysis_artifact(payload=payload, platform=platform, card_type="work")
    payload["analysis_sections"] = deepcopy(analysis_artifact.get("analysis_sections") or {})
    payload["extract_trace"] = list(payload.get("extract_trace") or [])
    payload["extract_trace"].append(
        {
            "step": "author_home.work_analysis.generated",
            "platform_work_id": work.get("platform_work_id"),
            "ok": True,
            "prompt_contract_hash": PROMPT_CONTRACT_HASH,
            "artifact_version": WORK_ANALYSIS_ARTIFACT_VERSION,
            "normalization_version": _normalization_version(platform),
        }
    )
    platform_work_id = _safe_text(work.get("platform_work_id"))
    return {
        "meta": {
            "platform": platform,
            "platform_work_id": platform_work_id,
            "content_kind": _safe_text(payload.get("content_kind")) or "author_home",
            "analysis_logic_version": WORK_ANALYSIS_ARTIFACT_VERSION,
            "prompt_contract_hash": PROMPT_CONTRACT_HASH,
            "author_home_timing_version": AUTHOR_HOME_TIMING_VERSION,
            "author_sample_card_contract_version": AUTHOR_HOME_CARD_CONTRACT_VERSION,
            "normalization_version": _normalization_version(platform),
            "cache_key": _artifact_cache_key(
                platform=platform,
                content_kind=_safe_text(payload.get("content_kind")) or "author_home",
                platform_work_id=platform_work_id,
            ) if platform_work_id else None,
            "written_at": datetime.now().isoformat(timespec="seconds"),
        },
        "payload": payload,
        "analysis_sections": analysis_artifact.get("analysis_sections") if isinstance(analysis_artifact.get("analysis_sections"), dict) else {},
        "required_fields": analysis_artifact.get("fields") if isinstance(analysis_artifact.get("fields"), dict) else {},
    }


def _resolve_max_workers(storage_config: Optional[Dict[str, Any]]) -> int:
    configured = config_get(storage_config or {}, "author_home.work_analysis.max_workers", DEFAULT_MAX_WORKERS)
    try:
        value = int(configured)
    except Exception:
        value = DEFAULT_MAX_WORKERS
    return min(max(value, 1), MAX_MAX_WORKERS)


def orchestrate_work_analysis_artifacts(
    *,
    platform: str,
    profile: Dict[str, Any],
    works: List[Dict[str, Any]],
    storage_config: Optional[Dict[str, Any]],
    progress: Optional[ProgressReporter] = None,
) -> Dict[str, Any]:
    artifact_root = _resolve_artifact_root(storage_config)
    max_workers = _resolve_max_workers(storage_config)
    stats = {
        "total_count": len(works),
        "cache_hit_count": 0,
        "queued_count": 0,
        "running_workers": 0,
        "running_workers_peak": 0,
        "finished_count": 0,
        "failed_count": 0,
        "max_workers": max_workers,
    }
    trace: List[Dict[str, Any]] = []
    failed_items: List[Dict[str, Any]] = []
    render_payloads: Dict[str, Dict[str, Any]] = {}
    artifact_manifest: Dict[str, Dict[str, Any]] = {}
    queue: List[Dict[str, Any]] = []

    if progress is not None:
        progress.started(
            stage="author_home.work_analysis",
            message="preparing work analysis artifacts",
            data={"total_count": len(works), "max_workers": max_workers},
        )

    for work in works:
        platform_work_id = _safe_text(work.get("platform_work_id"))
        content_kind = "author_home"
        if not platform_work_id:
            stats["failed_count"] += 1
            failed_items.append({"platform_work_id": "", "error_reason": "missing_platform_work_id"})
            trace.append(
                {
                    "step": "author_home.work_analysis.failed",
                    "platform_work_id": "",
                    "ok": False,
                    "error_reason": "missing_platform_work_id",
                }
            )
            continue
        cached = _load_cached_artifact(
            artifact_root=artifact_root,
            platform=platform,
            content_kind=content_kind,
            platform_work_id=platform_work_id,
        ) if platform_work_id else None
        if cached is not None:
            artifact_path, _ = _artifact_path(
                artifact_root=artifact_root,
                platform=platform,
                platform_work_id=platform_work_id,
                content_kind=content_kind,
            )
            payload = _refresh_cached_payload(
                artifact=cached,
                profile=profile,
                work=work,
                from_cache=True,
                artifact_path=str(artifact_path) if artifact_path is not None else None,
            )
            render_payloads[platform_work_id] = payload
            artifact_manifest[platform_work_id] = {
                "from_cache": True,
                "artifact_path": str(artifact_path) if artifact_path is not None else None,
                "artifact_version": WORK_ANALYSIS_ARTIFACT_VERSION,
                "prompt_contract_hash": PROMPT_CONTRACT_HASH,
                "normalization_version": _normalization_version(platform),
            }
            stats["cache_hit_count"] += 1
            trace.append(
                {
                    "step": "author_home.work_analysis.cache_hit",
                    "platform_work_id": platform_work_id,
                    "ok": True,
                    "artifact_path": str(artifact_path) if artifact_path is not None else None,
                }
            )
            continue
        queue.append(work)

    stats["queued_count"] = len(queue)
    if progress is not None:
        progress.progress(
            stage="author_home.work_analysis.queue",
            message="work analysis queue prepared",
            data={
                "cache_hit_count": stats["cache_hit_count"],
                "queued_count": stats["queued_count"],
                "running_workers": stats["running_workers"],
                "finished_count": stats["finished_count"],
                "failed_count": stats["failed_count"],
            },
        )

    if queue:
        queued_failed_count = 0
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_map = {
                executor.submit(_build_artifact, platform=platform, profile=profile, work=work): work
                for work in queue
            }
            stats["running_workers"] = min(len(future_map), max_workers)
            stats["running_workers_peak"] = min(len(future_map), max_workers)
            for future in as_completed(future_map):
                work = future_map[future]
                platform_work_id = _safe_text(work.get("platform_work_id"))
                try:
                    artifact = future.result()
                    artifact_path = _write_cached_artifact(artifact_root=artifact_root, artifact=artifact)
                    payload = _refresh_cached_payload(
                        artifact=artifact,
                        profile=profile,
                        work=work,
                        from_cache=False,
                        artifact_path=artifact_path,
                    )
                    if platform_work_id:
                        render_payloads[platform_work_id] = payload
                        artifact_manifest[platform_work_id] = {
                            "from_cache": False,
                            "artifact_path": artifact_path,
                            "artifact_version": WORK_ANALYSIS_ARTIFACT_VERSION,
                            "prompt_contract_hash": PROMPT_CONTRACT_HASH,
                            "normalization_version": _normalization_version(platform),
                        }
                    stats["finished_count"] += 1
                    trace.append(
                        {
                            "step": "author_home.work_analysis.generated",
                            "platform_work_id": platform_work_id,
                            "ok": True,
                            "artifact_path": artifact_path,
                        }
                    )
                except Exception as error:
                    queued_failed_count += 1
                    stats["failed_count"] += 1
                    failed_items.append(
                        {
                            "platform_work_id": platform_work_id,
                            "error_reason": f"{type(error).__name__}:{error}",
                        }
                    )
                    trace.append(
                        {
                            "step": "author_home.work_analysis.failed",
                            "platform_work_id": platform_work_id,
                            "ok": False,
                            "error_reason": f"{type(error).__name__}:{error}",
                        }
                    )
                finally:
                    remaining = max(stats["queued_count"] - stats["finished_count"] - queued_failed_count, 0)
                    stats["running_workers"] = min(remaining, max_workers)
                    if progress is not None:
                        progress.progress(
                            stage="author_home.work_analysis.progress",
                            message="work analysis artifact progress updated",
                            data={
                                "cache_hit_count": stats["cache_hit_count"],
                                "queued_count": stats["queued_count"],
                                "running_workers": stats["running_workers"],
                                "finished_count": stats["finished_count"],
                                "failed_count": stats["failed_count"],
                            },
                        )

    if progress is not None:
        final_event = progress.failed if stats["failed_count"] else progress.done
        final_event(
            stage="author_home.work_analysis",
            message="work analysis artifacts ready" if not stats["failed_count"] else "work analysis artifacts partially failed",
            data={
                "cache_hit_count": stats["cache_hit_count"],
                "queued_count": stats["queued_count"],
                "running_workers": stats["running_workers"],
                "finished_count": stats["finished_count"],
                "failed_count": stats["failed_count"],
            },
        )

    return {
        "render_payloads": render_payloads,
        "artifact_manifest": artifact_manifest,
        "stats": stats,
        "failed_items": failed_items,
        "trace": trace,
        "artifact_root": str(artifact_root) if artifact_root is not None else None,
        "analysis_logic_version": WORK_ANALYSIS_ARTIFACT_VERSION,
        "prompt_contract_hash": PROMPT_CONTRACT_HASH,
        "normalization_version": _normalization_version(platform),
    }
