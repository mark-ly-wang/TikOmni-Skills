#!/usr/bin/env python3
"""Generate skill-local API capability catalogs from the canonical TikOmni OpenAPI."""

from __future__ import annotations

import json
import os
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple
from urllib.error import URLError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
REMOTE_OPENAPI_URL = os.getenv(
    "TIKOMNI_OPENAPI_URL",
    "https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json",
)
DEFAULT_HEADERS = {
    "Accept": "application/json, text/plain, */*",
    # The published OpenAPI endpoint rejects some empty/default clients.
    "User-Agent": os.getenv("TIKOMNI_OPENAPI_USER_AGENT", "Mozilla/5.0"),
}
OUTPUTS = [
    ROOT / "skills" / "meta-capability" / "references" / "api-capability-catalog.md",
    ROOT / "skills" / "single-work-analysis" / "references" / "api-capability-catalog.md",
    ROOT / "skills" / "creator-analysis" / "references" / "api-capability-catalog.md",
]
HTTP_METHODS = ("get", "post", "put", "patch", "delete", "head", "options")
ABILITY_RULES: Sequence[Tuple[str, str]] = (
    ("comment", "评论"),
    ("reply", "评论回复"),
    ("search", "搜索"),
    ("suggest", "搜索"),
    ("hot", "热点/榜单"),
    ("billboard", "热点/榜单"),
    ("trend", "热点/榜单"),
    ("creator", "创作者"),
    ("author", "创作者"),
    ("user", "主页/账号"),
    ("profile", "主页/账号"),
    ("channel", "主页/账号"),
    ("home", "主页/账号"),
    ("video", "作品详情"),
    ("note", "作品详情"),
    ("post", "作品详情"),
    ("article", "作品详情"),
    ("detail", "详情"),
    ("download", "下载/媒体"),
    ("media", "下载/媒体"),
    ("audio", "音频/媒体"),
    ("subtitle", "字幕/转写"),
    ("transcription", "字幕/转写"),
    ("tts", "字幕/转写"),
    ("shop", "电商"),
    ("product", "电商"),
    ("goods", "电商"),
    ("ads", "广告"),
    ("ad_", "广告"),
    ("creative", "广告"),
    ("analytics", "数据分析"),
    ("insight", "数据分析"),
    ("report", "数据分析"),
    ("live", "直播"),
    ("stream", "直播"),
    ("hashtag", "话题"),
    ("challenge", "话题"),
    ("topic", "话题"),
    ("music", "音乐/音频"),
)


def fetch_remote_spec(url: str) -> Dict[str, Any]:
    request = Request(url, headers=DEFAULT_HEADERS)
    with urlopen(request, timeout=60) as response:
        payload = json.load(response)
    if not isinstance(payload, dict) or not isinstance(payload.get("paths"), dict):
        raise ValueError(f"远端 OpenAPI 结构无效: {url}")
    return payload


def load_spec() -> Tuple[Dict[str, Any], Dict[str, str]]:
    fetched_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
    try:
        return fetch_remote_spec(REMOTE_OPENAPI_URL), {
            "mode": "remote",
            "source": REMOTE_OPENAPI_URL,
            "fetched_at": fetched_at,
        }
    except (OSError, URLError, ValueError, json.JSONDecodeError) as exc:
        raise RuntimeError(f"远端 OpenAPI 拉取失败: {exc}") from exc


def resolve_ref(spec: Dict[str, Any], ref: str) -> Dict[str, Any]:
    node: Any = spec
    for part in ref.lstrip("#/").split("/"):
        node = node[part]
    return node if isinstance(node, dict) else {}


def deref_schema(spec: Dict[str, Any], schema: Optional[Dict[str, Any]], seen: Optional[set[str]] = None) -> Dict[str, Any]:
    if not isinstance(schema, dict):
        return {}
    seen = seen or set()
    if "$ref" in schema:
        ref = str(schema["$ref"])
        if ref in seen:
            return {}
        return deref_schema(spec, resolve_ref(spec, ref), seen | {ref})
    if "allOf" in schema:
        merged: Dict[str, Any] = {"type": "object", "properties": {}, "required": []}
        for item in schema.get("allOf", []):
            resolved = deref_schema(spec, item, seen)
            if not resolved:
                continue
            merged["properties"].update(resolved.get("properties") or {})
            merged["required"].extend(resolved.get("required") or [])
            if resolved.get("type") and not merged.get("type"):
                merged["type"] = resolved["type"]
        merged["required"] = sorted(set(merged["required"]))
        return merged
    if "oneOf" in schema or "anyOf" in schema:
        variants = schema.get("oneOf") or schema.get("anyOf") or []
        for item in variants:
            resolved = deref_schema(spec, item, seen)
            if resolved:
                return resolved
    return schema


