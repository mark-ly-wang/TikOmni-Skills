# TikOmni API 能力索引

## 用途

- 本文档是自动生成的轻量入口，用来先锁定 tag、能力和认证方式。
- 当前数据源：`remote`
- 来源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T04:31:58+00:00`
- route 选择先读这里；当需要字段说明、默认值、示例或完整响应结构时，再进入 `api-tags/` 与 `api-contracts/`。
- 涉及 ASR 超时、公网 URL 不可读、U3 媒体中转时，再读 `service-guides/asr-u2-u3-fallback.md`。

## 全局认证

- 默认认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- 如果个别 route 覆盖或关闭了默认认证，以对应 `api-tags/` 与 `api-contracts/` 条目为准。

## 读取顺序

1. 先按平台和对象类型选 tag。
2. 再打开对应 `api-tags/<tag>.md` 看路由摘要、认证方式和关键字段。
3. 如果需要精确字段说明、默认值、示例或成功响应结构，再打开 `api-contracts/<tag>.md`。
4. 如果任务涉及音频转写、90 秒软观察或 120 秒（2 分钟）硬 fallback，再读 U2/U3 组合 guide。

## 统计

- 标签组数量：`53`
- 路由数量：`991`
- 生成目标：`3` 个 skill reference

## 特殊链路

- ASR 与 U3 fallback：[`service-guides/asr-u2-u3-fallback.md`](./service-guides/asr-u2-u3-fallback.md)
- ASR tag：[`api-tags/asr-api.md`](./api-tags/asr-api.md)
- U3 媒体中转 tag：[`api-tags/media-ingest-api.md`](./api-tags/media-ingest-api.md)

## 标签概览

| Tag | 文件 | 契约 | Ops | 认证 | 常见能力 | 常见入参 |
| --- | --- | --- | ---: | --- | --- | --- |
| `ASR-API` | [`api-tags/asr-api.md`](./api-tags/asr-api.md) | [`api-contracts/asr-api.md`](./api-contracts/asr-api.md) | 2 | 请求头 `Authorization` Bearer | ASR/字幕转写 / 音频/媒体 / 通用能力 | `input`, `task_id` |
| `Bilibili-App-API` | [`api-tags/bilibili-app-api.md`](./api-tags/bilibili-app-api.md) | [`api-contracts/bilibili-app-api.md`](./api-contracts/bilibili-app-api.md) | 11 | 请求头 `Authorization` Bearer | 通用能力 / 主页/账号 / 作品详情 / 搜索 | `av_id`, `bv_id`, `page`, `idx`, `next_offset`, `ps`, `keyword`, `page_size`, `order`, `user_id` |
| `Bilibili-Web-API` | [`api-tags/bilibili-web-api.md`](./api-tags/bilibili-web-api.md) | [`api-contracts/bilibili-web-api.md`](./api-contracts/bilibili-web-api.md) | 30 | 请求头 `Authorization` Bearer | 作品详情 / 主页/账号 / 直播 / 详情 | `bv_id`, `uid`, `pn`, `cid`, `dynamic_id`, `order`, `room_id`, `a_id`, `c_id`, `url` |
| `Demo-API` | [`api-tags/demo-api.md`](./api-tags/demo-api.md) | [`api-contracts/demo-api.md`](./api-contracts/demo-api.md) | 9 | 请求头 `Authorization` Bearer | 作品详情 / 主页/账号 / 通用能力 / 搜索 | 无 |
| `Douyin-App-V3-API` | [`api-tags/douyin-app-v3-api.md`](./api-tags/douyin-app-v3-api.md) | [`api-contracts/douyin-app-v3-api.md`](./api-contracts/douyin-app-v3-api.md) | 47 | 请求头 `Authorization` Bearer | 作品详情 / 搜索 / 主页/账号 / 详情 | `count`, `cursor`, `keyword`, `aweme_id`, `sec_user_id`, `offset`, `sort_type`, `publish_time`, `filter_duration`, `aweme_ids` |
| `Douyin-Billboard-API` | [`api-tags/douyin-billboard-api.md`](./api-tags/douyin-billboard-api.md) | [`api-contracts/douyin-billboard-api.md`](./api-contracts/douyin-billboard-api.md) | 31 | 请求头 `Authorization` Bearer | 热点/榜单 / 搜索 / 话题 / 详情 | `page_size`, `date_window`, `page`, `keyword`, `tags`, `sec_uid`, `option`, `page_num`, `end_date`, `start_date` |
| `Douyin-Creator-API` | [`api-tags/douyin-creator-api.md`](./api-tags/douyin-creator-api.md) | [`api-contracts/douyin-creator-api.md`](./api-contracts/douyin-creator-api.md) | 16 | 请求头 `Authorization` Bearer | 创作者 / 热点/榜单 / 话题 / 详情 | `billboard_tag`, `order_key`, `time_filter`, `limit`, `offset`, `category_id`, `order`, `activity_id`, `start_time`, `end_time` |
| `Douyin-Creator-V2-API` | [`api-tags/douyin-creator-v2-api.md`](./api-tags/douyin-creator-v2-api.md) | [`api-contracts/douyin-creator-v2-api.md`](./api-contracts/douyin-creator-v2-api.md) | 14 | 请求头 `Authorization` Bearer | 创作者 / 下载/媒体 / 搜索 / 热点/榜单 | `cookie`, `item_id`, `start_date`, `end_date`, `genres`, `primary_verticals`, `fields`, `need_long_article`, `metric_type`, `count` |
| `Douyin-Search-API` | [`api-tags/douyin-search-api.md`](./api-tags/douyin-search-api.md) | [`api-contracts/douyin-search-api.md`](./api-contracts/douyin-search-api.md) | 20 | 请求头 `Authorization` Bearer | 搜索 / 话题 / 主页/账号 / 作品详情 | `keyword`, `cursor`, `search_id`, `sort_type`, `publish_time`, `filter_duration`, `content_type`, `backtrace`, `douyin_user_fans`, `douyin_user_type` |
| `Douyin-Web-API` | [`api-tags/douyin-web-api.md`](./api-tags/douyin-web-api.md) | [`api-contracts/douyin-web-api.md`](./api-contracts/douyin-web-api.md) | 76 | 请求头 `Authorization` Bearer | 主页/账号 / 作品详情 / 通用能力 / 直播 | `count`, `cookie`, `refresh_index`, `keyword`, `sec_user_id`, `cursor`, `room_id`, `offset`, `aweme_id`, `max_cursor` |
| `Douyin-Xingtu-API` | [`api-tags/douyin-xingtu-api.md`](./api-tags/douyin-xingtu-api.md) | [`api-contracts/douyin-xingtu-api.md`](./api-contracts/douyin-xingtu-api.md) | 22 | 请求头 `Authorization` Bearer | 通用能力 / 作品详情 / 评论 / 热点/榜单 | `kolId`, `platformChannel`, `_range`, `page`, `onlyAssign`, `keyword`, `uri`, `durationTS`, `format`, `sec_user_id` |
| `Douyin-Xingtu-V2-API` | [`api-tags/douyin-xingtu-v2-api.md`](./api-tags/douyin-xingtu-v2-api.md) | [`api-contracts/douyin-xingtu-v2-api.md`](./api-contracts/douyin-xingtu-v2-api.md) | 21 | 请求头 `Authorization` Bearer | 创作者 / 通用能力 / 热点/榜单 / 评论 | `o_author_id`, `platform_source`, `limit`, `platform_channel`, `author_id`, `only_assign`, `flow_type`, `page`, `qualifier`, `period` |
| `Health-Check` | [`api-tags/health-check.md`](./api-tags/health-check.md) | [`api-contracts/health-check.md`](./api-contracts/health-check.md) | 1 | 请求头 `Authorization` Bearer | 通用能力 | 无 |
| `Hybrid-Parsing` | [`api-tags/hybrid-parsing.md`](./api-tags/hybrid-parsing.md) | [`api-contracts/hybrid-parsing.md`](./api-contracts/hybrid-parsing.md) | 1 | 请求头 `Authorization` Bearer | 作品详情 | `url`, `minimal`, `base64_url` |
| `Instagram-V1-API` | [`api-tags/instagram-v1-api.md`](./api-tags/instagram-v1-api.md) | [`api-contracts/instagram-v1-api.md`](./api-contracts/instagram-v1-api.md) | 29 | 请求头 `Authorization` Bearer | 主页/账号 / 作品详情 / 通用能力 / 评论 | `user_id`, `max_id`, `count`, `end_cursor`, `media_id`, `username`, `page`, `min_id`, `location_id`, `post_url` |
| `Instagram-V2-API` | [`api-tags/instagram-v2-api.md`](./api-tags/instagram-v2-api.md) | [`api-contracts/instagram-v2-api.md`](./api-contracts/instagram-v2-api.md) | 27 | 请求头 `Authorization` Bearer | 主页/账号 / 作品详情 / 搜索 / 评论 | `pagination_token`, `user_id`, `username`, `keyword`, `code_or_url`, `comment_id`, `feed_type`, `highlight_id`, `location_id`, `audio_canonical_id` |
| `Instagram-V3-API` | [`api-tags/instagram-v3-api.md`](./api-tags/instagram-v3-api.md) | [`api-contracts/instagram-v3-api.md`](./api-contracts/instagram-v3-api.md) | 26 | 请求头 `Authorization` Bearer | 主页/账号 / 作品详情 / 评论 / 搜索 | `user_id`, `username`, `url`, `first`, `after`, `query`, `media_id`, `code`, `max_id`, `comment_id` |
| `Kuaishou-App-API` | [`api-tags/kuaishou-app-api.md`](./api-tags/kuaishou-app-api.md) | [`api-contracts/kuaishou-app-api.md`](./api-contracts/kuaishou-app-api.md) | 20 | 请求头 `Authorization` Bearer | 作品详情 / 热点/榜单 / 主页/账号 / 搜索 | `pcursor`, `user_id`, `subTabId`, `subTabName`, `keyword`, `magic_face_id`, `photo_id`, `page`, `boardType`, `boardId` |
| `Kuaishou-Web-API` | [`api-tags/kuaishou-web-api.md`](./api-tags/kuaishou-web-api.md) | [`api-contracts/kuaishou-web-api.md`](./api-contracts/kuaishou-web-api.md) | 13 | 请求头 `Authorization` Bearer | 作品详情 / 主页/账号 / 热点/榜单 / 评论 | `pcursor`, `photo_id`, `user_id`, `share_link`, `board_type`, `share_text`, `url`, `root_comment_id` |
| `Lemon8-App-API` | [`api-tags/lemon8-app-api.md`](./api-tags/lemon8-app-api.md) | [`api-contracts/lemon8-app-api.md`](./api-contracts/lemon8-app-api.md) | 16 | 请求头 `Authorization` Bearer | 通用能力 / 主页/账号 / 作品详情 / 搜索 | `user_id`, `item_id`, `cursor`, `share_text`, `group_id`, `media_id`, `offset`, `query`, `max_cursor`, `filter_type` |
| `LinkedIn-Web-API` | [`api-tags/linkedin-web-api.md`](./api-tags/linkedin-web-api.md) | [`api-contracts/linkedin-web-api.md`](./api-contracts/linkedin-web-api.md) | 25 | 请求头 `Authorization` Bearer | 主页/账号 / 通用能力 / 作品详情 / 搜索 | `page`, `urn`, `company_id`, `pagination_token`, `sort_by`, `company`, `username`, `date_posted`, `experience_level`, `remote` |
| `Media-Ingest-API` | [`api-tags/media-ingest-api.md`](./api-tags/media-ingest-api.md) | [`api-contracts/media-ingest-api.md`](./api-contracts/media-ingest-api.md) | 2 | 请求头 `Authorization` Bearer | 媒体上传/公网URL | `provider`, `file_name`, `content_type`, `size_bytes`, `upload_id` |
| `PiPiXia-App-API` | [`api-tags/pipixia-app-api.md`](./api-tags/pipixia-app-api.md) | [`api-contracts/pipixia-app-api.md`](./api-contracts/pipixia-app-api.md) | 17 | 请求头 `Authorization` Bearer | 作品详情 / 主页/账号 / 搜索 / 详情 | `cursor`, `cell_id`, `user_id`, `cell_type`, `hashtag_id`, `feed_count`, `offset`, `hashtag_request_type`, `hashtag_sort_type`, `page` |
| `Reddit-APP-API` | [`api-tags/reddit-app-api.md`](./api-tags/reddit-app-api.md) | [`api-contracts/reddit-app-api.md`](./api-contracts/reddit-app-api.md) | 24 | 请求头 `Authorization` Bearer | 通用能力 / 主页/账号 / 作品详情 / 评论 | `need_format`, `after`, `sort`, `username`, `subreddit_name`, `subreddit_id`, `post_id`, `filter_posts`, `include_comment_id`, `comment_id` |
| `Sora2-API` | [`api-tags/sora2-api.md`](./api-tags/sora2-api.md) | [`api-contracts/sora2-api.md`](./api-contracts/sora2-api.md) | 17 | 请求头 `Authorization` Bearer | 作品详情 / 主页/账号 / 通用能力 / 评论 | `cursor`, `user_id`, `post_id`, `post_url`, `task_id`, `prompt`, `orientation`, `media_id`, `comment_id`, `eager_views` |
| `Temp-Mail-API` | [`api-tags/temp-mail-api.md`](./api-tags/temp-mail-api.md) | [`api-contracts/temp-mail-api.md`](./api-contracts/temp-mail-api.md) | 3 | 请求头 `Authorization` Bearer | 通用能力 | `token`, `message_id` |
| `Threads-Web-API` | [`api-tags/threads-web-api.md`](./api-tags/threads-web-api.md) | [`api-contracts/threads-web-api.md`](./api-contracts/threads-web-api.md) | 11 | 请求头 `Authorization` Bearer | 主页/账号 / 作品详情 / 搜索 / 详情 | `end_cursor`, `user_id`, `post_id`, `query`, `url`, `username` |
| `TikHub-Downloader-API` | [`api-tags/tikhub-downloader-api.md`](./api-tags/tikhub-downloader-api.md) | [`api-contracts/tikhub-downloader-api.md`](./api-contracts/tikhub-downloader-api.md) | 2 | 请求头 `Authorization` Bearer | 下载/媒体 | 无 |
| `TikHub-User-API` | [`api-tags/tikhub-user-api.md`](./api-tags/tikhub-user-api.md) | [`api-contracts/tikhub-user-api.md`](./api-contracts/tikhub-user-api.md) | 6 | 请求头 `Authorization` Bearer | 主页/账号 | `endpoint`, `request_per_day` |
| `TikTok-Ads-API` | [`api-tags/tiktok-ads-api.md`](./api-tags/tiktok-ads-api.md) | [`api-contracts/tiktok-ads-api.md`](./api-contracts/tiktok-ads-api.md) | 31 | 请求头 `Authorization` Bearer | 广告 / 搜索 / 详情 / 创作者 | `limit`, `page`, `country_code`, `period`, `keyword`, `period_type`, `industry`, `order_by`, `rank_type`, `material_id` |
| `TikTok-Analytics-API` | [`api-tags/tiktok-analytics-api.md`](./api-tags/tiktok-analytics-api.md) | [`api-contracts/tiktok-analytics-api.md`](./api-contracts/tiktok-analytics-api.md) | 4 | 请求头 `Authorization` Bearer | 数据分析 / 评论 / 创作者 / 作品详情 | `item_id`, `content_category`, `user_id` |
| `TikTok-App-V3-API` | [`api-tags/tiktok-app-v3-api.md`](./api-tags/tiktok-app-v3-api.md) | [`api-contracts/tiktok-app-v3-api.md`](./api-contracts/tiktok-app-v3-api.md) | 75 | 请求头 `Authorization` Bearer | 作品详情 / 电商 / 主页/账号 / 搜索 | `count`, `offset`, `keyword`, `sort_type`, `cursor`, `region`, `sec_user_id`, `user_id`, `room_id`, `seller_id` |
| `TikTok-Creator-API` | [`api-tags/tiktok-creator-api.md`](./api-tags/tiktok-creator-api.md) | [`api-contracts/tiktok-creator-api.md`](./api-contracts/tiktok-creator-api.md) | 14 | 请求头 `Authorization` Bearer | 创作者 / 作品详情 / 数据分析 / 电商 | `cookie`, `proxy`, `start_date`, `item_id`, `page`, `product_id`, `end_date`, `count`, `offset`, `item_ids` |
| `TikTok-Interaction-API` | [`api-tags/tiktok-interaction-api.md`](./api-tags/tiktok-interaction-api.md) | [`api-contracts/tiktok-interaction-api.md`](./api-contracts/tiktok-interaction-api.md) | 7 | 请求头 `Authorization` Bearer | 通用能力 / 评论 / 作品详情 / 评论回复 | `cookie`, `device_id`, `iid`, `proxy`, `aweme_id`, `text`, `api_key`, `invite_code`, `user_id`, `sec_user_id` |
| `TikTok-Shop-Web-API` | [`api-tags/tiktok-shop-web-api.md`](./api-tags/tiktok-shop-web-api.md) | [`api-contracts/tiktok-shop-web-api.md`](./api-contracts/tiktok-shop-web-api.md) | 15 | 请求头 `Authorization` Bearer | 电商 / 搜索 / 详情 / 热点/榜单 | `region`, `product_id`, `offset`, `seller_id`, `search_word`, `page_token`, `lang`, `count`, `sort_type`, `filter_id` |
| `TikTok-Web-API` | [`api-tags/tiktok-web-api.md`](./api-tags/tiktok-web-api.md) | [`api-contracts/tiktok-web-api.md`](./api-contracts/tiktok-web-api.md) | 58 | 请求头 `Authorization` Bearer | 通用能力 / 主页/账号 / 直播 / 作品详情 | `count`, `cursor`, `cookie`, `secUid`, `url`, `keyword`, `search_id`, `user_agent`, `offset`, `coverFormat` |
| `Toutiao-App-API` | [`api-tags/toutiao-app-api.md`](./api-tags/toutiao-app-api.md) | [`api-contracts/toutiao-app-api.md`](./api-contracts/toutiao-app-api.md) | 5 | 请求头 `Authorization` Bearer | 作品详情 / 主页/账号 / 评论 | `group_id`, `offset`, `user_profile_url`, `user_id` |
| `Toutiao-Web-API` | [`api-tags/toutiao-web-api.md`](./api-tags/toutiao-web-api.md) | [`api-contracts/toutiao-web-api.md`](./api-contracts/toutiao-web-api.md) | 2 | 请求头 `Authorization` Bearer | 作品详情 | `aweme_id` |
| `Twitter-Web-API` | [`api-tags/twitter-web-api.md`](./api-tags/twitter-web-api.md) | [`api-contracts/twitter-web-api.md`](./api-contracts/twitter-web-api.md) | 13 | 请求头 `Authorization` Bearer | 主页/账号 / 作品详情 / 评论 / 搜索 | `cursor`, `screen_name`, `tweet_id`, `rest_id`, `keyword`, `search_type`, `country`, `userId`, `count` |
| `WeChat-Channels-API` | [`api-tags/wechat-channels-api.md`](./api-tags/wechat-channels-api.md) | [`api-contracts/wechat-channels-api.md`](./api-contracts/wechat-channels-api.md) | 9 | 请求头 `Authorization` Bearer | 主页/账号 / 搜索 / 评论 / 热点/榜单 | `keywords`, `id`, `username`, `lastBuffer`, `comment_id`, `session_buffer`, `last_buffer`, `page`, `exportId` |
| `WeChat-Media-Platform-Web-API` | [`api-tags/wechat-media-platform-web-api.md`](./api-tags/wechat-media-platform-web-api.md) | [`api-contracts/wechat-media-platform-web-api.md`](./api-contracts/wechat-media-platform-web-api.md) | 10 | 请求头 `Authorization` Bearer | 作品详情 / 评论 / 详情 / 评论回复 | `url`, `comment_id`, `offset`, `buffer`, `content_id`, `ghid`, `sogou_url` |
| `Weibo-App-API` | [`api-tags/weibo-app-api.md`](./api-tags/weibo-app-api.md) | [`api-contracts/weibo-app-api.md`](./api-contracts/weibo-app-api.md) | 20 | 请求头 `Authorization` Bearer | 主页/账号 / 作品详情 / 搜索 / 详情 | `uid`, `page`, `since_id`, `status_id`, `query`, `count`, `max_id`, `category`, `search_type`, `sort_type` |
| `Weibo-Web-API` | [`api-tags/weibo-web-api.md`](./api-tags/weibo-web-api.md) | [`api-contracts/weibo-web-api.md`](./api-contracts/weibo-web-api.md) | 11 | 请求头 `Authorization` Bearer | 主页/账号 / 搜索 / 作品详情 / 评论 | `page`, `max_id`, `post_id`, `uid`, `channel_name`, `cid`, `mid`, `max_id_type`, `keyword`, `search_type` |
| `Weibo-Web-V2-API` | [`api-tags/weibo-web-v2-api.md`](./api-tags/weibo-web-v2-api.md) | [`api-contracts/weibo-web-v2-api.md`](./api-contracts/weibo-web-v2-api.md) | 33 | 请求头 `Authorization` Bearer | 搜索 / 主页/账号 / 作品详情 / 通用能力 | `page`, `uid`, `query`, `id`, `max_id`, `count`, `since_id`, `q`, `keyword`, `cursor` |
| `Xiaohongshu-App-API` | [`api-tags/xiaohongshu-app-api.md`](./api-tags/xiaohongshu-app-api.md) | [`api-contracts/xiaohongshu-app-api.md`](./api-contracts/xiaohongshu-app-api.md) | 12 | 请求头 `Authorization` Bearer | 作品详情 / 主页/账号 / 评论 / 电商 | `note_id`, `session_id`, `share_link`, `start`, `share_text`, `sort`, `user_id`, `keyword`, `page`, `search_id` |
| `Xiaohongshu-App-V2-API` | [`api-tags/xiaohongshu-app-v2-api.md`](./api-tags/xiaohongshu-app-v2-api.md) | [`api-contracts/xiaohongshu-app-v2-api.md`](./api-contracts/xiaohongshu-app-v2-api.md) | 21 | 请求头 `Authorization` Bearer | 作品详情 / 电商 / 搜索 / 详情 | `source`, `share_text`, `cursor`, `note_id`, `page`, `keyword`, `search_id`, `sku_id`, `user_id`, `tab` |
| `Xiaohongshu-Web-API` | [`api-tags/xiaohongshu-web-api.md`](./api-tags/xiaohongshu-web-api.md) | [`api-contracts/xiaohongshu-web-api.md`](./api-contracts/xiaohongshu-web-api.md) | 17 | 请求头 `Authorization` Bearer | 作品详情 / 主页/账号 / 搜索 / 评论 | `note_id`, `share_text`, `cookie`, `proxy`, `lastCursor`, `user_id`, `keyword`, `page`, `xsec_token`, `sort` |
| `Xiaohongshu-Web-V2-API` | [`api-tags/xiaohongshu-web-v2-api.md`](./api-tags/xiaohongshu-web-v2-api.md) | [`api-contracts/xiaohongshu-web-v2-api.md`](./api-contracts/xiaohongshu-web-v2-api.md) | 18 | 请求头 `Authorization` Bearer | 作品详情 / 主页/账号 / 通用能力 / 评论 | `note_id`, `user_id`, `cursor`, `page`, `keywords`, `short_url`, `sort_type`, `note_type`, `comment_id` |
| `Xigua-App-V2-API` | [`api-tags/xigua-app-v2-api.md`](./api-tags/xigua-app-v2-api.md) | [`api-contracts/xigua-app-v2-api.md`](./api-contracts/xigua-app-v2-api.md) | 7 | 请求头 `Authorization` Bearer | 作品详情 / 主页/账号 / 评论 / 搜索 | `item_id`, `user_id`, `offset`, `max_behot_time`, `count`, `keyword`, `order_type`, `min_duration`, `max_duration` |
| `YouTube-Web-API` | [`api-tags/youtube-web-api.md`](./api-tags/youtube-web-api.md) | [`api-contracts/youtube-web-api.md`](./api-contracts/youtube-web-api.md) | 21 | 请求头 `Authorization` Bearer | 作品详情 / 主页/账号 / 搜索 / 评论 | `continuation_token`, `language_code`, `country_code`, `channel_id`, `video_id`, `need_format`, `search_query`, `sort_by`, `lang`, `time_zone` |
| `YouTube-Web-V2-API` | [`api-tags/youtube-web-v2-api.md`](./api-tags/youtube-web-v2-api.md) | [`api-contracts/youtube-web-v2-api.md`](./api-contracts/youtube-web-v2-api.md) | 16 | 请求头 `Authorization` Bearer | 作品详情 / 主页/账号 / 搜索 / 直播 | `continuation_token`, `need_format`, `language_code`, `country_code`, `video_id`, `channel_id`, `video_url`, `sort_by`, `channel_url`, `search_query` |
| `Zhihu-Web-API` | [`api-tags/zhihu-web-api.md`](./api-tags/zhihu-web-api.md) | [`api-contracts/zhihu-web-api.md`](./api-contracts/zhihu-web-api.md) | 32 | 请求头 `Authorization` Bearer | 搜索 / 主页/账号 / 作品详情 / 通用能力 | `offset`, `limit`, `keyword`, `user_url_token`, `search_hash_id`, `article_id`, `order_by`, `message_content`, `message_id`, `show_all_topics` |
| `iOS-Shortcut` | [`api-tags/ios-shortcut.md`](./api-tags/ios-shortcut.md) | [`api-contracts/ios-shortcut.md`](./api-contracts/ios-shortcut.md) | 1 | 请求头 `Authorization` Bearer | 通用能力 | 无 |
