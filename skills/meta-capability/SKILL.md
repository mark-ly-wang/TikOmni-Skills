---
name: meta-capability
description: Use this skill for cross-platform content retrieval and analysis tasks. Trigger when the user asks to extract / fetch / inspect / organize / analyze, or 抓取 / 提取 / 查询 / 整理 / 分析, and the target is a concrete platform object such as a single content item, profile, comment thread, search result, ranking, livestream, or product page.
---

# Meta Capability

## When To Use

- Use this skill when the user already knows what they want to work on and wants a usable result.
- Use this skill for a single video, post, article, note, profile, creator page, comment thread, search result set, ranking, livestream, product page, or another concrete platform object.
- Use this skill when the user provides a link, share URL, page URL, platform ID, keyword, handle, or another clear entry point.
- Use this skill for general TikOmni tasks that require actual retrieval, extraction, organization, or analysis.

## What It Can Do

- Fetch and organize data for single content items.
- Fetch and organize data for profiles, creator pages, and content collections.
- Retrieve comments, replies, search results, rankings, livestream data, commerce-related data, and other supported platform objects.
- Extract captions, subtitles, transcripts, media URLs, author information, and engagement metrics when available.
- Return structured facts and analysis grounded in retrieved data.
- Return a reduced but still usable result when some fields are unavailable.

## Core Rules

- Start from the user's actual target object, not from the API catalog.
- Prefer the smallest route chain that can complete the task.
- Keep retrieved facts separate from inferred analysis.
- Base every conclusion on retrieved data only.
- Prefer platform-native text, subtitles, and structured fields first.
- If the task needs transcription and the media URL may not be publicly readable, follow the U2/U3 fallback guide.
- If required fields are missing, return the best clear partial result instead of fabricating data.

## Do Not

- Do not present guessed values as retrieved facts.
- Do not promise fields that the selected route chain cannot actually provide.
- Do not stop at route lookup if the user is clearly asking for actual retrieval or analysis.
- Do not stop the task just because a more specialized skill is unavailable; continue here when needed.

## Workflow

1. Read `references/api-capability-index.md` to identify the relevant platform, task type, auth pattern, tag file, and contract file.
2. Read the relevant files under `references/api-tags/` to confirm route summaries, key inputs, auth requirements, and key success responses.
3. Read the relevant files under `references/api-contracts/` only when exact field definitions, defaults, examples, or full success-response structures are needed.
4. If the task already matches a validated route chain, read `references/implemented-route-map.md` first.
5. If auth needs to be verified, run `python3 "skills/meta-capability/scripts/test_auth.py"`.
6. If a route needs to be called manually, run `python3 "skills/meta-capability/scripts/call_route.py" METHOD PATH --params-json '...' --body-json '...'`.
7. Read `references/execution-guidelines.md` to confirm object type, target fields, output shape, and fallback behavior.
8. If the task involves ASR timeout, non-public media URLs, or U3 media relay, read `references/service-guides/asr-u2-u3-fallback.md`.
9. Read `references/dispatch.md` to determine whether a more specialized skill is a better fit.
10. If a better specialized skill is available in the current skill workspace, hand off with the confirmed routes, retrieved facts, and intermediate findings.
11. If that specialized skill is missing, not installed, not checked out, or otherwise unavailable in the current workspace, continue in this skill and complete the task here.

## References

- API capability index: `references/api-capability-index.md`
- Tag-level route summaries: `references/api-tags/`
- Tag-level full contracts: `references/api-contracts/`
- Validated route chains: `references/implemented-route-map.md`
- Execution guidelines: `references/execution-guidelines.md`
- ASR and U3 fallback guide: `references/service-guides/asr-u2-u3-fallback.md`
- Dispatch guidance: `references/dispatch.md`

## Scripts

- Auth test: `scripts/test_auth.py`
- Manual route call: `scripts/call_route.py`
- Runtime defaults: `references/config-templates/defaults.yaml`
