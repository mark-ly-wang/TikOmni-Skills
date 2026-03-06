# Routing Rules

## 1. Runtime structure
1. Unified entry: `scripts/cli/run_tikomni_extract.py`
2. Registry mapping layer: `scripts/registry/workflow_registry.py`
3. Platform handlers: `scripts/platform/*/`
4. Shared logic: `scripts/core/` and `scripts/pipeline/`

## 2. Policy priority
1. Capability priority is defined by `references/capability-routing-matrix.md`.
2. `run_tikomni_extract` parses input, resolves workflow, and executes the selected handler.
3. Registry resolves `(platform, content_kind) -> handler` only.
4. Do not move routing policy priority into registry.

## 3. Global endpoint selection policy
1. For the same platform and intent, prefer `app > web`.
2. For endpoints of the same family, prefer higher version over lower version.
3. Prefer the minimal-cost route that can satisfy the user intent and required fields.
4. If core fields are missing, treat the route as insufficient even when HTTP is 2xx.
5. Keep fallback chains as short as possible.
6. Route traces should include `chosen_route`, `fallback_trigger_reason`, `field_completeness`, and `request_id` when available.

## 4. Global rate-limit and retry policy
1. Respect the global TikOmni rate-limit policy before preferring aggressive parallelism.
2. Prefer shared/global throttling over per-handler ad hoc throttling.
3. Retry timeout-class failures with bounded backoff; do not retry indefinitely.
4. When rate limit or retry affects execution, record the effect in trace/progress metadata.
5. Platform-specific files may refine route candidates, but they must not override these global limits without explicit policy change.

## 5. Fixed-route execution rules
1. Homepage extraction should use the fixed registry-backed route when a homepage capability is matched.
2. Single-content extraction should use the fixed registry-backed route when a single-content capability is matched.
3. Legacy playbooks may remain as references, but they are not execution entry points unless explicitly promoted back into an active route.

## 5. Default extraction bounds
1. Homepage default sort is latest-first unless the active platform route defines an explicit alternative.
2. Default extraction bounds: `page_size=20`, `pages_max=50`, total `max_items=200` hard cap unless the active handler defines a stricter cap.
3. Pagination should use the platform's stable cursor strategy with dedupe and resumable state when supported.

## 6. Universal fallback rule
1. When fixed capabilities are not matched, enter universal fallback.
2. Universal fallback must emit explicit `fallback_trace` and `missing_fields`.
3. Platform-specific endpoint candidates and route preferences belong in `references/platforms/*.md`, not here.
