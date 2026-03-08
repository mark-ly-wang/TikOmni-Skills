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
    "User-Agent": os.getenv("TIKOMNI_OPENAPI_USER_AGENT", "Mozilla/5.0"),
}
REFERENCE_ROOTS = [
    ROOT / "skills" / "meta-capability" / "references",
    ROOT / "skills" / "single-work-analysis" / "references",
    ROOT / "skills" / "creator-analysis" / "references",
]
INDEX_FILENAME = "api-capability-index.md"
TAGS_DIRNAME = "api-tags"
CONTRACTS_DIRNAME = "api-contracts"
SERVICE_GUIDES_DIRNAME = "service-guides"
ASR_FALLBACK_GUIDE_FILENAME = "asr-u2-u3-fallback.md"
HTTP_METHODS = ("get", "post", "put", "patch", "delete", "head", "options")
TAG_SECTION_FIELD_LIMIT = 12
TAG_SECTION_FIELD_DEPTH = 2
CONTRACT_SECTION_FIELD_LIMIT = 120
CONTRACT_SECTION_FIELD_DEPTH = 4
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


def deref_object(
    spec: Dict[str, Any],
    node: Optional[Dict[str, Any]],
    seen: Optional[set[str]] = None,
) -> Dict[str, Any]:
    if not isinstance(node, dict):
        return {}
    seen = seen or set()
    if "$ref" not in node:
        return node
    ref = str(node["$ref"])
    if ref in seen:
        return {}
    return deref_object(spec, resolve_ref(spec, ref), seen | {ref})


def deref_schema(
    spec: Dict[str, Any],
    schema: Optional[Dict[str, Any]],
    seen: Optional[set[str]] = None,
) -> Dict[str, Any]:
    resolved = deref_object(spec, schema, seen)
    if not resolved:
        return {}
    if "allOf" in resolved:
        merged: Dict[str, Any] = {"type": "", "properties": {}, "required": []}
        descriptions: List[str] = []
        for item in resolved.get("allOf", []):
            item_schema = deref_schema(spec, item, seen)
            if not item_schema:
                continue
            merged["properties"].update(item_schema.get("properties") or {})
            merged["required"].extend(item_schema.get("required") or [])
            if item_schema.get("type") and not merged.get("type"):
                merged["type"] = item_schema["type"]
            description = normalize_inline_text(item_schema.get("description"))
            if description:
                descriptions.append(description)
        merged["required"] = sorted(set(merged["required"]))
        if not merged["type"] and merged["properties"]:
            merged["type"] = "object"
        if descriptions:
            merged["description"] = " / ".join(dict.fromkeys(descriptions))
        return merged
    if "oneOf" in resolved or "anyOf" in resolved:
        variants = resolved.get("oneOf") or resolved.get("anyOf") or []
        resolved_variants: List[Dict[str, Any]] = []
        for item in variants:
            item_schema = deref_schema(spec, item, seen)
            if item_schema:
                resolved_variants.append(item_schema)
        for item_schema in resolved_variants:
            item_type = item_schema.get("type")
            if item_type in {"object", "array"} or isinstance(item_schema.get("properties"), dict):
                return item_schema
        for item_schema in resolved_variants:
            item_type = item_schema.get("type")
            if item_type != "null":
                return item_schema
        if resolved_variants:
            return resolved_variants[0]
    return resolved


def normalize_inline_text(value: Any) -> str:
    if value is None:
        return ""
    text = str(value).replace("\r\n", "\n").replace("\r", "\n")
    return re.sub(r"\s+", " ", text).strip()


def normalize_multiline_text(value: Any) -> str:
    if value is None:
        return ""
    text = str(value).replace("\r\n", "\n").replace("\r", "\n").strip()
    return "\n".join(line.rstrip() for line in text.splitlines()).strip()


def clip_text(text: str, limit: int) -> str:
    if len(text) <= limit:
        return text
    return text[: limit - 1].rstrip() + "…"


def markdown_escape(text: Any) -> str:
    normalized = normalize_inline_text(text)
    if not normalized:
        return "无"
    return normalized.replace("|", "\\|").replace("\n", "<br>")


def format_value(value: Any, limit: int = 120) -> str:
    if value in (None, "", [], {}):
        return ""
    if isinstance(value, str):
        rendered = value
    else:
        rendered = json.dumps(value, ensure_ascii=False)
    return clip_text(normalize_inline_text(rendered), limit)


