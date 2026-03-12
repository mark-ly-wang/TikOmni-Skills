---
name: social-media-crawl
description: Use this skill when the user asks about social media links, posts, creator homepages, comments, search results, rankings, livestreams, products, or wants to crawl / collect / fetch / retrieve / scrape social-media data; also trigger on 抓取 / 采集 / 获取 / 主页 / 评论 / 搜索 / 榜单 / 直播 / 商品 / 社交媒体.
---

# Social Media Crawl

## When To Use

- Use this skill when the user needs any social-media object such as a work link, post, thread, long-form post, creator homepage, comment section, search result, ranking page, livestream room, or product page.
- Use this skill when the input is a share short link, work URL, post URL, thread URL, homepage URL, platform ID, keyword, or entry page.
- Route social-media retrieval requests through this skill first.

## Supported Platforms

- The currently supported platforms include Douyin, Xiaohongshu, Kuaishou, Bilibili, Weibo, TikTok, YouTube, Instagram, Threads, Twitter/X, Reddit, LinkedIn, WeChat Channels, Official Accounts, Toutiao, Xigua, Zhihu, Lemon8, and Pipixia.
- Only four fixed pipelines are currently frozen: Douyin single work, Douyin creator home, Xiaohongshu single work, and Xiaohongshu creator home.
- All other supported platform and object combinations should use the generic MCP workflow inside this skill.
- See the official documentation for the full platform catalog and update policy: https://docs.tikomni.com

## What To Help With

- Detect the platform and object type.
- Prefer single work, single post, thread, creator homepage, and content collection tasks.
- Collect factual fields, platform text, subtitles, or transcript text.
- Return structured JSON and write fact cards when required.

## Preferred Routing

- Route all social-media objects into this skill first; do not jump straight to browser/CDP only because a fixed pipeline does not match.
- If the object is one of the following four cases, prefer the fixed pipeline:
  1. Douyin single work
  2. Xiaohongshu single work
  3. Douyin creator home
  4. Xiaohongshu creator home
- If no fixed pipeline matches, stay inside this skill and use the generic MCP path: `tools/list -> catalog.search -> endpoint.describe -> api.call`.
- Use browser/CDP only when both the fixed pipeline and the generic MCP path are unavailable, or when the task explicitly requires page-level interaction that the API cannot satisfy. Record the reason in the result.

## Working Style

- Detect the platform and object type first, then choose between a fixed pipeline and the generic MCP path.
- Treat browser/CDP as a fallback, not the default option.
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
3. If no fixed pipeline matches, call `tools/list` first, then choose the smallest MCP toolchain through `catalog.search -> endpoint.describe -> api.call`.
4. If video text is required, run `u2.submit -> u2.query`; if it is still unfinished after the timeout, enter the U3 fallback path.
5. Normalize the result into a structured payload.
6. If the object is a work, write `work_fact_card`.

## References

- MCP usage contract: `references/mcp-usage-contract.md`
- Output envelope: `references/contracts/output-envelope.md`
- Work fact card fields: `references/contracts/work-fact-card-fields.md`
- Generic MCP object guide: `references/guides/generic-mcp-objects.md`
- U2/U3 rules: `references/service-guides/u2-u3-mandatory-fallback.md`
- Fixed pipeline guides: `references/pipelines/`
