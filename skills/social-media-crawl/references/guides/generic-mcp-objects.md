# Generic MCP Objects Guide

The following objects do not freeze a fine-grained schema in the first release:

- Comment threads
- Search results
- Ranking pages
- Livestream rooms
- Product pages

In addition, every platform and object combination that does not match a fixed pipeline falls under this guide, for example:

- A single X/Twitter post
- An X/Twitter thread
- An X/Twitter long-form post
- An X/Twitter creator homepage
- The top N comments from a comment section

## Rules

- Route these objects through the generic MCP workflow inside this skill.
- The platform is not limited to the Douyin and Xiaohongshu cases covered by fixed pipelines. If the platform is discoverable in the MCP catalog, try this workflow first.
- Detect the object first, then use `catalog.search` and `endpoint.describe` to choose the smallest toolchain.
- Do not jump to browser/CDP only because the platform is not Douyin or Xiaohongshu.
- Use browser/CDP only when the generic MCP path is unavailable, or when the task explicitly requires page-level interaction that the API cannot satisfy. Explain the reason in the output.
- The output must satisfy the unified envelope.
- No card write is required in the first release.
- Do not fabricate fields only to satisfy schema completeness.

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
