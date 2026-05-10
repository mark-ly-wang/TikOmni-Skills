---
name: social-media-crawl
description: Use this skill when the user asks to fetch social-media data through TikOmni API, including links, posts, creator homepages, comments, search results, rankings, livestreams, products, subtitles, transcripts, or structured fields; also trigger on 抓取 / 采集 / 获取 / 主页 / 评论 / 搜索 / 榜单 / 直播 / 商品 / 社交媒体.
---

# Social Media Crawl

## When To Use

- Use this skill when the user needs TikOmni API data for a social-media object such as a work link, post, thread, long-form post, creator homepage, comment section, search result, ranking page, livestream room, or product page.
- Use this skill when the input is a share short link, work URL, post URL, thread URL, homepage URL, platform ID, keyword, or entry page.
- Route social-media retrieval requests through this skill first and call TikOmni API only.

## Supported Platforms

- The currently supported platforms include Douyin, Xiaohongshu, Kuaishou, Bilibili, Weibo, TikTok, YouTube, Instagram, Threads, Twitter/X, Reddit, LinkedIn, WeChat Channels, Official Accounts, Toutiao, Xigua, Zhihu, Lemon8, and Pipixia.
- Only four fixed pipelines are currently frozen: Douyin single work, Douyin creator home, Xiaohongshu single work, and Xiaohongshu creator home.
- All other supported platform and object combinations should use the API-only resolver and caller bundled with this skill.
- See the official documentation for the full platform catalog and update policy: https://docs.tikomni.com

## What To Help With

- Detect the platform, capability, and object type.
- Resolve a TikOmni API `endpoint_id` before making any request.
- Show the recommended endpoint and available API alternatives.
- Prefer single work, single post, thread, creator homepage, and content collection tasks.
- Collect factual fields, platform text, subtitles, or transcript text.
- Return structured JSON and write fact cards when required.

## Preferred Routing

- Route all social-media objects into this skill first.
- Do not construct TikOmni API paths manually.
- Do not pass arbitrary `path` or `method` values to API callers.
- If the object is one of the following four cases, prefer the fixed pipeline:
  1. Douyin single work
  2. Xiaohongshu single work
  3. Douyin creator home
  4. Xiaohongshu creator home
- If no fixed pipeline matches, run `scripts/core/resolve_api_endpoint.py` first, then call `scripts/core/call_tikomni_api.py` with the returned `endpoint_id`.
- For common deterministic tasks, prefer `scripts/run_task.py`.
- If the resolver cannot determine a platform or capability, return a structured clarification request instead of guessing an endpoint.

## Working Style

- Detect the platform and object type first, then choose between a fixed pipeline and API-only resolver/caller.
- Prioritize factual fields and avoid subjective analysis.
- Prefer native subtitles for video text; use ASR only when subtitles are unavailable.
- Default to structured JSON plus Markdown and persist outputs proactively.
- When a fixed pipeline matches, execute it and persist outputs by default.

## Typical Examples

- Extract the body text and factual fields from a single X/Twitter post.
- Collect TikTok comment data and normalize it into a unified structured result.
- Extract a creator profile and content collection from a homepage.
- Collect the top N comments from a comment section.
- Collect search results, ranking pages, livestream rooms, or product pages.

## Workflow

1. Detect the platform and object type.
2. If a fixed pipeline matches, run the fixed script directly.
3. If no fixed pipeline matches, resolve platform + capability to an `endpoint_id` with `scripts/core/resolve_api_endpoint.py`.
4. Call TikOmni API with `scripts/core/call_tikomni_api.py`; never pass arbitrary API paths.
5. If video text is required, use U2 ASR; use U3 media upload only to support video-to-text when media URLs are not directly usable.
6. Normalize the result into a structured payload.
7. If the object is a work, write `work_fact_card`.

## References

- API routing contract: `references/api-routing-contract.md`
- Output envelope: `references/contracts/output-envelope.md`
- Work fact card fields: `references/contracts/work-fact-card-fields.md`
- U2/U3 rules: `references/service-guides/u2-u3-mandatory-fallback.md`
- Fixed pipeline guides: `references/pipelines/`
