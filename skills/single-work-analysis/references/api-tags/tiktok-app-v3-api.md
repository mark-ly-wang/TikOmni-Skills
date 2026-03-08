# TikTok-App-V3-API Route Summary

- Back to index: [`api-capability-index.md`](../api-capability-index.md)
- Current tag file: `api-tags/tiktok-app-v3-api.md`
- Full contract: [`api-contracts/tiktok-app-v3-api.md`](../api-contracts/tiktok-app-v3-api.md)
- Source: `https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- Fetched at: `2026-03-08T06:54:04+00:00`
- Route count: `75`
- Common capabilities: content details / commerce / profiles / accounts / search / livestream / details
- Default auth: Header `Authorization` Bearer
- Common inputs: `count`, `offset`, `keyword`, `sort_type`, `cursor`, `region`, `sec_user_id`, `user_id`, `room_id`, `seller_id`
- Tag description: **(TikTok-App-V3-API数据接口（当前最新版本）/TikTok-App-V3-API (Current latest version))**

## Routes

### `POST /api/u1/v1/tiktok/app/v3/TTencrypt_algorithm`

- Summary: TikTok APP加密算法/TikTok APP encryption algorithm
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `TTencrypt_algorithm_api_v1_tiktok_app_v3_TTencrypt_algorithm_post`
- Full contract: [`api-contracts/tiktok-app-v3-api.md#post-api-u1-v1-tiktok-app-v3-ttencrypt-algorithm`](../api-contracts/tiktok-app-v3-api.md#post-api-u1-v1-tiktok-app-v3-ttencrypt-algorithm)

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: `url`:string, `data`:string, `device_info`{...}

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| url | string | No | 需要加密的URL/URL to be encrypted |
| data | string | No | 如果有POST请求，请填写POST请求的数据参与加密计算/If there is a POST request, please fill in the data of the POST request to participate in… |
| device_info | object | No | 设备信息，可选参数，如果不填写则使用默认设备信息/Device information, optional parameter, if not filled in, the default device information is us… |

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

### `GET /api/u1/v1/tiktok/app/v3/add_video_play_count`

- Summary: 根据视频ID来增加作品的播放数/Increase the number of plays of the work according to the video ID
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `add_video_play_count_api_v1_tiktok_app_v3_add_video_play_count_get`
- Full contract: [`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-add-video-play-count`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-add-video-play-count)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| aweme_type | query | integer | Yes | 作品类型/Video type |
| item_id | query | string | Yes | 作品id/Video id |

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

### `GET /api/u1/v1/tiktok/app/v3/check_live_room_online`

- Summary: 检测直播间是否在线/Check if live room is online
- Capabilities: livestream
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `check_live_room_online_api_v1_tiktok_app_v3_check_live_room_online_get`
- Full contract: [`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-check-live-room-online`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-check-live-room-online)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| room_id | query | string | Yes | 直播间id/Live room id |

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

### `POST /api/u1/v1/tiktok/app/v3/check_live_room_online_batch`

