# Xiaohongshu Platform Reference

Use this file only when the task specifically needs Xiaohongshu route or field guidance.

## Route selection rules
1. Prefer app routes over web routes.
2. Prefer higher-version app routes over lower-version app routes.
3. Reject routes that return insufficient core fields even when the request itself succeeded.

## Current preferred route families
### Single note
- Prefer APP V2 note-detail routes first.
- Fall back to older APP note-detail routes.
- Fall back to WEB_V2 / WEB only when app routes are unavailable or insufficient.

### Author homepage
- Prefer APP V2 profile/posts routes first.
- Fall back to WEB_V2 profile/posts routes.
- Fall back to older APP routes only when higher-priority routes are unavailable or insufficient.

## Core fields to watch
### Note
- note identity
- title or primary text
- media availability
- author identity
- engagement metrics when available

### Homepage
- author identity
- nickname
- pagination stability
- post list availability
- request trace fields

## Agent behavior
- Record route choice and fallback reason in trace.
- Treat field completeness as part of route success judgment.
- Prefer minimal-cost routes that satisfy the user task.
- Do not assume this file is exhaustive; consult the API catalog when fixed routes do not fit.