def format_field(spec: Dict[str, Any], name: str, schema: Dict[str, Any], required: bool, depth: int = 1) -> str:
    resolved = deref_schema(spec, schema)
    marker = "*" if required else ""
    schema_type = str(resolved.get("type") or "")
    if schema_type == "array":
        items = deref_schema(spec, resolved.get("items") if isinstance(resolved.get("items"), dict) else {})
        if depth > 0 and items.get("type") == "object" and isinstance(items.get("properties"), dict):
            nested = summarize_schema_fields(spec, items, depth=depth - 1)
            return f"`{name}{marker}`[{nested}]"
        return f"`{name}{marker}`[]"
    if schema_type == "object":
        if depth > 0 and isinstance(resolved.get("properties"), dict) and resolved["properties"]:
            nested = summarize_schema_fields(spec, resolved, depth=depth - 1)
            return f"`{name}{marker}`{{{nested}}}"
        return f"`{name}{marker}`{{...}}"
    if schema_type:
        return f"`{name}{marker}`:{schema_type}"
    return f"`{name}{marker}`"


def summarize_schema_fields(spec: Dict[str, Any], schema: Dict[str, Any], depth: int = 1, limit: int = 8) -> str:
    resolved = deref_schema(spec, schema)
    properties = resolved.get("properties")
    if not isinstance(properties, dict) or not properties:
        return "动态对象"
    required = set(resolved.get("required") or [])
    fields: List[str] = []
    for index, (name, field_schema) in enumerate(properties.items()):
        if index >= limit:
            fields.append("...")
            break
        fields.append(format_field(spec, name, field_schema if isinstance(field_schema, dict) else {}, name in required, depth=depth))
    return ", ".join(fields)


def summarize_params(params: Sequence[Dict[str, Any]]) -> str:
    if not params:
        return "无"
    grouped: Dict[str, List[str]] = defaultdict(list)
    for param in params:
        if not isinstance(param, dict):
            continue
        name = str(param.get("name") or "").strip()
        if not name:
            continue
        location = str(param.get("in") or "query").strip()
        marker = "*" if param.get("required") else ""
        grouped[location].append(f"`{name}{marker}`")
    parts = [f"{location}: {', '.join(values)}" for location, values in grouped.items()]
    return "; ".join(parts) if parts else "无"


def summarize_request_body(spec: Dict[str, Any], request_body: Dict[str, Any]) -> str:
    if not isinstance(request_body, dict):
        return "无"
    content = request_body.get("content")
    if not isinstance(content, dict) or not content:
        return "无"
    media_type = "application/json" if "application/json" in content else next(iter(content.keys()))
    media_spec = content.get(media_type)
    if not isinstance(media_spec, dict):
        return media_type
    schema = media_spec.get("schema")
    if not isinstance(schema, dict):
        return media_type
    summary = summarize_schema_fields(spec, schema, depth=1)
    return f"{media_type}: {summary}"


def infer_abilities(path: str) -> List[str]:
    lowered = path.lower()
    abilities: List[str] = []
    for token, label in ABILITY_RULES:
        if token in lowered and label not in abilities:
            abilities.append(label)
    return abilities or ["通用能力"]


def collect_common_inputs(spec: Dict[str, Any], operations: Sequence[Tuple[str, str, Dict[str, Any]]]) -> str:
    counter: Counter[str] = Counter()
    for _, _, op in operations:
        for param in op.get("parameters", []):
            if isinstance(param, dict) and param.get("name"):
                counter[str(param["name"])] += 1
        request_body = op.get("requestBody")
        if not isinstance(request_body, dict):
            continue
        content = request_body.get("content")
        if not isinstance(content, dict) or not content:
            continue
        media_spec = content.get("application/json") or next(iter(content.values()))
        if not isinstance(media_spec, dict):
            continue
        schema = media_spec.get("schema")
        if not isinstance(schema, dict):
            continue
        resolved = deref_schema(spec, schema)
        for field_name in list((resolved.get("properties") or {}).keys())[:10]:
            counter[str(field_name)] += 1
    if not counter:
        return "无"
    return ", ".join(f"`{name}`" for name, _ in counter.most_common(10))


