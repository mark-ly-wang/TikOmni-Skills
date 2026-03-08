# TikTok-App-V3-API 路由详情

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 当前 tag 文件：`api-tags/tiktok-app-v3-api.md`
- 完整契约：[`api-contracts/tiktok-app-v3-api.md`](../api-contracts/tiktok-app-v3-api.md)
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T04:31:58+00:00`
- 路由数：`75`
- 常见能力：作品详情 / 电商 / 主页/账号 / 搜索 / 直播 / 详情
- 默认认证：请求头 `Authorization` Bearer
- 常见入参：`count`, `offset`, `keyword`, `sort_type`, `cursor`, `region`, `sec_user_id`, `user_id`, `room_id`, `seller_id`
- 标签说明：**(TikTok-App-V3-API数据接口（当前最新版本）/TikTok-App-V3-API (Current latest version))**

## 路由列表

### `POST /api/u1/v1/tiktok/app/v3/TTencrypt_algorithm`

- 摘要：TikTok APP加密算法/TikTok APP encryption algorithm
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`TTencrypt_algorithm_api_v1_tiktok_app_v3_TTencrypt_algorithm_post`
- 完整契约：[`api-contracts/tiktok-app-v3-api.md#post-api-u1-v1-tiktok-app-v3-ttencrypt-algorithm`](../api-contracts/tiktok-app-v3-api.md#post-api-u1-v1-tiktok-app-v3-ttencrypt-algorithm)

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`url`:string, `data`:string, `device_info`{...}

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 否 | 需要加密的URL/URL to be encrypted |
| data | string | 否 | 如果有POST请求，请填写POST请求的数据参与加密计算/If there is a POST request, please fill in the data of the POST request to participate in… |
| device_info | object | 否 | 设备信息，可选参数，如果不填写则使用默认设备信息/Device information, optional parameter, if not filled in, the default device information is us… |

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

### `GET /api/u1/v1/tiktok/app/v3/add_video_play_count`

- 摘要：根据视频ID来增加作品的播放数/Increase the number of plays of the work according to the video ID
- 能力：作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`add_video_play_count_api_v1_tiktok_app_v3_add_video_play_count_get`
- 完整契约：[`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-add-video-play-count`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-add-video-play-count)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| aweme_type | query | integer | 是 | 作品类型/Video type |
| item_id | query | string | 是 | 作品id/Video id |

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

### `GET /api/u1/v1/tiktok/app/v3/check_live_room_online`

- 摘要：检测直播间是否在线/Check if live room is online
- 能力：直播
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`check_live_room_online_api_v1_tiktok_app_v3_check_live_room_online_get`
- 完整契约：[`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-check-live-room-online`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-check-live-room-online)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| room_id | query | string | 是 | 直播间id/Live room id |

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

### `POST /api/u1/v1/tiktok/app/v3/check_live_room_online_batch`

