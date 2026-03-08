# Douyin-Billboard-API 路由详情

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 当前 tag 文件：`api-tags/douyin-billboard-api.md`
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T03:50:06+00:00`
- 路由数：`31`
- 常见能力：热点/榜单 / 搜索 / 话题 / 详情 / 评论 / 作品详情
- 常见入参：`page_size`, `date_window`, `page`, `keyword`, `tags`, `sec_uid`, `option`, `page_num`, `end_date`, `start_date`
- 标签说明：**(抖音热点榜数据接口/Douyin-Billboard-API data endpoints)**

## 路由列表

### `GET /api/u1/v1/douyin/billboard/fetch_city_list`

- 能力：热点/榜单
- 入参：无
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_city_list_api_v1_douyin_billboard_fetch_city_list_get`

### `GET /api/u1/v1/douyin/billboard/fetch_content_tag`

- 能力：热点/榜单
- 入参：无
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_content_tag_api_v1_douyin_billboard_fetch_content_tag_get`

### `GET /api/u1/v1/douyin/billboard/fetch_hot_account_fans_interest_account_list`

- 能力：热点/榜单
- 入参：query: `sec_uid*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_hot_account_fans_interest_account_list_api_v1_douyin_billboard_fetch_hot_account_fans_interest_account_list_get`

### `GET /api/u1/v1/douyin/billboard/fetch_hot_account_fans_interest_search_list`

- 能力：搜索 / 热点/榜单
- 入参：query: `sec_uid*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_hot_account_fans_interest_search_list_api_v1_douyin_billboard_fetch_hot_account_fans_interest_search_list_get`

### `GET /api/u1/v1/douyin/billboard/fetch_hot_account_fans_interest_topic_list`

- 能力：热点/榜单 / 话题
- 入参：query: `sec_uid*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_hot_account_fans_interest_topic_list_api_v1_douyin_billboard_fetch_hot_account_fans_interest_topic_list_get`

### `GET /api/u1/v1/douyin/billboard/fetch_hot_account_fans_portrait_list`

- 能力：热点/榜单
- 入参：query: `sec_uid*`, `option`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_hot_account_fans_portrait_list_api_v1_douyin_billboard_fetch_hot_account_fans_portrait_list_get`

### `GET /api/u1/v1/douyin/billboard/fetch_hot_account_item_analysis_list`

- 能力：热点/榜单
- 入参：query: `sec_uid*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_hot_account_item_analysis_list_api_v1_douyin_billboard_fetch_hot_account_item_analysis_list_get`

### `POST /api/u1/v1/douyin/billboard/fetch_hot_account_list`

- 能力：热点/榜单
- 入参：无
- 请求体：application/json: `date_window`:integer, `page_num`:integer, `page_size`:integer, `query_tag`{...}
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_hot_account_list_api_v1_douyin_billboard_fetch_hot_account_list_post`

### `GET /api/u1/v1/douyin/billboard/fetch_hot_account_search_list`

- 能力：搜索 / 热点/榜单
- 入参：query: `keyword*`, `cursor*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_hot_account_search_list_api_v1_douyin_billboard_fetch_hot_account_search_list_get`

### `GET /api/u1/v1/douyin/billboard/fetch_hot_account_trends_list`

- 能力：热点/榜单
- 入参：query: `sec_uid*`, `option`, `date_window`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_hot_account_trends_list_api_v1_douyin_billboard_fetch_hot_account_trends_list_get`

### `GET /api/u1/v1/douyin/billboard/fetch_hot_calendar_detail`

- 能力：热点/榜单 / 详情
- 入参：query: `calendar_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_hot_calendar_detail_api_v1_douyin_billboard_fetch_hot_calendar_detail_get`

### `POST /api/u1/v1/douyin/billboard/fetch_hot_calendar_list`

- 能力：热点/榜单
- 入参：无
- 请求体：application/json: `city_code`:string, `category_code`:string, `end_date`:integer, `start_date`:integer
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_hot_calendar_list_api_v1_douyin_billboard_fetch_hot_calendar_list_post`

### `GET /api/u1/v1/douyin/billboard/fetch_hot_category_list`

- 能力：热点/榜单
- 入参：query: `billboard_type*`, `snapshot_time`, `start_date`, `end_date`, `keyword`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_hot_category_list_api_v1_douyin_billboard_fetch_hot_category_list_get`

### `GET /api/u1/v1/douyin/billboard/fetch_hot_challenge_list`

- 能力：热点/榜单 / 话题
- 入参：query: `page*`, `page_size*`, `keyword`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_hot_challenge_list_api_v1_douyin_billboard_fetch_hot_challenge_list_get`

### `GET /api/u1/v1/douyin/billboard/fetch_hot_city_list`

- 能力：热点/榜单
- 入参：query: `page*`, `page_size*`, `order*`, `city_code`, `sentence_tag`, `keyword`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_hot_city_list_api_v1_douyin_billboard_fetch_hot_city_list_get`

### `GET /api/u1/v1/douyin/billboard/fetch_hot_comment_word_list`

- 能力：评论 / 热点/榜单
- 入参：query: `aweme_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_hot_comment_word_list_api_v1_douyin_billboard_fetch_hot_comment_word_list_get`