- Summary: 批量检测直播间是否在线/Batch check if live rooms are online
- Capabilities: livestream
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `check_live_room_online_batch_api_v1_tiktok_app_v3_check_live_room_online_batch_post`
- Full contract: [`api-contracts/tiktok-app-v3-api.md#post-api-u1-v1-tiktok-app-v3-check-live-room-online-batch`](../api-contracts/tiktok-app-v3-api.md#post-api-u1-v1-tiktok-app-v3-check-live-room-online-batch)

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: `room_ids`[string]

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| room_ids | array<string> | No | 多个直播间ID组成的数组 / List of TikTok live room IDs |

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

### `POST /api/u1/v1/tiktok/app/v3/encrypt_decrypt_login_request`

- Summary: 加密或解密 TikTok APP 登录请求体/Encrypt or Decrypt TikTok APP login request body
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `encrypt_decrypt_login_request_api_v1_tiktok_app_v3_encrypt_decrypt_login_request_post`
- Full contract: [`api-contracts/tiktok-app-v3-api.md#post-api-u1-v1-tiktok-app-v3-encrypt-decrypt-login-request`](../api-contracts/tiktok-app-v3-api.md#post-api-u1-v1-tiktok-app-v3-encrypt-decrypt-login-request)

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: `username`:string, `password`:string, `mode`:string

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| username | string | No | Plaintext or encrypted username |
| password | string | No | Plaintext or encrypted password |
| mode | string enum[encrypt, decrypt] | No | Encrypt or decrypt the input string |

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

### `POST /api/u1/v1/tiktok/app/v3/fetch_content_translate`

- Summary: 获取内容翻译数据/Get content translation data
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_content_translate_api_v1_tiktok_app_v3_fetch_content_translate_post`
- Full contract: [`api-contracts/tiktok-app-v3-api.md#post-api-u1-v1-tiktok-app-v3-fetch-content-translate`](../api-contracts/tiktok-app-v3-api.md#post-api-u1-v1-tiktok-app-v3-fetch-content-translate)

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: `trg_lang`:string, `src_content`:string

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| trg_lang | string | No | 目标语言ISO639-1代码，例如：zh-Hans/ Target language ISO639-1 code, e.g. zh-Hans |
| src_content | string | No | 源语言内容，也就是需要翻译的内容/ Source language content, i.e. the content to be translated |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_creator_info`

- Summary: 获取带货创作者信息/Get shopping creator information
- Capabilities: creators
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_creator_info_api_v1_tiktok_app_v3_fetch_creator_info_get`
- Full contract: [`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-creator-info`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-creator-info)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| creator_uid | query | string | Yes | 创作者uid/Creator uid |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_creator_search_insights`

- Summary: 创作者搜索洞察/Creator Search Insights
- Capabilities: search / creators / analytics
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_creator_search_insights_api_v1_tiktok_app_v3_fetch_creator_search_insights_get`
- Full contract: [`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-creator-search-insights`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-creator-search-insights)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| offset | query | integer | No | 分页偏移量/Pagination offset |
| limit | query | integer | No | 每页数量/Number per page |
| tab | query | string | No | 标签页类型/Tab type (all/content_gap/follower_searched/life_style/topics/challenges/sounds/hashtags) |
| language_filters | query | string | No | 语言过滤器，多个用逗号分隔/Language filters (id/de/en/es/fr/pt/vi/tr/ar/th/ja/ko) |
| category_filters | query | string | No | 分类过滤器，多个用逗号分隔/Category filters (Gaming/Fashion/Tourism/Science/Food/Sports) |
| creator_source | query | string | No | 创作者来源/Creator source |
| force_refresh | query | boolean | No | 是否强制刷新/Force refresh |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_creator_search_insights_detail`

- Summary: 创作者搜索洞察详情/Creator Search Insights Detail
- Capabilities: search / creators / details / analytics
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_creator_search_insights_detail_api_v1_tiktok_app_v3_fetch_creator_search_insights_detail_get`
- Full contract: [`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-creator-search-insights-detail`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-creator-search-insights-detail)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| query_id_str | query | string | Yes | 搜索词条ID，从 fetch_creator_search_insights 接口获取/Query ID from fetch_creator_search_insights |
| time_range | query | string | No | 时间范围/Time range (past_7_days/past_30_days/past_60_days/past_6_months/custom) |
| start_date | query | integer | No | 开始时间戳（秒），仅当 time_range=custom 时生效/Start timestamp (seconds), only for custom range |
| end_date | query | integer | No | 结束时间戳（秒），仅当 time_range=custom 时生效/End timestamp (seconds), only for custom range |
| dimension_list | query | string | No | 维度列表，多个用逗号分隔/Dimension list (gender/age/country) |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_creator_search_insights_trend`

- Summary: 创作者搜索洞察趋势/Creator Search Insights Trend
- Capabilities: search / trends / rankings / creators / analytics
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_creator_search_insights_trend_api_v1_tiktok_app_v3_fetch_creator_search_insights_trend_get`
- Full contract: [`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-creator-search-insights-trend`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-creator-search-insights-trend)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| query_id_str | query | string | Yes | 搜索词条ID，从 fetch_creator_search_insights 接口获取/Query ID from fetch_creator_search_insights |
| from_tab_path | query | string | No | 来源标签路径/From tab path |
| query_analysis_required | query | boolean | No | 是否需要查询分析/Whether query analysis is required |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_creator_search_insights_videos`

- Summary: 创作者搜索洞察相关视频/Creator Search Insights Videos
- Capabilities: search / creators / content details / analytics
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_creator_search_insights_videos_api_v1_tiktok_app_v3_fetch_creator_search_insights_videos_get`
- Full contract: [`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-creator-search-insights-videos`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-creator-search-insights-videos)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| keyword | query | string | Yes | 搜索关键词/Search keyword |
| offset | query | integer | No | 分页偏移量/Pagination offset |
| count | query | integer | No | 每页数量/Number per page |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_creator_showcase_product_list`

- Summary: 获取创作者橱窗商品列表/Get creator showcase product list
- Capabilities: creators / commerce
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_creator_showcase_product_list_api_v1_tiktok_app_v3_fetch_creator_showcase_product_list_get`
- Full contract: [`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-creator-showcase-product-list`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-creator-showcase-product-list)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| kol_id | query | string | Yes | 创作者的sec_user_id/Creator's sec_user_id |
| count | query | integer | No | 数量/Number |
| next_scroll_param | query | string | No | 翻页参数/Page parameter |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_general_search_result`

- Summary: 获取指定关键词的综合搜索结果/Get comprehensive search results of specified keywords
- Capabilities: search
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_general_search_result_api_v1_tiktok_app_v3_fetch_general_search_result_get`
- Full contract: [`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-general-search-result`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-general-search-result)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| keyword | query | string | Yes | 关键词/Keyword |
| offset | query | integer | No | 偏移量/Offset |
| count | query | integer | No | 数量/Number |
| sort_type | query | integer | No | 排序类型/Sort type |
| publish_time | query | integer | No | 发布时间/Publish time |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_hashtag_detail`

- Summary: 获取指定话题的详情数据/Get details of specified hashtag
- Capabilities: details / topics
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_hashtag_detail_api_v1_tiktok_app_v3_fetch_hashtag_detail_get`
- Full contract: [`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-hashtag-detail`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-hashtag-detail)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| ch_id | query | string | Yes | 话题id/Hashtag id |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_hashtag_search_result`

- Summary: 获取指定关键词的话题搜索结果/Get hashtag search results of specified keywords
- Capabilities: search / topics
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_hashtag_search_result_api_v1_tiktok_app_v3_fetch_hashtag_search_result_get`
- Full contract: [`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-hashtag-search-result`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-hashtag-search-result)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| keyword | query | string | Yes | 关键词/Keyword |
| offset | query | integer | No | 偏移量/Offset |
| count | query | integer | No | 数量/Number |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_hashtag_video_list`

- Summary: 获取指定话题的作品数据/Get video list of specified hashtag
- Capabilities: content details / topics
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_hashtag_video_list_api_v1_tiktok_app_v3_fetch_hashtag_video_list_get`
- Full contract: [`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-hashtag-video-list`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-hashtag-video-list)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| ch_id | query | string | Yes | 话题id/Hashtag id |
| cursor | query | integer | No | 游标/Cursor |
| count | query | integer | No | 数量/Number |

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

### `POST /api/u1/v1/tiktok/app/v3/fetch_home_feed`

- Summary: 获取主页视频推荐数据/Get home feed(recommend) video data
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_home_feed_api_v1_tiktok_app_v3_fetch_home_feed_post`
- Full contract: [`api-contracts/tiktok-app-v3-api.md#post-api-u1-v1-tiktok-app-v3-fetch-home-feed`](../api-contracts/tiktok-app-v3-api.md#post-api-u1-v1-tiktok-app-v3-fetch-home-feed)

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: `cookie`:string

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| cookie | string | No | 用户自己的cookie，可选参数，用于接口返回数据的个性化推荐。/ User's own cookie, optional parameter, used for personalized recommendations of inter… |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_live_daily_rank`

- Summary: 获取直播每日榜单数据/Get live daily rank data
- Capabilities: livestream
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_live_daily_rank_api_v1_tiktok_app_v3_fetch_live_daily_rank_get`
- Full contract: [`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-live-daily-rank`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-live-daily-rank)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| anchor_id | query | string | No | 主播id/Anchor id |
| room_id | query | string | No | 直播间id/Live room id |
| rank_type | query | integer | No | 榜单类型/Rank type |
| region_type | query | integer | No | 地区类型/Region type |
| gap_interval | query | integer | No | 时间间隔/Time interval |
| cookie | query | string | No | 用户自己的cookie/User's own cookie |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_live_ranking_list`

- Summary: 获取直播间排行榜数据/Get live room ranking list
- Capabilities: livestream
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_live_ranking_list_api_v1_tiktok_app_v3_fetch_live_ranking_list_get`
- Full contract: [`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-live-ranking-list`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-live-ranking-list)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| room_id | query | string | Yes | 直播间id/Live room id |
| anchor_id | query | string | Yes | 主播id/Anchor id |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_live_room_info`

- Summary: 获取指定直播间的数据/Get data of specified live room
- Capabilities: livestream
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_live_room_info_api_v1_tiktok_app_v3_fetch_live_room_info_get`
- Full contract: [`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-live-room-info`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-live-room-info)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| room_id | query | string | Yes | 直播间id/Live room id |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_live_room_product_list`

- Summary: 获取直播间商品列表数据/Get live room product list data
- Capabilities: commerce / livestream
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_live_room_product_list_api_v1_tiktok_app_v3_fetch_live_room_product_list_get`
- Full contract: [`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-live-room-product-list`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-live-room-product-list)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| room_id | query | string | Yes | 直播间id/Live room id |
| author_id | query | string | Yes | 主播id/Anchor id |
| page_size | query | integer | No | 数量/Number |
| offset | query | integer | No | 数量/Number |
| region | query | string | No | 地区/Region |
| cookie | query | string | No | 用户自己的cookie/User's own cookie |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_live_room_product_list_v2`

- Summary: 获取直播间商品列表数据 V2 /Get live room product list data V2
- Capabilities: commerce / livestream
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_live_room_product_list_v2_api_v1_tiktok_app_v3_fetch_live_room_product_list_v2_get`
- Full contract: [`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-live-room-product-list-v2`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-live-room-product-list-v2)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| room_id | query | string | Yes | 直播间id/Live room id |
| author_id | query | string | Yes | 主播id/Anchor id |
| page_size | query | integer | No | 数量/Number |
| offset | query | integer | No | 数量/Number |
| region | query | string | No | 地区/Region |
| cookie | query | string | No | 用户自己的cookie/User's own cookie |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_live_search_result`

- Summary: 获取指定关键词的直播搜索结果/Get live search results of specified keywords
- Capabilities: search / livestream
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_live_search_result_api_v1_tiktok_app_v3_fetch_live_search_result_get`
- Full contract: [`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-live-search-result`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-live-search-result)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| keyword | query | string | Yes | 关键词/Keyword |
| offset | query | integer | No | 偏移量/Offset |
| count | query | integer | No | 数量/Number |
| region | query | string | No | 地区/Region |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_location_search`

- Summary: 获取地点搜索结果/Get location search results
- Capabilities: search
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_location_search_api_v1_tiktok_app_v3_fetch_location_search_get`
- Full contract: [`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-location-search`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-location-search)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| keyword | query | string | Yes | 关键词/Keyword |
| offset | query | integer | No | 偏移量/Offset |
| count | query | integer | No | 数量/Number |

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

### `POST /api/u1/v1/tiktok/app/v3/fetch_multi_video`

- Summary: 批量获取视频信息/Batch Get Video Information
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_multi_video_api_v1_tiktok_app_v3_fetch_multi_video_post`
- Full contract: [`api-contracts/tiktok-app-v3-api.md#post-api-u1-v1-tiktok-app-v3-fetch-multi-video`](../api-contracts/tiktok-app-v3-api.md#post-api-u1-v1-tiktok-app-v3-fetch-multi-video)

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: [string]

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| [] | array<string> | Yes | 作品id列表/Video id list |

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

### `POST /api/u1/v1/tiktok/app/v3/fetch_multi_video_v2`

- Summary: 批量获取视频信息 V2/Batch Get Video Information V2
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_multi_video_v2_api_v1_tiktok_app_v3_fetch_multi_video_v2_post`
- Full contract: [`api-contracts/tiktok-app-v3-api.md#post-api-u1-v1-tiktok-app-v3-fetch-multi-video-v2`](../api-contracts/tiktok-app-v3-api.md#post-api-u1-v1-tiktok-app-v3-fetch-multi-video-v2)

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: [string]

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| [] | array<string> | Yes | 作品id列表/Video id list |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_music_chart_list`

- Summary: 音乐排行榜/Music Chart List
- Capabilities: music / audio
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_music_chart_list_api_v1_tiktok_app_v3_fetch_music_chart_list_get`
- Full contract: [`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-music-chart-list`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-music-chart-list)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| scene | query | integer | No | 排行榜类型/Chart type (0: Top 50, 1: Viral 50) |
| cursor | query | integer | No | 分页游标/Pagination cursor |
| count | query | integer | No | 每页数量/Number per page (max 50) |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_music_detail`

- Summary: 获取指定音乐的详情数据/Get details of specified music
- Capabilities: details / music / audio
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_music_detail_api_v1_tiktok_app_v3_fetch_music_detail_get`
- Full contract: [`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-music-detail`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-music-detail)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| music_id | query | string | Yes | 音乐id/Music id |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_music_search_result`

- Summary: 获取指定关键词的音乐搜索结果/Get music search results of specified keywords
- Capabilities: search / music / audio
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_music_search_result_api_v1_tiktok_app_v3_fetch_music_search_result_get`
- Full contract: [`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-music-search-result`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-music-search-result)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| keyword | query | string | Yes | 关键词/Keyword |
| offset | query | integer | No | 偏移量/Offset |
| count | query | integer | No | 数量/Number |
| filter_by | query | integer | No | 过滤类型/Filter type |
| sort_type | query | integer | No | 排序类型/Sort type |
| region | query | string | No | 地区/Region |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_music_video_list`

- Summary: 获取指定音乐的视频列表数据/Get video list of specified music
- Capabilities: content details / music / audio
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_music_video_list_api_v1_tiktok_app_v3_fetch_music_video_list_get`
- Full contract: [`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-music-video-list`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-music-video-list)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| music_id | query | string | Yes | 音乐id/Music id |
| cursor | query | integer | No | 游标/Cursor |
| count | query | integer | No | 数量/Number |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_one_video`

- Summary: 获取单个作品数据/Get single video data
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_one_video_api_v1_tiktok_app_v3_fetch_one_video_get`
- Full contract: [`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-one-video`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-one-video)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| aweme_id | query | string | Yes | 作品id/Video id |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_one_video_by_share_url`

- Summary: 根据分享链接获取单个作品数据/Get single video data by sharing link
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_one_video_by_share_url_api_v1_tiktok_app_v3_fetch_one_video_by_share_url_get`
- Full contract: [`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-one-video-by-share-url`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-one-video-by-share-url)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| share_url | query | string | Yes | 分享链接/Share link |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_one_video_by_share_url_v2`

- Summary: 根据分享链接获取单个作品数据/Get single video data by sharing link
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_one_video_by_share_url_v2_api_v1_tiktok_app_v3_fetch_one_video_by_share_url_v2_get`
- Full contract: [`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-one-video-by-share-url-v2`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-one-video-by-share-url-v2)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| share_url | query | string | Yes | 分享链接/Share link |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_one_video_v2`

- Summary: 获取单个作品数据 V2/Get single video data V2
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_one_video_v2_api_v1_tiktok_app_v3_fetch_one_video_v2_get`
- Full contract: [`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-one-video-v2`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-one-video-v2)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| aweme_id | query | string | Yes | 作品id/Video id |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_one_video_v3`

- Summary: 获取单个作品数据 V3(支持国家参数)/Get single video data V3 (support country parameter)
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_one_video_v3_api_v1_tiktok_app_v3_fetch_one_video_v3_get`
- Full contract: [`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-one-video-v3`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-one-video-v3)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| aweme_id | query | string | Yes | 作品id/Video id |
| region | query | string | No | 国家代码/Country code |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_product_detail`

- Summary: 获取商品详情数据（即将弃用，使用 fetch_product_detail_v2 代替）/Get product detail data (will be deprecated, use fetch_product_detail_v2 instead)
- Capabilities: details / commerce
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_product_detail_api_v1_tiktok_app_v3_fetch_product_detail_get`
- Full contract: [`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-product-detail`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-product-detail)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| product_id | query | string | Yes | 商品id/Product id |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_product_detail_v2`

- Summary: 获取商品详情数据V2/Get product detail data V2
- Capabilities: details / commerce
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_product_detail_v2_api_v1_tiktok_app_v3_fetch_product_detail_v2_get`
- Full contract: [`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-product-detail-v2`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-product-detail-v2)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| product_id | query | string | Yes | 商品id/Product id |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_product_detail_v3`

- Summary: 获取商品详情数据V3 / Get product detail data V3
- Capabilities: details / commerce
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_product_detail_v3_api_v1_tiktok_app_v3_fetch_product_detail_v3_get`
- Full contract: [`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-product-detail-v3`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-product-detail-v3)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| product_id | query | string | Yes | 商品id / Product ID |
| region | query | string | No | 商品的国家/地区代码/ Country/region code of the product |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_product_detail_v4`

- Summary: 获取商品详情数据V4 / Get product detail data V4
- Capabilities: details / commerce
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_product_detail_v4_api_v1_tiktok_app_v3_fetch_product_detail_v4_get`
- Full contract: [`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-product-detail-v4`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-product-detail-v4)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| product_id | query | string | Yes | 商品id / Product ID |
| region | query | string | No | 商品的国家/地区代码/ Country/region code of the product |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_product_id_by_share_link`

- Summary: 通过分享链接获取商品ID/Get Product ID by Share Link
- Capabilities: commerce
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_product_id_by_share_link_api_v1_tiktok_app_v3_fetch_product_id_by_share_link_get`
- Full contract: [`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-product-id-by-share-link`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-product-id-by-share-link)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| share_link | query | string | Yes | 分享链接/Share link |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_product_review`

- Summary: 获取商品评价数据/Get product review data
- Capabilities: commerce
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_product_review_api_v1_tiktok_app_v3_fetch_product_review_get`
- Full contract: [`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-product-review`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-product-review)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| product_id | query | string | Yes | 商品id/Product id |
| cursor | query | integer | No | 游标/Cursor |
| size | query | integer | No | 数量/Number |
| filter_id | query | integer | No | 筛选条件/Filter condition |
| sort_type | query | integer | No | 排序条件/Sorting conditions |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_product_search`

- Summary: 获取商品搜索结果/Get product search results
- Capabilities: search / commerce
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_product_search_api_v1_tiktok_app_v3_fetch_product_search_get`
- Full contract: [`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-product-search`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-product-search)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| keyword | query | string | Yes | 关键词/Keyword |
| cursor | query | integer | No | 游标/Cursor |
| count | query | integer | No | 数量/Number |
| sort_type | query | integer | No | 商品排序条件/Product sorting conditions |
| customer_review_four_star | query | boolean | No | 四星以上评价/Four-star or more reviews |
| have_discount | query | boolean | No | 有优惠/Having discount |
| min_price | query | string | No | 最低价格/Minimum price |
| max_price | query | string | No | 最高价格/Maximum price |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_share_qr_code`

- Summary: 获取分享二维码/Get share QR code
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_share_qr_code_api_v1_tiktok_app_v3_fetch_share_qr_code_get`
- Full contract: [`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-share-qr-code`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-share-qr-code)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| object_id | query | string | Yes | 对象id/Object id |
| schema_type | query | integer | No | 模式类型/Schema type |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_share_short_link`

- Summary: 获取分享短链接/Get share short link
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_share_short_link_api_v1_tiktok_app_v3_fetch_share_short_link_get`
- Full contract: [`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-share-short-link`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-share-short-link)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| url | query | string | Yes | 分享链接/Share link |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_shop_home`

- Summary: 获取商家主页数据/Get shop home page data
- Capabilities: profiles / accounts / commerce
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_shop_home_api_v1_tiktok_app_v3_fetch_shop_home_get`
- Full contract: [`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-shop-home`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-shop-home)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| page_id | query | string | Yes | 爬取的商家主页Page id/Page id of the crawled shop home page |
| seller_id | query | string | Yes | 商家id,店铺id/Seller id, shop id |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_shop_home_page_list`

- Summary: 获取商家主页Page列表数据/Get shop home page list data
- Capabilities: profiles / accounts / commerce
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_shop_home_page_list_api_v1_tiktok_app_v3_fetch_shop_home_page_list_get`
- Full contract: [`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-shop-home-page-list`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-shop-home-page-list)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| seller_id | query | string | Yes | 商家id,店铺id/Seller id, shop id |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_shop_id_by_share_link`

- Summary: 通过分享链接获取店铺ID/Get Shop ID by Share Link
- Capabilities: commerce
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_shop_id_by_share_link_api_v1_tiktok_app_v3_fetch_shop_id_by_share_link_get`
- Full contract: [`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-shop-id-by-share-link`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-shop-id-by-share-link)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| share_link | query | string | Yes | 分享链接/Share link |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_shop_info`

- Summary: 获取商家信息数据/Get shop information data
- Capabilities: commerce
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_shop_info_api_v1_tiktok_app_v3_fetch_shop_info_get`
- Full contract: [`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-shop-info`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-shop-info)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| shop_id | query | string | Yes | 商家id,店铺id/Seller id, shop id |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_shop_product_category`

- Summary: 获取商家产品分类数据/Get shop product category data
- Capabilities: commerce
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_shop_product_category_api_v1_tiktok_app_v3_fetch_shop_product_category_get`
- Full contract: [`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-shop-product-category`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-shop-product-category)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| seller_id | query | string | Yes | 商家id,店铺id/Seller id, shop id |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_shop_product_list`

- Summary: 获取商家商品列表数据/Get shop product list data
- Capabilities: commerce
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_shop_product_list_api_v1_tiktok_app_v3_fetch_shop_product_list_get`
- Full contract: [`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-shop-product-list`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-shop-product-list)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| seller_id | query | string | Yes | 商家id,店铺id/Seller id, shop id |
| scroll_params | query | string | No | 滚动参数，用于加载更多商品数据/Scroll parameter, used to load more product data |
| page_size | query | integer | No | 每页数量/Number per page |
| sort_field | query | integer | No | 排序字段/Sorting field |
| sort_order | query | integer | No | 排序方式/Sorting method |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_shop_product_list_v2`

- Summary: 获取商家商品列表数据 V2/Get shop product list data V2
- Capabilities: commerce
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_shop_product_list_v2_api_v1_tiktok_app_v3_fetch_shop_product_list_v2_get`
- Full contract: [`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-shop-product-list-v2`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-shop-product-list-v2)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| seller_id | query | string | Yes | 商家id,店铺id/Seller id, shop id |
| scroll_params | query | string | No | 滚动参数，用于加载更多商品数据/Scroll parameter, used to load more product data |
| page_size | query | integer | No | 每页数量/Number per page |
| sort_field | query | integer | No | 排序字段/Sorting field |
| sort_order | query | integer | No | 排序方式/Sorting method |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_shop_product_recommend`

- Summary: 获取商家商品推荐数据/Get shop product recommend data
- Capabilities: commerce
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_shop_product_recommend_api_v1_tiktok_app_v3_fetch_shop_product_recommend_get`
- Full contract: [`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-shop-product-recommend`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-shop-product-recommend)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| seller_id | query | string | Yes | 商家id,店铺id/Seller id, shop id |
| scroll_param | query | string | No | 滚动参数，用于加载更多商品数据/Scroll parameter, used to load more product data |
| page_size | query | integer | No | 每页数量/Number per page |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_similar_user_recommendations`

- Summary: 获取类似用户推荐/Similar User Recommendations
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_similar_user_recommendations_api_v1_tiktok_app_v3_fetch_similar_user_recommendations_get`
- Full contract: [`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-similar-user-recommendations`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-similar-user-recommendations)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| sec_uid | query | string | Yes | 用户sec_uid/User sec_uid |
| page_token | query | string | No | 分页标记/Page token |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_user_country_by_username`

- Summary: 通过用户名获取用户账号国家地区/Get user account country by username
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_country_by_username_api_v1_tiktok_app_v3_fetch_user_country_by_username_get`
- Full contract: [`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-user-country-by-username`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-user-country-by-username)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| username | query | string | Yes | 用户名/Username |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_user_follower_list`

- Summary: 获取指定用户的粉丝列表数据/Get follower list of specified user
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_follower_list_api_v1_tiktok_app_v3_fetch_user_follower_list_get`
- Full contract: [`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-user-follower-list`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-user-follower-list)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| user_id | query | string | No | 用户ID/User ID (与sec_user_id二选一/One of user_id and sec_user_id) |
| sec_user_id | query | string | No | 用户sec_user_id/User sec_user_id (与user_id二选一/One of user_id and sec_user_id) |
| count | query | integer | No | 数量/Number |
| min_time | query | integer | No | 最小时间，用于翻页/Minimum time for paging |
| page_token | query | string | No | 翻页token/Page token |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_user_following_list`

- Summary: 获取指定用户的关注列表数据/Get following list of specified user
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_following_list_api_v1_tiktok_app_v3_fetch_user_following_list_get`
- Full contract: [`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-user-following-list`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-user-following-list)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| user_id | query | string | No | 用户ID/User ID (与sec_user_id二选一/One of user_id and sec_user_id) |
| sec_user_id | query | string | No | 用户sec_user_id/User sec_user_id (与user_id二选一/One of user_id and sec_user_id) |
| count | query | integer | No | 数量/Number |
| min_time | query | integer | No | 最小时间，用于翻页/Minimum time for paging |
| page_token | query | string | No | 翻页token/Page token |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_user_like_videos`

- Summary: 获取用户喜欢作品数据/Get user like video data
- Capabilities: profiles / accounts / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_like_videos_api_v1_tiktok_app_v3_fetch_user_like_videos_get`
- Full contract: [`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-user-like-videos`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-user-like-videos)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| sec_user_id | query | string | Yes | 用户sec_user_id/User sec_user_id |
| max_cursor | query | integer | No | 最大游标/Maximum cursor |
| counts | query | integer | No | 每页数量/Number per page |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_user_music_list`

- Summary: 获取用户音乐列表数据/Get user music list data
- Capabilities: profiles / accounts / music / audio
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_music_list_api_v1_tiktok_app_v3_fetch_user_music_list_get`
- Full contract: [`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-user-music-list`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-user-music-list)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| sec_uid | query | string | Yes | 用户sec_uid/User sec_uid |
| cursor | query | integer | No | 游标/Cursor |
| count | query | integer | No | 数量/Number |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_user_post_videos`

- Summary: 获取用户主页作品数据 V1/Get user homepage video data V1
- Capabilities: profiles / accounts / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_post_videos_api_v1_tiktok_app_v3_fetch_user_post_videos_get`
- Full contract: [`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-user-post-videos`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-user-post-videos)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| sec_user_id | query | string | No | 用户sec_user_id/User sec_user_id |
| unique_id | query | string | No | 用户unique_id/User unique_id |
| max_cursor | query | integer | No | 最大游标/Maximum cursor |
| count | query | integer | No | 每页数量/Number per page |
| sort_type | query | integer | No | 排序类型/Sort type |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_user_post_videos_v2`

- Summary: 获取用户主页作品数据 V2/Get user homepage video data V2
- Capabilities: profiles / accounts / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_post_videos_api_v1_tiktok_app_v3_fetch_user_post_videos_v2_get`
- Full contract: [`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-user-post-videos-v2`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-user-post-videos-v2)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| sec_user_id | query | string | No | 用户sec_user_id/User sec_user_id |
| unique_id | query | string | No | 用户unique_id/User unique_id |
| max_cursor | query | integer | No | 最大游标/Maximum cursor |
| count | query | integer | No | 每页数量/Number per page |
| sort_type | query | integer | No | 排序类型/Sort type |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_user_post_videos_v3`

- Summary: 获取用户主页作品数据 V3（精简数据-更快速）/Get user homepage video data V3 (simplified data - faster)
- Capabilities: profiles / accounts / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_post_videos_v3_api_v1_tiktok_app_v3_fetch_user_post_videos_v3_get`
- Full contract: [`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-user-post-videos-v3`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-user-post-videos-v3)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| sec_user_id | query | string | No | 用户sec_user_id/User sec_user_id |
| unique_id | query | string | No | 用户unique_id/User unique_id |
| max_cursor | query | integer | No | 最大游标/Maximum cursor |
| count | query | integer | No | 每页数量/Number per page |
| sort_type | query | integer | No | 排序类型/Sort type |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_user_repost_videos`

- Summary: 获取用户转发的作品数据/Get user repost video data
- Capabilities: profiles / accounts / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_repost_videos_api_v1_tiktok_app_v3_fetch_user_repost_videos_get`
- Full contract: [`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-user-repost-videos`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-user-repost-videos)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| user_id | query | integer | Yes | 用户id/User id |
| offset | query | integer | No | 偏移量/Offset |
| count | query | integer | No | 数量/Number |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_user_search_result`

- Summary: 获取指定关键词的用户搜索结果/Get user search results of specified keywords
- Capabilities: search / profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_search_result_api_v1_tiktok_app_v3_fetch_user_search_result_get`
- Full contract: [`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-user-search-result`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-user-search-result)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| keyword | query | string | Yes | 关键词/Keyword |
| offset | query | integer | No | 偏移量/Offset |
| count | query | integer | No | 数量/Number |
| user_search_follower_count | query | string | No | 根据粉丝数排序/Sort by number of followers |
| user_search_profile_type | query | string | No | 根据账号类型排序/Sort by account type |
| user_search_other_pref | query | string | No | 根据其他偏好排序/Sort by other preferences |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_video_comment_replies`

- Summary: 获取指定视频的评论回复数据/Get comment replies data of specified video
- Capabilities: comments / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_video_comments_reply_api_v1_tiktok_app_v3_fetch_video_comment_replies_get`
- Full contract: [`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-video-comment-replies`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-video-comment-replies)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| item_id | query | string | Yes | 作品id/Video id |
| comment_id | query | string | Yes | 评论id/Comment id |
| cursor | query | integer | No | 游标/Cursor |
| count | query | integer | No | 数量/Number |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_video_comments`

- Summary: 获取单个视频评论数据/Get single video comments data
- Capabilities: comments / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_video_comments_api_v1_tiktok_app_v3_fetch_video_comments_get`
- Full contract: [`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-video-comments`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-video-comments)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| aweme_id | query | string | Yes | 作品id/Video id |
| cursor | query | integer | No | 游标/Cursor |
| count | query | integer | No | 数量/Number |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_video_search_result`

- Summary: 获取指定关键词的视频搜索结果/Get video search results of specified keywords
- Capabilities: search / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_video_search_result_api_v1_tiktok_app_v3_fetch_video_search_result_get`
- Full contract: [`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-video-search-result`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-video-search-result)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| keyword | query | string | Yes | 关键词/Keyword |
| offset | query | integer | No | 偏移量/Offset |
| count | query | integer | No | 数量/Number |
| sort_type | query | integer | No | 排序类型/Sort type |
| publish_time | query | integer | No | 发布时间/Publish time |
| region | query | string | No | 地区/Region |

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

### `GET /api/u1/v1/tiktok/app/v3/fetch_webcast_user_info`

- Summary: 获取指定 Webcast 用户的信息/Get information of specified Webcast user
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_webcast_user_info_api_v1_tiktok_app_v3_fetch_webcast_user_info_get`
- Full contract: [`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-webcast-user-info`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-fetch-webcast-user-info)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| user_id | query | string | No | 用户uid （可选，纯数字）/User uid (optional, pure number) |
| sec_user_id | query | string | No | 用户sec_user_id/User sec_user_id |

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

### `GET /api/u1/v1/tiktok/app/v3/get_user_id_and_sec_user_id_by_username`

- Summary: 使用用户名获取用户 user_id 和 sec_user_id/Get user_id and sec_user_id by Username
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_user_id_and_sec_user_id_by_username_api_v1_tiktok_app_v3_get_user_id_and_sec_user_id_by_username_get`
- Full contract: [`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-get-user-id-and-sec-user-id-by-username`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-get-user-id-and-sec-user-id-by-username)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| username | query | string | Yes | 用户名/Username |

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

### `GET /api/u1/v1/tiktok/app/v3/handler_user_profile`

- Summary: 获取指定用户的信息/Get information of specified user
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `handler_user_profile_api_v1_tiktok_app_v3_handler_user_profile_get`
- Full contract: [`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-handler-user-profile`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-handler-user-profile)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| user_id | query | string | No | 用户uid （可选，纯数字）/User uid (optional, pure number) |
| sec_user_id | query | string | No | 用户sec_user_id/User sec_user_id |
| unique_id | query | string | No | 用户unique_id （用户名）/User unique_id (username) |

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

### `GET /api/u1/v1/tiktok/app/v3/open_tiktok_app_to_keyword_search`

- Summary: 生成TikTok分享链接，唤起TikTok APP，跳转指定关键词搜索结果/Generate TikTok share link, call TikTok APP, and jump to the specified keyword search result
- Capabilities: search
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `open_tiktok_app_to_keyword_search_api_v1_tiktok_app_v3_open_tiktok_app_to_keyword_search_get`
- Full contract: [`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-open-tiktok-app-to-keyword-search`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-open-tiktok-app-to-keyword-search)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| keyword | query | string | Yes | 关键词/Keyword |

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

### `GET /api/u1/v1/tiktok/app/v3/open_tiktok_app_to_send_private_message`

- Summary: 生成TikTok分享链接，唤起TikTok APP，给指定用户发送私信/Generate TikTok share link, call TikTok APP, and send private messages to specified users
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `open_tiktok_app_to_send_private_message_api_v1_tiktok_app_v3_open_tiktok_app_to_send_private_message_get`
- Full contract: [`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-open-tiktok-app-to-send-private-message`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-open-tiktok-app-to-send-private-message)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| uid | query | string | Yes | 用户id/User id |

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

### `GET /api/u1/v1/tiktok/app/v3/open_tiktok_app_to_user_profile`

- Summary: 生成TikTok分享链接，唤起TikTok APP，跳转指定用户主页/Generate TikTok share link, call TikTok APP, and jump to the specified user profile
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `open_tiktok_app_to_user_profile_api_v1_tiktok_app_v3_open_tiktok_app_to_user_profile_get`
- Full contract: [`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-open-tiktok-app-to-user-profile`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-open-tiktok-app-to-user-profile)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| uid | query | string | Yes | 用户id/User id |

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

### `GET /api/u1/v1/tiktok/app/v3/open_tiktok_app_to_video_detail`

- Summary: 生成TikTok分享链接，唤起TikTok APP，跳转指定作品详情页/Generate TikTok share link, call TikTok APP, and jump to the specified video details page
- Capabilities: content details / details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `open_tiktok_app_to_video_detail_api_v1_tiktok_app_v3_open_tiktok_app_to_video_detail_get`
- Full contract: [`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-open-tiktok-app-to-video-detail`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-open-tiktok-app-to-video-detail)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| aweme_id | query | string | Yes | 作品id/Video id |

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

### `GET /api/u1/v1/tiktok/app/v3/search_follower_list`

- Summary: 搜索粉丝列表/Search follower list
- Capabilities: search
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `search_follower_list_api_v1_tiktok_app_v3_search_follower_list_get`
- Full contract: [`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-search-follower-list`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-search-follower-list)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| user_id | query | string | Yes | 用户ID/User ID |
| keyword | query | string | Yes | 搜索关键词/Search keyword |

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

### `GET /api/u1/v1/tiktok/app/v3/search_following_list`

- Summary: 搜索关注列表/Search following list
- Capabilities: search
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `search_following_list_api_v1_tiktok_app_v3_search_following_list_get`
- Full contract: [`api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-search-following-list`](../api-contracts/tiktok-app-v3-api.md#get-api-u1-v1-tiktok-app-v3-search-following-list)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| user_id | query | string | Yes | 用户ID/User ID |
| keyword | query | string | Yes | 搜索关键词/Search keyword |

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
