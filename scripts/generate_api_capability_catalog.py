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
    ("transcription", "ASR / transcription"),
    ("asr", "ASR / transcription"),
    ("subtitle", "subtitles / transcription"),
    ("upload", "media upload / public URL"),
    ("ingest", "media upload / public URL"),
    ("comment", "comments"),
    ("reply", "comment replies"),
    ("search", "search"),
    ("suggest", "search"),
    ("hot", "trends / rankings"),
    ("billboard", "trends / rankings"),
    ("trend", "trends / rankings"),
    ("creator", "creators"),
    ("author", "creators"),
    ("user", "profiles / accounts"),
    ("profile", "profiles / accounts"),
    ("channel", "profiles / accounts"),
    ("home", "profiles / accounts"),
    ("video", "content details"),
    ("note", "content details"),
    ("post", "content details"),
    ("article", "content details"),
    ("detail", "details"),
    ("download", "media / download"),
    ("media", "media / download"),
    ("audio", "audio / media"),
    ("tts", "subtitles / transcription"),
    ("shop", "commerce"),
    ("product", "commerce"),
    ("goods", "commerce"),
    ("ads", "ads"),
    ("ad_", "ads"),
    ("creative", "ads"),
    ("analytics", "analytics"),
    ("insight", "analytics"),
    ("report", "analytics"),
    ("live", "livestream"),
    ("stream", "livestream"),
    ("hashtag", "topics"),
    ("challenge", "topics"),
    ("topic", "topics"),
    ("music", "music / audio"),
)
SERVICE_GUIDE_ROUTES: Sequence[Tuple[str, str, str, str]] = (
    (
        "Submit U2 ASR job",
        "POST",
        "/api/u2/v1/services/audio/asr/transcription",
        "Default primary path. Submit the no-watermark or download URL returned by U1 directly to U2 ASR. Do not start with U3.",
    ),
    (
        "Poll U2 job status",
        "POST",
        "/api/u2/v1/tasks/{task_id}",
        "Observe job completion. Stay in soft observation after 90 seconds. Trigger U3 fallback only if there is still no result after 120 seconds.",
    ),
    (
        "Request U3 upload / relay",
        "POST",
        "/api/u3/v1/uploads",
        "Use only if U2 still has no result after 120 seconds. Its purpose is to convert a private or non-publicly-readable source link into a public URL.",
    ),
    (
        "Complete U3 upload and get a public URL",
        "POST",
        "/api/u3/v1/uploads/{upload_id}/complete",
        "Completion should return a public URL. Submit that URL to U2 ASR again. If it still fails, keep the fact card and return incomplete.",
    ),
)


def fetch_remote_spec(url: str) -> Dict[str, Any]:
    request = Request(url, headers=DEFAULT_HEADERS)
    with urlopen(request, timeout=60) as response:
        payload = json.load(response)
    if not isinstance(payload, dict) or not isinstance(payload.get("paths"), dict):
        raise ValueError(f"invalid_remote_openapi_structure:{url}")
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
        raise RuntimeError(f"failed_to_fetch_remote_openapi:{exc}") from exc


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
        return "None"
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
        return "Not declared"
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
        base = "dynamic object"

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
        return "dynamic object"
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
        return "No declared structure"
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
        detail = "Header `Authorization: Bearer {token}`"
        if "cookie" in description.lower() and "authorization" in description.lower():
            detail += "; docs also allow Cookie `Authorization` as fallback"
        return f"{detail} (`{scheme_name}`)"

    if scheme_type == "apiKey":
        location = scheme_in or "query"
        target = f"`{param_name}`" if param_name else "`<unnamed>`"
        return f"{location} {target} (`{scheme_name}`)"

    if scheme_type:
        detail = f"{scheme_type}"
        if http_scheme:
            detail = f"{detail}:{http_scheme}"
        return f"{detail} (`{scheme_name}`)"
    return f"`{scheme_name}`"


