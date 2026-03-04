#!/usr/bin/env python3

if __package__ in {None, ""}:
    import sys
    from pathlib import Path

    _self = Path(__file__).resolve()
    for _parent in _self.parents:
        if (_parent / "scripts").is_dir():
            sys.path.insert(0, str(_parent))
            break

"""Write benchmark markdown cards into card root zones."""

import argparse
import datetime as dt
import json
import os
import re
import unicodedata
from pathlib import Path
from typing import Any, Dict, List, Optional

from scripts.core.analysis_pipeline import DEFAULT_MODULE_SECTIONS, build_analysis_sections
from scripts.core.storage_router import build_card_output_path, normalize_card_type, resolve_effective_card_type
from scripts.core.tikomni_common import normalize_text, read_json_file, write_json_stdout

def resolve_default_card_root() -> str:
    raw = os.getenv("TIKOMNI_CARD_ROOT", "").strip()
    if not raw:
        raise ValueError(
            "missing_card_root: set --card-root or define TIKOMNI_CARD_ROOT in .env/.env.local"
        )

    candidate = Path(raw).expanduser()
    if not candidate.is_absolute():
        raise ValueError("TIKOMNI_CARD_ROOT must be an absolute path")
    return str(candidate.resolve())


# Keep import-time compatibility for other scripts without crashing when env is absent.
DEFAULT_CARD_ROOT = ""
CARD_TYPES = ["work", "author", "author_sample_work"]
ASR_CLEAN_CONTRACT = "prompt-contracts/asr-clean.md@v1"


def _normalize_lines(value: Any) -> List[str]:
    if isinstance(value, list):
        return [normalize_text(item) for item in value if normalize_text(item)]
    if isinstance(value, str):
        text = normalize_text(value)
        return [text] if text else []
    return []


def _safe_int(value: Any, default: int = 0) -> int:
    if value is None:
        return default
    if isinstance(value, bool):
        return int(value)
    if isinstance(value, int):
        return value
    if isinstance(value, float):
        return int(value)
    if isinstance(value, str):
        text = value.strip()
        if text.isdigit() or (text.startswith("-") and text[1:].isdigit()):
            return int(text)
    return default


def _source_dict(payload: Dict[str, Any]) -> Dict[str, Any]:
    source = payload.get("source")
    return source if isinstance(source, dict) else {}


def _extract_duration_ms(payload: Dict[str, Any]) -> int:
    source = _source_dict(payload)

    def _pick_int(keys: List[str], from_source: bool = False) -> int:
        base = source if from_source else payload
        for key in keys:
            value = _safe_int(base.get(key), default=0)
            if value > 0:
                return value
        return 0

    duration_ms = _pick_int(["duration_ms"])
    if duration_ms <= 0:
        duration_ms = _pick_int(["duration_ms"], from_source=True)

    if duration_ms <= 0:
        raw_duration = _pick_int(["duration", "duration_sec"])
        if raw_duration <= 0:
            raw_duration = _pick_int(["duration", "duration_sec"], from_source=True)
        if raw_duration > 0:
            duration_ms = raw_duration * 1000 if raw_duration < 10000 else raw_duration

    return duration_ms


def _ensure_sentence_end(text: str) -> str:
    if not text:
        return text
    if text[-1] in "。！？!?" or text.endswith("..."):
        return text
    return f"{text}。"


def _clean_asr_text(raw: str, provided_clean: str) -> str:
    """ASR_CLEAN prompt-contracts/asr-clean.md@v1

    Steps:
    1) base select: provided_clean > raw
    2) denoise: remove filler/repetition/whitespace noise
    3) sentence split + punctuation restore
    4) paragraphize: one sentence per line, 2-4 sentences per paragraph
    """
    base = normalize_text(provided_clean) or normalize_text(raw)
    if not base:
        return ""

    # step2: 去噪（口头禅/重复）
    base = re.sub(r"\b(嗯|啊|呃|额|那个|这个|然后|就是)\b", " ", base)
    base = re.sub(r"(嗯+|啊+|呃+)", " ", base)
    base = re.sub(r"(就是就是|然后然后|这个这个|那个那个)", " ", base)
    base = re.sub(r"\s+", " ", base).strip()

    # step3: 断句 + 句尾标点
    units = [normalize_text(part) for part in re.split(r"[。！？!?；;\n]+", base)]
    sentences = [_ensure_sentence_end(unit) for unit in units if unit]
    if not sentences:
        fallback = _ensure_sentence_end(base)
        return fallback if fallback else ""

    # step4: 每句一行；每段 2~4 句（默认 3 句）
    paragraphs: List[str] = []
    bucket: List[str] = []
    for sentence in sentences:
        bucket.append(sentence)
        if len(bucket) >= 3:
            paragraphs.append("\n".join(bucket))
            bucket = []

    if bucket:
        if len(bucket) == 1 and paragraphs:
            paragraphs[-1] = f"{paragraphs[-1]}\n{bucket[0]}"
        else:
            paragraphs.append("\n".join(bucket))

    return "\n\n".join(paragraphs)


