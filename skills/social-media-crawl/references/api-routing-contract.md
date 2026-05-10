# API Routing Contract

## Scope

This skill calls TikOmni API only and does not require any external server configuration.

Supported social-media tasks include single works, posts, creator homepages, comments, search results, rankings, livestreams, products, subtitles, transcripts, and structured fields.

## Required Inputs

- Auth: `TIKOMNI_API_KEY`.
- Default API base URL: `https://api.tikomni.com`.
- Optional override: `TIKOMNI_BASE_URL`.

Do not repeat the API key inside tool parameters.

## Required Route Order

1. Detect platform and capability.
2. If a fixed pipeline matches, run that fixed pipeline.
3. Otherwise resolve a TikOmni API endpoint:

```text
python scripts/core/resolve_api_endpoint.py --platform <platform> --capability <capability> --json '<context>'
```

4. Call the API by `endpoint_id`:

```text
python scripts/core/call_tikomni_api.py --endpoint-id <endpoint_id> --params '<json>'
```

5. For common tasks, the one-shot entry is allowed:

```text
python scripts/run_task.py --platform <platform> --capability <capability> --params '<json>'
```

## Hard Rules

- Do not construct TikOmni API paths manually.
- Do not pass arbitrary `path` or `method` values to callers.
- Do not call endpoint paths that are absent from `references/api-catalog/operations.json`.
- Resolve `endpoint_id` first, then call the API.
- Return recommended endpoint and alternatives to the user or agent.
- Do not automatically call alternatives; alternatives are explicit next choices.
- If platform or capability is ambiguous, return a clarification request instead of guessing.

## Variant Priority

For endpoints under the same platform and capability, default priority is:

```text
app_v3 > app_v2 > app_v1/app > web_v3 > web_v2 > web_v1/web
```

The catalog generator may apply deterministic specificity rules for common tasks such as hot search or article detail. All alternatives must remain visible.

## U2/U3

U2 and U3 stay inside this skill because they support video-to-text workflows:

- U2 handles ASR / transcription.
- U3 handles media upload or relay when a source media URL is not directly usable.

Use them only as TikOmni API service capabilities.

## Output Rules

- Keep factual fields separate from derived metadata.
- Include `request_id` when the API returns one.
- Include `endpoint_id`, `platform`, `capability`, `variant`, and `alternatives`.
- Include `completeness`, `missing_fields`, `error_reason`, and `extract_trace` in normalized task outputs.
