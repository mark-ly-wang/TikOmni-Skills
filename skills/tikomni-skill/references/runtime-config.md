# Runtime Config Template

Edit this file to customize skill behavior.

## 0. What does “local config” mean?

1. “Local” means the environment where your agent is currently running.
2. If you run from CLI/CUI on your laptop, local means your laptop.
3. If you run in CI/server, local means that CI runner/server.

## 1. Quick Start

1. Copy `skills/tikomni-skill/env.example` to a private env file (for example, workspace `.env` or `skills/tikomni-skill/.env.local`).
2. Fill in your real `TIKOMNI_API_KEY`.
3. Edit this file for output folders, metadata, and extraction behavior.
4. On execution, read this file first, then resolve the API key via `auth_env_key`.

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

1. `env_file` is a declared path and should never be printed with secret values.
2. Real API key must come from environment variables, never from markdown content.

## 4. Output Layout

```yaml
# Output root directory
root_dir: docs/skill-output
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
```

## 7. Routing Policy

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

## 8. FAQ

1. Where should I configure local env?
   - In local CLI/CUI runs: workspace `.env`.
   - In CI runs: CI secrets or private env file loaded at runtime.
2. How to prevent key leakage?
   - Never commit real `.env` files.
   - Never print `TIKOMNI_API_KEY` in logs.