def _pick_text(payload: Dict[str, Any], keys: List[str], source_keys: Optional[List[str]] = None) -> str:
    source = _source_dict(payload)
    for key in keys:
        text = normalize_text(payload.get(key))
        if text:
            return text
    for key in (source_keys or keys):
        text = normalize_text(source.get(key))
        if text:
            return text
    return ""


def _extract_platform_work_id(payload: Dict[str, Any]) -> str:
    return _pick_text(
        payload,
        ["platform_work_id", "aweme_id", "note_id", "item_id", "id"],
        ["platform_work_id", "aweme_id", "note_id", "item_id", "id"],
    )


def _extract_author(payload: Dict[str, Any]) -> Dict[str, str]:
    author_raw = payload.get("author")
    author = author_raw if isinstance(author_raw, dict) else {}

    source = _source_dict(payload)
    source_author = source.get("author") if isinstance(source.get("author"), dict) else {}

    author_text = normalize_text(author_raw) if isinstance(author_raw, str) else ""
    nickname = (
        normalize_text(author.get("nickname"))
        or author_text
        or normalize_text(source_author.get("nickname"))
    )
    unique_id = (
        normalize_text(payload.get("unique_id"))
        or normalize_text(author.get("unique_id"))
        or normalize_text(source_author.get("unique_id"))
    )
    sec_uid = (
        normalize_text(payload.get("sec_uid"))
        or normalize_text(author.get("sec_uid"))
        or normalize_text(source_author.get("sec_uid"))
    )

    return {
        "nickname": nickname,
        "unique_id": unique_id,
        "sec_uid": sec_uid,
    }


def _is_cjk(char: str) -> bool:
    code = ord(char)
    return 0x4E00 <= code <= 0x9FFF


def _clean_for_filename(text: str) -> str:
    if not text:
        return ""

    normalized = unicodedata.normalize("NFKC", text)
    normalized = re.sub(r"[#＃][^\s#＃]+", " ", normalized)
    normalized = re.sub(r"\[[^\]]+\]", " ", normalized)
    normalized = normalized.replace("\n", " ").replace("\r", " ")

    kept: List[str] = []
    for ch in normalized:
        cat = unicodedata.category(ch)
        if _is_cjk(ch) or ch.isalnum() or ch in {" ", "-", "_"}:
            kept.append(ch)
        elif cat.startswith("Z"):
            kept.append(" ")

    compact = "".join(kept)
    compact = re.sub(r"\s+", "", compact)
    compact = re.sub(r"[\\/:*?\"<>|]", "", compact)
    return compact.strip("._-")


def _clip_with_min(text: str, min_len: int, max_len: int, fallback: str) -> str:
    candidate = _clean_for_filename(text)
    fallback_clean = _clean_for_filename(fallback)

    if not candidate:
        candidate = fallback_clean
    if len(candidate) < min_len:
        candidate = (candidate + fallback_clean)[:max_len]
    if len(candidate) < min_len:
        candidate = (candidate + "内容速览")[:max_len]

    candidate = candidate[:max_len]
    if len(candidate) < min_len:
        candidate = (candidate + "作品卡")[:max_len]
    return candidate[:max_len] if candidate else fallback_clean[:max_len]


def _pick_author_slug(payload: Dict[str, Any], author_hint: Optional[str] = None) -> str:
    base = normalize_text(author_hint)
    if not base:
        author = _extract_author(payload)
        base = author["nickname"] or author["unique_id"] or author["sec_uid"] or "作者"
    slug = _clip_with_min(base, min_len=2, max_len=18, fallback="作者")
    return slug if len(slug) >= 2 else "作者"


def _pick_title_source(payload: Dict[str, Any]) -> str:
    for key in ("title", "desc", "summary"):
        text = normalize_text(payload.get(key))
        if text:
            return text

    source = _source_dict(payload)
    for key in ("title", "desc"):
        text = normalize_text(source.get(key))
        if text:
            return text

    raw_content = normalize_text(payload.get("raw_content"))
    if raw_content:
        return raw_content[:48]

    platform_work_id = _extract_platform_work_id(payload)
    if platform_work_id:
        return f"作品拆解{platform_work_id[-8:]}"

    return "内容拆解速览"


