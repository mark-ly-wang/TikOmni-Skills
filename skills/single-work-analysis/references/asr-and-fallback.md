# Single-Item ASR and Failure Handling

## Video ASR

1. Read `references/service-guides/asr-u2-u3-fallback.md` first and follow the shared flow: U2 primary path -> 90-second soft observation -> 120-second hard fallback -> U3 -> back to U2.
2. If the route already returns `subtitle_raw`, map it to `asr_raw` first.
3. If `subtitle_raw` is unavailable, call ASR with `video_download_url`.
4. Derive `asr_clean` only from `asr_raw` through the cleaning rules.

## Timeout and Fallback

- 90 seconds: soft observation threshold.
- 120 seconds: hard fallback threshold.
- If there is still no complete `asr_raw` after 120 seconds, use the upload-media -> public URL -> ASR retry fallback path.

## Failure End State

- If the upstream media-upload route is unavailable, or if `asr_raw` is still unavailable after fallback, keep the fact card.
- Return `incomplete` in that state.
- Do not fabricate `primary_text`, and do not output analysis conclusions that depend on missing main text.
