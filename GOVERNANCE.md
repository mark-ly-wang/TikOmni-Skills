# TikOmni-Skills Governance

## Hard Rules
1. Never push directly to `main`.
2. Every change must go through PR.
3. Merge requires explicit owner approval: `批准合并`.
4. Release/tag requires explicit owner approval: `批准发布`.
5. Secret-scan must pass before merge/release.

## Required Checks
- `validate`
- `secret-scan`
- `package-manifest`

Configured in `.github/workflows/skill-guard.yml`.

## Packaging Policy
Distributable `.skill` package is built from allowlist only:
- `.skill-package-allowlist.txt`

This prevents accidental inclusion of:
- `.env*` (except `env.example`)
- `.source-meta.json`
- local/private metadata

## Local operator workflow
1. Create branch: `feat/*` `fix/*` `chore/*`
2. Run local checks:
   - `python3 scripts/ci_skill_validate.py`
   - `python3 scripts/ci_secret_scan.py`
   - `python3 scripts/ci_package_manifest.py`
   - `python3 scripts/ci_build_skill_zip.py`
3. Open PR with template filled.
4. Wait for owner approval.
5. Merge only after checks + approval.

## Emergency policy
In an emergency hotfix, branch + PR is still required. No direct push to `main`.
