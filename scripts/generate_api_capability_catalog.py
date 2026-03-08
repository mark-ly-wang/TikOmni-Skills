#!/usr/bin/env python3
"""Generate skill-local API capability references from the canonical TikOmni OpenAPI."""

from __future__ import annotations

import json
import os
import re
import shutil
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
REFERENCE_ROOTS = [
    ROOT / "skills" / "meta-capability" / "references",
    ROOT / "skills" / "single-work-analysis" / "references",
    ROOT / "skills" / "creator-analysis" / "references",
]
INDEX_FILENAME = "api-capability-index.md"
TAGS_DIRNAME = "api-tags"
SERVICE_GUIDES_DIRNAME = "service-guides"
ASR_FALLBACK_GUIDE_FILENAME = "asr-u2-u3-fallback.md"
HTTP_METHODS = ("get", "post", "put", "patch", "delete", "head", "options")
ABILITY_RULES: Sequence[Tuple[str, str]] = (
    ("transcription", "ASR/字幕转写"),
    ("asr", "ASR/字幕转写"),
    ("subtitle", "字幕/转写"),
    ("upload", "媒体上传/公网URL"),
    ("ingest", "媒体上传/公网URL"),
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
SERVICE_GUIDE_ROUTES: Sequence[Tuple[str, str, str, str]] = (
    (
        "U2 提交 ASR 任务",
        "POST",
        "/api/u2/v1/services/audio/asr/transcription",
        "默认主路径。先用 U1 返回的无水印下载链接或下载链接直接提交 ASR，不允许先走 U3。",
    ),
    (
        "U2 轮询任务状态",
        "POST",
        "/api/u2/v1/tasks/{task_id}",
        "用于观察任务完成度。90 秒仍未完成时进入软观察，120 秒（2 分钟）仍无结果时触发 U3 fallback。",
    ),
    (
        "U3 申请上传/中转",
        "POST",
        "/api/u3/v1/uploads",
        "仅在 U2 超过 120 秒仍无结果时使用。它的目标是把私有或非公网可读源链接转成公网可读 URL。",
    ),
    (
        "U3 完成上传并获取公网 URL",
        "POST",
        "/api/u3/v1/uploads/{upload_id}/complete",
        "完成后应拿到公网可读 URL，再次回调 U2 ASR。若仍失败，则保留事实卡并返回 incomplete。",
    ),
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


def deref_schema(
    spec: Dict[str, Any],
    schema: Optional[Dict[str, Any]],
    seen: Optional[set[str]] = None,
) -> Dict[str, Any]:
    if not isinstance(schema, dict):
        return {}
    seen = seen or set()
    if "$ref" in schema:
        ref = str(schema["$ref"])
        if ref in seen:
            return {}
        return deref_schema(spec, resolve_ref(spec, ref), seen | {ref})
    if "allOf" in schema:
        merged: Dict[str, Any] = {"type": "", "properties": {}, "required": []}
        for item in schema.get("allOf", []):
            resolved = deref_schema(spec, item, seen)
            if not resolved:
                continue
            merged["properties"].update(resolved.get("properties") or {})
            merged["required"].extend(resolved.get("required") or [])
            if resolved.get("type") and not merged.get("type"):
                merged["type"] = resolved["type"]
        merged["required"] = sorted(set(merged["required"]))
        if not merged["type"] and merged["properties"]:
            merged["type"] = "object"
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
        item_type = str(items.get("type") or "").strip()
        return f"`{name}{marker}`[{item_type}]" if item_type else f"`{name}{marker}`[]"
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


def summarize_schema(spec: Dict[str, Any], schema: Optional[Dict[str, Any]], depth: int = 1, limit: int = 8) -> str:
    resolved = deref_schema(spec, schema)
    if not resolved:
        return "无结构声明"
    schema_type = str(resolved.get("type") or "").strip()
    if schema_type == "object" or isinstance(resolved.get("properties"), dict):
        return summarize_schema_fields(spec, resolved, depth=depth, limit=limit)
    if schema_type == "array":
        items = deref_schema(spec, resolved.get("items") if isinstance(resolved.get("items"), dict) else {})
        item_type = str(items.get("type") or "").strip()
        if item_type == "object" or isinstance(items.get("properties"), dict):
            nested = summarize_schema_fields(spec, items, depth=max(0, depth - 1), limit=limit)
            return f"[{nested}]"
        return f"[{item_type}]" if item_type else "[]"
    return schema_type or "动态对象"


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


def pick_media_entry(content: Any) -> Tuple[str, Dict[str, Any]]:
    if not isinstance(content, dict) or not content:
        return "无", {}
    media_type = "application/json" if "application/json" in content else next(iter(content.keys()))
    media_spec = content.get(media_type)
    return media_type, media_spec if isinstance(media_spec, dict) else {}


def summarize_request_body(spec: Dict[str, Any], request_body: Dict[str, Any]) -> str:
    if not isinstance(request_body, dict):
        return "无"
    media_type, media_spec = pick_media_entry(request_body.get("content"))
    if media_type == "无":
        return "无"
    schema = media_spec.get("schema")
    if not isinstance(schema, dict):
        return media_type
    summary = summarize_schema(spec, schema, depth=1)
    return f"{media_type}: {summary}"


def response_sort_key(status_code: str) -> Tuple[int, int]:
    if status_code == "200":
        return (0, 200)
    if status_code == "201":
        return (0, 201)
    if status_code == "202":
        return (0, 202)
    if status_code.isdigit() and status_code.startswith("2"):
        return (1, int(status_code))
    if status_code == "default":
        return (2, 999)
    return (3, 999)


def summarize_success_response(spec: Dict[str, Any], responses: Any) -> str:
    if not isinstance(responses, dict) or not responses:
        return "无"

    success_codes = [code for code in responses.keys() if code == "default" or (isinstance(code, str) and code.startswith("2"))]
    if not success_codes:
        return "无成功响应声明"

    chosen_code = sorted((str(code) for code in success_codes), key=response_sort_key)[0]
    chosen_response = responses.get(chosen_code)
    if not isinstance(chosen_response, dict):
        return f"{chosen_code}: 无结构声明"

    media_type, media_spec = pick_media_entry(chosen_response.get("content"))
    if media_type == "无":
        return f"{chosen_code}: 无响应体"

    schema = media_spec.get("schema")
    if not isinstance(schema, dict):
        return f"{chosen_code} {media_type}"

    summary = summarize_schema(spec, schema, depth=1)
    return f"{chosen_code} {media_type}: {summary}"


def infer_abilities(path: str) -> List[str]:
    lowered = path.lower()
    abilities: List[str] = []
    for token, label in ABILITY_RULES:
        if token == "ads" and re.search(r"(?:^|[/_-])ads(?:$|[/_-])", lowered) is None:
            continue
        if token == "ad_" and re.search(r"(?:^|[/_])ad_", lowered) is None:
            continue
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
        _, media_spec = pick_media_entry(request_body.get("content"))
        schema = media_spec.get("schema")
        if not isinstance(schema, dict):
            continue
        resolved = deref_schema(spec, schema)
        for field_name in list((resolved.get("properties") or {}).keys())[:10]:
            counter[str(field_name)] += 1
    if not counter:
        return "无"
    return ", ".join(f"`{name}`" for name, _ in counter.most_common(10))


def slugify_tag(tag: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", tag.lower()).strip("-")
    return slug or "untagged"


def tag_file_relpath(tag: str) -> str:
    return f"{TAGS_DIRNAME}/{slugify_tag(tag)}.md"


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


def group_operations(spec: Dict[str, Any]) -> Tuple[Dict[str, List[Tuple[str, str, Dict[str, Any]]]], Dict[str, Dict[str, Any]]]:
    tags_meta = {
        str(item.get("name")): item
        for item in spec.get("tags", [])
        if isinstance(item, dict) and item.get("name")
    }
    grouped: Dict[str, List[Tuple[str, str, Dict[str, Any]]]] = defaultdict(list)
    for tag, method, path, op in iter_operations(spec):
        grouped[tag].append((method, path, op))
    return grouped, tags_meta


def build_index_markdown(
    spec: Dict[str, Any],
    source_meta: Dict[str, str],
    grouped: Dict[str, List[Tuple[str, str, Dict[str, Any]]]],
    tags_meta: Dict[str, Dict[str, Any]],
) -> str:
    op_count = sum(len(items) for items in grouped.values())
    lines: List[str] = [
        "# TikOmni API 能力索引",
        "",
        "## 用途",
        "",
        "- 本文档是自动生成的轻量入口，不再承载全量 route 明细。",
        f"- 当前数据源：`{source_meta['mode']}`",
        f"- 来源：`{source_meta['source']}`",
        f"- 获取时间：`{source_meta['fetched_at']}`",
        "- 先在这里锁定平台 tag、能力类型和常见入参；需要具体 route 时再进入 `api-tags/`。",
        "- 涉及 ASR 超时、公网 URL 不可读、U3 媒体中转时，再读 `service-guides/asr-u2-u3-fallback.md`。",
        "",
        "## 读取顺序",
        "",
        "1. 先按平台和对象类型选 tag。",
        "2. 再打开对应 `api-tags/<tag>.md` 看 route、入参、请求体和成功响应摘要。",
        "3. 如果任务涉及音频转写、90 秒软观察或 120 秒（2 分钟）硬 fallback，再读 U2/U3 组合 guide。",
        "",
        "## 统计",
        "",
        f"- 标签组数量：`{len(grouped)}`",
        f"- 路由数量：`{op_count}`",
        f"- 生成目标：`{len(REFERENCE_ROOTS)}` 个 skill reference",
        "",
        "## 特殊链路",
        "",
        f"- ASR 与 U3 fallback：[`{SERVICE_GUIDES_DIRNAME}/{ASR_FALLBACK_GUIDE_FILENAME}`](./{SERVICE_GUIDES_DIRNAME}/{ASR_FALLBACK_GUIDE_FILENAME})",
        f"- ASR tag：[`{tag_file_relpath('ASR-API')}`](./{tag_file_relpath('ASR-API')})" if "ASR-API" in grouped else "- ASR tag：当前 OpenAPI 未声明 `ASR-API`。",
        f"- U3 媒体中转 tag：[`{tag_file_relpath('Media-Ingest-API')}`](./{tag_file_relpath('Media-Ingest-API')})" if "Media-Ingest-API" in grouped else "- U3 媒体中转 tag：当前 OpenAPI 未声明 `Media-Ingest-API`。",
        "",
        "## 标签概览",
        "",
        "| Tag | 文件 | Ops | 常见能力 | 常见入参 |",
        "| --- | --- | ---: | --- | --- |",
    ]

    for tag in sorted(grouped):
        operations = grouped[tag]
        ability_counter: Counter[str] = Counter()
        for _, path, _ in operations:
            ability_counter.update(infer_abilities(path))
        top_abilities = " / ".join(label for label, _ in ability_counter.most_common(4)) or "通用能力"
        common_inputs = collect_common_inputs(spec, operations)
        file_link = f"[`{tag_file_relpath(tag)}`](./{tag_file_relpath(tag)})"
        lines.append(f"| `{tag}` | {file_link} | {len(operations)} | {top_abilities} | {common_inputs} |")

    return "\n".join(lines).rstrip() + "\n"

def build_tag_markdown(
    spec: Dict[str, Any],
    source_meta: Dict[str, str],
    tag: str,
    operations: List[Tuple[str, str, Dict[str, Any]]],
    tag_meta: Dict[str, Any],
) -> str:
    ability_counter: Counter[str] = Counter()
    for _, path, _ in operations:
        ability_counter.update(infer_abilities(path))
    top_abilities = " / ".join(label for label, _ in ability_counter.most_common(6)) or "通用能力"
    desc = str(tag_meta.get("description") or "").strip().replace("\n", " ")

    lines: List[str] = [
        f"# {tag} 路由详情",
        "",
        f"- 回到索引：[`{INDEX_FILENAME}`](../{INDEX_FILENAME})",
        f"- 当前 tag 文件：`{tag_file_relpath(tag)}`",
        f"- 数据源：`{source_meta['source']}`",
        f"- 获取时间：`{source_meta['fetched_at']}`",
        f"- 路由数：`{len(operations)}`",
        f"- 常见能力：{top_abilities}",
        f"- 常见入参：{collect_common_inputs(spec, operations)}",
    ]
    if desc:
        lines.append(f"- 标签说明：{desc}")

    if tag in {"ASR-API", "Media-Ingest-API"}:
        lines.append(f"- 相关组合 guide：[`{SERVICE_GUIDES_DIRNAME}/{ASR_FALLBACK_GUIDE_FILENAME}`](../{SERVICE_GUIDES_DIRNAME}/{ASR_FALLBACK_GUIDE_FILENAME})")

    lines.extend(["", "## 路由列表", ""])

    for method, path, op in operations:
        ability = " / ".join(infer_abilities(path))
        params = summarize_params(op.get("parameters") or [])
        request_body = summarize_request_body(spec, op.get("requestBody") or {})
        success_response = summarize_success_response(spec, op.get("responses") or {})
        operation_id = str(op.get("operationId") or "").strip()

        lines.append(f"### `{method} {path}`")
        lines.append("")
        lines.append(f"- 能力：{ability}")
        lines.append(f"- 入参：{params}")
        lines.append(f"- 请求体：{request_body}")
        lines.append(f"- 成功响应：{success_response}")
        if operation_id:
            lines.append(f"- operationId：`{operation_id}`")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def build_operation_index(
    grouped: Dict[str, List[Tuple[str, str, Dict[str, Any]]]],
) -> Dict[Tuple[str, str], Tuple[str, Dict[str, Any]]]:
    index: Dict[Tuple[str, str], Tuple[str, Dict[str, Any]]] = {}
    for tag, operations in grouped.items():
        for method, path, op in operations:
            index[(method.upper(), path)] = (tag, op)
    return index


def build_asr_u2_u3_fallback_markdown(
    spec: Dict[str, Any],
    source_meta: Dict[str, str],
    grouped: Dict[str, List[Tuple[str, str, Dict[str, Any]]]],
) -> str:
    operation_index = build_operation_index(grouped)
    lines: List[str] = [
        "# U2 ASR 与 U3 公网 URL Fallback",
        "",
        "## 用途",
        "",
        "- 这个 guide 用于视频 ASR 主路径和超时 fallback，不用于文本作品。",
        "- 默认必须先走 U2 ASR；U3 只能作为 fallback，不允许直接绕过 U2。",
        "- 当 U1 详情接口返回的是无水印下载链接或下载链接，但该链接可能不是公网可读 URL 时，用本 guide 判断何时转入 U3。",
        f"- 数据源：`{source_meta['source']}`",
        f"- 获取时间：`{source_meta['fetched_at']}`",
        "",
        "## 固定策略",
        "",
        "1. 先调用 U1 详情接口，拿到 `video_download_url`、无水印下载链接或其他可直接下载媒体链接。",
        "2. 直接用该链接提交 U2 ASR，不允许默认先走 U3。",
        "3. 90 秒仍未返回完整结果，只进入软观察，不切换主路径。",
        "4. 120 秒（2 分钟）仍未返回结果或未返回完整结果，判定源链接大概率不是公网可读 URL，才允许进入 U3 fallback。",
        "5. U3 完成后必须拿公网可读 URL，再次提交 U2 ASR。",
        "6. 如果 U3 或二次 U2 仍失败，保留事实卡并返回 `incomplete`；不要伪造主文本或分析结论。",
        "",
        "## 场景补充",
        "",
        "- 单作品：对当前作品单独执行这条链路。",
        "- Creator 批量：只对 120 秒后仍未成功的子集走 U3 fallback，不要把整批已成功项重新上传。",
        "",
        "## 路由事实",
        "",
    ]

    for title, method, path, explanation in SERVICE_GUIDE_ROUTES:
        lines.append(f"### {title}")
        lines.append("")
        lines.append(f"- 说明：{explanation}")

        entry = operation_index.get((method.upper(), path))
        if entry is None:
            lines.append("- 当前 OpenAPI 未找到该 route。")
            lines.append("")
            continue

        tag, op = entry
        tag_relpath = tag_file_relpath(tag)
        lines.append(f"- Tag：[`{tag}`](../{tag_relpath})")
        lines.append(f"- Route：`{method.upper()} {path}`")
        lines.append(f"- 入参：{summarize_params(op.get('parameters') or [])}")
        lines.append(f"- 请求体：{summarize_request_body(spec, op.get('requestBody') or {})}")
        lines.append(f"- 成功响应：{summarize_success_response(spec, op.get('responses') or {})}")
        lines.append("")

    lines.extend(
        [
            "## 执行备注",
            "",
            "- 本 guide 只定义路由选择和 fallback 顺序，不替代各平台自己的 detail route 选择。",
            "- U1 来源 route 由平台决定，例如抖音/小红书的 detail route；本 guide 只要求优先使用它们返回的下载链接。",
            "- 如果平台已直接返回可用 `subtitle_raw`，优先直接映射为 `asr_raw`，不必再走 U2/U3。",
            "",
        ]
    )

    return "\n".join(lines).rstrip() + "\n"


def write_outputs(
    spec: Dict[str, Any],
    source_meta: Dict[str, str],
    grouped: Dict[str, List[Tuple[str, str, Dict[str, Any]]]],
    tags_meta: Dict[str, Dict[str, Any]],
) -> List[Path]:
    written: List[Path] = []
    index_markdown = build_index_markdown(spec, source_meta, grouped, tags_meta)
    asr_guide = build_asr_u2_u3_fallback_markdown(spec, source_meta, grouped)

    for reference_root in REFERENCE_ROOTS:
        tags_dir = reference_root / TAGS_DIRNAME
        service_guides_dir = reference_root / SERVICE_GUIDES_DIRNAME
        legacy_catalog_path = reference_root / "api-capability-catalog.md"

        if tags_dir.exists():
            shutil.rmtree(tags_dir)
        tags_dir.mkdir(parents=True, exist_ok=True)

        if service_guides_dir.exists():
            shutil.rmtree(service_guides_dir)
        service_guides_dir.mkdir(parents=True, exist_ok=True)

        index_path = reference_root / INDEX_FILENAME
        index_path.write_text(index_markdown, encoding="utf-8")
        written.append(index_path)

        if legacy_catalog_path.exists():
            legacy_catalog_path.unlink()

        asr_guide_path = service_guides_dir / ASR_FALLBACK_GUIDE_FILENAME
        asr_guide_path.write_text(asr_guide, encoding="utf-8")
        written.append(asr_guide_path)

        for tag in sorted(grouped):
            operations = grouped[tag]
            tag_markdown = build_tag_markdown(spec, source_meta, tag, operations, tags_meta.get(tag) or {})
            tag_path = reference_root / tag_file_relpath(tag)
            tag_path.write_text(tag_markdown, encoding="utf-8")
            written.append(tag_path)

    return written


def main() -> None:
    spec, source_meta = load_spec()
    grouped, tags_meta = group_operations(spec)
    written = write_outputs(spec, source_meta, grouped, tags_meta)
    for path in written:
        print(path.relative_to(ROOT))


if __name__ == "__main__":
    main()
