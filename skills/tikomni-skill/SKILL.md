---
name: tikomni-skill
description: Use this skill for cross-platform social content extraction, benchmarking, breakdown, copy/comment retrieval, and creator/account analysis across Douyin, Xiaohongshu, TikTok, YouTube, X and other supported platforms. 当用户说“对标、拆解、提取文案、分析作品/视频/图文、账号分析（如抖音/小红书/视频号/公众号）”或 asks for structured data or analysis for posts, videos, notes, comments, or creator homepages, trigger this skill.
---

# TikOmni Skill

Use TikOmni as a **general social-platform capability skill**, not as a narrow set of hardcoded routes.

## Do
- Parse the user intent first: platform, target object, quantity, fields needed, and desired output.
- Match fixed capabilities first via `references/capability-routing-matrix.md`.
- If a fixed capability matches, execute that TikOmni pipeline before producing the final output.
- When fixed capabilities do not fit, use universal API fallback with the API catalog and normalization rules.
- Keep TikOmni API-first and route-driven for both fixed-capability and universal-fallback paths.
- Return explicit `missing_fields`, `fallback_trace`, and `request_id` when available.
- Prefer reusable structured outputs/cards over loose prose.
- Read platform-specific references only when the task needs platform-specific route or field guidance.
- If no suitable API route can satisfy the request, report that limitation explicitly.

## Do not
- Fabricate unavailable fields.
- Treat the current fixed capability list as the full boundary of TikOmni.
- Explain internal governance history or implementation backstory to the agent.
- Do not use browser inspection or `web_fetch` for TikOmni capability selection.
- Do not use browser/manual observation as a fallback route inside this skill.
- Do not replace API extraction with browser/manual extraction.
- Do not present manual observation as a TikOmni result.
- Do not silently downgrade to browser/manual analysis when an API route fails.

## Default Behavior
- TikOmni is API-first and route-driven.
- Match fixed capabilities first; if one matches, execute that pipeline.
- If no fixed capability matches, use the universal API fallback path.
- Prefer the minimal-cost API route that can satisfy the user intent.
- Prefer app routes over web routes; prefer higher-version routes over lower-version routes within the same family.
- Respect the global TikOmni rate-limit and bounded-retry policy before preferring aggressive parallelism.
- Keep route decisions traceable with `fallback_trace` and `request_id` when available.
- Report unavailable data explicitly through `missing_fields`.
- Prefer structured, reusable outputs over loose prose.
- Read platform references only when the task needs platform-specific route or field guidance.
- If no suitable API route is available, report the limitation explicitly instead of switching to browser/manual analysis.

## Result Labeling Rules
- Call it a standard TikOmni result only when it is produced by the selected API pipeline/route.
- Call it a fallback result only when it comes from an explicit API fallback route with traceable fallback information.
- Call it manual observation only when it comes from browser/manual inspection, and do not present it as a TikOmni pipeline result.

## Universal Workflow
1. Parse the user intent: platform, object type, quantity, fields needed, and target output.
2. Read `references/capability-routing-matrix.md` and check whether a fixed capability fits.
3. If a fixed capability fits, execute that pipeline.
4. If no fixed capability fits, read `references/routing-rules.md` and `references/api-catalog/index.md`, then select the minimal-cost API route that satisfies the task.
5. Apply `references/normalize-rules.md` to normalize extracted fields.
6. Apply `references/output-markdown.md` to shape the final output/card/report.
7. If the task is platform-sensitive, read the relevant platform reference under `references/platforms/`.
8. If no API route can satisfy the task, state that explicitly and expose `missing_fields`, `fallback_trace`, and `request_id` when available.

## References (load as needed)
- Capability matrix: `references/capability-routing-matrix.md`
- Global routing policy: `references/routing-rules.md`
- Platform specifics: `references/platforms/xiaohongshu.md`, `references/platforms/douyin.md` (when needed)
- Normalize rules: `references/normalize-rules.md`
- Output markdown rules: `references/output-markdown.md`
- Copy/ASR playbook: `references/playbooks/copy-extract-rules.md`
- API catalog: `references/api-catalog/index.md`
- Prompt contracts: `references/prompt-contracts/`