def effective_security(spec: Dict[str, Any], op: Dict[str, Any]) -> List[Dict[str, Any]]:
    security = op.get("security")
    if security is None:
        security = spec.get("security")
    return security if isinstance(security, list) else []


def summarize_security(spec: Dict[str, Any], op: Dict[str, Any]) -> str:
    requirements = effective_security(spec, op)
    if not requirements:
        return "No auth required"

    options: List[str] = []
    for requirement in requirements:
        if not isinstance(requirement, dict):
            continue
        if not requirement:
            options.append("No auth required")
            continue
        parts = [describe_security_scheme(spec, scheme_name) for scheme_name in requirement.keys()]
        if parts:
            options.append(" + ".join(parts))
    unique_options = list(dict.fromkeys(options))
    return " or ".join(unique_options) if unique_options else "No auth required"


def compact_security_label(summary: str) -> str:
    if "Authorization: Bearer {token}" in summary:
        return "Header `Authorization` Bearer"
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
        return "None"
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
    return "; ".join(parts) if parts else "None"


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
                "Field": name,
                "In": str(resolved.get("in") or "query"),
                "Type": schema_type_name(spec, schema),
                "Required": "Yes" if resolved.get("required") else "No",
                "Description": normalize_inline_text(resolved.get("description") or schema.get("description")) or "None",
                "Default": format_value(schema.get("default")),
                "Example": format_value(first_non_empty(resolved.get("example"), schema.get("example"))),
                "Enum": format_enum(schema.get("enum")) or "None",
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
        description = normalize_inline_text(field_schema.get("description") or resolved.get("description")) or "None"
        rows.append(
            {
                "Field": path,
                "Type": schema_type_name(spec, field_schema),
                "Required": "Yes" if required else "No",
                "Description": description,
                "Default": format_value(first_non_empty(field_schema.get("default"), resolved.get("default"))),
                "Example": format_value(first_non_empty(field_schema.get("example"), resolved.get("example"))),
                "Enum": format_enum(first_non_empty(field_schema.get("enum"), resolved.get("enum"))) or "None",
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
        return "None"
    entries = pick_media_entries(resolved_body.get("content"))
    if not entries:
        return "None"
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
        return "No declared success response"
    if not chosen_response:
        return f"{chosen_code}: No declared structure"
    entries = pick_media_entries(chosen_response.get("content"))
    if not entries:
        return f"{chosen_code}: No response body"
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
    return abilities or ["general"]


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
        return "None"
    return ", ".join(f"`{name}`" for name, _ in counter.most_common(10))


def collect_common_security(spec: Dict[str, Any], operations: Sequence[Tuple[str, str, Dict[str, Any]]]) -> str:
    counter: Counter[str] = Counter()
    for _, _, op in operations:
        counter[summarize_security(spec, op)] += 1
    if not counter:
        return "No auth required"
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
            value = row.get(header, "") or "None"
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
    lines = ["#### Parameters", ""]
    if not rows:
        lines.extend(["None", ""])
        return lines

    headers = ["Field", "In", "Type", "Required", "Description"]
    clip_limits = {"Description": 120}
    if detailed:
        headers.extend(["Default", "Example", "Enum"])
        clip_limits = {"Description": 180, "Default": 80, "Example": 80, "Enum": 80}
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
    lines = ["#### Request Body", ""]
    if not resolved_body:
        lines.extend(["None", ""])
        return lines

    lines.append(f"- required: {'Yes' if resolved_body.get('required') else 'No'}")
    lines.append("")
    sections = collect_content_sections(
        spec,
        resolved_body.get("content"),
        max_depth=CONTRACT_SECTION_FIELD_DEPTH if detailed else TAG_SECTION_FIELD_DEPTH,
        max_rows=CONTRACT_SECTION_FIELD_LIMIT if detailed else TAG_SECTION_FIELD_LIMIT,
    )
    if not sections:
        lines.extend(["No declared structure", ""])
        return lines

    headers = ["Field", "Type", "Required", "Description"]
    clip_limits = {"Description": 120}
    if detailed:
        headers.extend(["Default", "Example", "Enum"])
        clip_limits = {"Description": 180, "Default": 80, "Example": 80, "Enum": 80}

    for section in sections:
        lines.append(f"##### `{section['media_type']}`")
        lines.append("")
        lines.append(f"- Schema summary: {section['summary']}")
        lines.append("")
        if section["rows"]:
            lines.extend(render_markdown_table(headers, section["rows"], clip_limits=clip_limits))
            lines.append("")
        else:
            lines.extend(["No field table", ""])
        if section["truncated"]:
            lines.append(
                f"- Fields truncated: this layer shows only the first `{CONTRACT_SECTION_FIELD_LIMIT if detailed else TAG_SECTION_FIELD_LIMIT}` rows."
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
    lines = ["#### Success Response", ""]
    if not status_code:
        lines.extend(["No declared success response", ""])
        return lines
    if not response:
        lines.extend([f"`{status_code}`: No declared structure", ""])
        return lines

    sections = collect_content_sections(
        spec,
        response.get("content"),
        max_depth=CONTRACT_SECTION_FIELD_DEPTH if detailed else TAG_SECTION_FIELD_DEPTH,
        max_rows=CONTRACT_SECTION_FIELD_LIMIT if detailed else TAG_SECTION_FIELD_LIMIT,
    )
    if not sections:
        lines.extend([f"`{status_code}`: No response body", ""])
        return lines

    headers = ["Field", "Type", "Required", "Description"]
    clip_limits = {"Description": 120}
    if detailed:
        headers.extend(["Default", "Example", "Enum"])
        clip_limits = {"Description": 180, "Default": 80, "Example": 80, "Enum": 80}

    for section in sections:
        lines.append(f"##### `{status_code} {section['media_type']}`")
        lines.append("")
        lines.append(f"- Schema summary: {section['summary']}")
        lines.append("")
        if section["rows"]:
            lines.extend(render_markdown_table(headers, section["rows"], clip_limits=clip_limits))
            lines.append("")
        else:
            lines.extend(["No field table", ""])
        if section["truncated"]:
            lines.append(
                f"- Fields truncated: this layer shows only the first `{CONTRACT_SECTION_FIELD_LIMIT if detailed else TAG_SECTION_FIELD_LIMIT}` rows."
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
        "# TikOmni API Capability Index",
        "",
        "## Purpose",
        "",
        "- This auto-generated lightweight entry point helps identify the right tag, capability area, and auth pattern first.",
        f"- Source mode: `{source_meta['mode']}`",
        f"- Source: `{source_meta['source']}`",
        f"- Fetched at: `{source_meta['fetched_at']}`",
        "- Start route selection here. Read `api-tags/` and `api-contracts/` only when you need field definitions, defaults, examples, or full response structures.",
        "- If the task involves ASR timeout, non-public media URLs, or U3 media relay, also read `service-guides/asr-u2-u3-fallback.md`.",
        "",
        "## Global Auth",
        "",
        f"- Default auth: {global_security}",
        "- If a route overrides or disables the default auth requirement, trust the corresponding `api-tags/` and `api-contracts/` entries.",
        "",
        "## Read Order",
        "",
        "1. Choose a tag by platform and object type.",
        "2. Open `api-tags/<tag>.md` for route summaries, auth requirements, and key fields.",
        "3. Open `api-contracts/<tag>.md` only when you need exact field definitions, defaults, examples, or full success-response structures.",
        "4. If the task involves transcription, the 90-second soft observation window, or the 120-second hard fallback, read the U2/U3 guide.",
        "",
        "## Stats",
        "",
        f"- Tag groups: `{len(grouped)}`",
        f"- Routes: `{op_count}`",
        f"- Generated targets: `{len(REFERENCE_ROOTS)}` skill reference sets",
        "",
        "## Special Flows",
        "",
        f"- ASR and U3 fallback: [`{SERVICE_GUIDES_DIRNAME}/{ASR_FALLBACK_GUIDE_FILENAME}`](./{SERVICE_GUIDES_DIRNAME}/{ASR_FALLBACK_GUIDE_FILENAME})",
        f"- ASR tag: [`{tag_file_relpath('ASR-API')}`](./{tag_file_relpath('ASR-API')})" if "ASR-API" in grouped else "- ASR tag: `ASR-API` is not declared in the current OpenAPI.",
        f"- U3 media relay tag: [`{tag_file_relpath('Media-Ingest-API')}`](./{tag_file_relpath('Media-Ingest-API')})" if "Media-Ingest-API" in grouped else "- U3 media relay tag: `Media-Ingest-API` is not declared in the current OpenAPI.",
        "",
        "## Tag Overview",
        "",
        "| Tag | File | Contract | Ops | Auth | Common Capabilities | Common Inputs |",
        "| --- | --- | --- | ---: | --- | --- | --- |",
    ]

    for tag in sorted(grouped):
        operations = grouped[tag]
        ability_counter: Counter[str] = Counter()
        for _, path, _ in operations:
            ability_counter.update(infer_abilities(path))
        top_abilities = " / ".join(label for label, _ in ability_counter.most_common(4)) or "general"
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
    top_abilities = " / ".join(label for label, _ in ability_counter.most_common(6)) or "general"
    desc = str(tag_meta.get("description") or "").strip().replace("\n", " ")
    common_auth = collect_common_security(spec, operations)
    contract_link = contract_file_relpath(tag)

    lines: List[str] = [
        f"# {tag} Route Summary",
        "",
        f"- Back to index: [`{INDEX_FILENAME}`](../{INDEX_FILENAME})",
        f"- Current tag file: `{tag_file_relpath(tag)}`",
        f"- Full contract: [`{contract_link}`](../{contract_link})",
        f"- Source: `{source_meta['source']}`",
        f"- Fetched at: `{source_meta['fetched_at']}`",
        f"- Route count: `{len(operations)}`",
        f"- Common capabilities: {top_abilities}",
        f"- Default auth: {common_auth}",
        f"- Common inputs: {collect_common_inputs(spec, operations)}",
    ]
    if desc:
        lines.append(f"- Tag description: {desc}")

    if tag in {"ASR-API", "Media-Ingest-API"}:
        lines.append(f"- Related service guide: [`{SERVICE_GUIDES_DIRNAME}/{ASR_FALLBACK_GUIDE_FILENAME}`](../{SERVICE_GUIDES_DIRNAME}/{ASR_FALLBACK_GUIDE_FILENAME})")

    lines.extend(["", "## Routes", ""])

    for method, path, op in operations:
        ability = " / ".join(infer_abilities(path))
        summary = normalize_inline_text(op.get("summary"))
        security = summarize_security(spec, op)
        operation_id = str(op.get("operationId") or "").strip()
        contract_anchor = operation_anchor(method, path)

        lines.append(f"### `{method} {path}`")
        lines.append("")
        if summary:
            lines.append(f"- Summary: {summary}")
        lines.append(f"- Capabilities: {ability}")
        lines.append(f"- Auth: {security}")
        if operation_id:
            lines.append(f"- operationId: `{operation_id}`")
        lines.append(f"- Full contract: [`{contract_link}#{contract_anchor}`](../{contract_link}#{contract_anchor})")
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
        f"# {tag} Full Contract",
        "",
        f"- Back to index: [`{INDEX_FILENAME}`](../{INDEX_FILENAME})",
        f"- Back to route summary: [`{tag_file_relpath(tag)}`](../{tag_file_relpath(tag)})",
        f"- Current contract file: `{contract_file_relpath(tag)}`",
        f"- Source: `{source_meta['source']}`",
        f"- Fetched at: `{source_meta['fetched_at']}`",
        f"- Route count: `{len(operations)}`",
        f"- Default auth: {common_auth}",
        "- Read this file only when you need precise auth notes, parameter descriptions, defaults, examples, or success-response fields.",
    ]
    if desc:
        lines.append(f"- Tag description: {desc}")

    lines.extend(["", "## Route Contracts", ""])

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
            lines.append(f"- Summary: {summary}")
        lines.append(f"- Capabilities: {' / '.join(infer_abilities(path))}")
        lines.append(f"- Auth: {security}")
        if operation_id:
            lines.append(f"- operationId: `{operation_id}`")
        lines.append("")

        if description:
            lines.append("#### Notes")
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
        "# U2 ASR and U3 Public URL Fallback",
        "",
        "## Purpose",
        "",
        "- This guide defines the primary ASR path and timeout fallback for video tasks. It does not apply to text-only works.",
        "- Always try U2 ASR first. U3 is fallback-only and must not bypass U2 by default.",
        "- If a U1 detail route returns a no-watermark download link or another download URL that may not be publicly readable, use this guide to decide when to switch to U3.",
        f"- Source: `{source_meta['source']}`",
        f"- Fetched at: `{source_meta['fetched_at']}`",
        "",
        "## Fixed Policy",
        "",
        "1. Call a U1 detail route first and collect `video_download_url`, a no-watermark download URL, or another directly downloadable media URL.",
        "2. Submit that URL to U2 ASR directly. Do not start with U3.",
        "3. If there is still no complete result after 90 seconds, stay in soft observation and keep the primary path unchanged.",
        "4. If there is still no result or still no complete result after 120 seconds, treat the source URL as likely not publicly readable and only then allow U3 fallback.",
        "5. After U3 completes, obtain a public URL and submit it to U2 ASR again.",
        "6. If U3 or the second U2 attempt still fails, keep the fact card and return `incomplete`. Do not fabricate the main text or any analysis conclusion.",
        "",
        "## Scenario Notes",
        "",
        "- Single content task: run this flow only for the current item.",
        "- Creator batch task: apply U3 fallback only to the subset that still has no result after 120 seconds. Do not re-upload items that already succeeded.",
        "",
        "## Route Facts",
        "",
    ]

    for title, method, path, explanation in SERVICE_GUIDE_ROUTES:
        lines.append(f"### {title}")
        lines.append("")
        lines.append(f"- Purpose: {explanation}")

        entry = operation_index.get((method.upper(), path))
        if entry is None:
            lines.append("- This route was not found in the current OpenAPI.")
            lines.append("")
            continue

        tag, op = entry
        tag_relpath = tag_file_relpath(tag)
        contract_relpath = contract_file_relpath(tag)
        lines.append(f"- Tag: [`{tag}`](../{tag_relpath})")
        lines.append(f"- Route: `{method.upper()} {path}`")
        lines.append(f"- Auth: {summarize_security(spec, op)}")
        lines.append(f"- Parameters: {summarize_params(op.get('parameters') or [])}")
        lines.append(f"- Request body: {summarize_request_body(spec, op.get('requestBody') or {})}")
        lines.append(f"- Success response: {summarize_success_response(spec, op.get('responses') or {})}")
        lines.append(
            f"- Full contract: [`{contract_relpath}#{operation_anchor(method.upper(), path)}`](../{contract_relpath}#{operation_anchor(method.upper(), path)})"
        )
        lines.append("")

    lines.extend(
        [
            "## Execution Notes",
            "",
            "- This guide only defines route order and fallback order. It does not replace platform-specific detail-route selection.",
            "- The U1 source route depends on the platform, for example a Douyin or Xiaohongshu detail route. This guide only requires using the returned download URL first.",
            "- If the platform already returns usable `subtitle_raw`, map it directly to `asr_raw` instead of calling U2 or U3.",
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
