# P3 Analysis Standardization Notes

Phase 3 introduces a shared analysis pipeline to reduce hardcoded segment assembly in card generation while keeping existing output behavior stable.

## What changed

- Added `scripts/analysis_pipeline.py`.
- Centralized prompt-contract mapping (`PROMPT_CONTRACT_FILES`) and default analysis sections.
- Moved prompt-contract loading + OpenClaw LLM invocation into shared helpers:
  - `load_contract_prompt(...)`
  - `call_prompt_llm(...)`
  - `build_module_lines(...)`
  - `build_single_section_lines(...)`
  - `build_analysis_sections(...)`
- Refactored `scripts/write_benchmark_card.py` to consume `build_analysis_sections(...)` instead of in-file section assembly.

## Compatibility intent

- Keep CLI args and return schema unchanged.
- Keep markdown section order/labels unchanged:
  - `选题`
  - `文风`
  - `Hook`
  - `结构`
  - `洞察分析`
- Keep fallback semantics unchanged (`"数据不足"` when prompt/LLM output is unavailable).

## Future extension point

If new analysis sections are added (e.g. CTA/总结), update only `analysis_pipeline.PROMPT_CONTRACT_FILES` and section selection at callsite, instead of duplicating per-script assembly logic.
