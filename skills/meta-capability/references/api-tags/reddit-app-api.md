# Reddit-APP-API Route Summary

- Back to index: [`api-capability-index.md`](../api-capability-index.md)
- Current tag file: `api-tags/reddit-app-api.md`
- Full contract: [`api-contracts/reddit-app-api.md`](../api-contracts/reddit-app-api.md)
- Source: `https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- Fetched at: `2026-03-08T06:54:04+00:00`
- Route count: `24`
- Common capabilities: general / profiles / accounts / content details / comments / search / details
- Default auth: Header `Authorization` Bearer
- Common inputs: `need_format`, `after`, `sort`, `username`, `subreddit_name`, `subreddit_id`, `post_id`, `filter_posts`, `include_comment_id`, `comment_id`
- Tag description: **(Reddit APP数据接口/Reddit-APP-API endpoints)**

## Routes

### `GET /api/u1/v1/reddit/app/check_subreddit_muted`

- Summary: 检查版块是否静音/Check if Subreddit is Muted
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `check_subreddit_muted_api_v1_reddit_app_check_subreddit_muted_get`
- Full contract: [`api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-check-subreddit-muted`](../api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-check-subreddit-muted)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| subreddit_id | query | string | Yes | 版块ID/Subreddit ID (format: t5_xxxxx) |
| need_format | query | boolean | No | 是否需要清洗数据/Whether to clean and format the data |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 |
| message | string | No | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | No | Support message \| 支持消息 |
| time | string | No | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL |

- Fields truncated: this layer shows only the first `12` rows.

### `GET /api/u1/v1/reddit/app/fetch_comment_replies`

- Summary: 获取Reddit APP评论回复（二级评论）/Fetch Reddit APP Comment Replies (Sub-comments)
- Capabilities: comments
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_comment_replies_api_v1_reddit_app_fetch_comment_replies_get`
- Full contract: [`api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-comment-replies`](../api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-comment-replies)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| post_id | query | string | Yes | 帖子ID/Post ID (e.g., t3_1qmup73) |
| cursor | query | string | Yes | 评论游标/Comment cursor from more.cursor field (e.g., commenttree:ex:(RjiJd) |
| sort_type | query | string | No | 排序方式/Sort method: CONFIDENCE, NEW, TOP, HOT, CONTROVERSIAL, OLD, RANDOM |
| need_format | query | boolean | No | 是否需要清洗数据/Whether to clean and format the data |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 |
| message | string | No | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | No | Support message \| 支持消息 |
| time | string | No | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL |

- Fields truncated: this layer shows only the first `12` rows.

### `GET /api/u1/v1/reddit/app/fetch_community_highlights`

- Summary: 获取Reddit APP社区亮点/Fetch Reddit APP Community Highlights
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_community_highlights_api_v1_reddit_app_fetch_community_highlights_get`
- Full contract: [`api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-community-highlights`](../api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-community-highlights)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| subreddit_id | query | string | Yes | 版块ID/Subreddit ID (format: t5_xxxxx) |
| need_format | query | boolean | No | 是否需要清洗数据/Whether to clean and format the data |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 |
| message | string | No | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | No | Support message \| 支持消息 |
| time | string | No | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL |

- Fields truncated: this layer shows only the first `12` rows.

### `GET /api/u1/v1/reddit/app/fetch_dynamic_search`

- Summary: 获取Reddit APP动态搜索结果/Fetch Reddit APP Dynamic Search Results
- Capabilities: search
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_dynamic_search_api_v1_reddit_app_fetch_dynamic_search_get`
- Full contract: [`api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-dynamic-search`](../api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-dynamic-search)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| query | query | string | Yes | 搜索关键词/Search query |
| search_type | query | string | No | 搜索类型/Search type: post(帖子), community(社区), comment(评论), media(媒体), people(用户) |
| sort | query | string | No | 排序方式(仅适用于post/comment/media)/Sort method (only for post/comment/media): RELEVANCE(相关性), HOT(热门), TOP(最受欢迎), NEW(最新), CO… |
| time_range | query | string | No | 时间范围(仅适用于post/media)/Time range (only for post/media): all(所有时间), year(去年), month(上月), week(上周), day(今天), hour(过去1小时) |
| safe_search | query | string | No | 安全搜索设置/Safe search setting: unset, strict |
| allow_nsfw | query | string | No | 是否允许NSFW内容/Allow NSFW content: 0, 1 |
| after | query | string | No | 分页参数/Pagination parameter |
| need_format | query | boolean | No | 是否需要清洗数据/Whether to clean and format the data |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 |
| message | string | No | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | No | Support message \| 支持消息 |
| time | string | No | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL |

- Fields truncated: this layer shows only the first `12` rows.

### `GET /api/u1/v1/reddit/app/fetch_games_feed`

- Summary: 获取Reddit APP游戏推荐内容/Fetch Reddit APP Games Feed
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_games_feed_api_v1_reddit_app_fetch_games_feed_get`
- Full contract: [`api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-games-feed`](../api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-games-feed)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| sort | query | string | No | 排序方式/Sort method: NEW, HOT, TOP, RISING |
| time | query | string | No | 时间范围/Time range: ALL, HOUR, DAY, WEEK, MONTH, YEAR |
| after | query | string | No | 分页参数/Pagination parameter |
| need_format | query | boolean | No | 是否需要清洗数据/Whether to clean and format the data |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 |
| message | string | No | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | No | Support message \| 支持消息 |
| time | string | No | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL |

- Fields truncated: this layer shows only the first `12` rows.

### `GET /api/u1/v1/reddit/app/fetch_home_feed`

- Summary: 获取Reddit APP首页推荐内容/Fetch Reddit APP Home Feed
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_home_feed_api_v1_reddit_app_fetch_home_feed_get`
- Full contract: [`api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-home-feed`](../api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-home-feed)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| sort | query | string | No | 排序方式/Sort method: HOT, NEW, TOP, BEST, CONTROVERSIAL |
| filter_posts | query | array<Not declared> | No | 过滤掉指定的帖子ID列表/Filter out specified post IDs |
| after | query | string | No | 分页参数/Pagination parameter for fetching next page |
| need_format | query | boolean | No | 是否需要清洗数据/Whether to clean and format the data |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 |
| message | string | No | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | No | Support message \| 支持消息 |
| time | string | No | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL |

- Fields truncated: this layer shows only the first `12` rows.

### `GET /api/u1/v1/reddit/app/fetch_news_feed`

- Summary: 获取Reddit APP资讯推荐内容/Fetch Reddit APP News Feed
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_news_feed_api_v1_reddit_app_fetch_news_feed_get`
- Full contract: [`api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-news-feed`](../api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-news-feed)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| subtopic_ids | query | array<Not declared> | No | 子话题ID列表/Subtopic IDs list |
| after | query | string | No | 分页参数/Pagination parameter |
| need_format | query | boolean | No | 是否需要清洗数据/Whether to clean and format the data |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 |
| message | string | No | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | No | Support message \| 支持消息 |
| time | string | No | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL |

- Fields truncated: this layer shows only the first `12` rows.

### `GET /api/u1/v1/reddit/app/fetch_popular_feed`

- Summary: 获取Reddit APP流行推荐内容/Fetch Reddit APP Popular Feed
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_popular_feed_api_v1_reddit_app_fetch_popular_feed_get`
- Full contract: [`api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-popular-feed`](../api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-popular-feed)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| sort | query | string | No | 排序方式/Sort method: BEST, HOT, NEW, TOP, CONTROVERSIAL, RISING |
| time | query | string | No | 时间范围/Time range: ALL, HOUR, DAY, WEEK, MONTH, YEAR |
| filter_posts | query | array<Not declared> | No | 过滤帖子ID列表/Filter post IDs |
| after | query | string | No | 分页参数/Pagination parameter |
| need_format | query | boolean | No | 是否需要清洗数据/Whether to clean and format the data |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 |
| message | string | No | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | No | Support message \| 支持消息 |
| time | string | No | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL |

- Fields truncated: this layer shows only the first `12` rows.

### `GET /api/u1/v1/reddit/app/fetch_post_comments`

- Summary: 获取Reddit APP帖子评论/Fetch Reddit APP Post Comments
- Capabilities: comments / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_post_comments_api_v1_reddit_app_fetch_post_comments_get`
- Full contract: [`api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-post-comments`](../api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-post-comments)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| post_id | query | string | Yes | 帖子ID/Post ID |
| sort_type | query | string | No | 排序方式/Sort method: CONFIDENCE, NEW, TOP, HOT, CONTROVERSIAL, OLD, RANDOM |
| after | query | string | No | 分页参数/Pagination parameter for fetching next page |
| need_format | query | boolean | No | 是否需要清洗数据/Whether to clean and format the data |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 |
| message | string | No | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | No | Support message \| 支持消息 |
| time | string | No | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL |

- Fields truncated: this layer shows only the first `12` rows.

### `GET /api/u1/v1/reddit/app/fetch_post_details`

- Summary: 获取单个Reddit帖子详情/Fetch Single Reddit Post Details
- Capabilities: content details / details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_post_details_api_v1_reddit_app_fetch_post_details_get`
- Full contract: [`api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-post-details`](../api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-post-details)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| post_id | query | string | Yes | 帖子ID/Post ID (e.g., t3_1ojnh50) |
| include_comment_id | query | boolean | No | 是否包含特定评论ID/Include specific comment ID |
| comment_id | query | string | No | 评论ID/Comment ID (when include_comment_id is True) |
| need_format | query | boolean | No | 是否需要清洗数据/Whether to clean and format the data |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 |
| message | string | No | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | No | Support message \| 支持消息 |
| time | string | No | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL |

- Fields truncated: this layer shows only the first `12` rows.

### `GET /api/u1/v1/reddit/app/fetch_post_details_batch`

- Summary: 批量获取Reddit帖子详情(最多5条)/Fetch Reddit Post Details in Batch (Max 5)
- Capabilities: content details / details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_post_details_batch_api_v1_reddit_app_fetch_post_details_batch_get`
- Full contract: [`api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-post-details-batch`](../api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-post-details-batch)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| post_ids | query | string | Yes | 帖子ID列表，逗号分隔，最多5条/Post IDs comma-separated, max 5 (e.g., t3_1ojnh50,t3_1ok432f) |
| include_comment_id | query | boolean | No | 是否包含特定评论ID/Include specific comment ID |
| comment_id | query | string | No | 评论ID/Comment ID (when include_comment_id is True) |
| need_format | query | boolean | No | 是否需要清洗数据/Whether to clean and format the data |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 |
| message | string | No | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | No | Support message \| 支持消息 |
| time | string | No | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL |

- Fields truncated: this layer shows only the first `12` rows.

### `GET /api/u1/v1/reddit/app/fetch_post_details_batch_large`

- Summary: 大批量获取Reddit帖子详情(最多30条)/Fetch Reddit Post Details in Large Batch (Max 30)
- Capabilities: content details / details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_post_details_batch_large_api_v1_reddit_app_fetch_post_details_batch_large_get`
- Full contract: [`api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-post-details-batch-large`](../api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-post-details-batch-large)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| post_ids | query | string | Yes | 帖子ID列表，逗号分隔，最多30条/Post IDs comma-separated, max 30 (e.g., t3_1ojnh50,t3_1ok432f,...) |
| include_comment_id | query | boolean | No | 是否包含特定评论ID/Include specific comment ID |
| comment_id | query | string | No | 评论ID/Comment ID (when include_comment_id is True) |
| need_format | query | boolean | No | 是否需要清洗数据/Whether to clean and format the data |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 |
| message | string | No | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | No | Support message \| 支持消息 |
| time | string | No | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL |

- Fields truncated: this layer shows only the first `12` rows.

### `GET /api/u1/v1/reddit/app/fetch_search_typeahead`

- Summary: 获取Reddit APP搜索自动补全建议/Fetch Reddit APP Search Typeahead Suggestions
- Capabilities: search
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_search_typeahead_api_v1_reddit_app_fetch_search_typeahead_get`
- Full contract: [`api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-search-typeahead`](../api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-search-typeahead)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| query | query | string | Yes | 搜索关键词/Search query |
| safe_search | query | string | No | 安全搜索设置/Safe search setting: unset, strict |
| allow_nsfw | query | string | No | 是否允许NSFW内容/Allow NSFW content: 0 or 1 |
| need_format | query | boolean | No | 是否需要清洗数据/Whether to clean and format the data |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 |
| message | string | No | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | No | Support message \| 支持消息 |
| time | string | No | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL |

- Fields truncated: this layer shows only the first `12` rows.

### `GET /api/u1/v1/reddit/app/fetch_subreddit_feed`

- Summary: 获取Reddit APP版块Feed内容/Fetch Reddit APP Subreddit Feed
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_subreddit_feed_api_v1_reddit_app_fetch_subreddit_feed_get`
- Full contract: [`api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-subreddit-feed`](../api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-subreddit-feed)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| subreddit_name | query | string | Yes | 版块名称/Subreddit name |
| sort | query | string | No | 排序方式/Sort method: BEST, HOT, NEW, TOP, CONTROVERSIAL, RISING |
| filter_posts | query | array<Not declared> | No | 过滤帖子ID列表/Filter post IDs |
| after | query | string | No | 分页参数/Pagination parameter |
| need_format | query | boolean | No | 是否需要清洗数据/Whether to clean and format the data |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 |
| message | string | No | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | No | Support message \| 支持消息 |
| time | string | No | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL |

- Fields truncated: this layer shows only the first `12` rows.

### `GET /api/u1/v1/reddit/app/fetch_subreddit_info`

- Summary: 获取Reddit APP版块信息/Fetch Reddit APP Subreddit Info
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_subreddit_info_api_v1_reddit_app_fetch_subreddit_info_get`
- Full contract: [`api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-subreddit-info`](../api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-subreddit-info)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| subreddit_name | query | string | No | 版块名称/Subreddit name |
| need_format | query | boolean | No | 是否需要清洗数据/Whether to clean and format the data |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 |
| message | string | No | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | No | Support message \| 支持消息 |
| time | string | No | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL |

- Fields truncated: this layer shows only the first `12` rows.

### `GET /api/u1/v1/reddit/app/fetch_subreddit_post_channels`

- Summary: 获取Reddit APP版块帖子频道信息/Fetch Reddit APP Subreddit Post Channels
- Capabilities: profiles / accounts / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_subreddit_post_channels_api_v1_reddit_app_fetch_subreddit_post_channels_get`
- Full contract: [`api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-subreddit-post-channels`](../api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-subreddit-post-channels)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| subreddit_name | query | string | No | 版块名称/Subreddit name |
| sort | query | string | No | 排序方式/Sort method: HOT, NEW, TOP, CONTROVERSIAL, RISING |
| range | query | string | No | 时间范围/Time range: HOUR, DAY, WEEK, MONTH, YEAR, ALL |
| need_format | query | boolean | No | 是否需要清洗数据/Whether to clean and format the data |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 |
| message | string | No | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | No | Support message \| 支持消息 |
| time | string | No | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL |

- Fields truncated: this layer shows only the first `12` rows.

### `GET /api/u1/v1/reddit/app/fetch_subreddit_settings`

- Summary: 获取Reddit APP版块设置/Fetch Reddit APP Subreddit Settings
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_subreddit_settings_api_v1_reddit_app_fetch_subreddit_settings_get`
- Full contract: [`api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-subreddit-settings`](../api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-subreddit-settings)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| subreddit_id | query | string | Yes | 版块ID/Subreddit ID (format: t5_xxxxx) |
| need_format | query | boolean | No | 是否需要清洗数据/Whether to clean and format the data |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 |
| message | string | No | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | No | Support message \| 支持消息 |
| time | string | No | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL |

- Fields truncated: this layer shows only the first `12` rows.

### `GET /api/u1/v1/reddit/app/fetch_subreddit_style`

- Summary: 获取Reddit APP版块规则样式信息/Fetch Reddit APP Subreddit Rules and Style Info
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_subreddit_style_api_v1_reddit_app_fetch_subreddit_style_get`
- Full contract: [`api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-subreddit-style`](../api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-subreddit-style)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| subreddit_name | query | string | No | 版块名称/Subreddit name |
| need_format | query | boolean | No | 是否需要清洗数据/Whether to clean and format the data |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 |
| message | string | No | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | No | Support message \| 支持消息 |
| time | string | No | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL |

- Fields truncated: this layer shows only the first `12` rows.

### `GET /api/u1/v1/reddit/app/fetch_trending_searches`

- Summary: 获取Reddit APP今日热门搜索/Fetch Reddit APP Trending Searches
- Capabilities: search / trends / rankings
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_trending_searches_api_v1_reddit_app_fetch_trending_searches_get`
- Full contract: [`api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-trending-searches`](../api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-trending-searches)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| need_format | query | boolean | No | 是否需要清洗数据/Whether to clean and format the data |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 |
| message | string | No | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | No | Support message \| 支持消息 |
| time | string | No | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL |

- Fields truncated: this layer shows only the first `12` rows.

### `GET /api/u1/v1/reddit/app/fetch_user_active_subreddits`

- Summary: 获取用户活跃的社区列表/Fetch User's Active Subreddits
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_active_subreddits_api_v1_reddit_app_fetch_user_active_subreddits_get`
- Full contract: [`api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-user-active-subreddits`](../api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-user-active-subreddits)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| username | query | string | Yes | 用户名/Username |
| need_format | query | boolean | No | 是否需要清洗数据/Whether to clean and format the data |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 |
| message | string | No | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | No | Support message \| 支持消息 |
| time | string | No | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL |

- Fields truncated: this layer shows only the first `12` rows.

### `GET /api/u1/v1/reddit/app/fetch_user_comments`

- Summary: 获取用户评论列表/Fetch User Comments
- Capabilities: comments / profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_comments_api_v1_reddit_app_fetch_user_comments_get`
- Full contract: [`api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-user-comments`](../api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-user-comments)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| username | query | string | Yes | 用户名/Username |
| sort | query | string | No | 排序方式/Sort method: NEW, TOP, HOT, CONTROVERSIAL |
| page_size | query | integer | No | 每页数量/Page size (default: 25) |
| after | query | string | No | 分页参数/Pagination parameter |
| need_format | query | boolean | No | 是否需要清洗数据/Whether to clean and format the data |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 |
| message | string | No | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | No | Support message \| 支持消息 |
| time | string | No | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL |

- Fields truncated: this layer shows only the first `12` rows.

### `GET /api/u1/v1/reddit/app/fetch_user_posts`

- Summary: 获取用户发布的帖子列表/Fetch User Posts
- Capabilities: profiles / accounts / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_posts_api_v1_reddit_app_fetch_user_posts_get`
- Full contract: [`api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-user-posts`](../api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-user-posts)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| username | query | string | Yes | 用户名/Username |
| sort | query | string | No | 排序方式/Sort method: NEW, TOP, HOT, CONTROVERSIAL |
| after | query | string | No | 分页参数/Pagination parameter |
| need_format | query | boolean | No | 是否需要清洗数据/Whether to clean and format the data |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 |
| message | string | No | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | No | Support message \| 支持消息 |
| time | string | No | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL |

- Fields truncated: this layer shows only the first `12` rows.

### `GET /api/u1/v1/reddit/app/fetch_user_profile`

- Summary: 获取Reddit APP用户资料信息/Fetch Reddit APP User Profile
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_profile_api_v1_reddit_app_fetch_user_profile_get`
- Full contract: [`api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-user-profile`](../api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-user-profile)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| username | query | string | Yes | 用户名/Username |
| need_format | query | boolean | No | 是否需要清洗数据/Whether to clean and format the data |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 |
| message | string | No | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | No | Support message \| 支持消息 |
| time | string | No | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL |

- Fields truncated: this layer shows only the first `12` rows.

### `GET /api/u1/v1/reddit/app/fetch_user_trophies`

- Summary: 获取用户公开奖杯/Fetch User Public Trophies
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_trophies_api_v1_reddit_app_fetch_user_trophies_get`
- Full contract: [`api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-user-trophies`](../api-contracts/reddit-app-api.md#get-api-u1-v1-reddit-app-fetch-user-trophies)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| username | query | string | Yes | 用户名/Username |
| need_format | query | boolean | No | 是否需要清洗数据/Whether to clean and format the data |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 |
| message | string | No | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | No | Support message \| 支持消息 |
| time | string | No | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL |

- Fields truncated: this layer shows only the first `12` rows.
