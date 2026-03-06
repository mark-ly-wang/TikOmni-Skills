# Douyin Platform Reference

Use this file only when the task specifically needs Douyin route or field guidance.

## Route selection rules
1. Prefer app routes over web routes.
2. Prefer higher-version routes over lower-version routes within the same family.
3. Reject routes that do not return core fields needed for the user task.

## Current preferred route families
### Single video
- Prefer app one-video/detail routes first.
- Fall back to web routes when app routes are unavailable or insufficient.

### Author homepage
- Prefer stable profile + posted-video route pairs.
- Use latest-first pagination with cursor-based continuation where supported.

## Core fields to watch
### Single video
- work identity
- title or caption text
- media URL availability
- author identity
- engagement metrics

### Homepage
- author identity
- nickname
- pagination stability
- work list availability
- request trace fields

## Agent behavior
- Record route choice and fallback reason in trace.
- Prefer routes that preserve stable pagination and resumability.
- Do not assume this file is exhaustive; consult the API catalog when fixed routes do not fit.
