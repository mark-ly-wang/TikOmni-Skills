# TikOmni API 能力目录

## 目录

- [用途](#用途)
- [统计](#统计)
- [标签概览](#标签概览)
- [完整路由目录](#完整路由目录)

## 用途

- 本文档由 TikOmni 在线 OpenAPI 自动生成，是当前 skill 的权威接口目录。
- 当前数据源：`remote`
- 来源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-07T20:28:45+00:00`
- 当技能需要判断“有哪些接口、该调哪个路由、要传哪些字段”时，先读本文档，再读各 skill 自己的平台 guide。
- `*` 表示必填字段；`query/path/header/cookie` 表示参数位置；`application/json:` 后面是请求体顶层字段摘要。
- 完整返回结构以 OpenAPI 原始 JSON 为准；各 skill 只需要把平台原始返回映射到自己的 contract 字段。

## 统计

- 标签组数量：`53`
- 路由数量：`991`
- 生成目标：`3` 个 skill reference

## 标签概览

| Tag | Ops | 常见能力 | 常见入参 |
| --- | ---: | --- | --- |
| `ASR-API` | 2 | 音频/媒体 / 字幕/转写 / 通用能力 | `input`, `task_id` |
| `Bilibili-App-API` | 11 | 通用能力 / 主页/账号 / 作品详情 / 搜索 | `av_id`, `bv_id`, `page`, `idx`, `next_offset`, `ps`, `keyword`, `page_size`, `order`, `user_id` |
| `Bilibili-Web-API` | 30 | 作品详情 / 主页/账号 / 直播 / 详情 | `bv_id`, `uid`, `pn`, `cid`, `dynamic_id`, `order`, `room_id`, `a_id`, `c_id`, `url` |
| `Demo-API` | 9 | 作品详情 / 主页/账号 / 通用能力 / 搜索 | 无 |
| `Douyin-App-V3-API` | 47 | 作品详情 / 搜索 / 主页/账号 / 详情 | `count`, `cursor`, `keyword`, `aweme_id`, `sec_user_id`, `offset`, `sort_type`, `publish_time`, `filter_duration`, `aweme_ids` |
| `Douyin-Billboard-API` | 31 | 热点/榜单 / 搜索 / 话题 / 详情 | `page_size`, `date_window`, `page`, `keyword`, `tags`, `sec_uid`, `option`, `page_num`, `end_date`, `start_date` |
| `Douyin-Creator-API` | 16 | 创作者 / 热点/榜单 / 话题 / 详情 | `billboard_tag`, `order_key`, `time_filter`, `limit`, `offset`, `category_id`, `order`, `activity_id`, `start_time`, `end_time` |
| `Douyin-Creator-V2-API` | 14 | 创作者 / 下载/媒体 / 搜索 / 热点/榜单 | `cookie`, `item_id`, `start_date`, `end_date`, `genres`, `primary_verticals`, `fields`, `need_long_article`, `metric_type`, `count` |
| `Douyin-Search-API` | 20 | 搜索 / 话题 / 主页/账号 / 作品详情 | `keyword`, `cursor`, `search_id`, `sort_type`, `publish_time`, `filter_duration`, `content_type`, `backtrace`, `douyin_user_fans`, `douyin_user_type` |
| `Douyin-Web-API` | 76 | 主页/账号 / 作品详情 / 通用能力 / 直播 | `count`, `cookie`, `refresh_index`, `keyword`, `sec_user_id`, `cursor`, `room_id`, `offset`, `aweme_id`, `max_cursor` |
| `Douyin-Xingtu-API` | 22 | 通用能力 / 作品详情 / 评论 / 热点/榜单 | `kolId`, `platformChannel`, `_range`, `page`, `onlyAssign`, `keyword`, `uri`, `durationTS`, `format`, `sec_user_id` |
| `Douyin-Xingtu-V2-API` | 21 | 创作者 / 通用能力 / 热点/榜单 / 评论 | `o_author_id`, `platform_source`, `limit`, `platform_channel`, `author_id`, `only_assign`, `flow_type`, `page`, `qualifier`, `period` |
| `Health-Check` | 1 | 通用能力 | 无 |
| `Hybrid-Parsing` | 1 | 作品详情 | `url`, `minimal`, `base64_url` |
| `Instagram-V1-API` | 29 | 主页/账号 / 作品详情 / 通用能力 / 评论 | `user_id`, `max_id`, `count`, `end_cursor`, `media_id`, `username`, `page`, `min_id`, `location_id`, `post_url` |
| `Instagram-V2-API` | 27 | 主页/账号 / 作品详情 / 搜索 / 评论 | `pagination_token`, `user_id`, `username`, `keyword`, `code_or_url`, `comment_id`, `feed_type`, `highlight_id`, `location_id`, `audio_canonical_id` |
| `Instagram-V3-API` | 26 | 主页/账号 / 作品详情 / 评论 / 搜索 | `user_id`, `username`, `url`, `first`, `after`, `query`, `media_id`, `code`, `max_id`, `comment_id` |
| `Kuaishou-App-API` | 20 | 作品详情 / 热点/榜单 / 主页/账号 / 搜索 | `pcursor`, `user_id`, `subTabId`, `subTabName`, `keyword`, `magic_face_id`, `photo_id`, `page`, `boardType`, `boardId` |
| `Kuaishou-Web-API` | 13 | 作品详情 / 主页/账号 / 热点/榜单 / 评论 | `pcursor`, `photo_id`, `user_id`, `share_link`, `board_type`, `share_text`, `url`, `root_comment_id` |
| `Lemon8-App-API` | 16 | 通用能力 / 主页/账号 / 作品详情 / 搜索 | `user_id`, `item_id`, `cursor`, `share_text`, `group_id`, `media_id`, `offset`, `query`, `max_cursor`, `filter_type` |
| `LinkedIn-Web-API` | 25 | 主页/账号 / 通用能力 / 作品详情 / 搜索 | `page`, `urn`, `company_id`, `pagination_token`, `sort_by`, `company`, `username`, `date_posted`, `experience_level`, `remote` |
| `Media-Ingest-API` | 2 | 广告 | `file_name`, `content_type`, `size_bytes`, `upload_id` |
| `PiPiXia-App-API` | 17 | 作品详情 / 主页/账号 / 搜索 / 详情 | `cursor`, `cell_id`, `user_id`, `cell_type`, `hashtag_id`, `feed_count`, `offset`, `hashtag_request_type`, `hashtag_sort_type`, `page` |
| `Reddit-APP-API` | 24 | 通用能力 / 主页/账号 / 作品详情 / 评论 | `need_format`, `after`, `sort`, `username`, `subreddit_name`, `subreddit_id`, `post_id`, `filter_posts`, `include_comment_id`, `comment_id` |
| `Sora2-API` | 17 | 作品详情 / 主页/账号 / 通用能力 / 评论 | `cursor`, `user_id`, `post_id`, `post_url`, `task_id`, `prompt`, `orientation`, `media_id`, `comment_id`, `eager_views` |
| `Temp-Mail-API` | 3 | 通用能力 | `token`, `message_id` |
| `Threads-Web-API` | 11 | 广告 / 主页/账号 / 作品详情 / 搜索 | `end_cursor`, `user_id`, `post_id`, `query`, `url`, `username` |
| `TikHub-Downloader-API` | 2 | 下载/媒体 | 无 |
| `TikHub-User-API` | 6 | 主页/账号 | `endpoint`, `request_per_day` |
| `TikTok-Ads-API` | 31 | 广告 / 搜索 / 详情 / 创作者 | `limit`, `page`, `country_code`, `period`, `keyword`, `period_type`, `industry`, `order_by`, `rank_type`, `material_id` |
| `TikTok-Analytics-API` | 4 | 数据分析 / 评论 / 创作者 / 作品详情 | `item_id`, `content_category`, `user_id` |
| `TikTok-App-V3-API` | 75 | 作品详情 / 电商 / 主页/账号 / 搜索 | `count`, `offset`, `keyword`, `sort_type`, `cursor`, `region`, `sec_user_id`, `user_id`, `room_id`, `seller_id` |
| `TikTok-Creator-API` | 14 | 创作者 / 作品详情 / 数据分析 / 电商 | `cookie`, `proxy`, `start_date`, `item_id`, `page`, `product_id`, `end_date`, `count`, `offset`, `item_ids` |
| `TikTok-Interaction-API` | 7 | 通用能力 / 评论 / 作品详情 / 评论回复 | `cookie`, `device_id`, `iid`, `proxy`, `aweme_id`, `text`, `api_key`, `invite_code`, `user_id`, `sec_user_id` |
| `TikTok-Shop-Web-API` | 15 | 电商 / 搜索 / 详情 / 热点/榜单 | `region`, `product_id`, `offset`, `seller_id`, `search_word`, `page_token`, `lang`, `count`, `sort_type`, `filter_id` |
| `TikTok-Web-API` | 58 | 通用能力 / 主页/账号 / 直播 / 作品详情 | `count`, `cursor`, `cookie`, `secUid`, `url`, `keyword`, `search_id`, `user_agent`, `offset`, `coverFormat` |
| `Toutiao-App-API` | 5 | 作品详情 / 主页/账号 / 评论 | `group_id`, `offset`, `user_profile_url`, `user_id` |
| `Toutiao-Web-API` | 2 | 作品详情 | `aweme_id` |
| `Twitter-Web-API` | 13 | 主页/账号 / 作品详情 / 评论 / 搜索 | `cursor`, `screen_name`, `tweet_id`, `rest_id`, `keyword`, `search_type`, `country`, `userId`, `count` |
| `WeChat-Channels-API` | 9 | 主页/账号 / 搜索 / 评论 / 热点/榜单 | `keywords`, `id`, `username`, `lastBuffer`, `comment_id`, `session_buffer`, `last_buffer`, `page`, `exportId` |
| `WeChat-Media-Platform-Web-API` | 10 | 作品详情 / 评论 / 详情 / 评论回复 | `url`, `comment_id`, `offset`, `buffer`, `content_id`, `ghid`, `sogou_url` |
| `Weibo-App-API` | 20 | 主页/账号 / 作品详情 / 搜索 / 详情 | `uid`, `page`, `since_id`, `status_id`, `query`, `count`, `max_id`, `category`, `search_type`, `sort_type` |
| `Weibo-Web-API` | 11 | 主页/账号 / 搜索 / 作品详情 / 评论 | `page`, `max_id`, `post_id`, `uid`, `channel_name`, `cid`, `mid`, `max_id_type`, `keyword`, `search_type` |
| `Weibo-Web-V2-API` | 33 | 搜索 / 主页/账号 / 作品详情 / 通用能力 | `page`, `uid`, `query`, `id`, `max_id`, `count`, `since_id`, `q`, `keyword`, `cursor` |
| `Xiaohongshu-App-API` | 12 | 作品详情 / 主页/账号 / 评论 / 电商 | `note_id`, `session_id`, `share_link`, `start`, `share_text`, `sort`, `user_id`, `keyword`, `page`, `search_id` |
| `Xiaohongshu-App-V2-API` | 21 | 作品详情 / 电商 / 搜索 / 详情 | `source`, `share_text`, `cursor`, `note_id`, `page`, `keyword`, `search_id`, `sku_id`, `user_id`, `tab` |
| `Xiaohongshu-Web-API` | 17 | 作品详情 / 主页/账号 / 搜索 / 评论 | `note_id`, `share_text`, `cookie`, `proxy`, `lastCursor`, `user_id`, `keyword`, `page`, `xsec_token`, `sort` |
| `Xiaohongshu-Web-V2-API` | 18 | 作品详情 / 主页/账号 / 通用能力 / 评论 | `note_id`, `user_id`, `cursor`, `page`, `keywords`, `short_url`, `sort_type`, `note_type`, `comment_id` |
| `Xigua-App-V2-API` | 7 | 作品详情 / 主页/账号 / 评论 / 搜索 | `item_id`, `user_id`, `offset`, `max_behot_time`, `count`, `keyword`, `order_type`, `min_duration`, `max_duration` |
| `YouTube-Web-API` | 21 | 作品详情 / 主页/账号 / 搜索 / 评论 | `continuation_token`, `language_code`, `country_code`, `channel_id`, `video_id`, `need_format`, `search_query`, `sort_by`, `lang`, `time_zone` |
| `YouTube-Web-V2-API` | 16 | 作品详情 / 主页/账号 / 搜索 / 直播 | `continuation_token`, `need_format`, `language_code`, `country_code`, `video_id`, `channel_id`, `video_url`, `sort_by`, `channel_url`, `search_query` |
| `Zhihu-Web-API` | 32 | 搜索 / 主页/账号 / 作品详情 / 通用能力 | `offset`, `limit`, `keyword`, `user_url_token`, `search_hash_id`, `article_id`, `order_by`, `message_content`, `message_id`, `show_all_topics` |
| `iOS-Shortcut` | 1 | 通用能力 | 无 |

## 完整路由目录

### `ASR-API`

- 路由数：`2`
- 标签说明：**(ASR 异步任务接口 / ASR async task endpoints)**
- 常见入参：`input`, `task_id`

- `POST /api/u2/v1/services/audio/asr/transcription`
  能力：音频/媒体 / 字幕/转写
  入参：无
  请求体：application/json: `input*`{`file_urls*`[]}
- `POST /api/u2/v1/tasks/{task_id}`
  能力：通用能力
  入参：path: `task_id*`
  请求体：无

### `Bilibili-App-API`

- 路由数：`11`
- 标签说明：**(哔哩哔哩App数据接口/Bilibili-App-API data endpoints)**
- 常见入参：`av_id`, `bv_id`, `page`, `idx`, `next_offset`, `ps`, `keyword`, `page_size`, `order`, `user_id`

- `GET /api/u1/v1/bilibili/app/fetch_bangumi_tab`
  能力：通用能力
  入参：无
  请求体：无
- `GET /api/u1/v1/bilibili/app/fetch_cinema_tab`
  能力：通用能力
  入参：无
  请求体：无
- `GET /api/u1/v1/bilibili/app/fetch_home_feed`
  能力：主页/账号
  入参：query: `idx`, `flush`, `pull`
  请求体：无
- `GET /api/u1/v1/bilibili/app/fetch_one_video`
  能力：作品详情
  入参：query: `av_id`, `bv_id`
  请求体：无
- `GET /api/u1/v1/bilibili/app/fetch_popular_feed`
  能力：通用能力
  入参：query: `idx`, `last_param`
  请求体：无
- `GET /api/u1/v1/bilibili/app/fetch_reply_detail`
  能力：评论回复 / 详情
  入参：query: `root*`, `av_id`, `bv_id`, `next_offset`, `ps`
  请求体：无
- `GET /api/u1/v1/bilibili/app/fetch_search_all`
  能力：搜索
  入参：query: `keyword*`, `page`, `page_size`, `order`
  请求体：无
- `GET /api/u1/v1/bilibili/app/fetch_search_by_type`
  能力：搜索
  入参：query: `keyword*`, `search_type`, `page`, `page_size`, `order`
  请求体：无
- `GET /api/u1/v1/bilibili/app/fetch_user_info`
  能力：主页/账号
  入参：query: `user_id*`
  请求体：无
- `GET /api/u1/v1/bilibili/app/fetch_user_videos`
  能力：主页/账号 / 作品详情
  入参：query: `user_id*`, `post_filter`, `page`, `ps`
  请求体：无
- `GET /api/u1/v1/bilibili/app/fetch_video_comments`
  能力：评论 / 作品详情
  入参：query: `av_id`, `bv_id`, `mode`, `next_offset`
  请求体：无

### `Bilibili-Web-API`

- 路由数：`30`
- 标签说明：**(哔哩哔哩Web数据接口/Bilibili-Web-API data endpoints)**
- 常见入参：`bv_id`, `uid`, `pn`, `cid`, `dynamic_id`, `order`, `room_id`, `a_id`, `c_id`, `url`

- `GET /api/u1/v1/bilibili/web/bv_to_aid`
  能力：通用能力
  入参：query: `bv_id*`
  请求体：无
- `GET /api/u1/v1/bilibili/web/fetch_all_live_areas`
  能力：直播
  入参：无
  请求体：无
- `GET /api/u1/v1/bilibili/web/fetch_collect_folders`
  能力：通用能力
  入参：query: `uid*`
  请求体：无
- `GET /api/u1/v1/bilibili/web/fetch_com_popular`
  能力：通用能力
  入参：query: `pn`
  请求体：无
- `GET /api/u1/v1/bilibili/web/fetch_comment_reply`
  能力：评论 / 评论回复
  入参：query: `bv_id*`, `pn`, `rpid*`
  请求体：无
- `GET /api/u1/v1/bilibili/web/fetch_dynamic_detail`
  能力：详情
  入参：query: `dynamic_id*`
  请求体：无
- `GET /api/u1/v1/bilibili/web/fetch_dynamic_detail_v2`
  能力：详情
  入参：query: `dynamic_id*`
  请求体：无
- `GET /api/u1/v1/bilibili/web/fetch_general_search`
  能力：搜索
  入参：query: `keyword*`, `order*`, `page*`, `page_size*`, `duration`, `pubtime_begin_s`, `pubtime_end_s`
  请求体：无
- `GET /api/u1/v1/bilibili/web/fetch_get_user_id`
  能力：主页/账号
  入参：query: `share_link*`
  请求体：无
- `GET /api/u1/v1/bilibili/web/fetch_hot_search`
  能力：搜索 / 热点/榜单
  入参：query: `limit*`
  请求体：无
- `GET /api/u1/v1/bilibili/web/fetch_live_room_detail`
  能力：详情 / 直播
  入参：query: `room_id*`
  请求体：无
- `GET /api/u1/v1/bilibili/web/fetch_live_streamers`
  能力：直播
  入参：query: `area_id*`, `pn`
  请求体：无
- `GET /api/u1/v1/bilibili/web/fetch_live_videos`
  能力：作品详情 / 直播
  入参：query: `room_id*`
  请求体：无
- `GET /api/u1/v1/bilibili/web/fetch_one_video`
  能力：作品详情
  入参：query: `bv_id*`
  请求体：无
- `GET /api/u1/v1/bilibili/web/fetch_one_video_v2`
  能力：作品详情
  入参：query: `a_id*`, `c_id*`
  请求体：无
- `GET /api/u1/v1/bilibili/web/fetch_one_video_v3`
  能力：作品详情
  入参：query: `url*`
  请求体：无
- `GET /api/u1/v1/bilibili/web/fetch_user_collection_videos`
  能力：主页/账号 / 作品详情
  入参：query: `folder_id*`, `pn`
  请求体：无
- `GET /api/u1/v1/bilibili/web/fetch_user_dynamic`
  能力：主页/账号
  入参：query: `uid*`, `offset`
  请求体：无
- `GET /api/u1/v1/bilibili/web/fetch_user_post_videos`
  能力：主页/账号 / 作品详情
  入参：query: `uid*`, `pn`, `order`
  请求体：无
- `GET /api/u1/v1/bilibili/web/fetch_user_profile`
  能力：主页/账号
  入参：query: `uid*`
  请求体：无
- `GET /api/u1/v1/bilibili/web/fetch_user_relation_stat`
  能力：主页/账号
  入参：query: `uid*`
  请求体：无
- `GET /api/u1/v1/bilibili/web/fetch_user_up_stat`
  能力：主页/账号
  入参：query: `uid*`
  请求体：无
- `GET /api/u1/v1/bilibili/web/fetch_video_comments`
  能力：评论 / 作品详情
  入参：query: `bv_id*`, `pn`
  请求体：无
- `GET /api/u1/v1/bilibili/web/fetch_video_danmaku`
  能力：作品详情
  入参：query: `cid*`
  请求体：无
- `GET /api/u1/v1/bilibili/web/fetch_video_detail`
  能力：作品详情 / 详情
  入参：query: `aid*`
  请求体：无
- `GET /api/u1/v1/bilibili/web/fetch_video_parts`
  能力：作品详情
  入参：query: `bv_id*`
  请求体：无
- `GET /api/u1/v1/bilibili/web/fetch_video_play_info`
  能力：作品详情
  入参：query: `url*`
  请求体：无
- `GET /api/u1/v1/bilibili/web/fetch_video_playurl`
  能力：作品详情
  入参：query: `bv_id*`, `cid*`
  请求体：无
- `GET /api/u1/v1/bilibili/web/fetch_video_subtitle`
  能力：作品详情 / 字幕/转写
  入参：query: `a_id*`, `c_id*`
  请求体：无
- `POST /api/u1/v1/bilibili/web/fetch_vip_video_playurl`
  能力：作品详情
  入参：无
  请求体：application/json: `bv_id*`:string, `cid*`:string, `cookie*`:string

### `Demo-API`

- 路由数：`9`
- 标签说明：**(TikHub API示例项目/Demo Project)**
- 常见入参：无

- `GET /api/u1/v1/demo/demo/cache_status`
  能力：通用能力
  入参：无
  请求体：无
- `GET /api/u1/v1/demo/douyin/app/fetch_one_video`
  能力：作品详情
  入参：无
  请求体：无
- `GET /api/u1/v1/demo/douyin/web/fetch_one_video`
  能力：作品详情
  入参：无
  请求体：无
- `GET /api/u1/v1/demo/douyin_search/app/general_search`
  能力：搜索
  入参：无
  请求体：无
- `GET /api/u1/v1/demo/instagram/web/fetch_user_info`
  能力：主页/账号
  入参：无
  请求体：无
- `GET /api/u1/v1/demo/kuaishou/web/fetch_one_video`
  能力：作品详情
  入参：无
  请求体：无
- `GET /api/u1/v1/demo/tiktok/app/fetch_one_video`
  能力：作品详情
  入参：无
  请求体：无
- `GET /api/u1/v1/demo/tiktok/web/fetch_user_profile`
  能力：主页/账号
  入参：无
  请求体：无
- `GET /api/u1/v1/demo/wechat/article_extract`
  能力：作品详情
  入参：无
  请求体：无

### `Douyin-App-V3-API`

- 路由数：`47`
- 标签说明：**(抖音-App-V3数据接口（当前最新版本）/Douyin-App-V3-API (Current latest version))**
- 常见入参：`count`, `cursor`, `keyword`, `aweme_id`, `sec_user_id`, `offset`, `sort_type`, `publish_time`, `filter_duration`, `aweme_ids`

- `GET /api/u1/v1/douyin/app/v3/add_video_play_count`
  能力：作品详情
  入参：query: `aweme_type*`, `item_id*`, `cookie`
  请求体：无
- `GET /api/u1/v1/douyin/app/v3/fetch_brand_hot_search_list`
  能力：搜索 / 热点/榜单
  入参：无
  请求体：无
- `GET /api/u1/v1/douyin/app/v3/fetch_brand_hot_search_list_detail`
  能力：搜索 / 热点/榜单 / 详情
  入参：query: `category_id*`
  请求体：无
- `GET /api/u1/v1/douyin/app/v3/fetch_general_search_result`
  能力：搜索
  入参：query: `keyword*`, `offset`, `count`, `sort_type`, `publish_time`, `filter_duration`, `content_type`
  请求体：无
- `GET /api/u1/v1/douyin/app/v3/fetch_hashtag_detail`
  能力：详情 / 话题
  入参：query: `ch_id*`
  请求体：无
- `GET /api/u1/v1/douyin/app/v3/fetch_hashtag_search_result`
  能力：搜索 / 话题
  入参：query: `keyword*`, `offset`, `count`
  请求体：无
- `GET /api/u1/v1/douyin/app/v3/fetch_hashtag_video_list`
  能力：作品详情 / 话题
  入参：query: `ch_id*`, `cursor`, `sort_type`, `count`
  请求体：无
- `GET /api/u1/v1/douyin/app/v3/fetch_hot_search_list`
  能力：搜索 / 热点/榜单
  入参：query: `board_type`, `board_sub_type`
  请求体：无
- `GET /api/u1/v1/douyin/app/v3/fetch_live_hot_search_list`
  能力：搜索 / 热点/榜单 / 直播
  入参：无
  请求体：无
- `GET /api/u1/v1/douyin/app/v3/fetch_live_search_result`
  能力：搜索 / 直播
  入参：query: `keyword*`, `cursor`, `count`
  请求体：无
- `POST /api/u1/v1/douyin/app/v3/fetch_multi_video`
  能力：作品详情
  入参：无
  请求体：application/json: 动态对象
- `POST /api/u1/v1/douyin/app/v3/fetch_multi_video_high_quality_play_url`
  能力：作品详情
  入参：无
  请求体：application/json: `aweme_ids`:string
- `GET /api/u1/v1/douyin/app/v3/fetch_multi_video_statistics`
  能力：作品详情
  入参：query: `aweme_ids*`
  请求体：无
- `POST /api/u1/v1/douyin/app/v3/fetch_multi_video_v2`
  能力：作品详情
  入参：无
  请求体：application/json: 动态对象
- `GET /api/u1/v1/douyin/app/v3/fetch_music_detail`
  能力：详情 / 音乐/音频
  入参：query: `music_id*`
  请求体：无
- `GET /api/u1/v1/douyin/app/v3/fetch_music_hot_search_list`
  能力：搜索 / 热点/榜单 / 音乐/音频
  入参：query: `chart_type`, `cursor`
  请求体：无
- `GET /api/u1/v1/douyin/app/v3/fetch_music_search_result`
  能力：搜索 / 音乐/音频
  入参：query: `keyword*`, `offset`, `count`
  请求体：无
- `GET /api/u1/v1/douyin/app/v3/fetch_music_video_list`
  能力：作品详情 / 音乐/音频
  入参：query: `music_id*`, `cursor`, `count`
  请求体：无
- `GET /api/u1/v1/douyin/app/v3/fetch_one_video`
  能力：作品详情
  入参：query: `aweme_id*`
  请求体：无
- `GET /api/u1/v1/douyin/app/v3/fetch_one_video_by_share_url`
  能力：作品详情
  入参：query: `share_url*`
  请求体：无
- `GET /api/u1/v1/douyin/app/v3/fetch_one_video_v2`
  能力：作品详情
  入参：query: `aweme_id*`
  请求体：无
- `GET /api/u1/v1/douyin/app/v3/fetch_one_video_v3`
  能力：作品详情
  入参：query: `aweme_id*`
  请求体：无
- `GET /api/u1/v1/douyin/app/v3/fetch_series_detail`
  能力：详情
  入参：query: `series_id*`
  请求体：无
- `GET /api/u1/v1/douyin/app/v3/fetch_series_video_list`
  能力：作品详情
  入参：query: `series_id*`, `cursor`
  请求体：无
- `GET /api/u1/v1/douyin/app/v3/fetch_share_info_by_share_code`
  能力：通用能力
  入参：query: `share_code*`
  请求体：无
- `GET /api/u1/v1/douyin/app/v3/fetch_user_fans_list`
  能力：主页/账号
  入参：query: `sec_user_id`, `max_time`, `count`
  请求体：无
- `GET /api/u1/v1/douyin/app/v3/fetch_user_following_list`
  能力：主页/账号
  入参：query: `sec_user_id`, `max_time`, `count`
  请求体：无
- `GET /api/u1/v1/douyin/app/v3/fetch_user_like_videos`
  能力：主页/账号 / 作品详情
  入参：query: `sec_user_id*`, `max_cursor`, `counts`
  请求体：无
- `GET /api/u1/v1/douyin/app/v3/fetch_user_post_videos`
  能力：主页/账号 / 作品详情
  入参：query: `sec_user_id*`, `max_cursor`, `count`, `sort_type`
  请求体：无
- `GET /api/u1/v1/douyin/app/v3/fetch_user_search_result`
  能力：搜索 / 主页/账号
  入参：query: `keyword*`, `offset`, `count`, `douyin_user_fans`, `douyin_user_type`
  请求体：无
- `GET /api/u1/v1/douyin/app/v3/fetch_user_series_list`
  能力：主页/账号
  入参：query: `user_id`, `sec_user_id`, `cursor`
  请求体：无
- `GET /api/u1/v1/douyin/app/v3/fetch_video_comment_replies`
  能力：评论 / 作品详情
  入参：query: `item_id*`, `comment_id*`, `cursor`, `count`
  请求体：无
- `GET /api/u1/v1/douyin/app/v3/fetch_video_comments`
  能力：评论 / 作品详情
  入参：query: `aweme_id*`, `cursor`, `count`
  请求体：无
- `GET /api/u1/v1/douyin/app/v3/fetch_video_high_quality_play_url`
  能力：作品详情
  入参：query: `aweme_id`, `share_url`
  请求体：无
- `GET /api/u1/v1/douyin/app/v3/fetch_video_mix_detail`
  能力：作品详情 / 详情
  入参：query: `mix_id*`
  请求体：无
- `GET /api/u1/v1/douyin/app/v3/fetch_video_mix_post_list`
  能力：作品详情
  入参：query: `mix_id*`, `cursor`, `count`
  请求体：无
- `GET /api/u1/v1/douyin/app/v3/fetch_video_search_result`
  能力：搜索 / 作品详情
  入参：query: `keyword*`, `offset`, `count`, `sort_type`, `publish_time`, `filter_duration`
  请求体：无
- `GET /api/u1/v1/douyin/app/v3/fetch_video_search_result_v2`
  能力：搜索 / 作品详情
  入参：query: `keyword*`, `sort_type`, `publish_time`, `filter_duration`, `page`, `search_id`
  请求体：无
- `GET /api/u1/v1/douyin/app/v3/fetch_video_statistics`
  能力：作品详情
  入参：query: `aweme_ids*`
  请求体：无
- `GET /api/u1/v1/douyin/app/v3/generate_douyin_short_url`
  能力：通用能力
  入参：query: `url*`
  请求体：无
- `GET /api/u1/v1/douyin/app/v3/generate_douyin_video_share_qrcode`
  能力：作品详情
  入参：query: `object_id*`
  请求体：无
- `GET /api/u1/v1/douyin/app/v3/handler_user_profile`
  能力：主页/账号
  入参：query: `sec_user_id*`
  请求体：无
- `GET /api/u1/v1/douyin/app/v3/open_douyin_app_to_keyword_search`
  能力：搜索
  入参：query: `keyword*`
  请求体：无
- `GET /api/u1/v1/douyin/app/v3/open_douyin_app_to_send_private_message`
  能力：通用能力
  入参：query: `uid*`, `sec_uid*`
  请求体：无
- `GET /api/u1/v1/douyin/app/v3/open_douyin_app_to_user_profile`
  能力：主页/账号
  入参：query: `uid*`, `sec_uid*`
  请求体：无
- `GET /api/u1/v1/douyin/app/v3/open_douyin_app_to_video_detail`
  能力：作品详情 / 详情
  入参：query: `aweme_id*`
  请求体：无
- `GET /api/u1/v1/douyin/app/v3/register_device`
  能力：通用能力
  入参：query: `proxy`
  请求体：无

### `Douyin-Billboard-API`

- 路由数：`31`
- 标签说明：**(抖音热点榜数据接口/Douyin-Billboard-API data endpoints)**
- 常见入参：`page_size`, `date_window`, `page`, `keyword`, `tags`, `sec_uid`, `option`, `page_num`, `end_date`, `start_date`

- `GET /api/u1/v1/douyin/billboard/fetch_city_list`
  能力：热点/榜单
  入参：无
  请求体：无
- `GET /api/u1/v1/douyin/billboard/fetch_content_tag`
  能力：热点/榜单
  入参：无
  请求体：无
- `GET /api/u1/v1/douyin/billboard/fetch_hot_account_fans_interest_account_list`
  能力：热点/榜单
  入参：query: `sec_uid*`
  请求体：无
- `GET /api/u1/v1/douyin/billboard/fetch_hot_account_fans_interest_search_list`
  能力：搜索 / 热点/榜单
  入参：query: `sec_uid*`
  请求体：无
- `GET /api/u1/v1/douyin/billboard/fetch_hot_account_fans_interest_topic_list`
  能力：热点/榜单 / 话题
  入参：query: `sec_uid*`
  请求体：无
- `GET /api/u1/v1/douyin/billboard/fetch_hot_account_fans_portrait_list`
  能力：热点/榜单
  入参：query: `sec_uid*`, `option`
  请求体：无
- `GET /api/u1/v1/douyin/billboard/fetch_hot_account_item_analysis_list`
  能力：热点/榜单
  入参：query: `sec_uid*`
  请求体：无
- `POST /api/u1/v1/douyin/billboard/fetch_hot_account_list`
  能力：热点/榜单
  入参：无
  请求体：application/json: `date_window`:integer, `page_num`:integer, `page_size`:integer, `query_tag`{...}
- `GET /api/u1/v1/douyin/billboard/fetch_hot_account_search_list`
  能力：搜索 / 热点/榜单
  入参：query: `keyword*`, `cursor*`
  请求体：无
- `GET /api/u1/v1/douyin/billboard/fetch_hot_account_trends_list`
  能力：热点/榜单
  入参：query: `sec_uid*`, `option`, `date_window`
  请求体：无
- `GET /api/u1/v1/douyin/billboard/fetch_hot_calendar_detail`
  能力：热点/榜单 / 详情
  入参：query: `calendar_id*`
  请求体：无
- `POST /api/u1/v1/douyin/billboard/fetch_hot_calendar_list`
  能力：热点/榜单
  入参：无
  请求体：application/json: `city_code`:string, `category_code`:string, `end_date`:integer, `start_date`:integer
- `GET /api/u1/v1/douyin/billboard/fetch_hot_category_list`
  能力：热点/榜单
  入参：query: `billboard_type*`, `snapshot_time`, `start_date`, `end_date`, `keyword`
  请求体：无
- `GET /api/u1/v1/douyin/billboard/fetch_hot_challenge_list`
  能力：热点/榜单 / 话题
  入参：query: `page*`, `page_size*`, `keyword`
  请求体：无
- `GET /api/u1/v1/douyin/billboard/fetch_hot_city_list`
  能力：热点/榜单
  入参：query: `page*`, `page_size*`, `order*`, `city_code`, `sentence_tag`, `keyword`
  请求体：无
- `GET /api/u1/v1/douyin/billboard/fetch_hot_comment_word_list`
  能力：评论 / 热点/榜单
  入参：query: `aweme_id*`
  请求体：无
- `GET /api/u1/v1/douyin/billboard/fetch_hot_item_trends_list`
  能力：热点/榜单
  入参：query: `aweme_id`, `option`, `date_window`
  请求体：无
- `GET /api/u1/v1/douyin/billboard/fetch_hot_rise_list`
  能力：热点/榜单
  入参：query: `page*`, `page_size*`, `order*`, `sentence_tag`, `keyword`
  请求体：无
- `POST /api/u1/v1/douyin/billboard/fetch_hot_total_high_fan_list`
  能力：热点/榜单
  入参：无
  请求体：application/json: `page`:integer, `page_size`:integer, `date_window`:integer, `tags`[]
- `POST /api/u1/v1/douyin/billboard/fetch_hot_total_high_like_list`
  能力：热点/榜单
  入参：无
  请求体：application/json: `page`:integer, `page_size`:integer, `date_window`:integer, `tags`[]
- `POST /api/u1/v1/douyin/billboard/fetch_hot_total_high_play_list`
  能力：热点/榜单
  入参：无
  请求体：application/json: `page`:integer, `page_size`:integer, `date_window`:integer, `tags`[]
- `POST /api/u1/v1/douyin/billboard/fetch_hot_total_high_search_list`
  能力：搜索 / 热点/榜单
  入参：无
  请求体：application/json: `page_num`:integer, `page_size`:integer, `date_window`:integer, `keyword`:string
- `POST /api/u1/v1/douyin/billboard/fetch_hot_total_high_topic_list`
  能力：热点/榜单 / 话题
  入参：无
  请求体：application/json: `page`:integer, `page_size`:integer, `date_window`:integer, `tags`[]
- `GET /api/u1/v1/douyin/billboard/fetch_hot_total_hot_word_detail_list`
  能力：热点/榜单 / 详情
  入参：query: `keyword*`, `word_id*`, `query_day*`
  请求体：无
- `POST /api/u1/v1/douyin/billboard/fetch_hot_total_hot_word_list`
  能力：热点/榜单
  入参：无
  请求体：application/json: `page_num`:integer, `page_size`:integer, `date_window`:integer, `keyword`:string
- `GET /api/u1/v1/douyin/billboard/fetch_hot_total_list`
  能力：热点/榜单
  入参：query: `page*`, `page_size*`, `type*`, `snapshot_time`, `start_date`, `end_date`, `sentence_tag`, `keyword`
  请求体：无
- `POST /api/u1/v1/douyin/billboard/fetch_hot_total_low_fan_list`
  能力：热点/榜单
  入参：无
  请求体：application/json: `page`:integer, `page_size`:integer, `date_window`:integer, `tags`[]
- `POST /api/u1/v1/douyin/billboard/fetch_hot_total_search_list`
  能力：搜索 / 热点/榜单
  入参：无
  请求体：application/json: `page_num`:integer, `page_size`:integer, `date_window`:integer, `keyword`:string
- `POST /api/u1/v1/douyin/billboard/fetch_hot_total_topic_list`
  能力：热点/榜单 / 话题
  入参：无
  请求体：application/json: `page`:integer, `page_size`:integer, `date_window`:integer, `tags`[]
- `POST /api/u1/v1/douyin/billboard/fetch_hot_total_video_list`
  能力：热点/榜单 / 作品详情
  入参：无
  请求体：application/json: `page`:integer, `page_size`:integer, `date_window`:integer, `sub_type`:integer, `tags`[]
- `GET /api/u1/v1/douyin/billboard/fetch_hot_user_portrait_list`
  能力：热点/榜单 / 主页/账号
  入参：query: `aweme_id*`, `option`
  请求体：无

### `Douyin-Creator-API`

- 路由数：`16`
- 标签说明：**(抖音创作者数据接口/Douyin-Creator-API data endpoints)**
- 常见入参：`billboard_tag`, `order_key`, `time_filter`, `limit`, `offset`, `category_id`, `order`, `activity_id`, `start_time`, `end_time`

- `GET /api/u1/v1/douyin/creator/fetch_creator_activity_detail`
  能力：创作者 / 详情
  入参：query: `activity_id*`
  请求体：无
- `GET /api/u1/v1/douyin/creator/fetch_creator_activity_list`
  能力：创作者
  入参：query: `start_time*`, `end_time*`
  请求体：无
- `GET /api/u1/v1/douyin/creator/fetch_creator_content_category`
  能力：创作者
  入参：无
  请求体：无
- `GET /api/u1/v1/douyin/creator/fetch_creator_content_course`
  能力：创作者
  入参：query: `category_id*`, `order`, `limit`, `offset`
  请求体：无
- `GET /api/u1/v1/douyin/creator/fetch_creator_hot_challenge_billboard`
  能力：热点/榜单 / 创作者 / 话题
  入参：无
  请求体：无
- `GET /api/u1/v1/douyin/creator/fetch_creator_hot_course`
  能力：热点/榜单 / 创作者
  入参：query: `order`, `limit`, `offset`, `category_id`
  请求体：无
- `GET /api/u1/v1/douyin/creator/fetch_creator_hot_music_billboard`
  能力：热点/榜单 / 创作者 / 音乐/音频
  入参：query: `billboard_tag`, `order_key`, `time_filter`
  请求体：无
- `GET /api/u1/v1/douyin/creator/fetch_creator_hot_props_billboard`
  能力：热点/榜单 / 创作者
  入参：query: `billboard_tag`, `order_key`, `time_filter`
  请求体：无
- `GET /api/u1/v1/douyin/creator/fetch_creator_hot_spot_billboard`
  能力：热点/榜单 / 创作者
  入参：query: `billboard_tag`, `hot_search_type`, `city_code`
  请求体：无
- `GET /api/u1/v1/douyin/creator/fetch_creator_hot_topic_billboard`
  能力：热点/榜单 / 创作者 / 话题
  入参：query: `billboard_tag`, `order_key`, `time_filter`
  请求体：无
- `GET /api/u1/v1/douyin/creator/fetch_creator_material_center_billboard`
  能力：热点/榜单 / 创作者
  入参：query: `billboard_tag`, `order_key`, `time_filter`
  请求体：无
- `GET /api/u1/v1/douyin/creator/fetch_creator_material_center_config`
  能力：创作者
  入参：无
  请求体：无
- `GET /api/u1/v1/douyin/creator/fetch_industry_category_config`
  能力：创作者
  入参：无
  请求体：无
- `GET /api/u1/v1/douyin/creator/fetch_mission_task_list`
  能力：创作者
  入参：query: `cursor`, `limit`, `mission_type`, `tab_scene`, `industry_lv1`, `industry_lv2`, `platform_channel`, `pay_type`, `greater_than_cost_progress`, `publish_time_start`, `quick_selector_scene`, `keyword`
  请求体：无
- `GET /api/u1/v1/douyin/creator/fetch_user_search`
  能力：搜索 / 创作者 / 主页/账号
  入参：query: `user_name*`
  请求体：无
- `GET /api/u1/v1/douyin/creator/fetch_video_danmaku_list`
  能力：创作者 / 作品详情
  入参：query: `item_id*`, `count`, `offset`, `order_type`, `is_blocked`
  请求体：无

### `Douyin-Creator-V2-API`

- 路由数：`14`
- 标签说明：**(抖音创作者V2数据接口（需要用户Cookie，可获取作品流量总览等数据）/Douyin-Creator-V2-API data endpoints (Requires user Cookie, can get item traffic overview data))**
- 常见入参：`cookie`, `item_id`, `start_date`, `end_date`, `genres`, `primary_verticals`, `fields`, `need_long_article`, `metric_type`, `count`

- `POST /api/u1/v1/douyin/creator_v2/fetch_author_diagnosis`
  能力：创作者
  入参：无
  请求体：application/json: `cookie*`:string
- `POST /api/u1/v1/douyin/creator_v2/fetch_item_analysis_involved_vertical`
  能力：创作者
  入参：无
  请求体：application/json: `cookie*`:string, `start_date*`:string, `end_date*`:string
- `POST /api/u1/v1/douyin/creator_v2/fetch_item_analysis_item_performance`
  能力：创作者
  入参：无
  请求体：application/json: `cookie*`:string, `start_date*`:string, `end_date*`:string, `genres`[], `primary_verticals*`[], `metric_type`:integer
- `POST /api/u1/v1/douyin/creator_v2/fetch_item_analysis_overview`
  能力：创作者
  入参：无
  请求体：application/json: `cookie*`:string, `start_date*`:string, `end_date*`:string, `genres`[], `primary_verticals*`[]
- `POST /api/u1/v1/douyin/creator_v2/fetch_item_audience_others`
  能力：创作者
  入参：无
  请求体：application/json: `cookie*`:string, `item_id*`:string
- `POST /api/u1/v1/douyin/creator_v2/fetch_item_audience_portrait`
  能力：创作者
  入参：无
  请求体：application/json: `cookie*`:string, `item_id*`:string
- `POST /api/u1/v1/douyin/creator_v2/fetch_item_danmaku_analysis`
  能力：创作者
  入参：无
  请求体：application/json: `cookie*`:string, `item_id*`:string
- `POST /api/u1/v1/douyin/creator_v2/fetch_item_list`
  能力：创作者
  入参：无
  请求体：application/json: `cookie*`:string, `count`:integer, `order_by`:integer, `fields`:string, `need_cooperation`:boolean, `start_time*`:integer, `end_time*`:integer, `need_long_article`:boolean, ...
- `POST /api/u1/v1/douyin/creator_v2/fetch_item_list_download`
  能力：创作者 / 下载/媒体
  入参：无
  请求体：application/json: `cookie*`:string, `min_cursor*`:integer, `max_cursor*`:integer, `type_filters`[], `need_long_article`:boolean
- `POST /api/u1/v1/douyin/creator_v2/fetch_item_overview_data`
  能力：创作者
  入参：无
  请求体：application/json: `cookie*`:string, `ids*`:string, `fields`:string
- `POST /api/u1/v1/douyin/creator_v2/fetch_item_play_source`
  能力：创作者
  入参：无
  请求体：application/json: `cookie*`:string, `item_id*`:string
- `POST /api/u1/v1/douyin/creator_v2/fetch_item_search_keyword`
  能力：搜索 / 创作者
  入参：无
  请求体：application/json: `cookie*`:string, `item_id*`:string
- `POST /api/u1/v1/douyin/creator_v2/fetch_item_watch_trend`
  能力：热点/榜单 / 创作者
  入参：无
  请求体：application/json: `cookie*`:string, `item_id*`:string, `analysis_type`:integer
- `POST /api/u1/v1/douyin/creator_v2/fetch_live_room_history_list`
  能力：创作者 / 直播
  入参：无
  请求体：application/json: `cookie*`:string, `start_date*`:string, `end_date*`:string, `limit`:integer, `need_living`:integer, `download`:integer

### `Douyin-Search-API`

- 路由数：`20`
- 标签说明：**(抖音搜索数据接口（当前最新版，请优先使用此目录下的接口而不是其他目录下的搜索接口）/Douyin-Search-API data endpoints (Current latest version, please use the interfaces in this directory first instead of the search interfaces in other directories))**
- 常见入参：`keyword`, `cursor`, `search_id`, `sort_type`, `publish_time`, `filter_duration`, `content_type`, `backtrace`, `douyin_user_fans`, `douyin_user_type`

- `POST /api/u1/v1/douyin/search/fetch_challenge_search_v1`
  能力：搜索 / 话题
  入参：无
  请求体：application/json: `keyword`:string, `cursor`:integer, `sort_type`:string, `publish_time`:string, `filter_duration`:string, `content_type`:string, `search_id`:string, `backtrace`:string
- `POST /api/u1/v1/douyin/search/fetch_challenge_search_v2`
  能力：搜索 / 话题
  入参：无
  请求体：application/json: `keyword`:string, `cursor`:integer, `sort_type`:string, `publish_time`:string, `filter_duration`:string, `content_type`:string, `search_id`:string, `backtrace`:string
- `POST /api/u1/v1/douyin/search/fetch_challenge_suggest`
  能力：搜索 / 话题
  入参：无
  请求体：application/json: `keyword`:string
- `POST /api/u1/v1/douyin/search/fetch_discuss_search`
  能力：搜索
  入参：无
  请求体：application/json: `keyword`:string, `cursor`:integer, `sort_type`:string, `publish_time`:string, `filter_duration`:string, `content_type`:string, `search_id`:string, `backtrace`:string
- `POST /api/u1/v1/douyin/search/fetch_experience_search`
  能力：搜索
  入参：无
  请求体：application/json: `keyword`:string, `cursor`:integer, `sort_type`:string, `publish_time`:string, `filter_duration`:string, `content_type`:string, `search_id`:string, `backtrace`:string
- `POST /api/u1/v1/douyin/search/fetch_general_search_v1`
  能力：搜索
  入参：无
  请求体：application/json: `keyword`:string, `cursor`:integer, `sort_type`:string, `publish_time`:string, `filter_duration`:string, `content_type`:string, `search_id`:string, `backtrace`:string
- `POST /api/u1/v1/douyin/search/fetch_general_search_v2`
  能力：搜索
  入参：无
  请求体：application/json: `keyword`:string, `cursor`:integer, `sort_type`:string, `publish_time`:string, `filter_duration`:string, `content_type`:string, `search_id`:string, `backtrace`:string
- `POST /api/u1/v1/douyin/search/fetch_general_search_v3`
  能力：搜索
  入参：无
  请求体：application/json: `keyword`:string, `cursor`:integer, `sort_type`:string, `publish_time`:string, `filter_duration`:string, `content_type`:string, `search_id`:string, `backtrace`:string
- `POST /api/u1/v1/douyin/search/fetch_image_search`
  能力：搜索
  入参：无
  请求体：application/json: `keyword`:string, `cursor`:integer, `sort_type`:string, `publish_time`:string, `filter_duration`:string, `content_type`:string, `search_id`:string, `backtrace`:string
- `POST /api/u1/v1/douyin/search/fetch_image_search_v3`
  能力：搜索
  入参：无
  请求体：application/json: `keyword*`:string, `cursor`:integer, `search_id`:string
- `POST /api/u1/v1/douyin/search/fetch_live_search_v1`
  能力：搜索 / 直播
  入参：无
  请求体：application/json: `keyword`:string, `cursor`:integer, `sort_type`:string, `publish_time`:string, `filter_duration`:string, `content_type`:string, `search_id`:string, `backtrace`:string
- `POST /api/u1/v1/douyin/search/fetch_multi_search`
  能力：搜索
  入参：无
  请求体：application/json: `keyword`:string, `cursor`:integer, `sort_type`:string, `publish_time`:string, `filter_duration`:string, `content_type`:string, `search_id`:string, `backtrace`:string
- `POST /api/u1/v1/douyin/search/fetch_music_search`
  能力：搜索 / 音乐/音频
  入参：无
  请求体：application/json: `keyword`:string, `cursor`:integer, `sort_type`:string, `publish_time`:string, `filter_duration`:string, `content_type`:string, `search_id`:string, `backtrace`:string
- `POST /api/u1/v1/douyin/search/fetch_school_search`
  能力：搜索
  入参：无
  请求体：application/json: `keyword`:string
- `POST /api/u1/v1/douyin/search/fetch_search_suggest`
  能力：搜索
  入参：无
  请求体：application/json: `keyword`:string
- `POST /api/u1/v1/douyin/search/fetch_user_search`
  能力：搜索 / 主页/账号
  入参：无
  请求体：application/json: `keyword`:string, `cursor`:integer, `douyin_user_fans`:string, `douyin_user_type`:string, `search_id`:string
- `POST /api/u1/v1/douyin/search/fetch_user_search_v2`
  能力：搜索 / 主页/账号
  入参：无
  请求体：application/json: `keyword`:string, `cursor`:integer
- `POST /api/u1/v1/douyin/search/fetch_video_search_v1`
  能力：搜索 / 作品详情
  入参：无
  请求体：application/json: `keyword`:string, `cursor`:integer, `sort_type`:string, `publish_time`:string, `filter_duration`:string, `content_type`:string, `search_id`:string, `backtrace`:string
- `POST /api/u1/v1/douyin/search/fetch_video_search_v2`
  能力：搜索 / 作品详情
  入参：无
  请求体：application/json: `keyword`:string, `cursor`:integer, `sort_type`:string, `publish_time`:string, `filter_duration`:string, `content_type`:string, `search_id`:string, `backtrace`:string
- `POST /api/u1/v1/douyin/search/fetch_vision_search`
  能力：搜索
  入参：无
  请求体：application/json: `image_uri*`:string, `cursor`:integer, `search_id`:string, `search_source`:string, `detection`:string, `detection_index`:integer, `user_query`:string, `aweme_id`:string

### `Douyin-Web-API`

- 路由数：`76`
- 标签说明：**(抖音Web数据接口/Douyin-Web-API data endpoints)**
- 常见入参：`count`, `cookie`, `refresh_index`, `keyword`, `sec_user_id`, `cursor`, `room_id`, `offset`, `aweme_id`, `max_cursor`

- `GET /api/u1/v1/douyin/web/douyin_live_room`
  能力：直播
  入参：query: `live_room_url*`, `danmaku_type*`
  请求体：无
- `GET /api/u1/v1/douyin/web/encrypt_uid_to_sec_user_id`
  能力：主页/账号
  入参：query: `uid*`
  请求体：无
- `GET /api/u1/v1/douyin/web/fetch_batch_user_profile_v1`
  能力：主页/账号
  入参：query: `sec_user_ids*`
  请求体：无
- `GET /api/u1/v1/douyin/web/fetch_batch_user_profile_v2`
  能力：主页/账号
  入参：query: `sec_user_ids*`
  请求体：无
- `GET /api/u1/v1/douyin/web/fetch_cartoon_aweme`
  能力：通用能力
  入参：query: `count*`, `refresh_index`, `cookie`
  请求体：无
- `POST /api/u1/v1/douyin/web/fetch_challenge_posts`
  能力：作品详情 / 话题
  入参：无
  请求体：application/json: `challenge_id`:string, `sort_type`:integer, `cursor`:integer, `count`:integer, `cookie`:string
- `GET /api/u1/v1/douyin/web/fetch_douyin_web_guest_cookie`
  能力：通用能力
  入参：query: `user_agent*`
  请求体：无
- `GET /api/u1/v1/douyin/web/fetch_food_aweme`
  能力：通用能力
  入参：query: `count*`, `refresh_index`, `cookie`
  请求体：无
- `GET /api/u1/v1/douyin/web/fetch_game_aweme`
  能力：通用能力
  入参：query: `count*`, `refresh_index`, `cookie`
  请求体：无
- `GET /api/u1/v1/douyin/web/fetch_general_search_result`
  能力：搜索
  入参：query: `keyword*`, `offset`, `count`, `sort_type`, `publish_time`, `filter_duration`, `search_range`, `content_type`, `search_id`
  请求体：无
- `GET /api/u1/v1/douyin/web/fetch_home_feed`
  能力：主页/账号
  入参：query: `count`, `refresh_index`
  请求体：无
- `GET /api/u1/v1/douyin/web/fetch_hot_search_result`
  能力：搜索 / 热点/榜单
  入参：无
  请求体：无
- `GET /api/u1/v1/douyin/web/fetch_knowledge_aweme`
  能力：通用能力
  入参：query: `count*`, `refresh_index`, `cookie`
  请求体：无
- `GET /api/u1/v1/douyin/web/fetch_live_gift_ranking`
  能力：直播
  入参：query: `room_id*`, `rank_type`
  请求体：无
- `GET /api/u1/v1/douyin/web/fetch_live_im_fetch`
  能力：直播
  入参：query: `room_id*`, `user_unique_id*`
  请求体：无
- `GET /api/u1/v1/douyin/web/fetch_live_room_product_result`
  能力：电商 / 直播
  入参：query: `room_id*`, `author_id*`, `offset`, `limit`
  请求体：无
- `GET /api/u1/v1/douyin/web/fetch_live_search_result`
  能力：搜索 / 直播
  入参：query: `keyword*`, `offset`, `count`, `search_id`
  请求体：无
- `POST /api/u1/v1/douyin/web/fetch_multi_video`
  能力：作品详情
  入参：无
  请求体：application/json: 动态对象
- `POST /api/u1/v1/douyin/web/fetch_multi_video_high_quality_play_url`
  能力：作品详情
  入参：无
  请求体：application/json: `aweme_ids`:string
- `GET /api/u1/v1/douyin/web/fetch_music_aweme`
  能力：音乐/音频
  入参：query: `count*`, `refresh_index`, `cookie`
  请求体：无
- `GET /api/u1/v1/douyin/web/fetch_one_video`
  能力：作品详情
  入参：query: `aweme_id*`, `need_anchor_info`
  请求体：无
- `GET /api/u1/v1/douyin/web/fetch_one_video_by_share_url`
  能力：作品详情
  入参：query: `share_url*`
  请求体：无
- `GET /api/u1/v1/douyin/web/fetch_one_video_danmaku`
  能力：作品详情
  入参：query: `item_id*`, `duration*`, `end_time*`, `start_time*`
  请求体：无
- `GET /api/u1/v1/douyin/web/fetch_one_video_v2`
  能力：作品详情
  入参：query: `aweme_id*`
  请求体：无
- `GET /api/u1/v1/douyin/web/fetch_product_coupon`
  能力：电商
  入参：query: `product_id*`, `shop_id*`, `price*`, `author_id*`, `sec_user_id*`
  请求体：无
- `GET /api/u1/v1/douyin/web/fetch_product_detail`
  能力：详情 / 电商
  入参：query: `product_id*`, `aweme_id`, `room_id`, `sec_user_id`
  请求体：无
- `GET /api/u1/v1/douyin/web/fetch_product_review_list`
  能力：电商
  入参：query: `product_id*`, `shop_id*`, `cursor`, `count`, `sort_type`
  请求体：无
- `GET /api/u1/v1/douyin/web/fetch_product_review_score`
  能力：电商
  入参：query: `product_id*`, `shop_id*`
  请求体：无
- `GET /api/u1/v1/douyin/web/fetch_product_sku_list`
  能力：电商
  入参：query: `product_id*`, `author_id*`
  请求体：无
- `POST /api/u1/v1/douyin/web/fetch_query_user`
  能力：主页/账号
  入参：无
  请求体：application/json: 动态对象
- `GET /api/u1/v1/douyin/web/fetch_related_posts`
  能力：作品详情
  入参：query: `aweme_id*`, `refresh_index`, `count`
  请求体：无
- `POST /api/u1/v1/douyin/web/fetch_search_challenge`
  能力：搜索 / 话题
  入参：无
  请求体：application/json: `keyword`:string, `cursor`:integer, `count`:integer, `cookie`:string
- `GET /api/u1/v1/douyin/web/fetch_series_aweme`
  能力：通用能力
  入参：query: `offset*`, `count*`, `content_type*`, `cookie`
  请求体：无
- `POST /api/u1/v1/douyin/web/fetch_user_collection_videos`
  能力：主页/账号 / 作品详情
  入参：无
  请求体：application/json: `cookie*`:string, `max_cursor`:integer, `counts`:integer
- `POST /api/u1/v1/douyin/web/fetch_user_collects`
  能力：主页/账号
  入参：无
  请求体：application/json: `max_cursor`:integer, `counts`:integer, `cookie*`:string
- `GET /api/u1/v1/douyin/web/fetch_user_collects_videos`
  能力：主页/账号 / 作品详情
  入参：query: `collects_id*`, `max_cursor`, `counts`
  请求体：无
- `GET /api/u1/v1/douyin/web/fetch_user_fans_list`
  能力：主页/账号
  入参：query: `sec_user_id`, `max_time`, `count`, `source_type`
  请求体：无
- `GET /api/u1/v1/douyin/web/fetch_user_following_list`
  能力：主页/账号
  入参：query: `sec_user_id`, `max_time`, `count`, `source_type`
  请求体：无
- `POST /api/u1/v1/douyin/web/fetch_user_like_videos`
  能力：主页/账号 / 作品详情
  入参：无
  请求体：application/json: `sec_user_id*`:string, `max_cursor`:integer, `counts`:integer, `cookie`:string
- `GET /api/u1/v1/douyin/web/fetch_user_live_info_by_uid`
  能力：主页/账号 / 直播
  入参：query: `uid*`
  请求体：无
- `GET /api/u1/v1/douyin/web/fetch_user_live_videos`
  能力：主页/账号 / 作品详情 / 直播
  入参：query: `webcast_id*`
  请求体：无
- `GET /api/u1/v1/douyin/web/fetch_user_live_videos_by_room_id`
  能力：主页/账号 / 作品详情 / 直播
  入参：query: `room_id*`
  请求体：无
- `GET /api/u1/v1/douyin/web/fetch_user_live_videos_by_room_id_v2`
  能力：主页/账号 / 作品详情 / 直播
  入参：query: `room_id*`
  请求体：无
- `GET /api/u1/v1/douyin/web/fetch_user_live_videos_by_sec_uid`
  能力：主页/账号 / 作品详情 / 直播
  入参：query: `sec_uid*`
  请求体：无
- `GET /api/u1/v1/douyin/web/fetch_user_mix_videos`
  能力：主页/账号 / 作品详情
  入参：query: `mix_id*`, `max_cursor`, `counts`
  请求体：无
- `GET /api/u1/v1/douyin/web/fetch_user_post_videos`
  能力：主页/账号 / 作品详情
  入参：query: `sec_user_id*`, `max_cursor`, `count`, `filter_type`, `cookie`
  请求体：无
- `GET /api/u1/v1/douyin/web/fetch_user_profile_by_short_id`
  能力：主页/账号
  入参：query: `short_id*`
  请求体：无
- `GET /api/u1/v1/douyin/web/fetch_user_profile_by_uid`
  能力：主页/账号
  入参：query: `uid*`
  请求体：无
- `GET /api/u1/v1/douyin/web/fetch_user_search_result`
  能力：搜索 / 主页/账号
  入参：query: `keyword*`, `offset`, `count`, `douyin_user_fans`, `douyin_user_type`, `search_id`
  请求体：无
- `GET /api/u1/v1/douyin/web/fetch_user_search_result_v2`
  能力：搜索 / 主页/账号
  入参：query: `keyword*`, `cursor`
  请求体：无
- `GET /api/u1/v1/douyin/web/fetch_user_search_result_v3`
  能力：搜索 / 主页/账号
  入参：query: `keyword*`, `cursor`, `douyin_user_type`, `douyin_user_fans`
  请求体：无
- `GET /api/u1/v1/douyin/web/fetch_video_channel_result`
  能力：主页/账号 / 作品详情
  入参：query: `tag_id*`, `count`, `refresh_index`
  请求体：无
- `GET /api/u1/v1/douyin/web/fetch_video_comment_replies`
  能力：评论 / 作品详情
  入参：query: `item_id*`, `comment_id*`, `cursor`, `count`
  请求体：无
- `GET /api/u1/v1/douyin/web/fetch_video_comments`
  能力：评论 / 作品详情
  入参：query: `aweme_id*`, `cursor`, `count`
  请求体：无
- `GET /api/u1/v1/douyin/web/fetch_video_high_quality_play_url`
  能力：作品详情
  入参：query: `aweme_id`, `share_url`
  请求体：无
- `GET /api/u1/v1/douyin/web/fetch_video_search_result`
  能力：搜索 / 作品详情
  入参：query: `keyword*`, `offset`, `count`, `sort_type`, `publish_time`, `filter_duration`, `search_id`
  请求体：无
- `GET /api/u1/v1/douyin/web/fetch_video_search_result_v2`
  能力：搜索 / 作品详情
  入参：query: `keyword*`, `sort_type`, `publish_time`, `filter_duration`, `page`, `search_id`
  请求体：无
- `POST /api/u1/v1/douyin/web/generate_a_bogus`
  能力：通用能力
  入参：无
  请求体：application/json: `url*`:string, `data*`:string, `user_agent*`:string, `index_0`:integer, `index_1`:integer, `index_2`:integer
- `GET /api/u1/v1/douyin/web/generate_real_msToken`
  能力：通用能力
  入参：无
  请求体：无
- `GET /api/u1/v1/douyin/web/generate_s_v_web_id`
  能力：通用能力
  入参：无
  请求体：无
- `GET /api/u1/v1/douyin/web/generate_ttwid`
  能力：通用能力
  入参：query: `user_agent`
  请求体：无
- `GET /api/u1/v1/douyin/web/generate_verify_fp`
  能力：通用能力
  入参：无
  请求体：无
- `GET /api/u1/v1/douyin/web/generate_wss_xb_signature`
  能力：通用能力
  入参：query: `user_agent*`, `room_id*`, `user_unique_id*`
  请求体：无
- `POST /api/u1/v1/douyin/web/generate_x_bogus`
  能力：通用能力
  入参：无
  请求体：application/json: `url*`:string, `user_agent*`:string
- `POST /api/u1/v1/douyin/web/get_all_aweme_id`
  能力：通用能力
  入参：无
  请求体：application/json: 动态对象
- `POST /api/u1/v1/douyin/web/get_all_sec_user_id`
  能力：主页/账号
  入参：无
  请求体：application/json: 动态对象
- `POST /api/u1/v1/douyin/web/get_all_webcast_id`
  能力：通用能力
  入参：无
  请求体：application/json: 动态对象
- `GET /api/u1/v1/douyin/web/get_aweme_id`
  能力：通用能力
  入参：query: `url*`
  请求体：无
- `GET /api/u1/v1/douyin/web/get_sec_user_id`
  能力：主页/账号
  入参：query: `url*`
  请求体：无
- `GET /api/u1/v1/douyin/web/get_webcast_id`
  能力：通用能力
  入参：query: `url*`
  请求体：无
- `GET /api/u1/v1/douyin/web/handler_shorten_url`
  能力：通用能力
  入参：query: `target_url*`
  请求体：无
- `GET /api/u1/v1/douyin/web/handler_user_profile`
  能力：主页/账号
  入参：query: `sec_user_id*`
  请求体：无
- `GET /api/u1/v1/douyin/web/handler_user_profile_v2`
  能力：主页/账号
  入参：query: `unique_id*`
  请求体：无
- `GET /api/u1/v1/douyin/web/handler_user_profile_v3`
  能力：主页/账号
  入参：query: `uid*`
  请求体：无
- `GET /api/u1/v1/douyin/web/handler_user_profile_v4`
  能力：主页/账号
  入参：query: `sec_user_id*`
  请求体：无
- `GET /api/u1/v1/douyin/web/webcast_id_2_room_id`
  能力：通用能力
  入参：query: `webcast_id*`
  请求体：无

### `Douyin-Xingtu-API`

- 路由数：`22`
- 标签说明：**(抖音星图数据接口/Douyin-Xingtu-API data endpoints)**
- 常见入参：`kolId`, `platformChannel`, `_range`, `page`, `onlyAssign`, `keyword`, `uri`, `durationTS`, `format`, `sec_user_id`

- `GET /api/u1/v1/douyin/xingtu/author_content_hot_comment_keywords_v1`
  能力：评论 / 热点/榜单 / 创作者
  入参：query: `kolId*`
  请求体：无
- `GET /api/u1/v1/douyin/xingtu/author_hot_comment_tokens_v1`
  能力：评论 / 热点/榜单 / 创作者
  入参：query: `kolId*`
  请求体：无
- `GET /api/u1/v1/douyin/xingtu/get_sign_image`
  能力：通用能力
  入参：query: `uri*`, `durationTS`, `format`
  请求体：无
- `GET /api/u1/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`
  能力：主页/账号
  入参：query: `sec_user_id*`
  请求体：无
- `GET /api/u1/v1/douyin/xingtu/get_xingtu_kolid_by_uid`
  能力：通用能力
  入参：query: `uid*`
  请求体：无
- `GET /api/u1/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id`
  能力：通用能力
  入参：query: `unique_id*`
  请求体：无
- `GET /api/u1/v1/douyin/xingtu/kol_audience_portrait_v1`
  能力：通用能力
  入参：query: `kolId*`
  请求体：无
- `GET /api/u1/v1/douyin/xingtu/kol_base_info_v1`
  能力：通用能力
  入参：query: `kolId*`, `platformChannel*`
  请求体：无
- `GET /api/u1/v1/douyin/xingtu/kol_conversion_ability_analysis_v1`
  能力：通用能力
  入参：query: `kolId*`, `_range*`
  请求体：无
- `GET /api/u1/v1/douyin/xingtu/kol_convert_video_display_v1`
  能力：作品详情
  入参：query: `kolId*`, `detailType*`, `page*`
  请求体：无
- `GET /api/u1/v1/douyin/xingtu/kol_cp_info_v1`
  能力：通用能力
  入参：query: `kolId*`
  请求体：无
- `GET /api/u1/v1/douyin/xingtu/kol_daily_fans_v1`
  能力：通用能力
  入参：query: `kolId*`, `startDate*`, `endDate*`
  请求体：无
- `GET /api/u1/v1/douyin/xingtu/kol_data_overview_v1`
  能力：通用能力
  入参：query: `kolId*`, `_type*`, `_range*`, `flowType*`, `onlyAssign`
  请求体：无
- `GET /api/u1/v1/douyin/xingtu/kol_fans_portrait_v1`
  能力：通用能力
  入参：query: `kolId*`, `fansType`
  请求体：无
- `GET /api/u1/v1/douyin/xingtu/kol_link_struct_v1`
  能力：通用能力
  入参：query: `kolId*`
  请求体：无
- `GET /api/u1/v1/douyin/xingtu/kol_rec_videos_v1`
  能力：作品详情
  入参：query: `kolId*`
  请求体：无
- `GET /api/u1/v1/douyin/xingtu/kol_service_price_v1`
  能力：通用能力
  入参：query: `kolId*`, `platformChannel*`
  请求体：无
- `GET /api/u1/v1/douyin/xingtu/kol_touch_distribution_v1`
  能力：通用能力
  入参：query: `kolId*`
  请求体：无
- `GET /api/u1/v1/douyin/xingtu/kol_video_performance_v1`
  能力：作品详情
  入参：query: `kolId*`, `onlyAssign*`
  请求体：无
- `GET /api/u1/v1/douyin/xingtu/kol_xingtu_index_v1`
  能力：通用能力
  入参：query: `kolId*`
  请求体：无
- `GET /api/u1/v1/douyin/xingtu/search_kol_v1`
  能力：搜索
  入参：query: `keyword*`, `platformSource*`, `page*`
  请求体：无
- `GET /api/u1/v1/douyin/xingtu/search_kol_v2`
  能力：搜索
  入参：query: `keyword*`, `followerRange`, `contentTag`
  请求体：无

### `Douyin-Xingtu-V2-API`

- 路由数：`21`
- 标签说明：**(抖音星图V2数据接口/Douyin-Xingtu-V2-API data endpoints)**
- 常见入参：`o_author_id`, `platform_source`, `limit`, `platform_channel`, `author_id`, `only_assign`, `flow_type`, `page`, `qualifier`, `period`

- `GET /api/u1/v1/douyin/xingtu_v2/get_author_base_info`
  能力：创作者
  入参：query: `o_author_id*`, `platform_source`, `platform_channel`, `recommend`, `need_sec_uid`, `need_linkage_info`
  请求体：无
- `GET /api/u1/v1/douyin/xingtu_v2/get_author_business_card_info`
  能力：创作者
  入参：query: `o_author_id*`
  请求体：无
- `GET /api/u1/v1/douyin/xingtu_v2/get_author_content_hot_keywords`
  能力：热点/榜单 / 创作者
  入参：query: `author_id*`, `keyword_type`
  请求体：无
- `GET /api/u1/v1/douyin/xingtu_v2/get_author_hot_comment_tokens`
  能力：评论 / 热点/榜单 / 创作者
  入参：query: `author_id*`, `num`, `without_emoji`
  请求体：无
- `GET /api/u1/v1/douyin/xingtu_v2/get_author_local_info`
  能力：创作者
  入参：query: `o_author_id*`, `platform_source`, `platform_channel`, `time_range`
  请求体：无
- `GET /api/u1/v1/douyin/xingtu_v2/get_author_market_fields`
  能力：创作者
  入参：query: `market_scene`
  请求体：无
- `GET /api/u1/v1/douyin/xingtu_v2/get_author_show_items`
  能力：创作者
  入参：query: `o_author_id*`, `platform_source`, `platform_channel`, `limit`, `only_assign`, `flow_type`
  请求体：无
- `GET /api/u1/v1/douyin/xingtu_v2/get_author_spread_info`
  能力：创作者 / 广告
  入参：query: `o_author_id*`, `platform_source`, `platform_channel`, `type`, `flow_type`, `only_assign`, `range`
  请求体：无
- `GET /api/u1/v1/douyin/xingtu_v2/get_content_trend_guide`
  能力：热点/榜单
  入参：无
  请求体：无
- `GET /api/u1/v1/douyin/xingtu_v2/get_demander_mcn_list`
  能力：通用能力
  入参：query: `mcn_name`, `page`, `limit`, `order_by`
  请求体：无
- `GET /api/u1/v1/douyin/xingtu_v2/get_excellent_case_category_list`
  能力：通用能力
  入参：query: `platform_source`
  请求体：无
- `GET /api/u1/v1/douyin/xingtu_v2/get_ip_activity_detail`
  能力：详情
  入参：query: `id*`
  请求体：无
- `GET /api/u1/v1/douyin/xingtu_v2/get_ip_activity_industry_list`
  能力：通用能力
  入参：无
  请求体：无
- `POST /api/u1/v1/douyin/xingtu_v2/get_ip_activity_list`
  能力：通用能力
  入参：无
  请求体：application/json: `query_start_time*`:string, `query_end_time*`:string, `industry_id_list`[], `category_list`[], `status_list`[]
- `POST /api/u1/v1/douyin/xingtu_v2/get_playlet_actor_rank_catalog`
  能力：通用能力
  入参：无
  请求体：无
- `GET /api/u1/v1/douyin/xingtu_v2/get_playlet_actor_rank_list`
  能力：通用能力
  入参：query: `category`, `name`, `qualifier`, `period`, `date`, `limit`
  请求体：无
- `GET /api/u1/v1/douyin/xingtu_v2/get_ranking_list_catalog`
  能力：通用能力
  入参：query: `codes`, `biz_scene`
  请求体：无
- `GET /api/u1/v1/douyin/xingtu_v2/get_ranking_list_data`
  能力：通用能力
  入参：query: `code`, `qualifier`, `version`, `period`, `date`, `limit`
  请求体：无
- `POST /api/u1/v1/douyin/xingtu_v2/get_recommend_for_star_authors`
  能力：创作者
  入参：无
  请求体：application/json: `author_ids*`[], `similar_type`:string, `page`:integer, `limit`:integer
- `GET /api/u1/v1/douyin/xingtu_v2/get_resource_list`
  能力：通用能力
  入参：query: `resource_id*`
  请求体：无
- `GET /api/u1/v1/douyin/xingtu_v2/get_user_profile_qrcode`
  能力：主页/账号
  入参：query: `core_user_id`, `sec_uid`
  请求体：无

### `Health-Check`

- 路由数：`1`
- 标签说明：**(服务器健康检查/Server Health Check)**
- 常见入参：无

- `GET /api/u1/v1/health/check`
  能力：通用能力
  入参：无
  请求体：无

### `Hybrid-Parsing`

- 路由数：`1`
- 标签说明：**(混合解析单个视频接口/Hybrid-Parsing endpoints)**
- 常见入参：`url`, `minimal`, `base64_url`

- `GET /api/u1/v1/hybrid/video_data`
  能力：作品详情
  入参：query: `url*`, `minimal`, `base64_url`
  请求体：无

### `Instagram-V1-API`

- 路由数：`29`
- 标签说明：**(Instagram V1数据接口（优先使用V1接口，V2接口仅在V1接口无法满足需求时使用）/Instagram-V1-API endpoints (Prefer using V1 endpoints, V2 endpoints are only for use when V1 endpoints cannot meet the requirements))**
- 常见入参：`user_id`, `max_id`, `count`, `end_cursor`, `media_id`, `username`, `page`, `min_id`, `location_id`, `post_url`

- `GET /api/u1/v1/instagram/v1/fetch_cities`
  能力：通用能力
  入参：query: `country_code*`, `page`
  请求体：无
- `GET /api/u1/v1/instagram/v1/fetch_comment_replies`
  能力：评论
  入参：query: `media_id*`, `comment_id*`, `min_id`
  请求体：无
- `GET /api/u1/v1/instagram/v1/fetch_explore_sections`
  能力：通用能力
  入参：无
  请求体：无
- `GET /api/u1/v1/instagram/v1/fetch_hashtag_posts`
  能力：作品详情 / 话题
  入参：query: `hashtag*`, `end_cursor`
  请求体：无
- `GET /api/u1/v1/instagram/v1/fetch_location_info`
  能力：通用能力
  入参：query: `location_id*`
  请求体：无
- `GET /api/u1/v1/instagram/v1/fetch_location_posts`
  能力：作品详情
  入参：query: `location_id*`, `tab`, `end_cursor`
  请求体：无
- `GET /api/u1/v1/instagram/v1/fetch_locations`
  能力：通用能力
  入参：query: `city_id*`, `page`
  请求体：无
- `GET /api/u1/v1/instagram/v1/fetch_music_posts`
  能力：作品详情 / 音乐/音频
  入参：query: `music_id`, `music_url`, `max_id`
  请求体：无
- `GET /api/u1/v1/instagram/v1/fetch_post_by_id`
  能力：作品详情
  入参：query: `post_id*`
  请求体：无
- `GET /api/u1/v1/instagram/v1/fetch_post_by_url`
  能力：作品详情
  入参：query: `post_url*`
  请求体：无
- `GET /api/u1/v1/instagram/v1/fetch_post_by_url_v2`
  能力：作品详情
  入参：query: `post_url*`
  请求体：无
- `GET /api/u1/v1/instagram/v1/fetch_post_comments_v2`
  能力：评论 / 作品详情
  入参：query: `media_id*`, `sort_order`, `min_id`
  请求体：无
- `GET /api/u1/v1/instagram/v1/fetch_related_profiles`
  能力：主页/账号
  入参：query: `user_id*`
  请求体：无
- `GET /api/u1/v1/instagram/v1/fetch_search`
  能力：搜索
  入参：query: `query*`, `select`
  请求体：无
- `GET /api/u1/v1/instagram/v1/fetch_section_posts`
  能力：作品详情
  入参：query: `section_id*`, `count`, `max_id`
  请求体：无
- `GET /api/u1/v1/instagram/v1/fetch_user_about_info`
  能力：主页/账号
  入参：query: `user_id*`
  请求体：无
- `GET /api/u1/v1/instagram/v1/fetch_user_info_by_id`
  能力：主页/账号
  入参：query: `user_id*`
  请求体：无
- `GET /api/u1/v1/instagram/v1/fetch_user_info_by_id_v2`
  能力：主页/账号
  入参：query: `user_id*`
  请求体：无
- `GET /api/u1/v1/instagram/v1/fetch_user_info_by_username`
  能力：主页/账号
  入参：query: `username*`
  请求体：无
- `GET /api/u1/v1/instagram/v1/fetch_user_info_by_username_v2`
  能力：主页/账号
  入参：query: `username*`
  请求体：无
- `GET /api/u1/v1/instagram/v1/fetch_user_info_by_username_v3`
  能力：主页/账号
  入参：query: `username*`
  请求体：无
- `GET /api/u1/v1/instagram/v1/fetch_user_posts`
  能力：主页/账号 / 作品详情
  入参：query: `user_id*`, `count`, `max_id`
  请求体：无
- `GET /api/u1/v1/instagram/v1/fetch_user_posts_v2`
  能力：主页/账号 / 作品详情
  入参：query: `user_id*`, `count`, `end_cursor`
  请求体：无
- `GET /api/u1/v1/instagram/v1/fetch_user_reels`
  能力：主页/账号
  入参：query: `user_id*`, `count`, `max_id`
  请求体：无
- `GET /api/u1/v1/instagram/v1/fetch_user_reposts`
  能力：主页/账号 / 作品详情
  入参：query: `user_id*`, `max_id`
  请求体：无
- `GET /api/u1/v1/instagram/v1/fetch_user_tagged_posts`
  能力：主页/账号 / 作品详情
  入参：query: `user_id*`, `count`, `end_cursor`
  请求体：无
- `GET /api/u1/v1/instagram/v1/media_id_to_shortcode`
  能力：下载/媒体
  入参：query: `media_id*`
  请求体：无
- `GET /api/u1/v1/instagram/v1/shortcode_to_media_id`
  能力：下载/媒体
  入参：query: `shortcode*`
  请求体：无
- `GET /api/u1/v1/instagram/v1/user_id_to_username`
  能力：主页/账号
  入参：query: `user_id*`
  请求体：无

### `Instagram-V2-API`

- 路由数：`27`
- 标签说明：**(Instagram V2数据接口（若V1接口的功能无法满足需求时使用，稳定性不如V1接口）/Instagram-V2-API endpoints (Use when V1 endpoints cannot meet the requirements, stability is not as good as V1 endpoints))**
- 常见入参：`pagination_token`, `user_id`, `username`, `keyword`, `code_or_url`, `comment_id`, `feed_type`, `highlight_id`, `location_id`, `audio_canonical_id`

- `GET /api/u1/v1/instagram/v2/fetch_comment_replies`
  能力：评论
  入参：query: `code_or_url*`, `comment_id*`, `pagination_token`
  请求体：无
- `GET /api/u1/v1/instagram/v2/fetch_hashtag_posts`
  能力：作品详情 / 话题
  入参：query: `keyword*`, `feed_type`, `pagination_token`
  请求体：无
- `GET /api/u1/v1/instagram/v2/fetch_highlight_stories`
  能力：通用能力
  入参：query: `highlight_id*`
  请求体：无
- `GET /api/u1/v1/instagram/v2/fetch_location_posts`
  能力：作品详情
  入参：query: `location_id*`, `pagination_token`
  请求体：无
- `GET /api/u1/v1/instagram/v2/fetch_music_posts`
  能力：作品详情 / 音乐/音频
  入参：query: `audio_canonical_id*`, `pagination_token`
  请求体：无
- `GET /api/u1/v1/instagram/v2/fetch_post_comments`
  能力：评论 / 作品详情
  入参：query: `code_or_url*`, `sort_by`, `pagination_token`
  请求体：无
- `GET /api/u1/v1/instagram/v2/fetch_post_info`
  能力：作品详情
  入参：query: `code_or_url*`
  请求体：无
- `GET /api/u1/v1/instagram/v2/fetch_post_likes`
  能力：作品详情
  入参：query: `code_or_url*`, `end_cursor`
  请求体：无
- `GET /api/u1/v1/instagram/v2/fetch_similar_users`
  能力：主页/账号
  入参：query: `username`, `user_id`
  请求体：无
- `GET /api/u1/v1/instagram/v2/fetch_user_followers`
  能力：主页/账号
  入参：query: `username`, `user_id`, `pagination_token`
  请求体：无
- `GET /api/u1/v1/instagram/v2/fetch_user_following`
  能力：主页/账号
  入参：query: `username`, `user_id`, `pagination_token`
  请求体：无
- `GET /api/u1/v1/instagram/v2/fetch_user_highlights`
  能力：主页/账号
  入参：query: `username`, `user_id`
  请求体：无
- `GET /api/u1/v1/instagram/v2/fetch_user_info`
  能力：主页/账号
  入参：query: `username`, `user_id`
  请求体：无
- `GET /api/u1/v1/instagram/v2/fetch_user_posts`
  能力：主页/账号 / 作品详情
  入参：query: `username`, `user_id`, `pagination_token`
  请求体：无
- `GET /api/u1/v1/instagram/v2/fetch_user_reels`
  能力：主页/账号
  入参：query: `username`, `user_id`, `pagination_token`
  请求体：无
- `GET /api/u1/v1/instagram/v2/fetch_user_stories`
  能力：主页/账号
  入参：query: `username`, `user_id`
  请求体：无
- `GET /api/u1/v1/instagram/v2/fetch_user_tagged_posts`
  能力：主页/账号 / 作品详情
  入参：query: `username`, `user_id`, `pagination_token`
  请求体：无
- `GET /api/u1/v1/instagram/v2/general_search`
  能力：搜索
  入参：query: `keyword*`, `pagination_token`
  请求体：无
- `GET /api/u1/v1/instagram/v2/media_id_to_shortcode`
  能力：下载/媒体
  入参：query: `media_id*`
  请求体：无
- `GET /api/u1/v1/instagram/v2/search_by_coordinates`
  能力：搜索
  入参：query: `latitude*`, `longitude*`
  请求体：无
- `GET /api/u1/v1/instagram/v2/search_hashtags`
  能力：搜索 / 话题
  入参：query: `keyword*`
  请求体：无
- `GET /api/u1/v1/instagram/v2/search_locations`
  能力：搜索
  入参：query: `keyword*`
  请求体：无
- `GET /api/u1/v1/instagram/v2/search_music`
  能力：搜索 / 音乐/音频
  入参：query: `keyword*`
  请求体：无
- `GET /api/u1/v1/instagram/v2/search_reels`
  能力：搜索
  入参：query: `keyword*`, `pagination_token`
  请求体：无
- `GET /api/u1/v1/instagram/v2/search_users`
  能力：搜索 / 主页/账号
  入参：query: `keyword*`
  请求体：无
- `GET /api/u1/v1/instagram/v2/shortcode_to_media_id`
  能力：下载/媒体
  入参：query: `shortcode*`
  请求体：无
- `GET /api/u1/v1/instagram/v2/user_id_to_username`
  能力：主页/账号
  入参：query: `user_id*`
  请求体：无

### `Instagram-V3-API`

- 路由数：`26`
- 标签说明：**(Instagram V3数据接口/Instagram-V3-API endpoints)**
- 常见入参：`user_id`, `username`, `url`, `first`, `after`, `query`, `media_id`, `code`, `max_id`, `comment_id`

- `GET /api/u1/v1/instagram/v3/bulk_translate_comments`
  能力：评论
  入参：query: `comment_ids*`
  请求体：无
- `GET /api/u1/v1/instagram/v3/general_search`
  能力：搜索
  入参：query: `query*`, `next_max_id`, `rank_token`, `enable_metadata`
  请求体：无
- `GET /api/u1/v1/instagram/v3/get_comment_replies`
  能力：评论
  入参：query: `media_id`, `code`, `url`, `comment_id*`, `min_id`
  请求体：无
- `GET /api/u1/v1/instagram/v3/get_explore`
  能力：通用能力
  入参：query: `max_id`
  请求体：无
- `GET /api/u1/v1/instagram/v3/get_highlight_stories`
  能力：通用能力
  入参：query: `highlight_id*`, `reel_ids`
  请求体：无
- `GET /api/u1/v1/instagram/v3/get_location_info`
  能力：通用能力
  入参：query: `location_id*`, `show_nearby`
  请求体：无
- `GET /api/u1/v1/instagram/v3/get_location_posts`
  能力：作品详情
  入参：query: `location_id*`, `tab`, `page_size_override`
  请求体：无
- `GET /api/u1/v1/instagram/v3/get_post_comments`
  能力：评论 / 作品详情
  入参：query: `media_id`, `code`, `url`, `min_id`, `sort_order`
  请求体：无
- `GET /api/u1/v1/instagram/v3/get_post_info`
  能力：作品详情
  入参：query: `media_id`, `url`
  请求体：无
- `GET /api/u1/v1/instagram/v3/get_post_info_by_code`
  能力：作品详情
  入参：query: `code`, `url`
  请求体：无
- `GET /api/u1/v1/instagram/v3/get_post_oembed`
  能力：作品详情
  入参：query: `url*`, `hidecaption`, `maxwidth`
  请求体：无
- `GET /api/u1/v1/instagram/v3/get_recommended_reels`
  能力：通用能力
  入参：query: `first`, `after`
  请求体：无
- `GET /api/u1/v1/instagram/v3/get_user_about`
  能力：主页/账号
  入参：query: `user_id`, `username`
  请求体：无
- `GET /api/u1/v1/instagram/v3/get_user_brief`
  能力：主页/账号
  入参：query: `user_id*`, `username*`
  请求体：无
- `GET /api/u1/v1/instagram/v3/get_user_followers`
  能力：主页/账号
  入参：query: `user_id`, `username`, `count`, `max_id`
  请求体：无
- `GET /api/u1/v1/instagram/v3/get_user_following`
  能力：主页/账号
  入参：query: `user_id`, `username`, `count`, `max_id`
  请求体：无
- `GET /api/u1/v1/instagram/v3/get_user_highlights`
  能力：主页/账号
  入参：query: `user_id`, `username`, `first`, `after`
  请求体：无
- `GET /api/u1/v1/instagram/v3/get_user_posts`
  能力：主页/账号 / 作品详情
  入参：query: `username`, `user_id`, `first`, `after`
  请求体：无
- `GET /api/u1/v1/instagram/v3/get_user_profile`
  能力：主页/账号
  入参：query: `user_id`, `username`
  请求体：无
- `GET /api/u1/v1/instagram/v3/get_user_reels`
  能力：主页/账号
  入参：query: `user_id`, `username`, `first`, `after`
  请求体：无
- `GET /api/u1/v1/instagram/v3/get_user_stories`
  能力：主页/账号
  入参：query: `user_id`, `username`, `reel_ids`
  请求体：无
- `GET /api/u1/v1/instagram/v3/get_user_tagged_posts`
  能力：主页/账号 / 作品详情
  入参：query: `user_id`, `username`, `first`, `after`
  请求体：无
- `GET /api/u1/v1/instagram/v3/search_hashtags`
  能力：搜索 / 话题
  入参：query: `query*`
  请求体：无
- `GET /api/u1/v1/instagram/v3/search_places`
  能力：搜索
  入参：query: `query*`
  请求体：无
- `GET /api/u1/v1/instagram/v3/search_users`
  能力：搜索 / 主页/账号
  入参：query: `query*`
  请求体：无
- `GET /api/u1/v1/instagram/v3/translate_comment`
  能力：评论
  入参：query: `comment_id*`
  请求体：无

### `Kuaishou-App-API`

- 路由数：`20`
- 标签说明：**(快手App数据接口/Kuaishou-App-API data endpoints)**
- 常见入参：`pcursor`, `user_id`, `subTabId`, `subTabName`, `keyword`, `magic_face_id`, `photo_id`, `page`, `boardType`, `boardId`

- `GET /api/u1/v1/kuaishou/app/fetch_brand_top_list`
  能力：通用能力
  入参：query: `subTabId`, `subTabName`
  请求体：无
- `GET /api/u1/v1/kuaishou/app/fetch_hot_board_categories`
  能力：热点/榜单
  入参：无
  请求体：无
- `GET /api/u1/v1/kuaishou/app/fetch_hot_board_detail`
  能力：热点/榜单 / 详情
  入参：query: `boardType`, `boardId`
  请求体：无
- `GET /api/u1/v1/kuaishou/app/fetch_hot_search_person`
  能力：搜索 / 热点/榜单
  入参：无
  请求体：无
- `GET /api/u1/v1/kuaishou/app/fetch_live_top_list`
  能力：直播
  入参：query: `subTabId`, `subTabName`
  请求体：无
- `GET /api/u1/v1/kuaishou/app/fetch_magic_face_hot`
  能力：热点/榜单
  入参：query: `magic_face_id*`, `pcursor`, `count`
  请求体：无
- `GET /api/u1/v1/kuaishou/app/fetch_magic_face_usage`
  能力：通用能力
  入参：query: `magic_face_id*`
  请求体：无
- `GET /api/u1/v1/kuaishou/app/fetch_one_user_v2`
  能力：主页/账号
  入参：query: `user_id*`
  请求体：无
- `GET /api/u1/v1/kuaishou/app/fetch_one_video`
  能力：作品详情
  入参：query: `photo_id*`
  请求体：无
- `GET /api/u1/v1/kuaishou/app/fetch_one_video_by_url`
  能力：作品详情
  入参：query: `share_text*`
  请求体：无
- `GET /api/u1/v1/kuaishou/app/fetch_one_video_comment`
  能力：评论 / 作品详情
  入参：query: `photo_id*`, `pcursor`
  请求体：无
- `GET /api/u1/v1/kuaishou/app/fetch_shopping_top_list`
  能力：电商
  入参：query: `subTabId`, `subTabName`
  请求体：无
- `GET /api/u1/v1/kuaishou/app/fetch_user_hot_post`
  能力：热点/榜单 / 主页/账号 / 作品详情
  入参：query: `user_id*`, `pcursor`
  请求体：无
- `GET /api/u1/v1/kuaishou/app/fetch_user_live_info`
  能力：主页/账号 / 直播
  入参：query: `user_id*`
  请求体：无
- `GET /api/u1/v1/kuaishou/app/fetch_user_post_v2`
  能力：主页/账号 / 作品详情
  入参：query: `user_id*`, `pcursor`
  请求体：无
- `GET /api/u1/v1/kuaishou/app/fetch_videos_batch`
  能力：作品详情
  入参：query: `photo_ids*`
  请求体：无
- `GET /api/u1/v1/kuaishou/app/generate_kuaishou_share_link`
  能力：通用能力
  入参：query: `shareObjectId*`
  请求体：无
- `GET /api/u1/v1/kuaishou/app/search_comprehensive`
  能力：搜索
  入参：query: `keyword*`, `pcursor`, `sort_type`, `publish_time`, `duration`, `search_scope`
  请求体：无
- `GET /api/u1/v1/kuaishou/app/search_user_v2`
  能力：搜索 / 主页/账号
  入参：query: `keyword*`, `page`
  请求体：无
- `GET /api/u1/v1/kuaishou/app/search_video_v2`
  能力：搜索 / 作品详情
  入参：query: `keyword*`, `page`
  请求体：无

### `Kuaishou-Web-API`

- 路由数：`13`
- 标签说明：**(快手Web数据接口/Kuaishou-Web-API data endpoints)**
- 常见入参：`pcursor`, `photo_id`, `user_id`, `share_link`, `board_type`, `share_text`, `url`, `root_comment_id`

- `GET /api/u1/v1/kuaishou/web/fetch_get_user_id`
  能力：主页/账号
  入参：query: `share_link*`
  请求体：无
- `GET /api/u1/v1/kuaishou/web/fetch_kuaishou_hot_list_v1`
  能力：热点/榜单
  入参：无
  请求体：无
- `GET /api/u1/v1/kuaishou/web/fetch_kuaishou_hot_list_v2`
  能力：热点/榜单
  入参：query: `board_type`
  请求体：无
- `GET /api/u1/v1/kuaishou/web/fetch_one_video`
  能力：作品详情
  入参：query: `share_text*`
  请求体：无
- `GET /api/u1/v1/kuaishou/web/fetch_one_video_by_url`
  能力：作品详情
  入参：query: `url*`
  请求体：无
- `GET /api/u1/v1/kuaishou/web/fetch_one_video_comment`
  能力：评论 / 作品详情
  入参：query: `photo_id*`, `pcursor`
  请求体：无
- `GET /api/u1/v1/kuaishou/web/fetch_one_video_sub_comment`
  能力：评论 / 作品详情
  入参：query: `photo_id*`, `pcursor`, `root_comment_id*`
  请求体：无
- `GET /api/u1/v1/kuaishou/web/fetch_one_video_v2`
  能力：作品详情
  入参：query: `photo_id*`
  请求体：无
- `GET /api/u1/v1/kuaishou/web/fetch_user_collect`
  能力：主页/账号
  入参：query: `user_id*`, `pcursor`
  请求体：无
- `GET /api/u1/v1/kuaishou/web/fetch_user_info`
  能力：主页/账号
  入参：query: `user_id*`
  请求体：无
- `GET /api/u1/v1/kuaishou/web/fetch_user_live_replay`
  能力：主页/账号 / 直播
  入参：query: `user_id*`, `pcursor`
  请求体：无
- `GET /api/u1/v1/kuaishou/web/fetch_user_post`
  能力：主页/账号 / 作品详情
  入参：query: `user_id*`, `pcursor`
  请求体：无
- `GET /api/u1/v1/kuaishou/web/generate_share_short_url`
  能力：通用能力
  入参：query: `photo_id*`
  请求体：无

### `Lemon8-App-API`

- 路由数：`16`
- 标签说明：**(Lemon8 APP数据接口/Lemon8-APP-API data endpoints)**
- 常见入参：`user_id`, `item_id`, `cursor`, `share_text`, `group_id`, `media_id`, `offset`, `query`, `max_cursor`, `filter_type`

- `GET /api/u1/v1/lemon8/app/fetch_discover_banners`
  能力：通用能力
  入参：无
  请求体：无
- `GET /api/u1/v1/lemon8/app/fetch_discover_tab`
  能力：通用能力
  入参：无
  请求体：无
- `GET /api/u1/v1/lemon8/app/fetch_discover_tab_information_tabs`
  能力：通用能力
  入参：无
  请求体：无
- `GET /api/u1/v1/lemon8/app/fetch_hot_search_keywords`
  能力：搜索 / 热点/榜单
  入参：无
  请求体：无
- `GET /api/u1/v1/lemon8/app/fetch_post_comment_list`
  能力：评论 / 作品详情
  入参：query: `group_id*`, `item_id*`, `media_id*`, `offset`
  请求体：无
- `GET /api/u1/v1/lemon8/app/fetch_post_detail`
  能力：作品详情 / 详情
  入参：query: `item_id*`
  请求体：无
- `GET /api/u1/v1/lemon8/app/fetch_search`
  能力：搜索
  入参：query: `query*`, `max_cursor`, `filter_type`, `order_by`, `search_tab`
  请求体：无
- `GET /api/u1/v1/lemon8/app/fetch_topic_info`
  能力：话题
  入参：query: `forum_id*`
  请求体：无
- `GET /api/u1/v1/lemon8/app/fetch_topic_post_list`
  能力：作品详情 / 话题
  入参：query: `category*`, `max_behot_time`, `category_parameter*`, `hashtag_name*`, `sort_type`
  请求体：无
- `GET /api/u1/v1/lemon8/app/fetch_user_follower_list`
  能力：主页/账号
  入参：query: `user_id*`, `cursor`
  请求体：无
- `GET /api/u1/v1/lemon8/app/fetch_user_following_list`
  能力：主页/账号
  入参：query: `user_id*`, `cursor`
  请求体：无
- `GET /api/u1/v1/lemon8/app/fetch_user_profile`
  能力：主页/账号
  入参：query: `user_id*`
  请求体：无
- `GET /api/u1/v1/lemon8/app/get_item_id`
  能力：通用能力
  入参：query: `share_text*`
  请求体：无
- `POST /api/u1/v1/lemon8/app/get_item_ids`
  能力：通用能力
  入参：无
  请求体：application/json: 动态对象
- `GET /api/u1/v1/lemon8/app/get_user_id`
  能力：主页/账号
  入参：query: `share_text*`
  请求体：无
- `POST /api/u1/v1/lemon8/app/get_user_ids`
  能力：主页/账号
  入参：无
  请求体：application/json: 动态对象

### `LinkedIn-Web-API`

- 路由数：`25`
- 标签说明：**(LinkedIn Web数据接口/LinkedIn-Web-API endpoints)**
- 常见入参：`page`, `urn`, `company_id`, `pagination_token`, `sort_by`, `company`, `username`, `date_posted`, `experience_level`, `remote`

- `GET /api/u1/v1/linkedin/web/get_company_job_count`
  能力：通用能力
  入参：query: `company_id*`
  请求体：无
- `GET /api/u1/v1/linkedin/web/get_company_jobs`
  能力：通用能力
  入参：query: `company_id*`, `page`, `sort_by`, `date_posted`, `experience_level`, `remote`, `job_type`, `easy_apply`, `under_10_applicants`, `fair_chance_employer`
  请求体：无
- `GET /api/u1/v1/linkedin/web/get_company_people`
  能力：通用能力
  入参：query: `company_id*`, `page`
  请求体：无
- `GET /api/u1/v1/linkedin/web/get_company_posts`
  能力：作品详情
  入参：query: `company_id*`, `page`, `sort_by`
  请求体：无
- `GET /api/u1/v1/linkedin/web/get_company_profile`
  能力：主页/账号
  入参：query: `company`, `company_id`
  请求体：无
- `GET /api/u1/v1/linkedin/web/get_job_detail`
  能力：详情
  入参：query: `job_id*`, `include_skills`
  请求体：无
- `GET /api/u1/v1/linkedin/web/get_user_about`
  能力：主页/账号
  入参：query: `urn*`
  请求体：无
- `GET /api/u1/v1/linkedin/web/get_user_certifications`
  能力：主页/账号
  入参：query: `urn*`, `page`
  请求体：无
- `GET /api/u1/v1/linkedin/web/get_user_comments`
  能力：评论 / 主页/账号
  入参：query: `urn*`, `page`, `pagination_token`
  请求体：无
- `GET /api/u1/v1/linkedin/web/get_user_contact`
  能力：主页/账号
  入参：query: `username*`
  请求体：无
- `GET /api/u1/v1/linkedin/web/get_user_educations`
  能力：主页/账号
  入参：query: `urn*`, `page`
  请求体：无
- `GET /api/u1/v1/linkedin/web/get_user_experience`
  能力：主页/账号
  入参：query: `urn*`, `page`
  请求体：无
- `GET /api/u1/v1/linkedin/web/get_user_follower_and_connection`
  能力：主页/账号
  入参：query: `username*`
  请求体：无
- `GET /api/u1/v1/linkedin/web/get_user_honors`
  能力：主页/账号
  入参：query: `urn*`, `page`
  请求体：无
- `GET /api/u1/v1/linkedin/web/get_user_images`
  能力：主页/账号
  入参：query: `urn*`, `page`, `pagination_token`
  请求体：无
- `GET /api/u1/v1/linkedin/web/get_user_interests_companies`
  能力：主页/账号
  入参：query: `urn*`, `page`
  请求体：无
- `GET /api/u1/v1/linkedin/web/get_user_interests_groups`
  能力：主页/账号
  入参：query: `urn*`, `page`
  请求体：无
- `GET /api/u1/v1/linkedin/web/get_user_posts`
  能力：主页/账号 / 作品详情
  入参：query: `urn*`, `page`, `pagination_token`
  请求体：无
- `GET /api/u1/v1/linkedin/web/get_user_profile`
  能力：主页/账号
  入参：query: `username*`, `include_follower_and_connection`, `include_experiences`, `include_skills`, `include_certifications`, `include_publications`, `include_educations`, `include_volunteers`, `include_honors`, `include_interests`, `include_bio`
  请求体：无
- `GET /api/u1/v1/linkedin/web/get_user_publications`
  能力：主页/账号
  入参：query: `urn*`, `page`
  请求体：无
- `GET /api/u1/v1/linkedin/web/get_user_recommendations`
  能力：主页/账号
  入参：query: `urn*`, `page`, `type`, `pagination_token`
  请求体：无
- `GET /api/u1/v1/linkedin/web/get_user_skills`
  能力：主页/账号
  入参：query: `urn*`, `page`
  请求体：无
- `GET /api/u1/v1/linkedin/web/get_user_videos`
  能力：主页/账号 / 作品详情
  入参：query: `urn*`, `page`, `pagination_token`
  请求体：无
- `GET /api/u1/v1/linkedin/web/search_jobs`
  能力：搜索
  入参：query: `keyword*`, `page`, `sort_by`, `date_posted`, `geocode`, `company`, `experience_level`, `remote`, `job_type`, `easy_apply`, `has_verifications`, `under_10_applicants`, `fair_chance_employer`
  请求体：无
- `GET /api/u1/v1/linkedin/web/search_people`
  能力：搜索
  入参：query: `name`, `first_name`, `last_name`, `title`, `company`, `school`, `page`, `geocode_location`, `current_company`, `profile_language`, `industry`, `service_category`
  请求体：无

### `Media-Ingest-API`

- 路由数：`2`
- 标签说明：**(媒体中转接口 / media ingest endpoints)**
- 常见入参：`file_name`, `content_type`, `size_bytes`, `upload_id`

- `POST /api/u3/v1/uploads`
  能力：广告
  入参：无
  请求体：application/json: `file_name*`:string, `content_type*`:string, `size_bytes*`:integer
- `POST /api/u3/v1/uploads/{upload_id}/complete`
  能力：广告
  入参：path: `upload_id*`
  请求体：application/json: 动态对象

### `PiPiXia-App-API`

- 路由数：`17`
- 标签说明：**(皮皮虾App数据接口/PiPiXia-App-API data endpoints)**
- 常见入参：`cursor`, `cell_id`, `user_id`, `cell_type`, `hashtag_id`, `feed_count`, `offset`, `hashtag_request_type`, `hashtag_sort_type`, `page`

- `GET /api/u1/v1/pipixia/app/fetch_hashtag_detail`
  能力：详情 / 话题
  入参：query: `hashtag_id*`
  请求体：无
- `GET /api/u1/v1/pipixia/app/fetch_hashtag_post_list`
  能力：作品详情 / 话题
  入参：query: `hashtag_id*`, `cursor`, `feed_count`, `hashtag_request_type`, `hashtag_sort_type`
  请求体：无
- `GET /api/u1/v1/pipixia/app/fetch_home_feed`
  能力：主页/账号
  入参：query: `cursor`
  请求体：无
- `GET /api/u1/v1/pipixia/app/fetch_home_short_drama_feed`
  能力：主页/账号
  入参：query: `page`
  请求体：无
- `GET /api/u1/v1/pipixia/app/fetch_hot_search_board_detail`
  能力：搜索 / 热点/榜单 / 详情
  入参：query: `block_type*`
  请求体：无
- `GET /api/u1/v1/pipixia/app/fetch_hot_search_board_list`
  能力：搜索 / 热点/榜单
  入参：无
  请求体：无
- `GET /api/u1/v1/pipixia/app/fetch_hot_search_words`
  能力：搜索 / 热点/榜单
  入参：无
  请求体：无
- `GET /api/u1/v1/pipixia/app/fetch_increase_post_view_count`
  能力：作品详情
  入参：query: `cell_id*`, `cell_type`
  请求体：无
- `GET /api/u1/v1/pipixia/app/fetch_post_comment_list`
  能力：评论 / 作品详情
  入参：query: `cell_id*`, `cell_type`, `offset`
  请求体：无
- `GET /api/u1/v1/pipixia/app/fetch_post_detail`
  能力：作品详情 / 详情
  入参：query: `cell_id*`, `cell_type`
  请求体：无
- `GET /api/u1/v1/pipixia/app/fetch_post_statistics`
  能力：作品详情
  入参：query: `cell_id*`
  请求体：无
- `GET /api/u1/v1/pipixia/app/fetch_search`
  能力：搜索
  入参：query: `keyword*`, `offset`, `search_type`
  请求体：无
- `GET /api/u1/v1/pipixia/app/fetch_short_url`
  能力：通用能力
  入参：query: `original_url*`
  请求体：无
- `GET /api/u1/v1/pipixia/app/fetch_user_follower_list`
  能力：主页/账号
  入参：query: `user_id*`, `cursor`
  请求体：无
- `GET /api/u1/v1/pipixia/app/fetch_user_following_list`
  能力：主页/账号
  入参：query: `user_id*`, `cursor`
  请求体：无
- `GET /api/u1/v1/pipixia/app/fetch_user_info`
  能力：主页/账号
  入参：query: `user_id*`
  请求体：无
- `GET /api/u1/v1/pipixia/app/fetch_user_post_list`
  能力：主页/账号 / 作品详情
  入参：query: `user_id*`, `cursor`, `feed_count`
  请求体：无

### `Reddit-APP-API`

- 路由数：`24`
- 标签说明：**(Reddit APP数据接口/Reddit-APP-API endpoints)**
- 常见入参：`need_format`, `after`, `sort`, `username`, `subreddit_name`, `subreddit_id`, `post_id`, `filter_posts`, `include_comment_id`, `comment_id`

- `GET /api/u1/v1/reddit/app/check_subreddit_muted`
  能力：通用能力
  入参：query: `subreddit_id*`, `need_format`
  请求体：无
- `GET /api/u1/v1/reddit/app/fetch_comment_replies`
  能力：评论
  入参：query: `post_id*`, `cursor*`, `sort_type`, `need_format`
  请求体：无
- `GET /api/u1/v1/reddit/app/fetch_community_highlights`
  能力：通用能力
  入参：query: `subreddit_id*`, `need_format`
  请求体：无
- `GET /api/u1/v1/reddit/app/fetch_dynamic_search`
  能力：搜索
  入参：query: `query*`, `search_type`, `sort`, `time_range`, `safe_search`, `allow_nsfw`, `after`, `need_format`
  请求体：无
- `GET /api/u1/v1/reddit/app/fetch_games_feed`
  能力：通用能力
  入参：query: `sort`, `time`, `after`, `need_format`
  请求体：无
- `GET /api/u1/v1/reddit/app/fetch_home_feed`
  能力：主页/账号
  入参：query: `sort`, `filter_posts`, `after`, `need_format`
  请求体：无
- `GET /api/u1/v1/reddit/app/fetch_news_feed`
  能力：通用能力
  入参：query: `subtopic_ids`, `after`, `need_format`
  请求体：无
- `GET /api/u1/v1/reddit/app/fetch_popular_feed`
  能力：通用能力
  入参：query: `sort`, `time`, `filter_posts`, `after`, `need_format`
  请求体：无
- `GET /api/u1/v1/reddit/app/fetch_post_comments`
  能力：评论 / 作品详情
  入参：query: `post_id*`, `sort_type`, `after`, `need_format`
  请求体：无
- `GET /api/u1/v1/reddit/app/fetch_post_details`
  能力：作品详情 / 详情
  入参：query: `post_id*`, `include_comment_id`, `comment_id`, `need_format`
  请求体：无
- `GET /api/u1/v1/reddit/app/fetch_post_details_batch`
  能力：作品详情 / 详情
  入参：query: `post_ids*`, `include_comment_id`, `comment_id`, `need_format`
  请求体：无
- `GET /api/u1/v1/reddit/app/fetch_post_details_batch_large`
  能力：作品详情 / 详情
  入参：query: `post_ids*`, `include_comment_id`, `comment_id`, `need_format`
  请求体：无
- `GET /api/u1/v1/reddit/app/fetch_search_typeahead`
  能力：搜索
  入参：query: `query*`, `safe_search`, `allow_nsfw`, `need_format`
  请求体：无
- `GET /api/u1/v1/reddit/app/fetch_subreddit_feed`
  能力：通用能力
  入参：query: `subreddit_name*`, `sort`, `filter_posts`, `after`, `need_format`
  请求体：无
- `GET /api/u1/v1/reddit/app/fetch_subreddit_info`
  能力：通用能力
  入参：query: `subreddit_name`, `need_format`
  请求体：无
- `GET /api/u1/v1/reddit/app/fetch_subreddit_post_channels`
  能力：主页/账号 / 作品详情
  入参：query: `subreddit_name`, `sort`, `range`, `need_format`
  请求体：无
- `GET /api/u1/v1/reddit/app/fetch_subreddit_settings`
  能力：通用能力
  入参：query: `subreddit_id*`, `need_format`
  请求体：无
- `GET /api/u1/v1/reddit/app/fetch_subreddit_style`
  能力：通用能力
  入参：query: `subreddit_name`, `need_format`
  请求体：无
- `GET /api/u1/v1/reddit/app/fetch_trending_searches`
  能力：搜索 / 热点/榜单
  入参：query: `need_format`
  请求体：无
- `GET /api/u1/v1/reddit/app/fetch_user_active_subreddits`
  能力：主页/账号
  入参：query: `username*`, `need_format`
  请求体：无
- `GET /api/u1/v1/reddit/app/fetch_user_comments`
  能力：评论 / 主页/账号
  入参：query: `username*`, `sort`, `page_size`, `after`, `need_format`
  请求体：无
- `GET /api/u1/v1/reddit/app/fetch_user_posts`
  能力：主页/账号 / 作品详情
  入参：query: `username*`, `sort`, `after`, `need_format`
  请求体：无
- `GET /api/u1/v1/reddit/app/fetch_user_profile`
  能力：主页/账号
  入参：query: `username*`, `need_format`
  请求体：无
- `GET /api/u1/v1/reddit/app/fetch_user_trophies`
  能力：主页/账号
  入参：query: `username*`, `need_format`
  请求体：无

### `Sora2-API`

- 路由数：`17`
- 标签说明：**(Sora2 接口/Sora2 API endpoints)**
- 常见入参：`cursor`, `user_id`, `post_id`, `post_url`, `task_id`, `prompt`, `orientation`, `media_id`, `comment_id`, `eager_views`

- `POST /api/u1/v1/sora2/create_video`
  能力：作品详情
  入参：无
  请求体：application/json: `prompt*`:string, `orientation`:string, `media_id`:string
- `GET /api/u1/v1/sora2/get_cameo_leaderboard`
  能力：通用能力
  入参：query: `cursor`
  请求体：无
- `GET /api/u1/v1/sora2/get_comment_replies`
  能力：评论
  入参：query: `comment_id*`, `cursor`
  请求体：无
- `GET /api/u1/v1/sora2/get_feed`
  能力：通用能力
  入参：query: `cursor`, `eager_views`
  请求体：无
- `GET /api/u1/v1/sora2/get_post_comments`
  能力：评论 / 作品详情
  入参：query: `post_id*`, `cursor`
  请求体：无
- `GET /api/u1/v1/sora2/get_post_detail`
  能力：作品详情 / 详情
  入参：query: `post_id`, `post_url`
  请求体：无
- `GET /api/u1/v1/sora2/get_post_remix_list`
  能力：作品详情
  入参：query: `post_id`, `post_url`, `cursor`
  请求体：无
- `GET /api/u1/v1/sora2/get_task_detail`
  能力：详情
  入参：query: `task_id`, `generation_id`
  请求体：无
- `GET /api/u1/v1/sora2/get_task_status`
  能力：通用能力
  入参：query: `task_id*`
  请求体：无
- `GET /api/u1/v1/sora2/get_user_cameo_appearances`
  能力：主页/账号
  入参：query: `user_id*`, `cursor`
  请求体：无
- `GET /api/u1/v1/sora2/get_user_followers`
  能力：主页/账号
  入参：query: `user_id*`, `cursor`
  请求体：无
- `GET /api/u1/v1/sora2/get_user_following`
  能力：主页/账号
  入参：query: `user_id*`, `cursor`
  请求体：无
- `GET /api/u1/v1/sora2/get_user_posts`
  能力：主页/账号 / 作品详情
  入参：query: `user_id*`, `cursor`
  请求体：无
- `GET /api/u1/v1/sora2/get_user_profile`
  能力：主页/账号
  入参：query: `user_id*`
  请求体：无
- `GET /api/u1/v1/sora2/get_video_download_info`
  能力：作品详情 / 下载/媒体 / 广告
  入参：query: `post_id`, `post_url`
  请求体：无
- `GET /api/u1/v1/sora2/search_users`
  能力：搜索 / 主页/账号
  入参：query: `username*`
  请求体：无
- `POST /api/u1/v1/sora2/upload_image`
  能力：广告
  入参：无
  请求体：multipart/form-data: `file*`:string

### `Temp-Mail-API`

- 路由数：`3`
- 标签说明：**(临时邮箱接口/Temp-Mail-API endpoints)**
- 常见入参：`token`, `message_id`

- `GET /api/u1/v1/temp_mail/v1/get_email_by_id`
  能力：通用能力
  入参：query: `token*`, `message_id*`
  请求体：无
- `GET /api/u1/v1/temp_mail/v1/get_emails_inbox`
  能力：通用能力
  入参：query: `token*`
  请求体：无
- `GET /api/u1/v1/temp_mail/v1/get_temp_email_address`
  能力：通用能力
  入参：无
  请求体：无

### `Threads-Web-API`

- 路由数：`11`
- 标签说明：**(Threads Web数据接口/Threads-Web-API endpoints)**
- 常见入参：`end_cursor`, `user_id`, `post_id`, `query`, `url`, `username`

- `GET /api/u1/v1/threads/web/fetch_post_comments`
  能力：评论 / 作品详情 / 广告
  入参：query: `post_id*`, `end_cursor`
  请求体：无
- `GET /api/u1/v1/threads/web/fetch_post_detail`
  能力：作品详情 / 详情 / 广告
  入参：query: `post_id*`
  请求体：无
- `GET /api/u1/v1/threads/web/fetch_post_detail_v2`
  能力：作品详情 / 详情 / 广告
  入参：query: `post_id`, `url`
  请求体：无
- `GET /api/u1/v1/threads/web/fetch_user_info`
  能力：主页/账号 / 广告
  入参：query: `username*`
  请求体：无
- `GET /api/u1/v1/threads/web/fetch_user_info_by_id`
  能力：主页/账号 / 广告
  入参：query: `user_id*`
  请求体：无
- `GET /api/u1/v1/threads/web/fetch_user_posts`
  能力：主页/账号 / 作品详情 / 广告
  入参：query: `user_id*`, `end_cursor`
  请求体：无
- `GET /api/u1/v1/threads/web/fetch_user_replies`
  能力：主页/账号 / 广告
  入参：query: `user_id*`, `end_cursor`
  请求体：无
- `GET /api/u1/v1/threads/web/fetch_user_reposts`
  能力：主页/账号 / 作品详情 / 广告
  入参：query: `user_id*`, `end_cursor`
  请求体：无
- `GET /api/u1/v1/threads/web/search_profiles`
  能力：搜索 / 主页/账号 / 广告
  入参：query: `query*`
  请求体：无
- `GET /api/u1/v1/threads/web/search_recent`
  能力：搜索 / 广告
  入参：query: `query*`, `end_cursor`
  请求体：无
- `GET /api/u1/v1/threads/web/search_top`
  能力：搜索 / 广告
  入参：query: `query*`, `end_cursor`
  请求体：无

### `TikHub-Downloader-API`

- 路由数：`2`
- 标签说明：**(TikHub下载器接口/TikHub-Downloader-API endpoints)**
- 常见入参：无

- `GET /api/u1/v1/tikhub/downloader/redirect_download`
  能力：下载/媒体
  入参：无
  请求体：无
- `GET /api/u1/v1/tikhub/downloader/version`
  能力：下载/媒体
  入参：无
  请求体：无

### `TikHub-User-API`

- 路由数：`6`
- 标签说明：**(TikHub用户数据接口/TikHub-User-API endpoints)**
- 常见入参：`endpoint`, `request_per_day`

- `GET /api/u1/v1/tikhub/user/calculate_price`
  能力：主页/账号
  入参：query: `endpoint*`, `request_per_day`
  请求体：无
- `GET /api/u1/v1/tikhub/user/get_all_endpoints_info`
  能力：主页/账号
  入参：无
  请求体：无
- `GET /api/u1/v1/tikhub/user/get_endpoint_info`
  能力：主页/账号
  入参：query: `endpoint*`
  请求体：无
- `GET /api/u1/v1/tikhub/user/get_tiered_discount_info`
  能力：主页/账号
  入参：无
  请求体：无
- `GET /api/u1/v1/tikhub/user/get_user_daily_usage`
  能力：主页/账号
  入参：无
  请求体：无
- `GET /api/u1/v1/tikhub/user/get_user_info`
  能力：主页/账号
  入参：无
  请求体：无

### `TikTok-Ads-API`

- 路由数：`31`
- 标签说明：**(TikTok广告创意中心数据接口/TikTok-Ads-Creative-Center-API endpoints)**
- 常见入参：`limit`, `page`, `country_code`, `period`, `keyword`, `period_type`, `industry`, `order_by`, `rank_type`, `material_id`

- `GET /api/u1/v1/tiktok/ads/get_ad_interactive_analysis`
  能力：广告
  入参：query: `material_id*`, `metric_type`, `period_type`
  请求体：无
- `GET /api/u1/v1/tiktok/ads/get_ad_keyframe_analysis`
  能力：广告
  入参：query: `material_id*`, `metric`
  请求体：无
- `GET /api/u1/v1/tiktok/ads/get_ad_percentile`
  能力：广告
  入参：query: `material_id*`, `metric`, `period_type`
  请求体：无
- `GET /api/u1/v1/tiktok/ads/get_ads_detail`
  能力：详情 / 广告
  入参：query: `ads_id*`
  请求体：无
- `GET /api/u1/v1/tiktok/ads/get_creative_patterns`
  能力：广告
  入参：query: `first_industry_id`, `period_type`, `order_field`, `order_type`, `week`, `page`, `limit`
  请求体：无
- `GET /api/u1/v1/tiktok/ads/get_creator_filters`
  能力：创作者 / 广告
  入参：无
  请求体：无
- `GET /api/u1/v1/tiktok/ads/get_creator_list`
  能力：创作者 / 广告
  入参：query: `page`, `limit`, `sort_by`, `creator_country`, `audience_country`, `audience_count`, `keyword`
  请求体：无
- `GET /api/u1/v1/tiktok/ads/get_hashtag_creator`
  能力：创作者 / 广告 / 话题
  入参：query: `hashtag*`
  请求体：无
- `GET /api/u1/v1/tiktok/ads/get_hashtag_filters`
  能力：广告 / 话题
  入参：无
  请求体：无
- `GET /api/u1/v1/tiktok/ads/get_hashtag_list`
  能力：广告 / 话题
  入参：query: `page`, `limit`, `period`, `country_code`, `sort_by`, `industry_id`, `filter_by`
  请求体：无
- `GET /api/u1/v1/tiktok/ads/get_keyword_details`
  能力：详情 / 广告
  入参：query: `keyword`, `page`, `limit`, `period`, `country_code`, `order_by`, `order_type`, `industry`, `objective`, `keyword_type`
  请求体：无
- `GET /api/u1/v1/tiktok/ads/get_keyword_filters`
  能力：广告
  入参：无
  请求体：无
- `GET /api/u1/v1/tiktok/ads/get_keyword_insights`
  能力：广告 / 数据分析
  入参：query: `page`, `limit`, `period`, `country_code`, `order_by`, `order_type`, `industry`, `objective`, `keyword_type`, `keyword`
  请求体：无
- `GET /api/u1/v1/tiktok/ads/get_keyword_list`
  能力：广告
  入参：query: `keyword`, `period`, `page`, `limit`, `country_code`, `industry`
  请求体：无
- `GET /api/u1/v1/tiktok/ads/get_popular_trends`
  能力：热点/榜单 / 广告
  入参：query: `period`, `page`, `limit`, `order_by`, `country_code`
  请求体：无
- `GET /api/u1/v1/tiktok/ads/get_product_detail`
  能力：详情 / 电商 / 广告
  入参：query: `id*`, `last`, `ecom_type`, `period_type`, `country_code`
  请求体：无
- `GET /api/u1/v1/tiktok/ads/get_product_filters`
  能力：电商 / 广告
  入参：无
  请求体：无
- `GET /api/u1/v1/tiktok/ads/get_product_metrics`
  能力：电商 / 广告
  入参：query: `id*`, `last`, `metrics`, `ecom_type`, `period_type`, `country_code`
  请求体：无
- `GET /api/u1/v1/tiktok/ads/get_query_suggestions`
  能力：搜索 / 广告
  入参：query: `count`, `scenario`
  请求体：无
- `GET /api/u1/v1/tiktok/ads/get_recommended_ads`
  能力：广告
  入参：query: `material_id*`, `industry`, `country_code`
  请求体：无
- `GET /api/u1/v1/tiktok/ads/get_related_keywords`
  能力：广告
  入参：query: `keyword`, `period`, `country_code`, `rank_type`, `content_type`, `page`, `limit`
  请求体：无
- `GET /api/u1/v1/tiktok/ads/get_sound_detail`
  能力：详情 / 广告
  入参：query: `clip_id*`, `period`, `country_code`
  请求体：无
- `GET /api/u1/v1/tiktok/ads/get_sound_filters`
  能力：广告
  入参：query: `rank_type`
  请求体：无
- `GET /api/u1/v1/tiktok/ads/get_sound_rank_list`
  能力：广告
  入参：query: `period`, `page`, `limit`, `rank_type`, `new_on_board`, `commercial_music`, `country_code`
  请求体：无
- `GET /api/u1/v1/tiktok/ads/get_sound_recommendations`
  能力：广告
  入参：query: `clip_id*`, `limit`
  请求体：无
- `GET /api/u1/v1/tiktok/ads/get_top_ads_spotlight`
  能力：广告
  入参：query: `industry`, `page`, `limit`
  请求体：无
- `GET /api/u1/v1/tiktok/ads/get_top_products`
  能力：电商 / 广告
  入参：query: `last`, `page`, `limit`, `country_code`, `first_ecom_category_id`, `ecom_type`, `period_type`, `order_by`, `order_type`
  请求体：无
- `GET /api/u1/v1/tiktok/ads/search_ads`
  能力：搜索 / 广告
  入参：query: `objective`, `like`, `period`, `industry`, `keyword`, `page`, `limit`, `order_by`, `country_code`, `ad_format`, `ad_language`, `search_id`
  请求体：无
- `GET /api/u1/v1/tiktok/ads/search_creators`
  能力：搜索 / 创作者 / 广告
  入参：query: `keyword*`, `page`, `limit`, `sort_by`, `creator_country`
  请求体：无
- `GET /api/u1/v1/tiktok/ads/search_sound`
  能力：搜索 / 广告
  入参：query: `keyword*`, `period`, `page`, `limit`, `rank_type`, `new_on_board`, `commercial_music`, `country_code`
  请求体：无
- `GET /api/u1/v1/tiktok/ads/search_sound_hint`
  能力：搜索 / 广告
  入参：query: `keyword*`, `period`, `page`, `limit`, `rank_type`, `country_code`, `filter_by_checked`, `commercial_music`
  请求体：无

### `TikTok-Analytics-API`

- 路由数：`4`
- 标签说明：**(TikTok数据分析接口/TikTok-Analytics-API data analysis endpoints)**
- 常见入参：`item_id`, `content_category`, `user_id`

- `GET /api/u1/v1/tiktok/analytics/detect_fake_views`
  能力：数据分析
  入参：query: `item_id*`, `content_category`
  请求体：无
- `GET /api/u1/v1/tiktok/analytics/fetch_comment_keywords`
  能力：评论 / 数据分析
  入参：query: `item_id*`
  请求体：无
- `GET /api/u1/v1/tiktok/analytics/fetch_creator_info_and_milestones`
  能力：创作者 / 数据分析
  入参：query: `user_id*`
  请求体：无
- `GET /api/u1/v1/tiktok/analytics/fetch_video_metrics`
  能力：作品详情 / 数据分析
  入参：query: `item_id*`
  请求体：无

### `TikTok-App-V3-API`

- 路由数：`75`
- 标签说明：**(TikTok-App-V3-API数据接口（当前最新版本）/TikTok-App-V3-API (Current latest version))**
- 常见入参：`count`, `offset`, `keyword`, `sort_type`, `cursor`, `region`, `sec_user_id`, `user_id`, `room_id`, `seller_id`

- `POST /api/u1/v1/tiktok/app/v3/TTencrypt_algorithm`
  能力：通用能力
  入参：无
  请求体：application/json: `url`:string, `data`:string, `device_info`{...}
- `GET /api/u1/v1/tiktok/app/v3/add_video_play_count`
  能力：作品详情
  入参：query: `aweme_type*`, `item_id*`
  请求体：无
- `GET /api/u1/v1/tiktok/app/v3/check_live_room_online`
  能力：直播
  入参：query: `room_id*`
  请求体：无
- `POST /api/u1/v1/tiktok/app/v3/check_live_room_online_batch`
  能力：直播
  入参：无
  请求体：application/json: `room_ids`[]
- `POST /api/u1/v1/tiktok/app/v3/encrypt_decrypt_login_request`
  能力：通用能力
  入参：无
  请求体：application/json: `username`:string, `password`:string, `mode`:string
- `POST /api/u1/v1/tiktok/app/v3/fetch_content_translate`
  能力：通用能力
  入参：无
  请求体：application/json: `trg_lang`:string, `src_content`:string
- `GET /api/u1/v1/tiktok/app/v3/fetch_creator_info`
  能力：创作者
  入参：query: `creator_uid*`
  请求体：无
- `GET /api/u1/v1/tiktok/app/v3/fetch_creator_search_insights`
  能力：搜索 / 创作者 / 数据分析
  入参：query: `offset`, `limit`, `tab`, `language_filters`, `category_filters`, `creator_source`, `force_refresh`
  请求体：无
- `GET /api/u1/v1/tiktok/app/v3/fetch_creator_search_insights_detail`
  能力：搜索 / 创作者 / 详情 / 数据分析
  入参：query: `query_id_str*`, `time_range`, `start_date`, `end_date`, `dimension_list`
  请求体：无
- `GET /api/u1/v1/tiktok/app/v3/fetch_creator_search_insights_trend`
  能力：搜索 / 热点/榜单 / 创作者 / 数据分析
  入参：query: `query_id_str*`, `from_tab_path`, `query_analysis_required`
  请求体：无
- `GET /api/u1/v1/tiktok/app/v3/fetch_creator_search_insights_videos`
  能力：搜索 / 创作者 / 作品详情 / 数据分析
  入参：query: `keyword*`, `offset`, `count`
  请求体：无
- `GET /api/u1/v1/tiktok/app/v3/fetch_creator_showcase_product_list`
  能力：创作者 / 电商
  入参：query: `kol_id*`, `count`, `next_scroll_param`
  请求体：无
- `GET /api/u1/v1/tiktok/app/v3/fetch_general_search_result`
  能力：搜索
  入参：query: `keyword*`, `offset`, `count`, `sort_type`, `publish_time`
  请求体：无
- `GET /api/u1/v1/tiktok/app/v3/fetch_hashtag_detail`
  能力：详情 / 话题
  入参：query: `ch_id*`
  请求体：无
- `GET /api/u1/v1/tiktok/app/v3/fetch_hashtag_search_result`
  能力：搜索 / 话题
  入参：query: `keyword*`, `offset`, `count`
  请求体：无
- `GET /api/u1/v1/tiktok/app/v3/fetch_hashtag_video_list`
  能力：作品详情 / 话题
  入参：query: `ch_id*`, `cursor`, `count`
  请求体：无
- `POST /api/u1/v1/tiktok/app/v3/fetch_home_feed`
  能力：主页/账号
  入参：无
  请求体：application/json: `cookie`:string
- `GET /api/u1/v1/tiktok/app/v3/fetch_live_daily_rank`
  能力：直播
  入参：query: `anchor_id`, `room_id`, `rank_type`, `region_type`, `gap_interval`, `cookie`
  请求体：无
- `GET /api/u1/v1/tiktok/app/v3/fetch_live_ranking_list`
  能力：直播
  入参：query: `room_id*`, `anchor_id*`
  请求体：无
- `GET /api/u1/v1/tiktok/app/v3/fetch_live_room_info`
  能力：直播
  入参：query: `room_id*`
  请求体：无
- `GET /api/u1/v1/tiktok/app/v3/fetch_live_room_product_list`
  能力：电商 / 直播
  入参：query: `room_id*`, `author_id*`, `page_size`, `offset`, `region`, `cookie`
  请求体：无
- `GET /api/u1/v1/tiktok/app/v3/fetch_live_room_product_list_v2`
  能力：电商 / 直播
  入参：query: `room_id*`, `author_id*`, `page_size`, `offset`, `region`, `cookie`
  请求体：无
- `GET /api/u1/v1/tiktok/app/v3/fetch_live_search_result`
  能力：搜索 / 直播
  入参：query: `keyword*`, `offset`, `count`, `region`
  请求体：无
- `GET /api/u1/v1/tiktok/app/v3/fetch_location_search`
  能力：搜索
  入参：query: `keyword*`, `offset`, `count`
  请求体：无
- `POST /api/u1/v1/tiktok/app/v3/fetch_multi_video`
  能力：作品详情
  入参：无
  请求体：application/json: 动态对象
- `POST /api/u1/v1/tiktok/app/v3/fetch_multi_video_v2`
  能力：作品详情
  入参：无
  请求体：application/json: 动态对象
- `GET /api/u1/v1/tiktok/app/v3/fetch_music_chart_list`
  能力：音乐/音频
  入参：query: `scene`, `cursor`, `count`
  请求体：无
- `GET /api/u1/v1/tiktok/app/v3/fetch_music_detail`
  能力：详情 / 音乐/音频
  入参：query: `music_id*`
  请求体：无
- `GET /api/u1/v1/tiktok/app/v3/fetch_music_search_result`
  能力：搜索 / 音乐/音频
  入参：query: `keyword*`, `offset`, `count`, `filter_by`, `sort_type`, `region`
  请求体：无
- `GET /api/u1/v1/tiktok/app/v3/fetch_music_video_list`
  能力：作品详情 / 音乐/音频
  入参：query: `music_id*`, `cursor`, `count`
  请求体：无
- `GET /api/u1/v1/tiktok/app/v3/fetch_one_video`
  能力：作品详情
  入参：query: `aweme_id*`
  请求体：无
- `GET /api/u1/v1/tiktok/app/v3/fetch_one_video_by_share_url`
  能力：作品详情
  入参：query: `share_url*`
  请求体：无
- `GET /api/u1/v1/tiktok/app/v3/fetch_one_video_by_share_url_v2`
  能力：作品详情
  入参：query: `share_url*`
  请求体：无
- `GET /api/u1/v1/tiktok/app/v3/fetch_one_video_v2`
  能力：作品详情
  入参：query: `aweme_id*`
  请求体：无
- `GET /api/u1/v1/tiktok/app/v3/fetch_one_video_v3`
  能力：作品详情
  入参：query: `aweme_id*`, `region`
  请求体：无
- `GET /api/u1/v1/tiktok/app/v3/fetch_product_detail`
  能力：详情 / 电商
  入参：query: `product_id*`
  请求体：无
- `GET /api/u1/v1/tiktok/app/v3/fetch_product_detail_v2`
  能力：详情 / 电商
  入参：query: `product_id*`
  请求体：无
- `GET /api/u1/v1/tiktok/app/v3/fetch_product_detail_v3`
  能力：详情 / 电商
  入参：query: `product_id*`, `region`
  请求体：无
- `GET /api/u1/v1/tiktok/app/v3/fetch_product_detail_v4`
  能力：详情 / 电商
  入参：query: `product_id*`, `region`
  请求体：无
- `GET /api/u1/v1/tiktok/app/v3/fetch_product_id_by_share_link`
  能力：电商
  入参：query: `share_link*`
  请求体：无
- `GET /api/u1/v1/tiktok/app/v3/fetch_product_review`
  能力：电商
  入参：query: `product_id*`, `cursor`, `size`, `filter_id`, `sort_type`
  请求体：无
- `GET /api/u1/v1/tiktok/app/v3/fetch_product_search`
  能力：搜索 / 电商
  入参：query: `keyword*`, `cursor`, `count`, `sort_type`, `customer_review_four_star`, `have_discount`, `min_price`, `max_price`
  请求体：无
- `GET /api/u1/v1/tiktok/app/v3/fetch_share_qr_code`
  能力：通用能力
  入参：query: `object_id*`, `schema_type`
  请求体：无
- `GET /api/u1/v1/tiktok/app/v3/fetch_share_short_link`
  能力：通用能力
  入参：query: `url*`
  请求体：无
- `GET /api/u1/v1/tiktok/app/v3/fetch_shop_home`
  能力：主页/账号 / 电商
  入参：query: `page_id*`, `seller_id*`
  请求体：无
- `GET /api/u1/v1/tiktok/app/v3/fetch_shop_home_page_list`
  能力：主页/账号 / 电商
  入参：query: `seller_id*`
  请求体：无
- `GET /api/u1/v1/tiktok/app/v3/fetch_shop_id_by_share_link`
  能力：电商
  入参：query: `share_link*`
  请求体：无
- `GET /api/u1/v1/tiktok/app/v3/fetch_shop_info`
  能力：电商
  入参：query: `shop_id*`
  请求体：无
- `GET /api/u1/v1/tiktok/app/v3/fetch_shop_product_category`
  能力：电商
  入参：query: `seller_id*`
  请求体：无
- `GET /api/u1/v1/tiktok/app/v3/fetch_shop_product_list`
  能力：电商
  入参：query: `seller_id*`, `scroll_params`, `page_size`, `sort_field`, `sort_order`
  请求体：无
- `GET /api/u1/v1/tiktok/app/v3/fetch_shop_product_list_v2`
  能力：电商
  入参：query: `seller_id*`, `scroll_params`, `page_size`, `sort_field`, `sort_order`
  请求体：无
- `GET /api/u1/v1/tiktok/app/v3/fetch_shop_product_recommend`
  能力：电商
  入参：query: `seller_id*`, `scroll_param`, `page_size`
  请求体：无
- `GET /api/u1/v1/tiktok/app/v3/fetch_similar_user_recommendations`
  能力：主页/账号
  入参：query: `sec_uid*`, `page_token`
  请求体：无
- `GET /api/u1/v1/tiktok/app/v3/fetch_user_country_by_username`
  能力：主页/账号
  入参：query: `username*`
  请求体：无
- `GET /api/u1/v1/tiktok/app/v3/fetch_user_follower_list`
  能力：主页/账号
  入参：query: `user_id`, `sec_user_id`, `count`, `min_time`, `page_token`
  请求体：无
- `GET /api/u1/v1/tiktok/app/v3/fetch_user_following_list`
  能力：主页/账号
  入参：query: `user_id`, `sec_user_id`, `count`, `min_time`, `page_token`
  请求体：无
- `GET /api/u1/v1/tiktok/app/v3/fetch_user_like_videos`
  能力：主页/账号 / 作品详情
  入参：query: `sec_user_id*`, `max_cursor`, `counts`
  请求体：无
- `GET /api/u1/v1/tiktok/app/v3/fetch_user_music_list`
  能力：主页/账号 / 音乐/音频
  入参：query: `sec_uid*`, `cursor`, `count`
  请求体：无
- `GET /api/u1/v1/tiktok/app/v3/fetch_user_post_videos`
  能力：主页/账号 / 作品详情
  入参：query: `sec_user_id`, `unique_id`, `max_cursor`, `count`, `sort_type`
  请求体：无
- `GET /api/u1/v1/tiktok/app/v3/fetch_user_post_videos_v2`
  能力：主页/账号 / 作品详情
  入参：query: `sec_user_id`, `unique_id`, `max_cursor`, `count`, `sort_type`
  请求体：无
- `GET /api/u1/v1/tiktok/app/v3/fetch_user_post_videos_v3`
  能力：主页/账号 / 作品详情
  入参：query: `sec_user_id`, `unique_id`, `max_cursor`, `count`, `sort_type`
  请求体：无
- `GET /api/u1/v1/tiktok/app/v3/fetch_user_repost_videos`
  能力：主页/账号 / 作品详情
  入参：query: `user_id*`, `offset`, `count`
  请求体：无
- `GET /api/u1/v1/tiktok/app/v3/fetch_user_search_result`
  能力：搜索 / 主页/账号
  入参：query: `keyword*`, `offset`, `count`, `user_search_follower_count`, `user_search_profile_type`, `user_search_other_pref`
  请求体：无
- `GET /api/u1/v1/tiktok/app/v3/fetch_video_comment_replies`
  能力：评论 / 作品详情
  入参：query: `item_id*`, `comment_id*`, `cursor`, `count`
  请求体：无
- `GET /api/u1/v1/tiktok/app/v3/fetch_video_comments`
  能力：评论 / 作品详情
  入参：query: `aweme_id*`, `cursor`, `count`
  请求体：无
- `GET /api/u1/v1/tiktok/app/v3/fetch_video_search_result`
  能力：搜索 / 作品详情
  入参：query: `keyword*`, `offset`, `count`, `sort_type`, `publish_time`, `region`
  请求体：无
- `GET /api/u1/v1/tiktok/app/v3/fetch_webcast_user_info`
  能力：主页/账号
  入参：query: `user_id`, `sec_user_id`
  请求体：无
- `GET /api/u1/v1/tiktok/app/v3/get_user_id_and_sec_user_id_by_username`
  能力：主页/账号
  入参：query: `username*`
  请求体：无
- `GET /api/u1/v1/tiktok/app/v3/handler_user_profile`
  能力：主页/账号
  入参：query: `user_id`, `sec_user_id`, `unique_id`
  请求体：无
- `GET /api/u1/v1/tiktok/app/v3/open_tiktok_app_to_keyword_search`
  能力：搜索
  入参：query: `keyword*`
  请求体：无
- `GET /api/u1/v1/tiktok/app/v3/open_tiktok_app_to_send_private_message`
  能力：通用能力
  入参：query: `uid*`
  请求体：无
- `GET /api/u1/v1/tiktok/app/v3/open_tiktok_app_to_user_profile`
  能力：主页/账号
  入参：query: `uid*`
  请求体：无
- `GET /api/u1/v1/tiktok/app/v3/open_tiktok_app_to_video_detail`
  能力：作品详情 / 详情
  入参：query: `aweme_id*`
  请求体：无
- `GET /api/u1/v1/tiktok/app/v3/search_follower_list`
  能力：搜索
  入参：query: `user_id*`, `keyword*`
  请求体：无
- `GET /api/u1/v1/tiktok/app/v3/search_following_list`
  能力：搜索
  入参：query: `user_id*`, `keyword*`
  请求体：无

### `TikTok-Creator-API`

- 路由数：`14`
- 标签说明：**(TikTok创作者数据和账号收益数据接口/TikTok-Creator-API data and account revenue data endpoints)**
- 常见入参：`cookie`, `proxy`, `start_date`, `item_id`, `page`, `product_id`, `end_date`, `count`, `offset`, `item_ids`

- `POST /api/u1/v1/tiktok/creator/get_account_health_status`
  能力：创作者
  入参：无
  请求体：application/json: `cookie`:string, `proxy`:string
- `POST /api/u1/v1/tiktok/creator/get_account_insights_overview`
  能力：创作者 / 数据分析
  入参：无
  请求体：application/json: `cookie`:string, `proxy`:string, `start_date`:string
- `POST /api/u1/v1/tiktok/creator/get_account_violation_list`
  能力：创作者
  入参：无
  请求体：application/json: `cookie`:string, `proxy`:string, `page`:integer
- `POST /api/u1/v1/tiktok/creator/get_creator_account_info`
  能力：创作者
  入参：无
  请求体：application/json: `cookie`:string, `proxy`:string
- `POST /api/u1/v1/tiktok/creator/get_live_analytics_summary`
  能力：创作者 / 数据分析 / 直播
  入参：无
  请求体：application/json: `cookie`:string, `proxy`:string, `start_date`:string
- `POST /api/u1/v1/tiktok/creator/get_product_analytics_list`
  能力：创作者 / 电商 / 数据分析
  入参：无
  请求体：application/json: `cookie`:string, `proxy`:string, `start_date`:string, `end_date`:string, `page`:integer
- `POST /api/u1/v1/tiktok/creator/get_product_related_videos`
  能力：创作者 / 作品详情 / 电商
  入参：无
  请求体：application/json: `cookie`:string, `proxy`:string, `start_date`:string, `item_id*`:string, `product_id*`:string
- `POST /api/u1/v1/tiktok/creator/get_showcase_product_list`
  能力：创作者 / 电商
  入参：无
  请求体：application/json: `cookie`:string, `proxy`:string, `count`:integer, `offset`:integer
- `POST /api/u1/v1/tiktok/creator/get_video_analytics_summary`
  能力：创作者 / 作品详情 / 数据分析
  入参：无
  请求体：application/json: `cookie`:string, `proxy`:string
- `POST /api/u1/v1/tiktok/creator/get_video_associated_product_list`
  能力：创作者 / 作品详情 / 电商
  入参：无
  请求体：application/json: `cookie`:string, `proxy`:string, `start_date`:string, `item_ids*`[]
- `POST /api/u1/v1/tiktok/creator/get_video_audience_stats`
  能力：创作者 / 作品详情
  入参：无
  请求体：application/json: `cookie`:string, `proxy`:string, `start_date`:string, `item_id*`:string
- `POST /api/u1/v1/tiktok/creator/get_video_detailed_stats`
  能力：创作者 / 作品详情 / 详情
  入参：无
  请求体：application/json: `cookie`:string, `proxy`:string, `start_date`:string, `item_id*`:string
- `POST /api/u1/v1/tiktok/creator/get_video_list_analytics`
  能力：创作者 / 作品详情 / 数据分析
  入参：无
  请求体：application/json: `cookie`:string, `proxy`:string, `start_date`:string, `page`:integer, `rules`:string
- `POST /api/u1/v1/tiktok/creator/get_video_to_product_stats`
  能力：创作者 / 作品详情 / 电商
  入参：无
  请求体：application/json: `cookie`:string, `proxy`:string, `start_date`:string, `item_id*`:string, `product_id*`:string

### `TikTok-Interaction-API`

- 路由数：`7`
- 标签说明：**(TikTok交互类接口（不在提供该业务）/TikTok-Interaction-API (This service is no longer available))**
- 常见入参：`cookie`, `device_id`, `iid`, `proxy`, `aweme_id`, `text`, `api_key`, `invite_code`, `user_id`, `sec_user_id`

- `GET /api/u1/v1/tiktok/interaction/apply`
  能力：通用能力
  入参：query: `api_key*`, `invite_code*`
  请求体：无
- `POST /api/u1/v1/tiktok/interaction/collect`
  能力：通用能力
  入参：无
  请求体：application/json: `aweme_id`:string, `cookie`:string, `device_id`:string, `iid`:string, `proxy`:string
- `POST /api/u1/v1/tiktok/interaction/follow`
  能力：通用能力
  入参：无
  请求体：application/json: `user_id`:string, `sec_user_id`:string, `cookie`:string, `device_id`:string, `iid`:string, `proxy`:string
- `POST /api/u1/v1/tiktok/interaction/forward`
  能力：通用能力
  入参：无
  请求体：application/json: `aweme_id`:string, `cookie`:string, `device_id`:string, `iid`:string, `proxy`:string
- `POST /api/u1/v1/tiktok/interaction/like`
  能力：通用能力
  入参：无
  请求体：application/json: `aweme_id`:string, `cookie`:string, `device_id`:string, `iid`:string, `proxy`:string
- `POST /api/u1/v1/tiktok/interaction/post_comment`
  能力：评论 / 作品详情
  入参：无
  请求体：application/json: `aweme_id`:string, `text`:string, `cookie`:string, `device_id`:string, `iid`:string, `proxy`:string
- `POST /api/u1/v1/tiktok/interaction/reply_comment`
  能力：评论 / 评论回复
  入参：无
  请求体：application/json: `aweme_id`:string, `reply_id`:string, `text`:string, `cookie`:string, `device_id`:string, `iid`:string, `proxy`:string

### `TikTok-Shop-Web-API`

- 路由数：`15`
- 标签说明：**(TikTok电商网页版数据接口/TikTok-Shop-Web-API data endpoints)**
- 常见入参：`region`, `product_id`, `offset`, `seller_id`, `search_word`, `page_token`, `lang`, `count`, `sort_type`, `filter_id`

- `GET /api/u1/v1/tiktok/shop/web/fetch_hot_selling_products_list`
  能力：热点/榜单 / 电商
  入参：query: `region`, `count`
  请求体：无
- `GET /api/u1/v1/tiktok/shop/web/fetch_product_detail`
  能力：详情 / 电商
  入参：query: `product_id*`, `seller_id`, `region`
  请求体：无
- `GET /api/u1/v1/tiktok/shop/web/fetch_product_detail_v2`
  能力：详情 / 电商
  入参：query: `product_id*`, `seller_id`, `region`
  请求体：无
- `GET /api/u1/v1/tiktok/shop/web/fetch_product_detail_v3`
  能力：详情 / 电商
  入参：query: `product_id*`, `region`
  请求体：无
- `GET /api/u1/v1/tiktok/shop/web/fetch_product_reviews_v1`
  能力：电商
  入参：query: `product_id*`, `sort_type`, `filter_id`, `offset`
  请求体：无
- `GET /api/u1/v1/tiktok/shop/web/fetch_product_reviews_v2`
  能力：电商
  入参：query: `product_id*`, `page_start`, `sort_rule`, `filter_type`, `filter_value`, `region`
  请求体：无
- `GET /api/u1/v1/tiktok/shop/web/fetch_products_by_category_id`
  能力：电商
  入参：query: `category_id*`, `offset`, `region`
  请求体：无
- `GET /api/u1/v1/tiktok/shop/web/fetch_products_category_list`
  能力：电商
  入参：query: `region`
  请求体：无
- `GET /api/u1/v1/tiktok/shop/web/fetch_search_products_list`
  能力：搜索 / 电商
  入参：query: `search_word*`, `offset`, `page_token`, `region`
  请求体：无
- `GET /api/u1/v1/tiktok/shop/web/fetch_search_products_list_v2`
  能力：搜索 / 电商
  入参：query: `search_word*`, `offset`, `page_token`, `region`
  请求体：无
- `GET /api/u1/v1/tiktok/shop/web/fetch_search_products_list_v3`
  能力：搜索 / 电商
  入参：query: `keyword*`, `offset`, `region`, `sort_by`, `filters_data`
  请求体：无
- `GET /api/u1/v1/tiktok/shop/web/fetch_search_word_suggestion`
  能力：搜索 / 电商
  入参：query: `search_word*`, `lang`, `region`
  请求体：无
- `GET /api/u1/v1/tiktok/shop/web/fetch_search_word_suggestion_v2`
  能力：搜索 / 电商
  入参：query: `search_word*`, `lang`, `region`
  请求体：无
- `GET /api/u1/v1/tiktok/shop/web/fetch_seller_products_list`
  能力：电商
  入参：query: `seller_id*`, `search_params`, `region`
  请求体：无
- `GET /api/u1/v1/tiktok/shop/web/fetch_seller_products_list_v2`
  能力：电商
  入参：query: `seller_id*`, `searchParams`, `region`
  请求体：无

### `TikTok-Web-API`

- 路由数：`58`
- 标签说明：**(TikTok-Web-API数据接口/TikTok-Web-API data endpoints)**
- 常见入参：`count`, `cursor`, `cookie`, `secUid`, `url`, `keyword`, `search_id`, `user_agent`, `offset`, `coverFormat`

- `GET /api/u1/v1/tiktok/web/decrypt_strData`
  能力：通用能力
  入参：query: `encrypted_data*`
  请求体：无
- `GET /api/u1/v1/tiktok/web/device_register`
  能力：通用能力
  入参：无
  请求体：无
- `GET /api/u1/v1/tiktok/web/encrypt_strData`
  能力：通用能力
  入参：query: `data*`
  请求体：无
- `GET /api/u1/v1/tiktok/web/fetch_batch_check_live_alive`
  能力：直播
  入参：query: `room_ids*`
  请求体：无
- `GET /api/u1/v1/tiktok/web/fetch_check_live_alive`
  能力：直播
  入参：query: `room_id*`
  请求体：无
- `GET /api/u1/v1/tiktok/web/fetch_explore_post`
  能力：作品详情
  入参：query: `categoryType`, `count`
  请求体：无
- `GET /api/u1/v1/tiktok/web/fetch_general_search`
  能力：搜索
  入参：query: `keyword*`, `offset`, `search_id`, `cookie`
  请求体：无
- `POST /api/u1/v1/tiktok/web/fetch_gift_name_by_id`
  能力：通用能力
  入参：无
  请求体：application/json: `gift_id*`:string
- `POST /api/u1/v1/tiktok/web/fetch_gift_names_by_ids`
  能力：通用能力
  入参：无
  请求体：application/json: `gift_ids*`[]
- `POST /api/u1/v1/tiktok/web/fetch_home_feed`
  能力：主页/账号
  入参：无
  请求体：application/json: `count`:integer, `cookie`:string
- `GET /api/u1/v1/tiktok/web/fetch_live_gift_list`
  能力：直播
  入参：query: `room_id`
  请求体：无
- `GET /api/u1/v1/tiktok/web/fetch_live_im_fetch`
  能力：直播
  入参：query: `room_id*`, `user_unique_id*`
  请求体：无
- `GET /api/u1/v1/tiktok/web/fetch_live_recommend`
  能力：直播
  入参：query: `related_live_tag*`
  请求体：无
- `GET /api/u1/v1/tiktok/web/fetch_post_comment`
  能力：评论 / 作品详情
  入参：query: `aweme_id*`, `cursor`, `count`, `current_region`
  请求体：无
- `GET /api/u1/v1/tiktok/web/fetch_post_comment_reply`
  能力：评论 / 评论回复 / 作品详情
  入参：query: `item_id*`, `comment_id*`, `cursor`, `count`, `current_region`
  请求体：无
- `GET /api/u1/v1/tiktok/web/fetch_post_detail`
  能力：作品详情 / 详情
  入参：query: `itemId*`
  请求体：无
- `GET /api/u1/v1/tiktok/web/fetch_post_detail_v2`
  能力：作品详情 / 详情
  入参：query: `itemId*`
  请求体：无
- `GET /api/u1/v1/tiktok/web/fetch_search_keyword_suggest`
  能力：搜索
  入参：query: `keyword*`
  请求体：无
- `GET /api/u1/v1/tiktok/web/fetch_search_live`
  能力：搜索 / 直播
  入参：query: `keyword*`, `count`, `offset`, `search_id`, `cookie`
  请求体：无
- `GET /api/u1/v1/tiktok/web/fetch_search_photo`
  能力：搜索 / 热点/榜单
  入参：query: `keyword*`, `count`, `offset`, `search_id`, `cookie`
  请求体：无
- `GET /api/u1/v1/tiktok/web/fetch_search_user`
  能力：搜索 / 主页/账号
  入参：query: `keyword*`, `cursor`, `search_id`, `cookie`
  请求体：无
- `GET /api/u1/v1/tiktok/web/fetch_search_video`
  能力：搜索 / 作品详情
  入参：query: `keyword*`, `count`, `offset`, `search_id`, `cookie`
  请求体：无
- `GET /api/u1/v1/tiktok/web/fetch_sso_login_auth`
  能力：通用能力
  入参：query: `device_id*`, `verifyFp*`, `region*`, `proxy*`
  请求体：无
- `GET /api/u1/v1/tiktok/web/fetch_sso_login_qrcode`
  能力：通用能力
  入参：query: `device_id*`, `region*`, `proxy*`
  请求体：无
- `GET /api/u1/v1/tiktok/web/fetch_sso_login_status`
  能力：通用能力
  入参：query: `token*`, `device_id*`, `verifyFp*`, `region*`, `proxy*`
  请求体：无
- `GET /api/u1/v1/tiktok/web/fetch_tag_detail`
  能力：详情
  入参：query: `tag_name*`
  请求体：无
- `GET /api/u1/v1/tiktok/web/fetch_tag_post`
  能力：作品详情
  入参：query: `challengeID*`, `count`, `cursor`
  请求体：无
- `GET /api/u1/v1/tiktok/web/fetch_tiktok_live_data`
  能力：直播
  入参：query: `live_room_url*`
  请求体：无
- `GET /api/u1/v1/tiktok/web/fetch_tiktok_web_guest_cookie`
  能力：通用能力
  入参：query: `user_agent*`
  请求体：无
- `GET /api/u1/v1/tiktok/web/fetch_trending_post`
  能力：热点/榜单 / 作品详情
  入参：无
  请求体：无
- `GET /api/u1/v1/tiktok/web/fetch_trending_searchwords`
  能力：搜索 / 热点/榜单
  入参：无
  请求体：无
- `GET /api/u1/v1/tiktok/web/fetch_user_collect`
  能力：主页/账号
  入参：query: `cookie*`, `secUid*`, `cursor`, `count`, `coverFormat`
  请求体：无
- `GET /api/u1/v1/tiktok/web/fetch_user_fans`
  能力：主页/账号
  入参：query: `secUid*`, `count`, `maxCursor`, `minCursor`
  请求体：无
- `GET /api/u1/v1/tiktok/web/fetch_user_follow`
  能力：主页/账号
  入参：query: `secUid*`, `count`, `maxCursor`, `minCursor`
  请求体：无
- `GET /api/u1/v1/tiktok/web/fetch_user_like`
  能力：主页/账号
  入参：query: `secUid*`, `cursor`, `count`, `coverFormat`, `post_item_list_request_type`
  请求体：无
- `GET /api/u1/v1/tiktok/web/fetch_user_live_detail`
  能力：主页/账号 / 详情 / 直播
  入参：query: `uniqueId*`
  请求体：无
- `GET /api/u1/v1/tiktok/web/fetch_user_mix`
  能力：主页/账号
  入参：query: `mixId*`, `cursor`, `count`
  请求体：无
- `GET /api/u1/v1/tiktok/web/fetch_user_play_list`
  能力：主页/账号
  入参：query: `secUid*`, `cursor`, `count`
  请求体：无
- `GET /api/u1/v1/tiktok/web/fetch_user_post`
  能力：主页/账号 / 作品详情
  入参：query: `secUid*`, `cursor`, `count`, `coverFormat`, `post_item_list_request_type`
  请求体：无
- `GET /api/u1/v1/tiktok/web/fetch_user_profile`
  能力：主页/账号
  入参：query: `uniqueId`, `secUid`
  请求体：无
- `GET /api/u1/v1/tiktok/web/fetch_user_repost`
  能力：主页/账号 / 作品详情
  入参：query: `secUid*`, `cursor`, `count`, `coverFormat`
  请求体：无
- `GET /api/u1/v1/tiktok/web/generate_fingerprint`
  能力：通用能力
  入参：query: `browser_type`
  请求体：无
- `GET /api/u1/v1/tiktok/web/generate_hashed_id`
  能力：通用能力
  入参：query: `email*`
  请求体：无
- `GET /api/u1/v1/tiktok/web/generate_real_msToken`
  能力：通用能力
  入参：query: `random_strData`, `browser_type`
  请求体：无
- `GET /api/u1/v1/tiktok/web/generate_ttwid`
  能力：通用能力
  入参：query: `user_agent`
  请求体：无
- `GET /api/u1/v1/tiktok/web/generate_webid`
  能力：通用能力
  入参：query: `cookie`, `user_agent`, `url`, `referer`, `user_unique_id`, `app_id`
  请求体：无
- `POST /api/u1/v1/tiktok/web/generate_xbogus`
  能力：通用能力
  入参：无
  请求体：application/json: `url*`:string, `user_agent*`:string
- `POST /api/u1/v1/tiktok/web/generate_xgnarly`
  能力：通用能力
  入参：无
  请求体：application/json: `url*`:string, `user_agent*`:string, `body`:string
- `POST /api/u1/v1/tiktok/web/generate_xgnarly_and_xbogus`
  能力：通用能力
  入参：无
  请求体：application/json: `url*`:string, `body`:string
- `POST /api/u1/v1/tiktok/web/get_all_aweme_id`
  能力：通用能力
  入参：无
  请求体：application/json: 动态对象
- `POST /api/u1/v1/tiktok/web/get_all_sec_user_id`
  能力：主页/账号
  入参：无
  请求体：application/json: 动态对象
- `POST /api/u1/v1/tiktok/web/get_all_unique_id`
  能力：通用能力
  入参：无
  请求体：application/json: 动态对象
- `GET /api/u1/v1/tiktok/web/get_aweme_id`
  能力：通用能力
  入参：query: `url*`
  请求体：无
- `GET /api/u1/v1/tiktok/web/get_live_room_id`
  能力：直播
  入参：query: `live_room_url*`
  请求体：无
- `GET /api/u1/v1/tiktok/web/get_sec_user_id`
  能力：主页/账号
  入参：query: `url*`
  请求体：无
- `GET /api/u1/v1/tiktok/web/get_unique_id`
  能力：通用能力
  入参：query: `url*`
  请求体：无
- `GET /api/u1/v1/tiktok/web/get_user_id`
  能力：主页/账号
  入参：query: `url*`
  请求体：无
- `GET /api/u1/v1/tiktok/web/tiktok_live_room`
  能力：直播
  入参：query: `live_room_url*`, `danmaku_type*`
  请求体：无

### `Toutiao-App-API`

- 路由数：`5`
- 标签说明：**(今日头条App数据接口/Toutiao-App-API data endpoints)**
- 常见入参：`group_id`, `offset`, `user_profile_url`, `user_id`

- `GET /api/u1/v1/toutiao/app/get_article_info`
  能力：作品详情
  入参：query: `group_id*`
  请求体：无
- `GET /api/u1/v1/toutiao/app/get_comments`
  能力：评论
  入参：query: `group_id*`, `offset*`
  请求体：无
- `GET /api/u1/v1/toutiao/app/get_user_id`
  能力：主页/账号
  入参：query: `user_profile_url*`
  请求体：无
- `GET /api/u1/v1/toutiao/app/get_user_info`
  能力：主页/账号
  入参：query: `user_id*`
  请求体：无
- `GET /api/u1/v1/toutiao/app/get_video_info`
  能力：作品详情
  入参：query: `group_id*`
  请求体：无

### `Toutiao-Web-API`

- 路由数：`2`
- 标签说明：**(今日头条Web数据接口/Toutiao-Web-API data endpoints)**
- 常见入参：`aweme_id`

- `GET /api/u1/v1/toutiao/web/get_article_info`
  能力：作品详情
  入参：query: `aweme_id*`
  请求体：无
- `GET /api/u1/v1/toutiao/web/get_video_info`
  能力：作品详情
  入参：query: `aweme_id*`
  请求体：无

### `Twitter-Web-API`

- 路由数：`13`
- 标签说明：**(Twitter Web数据接口/Twitter-Web-API endpoints)**
- 常见入参：`cursor`, `screen_name`, `tweet_id`, `rest_id`, `keyword`, `search_type`, `country`, `userId`, `count`

- `GET /api/u1/v1/twitter/web/fetch_latest_post_comments`
  能力：评论 / 作品详情
  入参：query: `tweet_id*`, `cursor`
  请求体：无
- `GET /api/u1/v1/twitter/web/fetch_post_comments`
  能力：评论 / 作品详情
  入参：query: `tweet_id*`, `cursor`
  请求体：无
- `GET /api/u1/v1/twitter/web/fetch_retweet_user_list`
  能力：主页/账号
  入参：query: `tweet_id*`, `cursor`
  请求体：无
- `GET /api/u1/v1/twitter/web/fetch_search_timeline`
  能力：搜索
  入参：query: `keyword*`, `search_type`, `cursor`
  请求体：无
- `GET /api/u1/v1/twitter/web/fetch_trending`
  能力：热点/榜单
  入参：query: `country`
  请求体：无
- `GET /api/u1/v1/twitter/web/fetch_tweet_detail`
  能力：详情
  入参：query: `tweet_id*`
  请求体：无
- `GET /api/u1/v1/twitter/web/fetch_user_followers`
  能力：主页/账号
  入参：query: `screen_name*`, `cursor`
  请求体：无
- `GET /api/u1/v1/twitter/web/fetch_user_followings`
  能力：主页/账号
  入参：query: `screen_name*`, `cursor`
  请求体：无
- `GET /api/u1/v1/twitter/web/fetch_user_highlights_tweets`
  能力：主页/账号
  入参：query: `userId*`, `count`, `cursor`
  请求体：无
- `GET /api/u1/v1/twitter/web/fetch_user_media`
  能力：主页/账号 / 下载/媒体
  入参：query: `screen_name*`, `rest_id`, `cursor`
  请求体：无
- `GET /api/u1/v1/twitter/web/fetch_user_post_tweet`
  能力：主页/账号 / 作品详情
  入参：query: `screen_name`, `rest_id`, `cursor`
  请求体：无
- `GET /api/u1/v1/twitter/web/fetch_user_profile`
  能力：主页/账号
  入参：query: `screen_name`, `rest_id`
  请求体：无
- `GET /api/u1/v1/twitter/web/fetch_user_tweet_replies`
  能力：主页/账号
  入参：query: `screen_name*`, `cursor`
  请求体：无

### `WeChat-Channels-API`

- 路由数：`9`
- 标签说明：**(微信视频号数据接口/WeChat-Channels-API data endpoints)**
- 常见入参：`keywords`, `id`, `username`, `lastBuffer`, `comment_id`, `session_buffer`, `last_buffer`, `page`, `exportId`

- `POST /api/u1/v1/wechat_channels/fetch_comments`
  能力：评论 / 主页/账号
  入参：无
  请求体：application/json: `id*`:string, `lastBuffer`:string, `comment_id`:string
- `POST /api/u1/v1/wechat_channels/fetch_default_search`
  能力：搜索 / 主页/账号
  入参：无
  请求体：application/json: `keywords*`:string, `session_buffer`:string
- `POST /api/u1/v1/wechat_channels/fetch_home_page`
  能力：主页/账号
  入参：无
  请求体：application/json: `username*`:string, `last_buffer`:string
- `GET /api/u1/v1/wechat_channels/fetch_hot_words`
  能力：热点/榜单 / 主页/账号
  入参：无
  请求体：无
- `GET /api/u1/v1/wechat_channels/fetch_live_history`
  能力：主页/账号 / 直播
  入参：query: `username*`
  请求体：无
- `GET /api/u1/v1/wechat_channels/fetch_search_latest`
  能力：搜索 / 主页/账号
  入参：query: `keywords*`
  请求体：无
- `GET /api/u1/v1/wechat_channels/fetch_search_ordinary`
  能力：搜索 / 主页/账号
  入参：query: `keywords*`
  请求体：无
- `GET /api/u1/v1/wechat_channels/fetch_user_search`
  能力：搜索 / 主页/账号
  入参：query: `keywords*`, `page`
  请求体：无
- `GET /api/u1/v1/wechat_channels/fetch_video_detail`
  能力：主页/账号 / 作品详情 / 详情
  入参：query: `id`, `exportId`
  请求体：无

### `WeChat-Media-Platform-Web-API`

- 路由数：`10`
- 标签说明：**(微信公众号Web数据接口/WeChat-Media-Platform-Web-API data endpoints)**
- 常见入参：`url`, `comment_id`, `offset`, `buffer`, `content_id`, `ghid`, `sogou_url`

- `GET /api/u1/v1/wechat_mp/web/fetch_mp_article_ad`
  能力：作品详情
  入参：query: `url*`
  请求体：无
- `GET /api/u1/v1/wechat_mp/web/fetch_mp_article_comment_list`
  能力：评论 / 作品详情
  入参：query: `url*`, `comment_id`, `buffer`
  请求体：无
- `GET /api/u1/v1/wechat_mp/web/fetch_mp_article_comment_reply_list`
  能力：评论 / 评论回复 / 作品详情
  入参：query: `url`, `comment_id*`, `content_id*`, `offset`
  请求体：无
- `GET /api/u1/v1/wechat_mp/web/fetch_mp_article_detail_html`
  能力：作品详情 / 详情
  入参：query: `url*`
  请求体：无
- `GET /api/u1/v1/wechat_mp/web/fetch_mp_article_detail_json`
  能力：作品详情 / 详情
  入参：query: `url*`
  请求体：无
- `GET /api/u1/v1/wechat_mp/web/fetch_mp_article_list`
  能力：作品详情
  入参：query: `ghid*`, `offset`
  请求体：无
- `GET /api/u1/v1/wechat_mp/web/fetch_mp_article_read_count`
  能力：作品详情 / 广告
  入参：query: `url*`, `comment_id*`
  请求体：无
- `GET /api/u1/v1/wechat_mp/web/fetch_mp_article_url`
  能力：作品详情
  入参：query: `sogou_url*`
  请求体：无
- `GET /api/u1/v1/wechat_mp/web/fetch_mp_article_url_conversion`
  能力：作品详情
  入参：query: `url*`
  请求体：无
- `GET /api/u1/v1/wechat_mp/web/fetch_mp_related_articles`
  能力：作品详情
  入参：query: `url*`
  请求体：无

### `Weibo-App-API`

- 路由数：`20`
- 标签说明：**(新浪微博APP数据接口/Weibo-App-API data endpoints)**
- 常见入参：`uid`, `page`, `since_id`, `status_id`, `query`, `count`, `max_id`, `category`, `search_type`, `sort_type`

- `GET /api/u1/v1/weibo/app/fetch_ai_smart_search`
  能力：搜索
  入参：query: `query*`, `page`
  请求体：无
- `GET /api/u1/v1/weibo/app/fetch_home_recommend_feed`
  能力：主页/账号
  入参：query: `page`, `count`
  请求体：无
- `GET /api/u1/v1/weibo/app/fetch_hot_search`
  能力：搜索 / 热点/榜单
  入参：query: `category`, `page`, `count`
  请求体：无
- `GET /api/u1/v1/weibo/app/fetch_hot_search_categories`
  能力：搜索 / 热点/榜单
  入参：无
  请求体：无
- `GET /api/u1/v1/weibo/app/fetch_search_all`
  能力：搜索
  入参：query: `query*`, `page`, `search_type`
  请求体：无
- `GET /api/u1/v1/weibo/app/fetch_status_comments`
  能力：评论
  入参：query: `status_id*`, `max_id`, `sort_type`
  请求体：无
- `GET /api/u1/v1/weibo/app/fetch_status_detail`
  能力：详情
  入参：query: `status_id*`
  请求体：无
- `GET /api/u1/v1/weibo/app/fetch_status_likes`
  能力：通用能力
  入参：query: `status_id*`, `attitude_type`
  请求体：无
- `GET /api/u1/v1/weibo/app/fetch_status_reposts`
  能力：作品详情
  入参：query: `status_id*`, `max_id`
  请求体：无
- `GET /api/u1/v1/weibo/app/fetch_user_album`
  能力：主页/账号
  入参：query: `uid*`, `since_id`
  请求体：无
- `GET /api/u1/v1/weibo/app/fetch_user_articles`
  能力：主页/账号 / 作品详情
  入参：query: `uid*`, `since_id`
  请求体：无
- `GET /api/u1/v1/weibo/app/fetch_user_audios`
  能力：主页/账号 / 音频/媒体
  入参：query: `uid*`, `since_id`
  请求体：无
- `GET /api/u1/v1/weibo/app/fetch_user_info`
  能力：主页/账号
  入参：query: `uid*`
  请求体：无
- `GET /api/u1/v1/weibo/app/fetch_user_info_detail`
  能力：主页/账号 / 详情
  入参：query: `uid*`
  请求体：无
- `GET /api/u1/v1/weibo/app/fetch_user_profile_feed`
  能力：主页/账号
  入参：query: `uid*`, `since_id`
  请求体：无
- `GET /api/u1/v1/weibo/app/fetch_user_super_topics`
  能力：主页/账号 / 话题
  入参：query: `uid*`, `page`
  请求体：无
- `GET /api/u1/v1/weibo/app/fetch_user_timeline`
  能力：主页/账号
  入参：query: `uid*`, `page`, `filter_type`, `month`
  请求体：无
- `GET /api/u1/v1/weibo/app/fetch_user_videos`
  能力：主页/账号 / 作品详情
  入参：query: `uid*`, `since_id`
  请求体：无
- `GET /api/u1/v1/weibo/app/fetch_video_detail`
  能力：作品详情 / 详情
  入参：query: `mid*`
  请求体：无
- `GET /api/u1/v1/weibo/app/fetch_video_featured_feed`
  能力：作品详情
  入参：query: `page`
  请求体：无

### `Weibo-Web-API`

- 路由数：`11`
- 标签说明：**(新浪微博Web数据接口/Weibo-Web-API data endpoints)**
- 常见入参：`page`, `max_id`, `post_id`, `uid`, `channel_name`, `cid`, `mid`, `max_id_type`, `keyword`, `search_type`

- `GET /api/u1/v1/weibo/web/fetch_channel_feed`
  能力：主页/账号
  入参：query: `channel_name`, `page`
  请求体：无
- `GET /api/u1/v1/weibo/web/fetch_comment_replies`
  能力：评论
  入参：query: `cid*`, `max_id`
  请求体：无
- `GET /api/u1/v1/weibo/web/fetch_config_list`
  能力：通用能力
  入参：无
  请求体：无
- `GET /api/u1/v1/weibo/web/fetch_hot_search`
  能力：搜索 / 热点/榜单
  入参：无
  请求体：无
- `GET /api/u1/v1/weibo/web/fetch_post_comments`
  能力：评论 / 作品详情
  入参：query: `post_id*`, `mid*`, `max_id`, `max_id_type`
  请求体：无
- `GET /api/u1/v1/weibo/web/fetch_post_detail`
  能力：作品详情 / 详情
  入参：query: `post_id*`
  请求体：无
- `GET /api/u1/v1/weibo/web/fetch_search`
  能力：搜索
  入参：query: `keyword*`, `page`, `search_type`, `time_scope`
  请求体：无
- `GET /api/u1/v1/weibo/web/fetch_search_topics`
  能力：搜索 / 话题
  入参：无
  请求体：无
- `GET /api/u1/v1/weibo/web/fetch_trend_top`
  能力：热点/榜单
  入参：query: `containerid*`, `page`
  请求体：无
- `GET /api/u1/v1/weibo/web/fetch_user_info`
  能力：主页/账号
  入参：query: `uid*`
  请求体：无
- `GET /api/u1/v1/weibo/web/fetch_user_posts`
  能力：主页/账号 / 作品详情
  入参：query: `uid*`, `page`, `since_id`
  请求体：无

### `Weibo-Web-V2-API`

- 路由数：`33`
- 标签说明：**(新浪微博 Web V2 数据接口/Weibo-Web-V2-API data endpoints)**
- 常见入参：`page`, `uid`, `query`, `id`, `max_id`, `count`, `since_id`, `q`, `keyword`, `cursor`

- `GET /api/u1/v1/weibo/web_v2/check_allow_comment_with_pic`
  能力：评论
  入参：query: `id*`
  请求体：无
- `GET /api/u1/v1/weibo/web_v2/fetch_advanced_search`
  能力：搜索
  入参：query: `q*`, `search_type`, `include_type`, `timescope`, `page`
  请求体：无
- `GET /api/u1/v1/weibo/web_v2/fetch_ai_related_search`
  能力：搜索
  入参：query: `keyword*`
  请求体：无
- `GET /api/u1/v1/weibo/web_v2/fetch_ai_search`
  能力：搜索
  入参：query: `query*`
  请求体：无
- `GET /api/u1/v1/weibo/web_v2/fetch_all_groups`
  能力：通用能力
  入参：无
  请求体：无
- `GET /api/u1/v1/weibo/web_v2/fetch_city_list`
  能力：通用能力
  入参：query: `normalized`
  请求体：无
- `GET /api/u1/v1/weibo/web_v2/fetch_entertainment_ranking`
  能力：通用能力
  入参：无
  请求体：无
- `GET /api/u1/v1/weibo/web_v2/fetch_hot_ranking_timeline`
  能力：热点/榜单
  入参：query: `ranking_type*`, `since_id`, `max_id`, `count`
  请求体：无
- `GET /api/u1/v1/weibo/web_v2/fetch_hot_search`
  能力：搜索 / 热点/榜单
  入参：无
  请求体：无
- `GET /api/u1/v1/weibo/web_v2/fetch_hot_search_index`
  能力：搜索 / 热点/榜单
  入参：无
  请求体：无
- `GET /api/u1/v1/weibo/web_v2/fetch_hot_search_summary`
  能力：搜索 / 热点/榜单
  入参：无
  请求体：无
- `GET /api/u1/v1/weibo/web_v2/fetch_life_ranking`
  能力：通用能力
  入参：无
  请求体：无
- `GET /api/u1/v1/weibo/web_v2/fetch_pic_search`
  能力：搜索
  入参：query: `query*`, `page`
  请求体：无
- `GET /api/u1/v1/weibo/web_v2/fetch_post_comments`
  能力：评论 / 作品详情
  入参：query: `id*`, `count`, `max_id`
  请求体：无
- `GET /api/u1/v1/weibo/web_v2/fetch_post_detail`
  能力：作品详情 / 详情
  入参：query: `id*`, `is_get_long_text`
  请求体：无
- `GET /api/u1/v1/weibo/web_v2/fetch_post_sub_comments`
  能力：评论 / 作品详情
  入参：query: `id*`, `count`, `max_id`
  请求体：无
- `GET /api/u1/v1/weibo/web_v2/fetch_realtime_search`
  能力：搜索
  入参：query: `query*`, `page`
  请求体：无
- `GET /api/u1/v1/weibo/web_v2/fetch_similar_search`
  能力：搜索
  入参：query: `keyword*`
  请求体：无
- `GET /api/u1/v1/weibo/web_v2/fetch_social_ranking`
  能力：通用能力
  入参：无
  请求体：无
- `GET /api/u1/v1/weibo/web_v2/fetch_topic_search`
  能力：搜索 / 话题
  入参：query: `query*`, `page`
  请求体：无
- `GET /api/u1/v1/weibo/web_v2/fetch_user_basic_info`
  能力：主页/账号
  入参：query: `uid*`
  请求体：无
- `GET /api/u1/v1/weibo/web_v2/fetch_user_fans`
  能力：主页/账号
  入参：query: `uid*`, `page`
  请求体：无
- `GET /api/u1/v1/weibo/web_v2/fetch_user_following`
  能力：主页/账号
  入参：query: `uid*`, `page`
  请求体：无
- `GET /api/u1/v1/weibo/web_v2/fetch_user_info`
  能力：主页/账号
  入参：query: `uid`, `custom`
  请求体：无
- `GET /api/u1/v1/weibo/web_v2/fetch_user_original_posts`
  能力：主页/账号 / 作品详情
  入参：query: `uid*`, `page`, `since_id`
  请求体：无
- `GET /api/u1/v1/weibo/web_v2/fetch_user_posts`
  能力：主页/账号 / 作品详情
  入参：query: `uid*`, `page`, `feature`, `since_id`
  请求体：无
- `GET /api/u1/v1/weibo/web_v2/fetch_user_recommend_timeline`
  能力：主页/账号
  入参：query: `refresh`, `group_id`, `containerid`, `extparam`, `max_id`, `count`
  请求体：无
- `GET /api/u1/v1/weibo/web_v2/fetch_user_search`
  能力：搜索 / 主页/账号
  入参：query: `query`, `page`, `region`, `auth`, `gender`, `age`, `nickname`, `tag`, `school`, `work`
  请求体：无
- `GET /api/u1/v1/weibo/web_v2/fetch_user_video_collection_detail`
  能力：主页/账号 / 作品详情 / 详情
  入参：query: `cid*`, `cursor`, `tab_code`
  请求体：无
- `GET /api/u1/v1/weibo/web_v2/fetch_user_video_collection_list`
  能力：主页/账号 / 作品详情
  入参：query: `uid*`
  请求体：无
- `GET /api/u1/v1/weibo/web_v2/fetch_user_video_list`
  能力：主页/账号 / 作品详情
  入参：query: `uid*`, `cursor`
  请求体：无
- `GET /api/u1/v1/weibo/web_v2/fetch_video_search`
  能力：搜索 / 作品详情
  入参：query: `query*`, `mode`, `page`
  请求体：无
- `GET /api/u1/v1/weibo/web_v2/search_user_posts`
  能力：搜索 / 主页/账号 / 作品详情
  入参：query: `uid*`, `q*`, `page`, `starttime*`, `endtime*`, `hasori`, `hasret`, `hastext`, `haspic`, `hasvideo`, `hasmusic`
  请求体：无

### `Xiaohongshu-App-API`

- 路由数：`12`
- 标签说明：**(小红书App数据接口/Xiaohongshu-App-API data endpoints)** - 第二优先/Second choice
- 常见入参：`note_id`, `session_id`, `share_link`, `start`, `share_text`, `sort`, `user_id`, `keyword`, `page`, `search_id`

- `GET /api/u1/v1/xiaohongshu/app/extract_share_info`
  能力：通用能力
  入参：query: `share_link*`
  请求体：无
- `GET /api/u1/v1/xiaohongshu/app/get_note_comments`
  能力：评论 / 作品详情
  入参：query: `note_id*`, `start`, `sort_strategy`
  请求体：无
- `GET /api/u1/v1/xiaohongshu/app/get_note_info`
  能力：作品详情
  入参：query: `note_id`, `share_text`
  请求体：无
- `GET /api/u1/v1/xiaohongshu/app/get_note_info_v2`
  能力：作品详情
  入参：query: `note_id`, `share_text`
  请求体：无
- `GET /api/u1/v1/xiaohongshu/app/get_notes_by_topic`
  能力：作品详情 / 话题
  入参：query: `page_id*`, `first_load_time*`, `sort`, `session_id`, `last_note_ct`, `last_note_id`, `cursor_score`
  请求体：无
- `GET /api/u1/v1/xiaohongshu/app/get_product_detail`
  能力：详情 / 电商
  入参：query: `sku_id*`
  请求体：无
- `GET /api/u1/v1/xiaohongshu/app/get_sub_comments`
  能力：评论
  入参：query: `note_id*`, `comment_id*`, `start`
  请求体：无
- `GET /api/u1/v1/xiaohongshu/app/get_user_id_and_xsec_token`
  能力：主页/账号
  入参：query: `share_link*`
  请求体：无
- `GET /api/u1/v1/xiaohongshu/app/get_user_info`
  能力：主页/账号
  入参：query: `user_id*`
  请求体：无
- `GET /api/u1/v1/xiaohongshu/app/get_user_notes`
  能力：主页/账号 / 作品详情
  入参：query: `user_id*`, `cursor`
  请求体：无
- `GET /api/u1/v1/xiaohongshu/app/search_notes`
  能力：搜索 / 作品详情
  入参：query: `keyword*`, `page*`, `search_id`, `session_id`, `sort_type`, `filter_note_type`, `filter_note_time`
  请求体：无
- `GET /api/u1/v1/xiaohongshu/app/search_products`
  能力：搜索 / 电商
  入参：query: `keyword*`, `page*`, `search_id`, `session_id`, `sort`, `scope`, `service_guarantee`, `min_price`, `max_price`, `super_promotion`
  请求体：无

### `Xiaohongshu-App-V2-API`

- 路由数：`21`
- 标签说明：**(小红书App V2数据接口/Xiaohongshu-App-V2-API data endpoints)** ⭐ 推荐优先使用/Recommended first choice - 稳定性最高、功能最全/Most stable and feature-rich
- 常见入参：`source`, `share_text`, `cursor`, `note_id`, `page`, `keyword`, `search_id`, `sku_id`, `user_id`, `tab`

- `GET /api/u1/v1/xiaohongshu/app_v2/get_creator_hot_inspiration_feed`
  能力：热点/榜单 / 创作者
  入参：query: `cursor`
  请求体：无
- `GET /api/u1/v1/xiaohongshu/app_v2/get_creator_inspiration_feed`
  能力：创作者
  入参：query: `cursor`, `tab`, `source`
  请求体：无
- `GET /api/u1/v1/xiaohongshu/app_v2/get_image_note_detail`
  能力：作品详情 / 详情
  入参：query: `note_id`, `share_text`
  请求体：无
- `GET /api/u1/v1/xiaohongshu/app_v2/get_mixed_note_detail`
  能力：作品详情 / 详情
  入参：query: `note_id`, `share_text`
  请求体：无
- `GET /api/u1/v1/xiaohongshu/app_v2/get_note_comments`
  能力：评论 / 作品详情
  入参：query: `note_id`, `share_text`, `cursor`, `index`, `sort_strategy`
  请求体：无
- `GET /api/u1/v1/xiaohongshu/app_v2/get_note_sub_comments`
  能力：评论 / 作品详情
  入参：query: `note_id`, `share_text`, `comment_id*`, `cursor`, `index`
  请求体：无
- `GET /api/u1/v1/xiaohongshu/app_v2/get_product_detail`
  能力：详情 / 电商
  入参：query: `sku_id*`, `source`, `pre_page`
  请求体：无
- `GET /api/u1/v1/xiaohongshu/app_v2/get_product_recommendations`
  能力：电商
  入参：query: `sku_id*`, `cursor_score`, `region`
  请求体：无
- `GET /api/u1/v1/xiaohongshu/app_v2/get_product_review_overview`
  能力：电商
  入参：query: `sku_id*`, `tab`
  请求体：无
- `GET /api/u1/v1/xiaohongshu/app_v2/get_product_reviews`
  能力：电商
  入参：query: `sku_id*`, `page`, `sort_strategy_type`, `share_pics_only`, `from_page`
  请求体：无
- `GET /api/u1/v1/xiaohongshu/app_v2/get_topic_feed`
  能力：话题
  入参：query: `page_id*`, `sort`, `cursor_score`, `last_note_id`, `last_note_ct`, `session_id`, `first_load_time`, `source`
  请求体：无
- `GET /api/u1/v1/xiaohongshu/app_v2/get_topic_info`
  能力：话题
  入参：query: `page_id*`, `source`, `note_id`
  请求体：无
- `GET /api/u1/v1/xiaohongshu/app_v2/get_user_faved_notes`
  能力：主页/账号 / 作品详情
  入参：query: `user_id`, `share_text`, `cursor`
  请求体：无
- `GET /api/u1/v1/xiaohongshu/app_v2/get_user_info`
  能力：主页/账号
  入参：query: `user_id`, `share_text`
  请求体：无
- `GET /api/u1/v1/xiaohongshu/app_v2/get_user_posted_notes`
  能力：主页/账号 / 作品详情
  入参：query: `user_id`, `share_text`, `cursor`
  请求体：无
- `GET /api/u1/v1/xiaohongshu/app_v2/get_video_note_detail`
  能力：作品详情 / 详情
  入参：query: `note_id`, `share_text`
  请求体：无
- `GET /api/u1/v1/xiaohongshu/app_v2/search_groups`
  能力：搜索
  入参：query: `keyword*`, `page_no`, `search_id`, `source`, `is_recommend`
  请求体：无
- `GET /api/u1/v1/xiaohongshu/app_v2/search_images`
  能力：搜索
  入参：query: `keyword*`, `page`, `search_id`, `search_session_id`, `word_request_id`, `source`
  请求体：无
- `GET /api/u1/v1/xiaohongshu/app_v2/search_notes`
  能力：搜索 / 作品详情
  入参：query: `keyword*`, `page`, `sort_type`, `note_type`, `time_filter`, `search_id`, `search_session_id`, `source`, `ai_mode`
  请求体：无
- `GET /api/u1/v1/xiaohongshu/app_v2/search_products`
  能力：搜索 / 电商
  入参：query: `keyword*`, `page`, `search_id`, `source`
  请求体：无
- `GET /api/u1/v1/xiaohongshu/app_v2/search_users`
  能力：搜索 / 主页/账号
  入参：query: `keyword*`, `page`, `search_id`, `source`
  请求体：无

### `Xiaohongshu-Web-API`

- 路由数：`17`
- 标签说明：**(小红书Web数据接口/Xiaohongshu-Web-API data endpoints)** - 第四优先/Fourth choice
- 常见入参：`note_id`, `share_text`, `cookie`, `proxy`, `lastCursor`, `user_id`, `keyword`, `page`, `xsec_token`, `sort`

- `POST /api/u1/v1/xiaohongshu/web/get_home_recommend`
  能力：主页/账号
  入参：无
  请求体：application/json: `feed_type`:string, `need_filter_image`:boolean, `cursor_score`:string, `cookie`:string, `proxy`:string
- `GET /api/u1/v1/xiaohongshu/web/get_note_comment_replies`
  能力：评论 / 作品详情
  入参：query: `note_id*`, `comment_id*`, `lastCursor`
  请求体：无
- `GET /api/u1/v1/xiaohongshu/web/get_note_comments`
  能力：评论 / 作品详情
  入参：query: `note_id*`, `lastCursor`
  请求体：无
- `GET /api/u1/v1/xiaohongshu/web/get_note_id_and_xsec_token`
  能力：作品详情
  入参：query: `share_text*`
  请求体：无
- `GET /api/u1/v1/xiaohongshu/web/get_note_info_v2`
  能力：作品详情
  入参：query: `note_id`, `share_text`
  请求体：无
- `GET /api/u1/v1/xiaohongshu/web/get_note_info_v4`
  能力：作品详情
  入参：query: `note_id`, `share_text`
  请求体：无
- `POST /api/u1/v1/xiaohongshu/web/get_note_info_v5`
  能力：作品详情
  入参：无
  请求体：application/json: `note_id`:string, `xsec_token`:string, `cookie`:string, `proxy`:string
- `GET /api/u1/v1/xiaohongshu/web/get_note_info_v7`
  能力：作品详情
  入参：query: `note_id`, `share_text`
  请求体：无
- `GET /api/u1/v1/xiaohongshu/web/get_product_info`
  能力：电商
  入参：query: `share_text`, `item_id`, `xsec_token`
  请求体：无
- `GET /api/u1/v1/xiaohongshu/web/get_user_info`
  能力：主页/账号
  入参：query: `user_id*`
  请求体：无
- `GET /api/u1/v1/xiaohongshu/web/get_user_info_v2`
  能力：主页/账号
  入参：query: `user_id`, `share_text`
  请求体：无
- `GET /api/u1/v1/xiaohongshu/web/get_user_notes_v2`
  能力：主页/账号 / 作品详情
  入参：query: `user_id*`, `lastCursor`
  请求体：无
- `GET /api/u1/v1/xiaohongshu/web/get_visitor_cookie`
  能力：通用能力
  入参：query: `proxy`
  请求体：无
- `GET /api/u1/v1/xiaohongshu/web/search_notes`
  能力：搜索 / 作品详情
  入参：query: `keyword*`, `page`, `sort`, `noteType`, `noteTime`
  请求体：无
- `GET /api/u1/v1/xiaohongshu/web/search_notes_v3`
  能力：搜索 / 作品详情
  入参：query: `keyword*`, `page`, `sort`, `noteType`, `noteTime`
  请求体：无
- `GET /api/u1/v1/xiaohongshu/web/search_users`
  能力：搜索 / 主页/账号
  入参：query: `keyword*`, `page`
  请求体：无
- `POST /api/u1/v1/xiaohongshu/web/sign`
  能力：通用能力
  入参：无
  请求体：application/json: `path`:string, `data`{...}, `cookie`:string

### `Xiaohongshu-Web-V2-API`

- 路由数：`18`
- 标签说明：**(小红书Web V2数据接口/Xiaohongshu-Web-V2-API data endpoints)** - 第三优先/Third choice
- 常见入参：`note_id`, `user_id`, `cursor`, `page`, `keywords`, `short_url`, `sort_type`, `note_type`, `comment_id`

- `GET /api/u1/v1/xiaohongshu/web_v2/fetch_feed_notes`
  能力：作品详情
  入参：query: `note_id*`
  请求体：无
- `GET /api/u1/v1/xiaohongshu/web_v2/fetch_feed_notes_v2`
  能力：作品详情
  入参：query: `note_id*`
  请求体：无
- `GET /api/u1/v1/xiaohongshu/web_v2/fetch_feed_notes_v3`
  能力：作品详情
  入参：query: `short_url*`
  请求体：无
- `GET /api/u1/v1/xiaohongshu/web_v2/fetch_feed_notes_v4`
  能力：作品详情
  入参：query: `note_id*`
  请求体：无
- `GET /api/u1/v1/xiaohongshu/web_v2/fetch_feed_notes_v5`
  能力：作品详情
  入参：query: `note_id*`
  请求体：无
- `GET /api/u1/v1/xiaohongshu/web_v2/fetch_follower_list`
  能力：通用能力
  入参：query: `user_id*`, `cursor`
  请求体：无
- `GET /api/u1/v1/xiaohongshu/web_v2/fetch_following_list`
  能力：通用能力
  入参：query: `user_id*`, `cursor`
  请求体：无
- `GET /api/u1/v1/xiaohongshu/web_v2/fetch_home_notes`
  能力：主页/账号 / 作品详情
  入参：query: `user_id*`, `cursor`
  请求体：无
- `GET /api/u1/v1/xiaohongshu/web_v2/fetch_home_notes_app`
  能力：主页/账号 / 作品详情
  入参：query: `user_id*`, `cursor`
  请求体：无
- `GET /api/u1/v1/xiaohongshu/web_v2/fetch_hot_list`
  能力：热点/榜单
  入参：无
  请求体：无
- `GET /api/u1/v1/xiaohongshu/web_v2/fetch_note_comments`
  能力：评论 / 作品详情
  入参：query: `note_id*`, `cursor`
  请求体：无
- `GET /api/u1/v1/xiaohongshu/web_v2/fetch_note_image`
  能力：作品详情
  入参：query: `note_id*`
  请求体：无
- `GET /api/u1/v1/xiaohongshu/web_v2/fetch_product_list`
  能力：电商
  入参：query: `user_id*`, `page`
  请求体：无
- `GET /api/u1/v1/xiaohongshu/web_v2/fetch_search_notes`
  能力：搜索 / 作品详情
  入参：query: `keywords*`, `page`, `sort_type`, `note_type`
  请求体：无
- `GET /api/u1/v1/xiaohongshu/web_v2/fetch_search_users`
  能力：搜索 / 主页/账号
  入参：query: `keywords*`, `page`
  请求体：无
- `GET /api/u1/v1/xiaohongshu/web_v2/fetch_sub_comments`
  能力：评论
  入参：query: `note_id*`, `comment_id*`, `cursor`
  请求体：无
- `GET /api/u1/v1/xiaohongshu/web_v2/fetch_user_info`
  能力：主页/账号
  入参：query: `user_id*`
  请求体：无
- `GET /api/u1/v1/xiaohongshu/web_v2/fetch_user_info_app`
  能力：主页/账号
  入参：query: `user_id*`
  请求体：无

### `Xigua-App-V2-API`

- 路由数：`7`
- 标签说明：**(西瓜视频App V2数据接口/Xigua-App-V2-API data endpoints)**
- 常见入参：`item_id`, `user_id`, `offset`, `max_behot_time`, `count`, `keyword`, `order_type`, `min_duration`, `max_duration`

- `GET /api/u1/v1/xigua/app/v2/fetch_one_video`
  能力：作品详情
  入参：query: `item_id*`
  请求体：无
- `GET /api/u1/v1/xigua/app/v2/fetch_one_video_play_url`
  能力：作品详情
  入参：query: `item_id*`
  请求体：无
- `GET /api/u1/v1/xigua/app/v2/fetch_one_video_v2`
  能力：作品详情
  入参：query: `item_id*`
  请求体：无
- `GET /api/u1/v1/xigua/app/v2/fetch_user_info`
  能力：主页/账号
  入参：query: `user_id*`
  请求体：无
- `GET /api/u1/v1/xigua/app/v2/fetch_user_post_list`
  能力：主页/账号 / 作品详情
  入参：query: `user_id*`, `max_behot_time`
  请求体：无
- `GET /api/u1/v1/xigua/app/v2/fetch_video_comment_list`
  能力：评论 / 作品详情
  入参：query: `item_id*`, `offset`, `count`
  请求体：无
- `GET /api/u1/v1/xigua/app/v2/search_video`
  能力：搜索 / 作品详情
  入参：query: `keyword*`, `offset`, `order_type`, `min_duration`, `max_duration`
  请求体：无

### `YouTube-Web-API`

- 路由数：`21`
- 标签说明：**(YouTube Web数据接口/YouTube-Web-API endpoints)**
- 常见入参：`continuation_token`, `language_code`, `country_code`, `channel_id`, `video_id`, `need_format`, `search_query`, `sort_by`, `lang`, `time_zone`

- `GET /api/u1/v1/youtube/web/get_channel_description`
  能力：主页/账号
  入参：query: `channel_id`, `continuation_token`, `language_code`, `country_code`, `need_format`
  请求体：无
- `GET /api/u1/v1/youtube/web/get_channel_id`
  能力：主页/账号
  入参：query: `channel_name*`
  请求体：无
- `GET /api/u1/v1/youtube/web/get_channel_id_v2`
  能力：主页/账号
  入参：query: `channel_url*`
  请求体：无
- `GET /api/u1/v1/youtube/web/get_channel_info`
  能力：主页/账号
  入参：query: `channel_id*`
  请求体：无
- `GET /api/u1/v1/youtube/web/get_channel_short_videos`
  能力：主页/账号 / 作品详情
  入参：query: `channel_id*`, `continuation_token`
  请求体：无
- `GET /api/u1/v1/youtube/web/get_channel_url`
  能力：主页/账号
  入参：query: `channel_id*`
  请求体：无
- `GET /api/u1/v1/youtube/web/get_channel_videos`
  能力：主页/账号 / 作品详情
  入参：query: `channel_id*`, `continuation_token`
  请求体：无
- `GET /api/u1/v1/youtube/web/get_channel_videos_v2`
  能力：主页/账号 / 作品详情
  入参：query: `channel_id*`, `lang`, `sortBy`, `contentType`, `nextToken`
  请求体：无
- `GET /api/u1/v1/youtube/web/get_channel_videos_v3`
  能力：主页/账号 / 作品详情
  入参：query: `channel_id*`, `language_code`, `country_code`, `continuation_token`, `need_format`
  请求体：无
- `GET /api/u1/v1/youtube/web/get_general_search`
  能力：搜索
  入参：query: `search_query*`, `language_code`, `country_code`, `time_zone`, `upload_time`, `duration`, `content_type`, `feature`, `sort_by`, `continuation_token`
  请求体：无
- `GET /api/u1/v1/youtube/web/get_relate_video`
  能力：作品详情
  入参：query: `video_id*`, `continuation_token`
  请求体：无
- `GET /api/u1/v1/youtube/web/get_shorts_search`
  能力：搜索
  入参：query: `search_query*`, `language_code`, `country_code`, `time_zone`, `upload_time`, `sort_by`, `continuation_token`, `filter_mixed_content`
  请求体：无
- `GET /api/u1/v1/youtube/web/get_trending_videos`
  能力：热点/榜单 / 作品详情
  入参：query: `language_code`, `country_code`, `section`
  请求体：无
- `GET /api/u1/v1/youtube/web/get_video_comment_replies`
  能力：评论 / 作品详情
  入参：query: `continuation_token*`, `language_code`, `country_code`, `need_format`
  请求体：无
- `GET /api/u1/v1/youtube/web/get_video_comments`
  能力：评论 / 作品详情
  入参：query: `video_id*`, `language_code`, `country_code`, `sort_by`, `continuation_token`, `need_format`
  请求体：无
- `GET /api/u1/v1/youtube/web/get_video_info`
  能力：作品详情
  入参：query: `video_id*`, `url_access`, `lang`, `videos`, `audios`, `subtitles`, `related`
  请求体：无
- `GET /api/u1/v1/youtube/web/get_video_info_v2`
  能力：作品详情
  入参：query: `video_id*`
  请求体：无
- `GET /api/u1/v1/youtube/web/get_video_info_v3`
  能力：作品详情
  入参：query: `video_id*`, `language_code`
  请求体：无
- `GET /api/u1/v1/youtube/web/get_video_subtitles`
  能力：作品详情 / 字幕/转写
  入参：query: `subtitle_url*`, `format`, `fix_overlap`, `target_lang`
  请求体：无
- `GET /api/u1/v1/youtube/web/search_channel`
  能力：搜索 / 主页/账号
  入参：query: `channel_id*`, `search_query*`, `language_code`, `country_code`, `continuation_token`
  请求体：无
- `GET /api/u1/v1/youtube/web/search_video`
  能力：搜索 / 作品详情
  入参：query: `search_query*`, `language_code`, `order_by`, `country_code`, `continuation_token`
  请求体：无

### `YouTube-Web-V2-API`

- 路由数：`16`
- 标签说明：**(YouTube Web V2数据接口/YouTube-Web-V2-API endpoints)**
- 常见入参：`continuation_token`, `need_format`, `language_code`, `country_code`, `video_id`, `channel_id`, `video_url`, `sort_by`, `channel_url`, `search_query`

- `GET /api/u1/v1/youtube/web_v2/get_channel_description`
  能力：主页/账号
  入参：query: `channel_id`, `continuation_token`, `language_code`, `country_code`, `need_format`
  请求体：无
- `GET /api/u1/v1/youtube/web_v2/get_channel_id`
  能力：主页/账号
  入参：query: `channel_url*`
  请求体：无
- `GET /api/u1/v1/youtube/web_v2/get_channel_shorts`
  能力：主页/账号
  入参：query: `channel_id`, `channel_url`, `continuation_token`, `need_format`
  请求体：无
- `GET /api/u1/v1/youtube/web_v2/get_channel_url`
  能力：主页/账号
  入参：query: `channel_id*`
  请求体：无
- `GET /api/u1/v1/youtube/web_v2/get_channel_videos`
  能力：主页/账号 / 作品详情
  入参：query: `channel_id*`, `language_code`, `country_code`, `continuation_token`, `need_format`
  请求体：无
- `GET /api/u1/v1/youtube/web_v2/get_general_search`
  能力：搜索
  入参：query: `search_query*`, `language_code`, `country_code`, `time_zone`, `upload_time`, `duration`, `content_type`, `feature`, `sort_by`, `continuation_token`
  请求体：无
- `GET /api/u1/v1/youtube/web_v2/get_related_videos`
  能力：作品详情
  入参：query: `video_id`, `video_url`, `need_format`
  请求体：无
- `GET /api/u1/v1/youtube/web_v2/get_search_suggestions`
  能力：搜索
  入参：query: `keyword*`, `language`, `region`
  请求体：无
- `GET /api/u1/v1/youtube/web_v2/get_shorts_search`
  能力：搜索
  入参：query: `search_query*`, `language_code`, `country_code`, `time_zone`, `upload_time`, `sort_by`, `continuation_token`, `filter_mixed_content`
  请求体：无
- `GET /api/u1/v1/youtube/web_v2/get_signed_stream_url`
  能力：直播
  入参：query: `video_id`, `video_url`, `itag*`
  请求体：无
- `GET /api/u1/v1/youtube/web_v2/get_video_comment_replies`
  能力：评论 / 作品详情
  入参：query: `continuation_token*`, `language_code`, `country_code`, `need_format`
  请求体：无
- `GET /api/u1/v1/youtube/web_v2/get_video_comments`
  能力：评论 / 作品详情
  入参：query: `video_id*`, `language_code`, `country_code`, `sort_by`, `continuation_token`, `need_format`
  请求体：无
- `GET /api/u1/v1/youtube/web_v2/get_video_info`
  能力：作品详情
  入参：query: `video_id*`, `language_code`, `need_format`
  请求体：无
- `GET /api/u1/v1/youtube/web_v2/get_video_streams`
  能力：作品详情 / 直播
  入参：query: `video_id`, `video_url`
  请求体：无
- `GET /api/u1/v1/youtube/web_v2/get_video_streams_v2`
  能力：作品详情 / 直播
  入参：query: `video_id`, `video_url`
  请求体：无
- `GET /api/u1/v1/youtube/web_v2/search_channels`
  能力：搜索 / 主页/账号
  入参：query: `keyword`, `continuation_token`, `need_format`
  请求体：无

### `Zhihu-Web-API`

- 路由数：`32`
- 标签说明：**(知乎Web数据接口/Zhihu-Web-API endpoints)**
- 常见入参：`offset`, `limit`, `keyword`, `user_url_token`, `search_hash_id`, `article_id`, `order_by`, `message_content`, `message_id`, `show_all_topics`

- `GET /api/u1/v1/zhihu/web/fetch_ai_search`
  能力：搜索
  入参：query: `message_content*`
  请求体：无
- `GET /api/u1/v1/zhihu/web/fetch_ai_search_result`
  能力：搜索
  入参：query: `message_id*`
  请求体：无
- `GET /api/u1/v1/zhihu/web/fetch_article_search_v3`
  能力：搜索 / 作品详情
  入参：query: `keyword*`, `offset`, `limit`, `show_all_topics`, `search_source`, `search_hash_id`, `vertical`, `sort`, `time_interval`, `vertical_info`
  请求体：无
- `GET /api/u1/v1/zhihu/web/fetch_column_article_detail`
  能力：作品详情 / 详情
  入参：query: `article_id*`
  请求体：无
- `GET /api/u1/v1/zhihu/web/fetch_column_articles`
  能力：作品详情
  入参：query: `column_id*`, `limit`, `offset`
  请求体：无
- `GET /api/u1/v1/zhihu/web/fetch_column_comment_config`
  能力：评论
  入参：query: `article_id*`
  请求体：无
- `GET /api/u1/v1/zhihu/web/fetch_column_recommend`
  能力：通用能力
  入参：query: `article_id*`, `limit`, `offset`
  请求体：无
- `GET /api/u1/v1/zhihu/web/fetch_column_relationship`
  能力：通用能力
  入参：query: `article_id*`
  请求体：无
- `GET /api/u1/v1/zhihu/web/fetch_column_search_v3`
  能力：搜索
  入参：query: `keyword*`, `offset`, `limit`, `search_hash_id`
  请求体：无
- `GET /api/u1/v1/zhihu/web/fetch_comment_v5`
  能力：评论
  入参：query: `answer_id*`, `order_by`, `limit`, `offset`
  请求体：无
- `GET /api/u1/v1/zhihu/web/fetch_ebook_search_v3`
  能力：搜索
  入参：query: `keyword*`, `offset`, `limit`, `search_hash_id`
  请求体：无
- `GET /api/u1/v1/zhihu/web/fetch_hot_list`
  能力：热点/榜单
  入参：query: `limit`, `desktop`
  请求体：无
- `GET /api/u1/v1/zhihu/web/fetch_hot_recommend`
  能力：热点/榜单
  入参：query: `offset`, `page_number`, `session_token`
  请求体：无
- `GET /api/u1/v1/zhihu/web/fetch_preset_search`
  能力：搜索
  入参：无
  请求体：无
- `GET /api/u1/v1/zhihu/web/fetch_question_answers`
  能力：通用能力
  入参：query: `question_id*`, `cursor`, `limit`, `offset`, `order`, `session_id`
  请求体：无
- `GET /api/u1/v1/zhihu/web/fetch_recommend_followees`
  能力：通用能力
  入参：无
  请求体：无
- `GET /api/u1/v1/zhihu/web/fetch_salt_search_v3`
  能力：搜索
  入参：query: `keyword*`, `offset`, `limit`, `search_hash_id`
  请求体：无
- `POST /api/u1/v1/zhihu/web/fetch_scholar_search_v3`
  能力：搜索
  入参：query: `keyword*`, `offset`, `limit`
  请求体：application/json: 动态对象
- `GET /api/u1/v1/zhihu/web/fetch_search_recommend`
  能力：搜索
  入参：无
  请求体：无
- `GET /api/u1/v1/zhihu/web/fetch_search_suggest`
  能力：搜索
  入参：query: `keyword*`
  请求体：无
- `GET /api/u1/v1/zhihu/web/fetch_sub_comment_v5`
  能力：评论
  入参：query: `comment_id*`, `order_by`, `limit`, `offset`
  请求体：无
- `GET /api/u1/v1/zhihu/web/fetch_topic_search_v3`
  能力：搜索 / 话题
  入参：query: `keyword*`, `offset`, `limit`
  请求体：无
- `GET /api/u1/v1/zhihu/web/fetch_user_follow_collections`
  能力：主页/账号
  入参：query: `user_url_token*`, `offset`, `limit`
  请求体：无
- `GET /api/u1/v1/zhihu/web/fetch_user_follow_columns`
  能力：主页/账号
  入参：query: `user_url_token*`, `offset`, `limit`
  请求体：无
- `GET /api/u1/v1/zhihu/web/fetch_user_follow_questions`
  能力：主页/账号
  入参：query: `user_url_token*`, `offset`, `limit`
  请求体：无
- `GET /api/u1/v1/zhihu/web/fetch_user_follow_topics`
  能力：主页/账号 / 话题
  入参：query: `user_url_token*`, `offset`, `limit`
  请求体：无
- `GET /api/u1/v1/zhihu/web/fetch_user_followees`
  能力：主页/账号
  入参：query: `user_url_token*`, `offset`, `limit`
  请求体：无
- `GET /api/u1/v1/zhihu/web/fetch_user_followers`
  能力：主页/账号
  入参：query: `user_url_token*`, `offset`, `limit`
  请求体：无
- `GET /api/u1/v1/zhihu/web/fetch_user_info`
  能力：主页/账号
  入参：query: `user_url_token*`
  请求体：无
- `GET /api/u1/v1/zhihu/web/fetch_user_search_v3`
  能力：搜索 / 主页/账号
  入参：query: `keyword*`, `offset`, `limit`
  请求体：无
- `GET /api/u1/v1/zhihu/web/fetch_video_list`
  能力：作品详情
  入参：query: `offset`, `limit`
  请求体：无
- `GET /api/u1/v1/zhihu/web/fetch_video_search_v3`
  能力：搜索 / 作品详情
  入参：query: `keyword*`, `limit`, `offset`, `search_hash_id`
  请求体：无

### `iOS-Shortcut`

- 路由数：`1`
- 标签说明：**(iOS快捷方式接口/iOS-Shortcut endpoints)**
- 常见入参：无

- `GET /api/u1/v1/ios_shortcut/shortcut`
  能力：通用能力
  入参：无
  请求体：无
