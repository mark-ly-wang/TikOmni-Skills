---
name: tikomni-skill
description: Use this skill for cross-platform social content extraction, benchmarking, breakdown, copy/comment retrieval, and creator/account analysis across Douyin, Xiaohongshu, TikTok, YouTube, X and other supported platforms. 当用户说“对标、拆解、提取文案、分析作品/视频/图文、账号分析（如抖音/小红书/视频号/公众号）”或 asks for structured data or analysis for posts, videos, notes, comments, or creator homepages, trigger this skill.
---

# TikOmni Skill

Use TikOmni as a **general social-platform capability skill**, not as a narrow set of hardcoded routes.

## Do
- Parse the user intent first: platform, target object, quantity, fields needed, and desired output.
- Match fixed capabilities first via `references/capability-routing-matrix.md`.
- When fixed capabilities do not fit, use universal fallback with the API catalog and normalization rules.
- Return explicit `missing_fields`, `fallback_trace`, and `request_id` when available.
- Prefer reusable structured outputs/cards over loose prose.
- Read platform-specific references only when the task needs platform-specific route or field guidance.

## Do not
- Fabricate unavailable fields.
- Treat the current fixed capability list as the full boundary of TikOmni.
- Explain internal governance history or implementation backstory to the agent.

## Default Behavior
- Match fixed capabilities first; if none fits, use universal fallback.
- Prefer the minimal-cost route that can satisfy the user intent.
- Prefer app routes over web routes; prefer higher-version routes over lower-version routes within the same family.
- Respect the global TikOmni rate-limit and bounded-retry policy before preferring aggressive parallelism.
- Keep route decisions traceable with `fallback_trace` and `request_id` when available.
- Report unavailable data explicitly through `missing_fields`.
- Prefer structured, reusable outputs over loose prose.
- Read platform references only when the task needs platform-specific route or field guidance.

## Universal Workflow
1. Parse the user intent: platform, object type, quantity, fields needed, and target output.
2. Read `references/capability-routing-matrix.md` and check whether a fixed capability fits.
3. If a fixed capability fits, execute that route chain.
4. If not, read `references/routing-rules.md` and `references/api-catalog/index.md`, then select the minimal-cost route that satisfies the task.
5. Apply `references/normalize-rules.md` to normalize extracted fields.
6. Apply `references/output-markdown.md` to shape the final output/card/report.
7. If the task is platform-sensitive, read the relevant platform reference under `references/platforms/`.

## References (load as needed)
- Capability matrix: `references/capability-routing-matrix.md`
- Global routing policy: `references/routing-rules.md`
- Platform specifics: `references/platforms/xiaohongshu.md`, `references/platforms/douyin.md` (when needed)
- Normalize rules: `references/normalize-rules.md`
- Output markdown rules: `references/output-markdown.md`
- Copy/ASR playbook: `references/playbooks/copy-extract-rules.md`
- API catalog: `references/api-catalog/index.md`
- Prompt contracts: `references/prompt-contracts/`
