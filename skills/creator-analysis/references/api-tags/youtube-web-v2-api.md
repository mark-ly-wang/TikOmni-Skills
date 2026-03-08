# YouTube-Web-V2-API 路由详情

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 当前 tag 文件：`api-tags/youtube-web-v2-api.md`
- 完整契约：[`api-contracts/youtube-web-v2-api.md`](../api-contracts/youtube-web-v2-api.md)
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T04:31:58+00:00`
- 路由数：`16`
- 常见能力：作品详情 / 主页/账号 / 搜索 / 直播 / 评论
- 默认认证：请求头 `Authorization` Bearer
- 常见入参：`continuation_token`, `need_format`, `language_code`, `country_code`, `video_id`, `channel_id`, `video_url`, `sort_by`, `channel_url`, `search_query`
- 标签说明：**(YouTube Web V2数据接口/YouTube-Web-V2-API endpoints)**

## 路由列表

### `GET /api/u1/v1/youtube/web_v2/get_channel_description`

- 摘要：获取频道描述信息/Get channel description
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_channel_description_api_v1_youtube_web_v2_get_channel_description_get`
- 完整契约：[`api-contracts/youtube-web-v2-api.md#get-api-u1-v1-youtube-web-v2-get-channel-description`](../api-contracts/youtube-web-v2-api.md#get-api-u1-v1-youtube-web-v2-get-channel-description)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| channel_id | query | string | 否 | 频道ID（格式如：UCeu6U67OzJhV1KwBansH3Dg），可通过get_channel_id接口从频道URL获取/Channel ID, can be obtained from channel URL via get_cha… |
| continuation_token | query | string | 否 | 翻页标志（用于获取频道注册时间等高级信息）/Continuation token for getting advanced info like channel creation date |
| language_code | query | string | 否 | 语言代码（如zh-CN, en-US等）/Language code |
| country_code | query | string | 否 | 国家代码（如US, JP等）/Country code |
| need_format | query | boolean | 否 | 是否需要清洗数据，提取关键内容，移除冗余数据/Whether to clean and format the data |

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

### `GET /api/u1/v1/youtube/web_v2/get_channel_id`

- 摘要：从频道URL获取频道ID /Get channel ID from URL
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_channel_id_api_v1_youtube_web_v2_get_channel_id_get`
- 完整契约：[`api-contracts/youtube-web-v2-api.md#get-api-u1-v1-youtube-web-v2-get-channel-id`](../api-contracts/youtube-web-v2-api.md#get-api-u1-v1-youtube-web-v2-get-channel-id)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| channel_url | query | string | 是 | 频道URL/Channel URL，支持多种格式如：https://www.youtube.com/@username, https://www.youtube.com/channel/UCxxxxxx, https://www.yout… |

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

### `GET /api/u1/v1/youtube/web_v2/get_channel_shorts`

- 摘要：获取频道短视频列表/Get channel shorts
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_channel_shorts_api_v1_youtube_web_v2_get_channel_shorts_get`
- 完整契约：[`api-contracts/youtube-web-v2-api.md#get-api-u1-v1-youtube-web-v2-get-channel-shorts`](../api-contracts/youtube-web-v2-api.md#get-api-u1-v1-youtube-web-v2-get-channel-shorts)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| channel_id | query | string | 否 | 频道ID/Channel ID (e.g., UCuAXFkgsw1L7xaCfnd5JJOw) |
| channel_url | query | string | 否 | 频道URL/Channel URL (如果提供channel_id则忽略/Ignored if channel_id is provided) |
| continuation_token | query | string | 否 | 分页token/Pagination token |
| need_format | query | boolean | 否 | 是否格式化数据/Whether to format data |

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

### `GET /api/u1/v1/youtube/web_v2/get_channel_url`

- 摘要：从频道ID获取频道URL/Get channel URL from channel ID
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_channel_url_api_v1_youtube_web_v2_get_channel_url_get`
- 完整契约：[`api-contracts/youtube-web-v2-api.md#get-api-u1-v1-youtube-web-v2-get-channel-url`](../api-contracts/youtube-web-v2-api.md#get-api-u1-v1-youtube-web-v2-get-channel-url)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| channel_id | query | string | 是 | 频道ID/Channel ID (格式如：UCeu6U67OzJhV1KwBansH3Dg) |

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

### `GET /api/u1/v1/youtube/web_v2/get_channel_videos`

- 摘要：获取频道视频 /Get channel videos
- 能力：主页/账号 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_channel_videos_api_v1_youtube_web_v2_get_channel_videos_get`
- 完整契约：[`api-contracts/youtube-web-v2-api.md#get-api-u1-v1-youtube-web-v2-get-channel-videos`](../api-contracts/youtube-web-v2-api.md#get-api-u1-v1-youtube-web-v2-get-channel-videos)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| channel_id | query | string | 是 | 频道ID/Channel ID |
| language_code | query | string | 否 | 语言代码（如zh-CN, en-US等）/Language code |
| country_code | query | string | 否 | 国家代码（如US, JP等）/Country code |
| continuation_token | query | string | 否 | 分页token，用于获取下一页/Pagination token for next page |
| need_format | query | boolean | 否 | 是否需要清洗数据，提取关键内容，移除冗余数据/Whether to clean and format the data |

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

### `GET /api/u1/v1/youtube/web_v2/get_general_search`

- 摘要：综合搜索（支持过滤条件）/General search with filters
- 能力：搜索
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_general_search_api_v1_youtube_web_v2_get_general_search_get`
- 完整契约：[`api-contracts/youtube-web-v2-api.md#get-api-u1-v1-youtube-web-v2-get-general-search`](../api-contracts/youtube-web-v2-api.md#get-api-u1-v1-youtube-web-v2-get-general-search)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| search_query | query | string | 是 | 搜索关键字/Search keyword |
| language_code | query | string | 否 | 语言代码（如zh-CN, en-US等）/Language code |
| country_code | query | string | 否 | 国家代码（如US, CN等）/Country code |
| time_zone | query | string | 否 | 时区（如America/Los_Angeles, Asia/Shanghai等）/Time zone |
| upload_time | query | string enum[hour, today, week, month, year] | 否 | 上传时间过滤 \| Upload time filter |
| duration | query | string enum[short, medium, long] | 否 | 视频时长过滤 \| Duration filter |
| content_type | query | string enum[video, channel, playlist, movie] | 否 | 内容类型过滤 \| Content type filter |
| feature | query | string enum[live, 4k, hd, subtitles, creative_commons, 360, ...] | 否 | 特征过滤 \| Feature filter |
| sort_by | query | string enum[relevance, upload_date, view_count, rating] | 否 | 排序方式 \| Sort by |
| continuation_token | query | string | 否 | 翻页令牌/Pagination token |

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

### `GET /api/u1/v1/youtube/web_v2/get_related_videos`

- 摘要：获取视频相似内容/Get related videos
- 能力：作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_related_videos_api_v1_youtube_web_v2_get_related_videos_get`
- 完整契约：[`api-contracts/youtube-web-v2-api.md#get-api-u1-v1-youtube-web-v2-get-related-videos`](../api-contracts/youtube-web-v2-api.md#get-api-u1-v1-youtube-web-v2-get-related-videos)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| video_id | query | string | 否 | 视频ID/Video ID |
| video_url | query | string | 否 | 视频URL/Video URL (如果提供video_id则忽略此参数/Ignored if video_id is provided) |
| need_format | query | boolean | 否 | 是否格式化数据。true: 返回格式化的结构化数据，false: 返回原始API结构/Whether to format data. true: return formatted structured data, false: retur… |

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

### `GET /api/u1/v1/youtube/web_v2/get_search_suggestions`

- 摘要：获取搜索推荐词/Get search suggestions
- 能力：搜索
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_search_suggestions_api_v1_youtube_web_v2_get_search_suggestions_get`
- 完整契约：[`api-contracts/youtube-web-v2-api.md#get-api-u1-v1-youtube-web-v2-get-search-suggestions`](../api-contracts/youtube-web-v2-api.md#get-api-u1-v1-youtube-web-v2-get-search-suggestions)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| keyword | query | string | 是 | 搜索关键词/Search keyword |
| language | query | string | 否 | 语言代码/Language code (e.g., en, zh-cn, ja) |
| region | query | string | 否 | 地区代码/Region code (e.g., US, SG, CN, JP) |

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

### `GET /api/u1/v1/youtube/web_v2/get_shorts_search`

- 摘要：YouTube Shorts短视频搜索/YouTube Shorts search
- 能力：搜索
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_shorts_search_api_v1_youtube_web_v2_get_shorts_search_get`
- 完整契约：[`api-contracts/youtube-web-v2-api.md#get-api-u1-v1-youtube-web-v2-get-shorts-search`](../api-contracts/youtube-web-v2-api.md#get-api-u1-v1-youtube-web-v2-get-shorts-search)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| search_query | query | string | 是 | 搜索关键字/Search keyword |
| language_code | query | string | 否 | 语言代码（如zh-CN, en-US等）/Language code |
| country_code | query | string | 否 | 国家代码（如US, CN等）/Country code |
| time_zone | query | string | 否 | 时区（如America/Los_Angeles, Asia/Shanghai等）/Time zone |
| upload_time | query | string enum[hour, today, week, month, year] | 否 | 上传时间过滤 \| Upload time filter for Shorts |
| sort_by | query | string enum[relevance, upload_date, view_count, rating] | 否 | 排序方式 \| Sort by for Shorts |
| continuation_token | query | string | 否 | 翻页令牌/Pagination token |
| filter_mixed_content | query | boolean | 否 | 是否过滤混合内容（长视频），默认True / Filter mixed content (long videos), default True |

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

### `GET /api/u1/v1/youtube/web_v2/get_signed_stream_url`

- 摘要：获取已签名的视频流URL/Get signed video stream URL
- 能力：直播
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_signed_stream_url_api_v1_youtube_web_v2_get_signed_stream_url_get`
- 完整契约：[`api-contracts/youtube-web-v2-api.md#get-api-u1-v1-youtube-web-v2-get-signed-stream-url`](../api-contracts/youtube-web-v2-api.md#get-api-u1-v1-youtube-web-v2-get-signed-stream-url)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| video_id | query | string | 否 | 视频ID/Video ID |
| video_url | query | string | 否 | 视频URL/Video URL (如果提供video_id则忽略此参数/Ignored if video_id is provided) |
| itag | query | integer | 是 | 格式标识符 itag (从 get_video_streams 接口获取)/Format identifier itag (obtained from get_video_streams endpoint) |

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

### `GET /api/u1/v1/youtube/web_v2/get_video_comment_replies`

- 摘要：获取视频二级评论/Get video sub comments
- 能力：评论 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_video_comment_replies_api_v1_youtube_web_v2_get_video_comment_replies_get`
- 完整契约：[`api-contracts/youtube-web-v2-api.md#get-api-u1-v1-youtube-web-v2-get-video-comment-replies`](../api-contracts/youtube-web-v2-api.md#get-api-u1-v1-youtube-web-v2-get-video-comment-replies)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| continuation_token | query | string | 是 | 回复的continuation token（从一级评论的reply_continuation_token字段获取）/Reply continuation token from first-level comment |
| language_code | query | string | 否 | 语言代码（如zh-CN, en-US等）/Language code |
| country_code | query | string | 否 | 国家代码（如US, JP等）/Country code |
| need_format | query | boolean | 否 | 是否需要清洗数据，提取关键内容，移除冗余数据/Whether to clean and format the data |

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

### `GET /api/u1/v1/youtube/web_v2/get_video_comments`

- 摘要：获取视频评论/Get video comments
- 能力：评论 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_video_comments_api_v1_youtube_web_v2_get_video_comments_get`
- 完整契约：[`api-contracts/youtube-web-v2-api.md#get-api-u1-v1-youtube-web-v2-get-video-comments`](../api-contracts/youtube-web-v2-api.md#get-api-u1-v1-youtube-web-v2-get-video-comments)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| video_id | query | string | 是 | 视频ID/Video ID |
| language_code | query | string | 否 | 语言代码（如zh-CN, en-US等）/Language code |
| country_code | query | string | 否 | 国家代码（如US, JP等）/Country code |
| sort_by | query | string enum[top, newest] | 否 | 排序方式 \| Sort by |
| continuation_token | query | string | 否 | 翻页令牌/Pagination token |
| need_format | query | boolean | 否 | 是否需要清洗数据，提取关键内容，移除冗余数据/Whether to clean and format the data |

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

### `GET /api/u1/v1/youtube/web_v2/get_video_info`

- 摘要：获取视频详情 /Get video information
- 能力：作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_video_info_api_v1_youtube_web_v2_get_video_info_get`
- 完整契约：[`api-contracts/youtube-web-v2-api.md#get-api-u1-v1-youtube-web-v2-get-video-info`](../api-contracts/youtube-web-v2-api.md#get-api-u1-v1-youtube-web-v2-get-video-info)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| video_id | query | string | 是 | 视频ID/Video ID |
| language_code | query | string | 否 | 语言代码（如zh-CN, en-US等）/Language code |
| need_format | query | boolean | 否 | 是否需要清洗数据，提取关键内容，移除冗余数据/Whether to clean and format the data |

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

### `GET /api/u1/v1/youtube/web_v2/get_video_streams`

- 摘要：获取视频流信息/Get video streams info
- 能力：作品详情 / 直播
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_video_streams_api_v1_youtube_web_v2_get_video_streams_get`
- 完整契约：[`api-contracts/youtube-web-v2-api.md#get-api-u1-v1-youtube-web-v2-get-video-streams`](../api-contracts/youtube-web-v2-api.md#get-api-u1-v1-youtube-web-v2-get-video-streams)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| video_id | query | string | 否 | 视频ID/Video ID |
| video_url | query | string | 否 | 视频URL/Video URL (如果提供video_id则忽略此参数/Ignored if video_id is provided) |

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

### `GET /api/u1/v1/youtube/web_v2/get_video_streams_v2`

- 摘要：获取视频流信息 V2/Get video streams info V2
- 能力：作品详情 / 直播
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_video_streams_v2_api_v1_youtube_web_v2_get_video_streams_v2_get`
- 完整契约：[`api-contracts/youtube-web-v2-api.md#get-api-u1-v1-youtube-web-v2-get-video-streams-v2`](../api-contracts/youtube-web-v2-api.md#get-api-u1-v1-youtube-web-v2-get-video-streams-v2)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| video_id | query | string | 否 | 视频ID/Video ID |
| video_url | query | string | 否 | 视频URL/Video URL (如果提供video_id则忽略此参数/Ignored if video_id is provided) |

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

### `GET /api/u1/v1/youtube/web_v2/search_channels`

- 摘要：搜索频道/Search channels
- 能力：搜索 / 主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`search_channels_api_v1_youtube_web_v2_search_channels_get`
- 完整契约：[`api-contracts/youtube-web-v2-api.md#get-api-u1-v1-youtube-web-v2-search-channels`](../api-contracts/youtube-web-v2-api.md#get-api-u1-v1-youtube-web-v2-search-channels)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| keyword | query | string | 否 | 搜索关键词/Search keyword |
| continuation_token | query | string | 否 | 分页token/Pagination token |
| need_format | query | boolean | 否 | 是否格式化数据/Whether to format data |

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
