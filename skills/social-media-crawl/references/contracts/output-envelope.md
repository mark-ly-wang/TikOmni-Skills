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

- `normalized` stores structured facts only, not analytical inference.
- `completeness` allows `complete`, `partial`, and `incomplete`.
- `missing_fields` is the list of missing fields.
- `error_reason` may be an empty string or `null` on success.
- `extract_trace` records the fixed-pipeline or MCP dispatch steps. If the flow ends in browser/CDP fallback, it must also record the earlier MCP attempts and the fallback reason.
