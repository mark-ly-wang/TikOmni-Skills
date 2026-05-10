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
- `extract_trace` records fixed-pipeline steps or API-only resolver/caller steps, including `endpoint_id`, selected variant, alternatives, and request status when available.
