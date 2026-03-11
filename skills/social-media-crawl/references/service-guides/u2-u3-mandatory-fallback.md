# U2 U3 Mandatory Fallback

## Hard Rule

- 视频文本优先尝试平台原生字幕。
- 无原生字幕时先走 U2。
- `u2.submit` 成功后，最多轮询 60 秒。
- 如果 60 秒后仍是 `pending`，必须进入 U3 fallback。
- U3 成功后继续完成 ASR 链路。
- 若最终失败，保留事实卡并标记 `completeness=incomplete`。

## Trace Requirement

至少记录：

- U2 submit
- U2 poll
- 触发 U3 的原因
- U3 调用步骤
- 最终文本来源

