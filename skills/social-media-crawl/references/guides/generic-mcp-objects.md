# Generic MCP Objects Guide

以下对象在首期不冻结细粒度 schema：

- 评论线程
- 搜索结果
- 榜单
- 直播间
- 商品页

此外，所有未命中固定 pipeline 的平台/对象组合都归入本指引，例如：

- X/Twitter 单条帖子
- X/Twitter 线程
- X/Twitter 长文
- X/Twitter 作者主页
- 评论区前 N 条

## Rules

- 这些对象统一走本 skill 内的 MCP 通用工作流。
- 平台不限于固定 pipeline 所覆盖的抖音和小红书；凡是 MCP catalog 可检索到的社交媒体平台，都应先尝试该工作流。
- agent 先做对象识别，再用 `catalog.search` 和 `endpoint.describe` 选最小工具链。
- 不允许因为平台不是抖音或小红书，就直接绕到 browser/CDP。
- 仅当 MCP 通用链路不可用，或任务明确需要页面级交互且 API 无法满足时，才允许使用 browser/CDP 兜底，并在输出中说明理由。
- 输出必须满足统一 envelope。
- 不要求首期落卡。
- 不允许为了 schema 完整性去编造字段。

## Minimum Deliverable

- `object_type`
- `platform`
- `input`
- `normalized`
- `request_id`
- `completeness`
- `missing_fields`
- `error_reason`
- `extract_trace`
