#!/usr/bin/env python3
"""Shared analysis helpers for single-work benchmark card generation."""

from __future__ import annotations

import json
import os
import re
import time
from typing import Any, Dict, List, Optional

from scripts.core.analysis_adapter import (
    resolve_analysis_timeout,
    resolve_preferred_provider,
    run_structured_analysis,
)
from scripts.core.progress_report import ProgressReporter
from scripts.core.tikomni_common import normalize_text


ANALYSIS_PROMPT_FILE = "analysis-bundle.md"
DEFAULT_MODULE_SECTIONS: List[str] = ["选题", "文风", "Hook", "结构"]
DEFAULT_INSIGHT_SECTION = "洞察分析"
SECTION_FIELD_MAP = {
    "选题": "topic",
    "文风": "style",
    "Hook": "hook",
    "结构": "structure",
}


def contracts_dir() -> str:
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.normpath(os.path.join(here, "..", "..", "references", "prompt-contracts"))


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


def _normalize_lines(value: Any) -> List[str]:
    if isinstance(value, list):
        return [normalize_text(item) for item in value if normalize_text(item)]
    text = normalize_text(value)
    return [text] if text else []


def _safe_int(value: Any, default: int = 0) -> int:
    if value is None:
        return default
    if isinstance(value, bool):
        return int(value)
    if isinstance(value, int):
        return value
    if isinstance(value, float):
        return int(value)
    text = str(value).strip()
    if not text:
        return default
    try:
        return int(float(text))
    except Exception:
        return default


def _sentence_units(text: str) -> List[str]:
    return [normalize_text(part) for part in re.split(r"[。！？!?；;\n]+", normalize_text(text)) if normalize_text(part)]


def _first_sentence(text: str) -> str:
    units = _sentence_units(text)
    return units[0] if units else ""


def _hit_count(text: str, keywords: List[str]) -> int:
    base = normalize_text(text)
    if not base:
        return 0
    return sum(1 for token in keywords if token in base)


def _top_keywords(text: str, candidates: List[str], topn: int = 3) -> List[str]:
    base = normalize_text(text)
    if not base:
        return []
    scored = []
    for token in candidates:
        count = base.count(token)
        if count > 0:
            scored.append((count, token))
    scored.sort(key=lambda item: (-item[0], len(item[1])))
    return [token for _, token in scored[:topn]]


def _score_from_hits(hits: int, full_score_hits: int = 4) -> int:
    if hits <= 0:
        return 2
    if hits >= full_score_hits:
        return 5
    return min(5, hits + 2)


def _analysis_payload(fields: Dict[str, Any]) -> Dict[str, Any]:
    asr_raw = normalize_text(fields.get("asr_raw") or fields.get("raw_content"))
    return {
        "platform": normalize_text(fields.get("platform")),
        "title": normalize_text(fields.get("title")),
        "caption_raw": normalize_text(fields.get("caption_raw")),
        "asr_raw": asr_raw,
        "asr_clean": normalize_text(fields.get("asr_clean")) or asr_raw,
        "work_modality": normalize_text(fields.get("work_modality")),
        "tags": fields.get("tags") if isinstance(fields.get("tags"), list) else [],
        "metrics": {
            "digg_count": fields.get("digg_count"),
            "comment_count": fields.get("comment_count"),
            "collect_count": fields.get("collect_count"),
            "share_count": fields.get("share_count"),
            "play_count": fields.get("play_count"),
        },
    }


