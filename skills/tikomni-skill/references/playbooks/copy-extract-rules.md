# Copy Extract Rules

## 1) Default ASR Policy / 默认 ASR 策略

1. Once a usable video media URL is resolved, default to U2 ASR for transcript extraction.
2. Do not treat title/desc/caption as final transcript when ASR is available.
3. `desc/title` can be used as context only.

## 2) Platform-Agnostic Route / 平台无关路由

1. These rules apply to all supported platforms, not only specific platforms.
2. If the platform route provides usable subtitle data, subtitle can be used first.
3. If subtitle is unavailable, invalid, or the route has no subtitle capability, fallback to U2.

## 3) Batch Strategy / 批量策略

1. For multi-video tasks, prefer one batch submit first, instead of many concurrent single submits.
2. Batch submit should carry multiple URLs in one request (up to 100 per request).
3. If batch result is incomplete or partially failed, fallback only for failed/unmapped items.

## 4) Query Decision Rules / Query 判定规则

1. In-progress: `pending_count > 0`.
2. Fully succeeded: `platform_task_status=SUCCEEDED` and `pending_count=0`.
3. Partial succeeded: `platform_task_status=PARTIAL_SUCCEEDED` and `pending_count=0`.
4. Failed: `platform_task_status=FAILED` and `pending_count=0`.
5. Do not stop at submit accepted (HTTP 200); final state must be judged by query.

## 5) Batch Outcome Handling / 批量结果处理

1. Fully succeeded: consume all item transcripts and mark batch completed.
2. Partial succeeded: consume succeeded items directly, keep failed items for fallback/retry.
3. Failed: record failure reasons, then fallback according to workflow policy.