def _pick_title_slug(payload: Dict[str, Any]) -> str:
    title_source = _pick_title_source(payload)
    platform_work_id = _extract_platform_work_id(payload)
    fallback = f"内容拆解{platform_work_id[-8:]}" if platform_work_id else "内容拆解速览"
    slug = _clip_with_min(title_source, min_len=8, max_len=28, fallback=fallback)
    return slug if slug else "内容拆解速览"


def _extract_tags(payload: Dict[str, Any]) -> List[str]:
    for key in ("tags", "tag_list", "hashtags"):
        value = payload.get(key)
        if isinstance(value, list):
            tags = [normalize_text(item).lstrip("#") for item in value if normalize_text(item)]
            if tags:
                return list(dict.fromkeys(tags))
        if isinstance(value, str) and normalize_text(value):
            parts = re.split(r"[,，\s]+", normalize_text(value))
            tags = [part.lstrip("#") for part in parts if part]
            if tags:
                return list(dict.fromkeys(tags))

    source = _source_dict(payload)
    for key in ("tags", "tag_list", "hashtags"):
        value = source.get(key)
        if isinstance(value, list):
            tags = [normalize_text(item).lstrip("#") for item in value if normalize_text(item)]
            if tags:
                return list(dict.fromkeys(tags))

    return []


def _extract_required_fields(payload: Dict[str, Any], platform: str) -> Dict[str, Any]:
    author = _extract_author(payload)

    title = _pick_text(payload, ["title", "desc"], ["title", "desc"])
    platform_work_id = _extract_platform_work_id(payload)

    source_url = _pick_text(
        payload,
        ["source_url", "share_url", "url"],
        ["source_url", "share_url", "url", "share_text"],
    )
    share_url = _pick_text(
        payload,
        ["share_url", "canonical_share_url"],
        ["share_url", "canonical_share_url", "url", "source_url", "share_text"],
    ) or source_url

    cover_image = _pick_text(
        payload,
        ["cover_image", "cover_url", "cover"],
        ["cover_image", "cover_url", "cover", "origin_cover"],
    )
    selected_images = payload.get("selected_image_urls")
    if not cover_image and isinstance(selected_images, list) and selected_images:
        cover_image = normalize_text(selected_images[0])

    video_down_url = _pick_text(
        payload,
        ["video_down_url", "selected_video_url", "original_video_url", "video_url", "download_url"],
        ["video_down_url", "selected_video_url", "original_video_url", "video_url", "download_url"],
    )

    create_time_sec = _safe_int(payload.get("create_time_sec"), default=0)
    if create_time_sec <= 0:
        create_time_sec = _safe_int(payload.get("create_time"), default=0)
    if create_time_sec <= 0:
        create_time_sec = _safe_int(_source_dict(payload).get("create_time"), default=0)

    digg_count = _safe_int(payload.get("digg_count"), default=0)
    comment_count = _safe_int(payload.get("comment_count"), default=0)
    collect_count = _safe_int(payload.get("collect_count"), default=0)
    share_count = _safe_int(payload.get("share_count"), default=0)
    play_count = _safe_int(payload.get("play_count"), default=0)

    summary = normalize_text(payload.get("summary"))
    raw_content = normalize_text(payload.get("raw_content"))
    provided_asr_clean = normalize_text(payload.get("asr_clean"))
    asr_clean = _clean_asr_text(raw_content, provided_asr_clean)

    duration_ms = _extract_duration_ms(payload)

    category = normalize_text(payload.get("category"))
    if not category:
        category = "观点"

    hot_score = _safe_int(payload.get("hot_score"), default=0)
    if hot_score <= 0:
        hot_score = digg_count + comment_count * 2 + collect_count * 3 + share_count * 4

    content_type = normalize_text(payload.get("content_type"))
    if not content_type:
        content_type = "video"

    caption_status = normalize_text(payload.get("caption_status"))
    if not caption_status:
        caption_status = "missing" if not raw_content else "ready"

    return {
        "title": title,
        "platform": platform,
        "platform_work_id": platform_work_id,
        "author": author.get("nickname") or "",
        "unique_id": author.get("unique_id") or "",
        "sec_uid": author.get("sec_uid") or "",
        "share_url": share_url,
        "source_url": source_url,
        "cover_image": cover_image,
        "video_down_url": video_down_url,
        "create_time_sec": create_time_sec,
        "duration_ms": duration_ms,
        "digg_count": digg_count,
        "comment_count": comment_count,
        "collect_count": collect_count,
        "share_count": share_count,
        "play_count": play_count,
        "caption_status": caption_status,
        "tags": _extract_tags(payload),
        "content_type": content_type,
        "category": category,
        "summary": summary,
        "hot_score": hot_score,
        "raw_content": raw_content,
        "asr_clean": asr_clean,
        "asr_clean_contract": ASR_CLEAN_CONTRACT,
        "request_id": payload.get("request_id"),
        "confidence": normalize_text(payload.get("confidence")) or "low",
        "error_reason": payload.get("error_reason"),
        "extract_trace": payload.get("extract_trace", []),
    }


