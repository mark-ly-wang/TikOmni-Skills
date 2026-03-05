# TikOmni Douyin Author Home Fix Implementation Report

- Date: 2026-03-05
- Repo: `/mnt/openclaw/data/openclaw-workspace/data/repos/TikOmni-Skills`
- Scope: Douyin author_home A/B/C fix + regression updates

## 1) Changed Files

1. `skills/tikomni-skill/scripts/author_home/collectors/homepage_collectors.py`
2. `skills/tikomni-skill/scripts/author_home/schema.py`
3. `skills/tikomni-skill/scripts/author_home/adapters/platform_adapters.py`
4. `skills/tikomni-skill/scripts/cli/regression_author_home_componentized.py`
5. `skills/tikomni-skill/scripts/cli/smoke_structure_checks.py`

## 2) Implemented Fixes

### A) sec_user_id extraction robustness (P0)
- Supports direct string payload in `resolve_resp.data` (e.g. `MS4...`)
- Supports nested `data.data`
- Supports deep key scan for `sec_user_id/sec_uid/secUserId/secuid`
- Adds unresolved diagnostic trace when author id cannot be resolved

### B) works list extraction conflict (P0)
- Removed `data` conflict from primary list candidate keys
- `_pick_list` now continues searching until list is found instead of stopping at dict hit
- Douyin pages now prioritize `aweme_list/items/list`

### C) semantic-empty missing_fields validation (P0.5)
- `schema.py` now validates semantic empty values for key fields
- Added `validate_works_collection` for `empty_collection`
- Adapter appends collection-level validation into `missing_fields`

## 3) Verification

### 3.1 Static checks
```bash
python3 -m py_compile \
  skills/tikomni-skill/scripts/author_home/collectors/homepage_collectors.py \
  skills/tikomni-skill/scripts/author_home/schema.py \
  skills/tikomni-skill/scripts/author_home/adapters/platform_adapters.py \
  skills/tikomni-skill/scripts/cli/regression_author_home_componentized.py \
  skills/tikomni-skill/scripts/cli/smoke_structure_checks.py
```
Result: PASS

### 3.2 Regression
```bash
python3 skills/tikomni-skill/scripts/cli/regression_author_home_componentized.py
```
Result: PASS (`ok: true`)

### 3.3 Smoke
```bash
cd skills/tikomni-skill
python3 scripts/cli/smoke_structure_checks.py
```
Result: PASS (`ok: true`)

### 3.4 Real reproduction (required URL)
```bash
cd /mnt/openclaw/data/openclaw-workspace/skills/tikomni-skill
python3 scripts/cli/run_tikomni_extract.py \
  "https://v.douyin.com/A2MmA6iO6fA/" \
  --platform douyin \
  --content-kind author_home \
  --no-write-card \
  --no-persist-output
```
Observed:
- `error_reason = null`
- `request_id = 50e23e5f-7b6d-4b4d-866b-6010646b4479`
- `works_count = 14`
- `missing_fields = []`

## 4) Sync / Drift (workspace policy)
From `/mnt/openclaw/data/openclaw-workspace`:
```bash
bash scripts/tikomni-sync-dev-to-runtime.sh
bash scripts/tikomni-sync-drift-check.sh
```
Result: PASS (only expected `.env.local` drift)

## 5) Remaining Risks

1. Upstream endpoint schema may evolve; key lists in collectors should be maintained with API changes.
2. Auto routing still defaults to `single_video` for douyin; homepage intent still benefits from explicit `--content-kind author_home` unless future routing enhancement is implemented.
