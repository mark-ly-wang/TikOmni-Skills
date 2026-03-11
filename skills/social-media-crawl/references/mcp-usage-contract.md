# MCP Usage Contract

## Fixed Inputs

- MCP URL: `https://mcp.tikomni.com/mcp`
- Auth: `Authorization: Bearer <TIKOMNI_API_KEY>`
- 不在工具参数中重复传 API key

## Required Tool Order

1. `tools/list`
2. 识别是否命中固定 pipeline
3. 若不命中固定 pipeline：
   - `catalog.search`
   - `endpoint.describe`
   - `api.call`
4. 若需要视频文本：
   - `u2.submit`
   - `u2.query`
   - 超过 60 秒仍 `pending` 时进入 U3 fallback

## Output Rules

- 事实字段与派生元数据分离
- 结果必须包含 `request_id`
- 结果必须包含 `completeness`
- 结果必须包含 `missing_fields`
- 结果必须包含 `error_reason`
- 结果必须包含 `extract_trace`

