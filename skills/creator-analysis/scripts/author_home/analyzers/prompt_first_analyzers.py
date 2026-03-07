#!/usr/bin/env python3
"""Prompt-first analyzers for author-home insights."""

from __future__ import annotations

import json
import os
import re
import subprocess
from typing import Any, Dict, List, Tuple

from scripts.author_home.analyzers.author_analysis_v2_support import (
    build_author_analysis_input_v1,
    build_fallback_author_analysis_v2,
    derive_legacy_summary,
    prompt_contract_text,
    validate_author_analysis_v2,
)
from scripts.author_home.analyzers.sampled_work_batch_explainer import run_sampled_work_batch_explanations

AUTHOR_ANALYSIS_PROMPT_FILE = "author-analysis-v2.md"
DEFAULT_ANALYSIS_TIMEOUT_SEC = 45
DEFAULT_SMALL_SAMPLE_SKIP_THRESHOLD = 5
PROMPT_TEXT_LIMITS = {
    "title": 120,
    "caption_raw": 240,
    "primary_text": 480,
    "signature": 160,
    "top_list": 8,
    "notes": 6,
}


def _truncate_text(value: Any, limit: int) -> str:
    text = str(value or "").strip()
    if limit <= 0 or len(text) <= limit:
        return text
    return text[: max(limit - 1, 0)] + "…"



def _compact_distribution(block: Any, *, item_limit: int) -> Any:
    if not isinstance(block, dict):
        return block
    compacted = dict(block)
    items = compacted.get("items")
    if isinstance(items, list):
        compacted["items"] = items[:item_limit]
    return compacted



def _compact_analysis_input_for_prompt(analysis_input: Dict[str, Any]) -> Dict[str, Any]:
    compacted = json.loads(json.dumps(analysis_input, ensure_ascii=False))

    author_profile = compacted.get("author_profile")
    if isinstance(author_profile, dict):
        author_profile["signature"] = _truncate_text(author_profile.get("signature"), PROMPT_TEXT_LIMITS["signature"])

    sampled_works = compacted.get("sampled_works")
    if isinstance(sampled_works, list):
        trimmed_works: List[Dict[str, Any]] = []
        for work in sampled_works:
            if not isinstance(work, dict):
                continue
            row = dict(work)
            row["title"] = _truncate_text(row.get("title"), PROMPT_TEXT_LIMITS["title"])
            row["caption_raw"] = _truncate_text(row.get("caption_raw"), PROMPT_TEXT_LIMITS["caption_raw"])
            row["primary_text"] = _truncate_text(row.get("primary_text"), PROMPT_TEXT_LIMITS["primary_text"])
            if isinstance(row.get("tags"), list):
                row["tags"] = row.get("tags")[: PROMPT_TEXT_LIMITS["top_list"]]
            if isinstance(row.get("style_markers"), list):
                row["style_markers"] = row.get("style_markers")[: PROMPT_TEXT_LIMITS["top_list"]]
            trimmed_works.append(row)
        compacted["sampled_works"] = trimmed_works

    aggregate_stats = compacted.get("aggregate_stats")
    if isinstance(aggregate_stats, dict):
        for key in (
            "global_title_keyword_distribution",
            "global_caption_keyword_distribution",
            "global_primary_text_keyword_distribution",
            "global_hook_type_distribution",
            "global_structure_type_distribution",
            "global_cta_type_distribution",
            "global_content_form_distribution",
            "global_work_modality_distribution",
            "global_bucket_distribution",
        ):
            aggregate_stats[key] = _compact_distribution(aggregate_stats.get(key), item_limit=PROMPT_TEXT_LIMITS["top_list"])
        deltas = aggregate_stats.get("global_top_vs_mid_vs_bottom_deltas")
        if isinstance(deltas, dict):
            for group in ("top", "mid", "bottom"):
                block = deltas.get(group)
                if not isinstance(block, dict):
                    continue
                for key in ("title_keywords", "caption_keywords", "primary_text_keywords", "hook_types", "structure_types", "cta_types", "content_forms"):
                    value = block.get(key)
                    if isinstance(value, list):
                        block[key] = value[: PROMPT_TEXT_LIMITS["top_list"]]
        duration_dist = aggregate_stats.get("global_duration_distribution")
        if isinstance(duration_dist, dict) and isinstance(duration_dist.get("items"), list):
            duration_dist["items"] = duration_dist["items"][:3]

    return compacted



def _build_prompt(analysis_input: Dict[str, Any], sampled_work_explanations: Dict[str, Any]) -> str:
    contract_prompt = prompt_contract_text()
    prompt_input = _compact_analysis_input_for_prompt(analysis_input)
    prompt_payload = {"author_analysis_input_v1": prompt_input}
    if isinstance(sampled_work_explanations, dict) and sampled_work_explanations.get("sampled_work_explanations"):
        prompt_payload["sampled_work_explanations"] = sampled_work_explanations["sampled_work_explanations"]
    return (
        "请严格根据以下提示词原文输出，结果必须是 JSON 对象，且只输出 JSON。\n"
        "顶层对象必须是 author_analysis_v2。\n"
        "不得输出 markdown，不得输出解释。\n\n"
        "=== 提示词原文开始 ===\n"
        f"{contract_prompt}\n"
        "=== 提示词原文结束 ===\n\n"
        "=== 标准化输入对象名 ===\n"
        "author_analysis_input_v1\n\n"
        "=== 输入数据(JSON) ===\n"
        f"{json.dumps(prompt_payload, ensure_ascii=False)}"
    )


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


