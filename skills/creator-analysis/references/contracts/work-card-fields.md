# Creator Analysis Work Card Fields

## Card Roles

- `author_sample_card`
  - Fact-and-structure card for every retrieved work in creator analysis.
- `sample_work_card`
  - Sampled-only enhanced card that reuses the same fact-and-structure fields and adds the explanation block.

## Fixed Display Fields

- `platform`
- `platform_work_id`
- `platform_author_id`
- `author_handle`
- `title`
- `caption_raw`
- `work_modality`
- `published_date`
- `digg_count`
- `comment_count`
- `collect_count`
- `share_count`
- `play_count`
- `cover_image`
- `source_url`
- `share_url`
- `primary_text`

## Structural Display Fields

- `performance_score`
- `performance_score_norm`
- `bucket`
- `hook_type`
- `structure_type`
- `cta_type`
- `content_form`
- `style_markers`
- `tags`

## Shared Appendix Fields

- `analysis_eligibility`
- `analysis_exclusion_reason`

## Video-Only Appendix Fields

- `asr_raw`
- `video_download_url`

## Sampled-Only Explanation Block

- `sampled_explanation.why_it_worked_or_failed`
- `sampled_explanation.copyable_elements`
- `sampled_explanation.non_copyable_elements`
- `sampled_explanation.emotional_triggers`
- `sampled_explanation.cognitive_gap`
- `sampled_explanation.commercial_signal`

## Key Rules

- Keep author sample cards for all retrieved works.
- Only sampled works receive the sampled explanation block.
- The final card should not expose `content_type`, `publish_time`, `create_time_sec`, `subtitle_raw`, `asr_source`, `asr_status`, or `asr_error_reason`.
- Use `primary_text` as the main reading body and keep `asr_raw` in appendix/details only.
- If a video item cannot obtain `asr_raw`, keep the fact card but mark `analysis_eligibility=incomplete` and exclude that item from creator analysis.
- Do not introduce per-work standalone LLM analysis in creator analysis.
