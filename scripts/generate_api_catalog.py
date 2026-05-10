#!/usr/bin/env python3
"""Generate the social-media-crawl API-only routing catalog."""

from __future__ import annotations

import hashlib
import json
import os
import re
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = ROOT / "skills" / "social-media-crawl"
CATALOG_ROOT = SKILL_ROOT / "references" / "api-catalog"
REMOTE_OPENAPI_URL = os.getenv(
    "TIKOMNI_OPENAPI_URL",
    "https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json",
)
LOCAL_OPENAPI_FILE = os.getenv("TIKOMNI_OPENAPI_FILE", "").strip()
HTTP_METHODS = ("get", "post", "put", "patch", "delete", "head", "options")

PLATFORM_ALIASES: Dict[str, List[str]] = {
    "bilibili": ["bilibili", "b站", "哔哩哔哩", "b23.tv"],
    "douyin": ["douyin", "dy", "抖音", "v.douyin.com", "iesdouyin.com"],
    "instagram": ["instagram", "ig", "ins"],
    "kuaishou": ["kuaishou", "ks", "快手"],
    "lemon8": ["lemon8"],
    "linkedin": ["linkedin", "领英"],
    "pipixia": ["pipixia", "皮皮虾"],
    "reddit": ["reddit"],
    "threads": ["threads"],
    "tiktok": ["tiktok", "tik tok"],
    "toutiao": ["toutiao", "今日头条", "头条"],
    "twitter": ["twitter", "x", "x.com", "推特"],
    "u2": ["u2", "asr", "transcription", "语音转写", "转文案"],
    "u3": ["u3", "upload", "media upload", "媒体上传", "中转"],
    "wechat_channels": ["wechat_channels", "wechat channels", "微信视频号", "视频号"],
    "wechat_mp": ["wechat_mp", "wechat official accounts", "微信公众号", "公众号", "mp.weixin.qq.com"],
    "weibo": ["weibo", "微博"],
    "xiaohongshu": ["xiaohongshu", "xhs", "小红书", "xhslink.com", "xiaohongshu.com"],
    "xigua": ["xigua", "西瓜视频"],
    "youtube": ["youtube", "yt", "youtu.be"],
    "zhihu": ["zhihu", "知乎"],
}

CAPABILITY_ALIASES: Dict[str, List[str]] = {
    "article_detail": ["article_detail", "article", "文章详情", "文章内容", "公众号文章"],
    "article_list": ["article_list", "文章列表"],
    "article_url": ["article_url", "文章链接", "公众号链接"],
    "comments": ["comments", "comment", "评论", "评论列表"],
    "hot_search": ["hot_search", "hot search", "热搜", "热榜", "hot words"],
    "livestream": ["livestream", "live", "直播"],
    "media_upload": ["media_upload", "upload", "上传", "媒体中转"],
    "music": ["music", "音乐"],
    "note_detail": ["note_detail", "note", "笔记", "笔记详情", "小红书笔记"],
    "product_detail": ["product_detail", "product", "goods", "商品", "商品详情"],
    "ranking": ["ranking", "rank", "榜单", "排行"],
    "search": ["search", "搜索", "检索"],
    "transcription": ["transcription", "asr", "字幕", "转写", "转文案", "语音识别"],
    "user_posts": ["user_posts", "posts", "作品列表", "主页作品"],
    "user_profile": ["user_profile", "profile", "author", "creator", "用户信息", "主页"],
    "video_detail": ["video_detail", "video", "视频详情", "单个视频", "作品详情"],
}

VARIANT_PRIORITY = {
    "app_v3": 10,
    "app_v2": 20,
    "app_v1": 30,
    "app": 35,
    "web_v3": 40,
    "web_v2": 50,
    "web_v1": 60,
    "web": 65,
    "service": 70,
    "default": 90,
}


