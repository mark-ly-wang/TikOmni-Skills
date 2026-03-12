# MCP Usage Contract

## Scope

- 本契约适用于所有未命中固定 pipeline 的社交媒体对象，不限于抖音和小红书。
- 当前明确支持的平台包括：抖音、小红书、快手、B站、微博、TikTok、YouTube、Instagram、Threads、Twitter/X、Reddit、LinkedIn、视频号、公众号、头条、西瓜、知乎、Lemon8、皮皮虾。
- 典型对象包括 X/Twitter 帖子、线程、长文、作者主页、评论区、搜索结果、榜单、直播间、商品页。
- 固定 pipeline 仅冻结抖音/小红书的单作品与作者主页；其余已支持平台默认按本契约走 MCP 通用链路。

## Fixed Inputs

- MCP URL: `https://mcp.tikomni.com/mcp`
- Auth: `Authorization: Bearer <TIKOMNI_API_KEY>`
- 不在工具参数中重复传 API key

## Required Tool Order

1. 识别平台和对象类型
2. 判断是否命中固定 pipeline
3. 若命中固定 pipeline，直接执行固定脚本，不进入 MCP 通用链路
4. 若不命中固定 pipeline：
   - `tools/list`
   - `catalog.search`
   - `endpoint.describe`
   - `api.call`
5. 若需要视频文本：
   - `u2.submit`
   - `u2.query`
   - 超过 60 秒仍 `pending` 时进入 U3 fallback
6. 只有在 MCP 通用链路不可用或明显不足时，才允许 browser/CDP 兜底；不得跳过第 4 步直接进入 browser/CDP

## Output Rules

- 事实字段与派生元数据分离
- 结果必须包含 `request_id`
- 结果必须包含 `completeness`
- 结果必须包含 `missing_fields`
- 结果必须包含 `error_reason`
- 结果必须包含 `extract_trace`
- 若最终进入 browser/CDP 兜底，`extract_trace` 必须包含前置 MCP 尝试记录与兜底原因
