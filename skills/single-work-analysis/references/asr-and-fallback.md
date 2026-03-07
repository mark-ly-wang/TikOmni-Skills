# 单作品 ASR 与失败路径

## 视频作品 ASR

1. 如果接口直接返回 `subtitle_raw`，优先映射到 `asr_raw`。
2. 如果没有 `subtitle_raw`，使用 `video_download_url` 调用 ASR。
3. `asr_clean` 只能由 `asr_raw` 规则清洗得到。

## 超时与 fallback

- 90 秒：软观察阈值。
- 120 秒：硬 fallback 阈值。
- 120 秒时若仍无完整 `asr_raw`，走“上传媒体 -> 公网 URL -> 再调 ASR”fallback。

## 失败终态

- 如果上游上传媒体接口未就绪，或 fallback 后仍拿不到 `asr_raw`，保留事实卡。
- 此时返回 `incomplete` 结果。
- 不伪造 `primary_text`，不输出依赖主文本的分析结论。
