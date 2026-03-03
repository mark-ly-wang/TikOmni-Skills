#!/usr/bin/env python3
"""Shared analysis pipeline helpers for benchmark card generation."""

import json
import os
import re
import subprocess
from typing import Any, Dict, List, Optional

PROMPT_CONTRACT_FILES: Dict[str, str] = {
    "选题": "topic.md",
    "文风": "style.md",
    "Hook": "hook.md",
    "结构": "structure.md",
    "洞察分析": "insight.md",
    "CTA": "cta.md",
    "总结": "summary.md",
}

DEFAULT_MODULE_SECTIONS: List[str] = ["选题", "文风", "Hook", "结构"]
DEFAULT_INSIGHT_SECTION = "洞察分析"


def contracts_dir() -> str:
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.normpath(os.path.join(here, "..", "references", "prompt-contracts"))


def load_contract_prompt(filename: str) -> str:
    path = os.path.join(contracts_dir(), filename)
    try:
        with open(path, "r", encoding="utf-8") as handle:
            content = handle.read()
    except Exception:
        return ""

    match = re.search(r"##\s*User Prompt \(Verbatim\).*?```text\n(.*?)\n```", content, flags=re.S)
    if match:
        return match.group(1).strip()
    return content.strip()


def _analysis_payload(fields: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "title": fields.get("title"),
        "asr_clean": fields.get("asr_clean"),
        "asr_raw": fields.get("raw_content"),
        "metrics": {
            "digg_count": fields.get("digg_count"),
            "comment_count": fields.get("comment_count"),
            "collect_count": fields.get("collect_count"),
            "share_count": fields.get("share_count"),
            "play_count": fields.get("play_count"),
        },
    }


def call_prompt_llm(section: str, prompt_text: str, fields: Dict[str, Any], timeout_sec: int = 240) -> str:
    if not prompt_text:
        return "数据不足"

    message = (
        f"请严格根据下面提示词原文完成【{section}】段落输出。\n"
        "要求：\n"
        "1) 不要解释提示词，不要输出思考过程。\n"
        "2) 不要套额外模板，不要输出打分。\n"
        "3) 仅输出该段正文内容。\n\n"
        "=== 提示词原文开始 ===\n"
        f"{prompt_text}\n"
        "=== 提示词原文结束 ===\n\n"
        "=== 输入数据(JSON) ===\n"
        f"{json.dumps(_analysis_payload(fields), ensure_ascii=False)}"
    )

    try:
        run = subprocess.run(
            ["openclaw", "agent", "--agent", "main", "--message", message, "--json"],
            capture_output=True,
            text=True,
            timeout=timeout_sec,
            check=False,
        )
        data = json.loads(run.stdout or "{}")
        texts: List[str] = []
        for payload in data.get("result", {}).get("payloads", []):
            text = payload.get("text") if isinstance(payload, dict) else None
            if isinstance(text, str) and text.strip():
                texts.append(text.strip())
        if texts:
            return "\n".join(texts).strip()
    except Exception:
        pass

    return "数据不足"


def build_module_lines(
    fields: Dict[str, Any],
    sections: Optional[List[str]] = None,
    contract_files: Optional[Dict[str, str]] = None,
) -> Dict[str, List[str]]:
    picked_sections = sections or DEFAULT_MODULE_SECTIONS
    mapping = contract_files or PROMPT_CONTRACT_FILES
    outputs: Dict[str, List[str]] = {}

    for section in picked_sections:
        prompt_text = load_contract_prompt(mapping.get(section, ""))
        content = call_prompt_llm(section, prompt_text, fields)
        outputs[section] = [content if content else "数据不足"]

    return outputs


def build_single_section_lines(
    fields: Dict[str, Any],
    section: str = DEFAULT_INSIGHT_SECTION,
    contract_files: Optional[Dict[str, str]] = None,
) -> List[str]:
    mapping = contract_files or PROMPT_CONTRACT_FILES
    prompt_text = load_contract_prompt(mapping.get(section, ""))
    content = call_prompt_llm(section, prompt_text, fields)
    return [content if content else "数据不足"]


def build_analysis_sections(fields: Dict[str, Any]) -> Dict[str, Any]:
    """Build prompt-contract-driven analysis sections for benchmark cards."""
    modules = build_module_lines(fields)
    insight = build_single_section_lines(fields, section=DEFAULT_INSIGHT_SECTION)
    return {
        "modules": modules,
        "insight": insight,
    }