### `GET /api/u1/v1/douyin/billboard/fetch_hot_item_trends_list`

- 能力：热点/榜单
- 入参：query: `aweme_id`, `option`, `date_window`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_hot_item_trends_list_api_v1_douyin_billboard_fetch_hot_item_trends_list_get`

### `GET /api/u1/v1/douyin/billboard/fetch_hot_rise_list`

- 能力：热点/榜单
- 入参：query: `page*`, `page_size*`, `order*`, `sentence_tag`, `keyword`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_hot_rise_list_api_v1_douyin_billboard_fetch_hot_rise_list_get`

### `POST /api/u1/v1/douyin/billboard/fetch_hot_total_high_fan_list`

- 能力：热点/榜单
- 入参：无
- 请求体：application/json: `page`:integer, `page_size`:integer, `date_window`:integer, `tags`[object]
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_hot_total_high_fan_list_api_v1_douyin_billboard_fetch_hot_total_high_fan_list_post`

### `POST /api/u1/v1/douyin/billboard/fetch_hot_total_high_like_list`

- 能力：热点/榜单
- 入参：无
- 请求体：application/json: `page`:integer, `page_size`:integer, `date_window`:integer, `tags`[object]
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_hot_total_high_like_list_api_v1_douyin_billboard_fetch_hot_total_high_like_list_post`

### `POST /api/u1/v1/douyin/billboard/fetch_hot_total_high_play_list`

- 能力：热点/榜单
- 入参：无
- 请求体：application/json: `page`:integer, `page_size`:integer, `date_window`:integer, `tags`[object]
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_hot_total_high_play_list_api_v1_douyin_billboard_fetch_hot_total_high_play_list_post`

### `POST /api/u1/v1/douyin/billboard/fetch_hot_total_high_search_list`

- 能力：搜索 / 热点/榜单
- 入参：无
- 请求体：application/json: `page_num`:integer, `page_size`:integer, `date_window`:integer, `keyword`:string
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_hot_total_high_search_list_api_v1_douyin_billboard_fetch_hot_total_high_search_list_post`

### `POST /api/u1/v1/douyin/billboard/fetch_hot_total_high_topic_list`

- 能力：热点/榜单 / 话题
- 入参：无
- 请求体：application/json: `page`:integer, `page_size`:integer, `date_window`:integer, `tags`[object]
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_hot_total_high_topic_list_api_v1_douyin_billboard_fetch_hot_total_high_topic_list_post`

### `GET /api/u1/v1/douyin/billboard/fetch_hot_total_hot_word_detail_list`

- 能力：热点/榜单 / 详情
- 入参：query: `keyword*`, `word_id*`, `query_day*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_hot_total_hot_word_detail_list_api_v1_douyin_billboard_fetch_hot_total_hot_word_detail_list_get`

### `POST /api/u1/v1/douyin/billboard/fetch_hot_total_hot_word_list`

- 能力：热点/榜单
- 入参：无
- 请求体：application/json: `page_num`:integer, `page_size`:integer, `date_window`:integer, `keyword`:string
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_hot_total_hot_word_list_api_v1_douyin_billboard_fetch_hot_total_hot_word_list_post`

### `GET /api/u1/v1/douyin/billboard/fetch_hot_total_list`

- 能力：热点/榜单
- 入参：query: `page*`, `page_size*`, `type*`, `snapshot_time`, `start_date`, `end_date`, `sentence_tag`, `keyword`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_hot_total_list_api_v1_douyin_billboard_fetch_hot_total_list_get`

### `POST /api/u1/v1/douyin/billboard/fetch_hot_total_low_fan_list`

- 能力：热点/榜单
- 入参：无
- 请求体：application/json: `page`:integer, `page_size`:integer, `date_window`:integer, `tags`[object]
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_hot_total_low_fan_list_api_v1_douyin_billboard_fetch_hot_total_low_fan_list_post`

### `POST /api/u1/v1/douyin/billboard/fetch_hot_total_search_list`

- 能力：搜索 / 热点/榜单
- 入参：无
- 请求体：application/json: `page_num`:integer, `page_size`:integer, `date_window`:integer, `keyword`:string
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_hot_total_search_list_api_v1_douyin_billboard_fetch_hot_total_search_list_post`

### `POST /api/u1/v1/douyin/billboard/fetch_hot_total_topic_list`

- 能力：热点/榜单 / 话题
- 入参：无
- 请求体：application/json: `page`:integer, `page_size`:integer, `date_window`:integer, `tags`[object]
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_hot_total_topic_list_api_v1_douyin_billboard_fetch_hot_total_topic_list_post`

### `POST /api/u1/v1/douyin/billboard/fetch_hot_total_video_list`

- 能力：热点/榜单 / 作品详情
- 入参：无
- 请求体：application/json: `page`:integer, `page_size`:integer, `date_window`:integer, `sub_type`:integer, `tags`[object]
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_hot_total_video_list_api_v1_douyin_billboard_fetch_hot_total_video_list_post`

### `GET /api/u1/v1/douyin/billboard/fetch_hot_user_portrait_list`

- 能力：热点/榜单 / 主页/账号
- 入参：query: `aweme_id*`, `option`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_hot_user_portrait_list_api_v1_douyin_billboard_fetch_hot_user_portrait_list_get`
