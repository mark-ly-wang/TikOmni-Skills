# Runtime Config Template

Edit this file to customize skill behavior.

## 0. Local Config Scope

1. "Local" is the environment where your agent is running.
2. For laptop CLI/CUI runs, local means your laptop.
3. For CI/server runs, local means that runner/server.

## 1. Quick Start

1. Copy `skills/tikomni-skill/env.example` to a private env file (for example, workspace `.env` or `skills/tikomni-skill/.env.local`).
2. Fill in your real `TIKOMNI_API_KEY`.
3. Edit this file for output folders, metadata, and extraction behavior.
4. On execution, `scripts/cli/run_tikomni_extract.py` loads config first, then resolves API key via `auth_env_key`.

## 2. Profile

```yaml
# Profile name for scenario separation
profile_name: default
# Owner/operator label
owner: ""
# Output language, e.g. en or zh-CN
language: en
```

## 3. API Runtime

```yaml
# API base URL
base_url: https://api.tikomni.com
# Environment variable name that stores API key
auth_env_key: TIKOMNI_API_KEY
# Request timeout in milliseconds
timeout_ms: 60000
# Optional: declared env file path for team conventions
env_file: .env
```

Notes:

1. `env_file` is a declared path and must never be printed with secret values.
2. If `env_file` is relative, resolve it from repository root (not CWD).
3. If `env_file` is omitted, default is `<repo_root>/.env`.
4. Real API key must come from environment variables, never from markdown content.

## 4. Output Layout

`TIKOMNI_OUTPUT_ROOT` controls runner outputs (`_runs/results/_errors`) only.

Default behavior:
- Unified entry (`run_tikomni_extract`) persists JSON by default for all registered workflows.
- success -> `<runs_dir>/<results_dir>/<YYYYMMDD>/<timestamp>-<platform>-<id>.json`
- error -> `<errors_dir>/<YYYYMMDD>/<timestamp>-<platform>-<id>.json`
- fixed pipelines do not expose a per-run persistence disable switch.

Card markdown is routed by `TIKOMNI_CARD_ROOT` + card routes.

Default behavior:
- Fixed pipelines always write cards and workflow JSON artifacts.
- Unified entry + fixed platform handlers hard-reject attempts to skip card writing or output persistence.
- Do not assume card files are always under output root.

```yaml
# Output root directory (default resolves from repo root, not current CWD)
root_dir: tikomni-output
# Run trace sub-directory
runs_dir: _runs
# Result sub-directory
results_dir: results
# Error sub-directory
errors_dir: _errors
# Filename pattern placeholders: {type} {timestamp} {job_id}
filename_pattern: "{type}-{timestamp}-{job_id}.md"
```

## 5. Markdown Defaults

```yaml
# Frontmatter title prefix
title_prefix: Tikomni Extraction
# Default frontmatter tags
default_tags:
  - tikomni
  - extraction
# Extra frontmatter fields as key-value object
frontmatter_extra: {}
```

## 6. Extraction Policy

```yaml
# Enable per-item copy extraction in homepage flows
homepage_batch_copy_enabled: true
# Copy language strategy: auto / zh-CN / en
copy_language: auto
# Prefer subtitle fields first for Xiaohongshu
xhs_subtitle_first: true
# Force U2 for Douyin copy extraction
douyin_copy_via_u2: true
# Conservative retry: only retry on U2 polling timeout; configurable 0~3 retries
u2_timeout_retry:
  enabled: true
  max_retries: 3
```

Notes:

1. U2 submit no longer accepts or forwards `idempotency-key` headers.
2. Non-timeout errors keep original behavior and are not retried by `u2_timeout_retry`.

## 7. Registry + Routing Runtime

```yaml
# Endpoint priority for same platform + same intent
endpoint_priority:
  - app
  - web_v2
  - web
# Enable fallback
fallback_enabled: true
# Maximum fallback attempts
max_fallback_attempts: 2
```

Notes:

1. `--content-kind auto` uses registry default mapping per platform.
2. Registry is mapping-only; policy priority stays in capability matrix/routing rules.

## 8. FAQ

1. Where should I configure local env?
   - In local CLI/CUI runs: workspace `.env`.
   - In CI runs: CI secrets or private env file loaded at runtime.
2. Which root controls what?
   - `TIKOMNI_OUTPUT_ROOT`: runner output files (`_runs/results/_errors`); fixed pipelines always persist workflow JSON artifacts and do not expose a disable switch.
   - `TIKOMNI_CARD_ROOT`: markdown cards; fixed pipelines always write cards and do not expose a disable switch.
3. How to verify which source provided the key?
   - Run `python3 scripts/cli/check_tikomni_readiness.py`.
   - It prints `key_source` and `source_chain` only (no secret value).
4. How to prevent key leakage?
   - Never commit real `.env` files.
   - Never print `TIKOMNI_API_KEY` in logs.
