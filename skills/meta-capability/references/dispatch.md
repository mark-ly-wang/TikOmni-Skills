# Dispatch Guidance

## Dispatch Principle

- `meta-capability` can always complete general TikOmni tasks on its own.
- If a more specialized skill exists in the current skill workspace and clearly matches the task, prefer handing off to that skill.
- If the better specialized skill is missing, not installed, not checked out, or otherwise unavailable, stay in `meta-capability` and complete the task here.

## When To Prefer `single-work-analysis`

- The target object is a single video, single post, single note, single article, or another single content item.
- The user wants a work card, single-item structured analysis, or transcription for one content item.
- `single-work-analysis` is available in the current skill workspace.

## When To Prefer `creator-analysis`

- The target object is a creator, account, profile page, or a creator-level content collection.
- The user wants an author card, a full content set, bucketed sampling, sampled explanations, or creator-level conclusions.
- `creator-analysis` is available in the current skill workspace.

## When To Stay In `meta-capability`

- The object boundary is still unclear.
- The platform is unfamiliar and the task first needs route confirmation, parameter confirmation, or media-entry discovery.
- The task first needs capability checking before a stricter work-card or author-card contract can be satisfied.
- The user is asking what is available, what route to use, or what fields are required.
- A better specialized skill is not currently available.
