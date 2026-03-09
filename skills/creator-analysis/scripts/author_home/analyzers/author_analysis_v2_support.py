#!/usr/bin/env python3
"""Support helpers for author_home v2 standardized input / aggregate stats / validation."""

from __future__ import annotations

import json
import math
import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Tuple

import jsonschema

SKILL_ROOT = Path(__file__).resolve().parents[3]
INPUT_SCHEMA_PATH = SKILL_ROOT / "references" / "schemas" / "author-analysis-input-v1.schema.json"
OUTPUT_SCHEMA_PATH = SKILL_ROOT / "references" / "schemas" / "author-analysis-v2.schema.json"
PROMPT_CONTRACT_PATH = SKILL_ROOT / "references" / "prompt-contracts" / "author-analysis-v2.md"

LOW_HIGH_MID = {"low", "mid", "high"}
RELATIONSHIP_DISTANCE = {"near", "mid", "far"}
AUTHOR_TYPES = {
    "ai_content_growth", "benchmark_deconstruction", "workflow_automation", "tool_education", "business_cognition",
    "ip_growth", "industry_commentary", "case_breakdown", "efficiency_hacking", "creator_education",
}
PRIMARY_ROLES = {"coach", "operator", "researcher", "builder", "companion", "commentator", "teacher", "practitioner", "evangelist", "critic"}
TRUST_SOURCES = {"results", "experience", "case_studies", "systematized_method", "demonstration", "strong_judgment", "consistency", "authority_signal", "community_signal"}
PROBLEM_DEFINITION_STYLES = {"cognition_problem", "execution_problem", "model_problem", "stage_mismatch", "positioning_problem", "traffic_problem", "conversion_problem", "offer_problem", "capability_problem"}
REASONING_MODES = {"benchmark_reasoning", "concept_deconstruction", "contrast_reasoning", "case_induction", "result_backtracking", "anti_common_sense", "framework_building", "workflow_packaging", "data_validation"}
HOOK_TYPES_ENUM = {"result_hook", "curiosity_hook", "shortcut_hook", "pain_point_hook", "comparison_hook", "proof_hook"}
STRUCTURE_TYPES = {"hook_demo_result", "benchmark_then_clone", "problem_solution_cta", "proof_then_pitch"}
CTA_TYPES = {"comment_cta", "private_message_cta", "follow_cta", "collect_cta", "share_cta", "lead_magnet_cta", "weak_cta", "no_cta"}
CONTENT_FORMS = {"talking_head", "voiceover", "screen_recording", "slideshow", "mixed_edit", "live_clip", "interview_clip"}
STYLE_MARKERS_ENUM = {"rhetorical_question", "imperative_tone", "strong_assertion", "self_mockery", "quote_like_phrase", "emotional_wording"}
FUNNEL_ROLES = {"acquire_attention", "build_trust", "educate", "qualify", "convert", "upsell", "retain", "occupy_mindshare"}
LIKELY_PRODUCTS = {"workflow_templates", "prompt_pack", "training_camp", "community", "consulting", "done_for_you_service", "course", "membership", "software_tool", "report"}
BUSINESS_MODEL_SIGNALS = {"high_ip_dependency", "strong_toolization", "template_scalability", "service_extension", "low_marginal_distribution", "high_touch_delivery", "community_leverage", "content_led_growth"}
CORE_COGNITIVE_ACTIONS = {"benchmark_deconstruction", "workflow_packaging", "concept_deconstruction", "contrast_reasoning", "case_induction", "framework_extraction", "result_compression", "anti_common_sense_reframing"}
TOPIC_SOURCES = {"benchmark_authors", "viral_cases", "audience_questions", "workflow_demos", "industry_pain_points", "personal_experience", "tool_updates", "client_cases", "market_signals"}
TOPIC_GOALS = {"acquire_attention", "build_trust", "show_capability", "drive_conversion", "occupy_mindshare", "differentiate_positioning", "nurture_audience"}
WINNING_CONTENT_STRUCTURES = set(STRUCTURE_TYPES)
MEMORABILITY_SOURCES = {"strong_keywords", "sharp_judgment", "identity_projection", "repeatable_phrases", "result_imagery", "emotional_contrast", "unexpected_framing"}
EMOTION_PATTERNS = {"calm_assertive", "sharp_direct", "playful_mocking", "high_energy_excitement", "pragmatic_cold", "empathetic_supportive", "provocative_challenge"}
TRAFFIC_DRIVERS = {"benchmark_target", "result_promise", "shortcut_imagination", "curiosity_gap", "identity_desire", "fear_of_missing_out", "proof_signal", "controversy_edge"}
STOPWORDS = {
    "我们", "你们", "他们", "这个", "那个", "一个", "一种", "已经", "如果", "因为", "所以", "然后", "就是", "没有", "自己",
    "可以", "还是", "需要", "以及", "并且", "真的", "今天", "现在", "内容", "作者", "账号", "作品", "视频", "老师", "方法",
    "the", "and", "for", "that", "with", "from", "this", "you", "your", "are", "was", "were", "have", "has", "had", "into",
}
SCHEMA_CACHE: Dict[Path, Dict[str, Any]] = {}


class AnalysisResourceError(RuntimeError):
    def __init__(self, *, code: str, path: Path, detail: str = "") -> None:
        self.code = code
        self.path = path
        self.detail = detail
        message = f"{code}:{path}"
        if detail:
            message = f"{message}:{detail}"
        super().__init__(message)

REQUIRED_V2_FIELDS = {
    "author_positioning": ["one_liner", "author_type", "primary_role", "target_audience", "core_problem_solved", "core_value_proposition", "evidence"],
    "trust_model": ["primary_trust_source", "secondary_trust_sources", "trust_building_mechanisms", "trust_risks", "relationship_posture", "evidence"],
    "cognitive_engine": ["worldview", "value_priority", "problem_definition_style", "reasoning_modes", "knowledge_sources", "judgment_style", "core_cognitive_actions", "evidence"],
    "expression_hooks": ["language_style", "hook_keywords", "hook_types", "argument_patterns", "emotion_patterns", "memorability_sources", "evidence"],
    "content_mechanism": ["topic_sources", "topic_goals", "winning_content_structures", "repeatable_series", "traffic_drivers", "content_flywheel", "cross_platform_variation", "dominant_themes", "theme_clusters", "evidence"],
    "commercial_bridge": ["content_role_in_funnel", "likely_products", "conversion_path", "content_product_fit", "business_model_signals", "commercial_risks", "evidence"],
    "core_tensions": ["tensions", "most_important_tension", "evidence"],
    "evidence_pack": ["sample_size", "sample_confidence", "representative_works", "top_keywords", "observed_hooks", "observed_ctas", "observed_structures", "notes"],
    "clone_guidance": ["copyable_elements", "non_copyable_elements", "borrowable_flavor", "danger_zones", "if_only_learn_one_thing"],
}


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


def _safe_float(value: Any, default: float = 0.0) -> float:
    try:
        if value is None:
            return default
        if isinstance(value, bool):
            return float(int(value))
        if isinstance(value, (int, float)):
            return float(value)
        text = _safe_text(value).replace(",", "")
        return float(text) if text else default
    except Exception:
        return default


def _clamp(value: float, low: float, high: float) -> float:
    return max(low, min(high, value))


def load_json_schema(path: Path) -> Dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as error:
        raise AnalysisResourceError(code="schema_load_failed", path=path, detail=f"{type(error).__name__}:{error}") from error


def prompt_contract_text() -> str:
    try:
        return PROMPT_CONTRACT_PATH.read_text(encoding="utf-8").strip()
    except Exception as error:
        raise AnalysisResourceError(code="contract_load_failed", path=PROMPT_CONTRACT_PATH, detail=f"{type(error).__name__}:{error}") from error


def _load_schema(path: Path) -> Dict[str, Any]:
    cached = SCHEMA_CACHE.get(path)
    if cached is not None:
        return cached
    schema = load_json_schema(path)
    SCHEMA_CACHE[path] = schema
    return schema


