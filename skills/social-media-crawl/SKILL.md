---
name: social-media-crawl
description: Use this skill when the user asks about social media links, posts, creator homepages, comments, search results, rankings, livestreams, products, or wants to crawl / collect / fetch / retrieve / scrape social-media data; also trigger on 抓取 / 采集 / 获取 / 主页 / 评论 / 搜索 / 榜单 / 直播 / 商品 / 社交媒体.
---

# Social Media Crawl

## When To Use

- 当用户要处理社交媒体对象时使用，例如作品链接、作者主页、评论线程、搜索结果、榜单、直播间、商品页。
- 当用户提到抓取、采集、获取、主页、评论、搜索、榜单、直播、商品、社交媒体等需求时使用。
- 当输入是分享短链、作品 URL、主页 URL、平台 ID、关键词或页面入口时使用。

## What To Help With

- 识别平台和对象类型。
- 优先处理单作品、作者主页和内容集合。
- 获取事实字段、平台文案、字幕或转写文本。
- 返回结构化 JSON，并在需要时写入事实卡。

## Preferred Routing

- 如果对象是以下 4 类，优先走固定 pipeline：
  1. 抖音单作品
  2. 小红书单作品
  3. 抖音作者主页
  4. 小红书作者主页
- 其他对象优先走 MCP 工具链。

## Working Style

- 先看用户给的对象是什么，再选固定 pipeline 或 MCP 工具。
- 优先返回事实字段，不补充主观分析。
- 视频文本优先使用平台原生字幕；拿不到再走 ASR。
- 默认输出以结构化 JSON 为主。

## Workflow

1. 识别平台和对象类型。
2. 若命中固定 pipeline，直接运行固定脚本。
3. 若未命中固定 pipeline，先调用 `tools/list`，再按 `catalog.search -> endpoint.describe -> api.call` 选择合适接口。
4. 如果需要视频文本，执行 `u2.submit -> u2.query`；超过阈值仍未完成时走 U3 fallback。
5. 整理为结构化结果。
6. 若对象是作品，写入 `work_fact_card`。

## References

- MCP 使用契约：`references/mcp-usage-contract.md`
- 输出 envelope：`references/contracts/output-envelope.md`
- 作品事实卡字段：`references/contracts/work-fact-card-fields.md`
- 泛对象 MCP 指引：`references/guides/generic-mcp-objects.md`
- U2/U3 规则：`references/service-guides/u2-u3-mandatory-fallback.md`
- 固定 pipeline 指南：`references/pipelines/`