def _analyze_topic(fields: Dict[str, Any]) -> Dict[str, Any]:
    title = normalize_text(fields.get("title"))
    asr = normalize_text(fields.get("asr_clean"))
    category = normalize_text(fields.get("category"))
    text = f"{title} {asr}".strip()
    if not text:
        return {
            "lines": ["- 类型：数据不足。", "- 细分主题：数据不足。", "- 受众痛点：数据不足。"],
        }

    type_rules = {
        "流量型": ["热点", "挑战", "反转", "揭秘", "真相", "别再", "为什么", "踩坑"],
        "人设型": ["我是", "我们", "日常", "分享", "经历", "成长", "复盘", "带你"],
        "营销型": ["领取", "私信", "咨询", "下单", "课程", "优惠", "报名", "合作"],
    }
    type_scores = {name: _hit_count(text, rules) for name, rules in type_rules.items()}
    if category in {"教程", "知识", "方法"}:
        type_scores["营销型"] += 1
    if category in {"观点", "人设", "日常"}:
        type_scores["人设型"] += 1

    main_type = max(type_scores, key=lambda key: type_scores[key])
    themes = _top_keywords(
        text,
        ["AI", "智能体", "变现", "副业", "教程", "工作流", "流量", "涨粉", "口播", "创业", "营销"],
        topn=3,
    )
    pains = _top_keywords(text, ["不会", "焦虑", "卡住", "没流量", "转化", "时间不够", "风险"], topn=2)
    return {
        "lines": [
            f"- 基础类型：{main_type}（命中信号 {type_scores[main_type]} 个）。",
            f"- 细分主题：{'、'.join(themes) if themes else '数据不足'}。",
            f"- 受众痛点：{'、'.join(pains) if pains else '以快速落地/降低门槛为主'}。",
        ],
    }


def _analyze_style(fields: Dict[str, Any]) -> Dict[str, Any]:
    asr = normalize_text(fields.get("asr_clean"))
    title = normalize_text(fields.get("title"))
    text = f"{title} {asr}".strip()
    units = _sentence_units(asr)
    if not text:
        return {
            "lines": ["- 句式结构：数据不足。", "- 语气分布：数据不足。", "- 人设与修辞：数据不足。"],
        }

    avg_len = int(sum(len(unit) for unit in units) / max(1, len(units))) if units else 0
    if avg_len <= 14:
        length_type = "短句为主"
    elif avg_len <= 24:
        length_type = "中短句混合"
    else:
        length_type = "中长句为主"
    q_count = text.count("?") + text.count("？")
    e_count = text.count("!") + text.count("！")
    statement_count = max(0, len(units) - q_count - e_count)
    persona_hits = _hit_count(text, ["我", "我们", "你", "大家", "朋友们"])
    rhetoric_hits = _hit_count(text, ["不是", "而是", "其实", "真的", "一定", "必须", "先", "再"])
    return {
        "lines": [
            f"- 句式结构：{length_type}，平均句长约 {avg_len} 字。",
            f"- 语气分布：疑问 {q_count} / 感叹 {e_count} / 陈述 {statement_count}。",
            f"- 人设与修辞：人设代词命中 {persona_hits} 次，强调/转折词命中 {rhetoric_hits} 次。",
        ],
    }


