# Creator Workflow

## Main Flow

1. Collect creator fact fields.
2. Collect the content set.
3. Run batch ASR for video items.
4. Exclude works with `analysis_eligibility=incomplete` from downstream analysis.
5. Run normalization, aggregation, bucketing, and sampling.
6. Run one batch explanation step for sampled works.
7. Generate `author_analysis_v2`.
8. Write author sample cards for all retrieved works.
9. Write sampled enhanced cards for sampled works only.
10. Write the creator card.
11. Return the creator card, author sample cards, sampled enhanced cards, and aggregated conclusions.

## Required Rules

- Do not run per-work LLM deep analysis.
- `sampled_work_explanations` must come from one batch stage only.
- `author_analysis_v2` is the formal creator-level primary output.
- Author sample cards are the fact-and-structure cards for all retrieved works.
- Sampled enhanced cards reuse the sampled works only and add the explanation block from `sampled_work_explanations`.
