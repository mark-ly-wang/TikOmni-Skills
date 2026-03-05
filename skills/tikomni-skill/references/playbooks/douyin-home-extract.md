# Douyin Home Extract Playbook (Decommissioned)

> Status: **OFFLINE / NO EXECUTION ENTRY**
>
> Effective date: 2026-03-05
>
> Replacement: componentized author-home pipeline
> `scripts/cli/run_tikomni_extract.py --platform douyin --content-kind author_home`

## Migration Notes

Legacy fixed playbook routing has been removed. Use the new componentized chain:

1. `collectors`: profile + paginated posts (`handler_user_profile`, `fetch_user_post_videos`)
2. `adapters`: normalize author/work schema
3. `orchestrator`: cursor loop + dedupe + hard cap 200 + checkpoint
4. `builders`: reuse existing single-work card writer (`write_benchmark_card`), plus author card
5. `analyzers`: prompt-first structured output + minimal schema validation

## Change Record

- 2026-03-05: decommissioned old homepage playbook execution path.
- 2026-03-05: switched capability entry to registry-backed `author_home` workflow.
