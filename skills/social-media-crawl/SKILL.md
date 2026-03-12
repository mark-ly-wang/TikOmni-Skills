---
name: social-media-crawl
description: Use this skill when the user asks about social media links, posts, creator homepages, comments, search results, rankings, livestreams, products, or wants to crawl / collect / fetch / retrieve / scrape social-media data; also trigger on 抓取 / 采集 / 获取 / 主页 / 评论 / 搜索 / 榜单 / 直播 / 商品 / 社交媒体.
---

# Social Media Crawl

## When To Use

- 当用户要处理任意社交媒体对象时使用，例如作品链接、帖子、线程、长文、作者主页、评论区、搜索结果、榜单、直播间、商品页。
- 当用户提到抓取、采集、获取、提取、主页、评论、搜索、榜单、直播、商品、社交媒体等需求时使用。
- 当输入是分享短链、作品 URL、帖子 URL、线程 URL、主页 URL、平台 ID、关键词或页面入口时使用。

## Supported Platforms

- 当前明确支持的平台包括：抖音、小红书、快手、B站、微博、TikTok、YouTube、Instagram、Threads、Twitter/X、Reddit、LinkedIn、视频号、公众号、头条、西瓜、知乎、Lemon8、皮皮虾。
- 其中固定 pipeline 当前只冻结 4 条：抖音单作品、抖音作者主页、小红书单作品、小红书作者主页。
- 除上述固定 pipeline 外，其他已支持平台与对象统一走本 skill 内的 MCP 通用链路。
- 完整平台目录与新增平台更新口径见官方文档：https://docs.tikomni.com

## What To Help With

- 识别平台和对象类型。
- 优先处理单作品、单帖子、线程、作者主页和内容集合。
- 获取事实字段、平台文案、字幕或转写文本。
- 返回结构化 JSON，并在需要时写入事实卡。

## Preferred Routing

- 凡是社交媒体对象，先进入本 skill；不要因为未命中固定 pipeline 就直接绕到 browser/CDP。
- 如果对象是以下 4 类，优先走固定 pipeline：
  1. 抖音单作品
  2. 小红书单作品
  3. 抖音作者主页
  4. 小红书作者主页
- 若未命中固定 pipeline，仍留在本 skill 内，按 `tools/list -> catalog.search -> endpoint.describe -> api.call` 走 MCP 通用链路。
- 仅当固定 pipeline 与 MCP 通用链路都不可用，或任务明确要求页面级交互且 API 无法满足时，才允许使用 browser/CDP 兜底，并在结果中记录原因。

## Working Style

- 先识别平台和对象类型，再决定固定 pipeline 或 MCP 通用链路。
- browser/CDP 是兜底，不是默认首选。
- 优先返回事实字段，不补充主观分析。
- 视频文本优先使用平台原生字幕；拿不到再走 ASR。
- 默认输出以结构化 JSON 和 Markdown 并主动落库。
- 当命中固定 pipeline 时，默认执行抓取并落库（强制）。

## Typical Examples

- 提取 X/Twitter 单条帖子正文与事实字段。
- 抓取 X/Twitter 线程并整理为统一结构化结果。
- 提取创作者主页资料与内容集合。
- 抓取评论区前 N 条。
- 抓取搜索结果、榜单、直播间或商品页。

## Workflow

1. 识别平台和对象类型。
2. 若命中固定 pipeline，直接运行固定脚本。
3. 若未命中固定 pipeline，先调用 `tools/list`，再按 `catalog.search -> endpoint.describe -> api.call` 选择最小 MCP 工具链。
4. 如果需要视频文本，执行 `u2.submit -> u2.query`；超过阈值仍未完成时走 U3 fallback。
5. 若固定 pipeline 与 MCP 通用链路都不足以完成任务，再考虑 browser/CDP 兜底，并记录前置失败原因。
6. 整理为结构化结果。
7. 若对象是作品，写入 `work_fact_card`。

## References

- MCP 使用契约：`references/mcp-usage-contract.md`
- 输出 envelope：`references/contracts/output-envelope.md`
- 作品事实卡字段：`references/contracts/work-fact-card-fields.md`
- 泛对象 MCP 指引：`references/guides/generic-mcp-objects.md`
- U2/U3 规则：`references/service-guides/u2-u3-mandatory-fallback.md`
- 固定 pipeline 指南：`references/pipelines/`