def load_spec() -> Tuple[Dict[str, Any], Dict[str, str]]:
    fetched_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
    if LOCAL_OPENAPI_FILE:
        path = Path(LOCAL_OPENAPI_FILE).expanduser().resolve()
        payload = json.loads(path.read_text(encoding="utf-8"))
        return payload, {"mode": "file", "source": str(path), "generated_at": fetched_at}

    request = Request(
        REMOTE_OPENAPI_URL,
        headers={
            "Accept": "application/json, text/plain, */*",
            "User-Agent": os.getenv("TIKOMNI_OPENAPI_USER_AGENT", "Mozilla/5.0"),
        },
    )
    with urlopen(request, timeout=60) as response:
        payload = json.load(response)
    return payload, {"mode": "remote", "source": REMOTE_OPENAPI_URL, "generated_at": fetched_at}


def resolve_ref(spec: Dict[str, Any], ref: str) -> Dict[str, Any]:
    node: Any = spec
    for raw_part in ref.lstrip("#/").split("/"):
        part = raw_part.replace("~1", "/").replace("~0", "~")
        node = node[part]
    return node if isinstance(node, dict) else {}


def deref_object(spec: Dict[str, Any], node: Optional[Dict[str, Any]], seen: Optional[set[str]] = None) -> Dict[str, Any]:
    if not isinstance(node, dict):
        return {}
    seen = seen or set()
    ref = node.get("$ref")
    if not ref:
        return node
    ref_text = str(ref)
    if ref_text in seen:
        return {}
    return deref_object(spec, resolve_ref(spec, ref_text), seen | {ref_text})


def deref_schema(spec: Dict[str, Any], schema: Optional[Dict[str, Any]], seen: Optional[set[str]] = None) -> Dict[str, Any]:
    resolved = dict(deref_object(spec, schema, seen))
    if not resolved:
        return {}

    if "allOf" in resolved:
        merged: Dict[str, Any] = {"type": "object", "properties": {}, "required": []}
        for item in resolved.get("allOf") or []:
            item_schema = deref_schema(spec, item if isinstance(item, dict) else {}, seen)
            if not item_schema:
                continue
            if isinstance(item_schema.get("properties"), dict):
                merged["properties"].update(item_schema["properties"])
            if isinstance(item_schema.get("required"), list):
                merged["required"].extend(item_schema["required"])
        merged["required"] = sorted(set(merged["required"]))
        return merged

    if "oneOf" in resolved or "anyOf" in resolved:
        variants = resolved.get("oneOf") or resolved.get("anyOf") or []
        for item in variants:
            item_schema = deref_schema(spec, item if isinstance(item, dict) else {}, seen)
            if item_schema.get("type") == "object" or isinstance(item_schema.get("properties"), dict):
                return item_schema
        for item in variants:
            item_schema = deref_schema(spec, item if isinstance(item, dict) else {}, seen)
            if item_schema:
                return item_schema

    if isinstance(resolved.get("properties"), dict):
        resolved["properties"] = {
            str(name): deref_schema(spec, field if isinstance(field, dict) else {}, seen)
            for name, field in resolved["properties"].items()
        }
    if isinstance(resolved.get("items"), dict):
        resolved["items"] = deref_schema(spec, resolved["items"], seen)
    return resolved


def normalize_text(value: Any) -> str:
    if value is None:
        return ""
    return re.sub(r"\s+", " ", str(value)).strip()


def snake(value: str) -> str:
    text = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", value)
    text = re.sub(r"[^A-Za-z0-9]+", "_", text).strip("_").lower()
    return re.sub(r"_+", "_", text) or "operation"


def path_segments(path: str) -> List[str]:
    return [segment for segment in path.strip("/").split("/") if segment]


def strip_api_prefix(path: str) -> List[str]:
    segments = path_segments(path)
    if len(segments) >= 3 and segments[0] == "api" and re.fullmatch(r"u\d+", segments[1]) and re.fullmatch(r"v\d+", segments[2]):
        return segments[3:]
    return segments


def classify_route(path: str) -> Tuple[str, List[str], bool]:
    segments = path_segments(path)
    if len(segments) >= 2 and segments[0] == "api":
        service = segments[1]
        if service == "u2":
            return "u2", segments[3:], False
        if service == "u3":
            return "u3", segments[3:], False

    tail = strip_api_prefix(path)
    demo = bool(tail and tail[0] == "demo")
    if demo:
        tail = tail[1:]
    platform = tail[0] if tail else "general"
    return platform, tail[1:], demo


