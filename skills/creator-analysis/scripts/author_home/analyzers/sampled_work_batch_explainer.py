#!/usr/bin/env python3
"""Batch explanations for sampled works."""

from __future__ import annotations

import json
import os
import re
import subprocess
from pathlib import Path
from typing import Any, Dict, List, Tuple

import jsonschema


PROMPT_CONTRACT_PATH = Path(__file__).resolve().parents[2] / "references" / "prompt-contracts" / "sampled-work-batch-explanations.md"
SCHEMA_PATH = Path(__file__).resolve().parents[2] / "references" / "schemas" / "sampled-work-batch-explanations.schema.json"
DEFAULT_TIMEOUT_SEC = 45
TEXT_LIMITS = {
    "title": 120,
    "caption_raw": 220,
    "primary_text": 420,
    "top_list": 8,
}


def _safe_text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value.strip()
    return str(value).strip()


def _truncate_text(value: Any, limit: int) -> str:
    text = _safe_text(value)
    if limit <= 0 or len(text) <= limit:
        return text
    return text[: max(limit - 1, 0)] + "…"


def _load_json(path: Path) -> Dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def _schema_errors(payload: Any) -> List[Dict[str, str]]:
    schema = _load_json(SCHEMA_PATH)
    if not schema:
        return []
    try:
        validator = jsonschema.Draft202012Validator(schema)
        errors: List[Dict[str, str]] = []
        for error in sorted(validator.iter_errors(payload), key=lambda item: list(item.absolute_path)):
            field = ".".join(str(part) for part in error.absolute_path) or "$"
            errors.append({"field": field, "reason": f"schema:{error.message}"})
        return errors
    except Exception as error:
        return [{"field": "$", "reason": f"schema_runtime:{type(error).__name__}:{error}"}]


def _prompt_contract_text() -> str:
    try:
        return PROMPT_CONTRACT_PATH.read_text(encoding="utf-8").strip()
    except Exception:
        return ""


def _extract_json_block(text: str) -> Dict[str, Any]:
    content = (text or "").strip()
    if not content:
        return {}
    try:
        return json.loads(content)
    except Exception:
        pass

    fenced = re.search(r"```(?:json)?\s*(\{[\s\S]*?\})\s*```", content)
    if fenced:
        try:
            return json.loads(fenced.group(1))
        except Exception:
            pass

    match = re.search(r"\{[\s\S]*\}", content)
    if not match:
        return {}
    try:
        return json.loads(match.group(0))
    except Exception:
        return {}


def _compact_input(analysis_input: Dict[str, Any]) -> Dict[str, Any]:
    sampled = analysis_input.get("sampled_works") if isinstance(analysis_input.get("sampled_works"), list) else []
    aggregate = analysis_input.get("aggregate_stats") if isinstance(analysis_input.get("aggregate_stats"), dict) else {}
    deltas = aggregate.get("global_top_vs_mid_vs_bottom_deltas") if isinstance(aggregate.get("global_top_vs_mid_vs_bottom_deltas"), dict) else {}

    compacted_sampled: List[Dict[str, Any]] = []
    for item in sampled:
        if not isinstance(item, dict):
            continue
        compacted_sampled.append(
            {
                "platform_work_id": _safe_text(item.get("platform_work_id")),
                "title": _truncate_text(item.get("title"), TEXT_LIMITS["title"]),
                "caption_raw": _truncate_text(item.get("caption_raw"), TEXT_LIMITS["caption_raw"]),
                "work_modality": _safe_text(item.get("work_modality")),
                "primary_text": _truncate_text(item.get("primary_text"), TEXT_LIMITS["primary_text"]),
                "bucket": _safe_text(item.get("bucket")),
                "hook_type": _safe_text(item.get("hook_type")),
                "structure_type": _safe_text(item.get("structure_type")),
                "cta_type": _safe_text(item.get("cta_type")),
                "content_form": _safe_text(item.get("content_form")),
                "style_markers": list(item.get("style_markers") or [])[: TEXT_LIMITS["top_list"]],
                "digg_count": item.get("digg_count"),
                "comment_count": item.get("comment_count"),
                "collect_count": item.get("collect_count"),
                "share_count": item.get("share_count"),
                "play_count": item.get("play_count"),
            }
        )

    compacted_deltas: Dict[str, Any] = {}
    for group in ("top", "mid", "bottom"):
        block = deltas.get(group) if isinstance(deltas, dict) else None
        if not isinstance(block, dict):
            continue
        compacted_deltas[group] = {
            "title_keywords": list(block.get("title_keywords") or [])[: TEXT_LIMITS["top_list"]],
            "caption_keywords": list(block.get("caption_keywords") or [])[: TEXT_LIMITS["top_list"]],
            "primary_text_keywords": list(block.get("primary_text_keywords") or [])[: TEXT_LIMITS["top_list"]],
            "hook_types": list(block.get("hook_types") or [])[: TEXT_LIMITS["top_list"]],
            "structure_types": list(block.get("structure_types") or [])[: TEXT_LIMITS["top_list"]],
            "cta_types": list(block.get("cta_types") or [])[: TEXT_LIMITS["top_list"]],
            "content_forms": list(block.get("content_forms") or [])[: TEXT_LIMITS["top_list"]],
        }

    return {
        "sampled_works": compacted_sampled,
        "aggregate_deltas": compacted_deltas,
    }


