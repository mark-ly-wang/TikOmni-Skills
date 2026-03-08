# Creator Workflow

## Main Flow

1. Collect creator fact fields.
2. Collect the content set and write a fact card for each work.
3. Run batch ASR for video items.
4. Exclude works with `analysis_eligibility=incomplete` from downstream analysis.
5. Run full aggregation, bucketing, and sampling.
6. Run one batch explanation step for sampled works.
7. Generate `author_analysis_v2`.
8. Return the creator card, work cards, and aggregated conclusions.

## Required Rules

- Do not run per-work LLM deep analysis.
- `sampled_work_explanations` must come from one batch stage only.
- `author_analysis_v2` is the formal creator-level primary output.