def detect_variant(route_tail: Sequence[str], demo: bool, platform: str) -> str:
    if platform in {"u2", "u3"}:
        return "service"
    if not route_tail:
        variant = "default"
    elif route_tail[0] in {"app", "web"}:
        base = route_tail[0]
        if len(route_tail) > 1 and re.fullmatch(r"v\d+", route_tail[1]):
            variant = f"{base}_{route_tail[1]}"
        else:
            variant = base
    elif re.fullmatch(r"(app|web)_v\d+", route_tail[0]):
        variant = route_tail[0]
    else:
        variant = "default"
    return f"demo_{variant}" if demo else variant


def operation_name_from_path(path: str, op: Dict[str, Any]) -> str:
    tail = strip_api_prefix(path)
    last = tail[-1] if tail else ""
    if last.startswith("{") and last.endswith("}"):
        return snake(str(op.get("operationId") or "operation"))
    return snake(last)


def capability_from_route(path: str, op: Dict[str, Any], platform: str) -> str:
    text = " ".join(
        [
            path,
            str(op.get("operationId") or ""),
            str(op.get("summary") or ""),
            str(op.get("description") or ""),
        ]
    ).lower()
    operation_name = operation_name_from_path(path, op)

    if platform == "u2" or any(token in text for token in ("asr", "transcription", "subtitle")):
        return "transcription"
    if platform == "u3" or any(token in text for token in ("upload", "ingest")):
        return "media_upload"
    if platform == "wechat_mp":
        if "comment" in operation_name or "reply" in operation_name:
            return "comments"
        if operation_name in {"fetch_mp_article_url", "fetch_mp_article_url_conversion"}:
            return "article_url"
        if operation_name in {"fetch_mp_article_list", "fetch_mp_related_articles"}:
            return "article_list"
        if "article" in operation_name:
            return "article_detail"
    if platform == "wechat_channels":
        if operation_name == "fetch_video_detail":
            return "video_detail"
        if "comment" in operation_name:
            return "comments"
        if "search" in operation_name:
            return "search"
        if operation_name == "fetch_hot_words":
            return "hot_search"
        if "live" in operation_name:
            return "livestream"
        if operation_name == "fetch_home_page":
            return "user_profile"
    if "hot_search" in text or "hot search" in text or "hot_words" in text or "hot words" in text:
        return "hot_search"
    if "search" in operation_name or "suggest" in operation_name:
        return "search"
    if "article_url" in text or "article url" in text:
        return "article_url"
    if "article_list" in text or "article list" in text:
        return "article_list"
    if "article" in text:
        if "comment" in text or "reply" in text:
            return "comments"
        return "article_detail"
    if "comment" in text or "reply" in text:
        return "comments"
    if "search" in text or "suggest" in text:
        return "search"
    if "billboard" in text or "ranking" in text or "rank" in text or "trend" in text:
        return "ranking"
    if "live" in text or "stream" in text:
        return "livestream"
    if "product" in text or "goods" in text or "shop" in text:
        return "product_detail"
    if "music" in text or "audio" in text:
        return "music"
    if "user_post" in text or "user_posted" in text or "user_videos" in text or "post_videos" in text or "fetch_user_post" in text:
        return "user_posts"
    if "user" in text or "profile" in text or "creator" in text or "author" in text or "home_page" in text:
        return "user_profile"
    if "note" in text:
        return "note_detail"
    if "one_video" in text or "video_detail" in text or ("video" in text and "detail" in text):
        return "video_detail"
    if "video" in text:
        return "video_detail"
    return "general"


def load_overrides() -> Dict[str, Any]:
    path = CATALOG_ROOT / "overrides.json"
    if not path.exists():
        return {}
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}
    return payload if isinstance(payload, dict) else {}


