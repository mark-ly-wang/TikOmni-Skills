# Creator 场景 ASR 编排

## 主路径

- creator / 主页场景的视频作品必须优先走批量 ASR。
- 单次批量请求上限为 100 条 `video_download_url`。
- 不建议逐条串行或逐条并行调用 ASR 作为主页主路径。

## 两级来源

1. 接口直接返回 `subtitle_raw`：
   - 先映射到 `asr_raw`
2. 没有 `subtitle_raw`：
   - 使用 `video_download_url` 调用 ASR

## 超时与 fallback

- 90 秒：软观察阈值
- 120 秒：硬 fallback 阈值
- 120 秒时若仍未完全返回，只对未成功子集走上传媒体 fallback

## 上传媒体 fallback

1. 调上游申请接口，拿临时上传 URL
2. 下载或流式转发无水印视频资源
3. 调完成接口，拿公网可读 URL
4. 用公网 URL 重新调 ASR

## 失败终态

- 上游上传媒体接口未就绪时，未成功子集标记为 `analysis_eligibility=incomplete`
- `analysis_eligibility=incomplete` 的作品保留事实卡，但排除出 sampling、sampled explanations、`author_analysis_v2`