def _unwrap_author_analysis(payload: Dict[str, Any]) -> Dict[str, Any]:
    if not isinstance(payload, dict):
        return {}
    if isinstance(payload.get("author_analysis_v2"), dict):
        return payload["author_analysis_v2"]
    return payload


def run_prompt_first_author_analysis(profile: Dict[str, Any], works: List[Dict[str, Any]]) -> Tuple[Dict[str, Any], List[Dict[str, str]], List[Dict[str, Any]]]:
    analysis_input, input_errors = build_author_analysis_input_v1(profile=profile, works=works, platform=str(profile.get("platform") or "unknown"))
    sampled_work_explanations, sampled_explanation_errors, sampled_explanation_trace = run_sampled_work_batch_explanations(analysis_input)
    sampled_works_count = len(analysis_input.get("sampled_works") or [])
    total_works = ((analysis_input.get("aggregate_stats") or {}).get("total_works") if isinstance(analysis_input.get("aggregate_stats"), dict) else 0)
    llm_timeout_sec = max(int(os.getenv("TIKOMNI_AUTHOR_ANALYSIS_TIMEOUT_SEC", str(DEFAULT_ANALYSIS_TIMEOUT_SEC))), 5)
    small_sample_skip_threshold = max(int(os.getenv("TIKOMNI_AUTHOR_ANALYSIS_SMALL_SAMPLE_SKIP", str(DEFAULT_SMALL_SAMPLE_SKIP_THRESHOLD))), 0)
    trace: List[Dict[str, Any]] = [
        {
            "step": "analysis.input_built",
            "input_object": "author_analysis_input_v1",
            "total_works": total_works,
            "sampled_works_count": sampled_works_count,
            "prompt_contract": f"prompt-contracts/{AUTHOR_ANALYSIS_PROMPT_FILE}@v1",
            "llm_timeout_sec": llm_timeout_sec,
            "small_sample_skip_threshold": small_sample_skip_threshold,
        }
    ] + sampled_explanation_trace
    if input_errors:
        trace.append({"step": "analysis.input_validation_failed", "error_count": len(input_errors)})
    if sampled_explanation_errors:
        trace.append({"step": "analysis.sampled_work_explanations_validation_failed", "error_count": len(sampled_explanation_errors)})

    prompt = _build_prompt(analysis_input, sampled_work_explanations)
    response_text = ""
    analysis_v2: Dict[str, Any] = {}
    llm_ok = False
    skip_llm = sampled_works_count < small_sample_skip_threshold
    if skip_llm:
        trace.append(
            {
                "step": "analysis.llm_skipped",
                "reason": "small_sample_below_threshold",
                "sampled_works_count": sampled_works_count,
                "threshold": small_sample_skip_threshold,
            }
        )
    else:
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
            raw_analysis = _extract_json_block(response_text)
            analysis_v2 = _unwrap_author_analysis(raw_analysis)
            llm_ok = bool(analysis_v2)
            trace.append(
                {
                    "step": "analysis.llm_called",
                    "returncode": run.returncode,
                    "has_text": bool(response_text),
                    "parsed": llm_ok,
                    "stdout_chars": len(run.stdout or ""),
                    "stderr_chars": len(run.stderr or ""),
                }
            )
        except Exception as error:
            trace.append({"step": "analysis.llm_error", "error": f"{type(error).__name__}:{error}"})

    validation_errors = validate_author_analysis_v2(analysis_v2, analysis_input=analysis_input) if analysis_v2 else []
    if not analysis_v2 or validation_errors:
        fallback = build_fallback_author_analysis_v2(analysis_input)
        fallback_errors = validate_author_analysis_v2(fallback, analysis_input=analysis_input)
        trace.append(
            {
                "step": "analysis.fallback_used",
                "reason": "llm_empty_or_validation_failed",
                "llm_ok": llm_ok,
                "validation_error_count": len(validation_errors),
                "fallback_error_count": len(fallback_errors),
            }
        )
        analysis_v2 = fallback
        validation_errors = input_errors + sampled_explanation_errors + validation_errors + fallback_errors
    else:
        validation_errors = input_errors + sampled_explanation_errors + validation_errors
        trace.append({"step": "analysis.schema_validation_passed"})

    legacy = derive_legacy_summary(analysis_v2, analysis_input=analysis_input, validation_errors=validation_errors)
    result = {
        **legacy,
        "author_analysis_v2": analysis_v2,
        "author_analysis_input_v1": analysis_input,
        "sampled_work_explanations": sampled_work_explanations,
        "validation": {
            "ok": not bool(validation_errors),
            "errors": validation_errors,
        },
    }
    return result, validation_errors, trace
