# Generic MCP Objects Guide

以下对象在首期不冻结细粒度 schema：

- 评论线程
- 搜索结果
- 榜单
- 直播间
- 商品页

## Rules

- 这些对象统一走 MCP 通用工作流。
- agent 先做对象识别，再用 `catalog.search` 和 `endpoint.describe` 选最小工具链。
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

