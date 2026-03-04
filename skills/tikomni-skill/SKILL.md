---
name: tikomni-skill
description: Direct HTTP Tikomni skill for u1/u2 public APIs. Use when users ask to fetch Douyin/Xiaohongshu homepage data, extract copy/subtitles/transcripts, call Tikomni APIs by intent, or save extraction outputs as Markdown. Homepage extraction for Douyin/Xiaohongshu must run fixed playbooks.
---

# Tikomni Skill

## Goal

Call Tikomni APIs via direct HTTP and output `raw + normalized` data with Markdown artifacts.

## Required Setup

1. Set `TIKOMNI_API_KEY` (template file: `skills/tikomni-skill/env.example`).
2. Use `https://api.tikomni.com` as base URL.
3. Never print API keys in logs or markdown.
4. Read runtime config first: `references/runtime-config.md`.
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

1. Routing rules: `references/routing-rules.md`
2. Normalize rules: `references/normalize-rules.md`
3. Douyin homepage playbook: `references/playbooks/douyin-home-extract.md`
4. Xiaohongshu homepage playbook: `references/playbooks/xiaohongshu-home-extract.md`
5. Copy extraction rules: `references/playbooks/copy-extract-rules.md`
6. Markdown output rules: `references/output-markdown.md`
7. Runtime config reference: `references/runtime-config.md`
8. Script defaults template (YAML): `references/config-templates/defaults.yaml`
9. Full API catalog: `references/api-catalog/index.md`
10. Benchmark card prompt contracts: `references/prompt-contracts/`
11. Topic contract: `references/prompt-contracts/topic.md`
12. Style contract: `references/prompt-contracts/style.md`
13. Hook contract: `references/prompt-contracts/hook.md`
14. Structure contract: `references/prompt-contracts/structure.md`
15. CTA contract: `references/prompt-contracts/cta.md`
16. Summary contract: `references/prompt-contracts/summary.md`
17. ASR clean contract: `references/prompt-contracts/asr-clean.md`
18. Insight contract: `references/prompt-contracts/insight.md`
