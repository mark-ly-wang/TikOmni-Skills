---
name: tikomni-skill
description: Use this skill for social content benchmark/breakdown/extract tasks (Douyin/Xiaohongshu/TikTok/YouTube/X and other supported platforms). 当用户说“对标、拆解、提取文案、分析作品/视频/图文、账号分析（如抖音/小红书/视频号/公众号）”或 asks to analyze posts/videos/creator accounts and fetch structured data/copy/comments, trigger this skill.
---

# TikOmni Skill

## Mission
Complete cross-platform content tasks with traceable outputs:
- analyze single posts/videos/images
- analyze creator/author accounts (homepage-level)
- extract structured data/copy/comments
- produce reusable markdown artifacts (cards/reports)

## Scope & Boundaries
- Use TikOmni workflows for supported platforms and return structured outputs.
- Never fabricate unavailable data; report gaps via `missing_fields` with reasons.
- Keep route decisions traceable via `fallback_trace` and `request_id` when available.
- Follow Prompt-First analysis style (prompt-led output constraints, minimal format validation only).

## Default Behavior
- `--write-card` is enabled by default (disable with `--no-write-card`).
- Unified output persistence is enabled by default (disable with `--no-persist-output`).
- Author-home defaults: latest-first + cursor pagination + hard cap `max_items<=200` (all platforms).

## Trigger Examples / 触发示例
- “帮我对标拆解这条抖音视频”
- “提取这个小红书笔记文案并分析”
- “做这个博主/自媒体账号分析（主页）”
- “分析这个视频号/公众号账号，给我对标结论”
- “benchmark or breakdown this TikTok/YouTube/X post”
- “analyze this creator account and extract structured fields/comments”

## Universal Workflow
1. Parse user intent and constraints (platform, content type, quantity, output form).
2. Match route via capability matrix first.
3. If fixed capability is matched, execute the fixed route chain.
4. If fixed capability is not matched, enter Universal Fallback (agent-led routing using API capability catalog + user intent).
5. Normalize extracted fields using shared normalization rules.
6. Emit required trace/contract fields (`missing_fields`, `fallback_trace`, `request_id`, etc.).
7. Produce markdown output/cards according to output rules.

## Universal Fallback Method (agent-led)
When fixed routes are not matched, the agent should:
1. Read capability catalog and routing references.
2. Select candidate endpoints by intent fit + data coverage + stability.
3. Execute a minimal-cost route chain and record selection/abandon decisions in `fallback_trace`.
4. Return explicit `missing_fields` for unavailable data instead of fabricating.

## Quality Bar (DoD)
A run is done only when all are true:
1. Required contract fields are present:
   - `missing_fields`
   - `fallback_trace`
   - `request_id`
   - `card_write`
   - `output_persist`
2. Missing data is explicit and non-fabricated.
3. Route decisions are traceable and reproducible.
4. Output is readable and directly reusable in downstream workflows.

## References (load as needed)
- Capability matrix: `references/capability-routing-matrix.md`
- Routing rules: `references/routing-rules.md`
- Normalize rules: `references/normalize-rules.md`
- Output markdown rules: `references/output-markdown.md`
- API catalog: `references/api-catalog/index.md`
- Prompt contracts: `references/prompt-contracts/`