def apply_overrides(operations: List[Dict[str, Any]], overrides: Dict[str, Any]) -> None:
    platform_overrides = overrides.get("platform_overrides") if isinstance(overrides.get("platform_overrides"), dict) else {}
    capability_overrides = (
        overrides.get("capability_overrides") if isinstance(overrides.get("capability_overrides"), dict) else {}
    )

    for operation in operations:
        endpoint_id = str(operation.get("endpoint_id") or "")
        platform = str(operation.get("platform") or "")
        capability = str(operation.get("capability") or "")

        if endpoint_id in platform_overrides:
            operation["platform"] = snake(str(platform_overrides[endpoint_id]))
        elif platform in platform_overrides:
            operation["platform"] = snake(str(platform_overrides[platform]))

        if endpoint_id in capability_overrides:
            operation["capability"] = snake(str(capability_overrides[endpoint_id]))
        elif capability in capability_overrides:
            operation["capability"] = snake(str(capability_overrides[capability]))


def apply_recommendation_overrides(operations: List[Dict[str, Any]], overrides: Dict[str, Any]) -> None:
    recommendation_overrides = (
        overrides.get("recommendation_overrides")
        if isinstance(overrides.get("recommendation_overrides"), dict)
        else {}
    )
    if not recommendation_overrides:
        return

    operation_by_id = {str(operation.get("endpoint_id") or ""): operation for operation in operations}
    for group_key, recommended_id in recommendation_overrides.items():
        platform, _, capability = str(group_key).partition(".")
        recommended = operation_by_id.get(str(recommended_id))
        if not platform or not capability or not recommended:
            continue
        group_ops = [
            operation
            for operation in operations
            if operation.get("platform") == platform and operation.get("capability") == capability
        ]
        if recommended not in group_ops:
            continue
        alternative_ids = [str(operation["endpoint_id"]) for operation in group_ops if operation is not recommended]
        for operation in group_ops:
            operation["recommended"] = operation is recommended
            operation["alternatives"] = alternative_ids if operation is recommended else [
                str(item["endpoint_id"]) for item in group_ops if item is not operation
            ]


def variant_sort_key(variant: str) -> Tuple[int, str]:
    clean = variant.removeprefix("demo_")
    base_priority = VARIANT_PRIORITY.get(clean, 80)
    if variant.startswith("demo_"):
        base_priority += 1000
    return base_priority, variant


def intent_specificity_penalty(op: Dict[str, Any]) -> int:
    capability = str(op.get("capability") or "")
    operation_name = str(op.get("operation_name") or "")
    path = str(op.get("path") or "").lower()

    if capability == "hot_search":
        if operation_name == "fetch_hot_search_list":
            return -20
        specific_tokens = ["brand", "music", "live", "city", "challenge", "rise", "category", "creator", "danmaku"]
        return sum(10 for token in specific_tokens if token in path)
    if capability == "article_detail":
        if "detail_json" in path:
            return -20
        if "detail_html" in path:
            return -10
        return 0
    if capability == "video_detail":
        if operation_name in {"fetch_one_video", "fetch_video_detail", "get_video_note_detail"}:
            return -20
        return 0
    if capability == "note_detail":
        if operation_name in {"get_note_detail", "get_video_note_detail", "get_image_note_detail"}:
            return -20
        return 0
    return 0


def operation_sort_key(op: Dict[str, Any]) -> Tuple[int, str, str]:
    return (*variant_sort_key(str(op.get("variant") or "")), str(op.get("path") or ""))


def schema_properties(schema: Dict[str, Any]) -> Tuple[Dict[str, Any], List[str]]:
    resolved_type = schema.get("type")
    if resolved_type == "object" or isinstance(schema.get("properties"), dict):
        props = schema.get("properties") if isinstance(schema.get("properties"), dict) else {}
        required = schema.get("required") if isinstance(schema.get("required"), list) else []
        return props, [str(item) for item in required]
    return {}, []


def resolve_parameter(spec: Dict[str, Any], param: Any) -> Dict[str, Any]:
    return deref_object(spec, param if isinstance(param, dict) else {})


