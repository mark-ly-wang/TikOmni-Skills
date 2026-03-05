#!/usr/bin/env python3
"""Prompt-first analyzers for author-home insights."""

from __future__ import annotations

import json
import re
import subprocess
from typing import Any, Dict, List, Tuple


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


def _build_prompt(profile: Dict[str, Any], works: List[Dict[str, Any]]) -> str:
    compact_works = [
        {
            "id": item.get("platform_work_id"),
            "title": item.get("title"),
            "desc": item.get("desc"),
            "metrics": item.get("metrics"),
            "tags": item.get("tags"),
        }
        for item in works[:30]
    ]
    return (
        "你是内容商业分析师。请基于作者主页样本，输出严格 JSON（不要 markdown，不要解释）。\n"
        "字段必须完整，类型必须正确：\n"
        "{\n"
        '  "author_portrait": "string",\n'
        '  "business_analysis": "string",\n'
        '  "benchmark_analysis": "string",\n'
        '  "business_score": 0,\n'
        '  "benchmark_gap_score": 0,\n'
        '  "style_radar": {"选题":0,"表达":0,"结构":0,"节奏":0,"人设":0,"转化":0,"差异化":0,"稳定性":0},\n'
        '  "core_contradictions": ["string"],\n'
        '  "recommendations": ["string"]\n'
        "}\n"
        "评分范围 0-100；文本请中文简洁。\n"
        f"作者画像输入: {json.dumps(profile, ensure_ascii=False)}\n"
        f"作品样本输入(最多30条): {json.dumps(compact_works, ensure_ascii=False)}\n"
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
    trace: List[Dict[str, Any]] = [{"step": "analysis.prompt_built", "works_used": min(len(works), 30)}]

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
        return fallback, schema_errors, trace

    return analysis, [], trace
