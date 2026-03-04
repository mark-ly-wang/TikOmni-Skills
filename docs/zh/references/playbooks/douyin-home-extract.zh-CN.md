# 抖音主页提取 Playbook

## 1. 输入

1. `sec_user_id` 或主页/分享链接。
2. 可选：`limit`、`pages_max`、`sort_type`。

## 2. 固定步骤

1. 若输入不是 `sec_user_id`，先解析：
   - `GET /api/u1/v1/douyin/web/get_sec_user_id`
2. 拉取作者信息：
   - `GET /api/u1/v1/douyin/app/v3/handler_user_profile`
3. 拉取主页作品：
   - `GET /api/u1/v1/douyin/app/v3/fetch_user_post_videos`
4. 仅在 `has_more == 1` 且 `max_cursor` 有效时继续翻页。
5. 默认参数：`sort_type=0`、`count<=20`、`limit=20`、`pages_max=50`。

## 3. 文案提取子规则

1. 主页流程默认开启批量逐条文案提取。
2. 仅当 `video_model=video` 且 `13s < duration_ms <= 15min` 时执行转写。
3. 抖音文案固定走 U2：
   - `POST /api/u2/v1/services/audio/asr/transcription`
   - `GET /api/u2/v1/tasks/{task_id}`

## 4. 输出

1. 必含作者摘要、作品列表、分页轨迹、接口链路、`request_id`。
2. 最终结果必须落地为 markdown 产物。