def _build_prompt(analysis_input: Dict[str, Any]) -> str:
    compacted = _compact_input(analysis_input)
    return (
        "请严格根据以下提示词原文输出，结果必须是 JSON 对象，且只输出 JSON。\n"
        "顶层对象必须是 sampled_work_explanations。\n"
        "不得输出 markdown，不得输出解释。\n\n"
        "=== 提示词原文开始 ===\n"
        f"{_prompt_contract_text()}\n"
        "=== 提示词原文结束 ===\n\n"
        "=== 输入数据(JSON) ===\n"
        f"{json.dumps(compacted, ensure_ascii=False)}"
    )


def _fallback_explanations(analysis_input: Dict[str, Any]) -> Dict[str, Any]:
    sampled = analysis_input.get("sampled_works") if isinstance(analysis_input.get("sampled_works"), list) else []
    explanations: Dict[str, Any] = {}
    for item in sampled:
        if not isinstance(item, dict):
            continue
        work_id = _safe_text(item.get("platform_work_id"))
        if not work_id:
            continue
        explanations[work_id] = {
            "why_it_worked_or_failed": f"该样本主要依赖 { _safe_text(item.get('hook_type')) or 'hook' }、{ _safe_text(item.get('structure_type')) or 'structure' } 与 { _safe_text(item.get('content_form')) or 'content_form' } 的组合。",
            "copyable_elements": [value for value in [_safe_text(item.get("hook_type")), _safe_text(item.get("structure_type")), _safe_text(item.get("cta_type"))] if value],
            "non_copyable_elements": ["具体个人经历或原始案例背书"],
            "emotional_triggers": [_safe_text(item.get("hook_type")) or "结果预期"],
            "cognitive_gap": "观众想知道为什么这个结构能成立，以及自己如何快速套用。",
            "commercial_signal": "从 CTA 与内容结构看，具备基础商业承接意图，但证据仍有限。",
        }
    return {"sampled_work_explanations": explanations}


def _coverage_errors(payload: Dict[str, Any], analysis_input: Dict[str, Any]) -> List[Dict[str, str]]:
    sampled = analysis_input.get("sampled_works") if isinstance(analysis_input.get("sampled_works"), list) else []
    explanations = payload.get("sampled_work_explanations") if isinstance(payload.get("sampled_work_explanations"), dict) else {}
    errors: List[Dict[str, str]] = []
    for item in sampled:
        if not isinstance(item, dict):
            continue
        work_id = _safe_text(item.get("platform_work_id"))
        if not work_id:
            continue
        if not isinstance(explanations.get(work_id), dict):
            errors.append({"field": f"sampled_work_explanations.{work_id}", "reason": "missing_work_explanation"})
    return errors


def run_sampled_work_batch_explanations(analysis_input: Dict[str, Any]) -> Tuple[Dict[str, Any], List[Dict[str, str]], List[Dict[str, Any]]]:
    sampled = analysis_input.get("sampled_works") if isinstance(analysis_input.get("sampled_works"), list) else []
    trace: List[Dict[str, Any]] = [
        {
            "step": "sampled_work_explanations.input_built",
            "sampled_works_count": len(sampled),
            "prompt_contract": "prompt-contracts/sampled-work-batch-explanations.md@v1",
        }
    ]

    if not sampled:
        trace.append({"step": "sampled_work_explanations.skipped", "reason": "empty_sampled_works"})
        return {"sampled_work_explanations": {}}, [], trace

    llm_timeout_sec = max(int(os.getenv("TIKOMNI_SAMPLED_EXPLANATION_TIMEOUT_SEC", str(DEFAULT_TIMEOUT_SEC))), 5)
    prompt = _build_prompt(analysis_input)
    result: Dict[str, Any] = {}
    errors: List[Dict[str, str]] = []

    try:
        run = subprocess.run(
            ["openclaw", "agent", "--agent", "main", "--message", prompt, "--json"],
            capture_output=True,
            text=True,
            timeout=llm_timeout_sec,
            check=False,
        )
        parsed = json.loads(run.stdout or "{}")
        chunks: List[str] = []
        for item in parsed.get("result", {}).get("payloads", []):
            if isinstance(item, dict) and isinstance(item.get("text"), str):
                chunks.append(item["text"])
        response_text = "\n".join(chunks).strip()
        result = _extract_json_block(response_text)
        trace.append(
            {
                "step": "sampled_work_explanations.llm_called",
                "returncode": run.returncode,
                "has_text": bool(response_text),
                "parsed": bool(result),
                "stdout_chars": len(run.stdout or ""),
                "stderr_chars": len(run.stderr or ""),
            }
        )
    except Exception as error:
        trace.append({"step": "sampled_work_explanations.llm_error", "error": f"{type(error).__name__}:{error}"})

    errors = _schema_errors(result) if result else [{"field": "$", "reason": "empty_result"}]
    if not errors:
        errors.extend(_coverage_errors(result, analysis_input))
    if errors:
        fallback = _fallback_explanations(analysis_input)
        fallback_errors = _schema_errors(fallback) + _coverage_errors(fallback, analysis_input)
        trace.append(
            {
                "step": "sampled_work_explanations.fallback_used",
                "reason": "llm_empty_or_validation_failed",
                "validation_error_count": len(errors),
                "fallback_error_count": len(fallback_errors),
            }
        )
        return fallback, errors + fallback_errors, trace

    trace.append({"step": "sampled_work_explanations.schema_validation_passed"})
    return result, [], trace
