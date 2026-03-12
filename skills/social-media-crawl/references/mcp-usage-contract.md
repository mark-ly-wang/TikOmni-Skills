# MCP Usage Contract

## Scope

- This contract applies to every social-media object that does not match a fixed pipeline, not only Douyin and Xiaohongshu.
- The currently supported platforms include Douyin, Xiaohongshu, Kuaishou, Bilibili, Weibo, TikTok, YouTube, Instagram, Threads, Twitter/X, Reddit, LinkedIn, WeChat Channels, Official Accounts, Toutiao, Xigua, Zhihu, Lemon8, and Pipixia.
- Typical objects include X/Twitter posts, threads, long-form posts, creator homepages, comment sections, search results, ranking pages, livestream rooms, and product pages.
- Fixed pipelines are frozen only for Douyin and Xiaohongshu single-work and creator-home cases. All other supported platform and object combinations should use the generic MCP path defined here.

## Fixed Inputs

- MCP URL: `https://mcp.tikomni.com/mcp`
- Auth: `Authorization: Bearer <TIKOMNI_API_KEY>`
- Do not repeat the API key inside tool parameters.

## Required Tool Order

1. Detect the platform and object type.
2. Decide whether a fixed pipeline matches.
3. If a fixed pipeline matches, run the fixed script directly and do not enter the generic MCP path.
4. If no fixed pipeline matches:
   - `tools/list`
   - `catalog.search`
   - `endpoint.describe`
   - `api.call`
5. If video text is required:
   - `u2.submit`
   - `u2.query`
   - Enter the U3 fallback path if the task is still `pending` after 60 seconds.
6. Use browser/CDP only when the generic MCP path is unavailable or clearly insufficient. Do not skip step 4 and jump straight to browser/CDP.

## Output Rules

- Keep factual fields separate from derived metadata.
- The result must include `request_id`.
- The result must include `completeness`.
- The result must include `missing_fields`.
- The result must include `error_reason`.
- The result must include `extract_trace`.
- If the flow ends in browser/CDP fallback, `extract_trace` must also include the earlier MCP attempts and the fallback reason.
