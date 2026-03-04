# 文案提取规则

## 1. 抖音

1. 涉及文案/字幕/逐字稿时，固定走 U2。
2. `desc/title` 仅作为上下文，不作为最终逐字稿。

## 2. 小红书

1. 先查字幕字段（`subtitle_url` / subtitles）。
2. 无字幕时走 U2。

## 3. 批量逐条文案

1. 主页流程默认开启。
2. 默认资格：`video_model=video` 且 `13s < duration_ms <= 15min`。
3. 时长上限支持配置：`15min`（默认）/ `30min` / `60min`。