def _format_create_time(create_time_sec: int) -> str:
    if create_time_sec <= 0:
        return "未知"
    try:
        ts = dt.datetime.fromtimestamp(create_time_sec)
        return ts.strftime("%Y-%m-%d %H:%M:%S")
    except Exception:
        return str(create_time_sec)


def _format_duration(duration_ms: int) -> str:
    if duration_ms <= 0:
        return "未知"
    total_sec = duration_ms // 1000
    minute, second = divmod(total_sec, 60)
    if minute:
        return f"{minute}分{second:02d}秒"
    return f"{second}秒"


def _sentence_units(text: str) -> List[str]:
    if not text:
        return []
    return [normalize_text(x) for x in re.split(r"[。！？!?；;\\n]+", text) if normalize_text(x)]


def _first_sentence(text: str) -> str:
    units = _sentence_units(text)
    return units[0] if units else ""


def _hit_count(text: str, keywords: List[str]) -> int:
    if not text:
        return 0
    return sum(1 for token in keywords if token in text)


def _top_keywords(text: str, candidates: List[str], topn: int = 3) -> List[str]:
    if not text:
        return []
    scored = []
    for token in candidates:
        count = text.count(token)
        if count > 0:
            scored.append((count, token))
    scored.sort(key=lambda x: (-x[0], len(x[1])))
    return [token for _, token in scored[:topn]]


def _score_from_hits(hits: int, full_score_hits: int = 4) -> int:
    if hits <= 0:
        return 2
    if hits >= full_score_hits:
        return 5
    return min(5, hits + 2)



def _analyze_topic(fields: Dict[str, Any]) -> Dict[str, Any]:
    title = normalize_text(fields.get("title") or "")
    asr = normalize_text(fields.get("asr_clean") or "")
    category = normalize_text(fields.get("category") or "")
    text = f"{title} {asr}"

    if not text.strip():
        return {
            "score": 2,
            "lines": ["- 类型：数据不足。", "- 细分主题：数据不足。", "- 受众痛点：数据不足，需补充标题或ASR。"],
            "gaps": ["补齐标题或ASR文本，才能完成选题分类与主题归因"],
            "evidence": "输入文本缺失",
        }

    type_rules = {
        "流量型": ["热点", "挑战", "反转", "揭秘", "真相", "别再", "为什么", "踩坑", "3秒", "爆款"],
        "人设型": ["我是", "我们", "日常", "系列", "分享", "经历", "成长", "复盘", "带你", "我"],
        "营销型": ["领取", "私信", "咨询", "下单", "课程", "优惠", "链接", "报名", "合作", "购买"],
    }
    type_scores = {name: _hit_count(text, kws) for name, kws in type_rules.items()}

    if category in ["教程", "知识", "方法"]:
        type_scores["营销型"] += 1
    if category in ["观点", "人设", "日常"]:
        type_scores["人设型"] += 1

    main_type = max(type_scores, key=lambda k: type_scores[k])
    main_hits = type_scores[main_type]

    theme_candidates = [
        "AI", "智能体", "变现", "副业", "教程", "工作流", "流量", "涨粉", "投流", "口播", "脚本", "工具", "私域", "创业", "营销",
    ]
    themes = _top_keywords(text, theme_candidates, topn=3)
    pain_candidates = ["不会", "焦虑", "卡住", "没流量", "转化", "不会写", "不会做", "时间不够", "担心", "风险"]
    pains = _top_keywords(text, pain_candidates, topn=2)

    lines = [
        f"- 基础类型：{main_type}（命中信号 {main_hits} 个）。",
        f"- 细分主题：{'、'.join(themes) if themes else '数据不足（未检测到显著主题词）'}。",
        f"- 受众痛点：{'、'.join(pains) if pains else '以“快速落地/降低门槛”为主（显性痛点词不足）'}。",
    ]

    return {
        "score": _score_from_hits(main_hits),
        "lines": lines,
        "gaps": [] if themes else ["补充更完整ASR，提高细分主题识别稳定性"],
        "evidence": f"类型命中分布={type_scores}",
    }