def format_enum(values: Any, limit: int = 6) -> str:
    if not isinstance(values, list) or not values:
        return ""
    rendered = ", ".join(format_value(item, limit=24) for item in values[:limit])
    if len(values) > limit:
        rendered += ", ..."
    return f"enum[{rendered}]"


def first_non_empty(*values: Any) -> Any:
    for value in values:
        if value not in (None, "", [], {}):
            return value
    return None


def quote_block(text: str) -> List[str]:
    normalized = normalize_multiline_text(text)
    if not normalized:
        return []
    return [f"> {line}" if line else ">" for line in normalized.splitlines()]


def slugify_tag(tag: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", tag.lower()).strip("-")
    return slug or "untagged"


def slugify_text(text: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return slug or "item"


def tag_file_relpath(tag: str) -> str:
    return f"{TAGS_DIRNAME}/{slugify_tag(tag)}.md"


def contract_file_relpath(tag: str) -> str:
    return f"{CONTRACTS_DIRNAME}/{slugify_tag(tag)}.md"


def operation_anchor(method: str, path: str) -> str:
    return slugify_text(f"{method.lower()}-{path}")


def schema_type_name(spec: Dict[str, Any], schema: Optional[Dict[str, Any]]) -> str:
    resolved = deref_schema(spec, schema)
    if not resolved:
        return "未声明"
    raw_type = resolved.get("type")
    if isinstance(raw_type, list):
        rendered_types = [str(item).strip() for item in raw_type if str(item).strip()]
        schema_type = " | ".join(rendered_types)
    else:
        schema_type = str(raw_type or "").strip()
    if not schema_type and isinstance(resolved.get("properties"), dict):
        schema_type = "object"
    if not schema_type and isinstance(resolved.get("items"), dict):
        schema_type = "array"

    if schema_type == "array":
        items = resolved.get("items") if isinstance(resolved.get("items"), dict) else {}
        item_type = schema_type_name(spec, items)
        base = f"array<{item_type}>"
    elif schema_type:
        base = schema_type
    else:
        base = "动态对象"

    schema_format = normalize_inline_text(resolved.get("format"))
    if schema_format:
        base = f"{base}({schema_format})"

    enum_text = format_enum(resolved.get("enum"))
    if enum_text:
        base = f"{base} {enum_text}"
    return base


def format_field(spec: Dict[str, Any], name: str, schema: Dict[str, Any], required: bool, depth: int = 1) -> str:
    resolved = deref_schema(spec, schema)
    marker = "*" if required else ""
    raw_type = resolved.get("type")
    if isinstance(raw_type, list):
        schema_type = " | ".join(str(item).strip() for item in raw_type if str(item).strip())
    else:
        schema_type = str(raw_type or "")
    if schema_type == "array":
        items = deref_schema(spec, resolved.get("items") if isinstance(resolved.get("items"), dict) else {})
        if depth > 0 and items.get("type") == "object" and isinstance(items.get("properties"), dict):
            nested = summarize_schema_fields(spec, items, depth=depth - 1)
            return f"`{name}{marker}`[{nested}]"
        item_type = schema_type_name(spec, items)
        return f"`{name}{marker}`[{item_type}]"
    if schema_type == "object" or isinstance(resolved.get("properties"), dict):
        if depth > 0 and isinstance(resolved.get("properties"), dict) and resolved["properties"]:
            nested = summarize_schema_fields(spec, resolved, depth=depth - 1)
            return f"`{name}{marker}`{{{nested}}}"
        return f"`{name}{marker}`{{...}}"
    if schema_type:
        return f"`{name}{marker}`:{schema_type}"
    return f"`{name}{marker}`"


def summarize_schema_fields(
    spec: Dict[str, Any],
    schema: Dict[str, Any],
    depth: int = 1,
    limit: int = 8,
) -> str:
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
        schema_dict = field_schema if isinstance(field_schema, dict) else {}
        fields.append(format_field(spec, name, schema_dict, name in required, depth=depth))
    return ", ".join(fields)


def summarize_schema(
    spec: Dict[str, Any],
    schema: Optional[Dict[str, Any]],
    depth: int = 1,
    limit: int = 8,
) -> str:
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
        return f"[{schema_type_name(spec, items)}]"
    return schema_type_name(spec, resolved)


def describe_security_scheme(spec: Dict[str, Any], scheme_name: str) -> str:
    security_schemes = (spec.get("components") or {}).get("securitySchemes") or {}
    scheme = deref_object(spec, security_schemes.get(scheme_name) if isinstance(security_schemes.get(scheme_name), dict) else {})
    scheme_type = str(scheme.get("type") or "").strip()
    scheme_in = str(scheme.get("in") or "").strip()
    param_name = str(scheme.get("name") or "").strip()
    http_scheme = str(scheme.get("scheme") or "").strip()
    description = normalize_inline_text(scheme.get("description"))

    if scheme_type == "http" and http_scheme.lower() == "bearer":
        detail = "请求头 `Authorization: Bearer {token}`"
        if "cookie" in description.lower() and "authorization" in description.lower():
            detail += "；文档说明还可用 Cookie `Authorization` 兜底"
        return f"{detail}（`{scheme_name}`）"

    if scheme_type == "apiKey":
        location = scheme_in or "query"
        target = f"`{param_name}`" if param_name else "`<unnamed>`"
        return f"{location} {target}（`{scheme_name}`）"

    if scheme_type:
        detail = f"{scheme_type}"
        if http_scheme:
            detail = f"{detail}:{http_scheme}"
        return f"{detail}（`{scheme_name}`）"
    return f"`{scheme_name}`"


def effective_security(spec: Dict[str, Any], op: Dict[str, Any]) -> List[Dict[str, Any]]:
    security = op.get("security")
    if security is None:
        security = spec.get("security")
    return security if isinstance(security, list) else []


def summarize_security(spec: Dict[str, Any], op: Dict[str, Any]) -> str:
    requirements = effective_security(spec, op)
    if not requirements:
        return "无认证要求"

    options: List[str] = []
    for requirement in requirements:
        if not isinstance(requirement, dict):
            continue
        if not requirement:
            options.append("无认证要求")
            continue
        parts = [describe_security_scheme(spec, scheme_name) for scheme_name in requirement.keys()]
        if parts:
            options.append(" + ".join(parts))
    unique_options = list(dict.fromkeys(options))
    return " 或 ".join(unique_options) if unique_options else "无认证要求"


def compact_security_label(summary: str) -> str:
    if "Authorization: Bearer {token}" in summary:
        return "请求头 `Authorization` Bearer"
    return summary


def resolve_parameter(spec: Dict[str, Any], param: Dict[str, Any]) -> Dict[str, Any]:
    return deref_object(spec, param)


def merge_parameters(
    spec: Dict[str, Any],
    path_params: Sequence[Dict[str, Any]],
    op_params: Sequence[Dict[str, Any]],
) -> List[Dict[str, Any]]:
    merged: Dict[Tuple[str, str], Dict[str, Any]] = {}
    order: List[Tuple[str, str]] = []
    for source in (path_params, op_params):
        for param in source:
            if not isinstance(param, dict):
                continue
            resolved = resolve_parameter(spec, param)
            name = str(resolved.get("name") or "").strip()
            location = str(resolved.get("in") or "query").strip()
            if not name:
                continue
            key = (name, location)
            if key not in merged:
                order.append(key)
            merged[key] = resolved
    return [merged[key] for key in order]


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


def extract_parameter_rows(spec: Dict[str, Any], params: Sequence[Dict[str, Any]]) -> List[Dict[str, str]]:
    rows: List[Dict[str, str]] = []
    for param in params:
        if not isinstance(param, dict):
            continue
        resolved = resolve_parameter(spec, param)
        name = str(resolved.get("name") or "").strip()
        if not name:
            continue
        schema = resolved.get("schema") if isinstance(resolved.get("schema"), dict) else {}
        rows.append(
            {
                "字段": name,
                "位置": str(resolved.get("in") or "query"),
                "类型": schema_type_name(spec, schema),
                "必填": "是" if resolved.get("required") else "否",
                "说明": normalize_inline_text(resolved.get("description") or schema.get("description")) or "无",
                "默认值": format_value(schema.get("default")),
                "示例": format_value(first_non_empty(resolved.get("example"), schema.get("example"))),
                "枚举": format_enum(schema.get("enum")) or "无",
            }
        )
    return rows


def collect_schema_rows(
    spec: Dict[str, Any],
    schema: Optional[Dict[str, Any]],
    *,
    max_depth: int,
    max_rows: int,
) -> Tuple[List[Dict[str, str]], bool]:
    rows: List[Dict[str, str]] = []
    truncated = False

    def push_row(path: str, field_schema: Dict[str, Any], required: bool, depth: int) -> None:
        nonlocal truncated
        if truncated:
            return
        if len(rows) >= max_rows:
            truncated = True
            return

        resolved = deref_schema(spec, field_schema)
        description = normalize_inline_text(field_schema.get("description") or resolved.get("description")) or "无"
        rows.append(
            {
                "字段": path,
                "类型": schema_type_name(spec, field_schema),
                "必填": "是" if required else "否",
                "说明": description,
                "默认值": format_value(first_non_empty(field_schema.get("default"), resolved.get("default"))),
                "示例": format_value(first_non_empty(field_schema.get("example"), resolved.get("example"))),
                "枚举": format_enum(first_non_empty(field_schema.get("enum"), resolved.get("enum"))) or "无",
            }
        )

        if depth >= max_depth:
            return

        raw_type = resolved.get("type")
        if isinstance(raw_type, list):
            if "object" in raw_type:
                schema_type = "object"
            elif "array" in raw_type:
                schema_type = "array"
            else:
                schema_type = str(raw_type[0]).strip() if raw_type else ""
        else:
            schema_type = str(raw_type or "").strip()
        if not schema_type and isinstance(resolved.get("properties"), dict):
            schema_type = "object"
        if schema_type == "object":
            properties = resolved.get("properties") or {}
            required_fields = set(resolved.get("required") or [])
            for child_name, child_schema in properties.items():
                if not isinstance(child_schema, dict):
                    continue
                child_path = f"{path}.{child_name}"
                push_row(child_path, child_schema, child_name in required_fields, depth + 1)
        elif schema_type == "array":
            items = resolved.get("items") if isinstance(resolved.get("items"), dict) else {}
            item_schema = deref_schema(spec, items)
            item_type = str(item_schema.get("type") or "").strip()
            if not item_type and isinstance(item_schema.get("properties"), dict):
                item_type = "object"
            if item_type in {"object", "array"}:
                push_row(f"{path}[]", items, True, depth + 1)

    root = deref_schema(spec, schema)
    if not root:
        return rows, truncated

    raw_root_type = root.get("type")
    if isinstance(raw_root_type, list):
        if "object" in raw_root_type:
            root_type = "object"
        elif "array" in raw_root_type:
            root_type = "array"
        else:
            root_type = str(raw_root_type[0]).strip() if raw_root_type else ""
    else:
        root_type = str(raw_root_type or "").strip()
    if not root_type and isinstance(root.get("properties"), dict):
        root_type = "object"
    if root_type == "object":
        properties = root.get("properties") or {}
        required_fields = set(root.get("required") or [])
        for name, field_schema in properties.items():
            if not isinstance(field_schema, dict):
                continue
            push_row(name, field_schema, name in required_fields, depth=1)
    elif root_type == "array":
        push_row("[]", root, True, depth=1)
    else:
        push_row("value", root, True, depth=1)

    return rows, truncated


def pick_media_entries(content: Any) -> List[Tuple[str, Dict[str, Any]]]:
    if not isinstance(content, dict) or not content:
        return []
    ordered_keys = ["application/json"] if "application/json" in content else []
    ordered_keys.extend(sorted(key for key in content.keys() if key != "application/json"))
    entries: List[Tuple[str, Dict[str, Any]]] = []
    for media_type in ordered_keys:
        media_spec = content.get(media_type)
        entries.append((media_type, media_spec if isinstance(media_spec, dict) else {}))
    return entries


def summarize_request_body(spec: Dict[str, Any], request_body: Dict[str, Any]) -> str:
    resolved_body = deref_object(spec, request_body)
    if not resolved_body:
        return "无"
    entries = pick_media_entries(resolved_body.get("content"))
    if not entries:
        return "无"
    media_type, media_spec = entries[0]
    schema = media_spec.get("schema")
    if not isinstance(schema, dict):
        return media_type
    return f"{media_type}: {summarize_schema(spec, schema, depth=1)}"


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


def pick_success_response(spec: Dict[str, Any], responses: Any) -> Tuple[str, Dict[str, Any]]:
    if not isinstance(responses, dict) or not responses:
        return "", {}
    success_codes = [code for code in responses.keys() if code == "default" or (isinstance(code, str) and code.startswith("2"))]
    if not success_codes:
        return "", {}
    chosen_code = sorted((str(code) for code in success_codes), key=response_sort_key)[0]
    response = responses.get(chosen_code)
    return chosen_code, deref_object(spec, response if isinstance(response, dict) else {})


def summarize_success_response(spec: Dict[str, Any], responses: Any) -> str:
    chosen_code, chosen_response = pick_success_response(spec, responses)
    if not chosen_code:
        return "无成功响应声明"
    if not chosen_response:
        return f"{chosen_code}: 无结构声明"
    entries = pick_media_entries(chosen_response.get("content"))
    if not entries:
        return f"{chosen_code}: 无响应体"
    media_type, media_spec = entries[0]
    schema = media_spec.get("schema")
    if not isinstance(schema, dict):
        return f"{chosen_code} {media_type}"
    summary = summarize_schema(spec, schema, depth=1)
    return f"{chosen_code} {media_type}: {summary}"


def collect_content_sections(
    spec: Dict[str, Any],
    content: Any,
    *,
    max_depth: int,
    max_rows: int,
) -> List[Dict[str, Any]]:
    sections: List[Dict[str, Any]] = []
    for media_type, media_spec in pick_media_entries(content):
        resolved_media = deref_object(spec, media_spec)
        schema = resolved_media.get("schema")
        summary = summarize_schema(spec, schema if isinstance(schema, dict) else None, depth=1)
        rows, truncated = collect_schema_rows(
            spec,
            schema if isinstance(schema, dict) else None,
            max_depth=max_depth,
            max_rows=max_rows,
        )
        sections.append(
            {
                "media_type": media_type,
                "summary": summary,
                "rows": rows,
                "truncated": truncated,
            }
        )
    return sections


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
        request_body = deref_object(spec, op.get("requestBody") if isinstance(op.get("requestBody"), dict) else {})
        if not request_body:
            continue
        entries = pick_media_entries(request_body.get("content"))
        if not entries:
            continue
        _, media_spec = entries[0]
        schema = media_spec.get("schema")
        if not isinstance(schema, dict):
            continue
        resolved = deref_schema(spec, schema)
        for field_name in list((resolved.get("properties") or {}).keys())[:10]:
            counter[str(field_name)] += 1
    if not counter:
        return "无"
    return ", ".join(f"`{name}`" for name, _ in counter.most_common(10))


def collect_common_security(spec: Dict[str, Any], operations: Sequence[Tuple[str, str, Dict[str, Any]]]) -> str:
    counter: Counter[str] = Counter()
    for _, _, op in operations:
        counter[summarize_security(spec, op)] += 1
    if not counter:
        return "无认证要求"
    return " / ".join(compact_security_label(summary) for summary, _ in counter.most_common(2))


def render_markdown_table(
    headers: Sequence[str],
    rows: Sequence[Dict[str, str]],
    *,
    clip_limits: Optional[Dict[str, int]] = None,
) -> List[str]:
    clip_limits = clip_limits or {}
    lines = [
        f"| {' | '.join(headers)} |",
        f"| {' | '.join('---' for _ in headers)} |",
    ]
    for row in rows:
        rendered_cells: List[str] = []
        for header in headers:
            value = row.get(header, "") or "无"
            if header in clip_limits:
                value = clip_text(value, clip_limits[header])
            rendered_cells.append(markdown_escape(value))
        lines.append(f"| {' | '.join(rendered_cells)} |")
    return lines


def render_parameter_section(
    spec: Dict[str, Any],
    params: Sequence[Dict[str, Any]],
    *,
    detailed: bool,
) -> List[str]:
    rows = extract_parameter_rows(spec, params)
    lines = ["#### 参数", ""]
    if not rows:
        lines.extend(["无", ""])
        return lines

    headers = ["字段", "位置", "类型", "必填", "说明"]
    clip_limits = {"说明": 120}
    if detailed:
        headers.extend(["默认值", "示例", "枚举"])
        clip_limits = {"说明": 180, "默认值": 80, "示例": 80, "枚举": 80}
    lines.extend(render_markdown_table(headers, rows, clip_limits=clip_limits))
    lines.append("")
    return lines


def render_request_body_section(
    spec: Dict[str, Any],
    request_body: Dict[str, Any],
    *,
    detailed: bool,
) -> List[str]:
    resolved_body = deref_object(spec, request_body)
    lines = ["#### 请求体", ""]
    if not resolved_body:
        lines.extend(["无", ""])
        return lines

    lines.append(f"- required：{'是' if resolved_body.get('required') else '否'}")
    lines.append("")
    sections = collect_content_sections(
        spec,
        resolved_body.get("content"),
        max_depth=CONTRACT_SECTION_FIELD_DEPTH if detailed else TAG_SECTION_FIELD_DEPTH,
        max_rows=CONTRACT_SECTION_FIELD_LIMIT if detailed else TAG_SECTION_FIELD_LIMIT,
    )
    if not sections:
        lines.extend(["无结构声明", ""])
        return lines

    headers = ["字段", "类型", "必填", "说明"]
    clip_limits = {"说明": 120}
    if detailed:
        headers.extend(["默认值", "示例", "枚举"])
        clip_limits = {"说明": 180, "默认值": 80, "示例": 80, "枚举": 80}

    for section in sections:
        lines.append(f"##### `{section['media_type']}`")
        lines.append("")
        lines.append(f"- Schema 摘要：{section['summary']}")
        lines.append("")
        if section["rows"]:
            lines.extend(render_markdown_table(headers, section["rows"], clip_limits=clip_limits))
            lines.append("")
        else:
            lines.extend(["无字段表", ""])
        if section["truncated"]:
            lines.append(
                f"- 字段已截断：当前层仅展示前 `{CONTRACT_SECTION_FIELD_LIMIT if detailed else TAG_SECTION_FIELD_LIMIT}` 行。"
            )
            lines.append("")
    return lines


def render_success_response_section(
    spec: Dict[str, Any],
    responses: Any,
    *,
    detailed: bool,
) -> List[str]:
    status_code, response = pick_success_response(spec, responses)
    lines = ["#### 成功响应", ""]
    if not status_code:
        lines.extend(["无成功响应声明", ""])
        return lines
    if not response:
        lines.extend([f"`{status_code}`：无结构声明", ""])
        return lines

    sections = collect_content_sections(
        spec,
        response.get("content"),
        max_depth=CONTRACT_SECTION_FIELD_DEPTH if detailed else TAG_SECTION_FIELD_DEPTH,
        max_rows=CONTRACT_SECTION_FIELD_LIMIT if detailed else TAG_SECTION_FIELD_LIMIT,
    )
    if not sections:
        lines.extend([f"`{status_code}`：无响应体", ""])
        return lines

    headers = ["字段", "类型", "必填", "说明"]
    clip_limits = {"说明": 120}
    if detailed:
        headers.extend(["默认值", "示例", "枚举"])
        clip_limits = {"说明": 180, "默认值": 80, "示例": 80, "枚举": 80}

    for section in sections:
        lines.append(f"##### `{status_code} {section['media_type']}`")
        lines.append("")
        lines.append(f"- Schema 摘要：{section['summary']}")
        lines.append("")
        if section["rows"]:
            lines.extend(render_markdown_table(headers, section["rows"], clip_limits=clip_limits))
            lines.append("")
        else:
            lines.extend(["无字段表", ""])
        if section["truncated"]:
            lines.append(
                f"- 字段已截断：当前层仅展示前 `{CONTRACT_SECTION_FIELD_LIMIT if detailed else TAG_SECTION_FIELD_LIMIT}` 行。"
            )
            lines.append("")
    return lines


def iter_operations(spec: Dict[str, Any]) -> Iterable[Tuple[str, str, str, Dict[str, Any]]]:
    for path, path_item in sorted((spec.get("paths") or {}).items()):
        if not isinstance(path_item, dict):
            continue
        path_params = path_item.get("parameters") if isinstance(path_item.get("parameters"), list) else []
        for method in HTTP_METHODS:
            raw_op = path_item.get(method)
            if not isinstance(raw_op, dict):
                continue
            op = dict(deref_object(spec, raw_op))
            op["parameters"] = merge_parameters(
                spec,
                path_params if isinstance(path_params, list) else [],
                op.get("parameters") if isinstance(op.get("parameters"), list) else [],
            )
            if isinstance(op.get("requestBody"), dict):
                op["requestBody"] = deref_object(spec, op["requestBody"])
            resolved_responses: Dict[str, Any] = {}
            for code, response in (op.get("responses") or {}).items():
                resolved_responses[str(code)] = deref_object(spec, response if isinstance(response, dict) else {})
            op["responses"] = resolved_responses
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
    _ = tags_meta
    op_count = sum(len(items) for items in grouped.values())
    global_security = summarize_security(spec, {})
    lines: List[str] = [
        "# TikOmni API 能力索引",
        "",
        "## 用途",
        "",
        "- 本文档是自动生成的轻量入口，用来先锁定 tag、能力和认证方式。",
        f"- 当前数据源：`{source_meta['mode']}`",
        f"- 来源：`{source_meta['source']}`",
        f"- 获取时间：`{source_meta['fetched_at']}`",
        "- route 选择先读这里；当需要字段说明、默认值、示例或完整响应结构时，再进入 `api-tags/` 与 `api-contracts/`。",
        "- 涉及 ASR 超时、公网 URL 不可读、U3 媒体中转时，再读 `service-guides/asr-u2-u3-fallback.md`。",
        "",
        "## 全局认证",
        "",
        f"- 默认认证：{global_security}",
        "- 如果个别 route 覆盖或关闭了默认认证，以对应 `api-tags/` 与 `api-contracts/` 条目为准。",
        "",
        "## 读取顺序",
        "",
        "1. 先按平台和对象类型选 tag。",
        "2. 再打开对应 `api-tags/<tag>.md` 看路由摘要、认证方式和关键字段。",
        "3. 如果需要精确字段说明、默认值、示例或成功响应结构，再打开 `api-contracts/<tag>.md`。",
        "4. 如果任务涉及音频转写、90 秒软观察或 120 秒（2 分钟）硬 fallback，再读 U2/U3 组合 guide。",
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
        "| Tag | 文件 | 契约 | Ops | 认证 | 常见能力 | 常见入参 |",
        "| --- | --- | --- | ---: | --- | --- | --- |",
    ]

    for tag in sorted(grouped):
        operations = grouped[tag]
        ability_counter: Counter[str] = Counter()
        for _, path, _ in operations:
            ability_counter.update(infer_abilities(path))
        top_abilities = " / ".join(label for label, _ in ability_counter.most_common(4)) or "通用能力"
        common_inputs = collect_common_inputs(spec, operations)
        auth = collect_common_security(spec, operations)
        file_link = f"[`{tag_file_relpath(tag)}`](./{tag_file_relpath(tag)})"
        contract_link = f"[`{contract_file_relpath(tag)}`](./{contract_file_relpath(tag)})"
        lines.append(f"| `{tag}` | {file_link} | {contract_link} | {len(operations)} | {auth} | {top_abilities} | {common_inputs} |")

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
    common_auth = collect_common_security(spec, operations)
    contract_link = contract_file_relpath(tag)

    lines: List[str] = [
        f"# {tag} 路由详情",
        "",
        f"- 回到索引：[`{INDEX_FILENAME}`](../{INDEX_FILENAME})",
        f"- 当前 tag 文件：`{tag_file_relpath(tag)}`",
        f"- 完整契约：[`{contract_link}`](../{contract_link})",
        f"- 数据源：`{source_meta['source']}`",
        f"- 获取时间：`{source_meta['fetched_at']}`",
        f"- 路由数：`{len(operations)}`",
        f"- 常见能力：{top_abilities}",
        f"- 默认认证：{common_auth}",
        f"- 常见入参：{collect_common_inputs(spec, operations)}",
    ]
    if desc:
        lines.append(f"- 标签说明：{desc}")

    if tag in {"ASR-API", "Media-Ingest-API"}:
        lines.append(f"- 相关组合 guide：[`{SERVICE_GUIDES_DIRNAME}/{ASR_FALLBACK_GUIDE_FILENAME}`](../{SERVICE_GUIDES_DIRNAME}/{ASR_FALLBACK_GUIDE_FILENAME})")

    lines.extend(["", "## 路由列表", ""])

    for method, path, op in operations:
        ability = " / ".join(infer_abilities(path))
        summary = normalize_inline_text(op.get("summary"))
        security = summarize_security(spec, op)
        operation_id = str(op.get("operationId") or "").strip()
        contract_anchor = operation_anchor(method, path)

        lines.append(f"### `{method} {path}`")
        lines.append("")
        if summary:
            lines.append(f"- 摘要：{summary}")
        lines.append(f"- 能力：{ability}")
        lines.append(f"- 认证：{security}")
        if operation_id:
            lines.append(f"- operationId：`{operation_id}`")
        lines.append(f"- 完整契约：[`{contract_link}#{contract_anchor}`](../{contract_link}#{contract_anchor})")
        lines.append("")
        lines.extend(render_parameter_section(spec, op.get("parameters") or [], detailed=False))
        lines.extend(render_request_body_section(spec, op.get("requestBody") or {}, detailed=False))
        lines.extend(render_success_response_section(spec, op.get("responses") or {}, detailed=False))

    return "\n".join(lines).rstrip() + "\n"


def build_contract_markdown(
    spec: Dict[str, Any],
    source_meta: Dict[str, str],
    tag: str,
    operations: List[Tuple[str, str, Dict[str, Any]]],
    tag_meta: Dict[str, Any],
) -> str:
    desc = normalize_inline_text(tag_meta.get("description"))
    common_auth = collect_common_security(spec, operations)
    lines: List[str] = [
        f"# {tag} 完整契约",
        "",
        f"- 回到索引：[`{INDEX_FILENAME}`](../{INDEX_FILENAME})",
        f"- 回到路由详情：[`{tag_file_relpath(tag)}`](../{tag_file_relpath(tag)})",
        f"- 当前契约文件：`{contract_file_relpath(tag)}`",
        f"- 数据源：`{source_meta['source']}`",
        f"- 获取时间：`{source_meta['fetched_at']}`",
        f"- 路由数：`{len(operations)}`",
        f"- 默认认证：{common_auth}",
        "- 使用方式：当需要精确的认证说明、参数描述、默认值、示例或成功响应字段时，再读本文件。",
    ]
    if desc:
        lines.append(f"- 标签说明：{desc}")

    lines.extend(["", "## 路由契约", ""])

    for method, path, op in operations:
        summary = normalize_inline_text(op.get("summary"))
        description = normalize_multiline_text(op.get("description"))
        security = summarize_security(spec, op)
        operation_id = str(op.get("operationId") or "").strip()
        anchor = operation_anchor(method, path)

        lines.append(f'<a id="{anchor}"></a>')
        lines.append(f"### `{method} {path}`")
        lines.append("")
        if summary:
            lines.append(f"- 摘要：{summary}")
        lines.append(f"- 能力：{' / '.join(infer_abilities(path))}")
        lines.append(f"- 认证：{security}")
        if operation_id:
            lines.append(f"- operationId：`{operation_id}`")
        lines.append("")

        if description:
            lines.append("#### 说明")
            lines.append("")
            lines.extend(quote_block(description))
            lines.append("")

        lines.extend(render_parameter_section(spec, op.get("parameters") or [], detailed=True))
        lines.extend(render_request_body_section(spec, op.get("requestBody") or {}, detailed=True))
        lines.extend(render_success_response_section(spec, op.get("responses") or {}, detailed=True))

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
        contract_relpath = contract_file_relpath(tag)
        lines.append(f"- Tag：[`{tag}`](../{tag_relpath})")
        lines.append(f"- Route：`{method.upper()} {path}`")
        lines.append(f"- 认证：{summarize_security(spec, op)}")
        lines.append(f"- 入参：{summarize_params(op.get('parameters') or [])}")
        lines.append(f"- 请求体：{summarize_request_body(spec, op.get('requestBody') or {})}")
        lines.append(f"- 成功响应：{summarize_success_response(spec, op.get('responses') or {})}")
        lines.append(
            f"- 完整契约：[`{contract_relpath}#{operation_anchor(method.upper(), path)}`](../{contract_relpath}#{operation_anchor(method.upper(), path)})"
        )
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
        contracts_dir = reference_root / CONTRACTS_DIRNAME
        service_guides_dir = reference_root / SERVICE_GUIDES_DIRNAME
        legacy_catalog_path = reference_root / "api-capability-catalog.md"

        if tags_dir.exists():
            shutil.rmtree(tags_dir)
        tags_dir.mkdir(parents=True, exist_ok=True)

        if contracts_dir.exists():
            shutil.rmtree(contracts_dir)
        contracts_dir.mkdir(parents=True, exist_ok=True)

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

            contract_markdown = build_contract_markdown(spec, source_meta, tag, operations, tags_meta.get(tag) or {})
            contract_path = reference_root / contract_file_relpath(tag)
            contract_path.write_text(contract_markdown, encoding="utf-8")
            written.append(contract_path)

    return written


def main() -> None:
    spec, source_meta = load_spec()
    grouped, tags_meta = group_operations(spec)
    written = write_outputs(spec, source_meta, grouped, tags_meta)
    for path in written:
        print(path.relative_to(ROOT))


if __name__ == "__main__":
    main()
