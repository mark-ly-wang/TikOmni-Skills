# Douyin-Xingtu-API Route Summary

- Back to index: [`api-capability-index.md`](../api-capability-index.md)
- Current tag file: `api-tags/douyin-xingtu-api.md`
- Full contract: [`api-contracts/douyin-xingtu-api.md`](../api-contracts/douyin-xingtu-api.md)
- Source: `https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- Fetched at: `2026-03-08T06:54:04+00:00`
- Route count: `22`
- Common capabilities: general / content details / comments / trends / rankings / creators / search
- Default auth: Header `Authorization` Bearer
- Common inputs: `kolId`, `platformChannel`, `_range`, `page`, `onlyAssign`, `keyword`, `uri`, `durationTS`, `format`, `sec_user_id`
- Tag description: **(抖音星图数据接口/Douyin-Xingtu-API data endpoints)**

## Routes

### `GET /api/u1/v1/douyin/xingtu/author_content_hot_comment_keywords_v1`

- Summary: 获取kol热词分析内容V1/Get Author Content Hot Comment Keywords V1
- Capabilities: comments / trends / rankings / creators
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `author_content_hot_comment_keywords_v1_api_v1_douyin_xingtu_author_content_hot_comment_keywords_v1_get`
- Full contract: [`api-contracts/douyin-xingtu-api.md#get-api-u1-v1-douyin-xingtu-author-content-hot-comment-keywords-v1`](../api-contracts/douyin-xingtu-api.md#get-api-u1-v1-douyin-xingtu-author-content-hot-comment-keywords-v1)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| kolId | query | string | Yes | 用户的kolId/User kolId |

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

### `GET /api/u1/v1/douyin/xingtu/author_hot_comment_tokens_v1`

