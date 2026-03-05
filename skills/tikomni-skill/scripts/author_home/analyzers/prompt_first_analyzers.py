#!/usr/bin/env python3
"""Prompt-first analyzers for author-home insights."""

from __future__ import annotations

import json
import re
import subprocess
from typing import Any, Dict, List, Tuple

from scripts.core.analysis_pipeline import load_contract_prompt


REQUIRED_ANALYSIS_KEYS = {
    "author_portrait": str,
    "business_analysis": str,
    "benchmark_analysis": str,
    "business_score": int,
    "benchmark_gap_score": int,
    "style_radar": dict,
    "core_contradictions": list,
    "recommendations": list,
}

AUTHOR_ANALYSIS_PROMPT_FILE = "author-analysis.md"


def _build_works_input(works: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    compact: List[Dict[str, Any]] = []
    for item in works[:30]:
        if not isinstance(item, dict):
            continue
        compact.append(
            {
                "id": item.get("platform_work_id"),
                "title": item.get("title"),
                "desc": item.get("desc"),
                "asr_clean": item.get("asr_clean"),
                "asr_source": item.get("asr_source"),
                "metrics": item.get("metrics"),
                "tags": item.get("tags"),
                "content_type": item.get("content_type"),
            }
        )
    return compact


def _build_prompt(profile: Dict[str, Any], works: List[Dict[str, Any]]) -> str:
    contract_prompt = load_contract_prompt(AUTHOR_ANALYSIS_PROMPT_FILE)
    payload = {
        "author_profile": profile,
        "works": _build_works_input(works),
    }
    return (
        "请严格根据以下提示词原文输出，结果必须是 JSON 对象，且只输出 JSON。\n"
        "不得输出 markdown，不得输出解释。\n\n"
        "=== 提示词原文开始 ===\n"
        f"{contract_prompt}\n"
        "=== 提示词原文结束 ===\n\n"
        "=== 输入数据(JSON) ===\n"
        f"{json.dumps(payload, ensure_ascii=False)}"
    )


def _extract_json_block(text: str) -> Dict[str, Any]:
    content = (text or "").strip()
    if not content:
        return {}
    try:
        return json.loads(content)
    except Exception:
        pass

    match = re.search(r"\{[\s\S]*\}", content)
    if not match:
        return {}
    try:
        return json.loads(match.group(0))
    except Exception:
        return {}


def _validate_min_schema(payload: Dict[str, Any]) -> List[Dict[str, str]]:
    errors: List[Dict[str, str]] = []
    for key, expected in REQUIRED_ANALYSIS_KEYS.items():
        if key not in payload:
            errors.append({"field": key, "reason": "missing"})
            continue
        value = payload.get(key)
        if expected is int and not isinstance(value, int):
            errors.append({"field": key, "reason": "type_error:int"})
        elif expected is str and not isinstance(value, str):
            errors.append({"field": key, "reason": "type_error:str"})
        elif expected is list and not isinstance(value, list):
            errors.append({"field": key, "reason": "type_error:list"})
        elif expected is dict and not isinstance(value, dict):
            errors.append({"field": key, "reason": "type_error:dict"})

    if isinstance(payload.get("style_radar"), dict):
        for required in ("选题", "表达", "结构", "节奏", "人设", "转化", "差异化", "稳定性"):
            if required not in payload["style_radar"]:
                errors.append({"field": f"style_radar.{required}", "reason": "missing"})

    return errors


def _fallback_analysis() -> Dict[str, Any]:
    return {
        "author_portrait": "样本不足，先给到基础画像：内容方向稳定，但需要更明确人设与差异化标签。",
        "business_analysis": "商业化链路需要补强 CTA 与产品承接，优先建立明确转化动作。",
        "benchmark_analysis": "与头部账号相比，内容结构和转化设计仍有提升空间。",
        "business_score": 60,
        "benchmark_gap_score": 55,
        "style_radar": {"选题": 65, "表达": 62, "结构": 58, "节奏": 57, "人设": 56, "转化": 52, "差异化": 54, "稳定性": 63},
        "core_contradictions": ["内容质量在提升，但转化动作不稳定", "账号定位有方向，但差异化标签不够尖锐"],
        "recommendations": ["优先统一选题母题与人设口径", "每条作品固定一个可执行 CTA", "按周复盘高表现作品并固化模板"],
    }


def run_prompt_first_author_analysis(profile: Dict[str, Any], works: List[Dict[str, Any]]) -> Tuple[Dict[str, Any], List[Dict[str, str]], List[Dict[str, Any]]]:
    prompt = _build_prompt(profile, works)
    trace: List[Dict[str, Any]] = [
        {
            "step": "analysis.prompt_built",
            "works_used": min(len(works), 30),
            "prompt_contract": f"prompt-contracts/{AUTHOR_ANALYSIS_PROMPT_FILE}@v1",
        }
    ]

    response_text = ""
    try:
        run = subprocess.run(
            ["openclaw", "agent", "--agent", "main", "--message", prompt, "--json"],
            capture_output=True,
            text=True,
            timeout=240,
            check=False,
        )
        parsed = json.loads(run.stdout or "{}")
        chunks: List[str] = []
        for item in parsed.get("result", {}).get("payloads", []):
            if isinstance(item, dict) and isinstance(item.get("text"), str):
                chunks.append(item["text"])
        response_text = "\n".join(chunks).strip()
        trace.append({"step": "analysis.llm_called", "returncode": run.returncode, "has_text": bool(response_text)})
    except Exception as error:
        trace.append({"step": "analysis.llm_error", "error": f"{type(error).__name__}:{error}"})

    analysis = _extract_json_block(response_text)
    schema_errors = _validate_min_schema(analysis)
    if schema_errors:
        fallback = _fallback_analysis()
        fallback["schema_validation_failed"] = True
        trace.append({"step": "analysis.schema_validation_failed", "error_count": len(schema_errors)})
        return fallback, schema_errors, trace

    trace.append({"step": "analysis.schema_validation_passed"})
    return analysis, [], trace