def _analyze_hook(fields: Dict[str, Any]) -> Dict[str, Any]:
    title = normalize_text(fields.get("title"))
    asr = normalize_text(fields.get("asr_clean"))
    units = _sentence_units(asr)
    first = _first_sentence(asr) or title
    middle = units[len(units) // 2] if units else ""
    if not first:
        return {
            "lines": ["- 开头钩子：数据不足。", "- 中段钩子：数据不足。", "- 结尾钩子：数据不足。"],
        }

    hook_type = "陈述式"
    if any(token in first for token in ["?", "？", "为什么", "怎么"]):
        hook_type = "疑问式"
    elif any(token in first for token in ["别再", "误区", "真相", "不是"]):
        hook_type = "反常识式"
    elif any(token in first for token in ["当你", "如果", "今天"]):
        hook_type = "场景代入式"
    end_candidates = [
        unit for unit in units if _hit_count(unit, ["关注", "评论", "私信", "收藏", "转发", "领取"]) > 0
    ]
    end = end_candidates[-1] if end_candidates else "未检测到明确结尾钩子"
    return {
        "lines": [
            f"- 开头钩子（{hook_type}）：{first}",
            f"- 中段钩子：{middle or '数据不足'}",
            f"- 结尾钩子：{end}",
        ],
    }


def _analyze_structure(fields: Dict[str, Any]) -> Dict[str, Any]:
    units = _sentence_units(fields.get("asr_clean"))
    if not units:
        return {
            "lines": ["- 结构标签：数据不足。", "- 模板判定：数据不足。", "- 缺失模块：数据不足。"],
        }

    label_rules = {
        "钩子": ["?", "？", "为什么", "怎么", "别再", "真相", "当你", "如果"],
        "冲突": ["但是", "却", "问题", "误区", "卡住", "焦虑", "失败"],
        "转折": ["所以", "于是", "然后", "接着", "这时候", "其实"],
        "举证": ["数据", "案例", "比如", "步骤", "第一", "第二", "第三"],
        "CTA": ["评论", "关注", "私信", "收藏", "转发", "领取"],
    }
    coverage = {label: 0 for label in label_rules}
    for sentence in units:
        for label, keywords in label_rules.items():
            if any(keyword in sentence for keyword in keywords):
                coverage[label] += 1

    present = [label for label, count in coverage.items() if count > 0]
    missing = [label for label, count in coverage.items() if count == 0]
    template = "钩子→冲突→转折→举证→CTA" if len(present) >= 4 else "钩子→观点→补充说明"
    return {
        "lines": [
            f"- 结构标签覆盖：{', '.join([f'{label}:{count}' for label, count in coverage.items()])}。",
            f"- 模板判定：{template}。",
            f"- 缺失模块：{'、'.join(missing) if missing else '无'}。",
        ],
    }


def _insight_metric_snapshot(fields: Dict[str, Any]) -> Dict[str, Any]:
    digg = _safe_int(fields.get("digg_count"), default=0)
    comment = _safe_int(fields.get("comment_count"), default=0)
    collect = _safe_int(fields.get("collect_count"), default=0)
    share = _safe_int(fields.get("share_count"), default=0)
    play = _safe_int(fields.get("play_count"), default=0)
    interaction = digg + comment * 2 + collect * 3 + share * 4
    interaction_rate = interaction / play if play > 0 else 0.0
    return {
        "interaction": interaction,
        "interaction_rate": interaction_rate,
    }


def _build_local_sections(fields: Dict[str, Any]) -> Dict[str, Any]:
    topic = _analyze_topic(fields)
    style = _analyze_style(fields)
    hook = _analyze_hook(fields)
    structure = _analyze_structure(fields)
    metrics = _insight_metric_snapshot(fields)

    strongest_signals = []
    for section_name, section_payload in {
        "选题": topic,
        "文风": style,
        "Hook": hook,
        "结构": structure,
    }.items():
        first_line = _normalize_lines(section_payload.get("lines"))
        if first_line:
            strongest_signals.append(f"- {section_name}：{first_line[0].lstrip('- ').strip()}")

    insight = strongest_signals[:3]
    insight.extend(
        [
            f"- 互动折算值：{metrics.get('interaction', 0)}。",
            f"- 粗略互动率：{metrics.get('interaction_rate', 0.0):.4f}。",
        ]
    )

    return {
        "modules": {
            "选题": _normalize_lines(topic.get("lines")) or ["数据不足"],
            "文风": _normalize_lines(style.get("lines")) or ["数据不足"],
            "Hook": _normalize_lines(hook.get("lines")) or ["数据不足"],
            "结构": _normalize_lines(structure.get("lines")) or ["数据不足"],
        },
        "insight": insight or ["数据不足"],
    }


def _normalize_llm_sections(payload: Dict[str, Any]) -> Dict[str, Any]:
    modules: Dict[str, List[str]] = {}
    for section_name, field_name in SECTION_FIELD_MAP.items():
        lines = _normalize_lines(payload.get(field_name))
        modules[section_name] = lines or ["数据不足"]
    insight = _normalize_lines(payload.get("insight")) or ["数据不足"]
    return {
        "modules": modules,
        "insight": insight,
    }


def _analysis_status_from_reason(reason: str) -> str:
    if not reason:
        return "completed"
    if "timeout" in reason:
        return "timeout"
    if "unavailable" in reason:
        return "unavailable"
    if reason == "analysis_mode_local":
        return "skipped"
    return "failed"


def ensure_analysis_sections_schema(
    payload: Optional[Dict[str, Any]],
    *,
    provider: str = "local",
    llm_used: bool = False,
    degraded: bool = False,
    reason: str = "",
    duration_ms: int = 0,
) -> Dict[str, Any]:
    source = payload if isinstance(payload, dict) else {}
    modules_raw = source.get("modules") if isinstance(source.get("modules"), dict) else {}
    modules = {
        section: _normalize_lines(modules_raw.get(section)) or ["数据不足"]
        for section in DEFAULT_MODULE_SECTIONS
    }
    insight = _normalize_lines(source.get("insight")) or ["数据不足"]
    return {
        "version": "v2",
        "provider": provider,
        "modules": modules,
        "insight": insight,
        "meta": {
            "llm_used": bool(llm_used),
            "degraded": bool(degraded),
            "reason": normalize_text(reason),
            "duration_ms": max(0, int(duration_ms or 0)),
        },
    }


def build_analysis_sections(
    fields: Dict[str, Any],
    *,
    analysis_mode: str = "auto",
    analysis_config: Optional[Dict[str, Any]] = None,
    progress: Optional[ProgressReporter] = None,
) -> Dict[str, Any]:
    mode = str(analysis_mode or "auto").strip().lower()
    if mode not in {"auto", "local"}:
        mode = "auto"

    local_sections = _build_local_sections(fields)
    start_at = time.perf_counter()
    if not normalize_text(fields.get("title")) and not normalize_text(fields.get("asr_clean")):
        duration_ms = int((time.perf_counter() - start_at) * 1000)
        return ensure_analysis_sections_schema(
            local_sections,
            provider="local",
            llm_used=False,
            degraded=True,
            reason="analysis_input_missing",
            duration_ms=duration_ms,
        )

    if mode == "local":
        duration_ms = int((time.perf_counter() - start_at) * 1000)
        return ensure_analysis_sections_schema(
            local_sections,
            provider="local",
            llm_used=False,
            degraded=False,
            reason="analysis_mode_local",
            duration_ms=duration_ms,
        )

    prompt_text = load_contract_prompt(ANALYSIS_PROMPT_FILE)
    provider_preference = resolve_preferred_provider(analysis_config)
    if provider_preference == "local":
        duration_ms = int((time.perf_counter() - start_at) * 1000)
        return ensure_analysis_sections_schema(
            local_sections,
            provider="local",
            llm_used=False,
            degraded=False,
            reason="analysis_mode_local",
            duration_ms=duration_ms,
        )
    timeout_sec = resolve_analysis_timeout(analysis_config)
    llm_result = run_structured_analysis(
        prompt_text=prompt_text,
        payload=_analysis_payload(fields),
        provider=provider_preference,
        timeout_sec=timeout_sec,
        progress=progress.child(scope="analysis.host") if progress is not None else None,
    )

    if llm_result.get("ok"):
        normalized = _normalize_llm_sections(llm_result.get("structured", {}))
        duration_ms = int(llm_result.get("duration_ms") or 0)
        return ensure_analysis_sections_schema(
            normalized,
            provider=str(llm_result.get("provider") or "openclaw"),
            llm_used=True,
            degraded=False,
            reason="",
            duration_ms=duration_ms,
        )

    duration_ms = int(llm_result.get("duration_ms") or int((time.perf_counter() - start_at) * 1000))
    fallback_reason = normalize_text(llm_result.get("error_reason")) or "analysis_provider_unavailable"
    if progress is not None:
        progress.failed(
            stage="analysis.fallback",
            message="structured analysis degraded to local rules",
            data={
                "provider": llm_result.get("provider"),
                "error_reason": fallback_reason,
                "duration_ms": duration_ms,
            },
        )
    return ensure_analysis_sections_schema(
        local_sections,
        provider="local",
        llm_used=False,
        degraded=True,
        reason=fallback_reason,
        duration_ms=duration_ms,
    )
