# Douyin-Search-API Route Summary

- Back to index: [`api-capability-index.md`](../api-capability-index.md)
- Current tag file: `api-tags/douyin-search-api.md`
- Full contract: [`api-contracts/douyin-search-api.md`](../api-contracts/douyin-search-api.md)
- Source: `https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- Fetched at: `2026-03-08T06:54:04+00:00`
- Route count: `20`
- Common capabilities: search / topics / profiles / accounts / content details / livestream / music / audio
- Default auth: Header `Authorization` Bearer
- Common inputs: `keyword`, `cursor`, `search_id`, `sort_type`, `publish_time`, `filter_duration`, `content_type`, `backtrace`, `douyin_user_fans`, `douyin_user_type`
- Tag description: **(抖音搜索数据接口（当前最新版，请优先使用此目录下的接口而不是其他目录下的搜索接口）/Douyin-Search-API data endpoints (Current latest version, please use the interfaces in this directory first instead of the search interfaces in other directories))**

## Routes

### `POST /api/u1/v1/douyin/search/fetch_challenge_search_v1`

- Summary: 获取话题搜索 V1/Fetch hashtag search V1
- Capabilities: search / topics
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_challenge_search_v1_api_v1_douyin_search_fetch_challenge_search_v1_post`
- Full contract: [`api-contracts/douyin-search-api.md#post-api-u1-v1-douyin-search-fetch-challenge-search-v1`](../api-contracts/douyin-search-api.md#post-api-u1-v1-douyin-search-fetch-challenge-search-v1)

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: `keyword`:string, `cursor`:integer, `sort_type`:string, `publish_time`:string, `filter_duration`:string, `content_type`:string, `search_id`:string, `backtrace`:string

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| keyword | string | No | 关键词 / Keyword |
| cursor | integer | No | 偏移游标，用于翻页，从上一次请求返回的响应中获取 / Offset cursor for pagination, obtained from the last response |
| sort_type | string | No | 排序方式：0=综合排序 1=最多点赞 2=最新发布 / Sort type: 0=Comprehensive, 1=Most Likes, 2=Latest |
| publish_time | string | No | 发布时间筛选：0=不限 1=最近一天 7=最近一周 180=最近半年 / Publish time filter: 0=Unlimited, 1=Last day, 7=Last week, 180=Last half year |
| filter_duration | string | No | 视频时长过滤：0=不限 0-1=一分钟以内 1-5=一到五分钟 5-10000=五分钟以上 / Video duration filter: 0=Unlimited, 0-1=Within 1 minute, 1-5=1 to 5 min… |
| content_type | string | No | 内容类型：0=不限 1=视频 2=图片 3=文章 / Content type: 0=All, 1=Video, 2=Picture, 3=Article |
| search_id | string | No | 搜索ID，用于翻页，从上一次请求返回的响应中获取 / Search ID for pagination, obtained from the last response |
| backtrace | string | No | 翻页回溯标识，用于翻页，从上一次请求返回的响应中获取 / Backtrace for pagination, obtained from the last response |

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

### `POST /api/u1/v1/douyin/search/fetch_challenge_search_v2`

- Summary: 获取话题搜索 V2/Fetch hashtag search V2
- Capabilities: search / topics
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_challenge_search_v2_api_v1_douyin_search_fetch_challenge_search_v2_post`
- Full contract: [`api-contracts/douyin-search-api.md#post-api-u1-v1-douyin-search-fetch-challenge-search-v2`](../api-contracts/douyin-search-api.md#post-api-u1-v1-douyin-search-fetch-challenge-search-v2)

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: `keyword`:string, `cursor`:integer, `sort_type`:string, `publish_time`:string, `filter_duration`:string, `content_type`:string, `search_id`:string, `backtrace`:string

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| keyword | string | No | 关键词 / Keyword |
| cursor | integer | No | 偏移游标，用于翻页，从上一次请求返回的响应中获取 / Offset cursor for pagination, obtained from the last response |
| sort_type | string | No | 排序方式：0=综合排序 1=最多点赞 2=最新发布 / Sort type: 0=Comprehensive, 1=Most Likes, 2=Latest |
| publish_time | string | No | 发布时间筛选：0=不限 1=最近一天 7=最近一周 180=最近半年 / Publish time filter: 0=Unlimited, 1=Last day, 7=Last week, 180=Last half year |
| filter_duration | string | No | 视频时长过滤：0=不限 0-1=一分钟以内 1-5=一到五分钟 5-10000=五分钟以上 / Video duration filter: 0=Unlimited, 0-1=Within 1 minute, 1-5=1 to 5 min… |
| content_type | string | No | 内容类型：0=不限 1=视频 2=图片 3=文章 / Content type: 0=All, 1=Video, 2=Picture, 3=Article |
| search_id | string | No | 搜索ID，用于翻页，从上一次请求返回的响应中获取 / Search ID for pagination, obtained from the last response |
| backtrace | string | No | 翻页回溯标识，用于翻页，从上一次请求返回的响应中获取 / Backtrace for pagination, obtained from the last response |

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

### `POST /api/u1/v1/douyin/search/fetch_challenge_suggest`

- Summary: 获取话题推荐搜索/Fetch hashtag suggestions
- Capabilities: search / topics
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_challenge_suggest_api_v1_douyin_search_fetch_challenge_suggest_post`
- Full contract: [`api-contracts/douyin-search-api.md#post-api-u1-v1-douyin-search-fetch-challenge-suggest`](../api-contracts/douyin-search-api.md#post-api-u1-v1-douyin-search-fetch-challenge-suggest)

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: `keyword`:string

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| keyword | string | No | 关键词，如 '游戏' / Keyword, e.g., 'game' |

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

### `POST /api/u1/v1/douyin/search/fetch_discuss_search`

- Summary: 获取讨论搜索/Fetch discussion search
- Capabilities: search
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_discuss_search_api_v1_douyin_search_fetch_discuss_search_post`
- Full contract: [`api-contracts/douyin-search-api.md#post-api-u1-v1-douyin-search-fetch-discuss-search`](../api-contracts/douyin-search-api.md#post-api-u1-v1-douyin-search-fetch-discuss-search)

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: `keyword`:string, `cursor`:integer, `sort_type`:string, `publish_time`:string, `filter_duration`:string, `content_type`:string, `search_id`:string, `backtrace`:string

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| keyword | string | No | 关键词 / Keyword |
| cursor | integer | No | 偏移游标，用于翻页，从上一次请求返回的响应中获取 / Offset cursor for pagination, obtained from the last response |
| sort_type | string | No | 排序方式：0=综合排序 1=最多点赞 2=最新发布 / Sort type: 0=Comprehensive, 1=Most Likes, 2=Latest |
| publish_time | string | No | 发布时间筛选：0=不限 1=最近一天 7=最近一周 180=最近半年 / Publish time filter: 0=Unlimited, 1=Last day, 7=Last week, 180=Last half year |
| filter_duration | string | No | 视频时长过滤：0=不限 0-1=一分钟以内 1-5=一到五分钟 5-10000=五分钟以上 / Video duration filter: 0=Unlimited, 0-1=Within 1 minute, 1-5=1 to 5 min… |
| content_type | string | No | 内容类型：0=不限 1=视频 2=图片 3=文章 / Content type: 0=All, 1=Video, 2=Picture, 3=Article |
| search_id | string | No | 搜索ID，用于翻页，从上一次请求返回的响应中获取 / Search ID for pagination, obtained from the last response |
| backtrace | string | No | 翻页回溯标识，用于翻页，从上一次请求返回的响应中获取 / Backtrace for pagination, obtained from the last response |

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

### `POST /api/u1/v1/douyin/search/fetch_experience_search`

- Summary: 获取经验搜索/Fetch experience search
- Capabilities: search
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_experience_search_api_v1_douyin_search_fetch_experience_search_post`
- Full contract: [`api-contracts/douyin-search-api.md#post-api-u1-v1-douyin-search-fetch-experience-search`](../api-contracts/douyin-search-api.md#post-api-u1-v1-douyin-search-fetch-experience-search)

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: `keyword`:string, `cursor`:integer, `sort_type`:string, `publish_time`:string, `filter_duration`:string, `content_type`:string, `search_id`:string, `backtrace`:string

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| keyword | string | No | 关键词 / Keyword |
| cursor | integer | No | 偏移游标，用于翻页，从上一次请求返回的响应中获取 / Offset cursor for pagination, obtained from the last response |
| sort_type | string | No | 排序方式：0=综合排序 1=最多点赞 2=最新发布 / Sort type: 0=Comprehensive, 1=Most Likes, 2=Latest |
| publish_time | string | No | 发布时间筛选：0=不限 1=最近一天 7=最近一周 180=最近半年 / Publish time filter: 0=Unlimited, 1=Last day, 7=Last week, 180=Last half year |
| filter_duration | string | No | 视频时长过滤：0=不限 0-1=一分钟以内 1-5=一到五分钟 5-10000=五分钟以上 / Video duration filter: 0=Unlimited, 0-1=Within 1 minute, 1-5=1 to 5 min… |
| content_type | string | No | 内容类型：0=不限 1=视频 2=图片 3=文章 / Content type: 0=All, 1=Video, 2=Picture, 3=Article |
| search_id | string | No | 搜索ID，用于翻页，从上一次请求返回的响应中获取 / Search ID for pagination, obtained from the last response |
| backtrace | string | No | 翻页回溯标识，用于翻页，从上一次请求返回的响应中获取 / Backtrace for pagination, obtained from the last response |

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

### `POST /api/u1/v1/douyin/search/fetch_general_search_v1`

- Summary: 获取综合搜索 V1/Fetch general search V1
- Capabilities: search
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_general_search_v1_api_v1_douyin_search_fetch_general_search_v1_post`
- Full contract: [`api-contracts/douyin-search-api.md#post-api-u1-v1-douyin-search-fetch-general-search-v1`](../api-contracts/douyin-search-api.md#post-api-u1-v1-douyin-search-fetch-general-search-v1)

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: `keyword`:string, `cursor`:integer, `sort_type`:string, `publish_time`:string, `filter_duration`:string, `content_type`:string, `search_id`:string, `backtrace`:string

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| keyword | string | No | 关键词 / Keyword |
| cursor | integer | No | 偏移游标，用于翻页，从上一次请求返回的响应中获取 / Offset cursor for pagination, obtained from the last response |
| sort_type | string | No | 排序方式：0=综合排序 1=最多点赞 2=最新发布 / Sort type: 0=Comprehensive, 1=Most Likes, 2=Latest |
| publish_time | string | No | 发布时间筛选：0=不限 1=最近一天 7=最近一周 180=最近半年 / Publish time filter: 0=Unlimited, 1=Last day, 7=Last week, 180=Last half year |
| filter_duration | string | No | 视频时长过滤：0=不限 0-1=一分钟以内 1-5=一到五分钟 5-10000=五分钟以上 / Video duration filter: 0=Unlimited, 0-1=Within 1 minute, 1-5=1 to 5 min… |
| content_type | string | No | 内容类型：0=不限 1=视频 2=图片 3=文章 / Content type: 0=All, 1=Video, 2=Picture, 3=Article |
| search_id | string | No | 搜索ID，用于翻页，从上一次请求返回的响应中获取 / Search ID for pagination, obtained from the last response |
| backtrace | string | No | 翻页回溯标识，用于翻页，从上一次请求返回的响应中获取 / Backtrace for pagination, obtained from the last response |

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

### `POST /api/u1/v1/douyin/search/fetch_general_search_v2`

- Summary: 获取综合搜索 V2/Fetch general search V2
- Capabilities: search
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_general_search_v2_api_v1_douyin_search_fetch_general_search_v2_post`
- Full contract: [`api-contracts/douyin-search-api.md#post-api-u1-v1-douyin-search-fetch-general-search-v2`](../api-contracts/douyin-search-api.md#post-api-u1-v1-douyin-search-fetch-general-search-v2)

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: `keyword`:string, `cursor`:integer, `sort_type`:string, `publish_time`:string, `filter_duration`:string, `content_type`:string, `search_id`:string, `backtrace`:string

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| keyword | string | No | 关键词 / Keyword |
| cursor | integer | No | 偏移游标，用于翻页，从上一次请求返回的响应中获取 / Offset cursor for pagination, obtained from the last response |
| sort_type | string | No | 排序方式：0=综合排序 1=最多点赞 2=最新发布 / Sort type: 0=Comprehensive, 1=Most Likes, 2=Latest |
| publish_time | string | No | 发布时间筛选：0=不限 1=最近一天 7=最近一周 180=最近半年 / Publish time filter: 0=Unlimited, 1=Last day, 7=Last week, 180=Last half year |
| filter_duration | string | No | 视频时长过滤：0=不限 0-1=一分钟以内 1-5=一到五分钟 5-10000=五分钟以上 / Video duration filter: 0=Unlimited, 0-1=Within 1 minute, 1-5=1 to 5 min… |
| content_type | string | No | 内容类型：0=不限 1=视频 2=图片 3=文章 / Content type: 0=All, 1=Video, 2=Picture, 3=Article |
| search_id | string | No | 搜索ID，用于翻页，从上一次请求返回的响应中获取 / Search ID for pagination, obtained from the last response |
| backtrace | string | No | 翻页回溯标识，用于翻页，从上一次请求返回的响应中获取 / Backtrace for pagination, obtained from the last response |

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

### `POST /api/u1/v1/douyin/search/fetch_general_search_v3`

- Summary: 获取综合搜索 V3/Fetch general search V3
- Capabilities: search
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_general_search_v3_api_v1_douyin_search_fetch_general_search_v3_post`
- Full contract: [`api-contracts/douyin-search-api.md#post-api-u1-v1-douyin-search-fetch-general-search-v3`](../api-contracts/douyin-search-api.md#post-api-u1-v1-douyin-search-fetch-general-search-v3)

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: `keyword`:string, `cursor`:integer, `sort_type`:string, `publish_time`:string, `filter_duration`:string, `content_type`:string, `search_id`:string, `backtrace`:string

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| keyword | string | No | 关键词 / Keyword |
| cursor | integer | No | 偏移游标，用于翻页，从上一次请求返回的响应中获取 / Offset cursor for pagination, obtained from the last response |
| sort_type | string | No | 排序方式：0=综合排序 1=最多点赞 2=最新发布 / Sort type: 0=Comprehensive, 1=Most Likes, 2=Latest |
| publish_time | string | No | 发布时间筛选：0=不限 1=最近一天 7=最近一周 180=最近半年 / Publish time filter: 0=Unlimited, 1=Last day, 7=Last week, 180=Last half year |
| filter_duration | string | No | 视频时长过滤：0=不限 0-1=一分钟以内 1-5=一到五分钟 5-10000=五分钟以上 / Video duration filter: 0=Unlimited, 0-1=Within 1 minute, 1-5=1 to 5 min… |
| content_type | string | No | 内容类型：0=不限 1=视频 2=图片 3=文章 / Content type: 0=All, 1=Video, 2=Picture, 3=Article |
| search_id | string | No | 搜索ID，用于翻页，从上一次请求返回的响应中获取 / Search ID for pagination, obtained from the last response |
| backtrace | string | No | 翻页回溯标识，用于翻页，从上一次请求返回的响应中获取 / Backtrace for pagination, obtained from the last response |

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

### `POST /api/u1/v1/douyin/search/fetch_image_search`

- Summary: 获取图片搜索/Fetch image search
- Capabilities: search
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_image_search_api_v1_douyin_search_fetch_image_search_post`
- Full contract: [`api-contracts/douyin-search-api.md#post-api-u1-v1-douyin-search-fetch-image-search`](../api-contracts/douyin-search-api.md#post-api-u1-v1-douyin-search-fetch-image-search)

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: `keyword`:string, `cursor`:integer, `sort_type`:string, `publish_time`:string, `filter_duration`:string, `content_type`:string, `search_id`:string, `backtrace`:string

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| keyword | string | No | 关键词 / Keyword |
| cursor | integer | No | 偏移游标，用于翻页，从上一次请求返回的响应中获取 / Offset cursor for pagination, obtained from the last response |
| sort_type | string | No | 排序方式：0=综合排序 1=最多点赞 2=最新发布 / Sort type: 0=Comprehensive, 1=Most Likes, 2=Latest |
| publish_time | string | No | 发布时间筛选：0=不限 1=最近一天 7=最近一周 180=最近半年 / Publish time filter: 0=Unlimited, 1=Last day, 7=Last week, 180=Last half year |
| filter_duration | string | No | 视频时长过滤：0=不限 0-1=一分钟以内 1-5=一到五分钟 5-10000=五分钟以上 / Video duration filter: 0=Unlimited, 0-1=Within 1 minute, 1-5=1 to 5 min… |
| content_type | string | No | 内容类型：0=不限 1=视频 2=图片 3=文章 / Content type: 0=All, 1=Video, 2=Picture, 3=Article |
| search_id | string | No | 搜索ID，用于翻页，从上一次请求返回的响应中获取 / Search ID for pagination, obtained from the last response |
| backtrace | string | No | 翻页回溯标识，用于翻页，从上一次请求返回的响应中获取 / Backtrace for pagination, obtained from the last response |

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

### `POST /api/u1/v1/douyin/search/fetch_image_search_v3`

- Summary: 获取图文搜索 V3/Fetch image-text search V3
- Capabilities: search
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_image_search_v3_api_v1_douyin_search_fetch_image_search_v3_post`
- Full contract: [`api-contracts/douyin-search-api.md#post-api-u1-v1-douyin-search-fetch-image-search-v3`](../api-contracts/douyin-search-api.md#post-api-u1-v1-douyin-search-fetch-image-search-v3)

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: `keyword*`:string, `cursor`:integer, `search_id`:string

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| keyword | string | Yes | 搜索关键词/Search keyword |
| cursor | integer | No | 翻页游标/Pagination cursor |
| search_id | string | No | 搜索ID/Search ID for pagination |

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

### `POST /api/u1/v1/douyin/search/fetch_live_search_v1`

- Summary: 获取直播搜索 V1/Fetch live search V1
- Capabilities: search / livestream
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_live_search_v1_api_v1_douyin_search_fetch_live_search_v1_post`
- Full contract: [`api-contracts/douyin-search-api.md#post-api-u1-v1-douyin-search-fetch-live-search-v1`](../api-contracts/douyin-search-api.md#post-api-u1-v1-douyin-search-fetch-live-search-v1)

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: `keyword`:string, `cursor`:integer, `sort_type`:string, `publish_time`:string, `filter_duration`:string, `content_type`:string, `search_id`:string, `backtrace`:string

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| keyword | string | No | 关键词 / Keyword |
| cursor | integer | No | 偏移游标，用于翻页，从上一次请求返回的响应中获取 / Offset cursor for pagination, obtained from the last response |
| sort_type | string | No | 排序方式：0=综合排序 1=最多点赞 2=最新发布 / Sort type: 0=Comprehensive, 1=Most Likes, 2=Latest |
| publish_time | string | No | 发布时间筛选：0=不限 1=最近一天 7=最近一周 180=最近半年 / Publish time filter: 0=Unlimited, 1=Last day, 7=Last week, 180=Last half year |
| filter_duration | string | No | 视频时长过滤：0=不限 0-1=一分钟以内 1-5=一到五分钟 5-10000=五分钟以上 / Video duration filter: 0=Unlimited, 0-1=Within 1 minute, 1-5=1 to 5 min… |
| content_type | string | No | 内容类型：0=不限 1=视频 2=图片 3=文章 / Content type: 0=All, 1=Video, 2=Picture, 3=Article |
| search_id | string | No | 搜索ID，用于翻页，从上一次请求返回的响应中获取 / Search ID for pagination, obtained from the last response |
| backtrace | string | No | 翻页回溯标识，用于翻页，从上一次请求返回的响应中获取 / Backtrace for pagination, obtained from the last response |

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

### `POST /api/u1/v1/douyin/search/fetch_multi_search`

- Summary: 获取多重搜索/Fetch multi-type search
- Capabilities: search
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_multi_search_api_v1_douyin_search_fetch_multi_search_post`
- Full contract: [`api-contracts/douyin-search-api.md#post-api-u1-v1-douyin-search-fetch-multi-search`](../api-contracts/douyin-search-api.md#post-api-u1-v1-douyin-search-fetch-multi-search)

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: `keyword`:string, `cursor`:integer, `sort_type`:string, `publish_time`:string, `filter_duration`:string, `content_type`:string, `search_id`:string, `backtrace`:string

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| keyword | string | No | 关键词 / Keyword |
| cursor | integer | No | 偏移游标，用于翻页，从上一次请求返回的响应中获取 / Offset cursor for pagination, obtained from the last response |
| sort_type | string | No | 排序方式：0=综合排序 1=最多点赞 2=最新发布 / Sort type: 0=Comprehensive, 1=Most Likes, 2=Latest |
| publish_time | string | No | 发布时间筛选：0=不限 1=最近一天 7=最近一周 180=最近半年 / Publish time filter: 0=Unlimited, 1=Last day, 7=Last week, 180=Last half year |
| filter_duration | string | No | 视频时长过滤：0=不限 0-1=一分钟以内 1-5=一到五分钟 5-10000=五分钟以上 / Video duration filter: 0=Unlimited, 0-1=Within 1 minute, 1-5=1 to 5 min… |
| content_type | string | No | 内容类型：0=不限 1=视频 2=图片 3=文章 / Content type: 0=All, 1=Video, 2=Picture, 3=Article |
| search_id | string | No | 搜索ID，用于翻页，从上一次请求返回的响应中获取 / Search ID for pagination, obtained from the last response |
| backtrace | string | No | 翻页回溯标识，用于翻页，从上一次请求返回的响应中获取 / Backtrace for pagination, obtained from the last response |

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

### `POST /api/u1/v1/douyin/search/fetch_music_search`

- Summary: 获取音乐搜索/Fetch music search
- Capabilities: search / music / audio
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_music_search_api_v1_douyin_search_fetch_music_search_post`
- Full contract: [`api-contracts/douyin-search-api.md#post-api-u1-v1-douyin-search-fetch-music-search`](../api-contracts/douyin-search-api.md#post-api-u1-v1-douyin-search-fetch-music-search)

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: `keyword`:string, `cursor`:integer, `sort_type`:string, `publish_time`:string, `filter_duration`:string, `content_type`:string, `search_id`:string, `backtrace`:string

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| keyword | string | No | 关键词 / Keyword |
| cursor | integer | No | 偏移游标，用于翻页，从上一次请求返回的响应中获取 / Offset cursor for pagination, obtained from the last response |
| sort_type | string | No | 排序方式：0=综合排序 1=最多点赞 2=最新发布 / Sort type: 0=Comprehensive, 1=Most Likes, 2=Latest |
| publish_time | string | No | 发布时间筛选：0=不限 1=最近一天 7=最近一周 180=最近半年 / Publish time filter: 0=Unlimited, 1=Last day, 7=Last week, 180=Last half year |
| filter_duration | string | No | 视频时长过滤：0=不限 0-1=一分钟以内 1-5=一到五分钟 5-10000=五分钟以上 / Video duration filter: 0=Unlimited, 0-1=Within 1 minute, 1-5=1 to 5 min… |
| content_type | string | No | 内容类型：0=不限 1=视频 2=图片 3=文章 / Content type: 0=All, 1=Video, 2=Picture, 3=Article |
| search_id | string | No | 搜索ID，用于翻页，从上一次请求返回的响应中获取 / Search ID for pagination, obtained from the last response |
| backtrace | string | No | 翻页回溯标识，用于翻页，从上一次请求返回的响应中获取 / Backtrace for pagination, obtained from the last response |

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

### `POST /api/u1/v1/douyin/search/fetch_school_search`

- Summary: 获取学校搜索/Fetch school search
- Capabilities: search
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_school_search_api_v1_douyin_search_fetch_school_search_post`
- Full contract: [`api-contracts/douyin-search-api.md#post-api-u1-v1-douyin-search-fetch-school-search`](../api-contracts/douyin-search-api.md#post-api-u1-v1-douyin-search-fetch-school-search)

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: `keyword`:string

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| keyword | string | No | 关键词，如学校名称或所在地区 / Keyword, such as school name or location |

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

### `POST /api/u1/v1/douyin/search/fetch_search_suggest`

- Summary: 获取搜索关键词推荐/Fetch search keyword suggestions
- Capabilities: search
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_search_suggest_api_v1_douyin_search_fetch_search_suggest_post`
- Full contract: [`api-contracts/douyin-search-api.md#post-api-u1-v1-douyin-search-fetch-search-suggest`](../api-contracts/douyin-search-api.md#post-api-u1-v1-douyin-search-fetch-search-suggest)

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: `keyword`:string

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| keyword | string | No | 需要联想的关键词/The keyword to be suggested |

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

### `POST /api/u1/v1/douyin/search/fetch_user_search`

- Summary: 获取用户搜索/Fetch user search
- Capabilities: search / profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_search_api_v1_douyin_search_fetch_user_search_post`
- Full contract: [`api-contracts/douyin-search-api.md#post-api-u1-v1-douyin-search-fetch-user-search`](../api-contracts/douyin-search-api.md#post-api-u1-v1-douyin-search-fetch-user-search)

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: `keyword`:string, `cursor`:integer, `douyin_user_fans`:string, `douyin_user_type`:string, `search_id`:string

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| keyword | string | No | 关键词 / Keyword |
| cursor | integer | No | 偏移游标，用于翻页，从上一次请求返回的响应中获取 / Offset cursor for pagination, obtained from the last response |
| douyin_user_fans | string | No | 粉丝数过滤：空=不限 0_1k=1千以下 1k_5k=1千到5千 5k_10k=5千到1万 10k_100k=1万到10万 100k_1M=10万到100万 1M_=100万以上 / Fans filter: empty=No limit… |
| douyin_user_type | string | No | 用户类型过滤：空=不限 300=创作者 900=小店 700=音乐人 800=明星 / User type filter: empty=No limit, 300=Creator, 900=Shop, 700=Musician, 800=… |
| search_id | string | No | 搜索ID，用于翻页，从上一次请求返回的响应中获取 / Search ID for pagination, obtained from the last response |

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

### `POST /api/u1/v1/douyin/search/fetch_user_search_v2`

- Summary: 获取用户搜索 V2/Fetch user search V2
- Capabilities: search / profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_search_v2_api_v1_douyin_search_fetch_user_search_v2_post`
- Full contract: [`api-contracts/douyin-search-api.md#post-api-u1-v1-douyin-search-fetch-user-search-v2`](../api-contracts/douyin-search-api.md#post-api-u1-v1-douyin-search-fetch-user-search-v2)

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: `keyword`:string, `cursor`:integer

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| keyword | string | No | 关键词 / Keyword |
| cursor | integer | No | 偏移游标，用于翻页，从上一次请求返回的响应中获取 / Offset cursor for pagination, obtained from the last response |

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

### `POST /api/u1/v1/douyin/search/fetch_video_search_v1`

- Summary: 获取视频搜索 V1/Fetch video search V1
- Capabilities: search / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_video_search_v1_api_v1_douyin_search_fetch_video_search_v1_post`
- Full contract: [`api-contracts/douyin-search-api.md#post-api-u1-v1-douyin-search-fetch-video-search-v1`](../api-contracts/douyin-search-api.md#post-api-u1-v1-douyin-search-fetch-video-search-v1)

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: `keyword`:string, `cursor`:integer, `sort_type`:string, `publish_time`:string, `filter_duration`:string, `content_type`:string, `search_id`:string, `backtrace`:string

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| keyword | string | No | 关键词 / Keyword |
| cursor | integer | No | 偏移游标，用于翻页，从上一次请求返回的响应中获取 / Offset cursor for pagination, obtained from the last response |
| sort_type | string | No | 排序方式：0=综合排序 1=最多点赞 2=最新发布 / Sort type: 0=Comprehensive, 1=Most Likes, 2=Latest |
| publish_time | string | No | 发布时间筛选：0=不限 1=最近一天 7=最近一周 180=最近半年 / Publish time filter: 0=Unlimited, 1=Last day, 7=Last week, 180=Last half year |
| filter_duration | string | No | 视频时长过滤：0=不限 0-1=一分钟以内 1-5=一到五分钟 5-10000=五分钟以上 / Video duration filter: 0=Unlimited, 0-1=Within 1 minute, 1-5=1 to 5 min… |
| content_type | string | No | 内容类型：0=不限 1=视频 2=图片 3=文章 / Content type: 0=All, 1=Video, 2=Picture, 3=Article |
| search_id | string | No | 搜索ID，用于翻页，从上一次请求返回的响应中获取 / Search ID for pagination, obtained from the last response |
| backtrace | string | No | 翻页回溯标识，用于翻页，从上一次请求返回的响应中获取 / Backtrace for pagination, obtained from the last response |

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

### `POST /api/u1/v1/douyin/search/fetch_video_search_v2`

- Summary: 获取视频搜索 V2/Fetch video search V2
- Capabilities: search / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_video_search_v2_api_v1_douyin_search_fetch_video_search_v2_post`
- Full contract: [`api-contracts/douyin-search-api.md#post-api-u1-v1-douyin-search-fetch-video-search-v2`](../api-contracts/douyin-search-api.md#post-api-u1-v1-douyin-search-fetch-video-search-v2)

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: `keyword`:string, `cursor`:integer, `sort_type`:string, `publish_time`:string, `filter_duration`:string, `content_type`:string, `search_id`:string, `backtrace`:string

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| keyword | string | No | 关键词 / Keyword |
| cursor | integer | No | 偏移游标，用于翻页，从上一次请求返回的响应中获取 / Offset cursor for pagination, obtained from the last response |
| sort_type | string | No | 排序方式：0=综合排序 1=最多点赞 2=最新发布 / Sort type: 0=Comprehensive, 1=Most Likes, 2=Latest |
| publish_time | string | No | 发布时间筛选：0=不限 1=最近一天 7=最近一周 180=最近半年 / Publish time filter: 0=Unlimited, 1=Last day, 7=Last week, 180=Last half year |
| filter_duration | string | No | 视频时长过滤：0=不限 0-1=一分钟以内 1-5=一到五分钟 5-10000=五分钟以上 / Video duration filter: 0=Unlimited, 0-1=Within 1 minute, 1-5=1 to 5 min… |
| content_type | string | No | 内容类型：0=不限 1=视频 2=图片 3=文章 / Content type: 0=All, 1=Video, 2=Picture, 3=Article |
| search_id | string | No | 搜索ID，用于翻页，从上一次请求返回的响应中获取 / Search ID for pagination, obtained from the last response |
| backtrace | string | No | 翻页回溯标识，用于翻页，从上一次请求返回的响应中获取 / Backtrace for pagination, obtained from the last response |

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

### `POST /api/u1/v1/douyin/search/fetch_vision_search`

- Summary: 获取图像识别搜索/Fetch vision search (image-based search)
- Capabilities: search
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_vision_search_api_v1_douyin_search_fetch_vision_search_post`
- Full contract: [`api-contracts/douyin-search-api.md#post-api-u1-v1-douyin-search-fetch-vision-search`](../api-contracts/douyin-search-api.md#post-api-u1-v1-douyin-search-fetch-vision-search)

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: `image_uri*`:string, `cursor`:integer, `search_id`:string, `search_source`:string, `detection`:string, `detection_index`:integer, `user_query`:string, `aweme_id`:string

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| image_uri | string | Yes | 图片URI，从抖音其他接口返回中获取（如视频详情、搜索结果、用户主页等接口的图片uri字段）/ Image URI obtained from other Douyin API responses (e.g., video details… |
| cursor | integer | No | 偏移游标，用于翻页，从上一次请求返回的响应中获取 / Offset cursor for pagination, obtained from the last response |
| search_id | string | No | 搜索ID，用于翻页，从上一次请求返回的响应中获取 / Search ID for pagination, obtained from the last response |
| search_source | string | No | 搜索来源：graphic_detail=图片详情页搜索, visual_normal_search=带关键词追加搜索 / Search source: graphic_detail=Image detail page search, vi… |
| detection | string | No | 检测区域坐标，格式为 x1,y1,x2,y2 / Detection area coordinates in format x1,y1,x2,y2 |
| detection_index | integer | No | 检测索引 / Detection index |
| user_query | string | No | 搜索关键词，仅当search_source=visual_normal_search时使用 / Search keyword, only used when search_source=visual_normal_search |
| aweme_id | string | No | 原视频ID，仅当search_source=visual_normal_search时使用 / Original video ID, only used when search_source=visual_normal_search |

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
