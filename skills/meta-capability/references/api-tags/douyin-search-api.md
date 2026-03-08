# Douyin-Search-API 路由详情

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 当前 tag 文件：`api-tags/douyin-search-api.md`
- 完整契约：[`api-contracts/douyin-search-api.md`](../api-contracts/douyin-search-api.md)
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T04:31:58+00:00`
- 路由数：`20`
- 常见能力：搜索 / 话题 / 主页/账号 / 作品详情 / 直播 / 音乐/音频
- 默认认证：请求头 `Authorization` Bearer
- 常见入参：`keyword`, `cursor`, `search_id`, `sort_type`, `publish_time`, `filter_duration`, `content_type`, `backtrace`, `douyin_user_fans`, `douyin_user_type`
- 标签说明：**(抖音搜索数据接口（当前最新版，请优先使用此目录下的接口而不是其他目录下的搜索接口）/Douyin-Search-API data endpoints (Current latest version, please use the interfaces in this directory first instead of the search interfaces in other directories))**

## 路由列表

### `POST /api/u1/v1/douyin/search/fetch_challenge_search_v1`

- 摘要：获取话题搜索 V1/Fetch hashtag search V1
- 能力：搜索 / 话题
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_challenge_search_v1_api_v1_douyin_search_fetch_challenge_search_v1_post`
- 完整契约：[`api-contracts/douyin-search-api.md#post-api-u1-v1-douyin-search-fetch-challenge-search-v1`](../api-contracts/douyin-search-api.md#post-api-u1-v1-douyin-search-fetch-challenge-search-v1)

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`keyword`:string, `cursor`:integer, `sort_type`:string, `publish_time`:string, `filter_duration`:string, `content_type`:string, `search_id`:string, `backtrace`:string

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyword | string | 否 | 关键词 / Keyword |
| cursor | integer | 否 | 偏移游标，用于翻页，从上一次请求返回的响应中获取 / Offset cursor for pagination, obtained from the last response |
| sort_type | string | 否 | 排序方式：0=综合排序 1=最多点赞 2=最新发布 / Sort type: 0=Comprehensive, 1=Most Likes, 2=Latest |
| publish_time | string | 否 | 发布时间筛选：0=不限 1=最近一天 7=最近一周 180=最近半年 / Publish time filter: 0=Unlimited, 1=Last day, 7=Last week, 180=Last half year |
| filter_duration | string | 否 | 视频时长过滤：0=不限 0-1=一分钟以内 1-5=一到五分钟 5-10000=五分钟以上 / Video duration filter: 0=Unlimited, 0-1=Within 1 minute, 1-5=1 to 5 min… |
| content_type | string | 否 | 内容类型：0=不限 1=视频 2=图片 3=文章 / Content type: 0=All, 1=Video, 2=Picture, 3=Article |
| search_id | string | 否 | 搜索ID，用于翻页，从上一次请求返回的响应中获取 / Search ID for pagination, obtained from the last response |
| backtrace | string | 否 | 翻页回溯标识，用于翻页，从上一次请求返回的响应中获取 / Backtrace for pagination, obtained from the last response |

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

### `POST /api/u1/v1/douyin/search/fetch_challenge_search_v2`

- 摘要：获取话题搜索 V2/Fetch hashtag search V2
- 能力：搜索 / 话题
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_challenge_search_v2_api_v1_douyin_search_fetch_challenge_search_v2_post`
- 完整契约：[`api-contracts/douyin-search-api.md#post-api-u1-v1-douyin-search-fetch-challenge-search-v2`](../api-contracts/douyin-search-api.md#post-api-u1-v1-douyin-search-fetch-challenge-search-v2)

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`keyword`:string, `cursor`:integer, `sort_type`:string, `publish_time`:string, `filter_duration`:string, `content_type`:string, `search_id`:string, `backtrace`:string

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyword | string | 否 | 关键词 / Keyword |
| cursor | integer | 否 | 偏移游标，用于翻页，从上一次请求返回的响应中获取 / Offset cursor for pagination, obtained from the last response |
| sort_type | string | 否 | 排序方式：0=综合排序 1=最多点赞 2=最新发布 / Sort type: 0=Comprehensive, 1=Most Likes, 2=Latest |
| publish_time | string | 否 | 发布时间筛选：0=不限 1=最近一天 7=最近一周 180=最近半年 / Publish time filter: 0=Unlimited, 1=Last day, 7=Last week, 180=Last half year |
| filter_duration | string | 否 | 视频时长过滤：0=不限 0-1=一分钟以内 1-5=一到五分钟 5-10000=五分钟以上 / Video duration filter: 0=Unlimited, 0-1=Within 1 minute, 1-5=1 to 5 min… |
| content_type | string | 否 | 内容类型：0=不限 1=视频 2=图片 3=文章 / Content type: 0=All, 1=Video, 2=Picture, 3=Article |
| search_id | string | 否 | 搜索ID，用于翻页，从上一次请求返回的响应中获取 / Search ID for pagination, obtained from the last response |
| backtrace | string | 否 | 翻页回溯标识，用于翻页，从上一次请求返回的响应中获取 / Backtrace for pagination, obtained from the last response |

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

### `POST /api/u1/v1/douyin/search/fetch_challenge_suggest`

- 摘要：获取话题推荐搜索/Fetch hashtag suggestions
- 能力：搜索 / 话题
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_challenge_suggest_api_v1_douyin_search_fetch_challenge_suggest_post`
- 完整契约：[`api-contracts/douyin-search-api.md#post-api-u1-v1-douyin-search-fetch-challenge-suggest`](../api-contracts/douyin-search-api.md#post-api-u1-v1-douyin-search-fetch-challenge-suggest)

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`keyword`:string

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyword | string | 否 | 关键词，如 '游戏' / Keyword, e.g., 'game' |

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

### `POST /api/u1/v1/douyin/search/fetch_discuss_search`

- 摘要：获取讨论搜索/Fetch discussion search
- 能力：搜索
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_discuss_search_api_v1_douyin_search_fetch_discuss_search_post`
- 完整契约：[`api-contracts/douyin-search-api.md#post-api-u1-v1-douyin-search-fetch-discuss-search`](../api-contracts/douyin-search-api.md#post-api-u1-v1-douyin-search-fetch-discuss-search)

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`keyword`:string, `cursor`:integer, `sort_type`:string, `publish_time`:string, `filter_duration`:string, `content_type`:string, `search_id`:string, `backtrace`:string

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyword | string | 否 | 关键词 / Keyword |
| cursor | integer | 否 | 偏移游标，用于翻页，从上一次请求返回的响应中获取 / Offset cursor for pagination, obtained from the last response |
| sort_type | string | 否 | 排序方式：0=综合排序 1=最多点赞 2=最新发布 / Sort type: 0=Comprehensive, 1=Most Likes, 2=Latest |
| publish_time | string | 否 | 发布时间筛选：0=不限 1=最近一天 7=最近一周 180=最近半年 / Publish time filter: 0=Unlimited, 1=Last day, 7=Last week, 180=Last half year |
| filter_duration | string | 否 | 视频时长过滤：0=不限 0-1=一分钟以内 1-5=一到五分钟 5-10000=五分钟以上 / Video duration filter: 0=Unlimited, 0-1=Within 1 minute, 1-5=1 to 5 min… |
| content_type | string | 否 | 内容类型：0=不限 1=视频 2=图片 3=文章 / Content type: 0=All, 1=Video, 2=Picture, 3=Article |
| search_id | string | 否 | 搜索ID，用于翻页，从上一次请求返回的响应中获取 / Search ID for pagination, obtained from the last response |
| backtrace | string | 否 | 翻页回溯标识，用于翻页，从上一次请求返回的响应中获取 / Backtrace for pagination, obtained from the last response |

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

### `POST /api/u1/v1/douyin/search/fetch_experience_search`

- 摘要：获取经验搜索/Fetch experience search
- 能力：搜索
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_experience_search_api_v1_douyin_search_fetch_experience_search_post`
- 完整契约：[`api-contracts/douyin-search-api.md#post-api-u1-v1-douyin-search-fetch-experience-search`](../api-contracts/douyin-search-api.md#post-api-u1-v1-douyin-search-fetch-experience-search)

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`keyword`:string, `cursor`:integer, `sort_type`:string, `publish_time`:string, `filter_duration`:string, `content_type`:string, `search_id`:string, `backtrace`:string

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyword | string | 否 | 关键词 / Keyword |
| cursor | integer | 否 | 偏移游标，用于翻页，从上一次请求返回的响应中获取 / Offset cursor for pagination, obtained from the last response |
| sort_type | string | 否 | 排序方式：0=综合排序 1=最多点赞 2=最新发布 / Sort type: 0=Comprehensive, 1=Most Likes, 2=Latest |
| publish_time | string | 否 | 发布时间筛选：0=不限 1=最近一天 7=最近一周 180=最近半年 / Publish time filter: 0=Unlimited, 1=Last day, 7=Last week, 180=Last half year |
| filter_duration | string | 否 | 视频时长过滤：0=不限 0-1=一分钟以内 1-5=一到五分钟 5-10000=五分钟以上 / Video duration filter: 0=Unlimited, 0-1=Within 1 minute, 1-5=1 to 5 min… |
| content_type | string | 否 | 内容类型：0=不限 1=视频 2=图片 3=文章 / Content type: 0=All, 1=Video, 2=Picture, 3=Article |
| search_id | string | 否 | 搜索ID，用于翻页，从上一次请求返回的响应中获取 / Search ID for pagination, obtained from the last response |
| backtrace | string | 否 | 翻页回溯标识，用于翻页，从上一次请求返回的响应中获取 / Backtrace for pagination, obtained from the last response |

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

### `POST /api/u1/v1/douyin/search/fetch_general_search_v1`

- 摘要：获取综合搜索 V1/Fetch general search V1
- 能力：搜索
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_general_search_v1_api_v1_douyin_search_fetch_general_search_v1_post`
- 完整契约：[`api-contracts/douyin-search-api.md#post-api-u1-v1-douyin-search-fetch-general-search-v1`](../api-contracts/douyin-search-api.md#post-api-u1-v1-douyin-search-fetch-general-search-v1)

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`keyword`:string, `cursor`:integer, `sort_type`:string, `publish_time`:string, `filter_duration`:string, `content_type`:string, `search_id`:string, `backtrace`:string

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyword | string | 否 | 关键词 / Keyword |
| cursor | integer | 否 | 偏移游标，用于翻页，从上一次请求返回的响应中获取 / Offset cursor for pagination, obtained from the last response |
| sort_type | string | 否 | 排序方式：0=综合排序 1=最多点赞 2=最新发布 / Sort type: 0=Comprehensive, 1=Most Likes, 2=Latest |
| publish_time | string | 否 | 发布时间筛选：0=不限 1=最近一天 7=最近一周 180=最近半年 / Publish time filter: 0=Unlimited, 1=Last day, 7=Last week, 180=Last half year |
| filter_duration | string | 否 | 视频时长过滤：0=不限 0-1=一分钟以内 1-5=一到五分钟 5-10000=五分钟以上 / Video duration filter: 0=Unlimited, 0-1=Within 1 minute, 1-5=1 to 5 min… |
| content_type | string | 否 | 内容类型：0=不限 1=视频 2=图片 3=文章 / Content type: 0=All, 1=Video, 2=Picture, 3=Article |
| search_id | string | 否 | 搜索ID，用于翻页，从上一次请求返回的响应中获取 / Search ID for pagination, obtained from the last response |
| backtrace | string | 否 | 翻页回溯标识，用于翻页，从上一次请求返回的响应中获取 / Backtrace for pagination, obtained from the last response |

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

### `POST /api/u1/v1/douyin/search/fetch_general_search_v2`

- 摘要：获取综合搜索 V2/Fetch general search V2
- 能力：搜索
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_general_search_v2_api_v1_douyin_search_fetch_general_search_v2_post`
- 完整契约：[`api-contracts/douyin-search-api.md#post-api-u1-v1-douyin-search-fetch-general-search-v2`](../api-contracts/douyin-search-api.md#post-api-u1-v1-douyin-search-fetch-general-search-v2)

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`keyword`:string, `cursor`:integer, `sort_type`:string, `publish_time`:string, `filter_duration`:string, `content_type`:string, `search_id`:string, `backtrace`:string

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyword | string | 否 | 关键词 / Keyword |
| cursor | integer | 否 | 偏移游标，用于翻页，从上一次请求返回的响应中获取 / Offset cursor for pagination, obtained from the last response |
| sort_type | string | 否 | 排序方式：0=综合排序 1=最多点赞 2=最新发布 / Sort type: 0=Comprehensive, 1=Most Likes, 2=Latest |
| publish_time | string | 否 | 发布时间筛选：0=不限 1=最近一天 7=最近一周 180=最近半年 / Publish time filter: 0=Unlimited, 1=Last day, 7=Last week, 180=Last half year |
| filter_duration | string | 否 | 视频时长过滤：0=不限 0-1=一分钟以内 1-5=一到五分钟 5-10000=五分钟以上 / Video duration filter: 0=Unlimited, 0-1=Within 1 minute, 1-5=1 to 5 min… |
| content_type | string | 否 | 内容类型：0=不限 1=视频 2=图片 3=文章 / Content type: 0=All, 1=Video, 2=Picture, 3=Article |
| search_id | string | 否 | 搜索ID，用于翻页，从上一次请求返回的响应中获取 / Search ID for pagination, obtained from the last response |
| backtrace | string | 否 | 翻页回溯标识，用于翻页，从上一次请求返回的响应中获取 / Backtrace for pagination, obtained from the last response |

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

### `POST /api/u1/v1/douyin/search/fetch_general_search_v3`

- 摘要：获取综合搜索 V3/Fetch general search V3
- 能力：搜索
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_general_search_v3_api_v1_douyin_search_fetch_general_search_v3_post`
- 完整契约：[`api-contracts/douyin-search-api.md#post-api-u1-v1-douyin-search-fetch-general-search-v3`](../api-contracts/douyin-search-api.md#post-api-u1-v1-douyin-search-fetch-general-search-v3)

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`keyword`:string, `cursor`:integer, `sort_type`:string, `publish_time`:string, `filter_duration`:string, `content_type`:string, `search_id`:string, `backtrace`:string

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyword | string | 否 | 关键词 / Keyword |
| cursor | integer | 否 | 偏移游标，用于翻页，从上一次请求返回的响应中获取 / Offset cursor for pagination, obtained from the last response |
| sort_type | string | 否 | 排序方式：0=综合排序 1=最多点赞 2=最新发布 / Sort type: 0=Comprehensive, 1=Most Likes, 2=Latest |
| publish_time | string | 否 | 发布时间筛选：0=不限 1=最近一天 7=最近一周 180=最近半年 / Publish time filter: 0=Unlimited, 1=Last day, 7=Last week, 180=Last half year |
| filter_duration | string | 否 | 视频时长过滤：0=不限 0-1=一分钟以内 1-5=一到五分钟 5-10000=五分钟以上 / Video duration filter: 0=Unlimited, 0-1=Within 1 minute, 1-5=1 to 5 min… |
| content_type | string | 否 | 内容类型：0=不限 1=视频 2=图片 3=文章 / Content type: 0=All, 1=Video, 2=Picture, 3=Article |
| search_id | string | 否 | 搜索ID，用于翻页，从上一次请求返回的响应中获取 / Search ID for pagination, obtained from the last response |
| backtrace | string | 否 | 翻页回溯标识，用于翻页，从上一次请求返回的响应中获取 / Backtrace for pagination, obtained from the last response |

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

### `POST /api/u1/v1/douyin/search/fetch_image_search`

- 摘要：获取图片搜索/Fetch image search
- 能力：搜索
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_image_search_api_v1_douyin_search_fetch_image_search_post`
- 完整契约：[`api-contracts/douyin-search-api.md#post-api-u1-v1-douyin-search-fetch-image-search`](../api-contracts/douyin-search-api.md#post-api-u1-v1-douyin-search-fetch-image-search)

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`keyword`:string, `cursor`:integer, `sort_type`:string, `publish_time`:string, `filter_duration`:string, `content_type`:string, `search_id`:string, `backtrace`:string

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyword | string | 否 | 关键词 / Keyword |
| cursor | integer | 否 | 偏移游标，用于翻页，从上一次请求返回的响应中获取 / Offset cursor for pagination, obtained from the last response |
| sort_type | string | 否 | 排序方式：0=综合排序 1=最多点赞 2=最新发布 / Sort type: 0=Comprehensive, 1=Most Likes, 2=Latest |
| publish_time | string | 否 | 发布时间筛选：0=不限 1=最近一天 7=最近一周 180=最近半年 / Publish time filter: 0=Unlimited, 1=Last day, 7=Last week, 180=Last half year |
| filter_duration | string | 否 | 视频时长过滤：0=不限 0-1=一分钟以内 1-5=一到五分钟 5-10000=五分钟以上 / Video duration filter: 0=Unlimited, 0-1=Within 1 minute, 1-5=1 to 5 min… |
| content_type | string | 否 | 内容类型：0=不限 1=视频 2=图片 3=文章 / Content type: 0=All, 1=Video, 2=Picture, 3=Article |
| search_id | string | 否 | 搜索ID，用于翻页，从上一次请求返回的响应中获取 / Search ID for pagination, obtained from the last response |
| backtrace | string | 否 | 翻页回溯标识，用于翻页，从上一次请求返回的响应中获取 / Backtrace for pagination, obtained from the last response |

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

### `POST /api/u1/v1/douyin/search/fetch_image_search_v3`

- 摘要：获取图文搜索 V3/Fetch image-text search V3
- 能力：搜索
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_image_search_v3_api_v1_douyin_search_fetch_image_search_v3_post`
- 完整契约：[`api-contracts/douyin-search-api.md#post-api-u1-v1-douyin-search-fetch-image-search-v3`](../api-contracts/douyin-search-api.md#post-api-u1-v1-douyin-search-fetch-image-search-v3)

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`keyword*`:string, `cursor`:integer, `search_id`:string

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyword | string | 是 | 搜索关键词/Search keyword |
| cursor | integer | 否 | 翻页游标/Pagination cursor |
| search_id | string | 否 | 搜索ID/Search ID for pagination |

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

### `POST /api/u1/v1/douyin/search/fetch_live_search_v1`

- 摘要：获取直播搜索 V1/Fetch live search V1
- 能力：搜索 / 直播
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_live_search_v1_api_v1_douyin_search_fetch_live_search_v1_post`
- 完整契约：[`api-contracts/douyin-search-api.md#post-api-u1-v1-douyin-search-fetch-live-search-v1`](../api-contracts/douyin-search-api.md#post-api-u1-v1-douyin-search-fetch-live-search-v1)

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`keyword`:string, `cursor`:integer, `sort_type`:string, `publish_time`:string, `filter_duration`:string, `content_type`:string, `search_id`:string, `backtrace`:string

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyword | string | 否 | 关键词 / Keyword |
| cursor | integer | 否 | 偏移游标，用于翻页，从上一次请求返回的响应中获取 / Offset cursor for pagination, obtained from the last response |
| sort_type | string | 否 | 排序方式：0=综合排序 1=最多点赞 2=最新发布 / Sort type: 0=Comprehensive, 1=Most Likes, 2=Latest |
| publish_time | string | 否 | 发布时间筛选：0=不限 1=最近一天 7=最近一周 180=最近半年 / Publish time filter: 0=Unlimited, 1=Last day, 7=Last week, 180=Last half year |
| filter_duration | string | 否 | 视频时长过滤：0=不限 0-1=一分钟以内 1-5=一到五分钟 5-10000=五分钟以上 / Video duration filter: 0=Unlimited, 0-1=Within 1 minute, 1-5=1 to 5 min… |
| content_type | string | 否 | 内容类型：0=不限 1=视频 2=图片 3=文章 / Content type: 0=All, 1=Video, 2=Picture, 3=Article |
| search_id | string | 否 | 搜索ID，用于翻页，从上一次请求返回的响应中获取 / Search ID for pagination, obtained from the last response |
| backtrace | string | 否 | 翻页回溯标识，用于翻页，从上一次请求返回的响应中获取 / Backtrace for pagination, obtained from the last response |

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

### `POST /api/u1/v1/douyin/search/fetch_multi_search`

- 摘要：获取多重搜索/Fetch multi-type search
- 能力：搜索
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_multi_search_api_v1_douyin_search_fetch_multi_search_post`
- 完整契约：[`api-contracts/douyin-search-api.md#post-api-u1-v1-douyin-search-fetch-multi-search`](../api-contracts/douyin-search-api.md#post-api-u1-v1-douyin-search-fetch-multi-search)

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`keyword`:string, `cursor`:integer, `sort_type`:string, `publish_time`:string, `filter_duration`:string, `content_type`:string, `search_id`:string, `backtrace`:string

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyword | string | 否 | 关键词 / Keyword |
| cursor | integer | 否 | 偏移游标，用于翻页，从上一次请求返回的响应中获取 / Offset cursor for pagination, obtained from the last response |
| sort_type | string | 否 | 排序方式：0=综合排序 1=最多点赞 2=最新发布 / Sort type: 0=Comprehensive, 1=Most Likes, 2=Latest |
| publish_time | string | 否 | 发布时间筛选：0=不限 1=最近一天 7=最近一周 180=最近半年 / Publish time filter: 0=Unlimited, 1=Last day, 7=Last week, 180=Last half year |
| filter_duration | string | 否 | 视频时长过滤：0=不限 0-1=一分钟以内 1-5=一到五分钟 5-10000=五分钟以上 / Video duration filter: 0=Unlimited, 0-1=Within 1 minute, 1-5=1 to 5 min… |
| content_type | string | 否 | 内容类型：0=不限 1=视频 2=图片 3=文章 / Content type: 0=All, 1=Video, 2=Picture, 3=Article |
| search_id | string | 否 | 搜索ID，用于翻页，从上一次请求返回的响应中获取 / Search ID for pagination, obtained from the last response |
| backtrace | string | 否 | 翻页回溯标识，用于翻页，从上一次请求返回的响应中获取 / Backtrace for pagination, obtained from the last response |

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

### `POST /api/u1/v1/douyin/search/fetch_music_search`

- 摘要：获取音乐搜索/Fetch music search
- 能力：搜索 / 音乐/音频
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_music_search_api_v1_douyin_search_fetch_music_search_post`
- 完整契约：[`api-contracts/douyin-search-api.md#post-api-u1-v1-douyin-search-fetch-music-search`](../api-contracts/douyin-search-api.md#post-api-u1-v1-douyin-search-fetch-music-search)

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`keyword`:string, `cursor`:integer, `sort_type`:string, `publish_time`:string, `filter_duration`:string, `content_type`:string, `search_id`:string, `backtrace`:string

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyword | string | 否 | 关键词 / Keyword |
| cursor | integer | 否 | 偏移游标，用于翻页，从上一次请求返回的响应中获取 / Offset cursor for pagination, obtained from the last response |
| sort_type | string | 否 | 排序方式：0=综合排序 1=最多点赞 2=最新发布 / Sort type: 0=Comprehensive, 1=Most Likes, 2=Latest |
| publish_time | string | 否 | 发布时间筛选：0=不限 1=最近一天 7=最近一周 180=最近半年 / Publish time filter: 0=Unlimited, 1=Last day, 7=Last week, 180=Last half year |
| filter_duration | string | 否 | 视频时长过滤：0=不限 0-1=一分钟以内 1-5=一到五分钟 5-10000=五分钟以上 / Video duration filter: 0=Unlimited, 0-1=Within 1 minute, 1-5=1 to 5 min… |
| content_type | string | 否 | 内容类型：0=不限 1=视频 2=图片 3=文章 / Content type: 0=All, 1=Video, 2=Picture, 3=Article |
| search_id | string | 否 | 搜索ID，用于翻页，从上一次请求返回的响应中获取 / Search ID for pagination, obtained from the last response |
| backtrace | string | 否 | 翻页回溯标识，用于翻页，从上一次请求返回的响应中获取 / Backtrace for pagination, obtained from the last response |

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

### `POST /api/u1/v1/douyin/search/fetch_school_search`

- 摘要：获取学校搜索/Fetch school search
- 能力：搜索
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_school_search_api_v1_douyin_search_fetch_school_search_post`
- 完整契约：[`api-contracts/douyin-search-api.md#post-api-u1-v1-douyin-search-fetch-school-search`](../api-contracts/douyin-search-api.md#post-api-u1-v1-douyin-search-fetch-school-search)

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`keyword`:string

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyword | string | 否 | 关键词，如学校名称或所在地区 / Keyword, such as school name or location |

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

### `POST /api/u1/v1/douyin/search/fetch_search_suggest`

- 摘要：获取搜索关键词推荐/Fetch search keyword suggestions
- 能力：搜索
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_search_suggest_api_v1_douyin_search_fetch_search_suggest_post`
- 完整契约：[`api-contracts/douyin-search-api.md#post-api-u1-v1-douyin-search-fetch-search-suggest`](../api-contracts/douyin-search-api.md#post-api-u1-v1-douyin-search-fetch-search-suggest)

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`keyword`:string

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyword | string | 否 | 需要联想的关键词/The keyword to be suggested |

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

### `POST /api/u1/v1/douyin/search/fetch_user_search`

- 摘要：获取用户搜索/Fetch user search
- 能力：搜索 / 主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_search_api_v1_douyin_search_fetch_user_search_post`
- 完整契约：[`api-contracts/douyin-search-api.md#post-api-u1-v1-douyin-search-fetch-user-search`](../api-contracts/douyin-search-api.md#post-api-u1-v1-douyin-search-fetch-user-search)

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`keyword`:string, `cursor`:integer, `douyin_user_fans`:string, `douyin_user_type`:string, `search_id`:string

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyword | string | 否 | 关键词 / Keyword |
| cursor | integer | 否 | 偏移游标，用于翻页，从上一次请求返回的响应中获取 / Offset cursor for pagination, obtained from the last response |
| douyin_user_fans | string | 否 | 粉丝数过滤：空=不限 0_1k=1千以下 1k_5k=1千到5千 5k_10k=5千到1万 10k_100k=1万到10万 100k_1M=10万到100万 1M_=100万以上 / Fans filter: empty=No limit… |
| douyin_user_type | string | 否 | 用户类型过滤：空=不限 300=创作者 900=小店 700=音乐人 800=明星 / User type filter: empty=No limit, 300=Creator, 900=Shop, 700=Musician, 800=… |
| search_id | string | 否 | 搜索ID，用于翻页，从上一次请求返回的响应中获取 / Search ID for pagination, obtained from the last response |

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

### `POST /api/u1/v1/douyin/search/fetch_user_search_v2`

- 摘要：获取用户搜索 V2/Fetch user search V2
- 能力：搜索 / 主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_search_v2_api_v1_douyin_search_fetch_user_search_v2_post`
- 完整契约：[`api-contracts/douyin-search-api.md#post-api-u1-v1-douyin-search-fetch-user-search-v2`](../api-contracts/douyin-search-api.md#post-api-u1-v1-douyin-search-fetch-user-search-v2)

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`keyword`:string, `cursor`:integer

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyword | string | 否 | 关键词 / Keyword |
| cursor | integer | 否 | 偏移游标，用于翻页，从上一次请求返回的响应中获取 / Offset cursor for pagination, obtained from the last response |

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

### `POST /api/u1/v1/douyin/search/fetch_video_search_v1`

- 摘要：获取视频搜索 V1/Fetch video search V1
- 能力：搜索 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_video_search_v1_api_v1_douyin_search_fetch_video_search_v1_post`
- 完整契约：[`api-contracts/douyin-search-api.md#post-api-u1-v1-douyin-search-fetch-video-search-v1`](../api-contracts/douyin-search-api.md#post-api-u1-v1-douyin-search-fetch-video-search-v1)

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`keyword`:string, `cursor`:integer, `sort_type`:string, `publish_time`:string, `filter_duration`:string, `content_type`:string, `search_id`:string, `backtrace`:string

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyword | string | 否 | 关键词 / Keyword |
| cursor | integer | 否 | 偏移游标，用于翻页，从上一次请求返回的响应中获取 / Offset cursor for pagination, obtained from the last response |
| sort_type | string | 否 | 排序方式：0=综合排序 1=最多点赞 2=最新发布 / Sort type: 0=Comprehensive, 1=Most Likes, 2=Latest |
| publish_time | string | 否 | 发布时间筛选：0=不限 1=最近一天 7=最近一周 180=最近半年 / Publish time filter: 0=Unlimited, 1=Last day, 7=Last week, 180=Last half year |
| filter_duration | string | 否 | 视频时长过滤：0=不限 0-1=一分钟以内 1-5=一到五分钟 5-10000=五分钟以上 / Video duration filter: 0=Unlimited, 0-1=Within 1 minute, 1-5=1 to 5 min… |
| content_type | string | 否 | 内容类型：0=不限 1=视频 2=图片 3=文章 / Content type: 0=All, 1=Video, 2=Picture, 3=Article |
| search_id | string | 否 | 搜索ID，用于翻页，从上一次请求返回的响应中获取 / Search ID for pagination, obtained from the last response |
| backtrace | string | 否 | 翻页回溯标识，用于翻页，从上一次请求返回的响应中获取 / Backtrace for pagination, obtained from the last response |

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

### `POST /api/u1/v1/douyin/search/fetch_video_search_v2`

- 摘要：获取视频搜索 V2/Fetch video search V2
- 能力：搜索 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_video_search_v2_api_v1_douyin_search_fetch_video_search_v2_post`
- 完整契约：[`api-contracts/douyin-search-api.md#post-api-u1-v1-douyin-search-fetch-video-search-v2`](../api-contracts/douyin-search-api.md#post-api-u1-v1-douyin-search-fetch-video-search-v2)

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`keyword`:string, `cursor`:integer, `sort_type`:string, `publish_time`:string, `filter_duration`:string, `content_type`:string, `search_id`:string, `backtrace`:string

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyword | string | 否 | 关键词 / Keyword |
| cursor | integer | 否 | 偏移游标，用于翻页，从上一次请求返回的响应中获取 / Offset cursor for pagination, obtained from the last response |
| sort_type | string | 否 | 排序方式：0=综合排序 1=最多点赞 2=最新发布 / Sort type: 0=Comprehensive, 1=Most Likes, 2=Latest |
| publish_time | string | 否 | 发布时间筛选：0=不限 1=最近一天 7=最近一周 180=最近半年 / Publish time filter: 0=Unlimited, 1=Last day, 7=Last week, 180=Last half year |
| filter_duration | string | 否 | 视频时长过滤：0=不限 0-1=一分钟以内 1-5=一到五分钟 5-10000=五分钟以上 / Video duration filter: 0=Unlimited, 0-1=Within 1 minute, 1-5=1 to 5 min… |
| content_type | string | 否 | 内容类型：0=不限 1=视频 2=图片 3=文章 / Content type: 0=All, 1=Video, 2=Picture, 3=Article |
| search_id | string | 否 | 搜索ID，用于翻页，从上一次请求返回的响应中获取 / Search ID for pagination, obtained from the last response |
| backtrace | string | 否 | 翻页回溯标识，用于翻页，从上一次请求返回的响应中获取 / Backtrace for pagination, obtained from the last response |

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

### `POST /api/u1/v1/douyin/search/fetch_vision_search`

- 摘要：获取图像识别搜索/Fetch vision search (image-based search)
- 能力：搜索
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_vision_search_api_v1_douyin_search_fetch_vision_search_post`
- 完整契约：[`api-contracts/douyin-search-api.md#post-api-u1-v1-douyin-search-fetch-vision-search`](../api-contracts/douyin-search-api.md#post-api-u1-v1-douyin-search-fetch-vision-search)

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`image_uri*`:string, `cursor`:integer, `search_id`:string, `search_source`:string, `detection`:string, `detection_index`:integer, `user_query`:string, `aweme_id`:string

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| image_uri | string | 是 | 图片URI，从抖音其他接口返回中获取（如视频详情、搜索结果、用户主页等接口的图片uri字段）/ Image URI obtained from other Douyin API responses (e.g., video details… |
| cursor | integer | 否 | 偏移游标，用于翻页，从上一次请求返回的响应中获取 / Offset cursor for pagination, obtained from the last response |
| search_id | string | 否 | 搜索ID，用于翻页，从上一次请求返回的响应中获取 / Search ID for pagination, obtained from the last response |
| search_source | string | 否 | 搜索来源：graphic_detail=图片详情页搜索, visual_normal_search=带关键词追加搜索 / Search source: graphic_detail=Image detail page search, vi… |
| detection | string | 否 | 检测区域坐标，格式为 x1,y1,x2,y2 / Detection area coordinates in format x1,y1,x2,y2 |
| detection_index | integer | 否 | 检测索引 / Detection index |
| user_query | string | 否 | 搜索关键词，仅当search_source=visual_normal_search时使用 / Search keyword, only used when search_source=visual_normal_search |
| aweme_id | string | 否 | 原视频ID，仅当search_source=visual_normal_search时使用 / Original video ID, only used when search_source=visual_normal_search |

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