def _schema_errors(payload: Any, path: Path) -> List[Dict[str, str]]:
    schema = _load_schema(path)
    if not schema:
        raise AnalysisResourceError(code="schema_empty", path=path)
    try:
        validator = jsonschema.Draft202012Validator(schema)
        rows: List[Dict[str, str]] = []
        for error in sorted(validator.iter_errors(payload), key=lambda item: list(item.absolute_path)):
            field = ".".join(str(part) for part in error.absolute_path) or "$"
            rows.append({"field": field, "reason": f"schema:{error.message}"})
        return rows
    except Exception as error:
        return [{"field": "$", "reason": f"schema_runtime:{type(error).__name__}:{error}"}]


def _dedupe_keep_order(values: Sequence[str]) -> List[str]:
    result: List[str] = []
    seen = set()
    for value in values:
        clean = _safe_text(value)
        if not clean or clean in seen:
            continue
        seen.add(clean)
        result.append(clean)
    return result


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
    return _dedupe_keep_order(result)


def _dedupe_error_list(errors: Sequence[Dict[str, str]]) -> List[Dict[str, str]]:
    result: List[Dict[str, str]] = []
    seen = set()
    for item in errors:
        field = _safe_text(item.get("field"))
        reason = _safe_text(item.get("reason"))
        key = (field, reason)
        if key in seen:
            continue
        seen.add(key)
        result.append({"field": field, "reason": reason})
    return result


def _parse_datetime(value: Any) -> Optional[datetime]:
    if value is None:
        return None
    if isinstance(value, datetime):
        return value if value.tzinfo else value.replace(tzinfo=timezone.utc)
    num = _safe_int(value, default=0)
    if num > 0:
        if num > 1_000_000_000_000:
            num //= 1000
        try:
            return datetime.fromtimestamp(num, tz=timezone.utc)
        except Exception:
            return None
    text = _safe_text(value)
    if not text:
        return None
    for candidate in (text, text.replace("Z", "+00:00")):
        try:
            parsed = datetime.fromisoformat(candidate)
            return parsed if parsed.tzinfo else parsed.replace(tzinfo=timezone.utc)
        except Exception:
            continue
    for fmt in ("%Y-%m-%d %H:%M:%S", "%Y-%m-%d", "%Y/%m/%d %H:%M:%S", "%Y/%m/%d"):
        try:
            return datetime.strptime(text, fmt).replace(tzinfo=timezone.utc)
        except Exception:
            continue
    return None