- 摘要：批量检测直播间是否在线/Batch check if live rooms are online
- 能力：直播
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`check_live_room_online_batch_api_v1_tiktok_app_v3_check_live_room_online_batch_post`
- 完整契约：[`api-contracts/tiktok-app-v3-api.md#post-api-u1-v1-tiktok-app-v3-check-live-room-online-batch`](../api-contracts/tiktok-app-v3-api.md#post-api-u1-v1-tiktok-app-v3-check-live-room-online-batch)

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`room_ids`[string]

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| room_ids | array<string> | 否 | 多个直播间ID组成的数组 / List of TikTok live room IDs |

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

### `POST /api/u1/v1/tiktok/app/v3/encrypt_decrypt_login_request`

- 摘要：加密或解密 TikTok APP 登录请求体/Encrypt or Decrypt TikTok APP login request body
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`encrypt_decrypt_login_request_api_v1_tiktok_app_v3_encrypt_decrypt_login_request_post`
- 完整契约：[`api-contracts/tiktok-app-v3-api.md#post-api-u1-v1-tiktok-app-v3-encrypt-decrypt-login-request`](../api-contracts/tiktok-app-v3-api.md#post-api-u1-v1-tiktok-app-v3-encrypt-decrypt-login-request)

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`username`:string, `password`:string, `mode`:string

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| username | string | 否 | Plaintext or encrypted username |
| password | string | 否 | Plaintext or encrypted password |
| mode | string enum[encrypt, decrypt] | 否 | Encrypt or decrypt the input string |

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

### `POST /api/u1/v1/tiktok/app/v3/fetch_content_translate`

- 摘要：获取内容翻译数据/Get content translation data
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_content_translate_api_v1_tiktok_app_v3_fetch_content_translate_post`
- 完整契约：[`api-contracts/tiktok-app-v3-api.md#post-api-u1-v1-tiktok-app-v3-fetch-content-translate`](../api-contracts/tiktok-app-v3-api.md#post-api-u1-v1-tiktok-app-v3-fetch-content-translate)

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`trg_lang`:string, `src_content`:string

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| trg_lang | string | 否 | 目标语言ISO639-1代码，例如：zh-Hans/ Target language ISO639-1 code, e.g. zh-Hans |
| src_content | string | 否 | 源语言内容，也就是需要翻译的内容/ Source language content, i.e. the content to be translated |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_creator_info`

- 摘要：获取带货创作者信息/Get shopping creator information
- 能力：创作者
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_creator_info_api_v1_tiktok_app_v3_fetch_creator_info_get`
- 完整契约：[`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-creator-info`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-creator-info)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| creator_uid | query | string | 是 | 创作者uid/Creator uid |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_creator_search_insights`

- 摘要：创作者搜索洞察/Creator Search Insights
- 能力：搜索 / 创作者 / 数据分析
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_creator_search_insights_api_v1_tiktok_app_v3_fetch_creator_search_insights_get`
- 完整契约：[`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-creator-search-insights`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-creator-search-insights)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| offset | query | integer | 否 | 分页偏移量/Pagination offset |
| limit | query | integer | 否 | 每页数量/Number per page |
| tab | query | string | 否 | 标签页类型/Tab type (all/content_gap/follower_searched/life_style/topics/challenges/sounds/hashtags) |
| language_filters | query | string | 否 | 语言过滤器，多个用逗号分隔/Language filters (id/de/en/es/fr/pt/vi/tr/ar/th/ja/ko) |
| category_filters | query | string | 否 | 分类过滤器，多个用逗号分隔/Category filters (Gaming/Fashion/Tourism/Science/Food/Sports) |
| creator_source | query | string | 否 | 创作者来源/Creator source |
| force_refresh | query | boolean | 否 | 是否强制刷新/Force refresh |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_creator_search_insights_detail`

- 摘要：创作者搜索洞察详情/Creator Search Insights Detail
- 能力：搜索 / 创作者 / 详情 / 数据分析
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_creator_search_insights_detail_api_v1_tiktok_app_v3_fetch_creator_search_insights_detail_get`
- 完整契约：[`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-creator-search-insights-detail`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-creator-search-insights-detail)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| query_id_str | query | string | 是 | 搜索词条ID，从 fetch_creator_search_insights 接口获取/Query ID from fetch_creator_search_insights |
| time_range | query | string | 否 | 时间范围/Time range (past_7_days/past_30_days/past_60_days/past_6_months/custom) |
| start_date | query | integer | 否 | 开始时间戳（秒），仅当 time_range=custom 时生效/Start timestamp (seconds), only for custom range |
| end_date | query | integer | 否 | 结束时间戳（秒），仅当 time_range=custom 时生效/End timestamp (seconds), only for custom range |
| dimension_list | query | string | 否 | 维度列表，多个用逗号分隔/Dimension list (gender/age/country) |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_creator_search_insights_trend`

- 摘要：创作者搜索洞察趋势/Creator Search Insights Trend
- 能力：搜索 / 热点/榜单 / 创作者 / 数据分析
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_creator_search_insights_trend_api_v1_tiktok_app_v3_fetch_creator_search_insights_trend_get`
- 完整契约：[`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-creator-search-insights-trend`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-creator-search-insights-trend)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| query_id_str | query | string | 是 | 搜索词条ID，从 fetch_creator_search_insights 接口获取/Query ID from fetch_creator_search_insights |
| from_tab_path | query | string | 否 | 来源标签路径/From tab path |
| query_analysis_required | query | boolean | 否 | 是否需要查询分析/Whether query analysis is required |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_creator_search_insights_videos`

- 摘要：创作者搜索洞察相关视频/Creator Search Insights Videos
- 能力：搜索 / 创作者 / 作品详情 / 数据分析
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_creator_search_insights_videos_api_v1_tiktok_app_v3_fetch_creator_search_insights_videos_get`
- 完整契约：[`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-creator-search-insights-videos`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-creator-search-insights-videos)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| keyword | query | string | 是 | 搜索关键词/Search keyword |
| offset | query | integer | 否 | 分页偏移量/Pagination offset |
| count | query | integer | 否 | 每页数量/Number per page |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_creator_showcase_product_list`

- 摘要：获取创作者橱窗商品列表/Get creator showcase product list
- 能力：创作者 / 电商
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_creator_showcase_product_list_api_v1_tiktok_app_v3_fetch_creator_showcase_product_list_get`
- 完整契约：[`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-creator-showcase-product-list`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-creator-showcase-product-list)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| kol_id | query | string | 是 | 创作者的sec_user_id/Creator's sec_user_id |
| count | query | integer | 否 | 数量/Number |
| next_scroll_param | query | string | 否 | 翻页参数/Page parameter |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_general_search_result`

- 摘要：获取指定关键词的综合搜索结果/Get comprehensive search results of specified keywords
- 能力：搜索
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_general_search_result_api_v1_tiktok_app_v3_fetch_general_search_result_get`
- 完整契约：[`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-general-search-result`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-general-search-result)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| keyword | query | string | 是 | 关键词/Keyword |
| offset | query | integer | 否 | 偏移量/Offset |
| count | query | integer | 否 | 数量/Number |
| sort_type | query | integer | 否 | 排序类型/Sort type |
| publish_time | query | integer | 否 | 发布时间/Publish time |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_hashtag_detail`

- 摘要：获取指定话题的详情数据/Get details of specified hashtag
- 能力：详情 / 话题
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_hashtag_detail_api_v1_tiktok_app_v3_fetch_hashtag_detail_get`
- 完整契约：[`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-hashtag-detail`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-hashtag-detail)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| ch_id | query | string | 是 | 话题id/Hashtag id |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_hashtag_search_result`

- 摘要：获取指定关键词的话题搜索结果/Get hashtag search results of specified keywords
- 能力：搜索 / 话题
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_hashtag_search_result_api_v1_tiktok_app_v3_fetch_hashtag_search_result_get`
- 完整契约：[`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-hashtag-search-result`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-hashtag-search-result)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| keyword | query | string | 是 | 关键词/Keyword |
| offset | query | integer | 否 | 偏移量/Offset |
| count | query | integer | 否 | 数量/Number |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_hashtag_video_list`

- 摘要：获取指定话题的作品数据/Get video list of specified hashtag
- 能力：作品详情 / 话题
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_hashtag_video_list_api_v1_tiktok_app_v3_fetch_hashtag_video_list_get`
- 完整契约：[`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-hashtag-video-list`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-hashtag-video-list)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| ch_id | query | string | 是 | 话题id/Hashtag id |
| cursor | query | integer | 否 | 游标/Cursor |
| count | query | integer | 否 | 数量/Number |

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

### `POST /api/u1/v1/tiktok/app/v3/fetch_home_feed`

- 摘要：获取主页视频推荐数据/Get home feed(recommend) video data
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_home_feed_api_v1_tiktok_app_v3_fetch_home_feed_post`
- 完整契约：[`api-contracts/tiktok-app-v3-api.md#post-api-u1-v1-tiktok-app-v3-fetch-home-feed`](../api-contracts/tiktok-app-v3-api.md#post-api-u1-v1-tiktok-app-v3-fetch-home-feed)

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`cookie`:string

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cookie | string | 否 | 用户自己的cookie，可选参数，用于接口返回数据的个性化推荐。/ User's own cookie, optional parameter, used for personalized recommendations of inter… |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_live_daily_rank`

- 摘要：获取直播每日榜单数据/Get live daily rank data
- 能力：直播
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_live_daily_rank_api_v1_tiktok_app_v3_fetch_live_daily_rank_get`
- 完整契约：[`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-live-daily-rank`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-live-daily-rank)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| anchor_id | query | string | 否 | 主播id/Anchor id |
| room_id | query | string | 否 | 直播间id/Live room id |
| rank_type | query | integer | 否 | 榜单类型/Rank type |
| region_type | query | integer | 否 | 地区类型/Region type |
| gap_interval | query | integer | 否 | 时间间隔/Time interval |
| cookie | query | string | 否 | 用户自己的cookie/User's own cookie |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_live_ranking_list`

- 摘要：获取直播间排行榜数据/Get live room ranking list
- 能力：直播
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_live_ranking_list_api_v1_tiktok_app_v3_fetch_live_ranking_list_get`
- 完整契约：[`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-live-ranking-list`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-live-ranking-list)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| room_id | query | string | 是 | 直播间id/Live room id |
| anchor_id | query | string | 是 | 主播id/Anchor id |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_live_room_info`

- 摘要：获取指定直播间的数据/Get data of specified live room
- 能力：直播
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_live_room_info_api_v1_tiktok_app_v3_fetch_live_room_info_get`
- 完整契约：[`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-live-room-info`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-live-room-info)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| room_id | query | string | 是 | 直播间id/Live room id |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_live_room_product_list`

- 摘要：获取直播间商品列表数据/Get live room product list data
- 能力：电商 / 直播
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_live_room_product_list_api_v1_tiktok_app_v3_fetch_live_room_product_list_get`
- 完整契约：[`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-live-room-product-list`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-live-room-product-list)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| room_id | query | string | 是 | 直播间id/Live room id |
| author_id | query | string | 是 | 主播id/Anchor id |
| page_size | query | integer | 否 | 数量/Number |
| offset | query | integer | 否 | 数量/Number |
| region | query | string | 否 | 地区/Region |
| cookie | query | string | 否 | 用户自己的cookie/User's own cookie |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_live_room_product_list_v2`

- 摘要：获取直播间商品列表数据 V2 /Get live room product list data V2
- 能力：电商 / 直播
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_live_room_product_list_v2_api_v1_tiktok_app_v3_fetch_live_room_product_list_v2_get`
- 完整契约：[`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-live-room-product-list-v2`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-live-room-product-list-v2)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| room_id | query | string | 是 | 直播间id/Live room id |
| author_id | query | string | 是 | 主播id/Anchor id |
| page_size | query | integer | 否 | 数量/Number |
| offset | query | integer | 否 | 数量/Number |
| region | query | string | 否 | 地区/Region |
| cookie | query | string | 否 | 用户自己的cookie/User's own cookie |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_live_search_result`

- 摘要：获取指定关键词的直播搜索结果/Get live search results of specified keywords
- 能力：搜索 / 直播
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_live_search_result_api_v1_tiktok_app_v3_fetch_live_search_result_get`
- 完整契约：[`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-live-search-result`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-live-search-result)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| keyword | query | string | 是 | 关键词/Keyword |
| offset | query | integer | 否 | 偏移量/Offset |
| count | query | integer | 否 | 数量/Number |
| region | query | string | 否 | 地区/Region |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_location_search`

- 摘要：获取地点搜索结果/Get location search results
- 能力：搜索
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_location_search_api_v1_tiktok_app_v3_fetch_location_search_get`
- 完整契约：[`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-location-search`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-location-search)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| keyword | query | string | 是 | 关键词/Keyword |
| offset | query | integer | 否 | 偏移量/Offset |
| count | query | integer | 否 | 数量/Number |

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

### `POST /api/u1/v1/tiktok/app/v3/fetch_multi_video`

- 摘要：批量获取视频信息/Batch Get Video Information
- 能力：作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_multi_video_api_v1_tiktok_app_v3_fetch_multi_video_post`
- 完整契约：[`api-contracts/tiktok-app-v3-api.md#post-api-u1-v1-tiktok-app-v3-fetch-multi-video`](../api-contracts/tiktok-app-v3-api.md#post-api-u1-v1-tiktok-app-v3-fetch-multi-video)

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：[string]

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| [] | array<string> | 是 | 作品id列表/Video id list |

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

### `POST /api/u1/v1/tiktok/app/v3/fetch_multi_video_v2`

- 摘要：批量获取视频信息 V2/Batch Get Video Information V2
- 能力：作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_multi_video_v2_api_v1_tiktok_app_v3_fetch_multi_video_v2_post`
- 完整契约：[`api-contracts/tiktok-app-v3-api.md#post-api-u1-v1-tiktok-app-v3-fetch-multi-video-v2`](../api-contracts/tiktok-app-v3-api.md#post-api-u1-v1-tiktok-app-v3-fetch-multi-video-v2)

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：[string]

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| [] | array<string> | 是 | 作品id列表/Video id list |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_music_chart_list`

- 摘要：音乐排行榜/Music Chart List
- 能力：音乐/音频
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_music_chart_list_api_v1_tiktok_app_v3_fetch_music_chart_list_get`
- 完整契约：[`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-music-chart-list`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-music-chart-list)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| scene | query | integer | 否 | 排行榜类型/Chart type (0: Top 50, 1: Viral 50) |
| cursor | query | integer | 否 | 分页游标/Pagination cursor |
| count | query | integer | 否 | 每页数量/Number per page (max 50) |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_music_detail`

- 摘要：获取指定音乐的详情数据/Get details of specified music
- 能力：详情 / 音乐/音频
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_music_detail_api_v1_tiktok_app_v3_fetch_music_detail_get`
- 完整契约：[`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-music-detail`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-music-detail)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| music_id | query | string | 是 | 音乐id/Music id |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_music_search_result`

- 摘要：获取指定关键词的音乐搜索结果/Get music search results of specified keywords
- 能力：搜索 / 音乐/音频
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_music_search_result_api_v1_tiktok_app_v3_fetch_music_search_result_get`
- 完整契约：[`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-music-search-result`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-music-search-result)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| keyword | query | string | 是 | 关键词/Keyword |
| offset | query | integer | 否 | 偏移量/Offset |
| count | query | integer | 否 | 数量/Number |
| filter_by | query | integer | 否 | 过滤类型/Filter type |
| sort_type | query | integer | 否 | 排序类型/Sort type |
| region | query | string | 否 | 地区/Region |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_music_video_list`

- 摘要：获取指定音乐的视频列表数据/Get video list of specified music
- 能力：作品详情 / 音乐/音频
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_music_video_list_api_v1_tiktok_app_v3_fetch_music_video_list_get`
- 完整契约：[`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-music-video-list`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-music-video-list)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| music_id | query | string | 是 | 音乐id/Music id |
| cursor | query | integer | 否 | 游标/Cursor |
| count | query | integer | 否 | 数量/Number |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_one_video`

- 摘要：获取单个作品数据/Get single video data
- 能力：作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_one_video_api_v1_tiktok_app_v3_fetch_one_video_get`
- 完整契约：[`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-one-video`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-one-video)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| aweme_id | query | string | 是 | 作品id/Video id |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_one_video_by_share_url`

- 摘要：根据分享链接获取单个作品数据/Get single video data by sharing link
- 能力：作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_one_video_by_share_url_api_v1_tiktok_app_v3_fetch_one_video_by_share_url_get`
- 完整契约：[`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-one-video-by-share-url`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-one-video-by-share-url)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| share_url | query | string | 是 | 分享链接/Share link |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_one_video_by_share_url_v2`

- 摘要：根据分享链接获取单个作品数据/Get single video data by sharing link
- 能力：作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_one_video_by_share_url_v2_api_v1_tiktok_app_v3_fetch_one_video_by_share_url_v2_get`
- 完整契约：[`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-one-video-by-share-url-v2`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-one-video-by-share-url-v2)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| share_url | query | string | 是 | 分享链接/Share link |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_one_video_v2`

- 摘要：获取单个作品数据 V2/Get single video data V2
- 能力：作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_one_video_v2_api_v1_tiktok_app_v3_fetch_one_video_v2_get`
- 完整契约：[`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-one-video-v2`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-one-video-v2)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| aweme_id | query | string | 是 | 作品id/Video id |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_one_video_v3`

- 摘要：获取单个作品数据 V3(支持国家参数)/Get single video data V3 (support country parameter)
- 能力：作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_one_video_v3_api_v1_tiktok_app_v3_fetch_one_video_v3_get`
- 完整契约：[`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-one-video-v3`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-one-video-v3)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| aweme_id | query | string | 是 | 作品id/Video id |
| region | query | string | 否 | 国家代码/Country code |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_product_detail`

- 摘要：获取商品详情数据（即将弃用，使用 fetch_product_detail_v2 代替）/Get product detail data (will be deprecated, use fetch_product_detail_v2 instead)
- 能力：详情 / 电商
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_product_detail_api_v1_tiktok_app_v3_fetch_product_detail_get`
- 完整契约：[`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-product-detail`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-product-detail)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| product_id | query | string | 是 | 商品id/Product id |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_product_detail_v2`

- 摘要：获取商品详情数据V2/Get product detail data V2
- 能力：详情 / 电商
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_product_detail_v2_api_v1_tiktok_app_v3_fetch_product_detail_v2_get`
- 完整契约：[`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-product-detail-v2`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-product-detail-v2)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| product_id | query | string | 是 | 商品id/Product id |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_product_detail_v3`

- 摘要：获取商品详情数据V3 / Get product detail data V3
- 能力：详情 / 电商
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_product_detail_v3_api_v1_tiktok_app_v3_fetch_product_detail_v3_get`
- 完整契约：[`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-product-detail-v3`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-product-detail-v3)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| product_id | query | string | 是 | 商品id / Product ID |
| region | query | string | 否 | 商品的国家/地区代码/ Country/region code of the product |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_product_detail_v4`

- 摘要：获取商品详情数据V4 / Get product detail data V4
- 能力：详情 / 电商
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_product_detail_v4_api_v1_tiktok_app_v3_fetch_product_detail_v4_get`
- 完整契约：[`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-product-detail-v4`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-product-detail-v4)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| product_id | query | string | 是 | 商品id / Product ID |
| region | query | string | 否 | 商品的国家/地区代码/ Country/region code of the product |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_product_id_by_share_link`

- 摘要：通过分享链接获取商品ID/Get Product ID by Share Link
- 能力：电商
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_product_id_by_share_link_api_v1_tiktok_app_v3_fetch_product_id_by_share_link_get`
- 完整契约：[`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-product-id-by-share-link`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-product-id-by-share-link)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| share_link | query | string | 是 | 分享链接/Share link |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_product_review`

- 摘要：获取商品评价数据/Get product review data
- 能力：电商
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_product_review_api_v1_tiktok_app_v3_fetch_product_review_get`
- 完整契约：[`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-product-review`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-product-review)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| product_id | query | string | 是 | 商品id/Product id |
| cursor | query | integer | 否 | 游标/Cursor |
| size | query | integer | 否 | 数量/Number |
| filter_id | query | integer | 否 | 筛选条件/Filter condition |
| sort_type | query | integer | 否 | 排序条件/Sorting conditions |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_product_search`

- 摘要：获取商品搜索结果/Get product search results
- 能力：搜索 / 电商
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_product_search_api_v1_tiktok_app_v3_fetch_product_search_get`
- 完整契约：[`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-product-search`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-product-search)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| keyword | query | string | 是 | 关键词/Keyword |
| cursor | query | integer | 否 | 游标/Cursor |
| count | query | integer | 否 | 数量/Number |
| sort_type | query | integer | 否 | 商品排序条件/Product sorting conditions |
| customer_review_four_star | query | boolean | 否 | 四星以上评价/Four-star or more reviews |
| have_discount | query | boolean | 否 | 有优惠/Having discount |
| min_price | query | string | 否 | 最低价格/Minimum price |
| max_price | query | string | 否 | 最高价格/Maximum price |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_share_qr_code`

- 摘要：获取分享二维码/Get share QR code
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_share_qr_code_api_v1_tiktok_app_v3_fetch_share_qr_code_get`
- 完整契约：[`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-share-qr-code`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-share-qr-code)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| object_id | query | string | 是 | 对象id/Object id |
| schema_type | query | integer | 否 | 模式类型/Schema type |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_share_short_link`

- 摘要：获取分享短链接/Get share short link
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_share_short_link_api_v1_tiktok_app_v3_fetch_share_short_link_get`
- 完整契约：[`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-share-short-link`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-share-short-link)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| url | query | string | 是 | 分享链接/Share link |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_shop_home`

- 摘要：获取商家主页数据/Get shop home page data
- 能力：主页/账号 / 电商
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_shop_home_api_v1_tiktok_app_v3_fetch_shop_home_get`
- 完整契约：[`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-shop-home`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-shop-home)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| page_id | query | string | 是 | 爬取的商家主页Page id/Page id of the crawled shop home page |
| seller_id | query | string | 是 | 商家id,店铺id/Seller id, shop id |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_shop_home_page_list`

- 摘要：获取商家主页Page列表数据/Get shop home page list data
- 能力：主页/账号 / 电商
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_shop_home_page_list_api_v1_tiktok_app_v3_fetch_shop_home_page_list_get`
- 完整契约：[`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-shop-home-page-list`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-shop-home-page-list)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| seller_id | query | string | 是 | 商家id,店铺id/Seller id, shop id |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_shop_id_by_share_link`

- 摘要：通过分享链接获取店铺ID/Get Shop ID by Share Link
- 能力：电商
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_shop_id_by_share_link_api_v1_tiktok_app_v3_fetch_shop_id_by_share_link_get`
- 完整契约：[`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-shop-id-by-share-link`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-shop-id-by-share-link)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| share_link | query | string | 是 | 分享链接/Share link |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_shop_info`

- 摘要：获取商家信息数据/Get shop information data
- 能力：电商
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_shop_info_api_v1_tiktok_app_v3_fetch_shop_info_get`
- 完整契约：[`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-shop-info`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-shop-info)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| shop_id | query | string | 是 | 商家id,店铺id/Seller id, shop id |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_shop_product_category`

- 摘要：获取商家产品分类数据/Get shop product category data
- 能力：电商
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_shop_product_category_api_v1_tiktok_app_v3_fetch_shop_product_category_get`
- 完整契约：[`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-shop-product-category`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-shop-product-category)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| seller_id | query | string | 是 | 商家id,店铺id/Seller id, shop id |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_shop_product_list`

- 摘要：获取商家商品列表数据/Get shop product list data
- 能力：电商
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_shop_product_list_api_v1_tiktok_app_v3_fetch_shop_product_list_get`
- 完整契约：[`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-shop-product-list`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-shop-product-list)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| seller_id | query | string | 是 | 商家id,店铺id/Seller id, shop id |
| scroll_params | query | string | 否 | 滚动参数，用于加载更多商品数据/Scroll parameter, used to load more product data |
| page_size | query | integer | 否 | 每页数量/Number per page |
| sort_field | query | integer | 否 | 排序字段/Sorting field |
| sort_order | query | integer | 否 | 排序方式/Sorting method |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_shop_product_list_v2`

- 摘要：获取商家商品列表数据 V2/Get shop product list data V2
- 能力：电商
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_shop_product_list_v2_api_v1_tiktok_app_v3_fetch_shop_product_list_v2_get`
- 完整契约：[`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-shop-product-list-v2`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-shop-product-list-v2)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| seller_id | query | string | 是 | 商家id,店铺id/Seller id, shop id |
| scroll_params | query | string | 否 | 滚动参数，用于加载更多商品数据/Scroll parameter, used to load more product data |
| page_size | query | integer | 否 | 每页数量/Number per page |
| sort_field | query | integer | 否 | 排序字段/Sorting field |
| sort_order | query | integer | 否 | 排序方式/Sorting method |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_shop_product_recommend`

- 摘要：获取商家商品推荐数据/Get shop product recommend data
- 能力：电商
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_shop_product_recommend_api_v1_tiktok_app_v3_fetch_shop_product_recommend_get`
- 完整契约：[`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-shop-product-recommend`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-shop-product-recommend)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| seller_id | query | string | 是 | 商家id,店铺id/Seller id, shop id |
| scroll_param | query | string | 否 | 滚动参数，用于加载更多商品数据/Scroll parameter, used to load more product data |
| page_size | query | integer | 否 | 每页数量/Number per page |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_similar_user_recommendations`

- 摘要：获取类似用户推荐/Similar User Recommendations
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_similar_user_recommendations_api_v1_tiktok_app_v3_fetch_similar_user_recommendations_get`
- 完整契约：[`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-similar-user-recommendations`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-similar-user-recommendations)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| sec_uid | query | string | 是 | 用户sec_uid/User sec_uid |
| page_token | query | string | 否 | 分页标记/Page token |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_user_country_by_username`

- 摘要：通过用户名获取用户账号国家地区/Get user account country by username
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_country_by_username_api_v1_tiktok_app_v3_fetch_user_country_by_username_get`
- 完整契约：[`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-user-country-by-username`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-user-country-by-username)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| username | query | string | 是 | 用户名/Username |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_user_follower_list`

- 摘要：获取指定用户的粉丝列表数据/Get follower list of specified user
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_follower_list_api_v1_tiktok_app_v3_fetch_user_follower_list_get`
- 完整契约：[`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-user-follower-list`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-user-follower-list)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| user_id | query | string | 否 | 用户ID/User ID (与sec_user_id二选一/One of user_id and sec_user_id) |
| sec_user_id | query | string | 否 | 用户sec_user_id/User sec_user_id (与user_id二选一/One of user_id and sec_user_id) |
| count | query | integer | 否 | 数量/Number |
| min_time | query | integer | 否 | 最小时间，用于翻页/Minimum time for paging |
| page_token | query | string | 否 | 翻页token/Page token |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_user_following_list`

- 摘要：获取指定用户的关注列表数据/Get following list of specified user
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_following_list_api_v1_tiktok_app_v3_fetch_user_following_list_get`
- 完整契约：[`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-user-following-list`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-user-following-list)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| user_id | query | string | 否 | 用户ID/User ID (与sec_user_id二选一/One of user_id and sec_user_id) |
| sec_user_id | query | string | 否 | 用户sec_user_id/User sec_user_id (与user_id二选一/One of user_id and sec_user_id) |
| count | query | integer | 否 | 数量/Number |
| min_time | query | integer | 否 | 最小时间，用于翻页/Minimum time for paging |
| page_token | query | string | 否 | 翻页token/Page token |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_user_like_videos`

- 摘要：获取用户喜欢作品数据/Get user like video data
- 能力：主页/账号 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_like_videos_api_v1_tiktok_app_v3_fetch_user_like_videos_get`
- 完整契约：[`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-user-like-videos`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-user-like-videos)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| sec_user_id | query | string | 是 | 用户sec_user_id/User sec_user_id |
| max_cursor | query | integer | 否 | 最大游标/Maximum cursor |
| counts | query | integer | 否 | 每页数量/Number per page |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_user_music_list`

- 摘要：获取用户音乐列表数据/Get user music list data
- 能力：主页/账号 / 音乐/音频
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_music_list_api_v1_tiktok_app_v3_fetch_user_music_list_get`
- 完整契约：[`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-user-music-list`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-user-music-list)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| sec_uid | query | string | 是 | 用户sec_uid/User sec_uid |
| cursor | query | integer | 否 | 游标/Cursor |
| count | query | integer | 否 | 数量/Number |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_user_post_videos`

- 摘要：获取用户主页作品数据 V1/Get user homepage video data V1
- 能力：主页/账号 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_post_videos_api_v1_tiktok_app_v3_fetch_user_post_videos_get`
- 完整契约：[`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-user-post-videos`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-user-post-videos)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| sec_user_id | query | string | 否 | 用户sec_user_id/User sec_user_id |
| unique_id | query | string | 否 | 用户unique_id/User unique_id |
| max_cursor | query | integer | 否 | 最大游标/Maximum cursor |
| count | query | integer | 否 | 每页数量/Number per page |
| sort_type | query | integer | 否 | 排序类型/Sort type |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_user_post_videos_v2`

- 摘要：获取用户主页作品数据 V2/Get user homepage video data V2
- 能力：主页/账号 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_post_videos_api_v1_tiktok_app_v3_fetch_user_post_videos_v2_get`
- 完整契约：[`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-user-post-videos-v2`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-user-post-videos-v2)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| sec_user_id | query | string | 否 | 用户sec_user_id/User sec_user_id |
| unique_id | query | string | 否 | 用户unique_id/User unique_id |
| max_cursor | query | integer | 否 | 最大游标/Maximum cursor |
| count | query | integer | 否 | 每页数量/Number per page |
| sort_type | query | integer | 否 | 排序类型/Sort type |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_user_post_videos_v3`

- 摘要：获取用户主页作品数据 V3（精简数据-更快速）/Get user homepage video data V3 (simplified data - faster)
- 能力：主页/账号 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_post_videos_v3_api_v1_tiktok_app_v3_fetch_user_post_videos_v3_get`
- 完整契约：[`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-user-post-videos-v3`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-user-post-videos-v3)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| sec_user_id | query | string | 否 | 用户sec_user_id/User sec_user_id |
| unique_id | query | string | 否 | 用户unique_id/User unique_id |
| max_cursor | query | integer | 否 | 最大游标/Maximum cursor |
| count | query | integer | 否 | 每页数量/Number per page |
| sort_type | query | integer | 否 | 排序类型/Sort type |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_user_repost_videos`

- 摘要：获取用户转发的作品数据/Get user repost video data
- 能力：主页/账号 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_repost_videos_api_v1_tiktok_app_v3_fetch_user_repost_videos_get`
- 完整契约：[`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-user-repost-videos`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-user-repost-videos)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| user_id | query | integer | 是 | 用户id/User id |
| offset | query | integer | 否 | 偏移量/Offset |
| count | query | integer | 否 | 数量/Number |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_user_search_result`

- 摘要：获取指定关键词的用户搜索结果/Get user search results of specified keywords
- 能力：搜索 / 主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_search_result_api_v1_tiktok_app_v3_fetch_user_search_result_get`
- 完整契约：[`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-user-search-result`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-user-search-result)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| keyword | query | string | 是 | 关键词/Keyword |
| offset | query | integer | 否 | 偏移量/Offset |
| count | query | integer | 否 | 数量/Number |
| user_search_follower_count | query | string | 否 | 根据粉丝数排序/Sort by number of followers |
| user_search_profile_type | query | string | 否 | 根据账号类型排序/Sort by account type |
| user_search_other_pref | query | string | 否 | 根据其他偏好排序/Sort by other preferences |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_video_comment_replies`

- 摘要：获取指定视频的评论回复数据/Get comment replies data of specified video
- 能力：评论 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_video_comments_reply_api_v1_tiktok_app_v3_fetch_video_comment_replies_get`
- 完整契约：[`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-video-comment-replies`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-video-comment-replies)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| item_id | query | string | 是 | 作品id/Video id |
| comment_id | query | string | 是 | 评论id/Comment id |
| cursor | query | integer | 否 | 游标/Cursor |
| count | query | integer | 否 | 数量/Number |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_video_comments`

- 摘要：获取单个视频评论数据/Get single video comments data
- 能力：评论 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_video_comments_api_v1_tiktok_app_v3_fetch_video_comments_get`
- 完整契约：[`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-video-comments`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-video-comments)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| aweme_id | query | string | 是 | 作品id/Video id |
| cursor | query | integer | 否 | 游标/Cursor |
| count | query | integer | 否 | 数量/Number |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_video_search_result`

- 摘要：获取指定关键词的视频搜索结果/Get video search results of specified keywords
- 能力：搜索 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_video_search_result_api_v1_tiktok_app_v3_fetch_video_search_result_get`
- 完整契约：[`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-video-search-result`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-video-search-result)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| keyword | query | string | 是 | 关键词/Keyword |
| offset | query | integer | 否 | 偏移量/Offset |
| count | query | integer | 否 | 数量/Number |
| sort_type | query | integer | 否 | 排序类型/Sort type |
| publish_time | query | integer | 否 | 发布时间/Publish time |
| region | query | string | 否 | 地区/Region |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_webcast_user_info`

- 摘要：获取指定 Webcast 用户的信息/Get information of specified Webcast user
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_webcast_user_info_api_v1_tiktok_app_v3_fetch_webcast_user_info_get`
- 完整契约：[`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-webcast-user-info`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-webcast-user-info)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| user_id | query | string | 否 | 用户uid （可选，纯数字）/User uid (optional, pure number) |
| sec_user_id | query | string | 否 | 用户sec_user_id/User sec_user_id |

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

### `GET /api/u1/v1/tiktok/app/v3/get_user_id_and_sec_user_id_by_username`

- 摘要：使用用户名获取用户 user_id 和 sec_user_id/Get user_id and sec_user_id by Username
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_user_id_and_sec_user_id_by_username_api_v1_tiktok_app_v3_get_user_id_and_sec_user_id_by_username_get`
- 完整契约：[`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-get-user-id-and-sec-user-id-by-username`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-get-user-id-and-sec-user-id-by-username)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| username | query | string | 是 | 用户名/Username |

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

### `GET /api/u1/v1/tiktok/app/v3/handler_user_profile`

- 摘要：获取指定用户的信息/Get information of specified user
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`handler_user_profile_api_v1_tiktok_app_v3_handler_user_profile_get`
- 完整契约：[`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-handler-user-profile`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-handler-user-profile)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| user_id | query | string | 否 | 用户uid （可选，纯数字）/User uid (optional, pure number) |
| sec_user_id | query | string | 否 | 用户sec_user_id/User sec_user_id |
| unique_id | query | string | 否 | 用户unique_id （用户名）/User unique_id (username) |

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

### `GET /api/u1/v1/tiktok/app/v3/open_tiktok_app_to_keyword_search`

- 摘要：生成TikTok分享链接，唤起TikTok APP，跳转指定关键词搜索结果/Generate TikTok share link, call TikTok APP, and jump to the specified keyword search result
- 能力：搜索
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`open_tiktok_app_to_keyword_search_api_v1_tiktok_app_v3_open_tiktok_app_to_keyword_search_get`
- 完整契约：[`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-open-tiktok-app-to-keyword-search`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-open-tiktok-app-to-keyword-search)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| keyword | query | string | 是 | 关键词/Keyword |

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

### `GET /api/u1/v1/tiktok/app/v3/open_tiktok_app_to_send_private_message`

- 摘要：生成TikTok分享链接，唤起TikTok APP，给指定用户发送私信/Generate TikTok share link, call TikTok APP, and send private messages to specified users
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`open_tiktok_app_to_send_private_message_api_v1_tiktok_app_v3_open_tiktok_app_to_send_private_message_get`
- 完整契约：[`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-open-tiktok-app-to-send-private-message`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-open-tiktok-app-to-send-private-message)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| uid | query | string | 是 | 用户id/User id |

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

### `GET /api/u1/v1/tiktok/app/v3/open_tiktok_app_to_user_profile`

- 摘要：生成TikTok分享链接，唤起TikTok APP，跳转指定用户主页/Generate TikTok share link, call TikTok APP, and jump to the specified user profile
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`open_tiktok_app_to_user_profile_api_v1_tiktok_app_v3_open_tiktok_app_to_user_profile_get`
- 完整契约：[`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-open-tiktok-app-to-user-profile`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-open-tiktok-app-to-user-profile)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| uid | query | string | 是 | 用户id/User id |

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

### `GET /api/u1/v1/tiktok/app/v3/open_tiktok_app_to_video_detail`

- 摘要：生成TikTok分享链接，唤起TikTok APP，跳转指定作品详情页/Generate TikTok share link, call TikTok APP, and jump to the specified video details page
- 能力：作品详情 / 详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`open_tiktok_app_to_video_detail_api_v1_tiktok_app_v3_open_tiktok_app_to_video_detail_get`
- 完整契约：[`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-open-tiktok-app-to-video-detail`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-open-tiktok-app-to-video-detail)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| aweme_id | query | string | 是 | 作品id/Video id |

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

### `GET /api/u1/v1/tiktok/app/v3/search_follower_list`

- 摘要：搜索粉丝列表/Search follower list
- 能力：搜索
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`search_follower_list_api_v1_tiktok_app_v3_search_follower_list_get`
- 完整契约：[`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-search-follower-list`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-search-follower-list)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| user_id | query | string | 是 | 用户ID/User ID |
| keyword | query | string | 是 | 搜索关键词/Search keyword |

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

### `GET /api/u1/v1/tiktok/app/v3/search_following_list`

- 摘要：搜索关注列表/Search following list
- 能力：搜索
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`search_following_list_api_v1_tiktok_app_v3_search_following_list_get`
- 完整契约：[`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-search-following-list`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-search-following-list)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| user_id | query | string | 是 | 用户ID/User ID |
| keyword | query | string | 是 | 搜索关键词/Search keyword |

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