def merge_parameters(spec: Dict[str, Any], path_item: Dict[str, Any], op: Dict[str, Any]) -> List[Dict[str, Any]]:
    merged: Dict[Tuple[str, str], Dict[str, Any]] = {}
    order: List[Tuple[str, str]] = []
    for param_list in (path_item.get("parameters"), op.get("parameters")):
        if not isinstance(param_list, list):
            continue
        for param in param_list:
            resolved = resolve_parameter(spec, param)
            name = str(resolved.get("name") or "").strip()
            location = str(resolved.get("in") or "query").strip()
            if not name:
                continue
            key = (name, location)
            if key not in merged:
                order.append(key)
            schema = deref_schema(spec, resolved.get("schema") if isinstance(resolved.get("schema"), dict) else {})
            merged[key] = {
                "name": name,
                "in": location,
                "required": bool(resolved.get("required")),
                "schema": schema or {"type": "string"},
                "description": normalize_text(resolved.get("description") or schema.get("description")),
            }
    return [merged[key] for key in order]


def request_body_info(spec: Dict[str, Any], op: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    body = deref_object(spec, op.get("requestBody") if isinstance(op.get("requestBody"), dict) else {})
    if not body:
        return None
    content = body.get("content") if isinstance(body.get("content"), dict) else {}
    media_type = "application/json" if "application/json" in content else next(iter(content.keys()), "")
    media = content.get(media_type) if media_type else {}
    schema = deref_schema(spec, media.get("schema") if isinstance(media, dict) else {})
    return {
        "required": bool(body.get("required")),
        "content_type": media_type or "application/json",
        "schema": schema or {},
    }


def build_input_schema(parameters: Sequence[Dict[str, Any]], body: Optional[Dict[str, Any]]) -> Dict[str, Any]:
    properties: Dict[str, Any] = {}
    required: List[str] = []

    for param in parameters:
        name = str(param.get("name") or "")
        if not name:
            continue
        properties[name] = param.get("schema") if isinstance(param.get("schema"), dict) else {"type": "string"}
        if param.get("required"):
            required.append(name)

    if body:
        body_schema = body.get("schema") if isinstance(body.get("schema"), dict) else {}
        props, body_required = schema_properties(body_schema)
        if props:
            for name, field_schema in props.items():
                properties[str(name)] = field_schema if isinstance(field_schema, dict) else {}
            required.extend(body_required if body.get("required") else [])
        else:
            properties["body"] = body_schema or {"type": "object"}
            if body.get("required"):
                required.append("body")

    return {
        "type": "object",
        "properties": properties,
        "required": sorted(set(required)),
        "additionalProperties": False,
    }


def build_raw_operations(spec: Dict[str, Any]) -> List[Dict[str, Any]]:
    operations: List[Dict[str, Any]] = []
    for path, path_item in sorted((spec.get("paths") or {}).items()):
        if not isinstance(path_item, dict):
            continue
        for method in HTTP_METHODS:
            raw_op = path_item.get(method)
            if not isinstance(raw_op, dict):
                continue
            op = deref_object(spec, raw_op)
            platform, route_tail, demo = classify_route(path)
            variant = detect_variant(route_tail, demo, platform)
            capability = capability_from_route(path, op, platform)
            operation_name = operation_name_from_path(path, op)
            endpoint_id = f"{snake(platform)}.{snake(capability)}.{snake(variant)}.{operation_name}"
            params = merge_parameters(spec, path_item, op)
            body = request_body_info(spec, op)
            operations.append(
                {
                    "endpoint_id": endpoint_id,
                    "platform": snake(platform),
                    "capability": snake(capability),
                    "variant": snake(variant),
                    "operation_name": operation_name,
                    "recommended": False,
                    "alternatives": [],
                    "demo": demo,
                    "method": method.upper(),
                    "path": path,
                    "summary": normalize_text(op.get("summary")),
                    "tags": [str(tag) for tag in (op.get("tags") or [])],
                    "parameters": params,
                    "request_body": body,
                    "input_schema": build_input_schema(params, body),
                    "source_openapi_operation_id": str(op.get("operationId") or ""),
                }
            )
    return operations


def ensure_unique_endpoint_ids(operations: List[Dict[str, Any]]) -> None:
    buckets: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    for operation in operations:
        buckets[str(operation["endpoint_id"])].append(operation)
    for endpoint_id, bucket in buckets.items():
        if len(bucket) <= 1:
            continue
        for operation in bucket:
            digest = hashlib.sha1(f"{operation['method']} {operation['path']}".encode("utf-8")).hexdigest()[:8]
            operation["endpoint_id"] = f"{endpoint_id}_{digest}"


def assign_recommendations(operations: List[Dict[str, Any]]) -> None:
    groups: Dict[Tuple[str, str], List[Dict[str, Any]]] = defaultdict(list)
    for operation in operations:
        groups[(str(operation["platform"]), str(operation["capability"]))].append(operation)

    for group_ops in groups.values():
        sorted_ops = sorted(group_ops, key=lambda item: (intent_specificity_penalty(item), *operation_sort_key(item)))
        production_ops = [op for op in sorted_ops if not op.get("demo")]
        candidates = production_ops or sorted_ops
        if not candidates:
            continue
        recommended = candidates[0]
        alternative_ids = [str(op["endpoint_id"]) for op in candidates if op is not recommended]
        recommended["recommended"] = True
        recommended["alternatives"] = alternative_ids
        for operation in group_ops:
            if operation is recommended:
                continue
            operation["recommended"] = False
            operation["alternatives"] = [
                str(op["endpoint_id"])
                for op in candidates
                if op is not operation
            ]


def build_platforms(operations: Sequence[Dict[str, Any]]) -> List[Dict[str, Any]]:
    grouped: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    for operation in operations:
        grouped[str(operation["platform"])].append(operation)
    platforms: List[Dict[str, Any]] = []
    for platform, items in sorted(grouped.items()):
        capabilities = sorted({str(item["capability"]) for item in items})
        platforms.append(
            {
                "slug": platform,
                "aliases": sorted(set([platform] + PLATFORM_ALIASES.get(platform, []))),
                "operation_count": len(items),
                "capabilities": capabilities,
            }
        )
    return platforms


def build_capabilities(operations: Sequence[Dict[str, Any]]) -> List[Dict[str, Any]]:
    grouped: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    for operation in operations:
        grouped[str(operation["capability"])].append(operation)
    capabilities: List[Dict[str, Any]] = []
    for capability, items in sorted(grouped.items()):
        capabilities.append(
            {
                "slug": capability,
                "aliases": sorted(set([capability] + CAPABILITY_ALIASES.get(capability, []))),
                "operation_count": len(items),
                "platforms": sorted({str(item["platform"]) for item in items}),
            }
        )
    return capabilities


def build_aliases(platforms: Sequence[Dict[str, Any]], capabilities: Sequence[Dict[str, Any]]) -> Dict[str, Any]:
    return {
        "platforms": {str(item["slug"]): item.get("aliases", []) for item in platforms},
        "capabilities": {str(item["slug"]): item.get("aliases", []) for item in capabilities},
    }


def build_overrides() -> Dict[str, Any]:
    return {
        "schema_version": "v1",
        "notes": [
            "endpoint_id is generated automatically and must not be manually overridden.",
            "Overrides may adjust platform, capability, recommended endpoint, alternatives, and aliases only.",
        ],
        "platform_overrides": {},
        "capability_overrides": {},
        "recommendation_overrides": {},
    }


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> None:
    spec, source_meta = load_spec()
    if not isinstance(spec.get("paths"), dict):
        raise ValueError("invalid_openapi_paths")
    overrides = load_overrides()
    operations = build_raw_operations(spec)
    apply_overrides(operations, overrides)
    ensure_unique_endpoint_ids(operations)
    assign_recommendations(operations)
    apply_recommendation_overrides(operations, overrides)
    platforms = build_platforms(operations)
    capabilities = build_capabilities(operations)
    aliases = build_aliases(platforms, capabilities)
    meta = {
        "schema_version": "v1",
        "source": source_meta,
        "operation_count": len(operations),
        "platform_count": len(platforms),
        "capability_count": len(capabilities),
    }

    write_json(CATALOG_ROOT / "operations.json", operations)
    write_json(CATALOG_ROOT / "platforms.json", platforms)
    write_json(CATALOG_ROOT / "capabilities.json", capabilities)
    write_json(CATALOG_ROOT / "aliases.json", aliases)
    if not overrides:
        write_json(CATALOG_ROOT / "overrides.json", build_overrides())
    write_json(CATALOG_ROOT / "metadata.json", meta)
    print(json.dumps(meta, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
