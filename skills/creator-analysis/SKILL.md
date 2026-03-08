---
name: creator-analysis
description: Use this skill for creator, account profile, and content-collection retrieval, benchmarking, breakdown, and analysis. Trigger when the user asks to analyze creator / analyze account / profile analysis / creator benchmark / creator breakdown, or 创作者分析 / 账号分析 / 主页分析 / 博主分析 / 博主对标 / 账号拆解 / 作者卡 / 主页作品汇总, and the target is a creator, account profile, channel, or content collection rather than one content item.
---

# Creator Analysis

## When To Use

- Use this skill when the target is a creator, account, profile page, channel, or content collection rather than a single content item.
- Use this skill when the user wants a creator card, a full set of work cards, sampled explanations, or aggregated creator-level conclusions.
- Use this skill when multiple videos under one profile should go through batch ASR first.
- Use this skill when the user provides a profile URL, creator handle, account identifier, channel entry, or another creator-level entry point.

## What It Can Do

- Fetch and normalize creator-side fact fields.
- Fetch and normalize the full content collection under a profile.
- Produce work fact cards for the retrieved items.
- Run batch ASR for video items when needed.
- Complete bucketing, sampling, sampled explanations, and creator-level analysis.
- Return creator cards, work cards, and aggregated conclusions.

## Core Rules

- Keep the task scoped to a creator, account profile, or content collection.
- Prefer the platform guide first. Only go back to API discovery references when the guide is insufficient.
- Keep fact cards for all retrieved works, but do not run per-work deep LLM analysis.
- Prefer batch ASR for video items, with up to 100 links per batch.
- Let sampled-work explanation fields come from one batch LLM step only.
- Treat `author_analysis_v2` as the formal creator-level analysis object.
- If `analysis_eligibility=incomplete`, keep the fact card but exclude the item from sampling, sampled explanations, and creator-level analysis.

## Do Not

- Do not paste sampled explanations directly into every work-card body.
- Do not expose platform process fields directly in the final card body.
- Do not introduce per-work LLM explanations inside the creator path.
- Do not collapse a creator task into single-item analysis when the user clearly wants creator-level output.

## Workflow

1. Identify the platform and confirm that the target is a creator, account profile, channel, or content collection.
2. Read `references/contracts/creator-card-fields.md` to confirm required creator-card fields.
3. Read `references/contracts/work-card-fields.md` to confirm required work-card fields for the collected items.
4. Read the platform guide first:
   - Douyin: `references/platform-guides/douyin.md`
   - Xiaohongshu: `references/platform-guides/xiaohongshu.md`
   - Other platforms: `references/platform-guides/generic.md`
5. If video items are involved, read `references/service-guides/asr-u2-u3-fallback.md` and then `references/asr-orchestration.md` to run batch ASR and fallback.
6. Read `references/api-capability-index.md`, `references/api-tags/`, and `references/api-contracts/` only when the platform guide does not provide enough route or field detail.
7. Read `references/workflow.md` to complete bucketing, sampling, sampled explanations, and `author_analysis_v2`.
8. Return the creator card, work cards, and aggregated conclusions.

## References

- API capability index: `references/api-capability-index.md`
- Tag-level route summaries: `references/api-tags/`
- Tag-level full contracts: `references/api-contracts/`
- U2/U3 ASR fallback: `references/service-guides/asr-u2-u3-fallback.md`
- Creator-card fields: `references/contracts/creator-card-fields.md`
- Work-card fields: `references/contracts/work-card-fields.md`
- ASR orchestration: `references/asr-orchestration.md`
- Creator workflow: `references/workflow.md`
- Author-analysis prompt contract: `references/prompt-contracts/author-analysis-v2.md`
- Sampled-explanations prompt contract: `references/prompt-contracts/sampled-work-batch-explanations.md`
- Author-analysis schema: `references/schemas/author-analysis-v2.schema.json`
- Sampled-explanations schema: `references/schemas/sampled-work-batch-explanations.schema.json`
- Generic platform guide: `references/platform-guides/generic.md`
- Douyin guide: `references/platform-guides/douyin.md`
- Xiaohongshu guide: `references/platform-guides/xiaohongshu.md`