def _publish_days_ago(value: Any) -> Optional[int]:
    parsed = _parse_datetime(value)
    if parsed is None:
        return None
    return max(int((datetime.now(timezone.utc) - parsed).total_seconds() // 86400), 0)


def _first_sentence(text: str) -> str:
    if not text:
        return ""
    units = [part.strip() for part in re.split(r"[。！？!?\n]+", text) if part.strip()]
    return units[0] if units else text[:80]


def _unique_tokens(text: str) -> List[str]:
    if not text:
        return []
    lowered = text.lower()
    tokens: List[str] = []
    for token in re.findall(r"[a-z0-9_]{3,24}", lowered):
        if token not in STOPWORDS:
            tokens.append(token)
    for block in re.findall(r"[\u4e00-\u9fff]{2,8}", text):
        if block not in STOPWORDS:
            tokens.append(block)
    return _dedupe_keep_order(tokens)


def _top_counter(counter: Counter, *, limit: int = 10) -> List[Dict[str, Any]]:
    total = sum(counter.values())
    rows: List[Dict[str, Any]] = []
    for key, count in counter.most_common(limit):
        rows.append({"value": key, "count": int(count), "ratio": round((count / total), 4) if total else 0.0})
    return rows


def _distribution_from_values(values: Sequence[str], *, limit: int = 10) -> Dict[str, Any]:
    counter = Counter(_safe_text(value) for value in values if _safe_text(value))
    return {"total": int(sum(counter.values())), "items": _top_counter(counter, limit=limit)}


def _merged_text(work: Dict[str, Any]) -> str:
    parts = [
        _safe_text(work.get("title")),
        _safe_text(work.get("caption_raw") or work.get("desc")),
        _safe_text(work.get("primary_text") or work.get("asr_clean") or work.get("asr_raw")),
    ]
    return "\n".join(part for part in parts if part)


def _performance_metrics(work: Dict[str, Any]) -> Tuple[int, int, int, int, int]:
    metrics = work.get("metrics") if isinstance(work.get("metrics"), dict) else {}
    return (
        _safe_int(work.get("digg_count"), _safe_int(metrics.get("like"), 0)),
        _safe_int(work.get("comment_count"), _safe_int(metrics.get("comment"), 0)),
        _safe_int(work.get("collect_count"), _safe_int(metrics.get("collect"), 0)),
        _safe_int(work.get("share_count"), _safe_int(metrics.get("share"), 0)),
        _safe_int(work.get("play_count"), _safe_int(metrics.get("play"), 0)),
    )


def _score_signals(texts: Sequence[Tuple[str, float]], mapping: Sequence[Tuple[str, Sequence[str]]], *, default: str) -> str:
    scores = {label: 0.0 for label, _ in mapping}
    for text, weight in texts:
        lowered = _safe_text(text).lower()
        if not lowered:
            continue
        for label, tokens in mapping:
            hit_count = sum(1 for token in tokens if token and token.lower() in lowered)
            if hit_count:
                scores[label] += weight * hit_count
    ranked = sorted(scores.items(), key=lambda item: (-item[1], item[0]))
    return ranked[0][0] if ranked and ranked[0][1] > 0 else default


def _pick_hook_type(text: str, existing: Any = None) -> str:
    clean = _safe_text(existing)
    if clean in HOOK_TYPES_ENUM:
        return clean
    first = _first_sentence(text)
    return _score_signals(
        [(first, 2.0), (text[:180], 1.0)],
        [
            ("result_hook", ["结果", "涨粉", "成交", "翻倍", "跑通", "案例结果"]),
            ("curiosity_hook", ["为什么", "怎么", "?", "？", "真相", "你知道吗"]),
            ("shortcut_hook", ["一键", "直接", "立刻", "马上", "不用", "三步", "复制"]),
            ("pain_point_hook", ["不会", "卡住", "焦虑", "没流量", "做不出来", "误区"]),
            ("comparison_hook", ["对比", "vs", "还是", "比", "A还是B"]),
            ("proof_hook", ["案例", "证明", "数据", "实测", "截图", "后台"]),
        ],
        default="curiosity_hook" if first else "result_hook",
    )


def _pick_structure_type(text: str, existing: Any = None) -> str:
    clean = _safe_text(existing)
    if clean in STRUCTURE_TYPES:
        return clean
    return _score_signals(
        [(text, 1.0)],
        [
            ("benchmark_then_clone", ["对标", "拆解", "复刻", "照着做", "临摹"]),
            ("problem_solution_cta", ["问题", "解决", "评论", "私信", "领取", "回复"]),
            ("proof_then_pitch", ["案例", "证明", "结果", "报名", "咨询", "私信"]),
            ("hook_demo_result", ["演示", "实操", "结果", "前后对比", "跑一遍"]),
        ],
        default="hook_demo_result",
    )


def _pick_cta_type(text: str, existing: Any = None) -> str:
    clean = _safe_text(existing)
    if clean in CTA_TYPES:
        return clean
    tail = "\n".join([line.strip() for line in _safe_text(text).splitlines()[-3:] if line.strip()])
    return _score_signals(
        [(tail, 2.0), (text, 0.8)],
        [
            ("comment_cta", ["评论", "留言", "扣1", "回复区"]),
            ("private_message_cta", ["私信", "加我", "vx", "微信", "主页联系"]),
            ("lead_magnet_cta", ["领取", "模板", "资料", "清单", "关键词"]),
            ("collect_cta", ["收藏", "存下", "保存"]),
            ("share_cta", ["转发", "分享给", "发给"]),
            ("follow_cta", ["关注", "下期见"]),
        ],
        default="no_cta",
    )


def _style_markers(text: str, existing: Any = None) -> List[str]:
    markers: List[str] = []
    if isinstance(existing, list):
        markers.extend([_safe_text(item) for item in existing if _safe_text(item) in STYLE_MARKERS_ENUM])
    lowered = _safe_text(text).lower()
    mapping = [
        ("rhetorical_question", ["为什么", "怎么", "?", "？"]),
        ("imperative_tone", ["一定", "必须", "直接", "马上", "立刻"]),
        ("strong_assertion", ["就是", "本质上", "根本", "一定要"]),
        ("self_mockery", ["我自己也踩过", "我之前也傻", "我也翻车", "我也被打脸"]),
        ("quote_like_phrase", ["‘", "’", "“", "”", "所谓", "一句话说"]),
        ("emotional_wording", ["焦虑", "崩溃", "爽", "绝了", "离谱", "炸裂"]),
    ]
    for label, tokens in mapping:
        if any(token.lower() in lowered for token in tokens):
            markers.append(label)
    return _dedupe_keep_order(markers)[:6]


def _pick_content_form(work: Dict[str, Any]) -> str:
    existing = _safe_text(work.get("content_form"))
    if existing in CONTENT_FORMS:
        return existing
    work_modality = _safe_text(work.get("work_modality")).lower()
    raw_text = _merged_text(work)
    if work_modality == "text":
        return "slideshow"
    if "screen" in raw_text.lower() or "录屏" in raw_text:
        return "screen_recording"
    if "采访" in raw_text or "对谈" in raw_text:
        return "interview_clip"
    if "直播" in raw_text:
        return "live_clip"
    return "talking_head" if work_modality == "video" else "voiceover"


def _normalize_work(profile: Dict[str, Any], work: Dict[str, Any]) -> Dict[str, Any]:
    digg, comment, collect, share, play = _performance_metrics(work)
    publish_time = work.get("publish_time") or work.get("create_time") or work.get("create_time_sec")
    publish_days_ago = _publish_days_ago(publish_time)
    performance_score = round(0.15 * digg + 0.20 * comment + 0.35 * collect + 0.30 * share, 4)
    norm_divisor = math.log((publish_days_ago or 0) + 2)
    performance_score_norm = round((performance_score / norm_divisor) if norm_divisor > 0 else performance_score, 4)
    title = _safe_text(work.get("title"))
    caption_raw = _safe_text(work.get("caption_raw") or work.get("desc"))
    primary_text = _safe_text(work.get("primary_text") or work.get("asr_clean") or work.get("asr_raw") or caption_raw)
    primary_text_source_raw = _safe_text(work.get("primary_text_source"))
    primary_text_source = (
        primary_text_source_raw
        if primary_text_source_raw in {"asr_clean", "caption_raw"}
        else ("asr_clean" if _safe_text(work.get("work_modality")) == "video" else "caption_raw")
    )
    work_modality = _safe_text(work.get("work_modality")) or ("video" if _safe_text(work.get("video_download_url") or work.get("video_down_url") or work.get("asr_raw")) else "text")
    merged = "\n".join(part for part in [title, caption_raw, primary_text] if part)
    return {
        "platform_work_id": _safe_text(work.get("platform_work_id")),
        "title": title,
        "caption_raw": caption_raw,
        "work_modality": work_modality,
        "primary_text": primary_text,
        "primary_text_source": primary_text_source,
        "published_date": _safe_text(work.get("published_date")) or "",
        "publish_time": publish_time,
        "publish_days_ago": publish_days_ago,
        "duration_ms": _safe_int(work.get("duration_ms"), 0),
        "digg_count": digg,
        "comment_count": comment,
        "collect_count": collect,
        "share_count": share,
        "play_count": play,
        "content_form": _pick_content_form(work),
        "tags": _safe_text_list(work.get("tags")),
        "author_id": _safe_text(profile.get("author_platform_id") or profile.get("platform_author_id")),
        "author_name": _safe_text(profile.get("nickname")) or "作者",
        "performance_score": performance_score,
        "performance_score_norm": performance_score_norm,
        "bucket": "",
        "hook_type": _pick_hook_type(merged, work.get("hook_type") or work.get("hook")),
        "structure_type": _pick_structure_type(merged, work.get("structure_type") or work.get("content_structure")),
        "cta_type": _pick_cta_type(merged, work.get("cta_type") or work.get("cta")),
        "style_markers": _style_markers(merged, work.get("style_markers") or work.get("style_tags")),
        "analysis_eligibility": _safe_text(work.get("analysis_eligibility")) or "eligible",
        "analysis_exclusion_reason": _safe_text(work.get("analysis_exclusion_reason")),
        "analysis_artifact_status": work.get("analysis_artifact_status"),
        "recent_30d_score_rank": None,
    }


def _assign_recent_30d_ranks(items: List[Dict[str, Any]]) -> None:
    recent = [item for item in items if _safe_int(item.get("publish_days_ago"), 999999) <= 30]
    ranked = sorted(recent, key=lambda item: (-_safe_float(item.get("performance_score_norm"), 0.0), _safe_text(item.get("platform_work_id"))))
    for idx, item in enumerate(ranked):
        item["recent_30d_score_rank"] = idx + 1
    recent_ids = {_safe_text(item.get("platform_work_id")) for item in ranked}
    for item in items:
        if _safe_text(item.get("platform_work_id")) not in recent_ids:
            item["recent_30d_score_rank"] = None


def _assign_buckets(items: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    total = len(items)
    ranked = sorted(items, key=lambda item: (-_safe_float(item.get("performance_score_norm"), 0.0), _safe_text(item.get("platform_work_id"))))
    for idx, item in enumerate(ranked):
        percentile = (idx + 1) / total if total else 1.0
        if total < 20:
            bucket = "Top" if idx < 4 else ("Strong" if idx < 8 else ("Mid" if idx < max(10, total - 2) else "Bottom"))
        elif percentile <= 0.20:
            bucket = "Top"
        elif percentile <= 0.50:
            bucket = "Strong"
        elif percentile <= 0.85:
            bucket = "Mid"
        else:
            bucket = "Bottom"
        item["bucket"] = bucket
        item["all_time_score_rank"] = idx + 1
    _assign_recent_30d_ranks(ranked)
    return ranked


def _scaled_bucket_quota(sample_size: int) -> Dict[str, int]:
    if sample_size <= 0:
        return {"Top": 0, "Strong": 0, "Mid": 0, "Bottom": 0}
    base = {"Top": 18, "Strong": 18, "Mid": 14, "Bottom": 10}
    raw = {key: sample_size * (value / 60.0) for key, value in base.items()}
    quota = {key: int(math.floor(value)) for key, value in raw.items()}
    quota["Bottom"] = max(quota.get("Bottom", 0), 1)
    deficit = sample_size - sum(quota.values())
    order = sorted(raw.items(), key=lambda item: raw[item[0]] - quota[item[0]], reverse=True)
    idx = 0
    while deficit > 0 and order:
        key = order[idx % len(order)][0]
        quota[key] += 1
        deficit -= 1
        idx += 1
    while sum(quota.values()) > sample_size:
        for key in ("Mid", "Strong", "Top", "Bottom"):
            min_keep = 1 if key == "Bottom" else 0
            if quota[key] > min_keep and sum(quota.values()) > sample_size:
                quota[key] -= 1
    if quota["Top"] + quota["Strong"] < math.ceil(sample_size * 0.55):
        needed = math.ceil(sample_size * 0.55) - (quota["Top"] + quota["Strong"])
        for _ in range(needed):
            if quota["Mid"] > 0:
                quota["Mid"] -= 1
                quota["Top"] += 1
            elif quota["Bottom"] > 1:
                quota["Bottom"] -= 1
                quota["Strong"] += 1
    return quota


def _pick_sample_size(total: int) -> int:
    if total <= 0:
        return 0
    return min(max(int(round(total * 0.30)), 40), 80, total)


def _value_variants(item: Dict[str, Any], field: str) -> List[str]:
    value = item.get(field)
    if isinstance(value, list):
        return [_safe_text(v) for v in value if _safe_text(v)]
    clean = _safe_text(value)
    return [clean] if clean else []


def _pick_diverse_items(pool: List[Dict[str, Any]], *, selected_ids: set, limits: Sequence[Tuple[str, int]], cap: int) -> List[Dict[str, Any]]:
    picked: List[Dict[str, Any]] = []
    covered: Dict[str, set] = {field: set() for field, _ in limits}
    local_ids: set = set()
    for field, minimum in limits:
        if minimum <= 0:
            continue
        for item in pool:
            if len(picked) >= cap:
                return picked
            work_id = _safe_text(item.get("platform_work_id"))
            if not work_id or work_id in selected_ids or work_id in local_ids:
                continue
            candidates = [value for value in _value_variants(item, field) if value not in covered[field]]
            if not candidates:
                continue
            picked.append(item)
            local_ids.add(work_id)
            for sync_field, _ in limits:
                covered[sync_field].update(_value_variants(item, sync_field))
            if len(covered[field]) >= minimum:
                break
    return picked


def _sample_standard_works(items: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    total = len(items)
    if total <= 0:
        return []
    sample_size = _pick_sample_size(total)
    quota = _scaled_bucket_quota(sample_size)
    bucket_groups: Dict[str, List[Dict[str, Any]]] = {"Top": [], "Strong": [], "Mid": [], "Bottom": []}
    for item in items:
        bucket_groups.setdefault(_safe_text(item.get("bucket")) or "Mid", []).append(item)
    selected: List[Dict[str, Any]] = []
    selected_ids: set = set()

    top_pool = bucket_groups.get("Top", [])
    for item in _pick_diverse_items(top_pool, selected_ids=selected_ids, limits=(("content_form", 3), ("hook_type", 2), ("structure_type", 2)), cap=quota.get("Top", 0)):
        selected.append(item)
        selected_ids.add(_safe_text(item.get("platform_work_id")))

    for bucket in ("Top", "Strong", "Mid", "Bottom"):
        pool = bucket_groups.get(bucket, [])
        for item in pool:
            if len([row for row in selected if _safe_text(row.get("bucket")) == bucket]) >= quota.get(bucket, 0):
                break
            work_id = _safe_text(item.get("platform_work_id"))
            if work_id in selected_ids:
                continue
            selected.append(item)
            selected_ids.add(work_id)
    if len(selected) < sample_size:
        for item in items:
            work_id = _safe_text(item.get("platform_work_id"))
            if work_id in selected_ids:
                continue
            selected.append(item)
            selected_ids.add(work_id)
            if len(selected) >= sample_size:
                break
    return selected[:sample_size]


def _keyword_distribution_from_texts(texts: Sequence[str], *, limit: int = 20) -> Dict[str, Any]:
    counter: Counter = Counter()
    for text in texts:
        counter.update(_unique_tokens(text))
    return {"items": _top_counter(counter, limit=limit), "counting_mode": "work_occurrence"}


def _field_keyword_distribution(works: List[Dict[str, Any]], field: str, *, limit: int = 20) -> Dict[str, Any]:
    return _keyword_distribution_from_texts([_safe_text(work.get(field)) for work in works], limit=limit)


def _publish_time_distribution(works: List[Dict[str, Any]]) -> Dict[str, Any]:
    weekday = Counter()
    hour = Counter()
    unavailable = 0
    for work in works:
        parsed = _parse_datetime(work.get("publish_time"))
        if parsed is None:
            unavailable += 1
            continue
        weekday[str(parsed.weekday())] += 1
        hour[str(parsed.hour)] += 1
    return {"weekday": _top_counter(weekday, limit=7), "hour": _top_counter(hour, limit=24), "unavailable_count": unavailable}


def _duration_distribution(works: List[Dict[str, Any]]) -> Dict[str, Any]:
    durations = [_safe_int(work.get("duration_ms"), 0) for work in works if _safe_int(work.get("duration_ms"), 0) > 0]
    if not durations:
        return {"available": False, "reason": "duration_unavailable"}
    counter = Counter()
    for duration in durations:
        counter["short" if duration < 30000 else ("medium" if duration < 120000 else "long")] += 1
    return {"available": True, "items": _top_counter(counter, limit=3)}


def _performance_distribution(items: List[Dict[str, Any]]) -> Dict[str, Any]:
    scores = [_safe_float(item.get("performance_score_norm"), 0.0) for item in items]
    if not scores:
        return {"available": False, "reason": "no_scores"}
    ordered = sorted(scores, reverse=True)
    def _pct(position: float) -> float:
        idx = min(max(int(math.floor((len(ordered) - 1) * position)), 0), len(ordered) - 1)
        return round(ordered[idx], 4)
    return {"available": True, "max": round(max(ordered), 4), "min": round(min(ordered), 4), "p20": _pct(0.20), "p50": _pct(0.50), "p85": _pct(0.85)}


def _engagement_pattern(items: List[Dict[str, Any]]) -> Dict[str, Any]:
    if not items:
        return {"count": 0, "avg_digg_count": 0, "avg_comment_count": 0, "avg_collect_count": 0, "avg_share_count": 0, "avg_play_count": 0}
    total = {"digg_count": 0, "comment_count": 0, "collect_count": 0, "share_count": 0, "play_count": 0}
    for item in items:
        for key in total:
            total[key] += _safe_int(item.get(key), 0)
    count = len(items)
    return {
        "count": count,
        "avg_digg_count": round(total["digg_count"] / count, 2),
        "avg_comment_count": round(total["comment_count"] / count, 2),
        "avg_collect_count": round(total["collect_count"] / count, 2),
        "avg_share_count": round(total["share_count"] / count, 2),
        "avg_play_count": round(total["play_count"] / count, 2),
    }


def _compare_bucket_groups(items: List[Dict[str, Any]]) -> Dict[str, Any]:
    groups = {name: [item for item in items if item.get("bucket") == name] for name in ("Top", "Mid", "Bottom")}
    result: Dict[str, Any] = {}
    for name, works in groups.items():
        result[name.lower()] = {
            "title_keywords": _field_keyword_distribution(works, "title", limit=8).get("items", []),
            "caption_keywords": _field_keyword_distribution(works, "caption_raw", limit=8).get("items", []),
            "primary_text_keywords": _field_keyword_distribution(works, "primary_text", limit=8).get("items", []),
            "hook_types": _distribution_from_values([_safe_text(work.get("hook_type")) for work in works], limit=6).get("items", []),
            "structure_types": _distribution_from_values([_safe_text(work.get("structure_type")) for work in works], limit=6).get("items", []),
            "cta_types": _distribution_from_values([_safe_text(work.get("cta_type")) for work in works], limit=6).get("items", []),
            "content_forms": _distribution_from_values([_safe_text(work.get("content_form")) for work in works], limit=6).get("items", []),
            "engagement_pattern": _engagement_pattern(works),
        }
    return result


def prepare_author_analysis_bundle(*, profile: Dict[str, Any], works: List[Dict[str, Any]], platform: str) -> Dict[str, Any]:
    normalized = [_normalize_work(profile, work) for work in works if isinstance(work, dict)]
    eligible = [item for item in normalized if _safe_text(item.get("analysis_eligibility")) == "eligible"]
    excluded_count = len(normalized) - len(eligible)
    ranked = _assign_buckets(eligible)
    sampled = _sample_standard_works(ranked)
    sampled_work_ids = [_safe_text(item.get("platform_work_id")) for item in sampled if _safe_text(item.get("platform_work_id"))]
    aggregate_stats = {
        "total_works": len(ranked),
        "excluded_works_count": excluded_count,
        "sampled_works_count": len(sampled),
        "sampling_ratio": round((len(sampled) / len(ranked)), 4) if ranked else 0.0,
        "sampling_mode": "standard",
        "analysis_window": "mixed",
        "global_title_keyword_distribution": _field_keyword_distribution(ranked, "title"),
        "global_caption_keyword_distribution": _field_keyword_distribution(ranked, "caption_raw"),
        "global_primary_text_keyword_distribution": _field_keyword_distribution(ranked, "primary_text"),
        "global_hook_type_distribution": _distribution_from_values([_safe_text(item.get("hook_type")) for item in ranked]),
        "global_structure_type_distribution": _distribution_from_values([_safe_text(item.get("structure_type")) for item in ranked]),
        "global_cta_type_distribution": _distribution_from_values([_safe_text(item.get("cta_type")) for item in ranked]),
        "global_content_form_distribution": _distribution_from_values([_safe_text(item.get("content_form")) for item in ranked]),
        "global_work_modality_distribution": _distribution_from_values([_safe_text(item.get("work_modality")) for item in ranked]),
        "global_performance_distribution": _performance_distribution(ranked),
        "global_publish_time_distribution": _publish_time_distribution(ranked),
        "global_duration_distribution": _duration_distribution(ranked),
        "global_bucket_distribution": _distribution_from_values([_safe_text(item.get("bucket")) for item in ranked], limit=4),
        "global_top_vs_mid_vs_bottom_deltas": _compare_bucket_groups(ranked),
    }
    analysis_input = {
        "author_profile": {
            "platform": _safe_text(profile.get("platform")) or platform,
            "platform_author_id": _safe_text(profile.get("author_platform_id") or profile.get("platform_author_id")),
            "nickname": _safe_text(profile.get("nickname")),
            "author_handle": _safe_text(profile.get("author_handle")),
            "signature": _safe_text(profile.get("signature")),
            "fans_count": _safe_int(profile.get("fans_count"), 0),
            "liked_count": _safe_int(profile.get("liked_count"), 0),
            "collected_count": _safe_int(profile.get("collected_count"), 0),
            "works_count": _safe_int(profile.get("works_count"), len(ranked)),
            "verified": bool(profile.get("verified", False)),
            "ip_location": _safe_text(profile.get("ip_location")),
        },
        "sampled_works": sampled,
        "aggregate_stats": aggregate_stats,
        "platform_context": {
            "platform": platform,
            "content_kind": "author_home",
            "primary_work_modality": ranked[0].get("work_modality") if ranked else None,
        },
        "analysis_metadata": {
            "input_object_name": "author_analysis_input_v1",
            "prompt_contract_path": str(PROMPT_CONTRACT_PATH),
            "input_schema_path": str(INPUT_SCHEMA_PATH),
            "output_schema_path": str(OUTPUT_SCHEMA_PATH),
            "analysis_mode": "standard",
            "total_works": len(normalized),
            "eligible_works_count": len(ranked),
            "excluded_works_count": excluded_count,
            "sampled_works_count": len(sampled),
        },
    }
    return {
        "analysis_input": analysis_input,
        "normalized_works": normalized,
        "ranked_works": ranked,
        "sampled_works": sampled,
        "sampled_work_ids": sampled_work_ids,
        "excluded_works_count": excluded_count,
    }


def build_author_analysis_input_v1(*, profile: Dict[str, Any], works: List[Dict[str, Any]], platform: str) -> Tuple[Dict[str, Any], List[Dict[str, str]]]:
    payload = prepare_author_analysis_bundle(profile=profile, works=works, platform=platform).get("analysis_input") or {}
    return payload, validate_author_analysis_input_v1(payload)


def _require_non_empty_string(errors: List[Dict[str, str]], field: str, value: Any) -> None:
    if not _safe_text(value):
        errors.append({"field": field, "reason": "empty_string"})


def _require_dict(errors: List[Dict[str, str]], field: str, value: Any) -> Dict[str, Any]:
    if not isinstance(value, dict):
        errors.append({"field": field, "reason": "type_error:dict"})
        return {}
    return value


def _require_list(errors: List[Dict[str, str]], field: str, value: Any) -> List[Any]:
    if not isinstance(value, list):
        errors.append({"field": field, "reason": "type_error:list"})
        return []
    return value


def _validate_distribution_object(errors: List[Dict[str, str]], field: str, value: Any) -> None:
    block = _require_dict(errors, field, value)
    if not block:
        return
    items = _require_list(errors, f"{field}.items", block.get("items"))
    for index, item in enumerate(items[:20]):
        row = _require_dict(errors, f"{field}.items.{index}", item)
        if row:
            _require_non_empty_string(errors, f"{field}.items.{index}.value", row.get("value"))
            if "count" not in row:
                errors.append({"field": f"{field}.items.{index}.count", "reason": "missing"})


def validate_author_analysis_input_v1(payload: Dict[str, Any]) -> List[Dict[str, str]]:
    errors: List[Dict[str, str]] = []
    errors.extend(_schema_errors(payload, INPUT_SCHEMA_PATH))
    author_profile = _require_dict(errors, "author_profile", payload.get("author_profile"))
    aggregate = _require_dict(errors, "aggregate_stats", payload.get("aggregate_stats"))
    platform_context = _require_dict(errors, "platform_context", payload.get("platform_context"))
    analysis_metadata = _require_dict(errors, "analysis_metadata", payload.get("analysis_metadata"))
    sampled_works = _require_list(errors, "sampled_works", payload.get("sampled_works"))

    _require_non_empty_string(errors, "author_profile.platform", author_profile.get("platform"))
    _require_non_empty_string(errors, "author_profile.platform_author_id", author_profile.get("platform_author_id"))
    _require_non_empty_string(errors, "author_profile.nickname", author_profile.get("nickname"))
    _require_non_empty_string(errors, "platform_context.platform", platform_context.get("platform"))
    _require_non_empty_string(errors, "platform_context.content_kind", platform_context.get("content_kind"))
    _require_non_empty_string(errors, "analysis_metadata.input_object_name", analysis_metadata.get("input_object_name"))
    _require_non_empty_string(errors, "analysis_metadata.analysis_mode", analysis_metadata.get("analysis_mode"))

    for key in [
        "global_title_keyword_distribution",
        "global_caption_keyword_distribution",
        "global_primary_text_keyword_distribution",
        "global_hook_type_distribution",
        "global_structure_type_distribution",
        "global_cta_type_distribution",
        "global_content_form_distribution",
        "global_work_modality_distribution",
        "global_performance_distribution",
        "global_publish_time_distribution",
        "global_bucket_distribution",
        "global_top_vs_mid_vs_bottom_deltas",
    ]:
        if key not in aggregate:
            errors.append({"field": f"aggregate_stats.{key}", "reason": "missing"})

    for field in [
        "aggregate_stats.global_title_keyword_distribution",
        "aggregate_stats.global_caption_keyword_distribution",
        "aggregate_stats.global_primary_text_keyword_distribution",
        "aggregate_stats.global_hook_type_distribution",
        "aggregate_stats.global_structure_type_distribution",
        "aggregate_stats.global_cta_type_distribution",
        "aggregate_stats.global_content_form_distribution",
        "aggregate_stats.global_work_modality_distribution",
        "aggregate_stats.global_bucket_distribution",
    ]:
        _validate_distribution_object(errors, field, payload.get(field.split(".")[0], {}).get(field.split(".")[1]) if field.startswith("aggregate_stats") else None)

    total_works = _safe_int(aggregate.get("total_works"), 0)
    if total_works > 0 and not sampled_works:
        errors.append({"field": "sampled_works", "reason": "empty_collection"})
    if sampled_works and _safe_int(aggregate.get("sampled_works_count"), -1) != len(sampled_works):
        errors.append({"field": "aggregate_stats.sampled_works_count", "reason": "count_mismatch"})

    for index, item in enumerate(sampled_works[:120]):
        row = _require_dict(errors, f"sampled_works.{index}", item)
        if not row:
            continue
        _require_non_empty_string(errors, f"sampled_works.{index}.platform_work_id", row.get("platform_work_id"))
        if not any(_safe_text(row.get(key)) for key in ("title", "caption_raw", "primary_text")):
            errors.append({"field": f"sampled_works.{index}", "reason": "all_text_fields_empty"})
        if _safe_text(row.get("work_modality")) not in {"video", "text"}:
            errors.append({"field": f"sampled_works.{index}.work_modality", "reason": "enum_required"})
        if _safe_text(row.get("primary_text_source")) not in {"asr_clean", "caption_raw"}:
            errors.append({"field": f"sampled_works.{index}.primary_text_source", "reason": "enum_required"})
        if _safe_text(row.get("hook_type")) not in HOOK_TYPES_ENUM:
            errors.append({"field": f"sampled_works.{index}.hook_type", "reason": "enum_required"})
        if _safe_text(row.get("structure_type")) not in STRUCTURE_TYPES:
            errors.append({"field": f"sampled_works.{index}.structure_type", "reason": "enum_required"})
        if _safe_text(row.get("cta_type")) not in CTA_TYPES:
            errors.append({"field": f"sampled_works.{index}.cta_type", "reason": "enum_required"})
        if _safe_text(row.get("content_form")) not in CONTENT_FORMS:
            errors.append({"field": f"sampled_works.{index}.content_form", "reason": "enum_required"})
        markers = _require_list(errors, f"sampled_works.{index}.style_markers", row.get("style_markers"))
        for marker in markers:
            if _safe_text(marker) not in STYLE_MARKERS_ENUM:
                errors.append({"field": f"sampled_works.{index}.style_markers", "reason": f"enum_required:{marker}"})
    return _dedupe_error_list(errors)


def _fallback_sample_confidence(sample_size: int) -> str:
    return "low" if sample_size < 5 else ("mid" if sample_size < 15 else "high")


def build_fallback_author_analysis_v2(payload: Dict[str, Any]) -> Dict[str, Any]:
    author = payload.get("author_profile") if isinstance(payload.get("author_profile"), dict) else {}
    aggregate = payload.get("aggregate_stats") if isinstance(payload.get("aggregate_stats"), dict) else {}
    sampled = payload.get("sampled_works") if isinstance(payload.get("sampled_works"), list) else []
    nickname = _safe_text(author.get("nickname")) or "该作者"
    top_keywords = [item.get("value") for item in ((aggregate.get("global_primary_text_keyword_distribution") or {}).get("items") or []) if isinstance(item, dict)][:5]
    theme_items = [item.get("value") for item in ((aggregate.get("global_caption_keyword_distribution") or {}).get("items") or []) if isinstance(item, dict)][:6]
    hook_items = [item.get("value") for item in ((aggregate.get("global_hook_type_distribution") or {}).get("items") or []) if isinstance(item, dict)][:3]
    structure_items = [item.get("value") for item in ((aggregate.get("global_structure_type_distribution") or {}).get("items") or []) if isinstance(item, dict)][:3]
    cta_items = [item.get("value") for item in ((aggregate.get("global_cta_type_distribution") or {}).get("items") or []) if isinstance(item, dict)][:3]
    sample_size = len(sampled)
    confidence = _fallback_sample_confidence(sample_size)
    representative = [{"platform_work_id": item.get("platform_work_id"), "title": item.get("title") or item.get("caption_raw") or item.get("primary_text"), "bucket": item.get("bucket")} for item in sampled[:5] if isinstance(item, dict)]
    dominant_themes = theme_items[:3]
    theme_clusters = []
    if dominant_themes:
        theme_clusters = [{"name": theme, "keywords": [theme]} for theme in dominant_themes]
    return {
        "author_positioning": {
            "one_liner": f"{nickname} 是一个围绕{dominant_themes[0] if dominant_themes else '内容增长'}持续输出的创作者，主要用高密度结构化表达帮助目标受众缩短试错路径。",
            "author_type": "creator_education",
            "primary_role": "teacher",
            "secondary_roles": ["operator"],
            "target_audience": "想提升内容与增长效率的创作者/操盘手",
            "core_problem_solved": "把复杂方法压缩成可快速模仿的内容动作",
            "core_value_proposition": "用短平快的机制化表达降低学习和执行门槛",
            "evidence": [f"top_keywords={top_keywords}", f"dominant_themes={dominant_themes}"],
        },
        "trust_model": {
            "primary_trust_source": "systematized_method",
            "secondary_trust_sources": ["demonstration", "consistency"],
            "trust_building_mechanisms": ["重复输出同类方法", "把观点包装成步骤/模板", "用案例或结果句强化可信度"],
            "trust_risks": ["样本主要来自单平台表达，真实性与转化深度证据有限"],
            "relationship_posture": {"distance": "mid", "authority_level": "mid", "affinity_level": "mid"},
            "evidence": [f"sample_size={sample_size}", f"structures={structure_items}"],
        },
        "cognitive_engine": {
            "worldview": "优先追求可执行、可复用、可放大的内容动作。",
            "value_priority": ["效率", "结果感", "方法压缩"],
            "problem_definition_style": "execution_problem",
            "reasoning_modes": ["workflow_packaging", "case_induction"],
            "knowledge_sources": ["作品标题/文案/字幕中的步骤化表达"],
            "judgment_style": {"certainty_level": "mid", "notes": "基于单平台主页样本初判"},
            "core_cognitive_actions": ["workflow_packaging", "result_compression"],
            "evidence": [f"keywords={top_keywords}", f"sample_size={sample_size}"],
        },
        "expression_hooks": {
            "language_style": {"oral_level": "mid", "assertiveness": "high", "emotional_intensity": "mid", "professional_density": "mid"},
            "hook_keywords": top_keywords[:5],
            "hook_types": [item for item in hook_items if item in HOOK_TYPES_ENUM] or ["result_hook"],
            "argument_patterns": ["先给结果/判断，再给步骤或解释", "用反差或对比压缩注意力获取"],
            "emotion_patterns": ["sharp_direct"],
            "memorability_sources": ["strong_keywords", "repeatable_phrases"],
            "evidence": [f"hook_types={hook_items}", f"keywords={top_keywords}"],
        },
        "content_mechanism": {
            "topic_sources": ["audience_questions", "workflow_demos"],
            "topic_goals": ["acquire_attention", "build_trust", "show_capability"],
            "winning_content_structures": [item for item in structure_items if item in WINNING_CONTENT_STRUCTURES] or ["hook_demo_result"],
            "repeatable_series": ["高频重复的母题/模板仍在持续输出"],
            "traffic_drivers": ["result_promise", "shortcut_imagination"],
            "content_flywheel": "用结果型标题拉点击，用结构化拆解留住注意力，再用 CTA 做后续动作承接。",
            "cross_platform_variation": "当前不可判断：缺少跨平台样本。",
            "dominant_themes": dominant_themes,
            "theme_clusters": theme_clusters,
            "evidence": [f"themes={dominant_themes}", f"structures={structure_items}", f"cta_types={cta_items}"],
        },
        "commercial_bridge": {
            "content_role_in_funnel": ["acquire_attention", "build_trust", "qualify"],
            "likely_products": ["course", "consulting"] if any(item in {"private_message_cta", "lead_magnet_cta"} for item in cta_items) else [],
            "conversion_path": "通过内容建立方法可信度，再用评论/私信/领取资料承接线索。",
            "content_product_fit": "mid",
            "business_model_signals": ["content_led_growth", "high_ip_dependency"],
            "commercial_risks": ["明确成交链路和产品证据不足，不能强断言单一模式。"],
            "evidence": [f"cta_types={cta_items}"],
        },
        "core_tensions": {
            "tensions": [
                {"label": "效率 vs 深度", "surface": "表达短促、结果先行", "deep_reason": "优先追求短视频环境下的注意力效率", "strategic_implication": "适合拉新，但要防止过度压缩导致信任深度不足"},
                {"label": "模板复用 vs 差异化", "surface": "高频复用相似母题", "deep_reason": "成熟模板能稳定产出", "strategic_implication": "需要持续刷新案例与视角，避免模板疲劳"},
            ],
            "most_important_tension": "高效率表达很强，但商业深度证据未必同步充足。",
            "evidence": [f"sample_size={sample_size}", f"themes={dominant_themes}"],
        },
        "evidence_pack": {
            "sample_size": sample_size,
            "sample_confidence": confidence,
            "representative_works": representative,
            "top_keywords": top_keywords,
            "observed_hooks": hook_items,
            "observed_ctas": cta_items,
            "observed_structures": structure_items,
            "notes": ["fallback_generated", "基于标准化输入的最小保底分析"],
        },
        "clone_guidance": {
            "copyable_elements": ["结果先行的标题结构", "步骤化表达", "稳定重复的母模板"],
            "non_copyable_elements": ["作者长期经验背书", "既有受众信任资产"],
            "borrowable_flavor": ["短句高密度", "判断明确", "先给结果再给解释"],
            "danger_zones": ["不要照抄口头禅和具体句子", "证据不足时别硬抄商业承诺"],
            "if_only_learn_one_thing": "学他把复杂方法压缩成高可执行内容动作的能力，而不是抄表面语气。",
        },
    }


def _enum_error(errors: List[Dict[str, str]], field: str, value: Any, allowed: set) -> None:
    if value in (None, "", []):
        return
    if isinstance(value, list):
        for item in value:
            if item not in allowed:
                errors.append({"field": field, "reason": f"enum_preferred:{item}"})
    elif value not in allowed:
        errors.append({"field": field, "reason": f"enum_preferred:{value}"})


def validate_author_analysis_v2(payload: Dict[str, Any], *, analysis_input: Optional[Dict[str, Any]] = None) -> List[Dict[str, str]]:
    errors: List[Dict[str, str]] = []
    errors.extend(_schema_errors(payload, OUTPUT_SCHEMA_PATH))
    for module, fields in REQUIRED_V2_FIELDS.items():
        block = payload.get(module)
        if not isinstance(block, dict):
            errors.append({"field": module, "reason": "missing_or_type_error:dict"})
            continue
        for field in fields:
            if field not in block:
                errors.append({"field": f"{module}.{field}", "reason": "missing"})

    author_positioning = _require_dict(errors, "author_positioning", payload.get("author_positioning"))
    trust_model = _require_dict(errors, "trust_model", payload.get("trust_model"))
    cognitive_engine = _require_dict(errors, "cognitive_engine", payload.get("cognitive_engine"))
    expression_hooks = _require_dict(errors, "expression_hooks", payload.get("expression_hooks"))
    content_mechanism = _require_dict(errors, "content_mechanism", payload.get("content_mechanism"))
    commercial_bridge = _require_dict(errors, "commercial_bridge", payload.get("commercial_bridge"))
    core_tensions = _require_dict(errors, "core_tensions", payload.get("core_tensions"))
    evidence_pack = _require_dict(errors, "evidence_pack", payload.get("evidence_pack"))
    clone_guidance = _require_dict(errors, "clone_guidance", payload.get("clone_guidance"))

    for field, value in [
        ("author_positioning.one_liner", author_positioning.get("one_liner")),
        ("author_positioning.target_audience", author_positioning.get("target_audience")),
        ("author_positioning.core_problem_solved", author_positioning.get("core_problem_solved")),
        ("author_positioning.core_value_proposition", author_positioning.get("core_value_proposition")),
        ("commercial_bridge.conversion_path", commercial_bridge.get("conversion_path")),
        ("content_mechanism.content_flywheel", content_mechanism.get("content_flywheel")),
        ("content_mechanism.cross_platform_variation", content_mechanism.get("cross_platform_variation")),
        ("core_tensions.most_important_tension", core_tensions.get("most_important_tension")),
        ("clone_guidance.if_only_learn_one_thing", clone_guidance.get("if_only_learn_one_thing")),
    ]:
        _require_non_empty_string(errors, field, value)

    posture = _require_dict(errors, "trust_model.relationship_posture", trust_model.get("relationship_posture"))
    lang_style = _require_dict(errors, "expression_hooks.language_style", expression_hooks.get("language_style"))
    judgment_style = _require_dict(errors, "cognitive_engine.judgment_style", cognitive_engine.get("judgment_style"))

    for list_field, value in [
        ("trust_model.secondary_trust_sources", trust_model.get("secondary_trust_sources")),
        ("trust_model.trust_building_mechanisms", trust_model.get("trust_building_mechanisms")),
        ("trust_model.trust_risks", trust_model.get("trust_risks")),
        ("cognitive_engine.value_priority", cognitive_engine.get("value_priority")),
        ("cognitive_engine.reasoning_modes", cognitive_engine.get("reasoning_modes")),
        ("cognitive_engine.knowledge_sources", cognitive_engine.get("knowledge_sources")),
        ("cognitive_engine.core_cognitive_actions", cognitive_engine.get("core_cognitive_actions")),
        ("expression_hooks.hook_keywords", expression_hooks.get("hook_keywords")),
        ("expression_hooks.hook_types", expression_hooks.get("hook_types")),
        ("expression_hooks.argument_patterns", expression_hooks.get("argument_patterns")),
        ("expression_hooks.emotion_patterns", expression_hooks.get("emotion_patterns")),
        ("expression_hooks.memorability_sources", expression_hooks.get("memorability_sources")),
        ("content_mechanism.topic_sources", content_mechanism.get("topic_sources")),
        ("content_mechanism.topic_goals", content_mechanism.get("topic_goals")),
        ("content_mechanism.winning_content_structures", content_mechanism.get("winning_content_structures")),
        ("content_mechanism.repeatable_series", content_mechanism.get("repeatable_series")),
        ("content_mechanism.traffic_drivers", content_mechanism.get("traffic_drivers")),
        ("content_mechanism.dominant_themes", content_mechanism.get("dominant_themes")),
        ("content_mechanism.theme_clusters", content_mechanism.get("theme_clusters")),
        ("commercial_bridge.content_role_in_funnel", commercial_bridge.get("content_role_in_funnel")),
        ("commercial_bridge.likely_products", commercial_bridge.get("likely_products")),
        ("commercial_bridge.business_model_signals", commercial_bridge.get("business_model_signals")),
        ("commercial_bridge.commercial_risks", commercial_bridge.get("commercial_risks")),
        ("evidence_pack.representative_works", evidence_pack.get("representative_works")),
        ("evidence_pack.top_keywords", evidence_pack.get("top_keywords")),
        ("evidence_pack.observed_hooks", evidence_pack.get("observed_hooks")),
        ("evidence_pack.observed_ctas", evidence_pack.get("observed_ctas")),
        ("evidence_pack.observed_structures", evidence_pack.get("observed_structures")),
        ("evidence_pack.notes", evidence_pack.get("notes")),
        ("clone_guidance.copyable_elements", clone_guidance.get("copyable_elements")),
        ("clone_guidance.non_copyable_elements", clone_guidance.get("non_copyable_elements")),
        ("clone_guidance.borrowable_flavor", clone_guidance.get("borrowable_flavor")),
        ("clone_guidance.danger_zones", clone_guidance.get("danger_zones")),
    ]:
        _require_list(errors, list_field, value)

    _enum_error(errors, "author_positioning.author_type", author_positioning.get("author_type"), AUTHOR_TYPES)
    _enum_error(errors, "author_positioning.primary_role", author_positioning.get("primary_role"), PRIMARY_ROLES)
    _enum_error(errors, "trust_model.primary_trust_source", trust_model.get("primary_trust_source"), TRUST_SOURCES)
    _enum_error(errors, "cognitive_engine.problem_definition_style", cognitive_engine.get("problem_definition_style"), PROBLEM_DEFINITION_STYLES)
    _enum_error(errors, "cognitive_engine.reasoning_modes", cognitive_engine.get("reasoning_modes"), REASONING_MODES)
    _enum_error(errors, "cognitive_engine.core_cognitive_actions", cognitive_engine.get("core_cognitive_actions"), CORE_COGNITIVE_ACTIONS)
    _enum_error(errors, "expression_hooks.hook_types", expression_hooks.get("hook_types"), HOOK_TYPES_ENUM)
    _enum_error(errors, "expression_hooks.emotion_patterns", expression_hooks.get("emotion_patterns"), EMOTION_PATTERNS)
    _enum_error(errors, "expression_hooks.memorability_sources", expression_hooks.get("memorability_sources"), MEMORABILITY_SOURCES)
    _enum_error(errors, "content_mechanism.topic_sources", content_mechanism.get("topic_sources"), TOPIC_SOURCES)
    _enum_error(errors, "content_mechanism.topic_goals", content_mechanism.get("topic_goals"), TOPIC_GOALS)
    _enum_error(errors, "content_mechanism.winning_content_structures", content_mechanism.get("winning_content_structures"), WINNING_CONTENT_STRUCTURES)
    _enum_error(errors, "content_mechanism.traffic_drivers", content_mechanism.get("traffic_drivers"), TRAFFIC_DRIVERS)
    _enum_error(errors, "commercial_bridge.content_role_in_funnel", commercial_bridge.get("content_role_in_funnel"), FUNNEL_ROLES)
    _enum_error(errors, "commercial_bridge.likely_products", commercial_bridge.get("likely_products"), LIKELY_PRODUCTS)
    _enum_error(errors, "commercial_bridge.business_model_signals", commercial_bridge.get("business_model_signals"), BUSINESS_MODEL_SIGNALS)
    _enum_error(errors, "trust_model.relationship_posture.distance", posture.get("distance"), RELATIONSHIP_DISTANCE)
    _enum_error(errors, "trust_model.relationship_posture.authority_level", posture.get("authority_level"), LOW_HIGH_MID)
    _enum_error(errors, "trust_model.relationship_posture.affinity_level", posture.get("affinity_level"), LOW_HIGH_MID)
    _enum_error(errors, "cognitive_engine.judgment_style.certainty_level", judgment_style.get("certainty_level"), LOW_HIGH_MID)
    _enum_error(errors, "expression_hooks.language_style.oral_level", lang_style.get("oral_level"), LOW_HIGH_MID)
    _enum_error(errors, "expression_hooks.language_style.assertiveness", lang_style.get("assertiveness"), LOW_HIGH_MID)
    _enum_error(errors, "expression_hooks.language_style.emotional_intensity", lang_style.get("emotional_intensity"), LOW_HIGH_MID)
    _enum_error(errors, "expression_hooks.language_style.professional_density", lang_style.get("professional_density"), LOW_HIGH_MID)
    _enum_error(errors, "commercial_bridge.content_product_fit", commercial_bridge.get("content_product_fit"), LOW_HIGH_MID)
    _enum_error(errors, "evidence_pack.sample_confidence", evidence_pack.get("sample_confidence"), LOW_HIGH_MID)
    _enum_error(errors, "evidence_pack.observed_hooks", evidence_pack.get("observed_hooks"), HOOK_TYPES_ENUM)
    _enum_error(errors, "evidence_pack.observed_ctas", evidence_pack.get("observed_ctas"), CTA_TYPES)
    _enum_error(errors, "evidence_pack.observed_structures", evidence_pack.get("observed_structures"), STRUCTURE_TYPES)

    tensions = _require_list(errors, "core_tensions.tensions", core_tensions.get("tensions"))
    if len(tensions) < 2:
        errors.append({"field": "core_tensions.tensions", "reason": "guardrail:need_at_least_2"})
    for index, tension in enumerate(tensions[:10]):
        block = _require_dict(errors, f"core_tensions.tensions.{index}", tension)
        for sub in ("label", "surface", "deep_reason", "strategic_implication"):
            _require_non_empty_string(errors, f"core_tensions.tensions.{index}.{sub}", block.get(sub))

    representative_works = evidence_pack.get("representative_works") if isinstance(evidence_pack.get("representative_works"), list) else []
    for index, work in enumerate(representative_works[:10]):
        block = _require_dict(errors, f"evidence_pack.representative_works.{index}", work)
        _require_non_empty_string(errors, f"evidence_pack.representative_works.{index}.platform_work_id", block.get("platform_work_id"))
        _require_non_empty_string(errors, f"evidence_pack.representative_works.{index}.title", block.get("title"))
        _require_non_empty_string(errors, f"evidence_pack.representative_works.{index}.bucket", block.get("bucket"))

    for field, value in [
        ("author_positioning.evidence", author_positioning.get("evidence")),
        ("trust_model.evidence", trust_model.get("evidence")),
        ("cognitive_engine.evidence", cognitive_engine.get("evidence")),
        ("expression_hooks.evidence", expression_hooks.get("evidence")),
        ("content_mechanism.evidence", content_mechanism.get("evidence")),
        ("commercial_bridge.evidence", commercial_bridge.get("evidence")),
        ("core_tensions.evidence", core_tensions.get("evidence")),
    ]:
        items = _require_list(errors, field, value)
        if not items:
            errors.append({"field": field, "reason": "empty_collection"})

    sample_size = _safe_int(evidence_pack.get("sample_size"), 0)
    sample_confidence = _safe_text(evidence_pack.get("sample_confidence"))
    if sample_size < 5 and sample_confidence == "high":
        errors.append({"field": "evidence_pack.sample_confidence", "reason": "guardrail:sample_lt_5_cannot_be_high"})

    if analysis_input is not None:
        platform_context = analysis_input.get("platform_context") if isinstance(analysis_input.get("platform_context"), dict) else {}
        if len({platform_context.get("platform")} - {None, ""}) <= 1:
            cross_platform_variation = _safe_text(content_mechanism.get("cross_platform_variation"))
            if cross_platform_variation and "不可判断" not in cross_platform_variation and "unknown" not in cross_platform_variation.lower():
                errors.append({"field": "content_mechanism.cross_platform_variation", "reason": "guardrail:single_platform_should_stay_weak"})
        aggregate = analysis_input.get("aggregate_stats") if isinstance(analysis_input.get("aggregate_stats"), dict) else {}
        cta_items = ((aggregate.get("global_cta_type_distribution") or {}).get("items") or []) if isinstance((aggregate.get("global_cta_type_distribution") or {}), dict) else []
        explicit_conversion = any(isinstance(item, dict) and item.get("value") in {"private_message_cta", "lead_magnet_cta"} for item in cta_items)
        likely_products = commercial_bridge.get("likely_products") if isinstance(commercial_bridge.get("likely_products"), list) else []
        if likely_products and not explicit_conversion:
            errors.append({"field": "commercial_bridge.likely_products", "reason": "guardrail:weak_conversion_signal"})
    return _dedupe_error_list(errors)


def derive_legacy_summary(author_analysis_v2: Dict[str, Any], *, analysis_input: Dict[str, Any], validation_errors: Optional[List[Dict[str, str]]] = None) -> Dict[str, Any]:
    positioning = author_analysis_v2.get("author_positioning") if isinstance(author_analysis_v2.get("author_positioning"), dict) else {}
    trust = author_analysis_v2.get("trust_model") if isinstance(author_analysis_v2.get("trust_model"), dict) else {}
    content = author_analysis_v2.get("content_mechanism") if isinstance(author_analysis_v2.get("content_mechanism"), dict) else {}
    bridge = author_analysis_v2.get("commercial_bridge") if isinstance(author_analysis_v2.get("commercial_bridge"), dict) else {}
    tensions = author_analysis_v2.get("core_tensions") if isinstance(author_analysis_v2.get("core_tensions"), dict) else {}
    clone = author_analysis_v2.get("clone_guidance") if isinstance(author_analysis_v2.get("clone_guidance"), dict) else {}
    evidence = author_analysis_v2.get("evidence_pack") if isinstance(author_analysis_v2.get("evidence_pack"), dict) else {}
    aggregate = analysis_input.get("aggregate_stats") if isinstance(analysis_input.get("aggregate_stats"), dict) else {}

    sample_confidence = _safe_text(evidence.get("sample_confidence")) or _fallback_sample_confidence(_safe_int(evidence.get("sample_size"), 0))
    score_base = {"low": 58, "mid": 72, "high": 84}.get(sample_confidence, 60)
    if validation_errors:
        score_base -= min(len(validation_errors) * 2, 12)
    business_score = int(_clamp(score_base + (6 if (bridge.get("likely_products") or []) else -4), 40, 92))
    benchmark_gap_score = int(_clamp(100 - business_score + 8, 35, 88))
    hook_items = [item.get("value") for item in ((aggregate.get("global_hook_type_distribution") or {}).get("items") or []) if isinstance(item, dict)]
    structure_items = [item.get("value") for item in ((aggregate.get("global_structure_type_distribution") or {}).get("items") or []) if isinstance(item, dict)]
    dominant_themes = content.get("dominant_themes") if isinstance(content.get("dominant_themes"), list) else []
    return {
        "author_portrait": _safe_text(positioning.get("one_liner")) or "作者画像数据不足。",
        "business_analysis": "；".join([
            _safe_text(positioning.get("core_value_proposition")),
            f"主要信任来源：{_safe_text(trust.get('primary_trust_source')) or '待确认'}",
            f"商业承接：{_safe_text(bridge.get('conversion_path')) or '当前证据不足'}",
        ]).strip("；"),
        "benchmark_analysis": "；".join([
            f"高频 hook：{', '.join(hook_items[:3]) or '待补'}",
            f"常见结构：{', '.join(structure_items[:3]) or '待补'}",
            f"主主题：{', '.join(dominant_themes[:3]) or '待补'}",
        ]).strip("；"),
        "business_score": business_score,
        "benchmark_gap_score": benchmark_gap_score,
        "style_radar": {"选题": 76, "表达": 78, "结构": 79, "节奏": 74, "人设": 73, "转化": 70, "差异化": 71, "稳定性": 79},
        "core_contradictions": [tensions.get("most_important_tension") or "张力信息不足"],
        "recommendations": [clone.get("if_only_learn_one_thing") or "优先学习其可复用的结构机制"],
    }