def _analyze_style(fields: Dict[str, Any]) -> Dict[str, Any]:
    asr = normalize_text(fields.get("asr_clean") or "")
    title = normalize_text(fields.get("title") or "")
    text = f"{title} {asr}".strip()
    units = _sentence_units(asr)

    if not text:
        return {
            "score": 2,
            "lines": ["- 人设匹配：数据不足。", "- 句式结构：数据不足。", "- 语气与情绪：数据不足。"],
            "gaps": ["补齐ASR文本后再做文风拆解"],
            "evidence": "输入文本缺失",
        }

    avg_len = int(sum(len(u) for u in units) / max(1, len(units))) if units else 0
    if avg_len <= 14:
        length_type = "短句为主"
    elif avg_len <= 24:
        length_type = "中短句混合"
    else:
        length_type = "中长句为主"

    q_count = text.count("?") + text.count("？")
    e_count = text.count("!") + text.count("！")
    statement_count = max(0, len(units) - q_count - e_count)
    persona_hits = _hit_count(text, ["我", "我们", "你", "大家", "朋友们", "聪明的你"])
    rhetoric_hits = _hit_count(text, ["不是", "而是", "其实", "真的", "一定", "必须", "先", "再"])

    lines = [
        f"- 句式结构：{length_type}，平均句长约 {avg_len} 字。",
        f"- 语气分布：疑问 {q_count} / 感叹 {e_count} / 陈述 {statement_count}。",
        f"- 人设与修辞：人设代词命中 {persona_hits} 次，强调/转折词命中 {rhetoric_hits} 次。",
    ]

    strength_hits = int(avg_len > 0) + int(persona_hits > 0) + int(rhetoric_hits > 0)
    return {
        "score": _score_from_hits(strength_hits, full_score_hits=3),
        "lines": lines,
        "gaps": [] if units else ["ASR分句失败，建议人工复核"],
        "evidence": f"avg_len={avg_len}, persona_hits={persona_hits}, rhetoric_hits={rhetoric_hits}",
    }


