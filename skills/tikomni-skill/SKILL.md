---
name: tikomni-skill
description: Direct HTTP Tikomni skill for u1/u2 public APIs. Use when users ask to fetch Douyin/Xiaohongshu homepage data, extract copy/subtitles/transcripts, call Tikomni APIs by intent, or save extraction outputs as Markdown. Also trigger on Chinese requests like “抓抖音主页”“抓小红书主页”“提取文案/字幕/逐字稿”. Homepage extraction for Douyin/Xiaohongshu must run fixed playbooks.
---

# Tikomni Skill

## Goal

Call Tikomni APIs via direct HTTP and output `raw + normalized` data with Markdown artifacts.

## Required Setup

1. Set `TIKOMNI_API_KEY` (template file: `skills/tikomni-skill/env.example`).
2. Use `https://api.tikomni.com` as base URL.
3. Never print API keys in logs or markdown.
4. Read runtime config first:
   - English: `references/runtime-config.md`
   - 中文: `references/runtime-config.zh-CN.md`
5. If user provides a custom config path, use that path as highest priority.
6. If runtime config defines `env_file`, load it silently (no secret echo), then resolve `auth_env_key`.

## Execution Flow

1. Load runtime config document and resolve API/output policy from config.
2. Detect whether the request matches a fixed sub-function.
3. If matched to Douyin/Xiaohongshu homepage extraction, run the fixed playbook only.
4. Otherwise, route from `references/api-catalog` using intent.
5. Follow endpoint priority from runtime config; if not configured, use default `app > web_v2 > web`.
6. Apply copy rules:
   - Douyin copy extraction always uses U2.
   - Xiaohongshu copy extraction checks subtitle fields first, then U2 fallback.
7. Write markdown outputs using runtime config output layout, with routing trace, fallback trace, and `request_id`.

## Defaults

1. Douyin homepage default sorting is latest: `sort_type=0`.
2. Default extraction window: `limit=20`, `pages_max=50`.
3. If user gives quantity constraints, pass them into API params with safe caps.
4. Batch per-item transcript extraction is enabled by default for homepage flow and only applies to `video_model=video` with `13s < duration_ms <= 15min`.

## References

1. Routing rules: `references/routing-rules.md` (中文: `references/routing-rules.zh-CN.md`)
2. Normalize rules: `references/normalize-rules.md` (中文: `references/normalize-rules.zh-CN.md`)
3. Douyin homepage playbook: `references/playbooks/douyin-home-extract.md` (中文: `references/playbooks/douyin-home-extract.zh-CN.md`)
4. Xiaohongshu homepage playbook: `references/playbooks/xiaohongshu-home-extract.md` (中文: `references/playbooks/xiaohongshu-home-extract.zh-CN.md`)
5. Copy extraction rules: `references/playbooks/copy-extract-rules.md` (中文: `references/playbooks/copy-extract-rules.zh-CN.md`)
6. Markdown output rules: `references/output-markdown.md` (中文: `references/output-markdown.zh-CN.md`)
7. Customization guide: `references/customization-guide.md` (中文: `references/customization-guide.zh-CN.md`)
8. Configuration guide: `references/configuration.md` (中文: `references/configuration.zh-CN.md`)
9. Runtime config template: `references/runtime-config.md` (中文: `references/runtime-config.zh-CN.md`)
10. Full API catalog: `references/api-catalog/index.md`
