# Reddit-APP-API 路由详情

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 当前 tag 文件：`api-tags/reddit-app-api.md`
- 完整契约：[`api-contracts/reddit-app-api.md`](../api-contracts/reddit-app-api.md)
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T04:31:58+00:00`
- 路由数：`24`
- 常见能力：通用能力 / 主页/账号 / 作品详情 / 评论 / 搜索 / 详情
- 默认认证：请求头 `Authorization` Bearer
- 常见入参：`need_format`, `after`, `sort`, `username`, `subreddit_name`, `subreddit_id`, `post_id`, `filter_posts`, `include_comment_id`, `comment_id`
- 标签说明：**(Reddit APP数据接口/Reddit-APP-API endpoints)**

## 路由列表

### `GET /api/u1/v1/reddit/app/check_subreddit_muted`

- 摘要：检查版块是否静音/Check if Subreddit is Muted
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`check_subreddit_muted_api_v1_reddit_app_check_subreddit_muted_get`
- 完整契约：[`api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-check-subreddit-muted`](../api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-check-subreddit-muted)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| subreddit_id | query | string | 是 | 版块ID/Subreddit ID (format: t5_xxxxx) |
| need_format | query | boolean | 否 | 是否需要清洗数据/Whether to clean and format the data |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | 否 | Support message \| 支持消息 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL |

- 字段已截断：当前层仅展示前 `12` 行。

### `GET /api/u1/v1/reddit/app/fetch_comment_replies`

- 摘要：获取Reddit APP评论回复（二级评论）/Fetch Reddit APP Comment Replies (Sub-comments)
- 能力：评论
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_comment_replies_api_v1_reddit_app_fetch_comment_replies_get`
- 完整契约：[`api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-comment-replies`](../api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-comment-replies)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| post_id | query | string | 是 | 帖子ID/Post ID (e.g., t3_1qmup73) |
| cursor | query | string | 是 | 评论游标/Comment cursor from more.cursor field (e.g., commenttree:ex:(RjiJd) |
| sort_type | query | string | 否 | 排序方式/Sort method: CONFIDENCE, NEW, TOP, HOT, CONTROVERSIAL, OLD, RANDOM |
| need_format | query | boolean | 否 | 是否需要清洗数据/Whether to clean and format the data |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | 否 | Support message \| 支持消息 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL |

- 字段已截断：当前层仅展示前 `12` 行。

### `GET /api/u1/v1/reddit/app/fetch_community_highlights`

- 摘要：获取Reddit APP社区亮点/Fetch Reddit APP Community Highlights
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_community_highlights_api_v1_reddit_app_fetch_community_highlights_get`
- 完整契约：[`api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-community-highlights`](../api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-community-highlights)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| subreddit_id | query | string | 是 | 版块ID/Subreddit ID (format: t5_xxxxx) |
| need_format | query | boolean | 否 | 是否需要清洗数据/Whether to clean and format the data |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | 否 | Support message \| 支持消息 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL |

- 字段已截断：当前层仅展示前 `12` 行。

### `GET /api/u1/v1/reddit/app/fetch_dynamic_search`

- 摘要：获取Reddit APP动态搜索结果/Fetch Reddit APP Dynamic Search Results
- 能力：搜索
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_dynamic_search_api_v1_reddit_app_fetch_dynamic_search_get`
- 完整契约：[`api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-dynamic-search`](../api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-dynamic-search)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| query | query | string | 是 | 搜索关键词/Search query |
| search_type | query | string | 否 | 搜索类型/Search type: post(帖子), community(社区), comment(评论), media(媒体), people(用户) |
| sort | query | string | 否 | 排序方式(仅适用于post/comment/media)/Sort method (only for post/comment/media): RELEVANCE(相关性), HOT(热门), TOP(最受欢迎), NEW(最新), CO… |
| time_range | query | string | 否 | 时间范围(仅适用于post/media)/Time range (only for post/media): all(所有时间), year(去年), month(上月), week(上周), day(今天), hour(过去1小时) |
| safe_search | query | string | 否 | 安全搜索设置/Safe search setting: unset, strict |
| allow_nsfw | query | string | 否 | 是否允许NSFW内容/Allow NSFW content: 0, 1 |
| after | query | string | 否 | 分页参数/Pagination parameter |
| need_format | query | boolean | 否 | 是否需要清洗数据/Whether to clean and format the data |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | 否 | Support message \| 支持消息 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL |

- 字段已截断：当前层仅展示前 `12` 行。

### `GET /api/u1/v1/reddit/app/fetch_games_feed`

- 摘要：获取Reddit APP游戏推荐内容/Fetch Reddit APP Games Feed
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_games_feed_api_v1_reddit_app_fetch_games_feed_get`
- 完整契约：[`api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-games-feed`](../api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-games-feed)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| sort | query | string | 否 | 排序方式/Sort method: NEW, HOT, TOP, RISING |
| time | query | string | 否 | 时间范围/Time range: ALL, HOUR, DAY, WEEK, MONTH, YEAR |
| after | query | string | 否 | 分页参数/Pagination parameter |
| need_format | query | boolean | 否 | 是否需要清洗数据/Whether to clean and format the data |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | 否 | Support message \| 支持消息 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL |

- 字段已截断：当前层仅展示前 `12` 行。

### `GET /api/u1/v1/reddit/app/fetch_home_feed`

- 摘要：获取Reddit APP首页推荐内容/Fetch Reddit APP Home Feed
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_home_feed_api_v1_reddit_app_fetch_home_feed_get`
- 完整契约：[`api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-home-feed`](../api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-home-feed)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| sort | query | string | 否 | 排序方式/Sort method: HOT, NEW, TOP, BEST, CONTROVERSIAL |
| filter_posts | query | array<未声明> | 否 | 过滤掉指定的帖子ID列表/Filter out specified post IDs |
| after | query | string | 否 | 分页参数/Pagination parameter for fetching next page |
| need_format | query | boolean | 否 | 是否需要清洗数据/Whether to clean and format the data |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | 否 | Support message \| 支持消息 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL |

- 字段已截断：当前层仅展示前 `12` 行。

### `GET /api/u1/v1/reddit/app/fetch_news_feed`

- 摘要：获取Reddit APP资讯推荐内容/Fetch Reddit APP News Feed
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_news_feed_api_v1_reddit_app_fetch_news_feed_get`
- 完整契约：[`api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-news-feed`](../api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-news-feed)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| subtopic_ids | query | array<未声明> | 否 | 子话题ID列表/Subtopic IDs list |
| after | query | string | 否 | 分页参数/Pagination parameter |
| need_format | query | boolean | 否 | 是否需要清洗数据/Whether to clean and format the data |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | 否 | Support message \| 支持消息 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL |

- 字段已截断：当前层仅展示前 `12` 行。

### `GET /api/u1/v1/reddit/app/fetch_popular_feed`

- 摘要：获取Reddit APP流行推荐内容/Fetch Reddit APP Popular Feed
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_popular_feed_api_v1_reddit_app_fetch_popular_feed_get`
- 完整契约：[`api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-popular-feed`](../api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-popular-feed)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| sort | query | string | 否 | 排序方式/Sort method: BEST, HOT, NEW, TOP, CONTROVERSIAL, RISING |
| time | query | string | 否 | 时间范围/Time range: ALL, HOUR, DAY, WEEK, MONTH, YEAR |
| filter_posts | query | array<未声明> | 否 | 过滤帖子ID列表/Filter post IDs |
| after | query | string | 否 | 分页参数/Pagination parameter |
| need_format | query | boolean | 否 | 是否需要清洗数据/Whether to clean and format the data |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | 否 | Support message \| 支持消息 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL |

- 字段已截断：当前层仅展示前 `12` 行。

### `GET /api/u1/v1/reddit/app/fetch_post_comments`

- 摘要：获取Reddit APP帖子评论/Fetch Reddit APP Post Comments
- 能力：评论 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_post_comments_api_v1_reddit_app_fetch_post_comments_get`
- 完整契约：[`api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-post-comments`](../api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-post-comments)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| post_id | query | string | 是 | 帖子ID/Post ID |
| sort_type | query | string | 否 | 排序方式/Sort method: CONFIDENCE, NEW, TOP, HOT, CONTROVERSIAL, OLD, RANDOM |
| after | query | string | 否 | 分页参数/Pagination parameter for fetching next page |
| need_format | query | boolean | 否 | 是否需要清洗数据/Whether to clean and format the data |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | 否 | Support message \| 支持消息 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL |

- 字段已截断：当前层仅展示前 `12` 行。

### `GET /api/u1/v1/reddit/app/fetch_post_details`

- 摘要：获取单个Reddit帖子详情/Fetch Single Reddit Post Details
- 能力：作品详情 / 详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_post_details_api_v1_reddit_app_fetch_post_details_get`
- 完整契约：[`api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-post-details`](../api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-post-details)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| post_id | query | string | 是 | 帖子ID/Post ID (e.g., t3_1ojnh50) |
| include_comment_id | query | boolean | 否 | 是否包含特定评论ID/Include specific comment ID |
| comment_id | query | string | 否 | 评论ID/Comment ID (when include_comment_id is True) |
| need_format | query | boolean | 否 | 是否需要清洗数据/Whether to clean and format the data |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | 否 | Support message \| 支持消息 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL |

- 字段已截断：当前层仅展示前 `12` 行。

### `GET /api/u1/v1/reddit/app/fetch_post_details_batch`

- 摘要：批量获取Reddit帖子详情(最多5条)/Fetch Reddit Post Details in Batch (Max 5)
- 能力：作品详情 / 详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_post_details_batch_api_v1_reddit_app_fetch_post_details_batch_get`
- 完整契约：[`api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-post-details-batch`](../api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-post-details-batch)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| post_ids | query | string | 是 | 帖子ID列表，逗号分隔，最多5条/Post IDs comma-separated, max 5 (e.g., t3_1ojnh50,t3_1ok432f) |
| include_comment_id | query | boolean | 否 | 是否包含特定评论ID/Include specific comment ID |
| comment_id | query | string | 否 | 评论ID/Comment ID (when include_comment_id is True) |
| need_format | query | boolean | 否 | 是否需要清洗数据/Whether to clean and format the data |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | 否 | Support message \| 支持消息 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL |

- 字段已截断：当前层仅展示前 `12` 行。

### `GET /api/u1/v1/reddit/app/fetch_post_details_batch_large`

- 摘要：大批量获取Reddit帖子详情(最多30条)/Fetch Reddit Post Details in Large Batch (Max 30)
- 能力：作品详情 / 详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_post_details_batch_large_api_v1_reddit_app_fetch_post_details_batch_large_get`
- 完整契约：[`api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-post-details-batch-large`](../api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-post-details-batch-large)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| post_ids | query | string | 是 | 帖子ID列表，逗号分隔，最多30条/Post IDs comma-separated, max 30 (e.g., t3_1ojnh50,t3_1ok432f,...) |
| include_comment_id | query | boolean | 否 | 是否包含特定评论ID/Include specific comment ID |
| comment_id | query | string | 否 | 评论ID/Comment ID (when include_comment_id is True) |
| need_format | query | boolean | 否 | 是否需要清洗数据/Whether to clean and format the data |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | 否 | Support message \| 支持消息 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL |

- 字段已截断：当前层仅展示前 `12` 行。

### `GET /api/u1/v1/reddit/app/fetch_search_typeahead`

- 摘要：获取Reddit APP搜索自动补全建议/Fetch Reddit APP Search Typeahead Suggestions
- 能力：搜索
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_search_typeahead_api_v1_reddit_app_fetch_search_typeahead_get`
- 完整契约：[`api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-search-typeahead`](../api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-search-typeahead)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| query | query | string | 是 | 搜索关键词/Search query |
| safe_search | query | string | 否 | 安全搜索设置/Safe search setting: unset, strict |
| allow_nsfw | query | string | 否 | 是否允许NSFW内容/Allow NSFW content: 0 or 1 |
| need_format | query | boolean | 否 | 是否需要清洗数据/Whether to clean and format the data |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | 否 | Support message \| 支持消息 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL |

- 字段已截断：当前层仅展示前 `12` 行。

### `GET /api/u1/v1/reddit/app/fetch_subreddit_feed`

- 摘要：获取Reddit APP版块Feed内容/Fetch Reddit APP Subreddit Feed
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_subreddit_feed_api_v1_reddit_app_fetch_subreddit_feed_get`
- 完整契约：[`api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-subreddit-feed`](../api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-subreddit-feed)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| subreddit_name | query | string | 是 | 版块名称/Subreddit name |
| sort | query | string | 否 | 排序方式/Sort method: BEST, HOT, NEW, TOP, CONTROVERSIAL, RISING |
| filter_posts | query | array<未声明> | 否 | 过滤帖子ID列表/Filter post IDs |
| after | query | string | 否 | 分页参数/Pagination parameter |
| need_format | query | boolean | 否 | 是否需要清洗数据/Whether to clean and format the data |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | 否 | Support message \| 支持消息 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL |

- 字段已截断：当前层仅展示前 `12` 行。

### `GET /api/u1/v1/reddit/app/fetch_subreddit_info`

- 摘要：获取Reddit APP版块信息/Fetch Reddit APP Subreddit Info
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_subreddit_info_api_v1_reddit_app_fetch_subreddit_info_get`
- 完整契约：[`api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-subreddit-info`](../api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-subreddit-info)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| subreddit_name | query | string | 否 | 版块名称/Subreddit name |
| need_format | query | boolean | 否 | 是否需要清洗数据/Whether to clean and format the data |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | 否 | Support message \| 支持消息 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL |

- 字段已截断：当前层仅展示前 `12` 行。

### `GET /api/u1/v1/reddit/app/fetch_subreddit_post_channels`

- 摘要：获取Reddit APP版块帖子频道信息/Fetch Reddit APP Subreddit Post Channels
- 能力：主页/账号 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_subreddit_post_channels_api_v1_reddit_app_fetch_subreddit_post_channels_get`
- 完整契约：[`api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-subreddit-post-channels`](../api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-subreddit-post-channels)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| subreddit_name | query | string | 否 | 版块名称/Subreddit name |
| sort | query | string | 否 | 排序方式/Sort method: HOT, NEW, TOP, CONTROVERSIAL, RISING |
| range | query | string | 否 | 时间范围/Time range: HOUR, DAY, WEEK, MONTH, YEAR, ALL |
| need_format | query | boolean | 否 | 是否需要清洗数据/Whether to clean and format the data |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | 否 | Support message \| 支持消息 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL |

- 字段已截断：当前层仅展示前 `12` 行。

### `GET /api/u1/v1/reddit/app/fetch_subreddit_settings`

- 摘要：获取Reddit APP版块设置/Fetch Reddit APP Subreddit Settings
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_subreddit_settings_api_v1_reddit_app_fetch_subreddit_settings_get`
- 完整契约：[`api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-subreddit-settings`](../api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-subreddit-settings)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| subreddit_id | query | string | 是 | 版块ID/Subreddit ID (format: t5_xxxxx) |
| need_format | query | boolean | 否 | 是否需要清洗数据/Whether to clean and format the data |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | 否 | Support message \| 支持消息 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL |

- 字段已截断：当前层仅展示前 `12` 行。

### `GET /api/u1/v1/reddit/app/fetch_subreddit_style`

- 摘要：获取Reddit APP版块规则样式信息/Fetch Reddit APP Subreddit Rules and Style Info
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_subreddit_style_api_v1_reddit_app_fetch_subreddit_style_get`
- 完整契约：[`api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-subreddit-style`](../api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-subreddit-style)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| subreddit_name | query | string | 否 | 版块名称/Subreddit name |
| need_format | query | boolean | 否 | 是否需要清洗数据/Whether to clean and format the data |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | 否 | Support message \| 支持消息 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL |

- 字段已截断：当前层仅展示前 `12` 行。

### `GET /api/u1/v1/reddit/app/fetch_trending_searches`

- 摘要：获取Reddit APP今日热门搜索/Fetch Reddit APP Trending Searches
- 能力：搜索 / 热点/榜单
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_trending_searches_api_v1_reddit_app_fetch_trending_searches_get`
- 完整契约：[`api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-trending-searches`](../api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-trending-searches)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| need_format | query | boolean | 否 | 是否需要清洗数据/Whether to clean and format the data |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | 否 | Support message \| 支持消息 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL |

- 字段已截断：当前层仅展示前 `12` 行。

### `GET /api/u1/v1/reddit/app/fetch_user_active_subreddits`

- 摘要：获取用户活跃的社区列表/Fetch User's Active Subreddits
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_active_subreddits_api_v1_reddit_app_fetch_user_active_subreddits_get`
- 完整契约：[`api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-user-active-subreddits`](../api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-user-active-subreddits)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| username | query | string | 是 | 用户名/Username |
| need_format | query | boolean | 否 | 是否需要清洗数据/Whether to clean and format the data |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | 否 | Support message \| 支持消息 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL |

- 字段已截断：当前层仅展示前 `12` 行。

### `GET /api/u1/v1/reddit/app/fetch_user_comments`

- 摘要：获取用户评论列表/Fetch User Comments
- 能力：评论 / 主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_comments_api_v1_reddit_app_fetch_user_comments_get`
- 完整契约：[`api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-user-comments`](../api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-user-comments)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| username | query | string | 是 | 用户名/Username |
| sort | query | string | 否 | 排序方式/Sort method: NEW, TOP, HOT, CONTROVERSIAL |
| page_size | query | integer | 否 | 每页数量/Page size (default: 25) |
| after | query | string | 否 | 分页参数/Pagination parameter |
| need_format | query | boolean | 否 | 是否需要清洗数据/Whether to clean and format the data |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | 否 | Support message \| 支持消息 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL |

- 字段已截断：当前层仅展示前 `12` 行。

### `GET /api/u1/v1/reddit/app/fetch_user_posts`

- 摘要：获取用户发布的帖子列表/Fetch User Posts
- 能力：主页/账号 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_posts_api_v1_reddit_app_fetch_user_posts_get`
- 完整契约：[`api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-user-posts`](../api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-user-posts)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| username | query | string | 是 | 用户名/Username |
| sort | query | string | 否 | 排序方式/Sort method: NEW, TOP, HOT, CONTROVERSIAL |
| after | query | string | 否 | 分页参数/Pagination parameter |
| need_format | query | boolean | 否 | 是否需要清洗数据/Whether to clean and format the data |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | 否 | Support message \| 支持消息 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL |

- 字段已截断：当前层仅展示前 `12` 行。

### `GET /api/u1/v1/reddit/app/fetch_user_profile`

- 摘要：获取Reddit APP用户资料信息/Fetch Reddit APP User Profile
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_profile_api_v1_reddit_app_fetch_user_profile_get`
- 完整契约：[`api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-user-profile`](../api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-user-profile)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| username | query | string | 是 | 用户名/Username |
| need_format | query | boolean | 否 | 是否需要清洗数据/Whether to clean and format the data |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | 否 | Support message \| 支持消息 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL |

- 字段已截断：当前层仅展示前 `12` 行。

### `GET /api/u1/v1/reddit/app/fetch_user_trophies`

- 摘要：获取用户公开奖杯/Fetch User Public Trophies
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_trophies_api_v1_reddit_app_fetch_user_trophies_get`
- 完整契约：[`api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-user-trophies`](../api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-user-trophies)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| username | query | string | 是 | 用户名/Username |
| need_format | query | boolean | 否 | 是否需要清洗数据/Whether to clean and format the data |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | 否 | Support message \| 支持消息 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL |

- 字段已截断：当前层仅展示前 `12` 行。