def iter_operations(spec: Dict[str, Any]) -> Iterable[Tuple[str, str, str, Dict[str, Any]]]:
    for path, methods in sorted((spec.get("paths") or {}).items()):
        if not isinstance(methods, dict):
            continue
        for method in HTTP_METHODS:
            op = methods.get(method)
            if isinstance(op, dict):
                tags = op.get("tags") or ["<untagged>"]
                tag = str(tags[0])
                yield tag, method.upper(), path, op


def build_markdown(spec: Dict[str, Any], source_meta: Dict[str, str]) -> str:
    tags_meta = {str(item.get("name")): item for item in spec.get("tags", []) if isinstance(item, dict) and item.get("name")}
    grouped: Dict[str, List[Tuple[str, str, Dict[str, Any]]]] = defaultdict(list)
    for tag, method, path, op in iter_operations(spec):
        grouped[tag].append((method, path, op))

    op_count = sum(len(items) for items in grouped.values())
    lines: List[str] = [
        "# TikOmni API 能力目录",
        "",
        "## 目录",
        "",
        "- [用途](#用途)",
        "- [统计](#统计)",
        "- [标签概览](#标签概览)",
        "- [完整路由目录](#完整路由目录)",
        "",
        "## 用途",
        "",
        "- 本文档由 TikOmni 在线 OpenAPI 自动生成，是当前 skill 的权威接口目录。",
        f"- 当前数据源：`{source_meta['mode']}`",
        f"- 来源：`{source_meta['source']}`",
        f"- 获取时间：`{source_meta['fetched_at']}`",
        "- 当技能需要判断“有哪些接口、该调哪个路由、要传哪些字段”时，先读本文档，再读各 skill 自己的平台 guide。",
        "- `*` 表示必填字段；`query/path/header/cookie` 表示参数位置；`application/json:` 后面是请求体顶层字段摘要。",
        "- 完整返回结构以 OpenAPI 原始 JSON 为准；各 skill 只需要把平台原始返回映射到自己的 contract 字段。",
        "",
        "## 统计",
        "",
        f"- 标签组数量：`{len(grouped)}`",
        f"- 路由数量：`{op_count}`",
        f"- 生成目标：`{len(OUTPUTS)}` 个 skill reference",
        "",
        "## 标签概览",
        "",
        "| Tag | Ops | 常见能力 | 常见入参 |",
        "| --- | ---: | --- | --- |",
    ]

    for tag in sorted(grouped):
        operations = grouped[tag]
        ability_counter: Counter[str] = Counter()
        for _, path, _ in operations:
            ability_counter.update(infer_abilities(path))
        top_abilities = " / ".join(label for label, _ in ability_counter.most_common(4)) or "通用能力"
        common_inputs = collect_common_inputs(spec, operations)
        lines.append(f"| `{tag}` | {len(operations)} | {top_abilities} | {common_inputs} |")

    lines.extend(["", "## 完整路由目录", ""])

    for tag in sorted(grouped):
        operations = grouped[tag]
        desc = str((tags_meta.get(tag) or {}).get("description") or "").strip().replace("\n", " ")
        lines.append(f"### `{tag}`")
        lines.append("")
        lines.append(f"- 路由数：`{len(operations)}`")
        if desc:
            lines.append(f"- 标签说明：{desc}")
        lines.append(f"- 常见入参：{collect_common_inputs(spec, operations)}")
        lines.append("")
        for method, path, op in operations:
            ability = " / ".join(infer_abilities(path))
            params = summarize_params(op.get("parameters") or [])
            body = summarize_request_body(spec, op.get("requestBody") or {})
            lines.append(f"- `{method} {path}`")
            lines.append(f"  能力：{ability}")
            lines.append(f"  入参：{params}")
            lines.append(f"  请求体：{body}")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    spec, source_meta = load_spec()
    markdown = build_markdown(spec, source_meta)
    for output_path in OUTPUTS:
        output_path.write_text(markdown, encoding="utf-8")
        print(output_path.relative_to(ROOT))


if __name__ == "__main__":
    main()
