# U2 U3 Mandatory Fallback

## Hard Rule

- Prefer native platform subtitles for video text.
- If native subtitles are unavailable, use U2 first.
- After `u2.submit` succeeds, poll for at most 60 seconds.
- If the task is still `pending` after 60 seconds, enter the U3 fallback path.
- If U3 succeeds, continue and complete the ASR path.
- If the flow still fails, keep the fact card and mark `completeness=incomplete`.

## Trace Requirement

Record at least:

- U2 submit
- U2 poll
- The reason that triggered U3
- The U3 invocation steps
- The final text source
