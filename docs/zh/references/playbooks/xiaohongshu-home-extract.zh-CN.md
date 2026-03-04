# 小红书主页提取 Playbook

## 1. 输入

1. `user_id` 或主页/分享链接。
2. 可选：`limit`、`pages_max`。

## 2. 固定步骤

1. 若输入不是 `user_id`，先解析：
   - `GET /api/u1/v1/xiaohongshu/app/get_user_id_and_xsec_token`
2. 拉取作者信息：
   - 主：`GET /api/u1/v1/xiaohongshu/web_v2/fetch_user_info_app`
   - 备：`GET /api/u1/v1/xiaohongshu/app/get_user_info`
3. 拉取主页作品：
   - 主：`GET /api/u1/v1/xiaohongshu/web_v2/fetch_home_notes_app`
   - 备：`GET /api/u1/v1/xiaohongshu/app/get_user_notes`
4. 分页优先使用 `has_more + cursor`；若不稳定，可用最后一条 `note_id` 作为游标候选。
5. 默认参数：`limit=20`、`pages_max=50`。

## 3. 文案提取子规则

1. 主页流程默认开启批量逐条文案提取。
2. 小红书文案固定“字幕优先”：
   - 先查 `subtitle_url` 或 `video_info_v2.media.video.subtitles`
   - 无字幕再走 U2 submit/query

## 4. 输出

1. 必含“字幕是否命中”“是否走 U2 fallback”“最终文本来源”。
2. 最终结果必须落地为 markdown 产物。
