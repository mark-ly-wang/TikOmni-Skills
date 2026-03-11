# Output Envelope

## Required Fields

- `object_type`
- `platform`
- `input`
- `normalized`
- `completeness`
- `missing_fields`
- `error_reason`
- `extract_trace`
- `request_id`

## Semantics

- `normalized` 只存结构化事实，不存分析推断。
- `completeness` 允许值：`complete`、`partial`、`incomplete`。
- `missing_fields` 是缺失字段列表。
- `error_reason` 成功时可为空字符串或 `null`。
- `extract_trace` 记录固定 pipeline 或 MCP 调度步骤。

