# Creator ASR Orchestration

## Primary Path

- Read `references/service-guides/asr-u2-u3-fallback.md` first and follow the shared flow: U2 primary path -> 90-second soft observation -> 120-second hard fallback -> U3 -> back to U2.
- Video items in creator or profile tasks must prefer batch ASR.
- The per-batch request limit is 100 `video_download_url` values.
- Do not treat one-by-one serial or one-by-one parallel ASR calls as the primary path for creator tasks.

## Two-Level Source Order

1. If the route directly returns `subtitle_raw`:
   - map it to `asr_raw` first
2. If `subtitle_raw` is unavailable:
   - call ASR with `video_download_url`

## Timeout and Fallback

- 90 seconds: soft observation threshold.
- 120 seconds: hard fallback threshold.
- If the batch is still incomplete after 120 seconds, run upload-media fallback only for the unsuccessful subset.

## Upload-Media Fallback

1. Call the upstream request route and obtain a temporary upload URL.
2. Download or stream-relay the no-watermark video resource.
3. Call the completion route and obtain a publicly readable URL.
4. Call ASR again with the public URL.

## Failure End State

- If the upstream media-upload route is unavailable, mark the unsuccessful subset as `analysis_eligibility=incomplete`.
- Keep fact cards for items with `analysis_eligibility=incomplete`, but exclude them from sampling, sampled explanations, and `author_analysis_v2`.