def _analyze_hook(fields: Dict[str, Any]) -> Dict[str, Any]:
    title = normalize_text(fields.get("title") or "")
    asr = normalize_text(fields.get("asr_clean") or "")
    first = _first_sentence(asr) or title
    middle = _sentence_units(asr)[len(_sentence_units(asr)) // 2] if _sentence_units(asr) else ""

    if not first:
        return {
            "score": 2,
            "lines": ["- 开头钩子：数据不足。", "- 中段钩子：数据不足。", "- 结尾钩子：数据不足。"],
            "gaps": ["缺少标题与ASR，无法提取钩子原话"],
            "evidence": "开头句缺失",
        }

    hook_type = "陈述式"
    if any(k in first for k in ["?", "？", "为什么", "怎么"]):
        hook_type = "疑问式"
    elif any(k in first for k in ["别再", "误区", "真相", "不是"]):
        hook_type = "反常识式"
    elif any(k in first for k in ["当你", "如果", "今天"]):
        hook_type = "场景代入式"

    end_candidates = [u for u in _sentence_units(asr) if _hit_count(u, ["关注", "评论", "私信", "收藏", "转发", "下次见", "领取"]) > 0]
    end = end_candidates[-1] if end_candidates else "未检测到明确结尾钩子"

    lines = [
        f"- 开头钩子（{hook_type}）：{first}",
        f"- 中段钩子：{middle or '数据不足（中段文本不足）'}",
        f"- 结尾钩子：{end}",
    ]

    hook_hits = int(first != "") + int(bool(middle)) + int(end != "未检测到明确结尾钩子")
    return {
        "score": _score_from_hits(hook_hits, full_score_hits=3),
        "lines": lines,
        "gaps": [] if hook_hits >= 2 else ["建议补充中段转折钩子与结尾动作钩子"],
        "evidence": f"hook_type={hook_type}, hook_hits={hook_hits}",
    }


def _analyze_structure(fields: Dict[str, Any]) -> Dict[str, Any]:
    asr = normalize_text(fields.get("asr_clean") or "")
    units = _sentence_units(asr)
    if not units:
        return {
            "score": 2,
            "lines": ["- 结构标签：数据不足。", "- 模板判定：数据不足。"],
            "gaps": ["补充ASR后再进行结构标注"],
            "evidence": "分句为空",
        }

    label_rules = {
        "钩子": ["?", "？", "为什么", "怎么", "别再", "真相", "当你", "如果"],
        "冲突": ["但是", "却", "问题", "误区", "卡住", "焦虑", "失败"],
        "转折": ["所以", "于是", "然后", "接着", "这时候", "其实"],
        "举证": ["数据", "案例", "比如", "步骤", "第一", "第二", "第三"],
        "CTA": ["评论", "关注", "私信", "收藏", "转发", "点击", "领取", "报名"],
    }
    coverage = {k: 0 for k in label_rules}
    for sent in units:
        for label, kws in label_rules.items():
            if any(kw in sent for kw in kws):
                coverage[label] += 1

    present = [k for k, v in coverage.items() if v > 0]
    missing = [k for k, v in coverage.items() if v == 0]
    template = "钩子→冲突→转折→举证→CTA" if len(present) >= 4 else "钩子→观点→补充说明"

    lines = [
        f"- 结构标签覆盖：{', '.join([f'{k}:{v}' for k, v in coverage.items()])}。",
        f"- 模板判定：{template}。",
        f"- 缺失模块：{'、'.join(missing) if missing else '无'}。",
    ]

    return {
        "score": _score_from_hits(len(present), full_score_hits=5),
        "lines": lines,
        "gaps": [f"优先补齐结构模块：{'、'.join(missing)}"] if missing else [],
        "evidence": f"coverage={coverage}",
    }


def _analyze_cta(fields: Dict[str, Any]) -> Dict[str, Any]:
    asr = normalize_text(fields.get("asr_clean") or "")
    units = _sentence_units(asr)
    cta_tokens = ["评论", "关注", "私信", "收藏", "转发", "点击", "领取", "报名", "下单", "咨询", "试试"]
    cta_sentences = [u for u in units if any(token in u for token in cta_tokens)]

    if not units:
        return {
            "score": 2,
            "lines": ["- CTA策略：数据不足。", "- 行动指令：数据不足。"],
            "gaps": ["缺少ASR，无法识别CTA"],
            "evidence": "分句为空",
        }

    if not cta_sentences:
        return {
            "score": 2,
            "lines": ["- CTA策略：未检测到明确行动号召。", "- 行动指令：建议补一句“评论区/私信领取”。"],
            "gaps": ["补充单一明确CTA，避免只有信息陈述"],
            "evidence": "cta_sentences=0",
        }

    primary_cta = cta_sentences[-1]
    cta_types = []
    if any(k in asr for k in ["评论", "点赞", "收藏", "转发", "关注"]):
        cta_types.append("互动型")
    if any(k in asr for k in ["私信", "领取", "链接", "资料"]):
        cta_types.append("线索型")
    if any(k in asr for k in ["下单", "报名", "咨询", "购买"]):
        cta_types.append("转化型")

    lines = [
        f"- CTA类型：{'、'.join(cta_types) if cta_types else '互动型（弱）'}。",
        f"- 关键动作句：{primary_cta}",
        f"- CTA密度：{len(cta_sentences)}/{len(units)} 句。",
    ]

    return {
        "score": _score_from_hits(len(cta_types) + int(len(cta_sentences) > 0), full_score_hits=3),
        "lines": lines,
        "gaps": [] if len(cta_types) > 0 else ["补充线索型或转化型CTA，提高商业闭环"],
        "evidence": f"cta_types={cta_types}, cta_count={len(cta_sentences)}",
    }


def _build_summary_module(results: Dict[str, Dict[str, Any]]) -> Dict[str, Any]:
    ordered = ["选题", "文风", "Hook", "结构", "CTA"]
    scored = [(name, results[name]["score"]) for name in ordered]
    avg_score = round(sum(score for _, score in scored) / max(1, len(scored)), 2)
    weakest = sorted(scored, key=lambda x: x[1])[:2]

    if avg_score >= 4.2:
        verdict = "可直接复用"
    elif avg_score >= 3.4:
        verdict = "可用，但需小幅优化"
    else:
        verdict = "需重写关键模块后再投放"

    suggestions = []
    for name, _ in weakest:
        gaps = results[name].get("gaps") or []
        if gaps:
            suggestions.append(f"- [{name}] {gaps[0]}")
    if not suggestions:
        suggestions = ["- 保持当前结构，持续做A/B测试验证Hook与CTA。"]

    return {
        "score": int(round(avg_score)),
        "lines": [
            f"- 结论：综合评分 {avg_score}/5，判定为“{verdict}”。",
            "- 建议：",
            *suggestions[:3],
        ],
        "gaps": [],
        "evidence": f"scores={dict(scored)}",
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
        "digg": digg,
        "comment": comment,
        "collect": collect,
        "share": share,
    }



def _build_output_path(
    *,
    card_root: str,
    platform: str,
    card_type: str,
    material: bool,
    payload: Dict[str, Any],
    now: dt.datetime,
    sample_author: Optional[str],
    storage_config: Optional[Dict[str, Any]],
) -> Dict[str, str]:
    author_slug = _pick_author_slug(payload, author_hint=sample_author)
    title_slug = _pick_title_slug(payload)
    target_type = "material" if material else card_type

    path, route_parts = build_card_output_path(
        card_root=card_root,
        platform=platform,
        card_type=target_type,
        author_slug=author_slug,
        title_slug=title_slug,
        year=now.strftime("%Y"),
        year_month=now.strftime("%Y-%m"),
        timestamp=now.strftime("%Y%m%d-%H%M%S"),
        storage_config=storage_config,
    )
    return {
        "path": path,
        "route_parts": route_parts,
        "author_slug": author_slug,
        "title_slug": title_slug,
        "target_type": target_type,
    }


def _render_markdown(
    *,
    card_id: str,
    card_type: str,
    fields: Dict[str, Any],
    generated_at: str,
) -> str:
    author_name = fields.get("author") or fields.get("unique_id") or fields.get("sec_uid") or "未知作者"
    title = fields.get("title") or "（标题缺失）"
    metrics_line = (
        f"赞 {fields['digg_count']} / 评 {fields['comment_count']} / "
        f"藏 {fields['collect_count']} / 转 {fields['share_count']}"
    )
    analysis_sections = build_analysis_sections(fields)
    creative_modules = analysis_sections.get("modules", {})
    insight_lines = analysis_sections.get("insight", ["数据不足"])
    extract_trace_json = json.dumps(fields.get("extract_trace", []), ensure_ascii=False, indent=2)

    fm = {
        "card_id": card_id,
        "card_type": card_type,
        "platform": fields.get("platform"),
        "generated_at": generated_at,
        "updated_at": generated_at,
        "title": fields.get("title"),
        "platform_work_id": fields.get("platform_work_id"),
        "author": fields.get("author"),
        "unique_id": fields.get("unique_id"),
        "sec_uid": fields.get("sec_uid"),
        "share_url": fields.get("share_url"),
        "source_url": fields.get("source_url"),
        "cover_image": fields.get("cover_image"),
        "video_down_url": fields.get("video_down_url"),
        "create_time_sec": fields.get("create_time_sec"),
        "duration_ms": fields.get("duration_ms"),
        "digg_count": fields.get("digg_count"),
        "comment_count": fields.get("comment_count"),
        "collect_count": fields.get("collect_count"),
        "share_count": fields.get("share_count"),
        "caption_status": fields.get("caption_status"),
        "tags": fields.get("tags", []),
        "content_type": fields.get("content_type"),
        "category": fields.get("category"),
    }

    frontmatter = ["---"]
    for key, value in fm.items():
        frontmatter.append(f"{key}: {json.dumps(value, ensure_ascii=False)}")
    frontmatter.append("---")

    lines = [
        *frontmatter,
        "",
        "## 基础信息",
        f"- 作者：{author_name}",
        f"- 标题：{title}",
        f"- 发布时间：{_format_create_time(fields.get('create_time_sec', 0))}",
        f"- 视频时长：{_format_duration(fields.get('duration_ms', 0))}",
        f"- 互动：{metrics_line}",
        f"- 链接：{fields.get('share_url') or '（未提供）'}",
    ]

    for heading in DEFAULT_MODULE_SECTIONS:
        lines.append("")
        lines.append(f"## {heading}")
        for item in creative_modules.get(heading, ["数据不足"]):
            lines.append(item)

    lines.append("")
    lines.append("## 洞察分析")
    for item in insight_lines:
        lines.append(item)

    lines.extend(
        [
            "",
            "## ASR_CLEAN",
            fields.get("asr_clean") or "（无可用 ASR 清洗文本）",
        ]
    )

    lines.extend(
        [
            "",
            "## 附录（ASR_RAW+trace）",
            "### ASR_RAW",
            fields.get("raw_content") or "（无可用 ASR 原文）",
            "",
            "### trace",
            f"- request_id: {fields.get('request_id')}",
            f"- asr_clean_contract: {fields.get('asr_clean_contract')}",
            f"- confidence: {fields.get('confidence')}",
            f"- error_reason: {fields.get('error_reason')}",
            "",
            "<details>",
            "<summary>extract_trace（点击展开）</summary>",
            "",
            "```json",
            extract_trace_json,
            "```",
            "",
            "</details>",
            "",
        ]
    )
    return "\n".join(lines)


def _write_file(path: str, content: str) -> None:
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(content)


def _resolve_card_root(card_root: Optional[str]) -> str:
    raw = (card_root or "").strip()
    if not raw:
        return resolve_default_card_root()

    candidate = Path(raw).expanduser()
    if not candidate.is_absolute():
        raise ValueError("card_root must be an absolute path")
    return str(candidate.resolve())


def write_benchmark_card(
    *,
    payload: Dict[str, Any],
    platform: str,
    card_type: str,
    card_root: Optional[str],
    collect_material: bool,
    sample_author: Optional[str] = None,
    content_kind: Optional[str] = None,
    storage_config: Optional[Dict[str, Any]] = None,
    force_card_type: bool = False,
) -> Dict[str, Any]:
    now = dt.datetime.now()
    generated_at = now.isoformat(timespec="seconds")

    payload_content_kind = normalize_text(payload.get("content_kind"))
    resolved_content_kind = normalize_text(content_kind) or payload_content_kind

    normalized_card_type = normalize_card_type(card_type)
    effective_card_type = resolve_effective_card_type(
        card_type=normalized_card_type,
        content_kind=resolved_content_kind,
        storage_config=storage_config,
        force_card_type=force_card_type,
    )
    fields = _extract_required_fields(payload, platform=platform)
    resolved_card_root = _resolve_card_root(card_root)

    primary_target = _build_output_path(
        card_root=resolved_card_root,
        platform=platform,
        card_type=effective_card_type,
        material=False,
        payload=payload,
        now=now,
        sample_author=sample_author,
        storage_config=storage_config,
    )
    primary_path = primary_target["path"]

    primary_card_id = os.path.basename(primary_path).replace(".md", "")
    primary_markdown = _render_markdown(
        card_id=primary_card_id,
        card_type=effective_card_type,
        fields=fields,
        generated_at=generated_at,
    )
    _write_file(primary_path, primary_markdown)

    material_path: Optional[str] = None
    material_route_parts: Optional[str] = None
    if collect_material:
        material_target = _build_output_path(
            card_root=resolved_card_root,
            platform=platform,
            card_type=effective_card_type,
            material=True,
            payload=payload,
            now=now,
            sample_author=sample_author,
            storage_config=storage_config,
        )
        material_path = material_target["path"]
        material_route_parts = material_target["route_parts"]
        material_card_id = os.path.basename(material_path).replace(".md", "")
        material_markdown = _render_markdown(
            card_id=material_card_id,
            card_type="material",
            fields=fields,
            generated_at=generated_at,
        )
        _write_file(material_path, material_markdown)

    return {
        "ok": True,
        "platform": platform,
        "card_type": effective_card_type,
        "requested_card_type": normalized_card_type,
        "force_card_type": bool(force_card_type),
        "content_kind": resolved_content_kind or None,
        "collect_material": collect_material,
        "primary_card_path": primary_path,
        "material_card_path": material_path,
        "routing": {
            "primary_route_parts": primary_target["route_parts"],
            "material_route_parts": material_route_parts,
            "storage_routes_configured": bool(isinstance(storage_config, dict) and isinstance(storage_config.get("storage_routes"), dict)),
        },
        "required_fields": fields,
    }


def _read_payload_from_input(input_json: str) -> Dict[str, Any]:
    if input_json == "-":
        raw = os.read(0, 1024 * 1024).decode("utf-8", errors="replace").strip()
        if not raw:
            return {}
        return json.loads(raw)
    return read_json_file(input_json)


def main() -> None:
    parser = argparse.ArgumentParser(description="Write benchmark card markdown to card root")
    parser.add_argument("--platform", required=True, help="Platform name, e.g. douyin or xiaohongshu")
    parser.add_argument("--card-type", choices=CARD_TYPES, default="work", help="Primary card type")
    parser.add_argument("--sample-author", default=None, help="Optional author slug override for author_sample_work")
    parser.add_argument("--content-kind", default=None, help="Optional workflow kind, e.g. single_video/author_home/author_analysis")
    parser.add_argument("--force-card-type", action="store_true", help="Force manual --card-type to override content_kind mapping")
    parser.add_argument("--card-root", default=None, help="Card root path (absolute); falls back to TIKOMNI_CARD_ROOT when omitted")
    parser.add_argument("--collect-material", action="store_true", help="Write extra CMAT card when explicitly requested")
    parser.add_argument(
        "--input-json",
        default="-",
        help="Input JSON path or '-' to read from stdin",
    )
    args = parser.parse_args()

    payload = _read_payload_from_input(args.input_json)
    result = write_benchmark_card(
        payload=payload,
        platform=args.platform,
        card_type=args.card_type,
        card_root=args.card_root,
        collect_material=args.collect_material,
        sample_author=args.sample_author,
        content_kind=args.content_kind,
        force_card_type=args.force_card_type,
    )
    write_json_stdout(result)


if __name__ == "__main__":
    main()
