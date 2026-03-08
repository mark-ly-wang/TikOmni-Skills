# Execution Guidelines

## Goal

Within a shared cross-platform execution flow, finish capability discovery, route selection, input confirmation, and field-availability checks before moving into extraction or analysis.

## Minimum Checklist

- Confirm the platform and object type: single content item, comments, profile, or content collection.
- Read `api-capability-index.md` and lock onto the relevant platform tag.
- Read the relevant routes in `api-tags/*.md` for auth requirements, key inputs, and key success responses.
- If exact field definitions, defaults, examples, or full success-response structures are needed, continue into the relevant `api-contracts/*.md`.
- Decide whether the task can use a validated route chain from this repository or needs an ad hoc route choice from the broader catalog.
- For video ASR, decide whether `service-guides/asr-u2-u3-fallback.md` is needed for the 90-second soft observation window and the 120-second hard fallback.
- Identify the usable entry points: share URL, landing-page URL, platform ID, profile URL, download URL, or raw text.
- Identify the retrievable resources: title, caption, subtitles, comments, media download URLs, author metadata, and engagement metrics.
- Confirm the output expectation: raw facts, structured fields, analysis conclusions, or a combination.
- Confirm missing-field and degradation behavior: which fields are stable, which need fallback, and which are currently unavailable.

## Output Requirements

- Return concrete routes, inputs, and results rather than generic advice.
- Make field origin, stability, and missing reasons explicit.
- Ground every analysis conclusion in retrieved facts only.
- Prefer platform-neutral output structures when possible so the results remain reusable.