- Summary: 获取kol热词分析评论V1/Get Author Hot Comment Tokens V1
- Capabilities: comments / trends / rankings / creators
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `author_hot_comment_tokens_v1_api_v1_douyin_xingtu_author_hot_comment_tokens_v1_get`
- Full contract: [`api-contracts/douyin-xingtu-api.md#get-api-u1-v1-douyin-xingtu-author-hot-comment-tokens-v1`](../api-contracts/douyin-xingtu-api.md#get-api-u1-v1-douyin-xingtu-author-hot-comment-tokens-v1)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| kolId | query | string | Yes | 用户的kolId/User kolId |

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

### `GET /api/u1/v1/douyin/xingtu/get_sign_image`

- Summary: 获取加密图片解析/Get Sign Image
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_sign_image_api_v1_douyin_xingtu_get_sign_image_get`
- Full contract: [`api-contracts/douyin-xingtu-api.md#get-api-u1-v1-douyin-xingtu-get-sign-image`](../api-contracts/douyin-xingtu-api.md#get-api-u1-v1-douyin-xingtu-get-sign-image)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| uri | query | string | Yes | 图片的uri/Image URI |
| durationTS | query | integer | No | 有效期时长（秒）/Duration in seconds |
| format | query | string | No | 图片格式/Image format |

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

### `GET /api/u1/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`

- Summary: 根据抖音sec_user_id获取游客星图kolid/Get XingTu kolid by Douyin sec_user_id
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_xingtu_kolid_by_sec_user_id_api_v1_douyin_xingtu_get_xingtu_kolid_by_sec_user_id_get`
- Full contract: [`api-contracts/douyin-xingtu-api.md#get-api-u1-v1-douyin-xingtu-get-xingtu-kolid-by-sec-user-id`](../api-contracts/douyin-xingtu-api.md#get-api-u1-v1-douyin-xingtu-get-xingtu-kolid-by-sec-user-id)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| sec_user_id | query | string | Yes | 抖音用户sec_user_id/Douyin User sec_user_id |

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

### `GET /api/u1/v1/douyin/xingtu/get_xingtu_kolid_by_uid`

- Summary: 根据抖音用户ID获取游客星图kolid/Get XingTu kolid by Douyin User ID
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_xingtu_kolid_by_uid_api_v1_douyin_xingtu_get_xingtu_kolid_by_uid_get`
- Full contract: [`api-contracts/douyin-xingtu-api.md#get-api-u1-v1-douyin-xingtu-get-xingtu-kolid-by-uid`](../api-contracts/douyin-xingtu-api.md#get-api-u1-v1-douyin-xingtu-get-xingtu-kolid-by-uid)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| uid | query | string | Yes | 抖音用户ID/Douyin User ID |

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

### `GET /api/u1/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id`

- Summary: 根据抖音号获取游客星图kolid/Get XingTu kolid by Douyin unique_id
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_xingtu_kolid_by_unique_id_api_v1_douyin_xingtu_get_xingtu_kolid_by_unique_id_get`
- Full contract: [`api-contracts/douyin-xingtu-api.md#get-api-u1-v1-douyin-xingtu-get-xingtu-kolid-by-unique-id`](../api-contracts/douyin-xingtu-api.md#get-api-u1-v1-douyin-xingtu-get-xingtu-kolid-by-unique-id)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| unique_id | query | string | Yes | 抖音号/Douyin User unique_id |

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

### `GET /api/u1/v1/douyin/xingtu/kol_audience_portrait_v1`

- Summary: 获取kol观众画像V1/Get kol Audience Portrait V1
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `kol_audience_portrait_v1_api_v1_douyin_xingtu_kol_audience_portrait_v1_get`
- Full contract: [`api-contracts/douyin-xingtu-api.md#get-api-u1-v1-douyin-xingtu-kol-audience-portrait-v1`](../api-contracts/douyin-xingtu-api.md#get-api-u1-v1-douyin-xingtu-kol-audience-portrait-v1)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| kolId | query | string | Yes | 用户的kolId/User kolId |

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

### `GET /api/u1/v1/douyin/xingtu/kol_base_info_v1`

- Summary: 获取kol基本信息V1/Get kol Base Info V1
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `kol_base_info_v1_api_v1_douyin_xingtu_kol_base_info_v1_get`
- Full contract: [`api-contracts/douyin-xingtu-api.md#get-api-u1-v1-douyin-xingtu-kol-base-info-v1`](../api-contracts/douyin-xingtu-api.md#get-api-u1-v1-douyin-xingtu-kol-base-info-v1)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| kolId | query | string | Yes | 用户的kolId/User kolId |
| platformChannel | query | string | Yes | 平台渠道/Platform Channel |

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

### `GET /api/u1/v1/douyin/xingtu/kol_conversion_ability_analysis_v1`

- Summary: 获取kol转化能力分析V1/Get kol Conversion Ability Analysis V1
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `kol_conversion_ability_analysis_v1_api_v1_douyin_xingtu_kol_conversion_ability_analysis_v1_get`
- Full contract: [`api-contracts/douyin-xingtu-api.md#get-api-u1-v1-douyin-xingtu-kol-conversion-ability-analysis-v1`](../api-contracts/douyin-xingtu-api.md#get-api-u1-v1-douyin-xingtu-kol-conversion-ability-analysis-v1)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| kolId | query | string | Yes | 用户的kolId/User kolId |
| _range | query | string | Yes | 时间范围/Time Range |

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

### `GET /api/u1/v1/douyin/xingtu/kol_convert_video_display_v1`

- Summary: 获取kol转化视频展示V1/Get kol Convert Video Display V1
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `kol_convert_video_display_v1_api_v1_douyin_xingtu_kol_convert_video_display_v1_get`
- Full contract: [`api-contracts/douyin-xingtu-api.md#get-api-u1-v1-douyin-xingtu-kol-convert-video-display-v1`](../api-contracts/douyin-xingtu-api.md#get-api-u1-v1-douyin-xingtu-kol-convert-video-display-v1)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| kolId | query | string | Yes | 用户的kolId/User kolId |
| detailType | query | string | Yes | 详情类型/Detail Type |
| page | query | integer | Yes | 页码/Page |

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

### `GET /api/u1/v1/douyin/xingtu/kol_cp_info_v1`

- Summary: 获取kol性价比能力分析V1/Get kol Cp Info V1
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `kol_cp_info_v1_api_v1_douyin_xingtu_kol_cp_info_v1_get`
- Full contract: [`api-contracts/douyin-xingtu-api.md#get-api-u1-v1-douyin-xingtu-kol-cp-info-v1`](../api-contracts/douyin-xingtu-api.md#get-api-u1-v1-douyin-xingtu-kol-cp-info-v1)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| kolId | query | string | Yes | 用户的kolId/User kolId |

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

### `GET /api/u1/v1/douyin/xingtu/kol_daily_fans_v1`

- Summary: 获取kol粉丝趋势V1/Get kol Daily Fans V1
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `kol_daily_fans_v1_api_v1_douyin_xingtu_kol_daily_fans_v1_get`
- Full contract: [`api-contracts/douyin-xingtu-api.md#get-api-u1-v1-douyin-xingtu-kol-daily-fans-v1`](../api-contracts/douyin-xingtu-api.md#get-api-u1-v1-douyin-xingtu-kol-daily-fans-v1)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| kolId | query | string | Yes | 用户的kolId/User kolId |
| startDate | query | string | Yes | 开始日期/Start Date |
| endDate | query | string | Yes | 结束日期/End Date |

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

### `GET /api/u1/v1/douyin/xingtu/kol_data_overview_v1`

- Summary: 获取kol数据概览V1/Get kol Data Overview V1
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `kol_data_overview_v1_api_v1_douyin_xingtu_kol_data_overview_v1_get`
- Full contract: [`api-contracts/douyin-xingtu-api.md#get-api-u1-v1-douyin-xingtu-kol-data-overview-v1`](../api-contracts/douyin-xingtu-api.md#get-api-u1-v1-douyin-xingtu-kol-data-overview-v1)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| kolId | query | string | Yes | 用户的kolId/User kolId |
| _type | query | string | Yes | 类型/Type |
| _range | query | string | Yes | 范围/Range |
| flowType | query | integer | Yes | 流量类型/Flow Type |
| onlyAssign | query | boolean | No | 是否指派/Whether assigned (optional) |

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

### `GET /api/u1/v1/douyin/xingtu/kol_fans_portrait_v1`

- Summary: 获取kol粉丝画像V1/Get kol Fans Portrait V1
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `kol_fans_portrait_v1_api_v1_douyin_xingtu_kol_fans_portrait_v1_get`
- Full contract: [`api-contracts/douyin-xingtu-api.md#get-api-u1-v1-douyin-xingtu-kol-fans-portrait-v1`](../api-contracts/douyin-xingtu-api.md#get-api-u1-v1-douyin-xingtu-kol-fans-portrait-v1)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| kolId | query | string | Yes | 用户的kolId/User kolId |
| fansType | query | string | No | 粉丝类型/Fans Type |

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

### `GET /api/u1/v1/douyin/xingtu/kol_link_struct_v1`

- Summary: 获取kol连接用户V1/Get kol Link Struct V1
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `kol_link_struct_v1_api_v1_douyin_xingtu_kol_link_struct_v1_get`
- Full contract: [`api-contracts/douyin-xingtu-api.md#get-api-u1-v1-douyin-xingtu-kol-link-struct-v1`](../api-contracts/douyin-xingtu-api.md#get-api-u1-v1-douyin-xingtu-kol-link-struct-v1)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| kolId | query | string | Yes | 用户的kolId/User kolId |

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

### `GET /api/u1/v1/douyin/xingtu/kol_rec_videos_v1`

- Summary: 获取kol内容表现V1/Get kol Rec Videos V1
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `kol_rec_videos_v1_api_v1_douyin_xingtu_kol_rec_videos_v1_get`
- Full contract: [`api-contracts/douyin-xingtu-api.md#get-api-u1-v1-douyin-xingtu-kol-rec-videos-v1`](../api-contracts/douyin-xingtu-api.md#get-api-u1-v1-douyin-xingtu-kol-rec-videos-v1)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| kolId | query | string | Yes | 用户的kolId/User kolId |

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

### `GET /api/u1/v1/douyin/xingtu/kol_service_price_v1`

- Summary: 获取kol服务报价V1/Get kol Service Price V1
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `kol_service_price_v1_api_v1_douyin_xingtu_kol_service_price_v1_get`
- Full contract: [`api-contracts/douyin-xingtu-api.md#get-api-u1-v1-douyin-xingtu-kol-service-price-v1`](../api-contracts/douyin-xingtu-api.md#get-api-u1-v1-douyin-xingtu-kol-service-price-v1)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| kolId | query | string | Yes | 用户的kolId/User kolId |
| platformChannel | query | string | Yes | 平台渠道/Platform Channel |

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

### `GET /api/u1/v1/douyin/xingtu/kol_touch_distribution_v1`

- Summary: 获取kol连接用户来源V1/Get kol Touch Distribution V1
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `kol_touch_distribution_v1_api_v1_douyin_xingtu_kol_touch_distribution_v1_get`
- Full contract: [`api-contracts/douyin-xingtu-api.md#get-api-u1-v1-douyin-xingtu-kol-touch-distribution-v1`](../api-contracts/douyin-xingtu-api.md#get-api-u1-v1-douyin-xingtu-kol-touch-distribution-v1)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| kolId | query | string | Yes | 用户的kolId/User kolId |

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

### `GET /api/u1/v1/douyin/xingtu/kol_video_performance_v1`

- Summary: 获取kol视频表现V1/Get kol Video Performance V1
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `kol_video_performance_v1_api_v1_douyin_xingtu_kol_video_performance_v1_get`
- Full contract: [`api-contracts/douyin-xingtu-api.md#get-api-u1-v1-douyin-xingtu-kol-video-performance-v1`](../api-contracts/douyin-xingtu-api.md#get-api-u1-v1-douyin-xingtu-kol-video-performance-v1)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| kolId | query | string | Yes | 用户的kolId/User kolId |
| onlyAssign | query | boolean | Yes | 是否只显示分配作品/Whether to display only assigned works |

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

### `GET /api/u1/v1/douyin/xingtu/kol_xingtu_index_v1`

- Summary: 获取kol星图指数V1/Get kol Xingtu Index V1
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `kol_xingtu_index_v1_api_v1_douyin_xingtu_kol_xingtu_index_v1_get`
- Full contract: [`api-contracts/douyin-xingtu-api.md#get-api-u1-v1-douyin-xingtu-kol-xingtu-index-v1`](../api-contracts/douyin-xingtu-api.md#get-api-u1-v1-douyin-xingtu-kol-xingtu-index-v1)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| kolId | query | string | Yes | 用户的kolId/User kolId |

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

### `GET /api/u1/v1/douyin/xingtu/search_kol_v1`

- Summary: 关键词搜索kol V1/Search Kol V1
- Capabilities: search
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `search_kol_v1_api_v1_douyin_xingtu_search_kol_v1_get`
- Full contract: [`api-contracts/douyin-xingtu-api.md#get-api-u1-v1-douyin-xingtu-search-kol-v1`](../api-contracts/douyin-xingtu-api.md#get-api-u1-v1-douyin-xingtu-search-kol-v1)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| keyword | query | string | Yes | 关键词/Keyword |
| platformSource | query | string | Yes | 平台来源/Platform Source |
| page | query | integer | Yes | 页码/Page |

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

### `GET /api/u1/v1/douyin/xingtu/search_kol_v2`

- Summary: 高级搜索kol V2/Search Kol Advanced V2
- Capabilities: search
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `search_kol_v2_api_v1_douyin_xingtu_search_kol_v2_get`
- Full contract: [`api-contracts/douyin-xingtu-api.md#get-api-u1-v1-douyin-xingtu-search-kol-v2`](../api-contracts/douyin-xingtu-api.md#get-api-u1-v1-douyin-xingtu-search-kol-v2)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| keyword | query | string | Yes | 关键词/Keyword |
| followerRange | query | string | No | 粉丝范围(可选)/Follower Range (optional), 例如 10-100 表示10万-100万粉丝 |
| contentTag | query | string | No | 内容标签(可选)/Content Tag (optional), 例如 tag-1 或 tag_level_two-7 |

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
