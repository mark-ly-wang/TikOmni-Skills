# Releasing `@tikomni/skills`

## Prerequisites

- You have an npm publisher account for the `@tikomni` scope.
- The repository has a GitHub Actions secret named `NPM_TOKEN`.
- Your working tree is clean for the files you intend to publish.

## What gets published

The npm package ships the installer CLI and the packaged `skills/` content declared in `package.json`.

It does not fetch skills from GitHub during user installation. End users download the npm package from the npm registry, then the CLI copies the packaged skill folders into the target runtime directory.

## Release flow

1. Update `package.json` version.
2. Run local verification:
   - `npm test`
   - `npm run pack:dry-run`
   - `python3 scripts/ci_skill_validate.py`
   - `python3 scripts/ci_secret_scan.py`
   - `python3 scripts/ci_package_manifest.py`
   - `python3 scripts/ci_build_skill_zip.py`
3. Commit the release changes.
4. Create and push a tag in the form `v<package-version>`.
   - Example: `v0.1.0`
5. GitHub Actions workflow `npm-publish` will:
   - verify the tag matches `package.json`
   - rerun tests and repository validation
   - run `npm pack --dry-run`
   - publish the package to npm

## Manual dry run

You can also trigger `npm-publish` via `workflow_dispatch` and set:

- `npm_dist_tag`: for example `latest`, `next`, or `beta`
- `dry_run`: `true`

This is useful before the first real publish.

## Rollback

- If the published package is bad but should remain installable, publish a fixed version immediately.
- If the version must be deprecated, use `npm deprecate`.
- Avoid relying on `npm unpublish` for normal rollback.
