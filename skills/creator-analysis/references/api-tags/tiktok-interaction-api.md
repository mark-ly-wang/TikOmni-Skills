# TikTok-Interaction-API Route Summary

- Back to index: [`api-capability-index.md`](../api-capability-index.md)
- Current tag file: `api-tags/tiktok-interaction-api.md`
- Full contract: [`api-contracts/tiktok-interaction-api.md`](../api-contracts/tiktok-interaction-api.md)
- Source: `https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- Fetched at: `2026-03-08T06:54:04+00:00`
- Route count: `7`
- Common capabilities: general / comments / content details / comment replies
- Default auth: Header `Authorization` Bearer
- Common inputs: `cookie`, `device_id`, `iid`, `proxy`, `aweme_id`, `text`, `api_key`, `invite_code`, `user_id`, `sec_user_id`
- Tag description: **(TikTok交互类接口（不在提供该业务）/TikTok-Interaction-API (This service is no longer available))**

## Routes

### `GET /api/u1/v1/tiktok/interaction/apply`

- Summary: 申请使用TikTok交互API权限（Scope）/Apply for TikTok Interaction API permission (Scope)
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `apply_for_scope_api_v1_tiktok_interaction_apply_get`
- Full contract: [`api-contracts/tiktok-interaction-api.md#get-api-u1-v1-tiktok-interaction-apply`](../api-contracts/tiktok-interaction-api.md#get-api-u1-v1-tiktok-interaction-apply)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| api_key | query | string | Yes | None |
| invite_code | query | string | Yes | None |

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

### `POST /api/u1/v1/tiktok/interaction/collect`

- Summary: 收藏/Collect
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `collect_api_v1_tiktok_interaction_collect_post`
- Full contract: [`api-contracts/tiktok-interaction-api.md#post-api-u1-v1-tiktok-interaction-collect`](../api-contracts/tiktok-interaction-api.md#post-api-u1-v1-tiktok-interaction-collect)

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: `aweme_id`:string, `cookie`:string, `device_id`:string, `iid`:string, `proxy`:string

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| aweme_id | string | No | Video ID, which can be obtained from the sharing link, for example: https://www.tiktok.com/@username/video/741996634044… |
| cookie | string | No | User Cookie, you can log in to your TikTok account in the browser and then copy the Cookie information, please use URL-… |
| device_id | string | No | Device id, optional, if not filled in, it will be automatically generated, if you need to customize the device id, plea… |
| iid | string | No | Device install id, optional, if not filled in, it will be automatically generated, if you need to customize the device… |
| proxy | string | No | Proxy IP, optional, if not filled in, it will be automatically generated, if you need to customize the proxy IP, please… |

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

### `POST /api/u1/v1/tiktok/interaction/follow`

- Summary: 关注/Follow
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `follow_api_v1_tiktok_interaction_follow_post`
- Full contract: [`api-contracts/tiktok-interaction-api.md#post-api-u1-v1-tiktok-interaction-follow`](../api-contracts/tiktok-interaction-api.md#post-api-u1-v1-tiktok-interaction-follow)

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: `user_id`:string, `sec_user_id`:string, `cookie`:string, `device_id`:string, `iid`:string, `proxy`:string

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| user_id | string | No | Video ID, which can be obtained from the sharing link, for example: https://www.tiktok.com/@username/video/741996634044… |
| sec_user_id | string | No | User sec_id, which can be obtained from the sharing link, for example: https://www.tiktok.com/@username/video/741996634… |
| cookie | string | No | User Cookie, you can log in to your TikTok account in the browser and then copy the Cookie information, please use URL-… |
| device_id | string | No | Device id, optional, if not filled in, it will be automatically generated, if you need to customize the device id, plea… |
| iid | string | No | Device install id, optional, if not filled in, it will be automatically generated, if you need to customize the device… |
| proxy | string | No | Proxy IP, optional, if not filled in, it will be automatically generated, if you need to customize the proxy IP, please… |

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

### `POST /api/u1/v1/tiktok/interaction/forward`

- Summary: 转发/Forward
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `forward_api_v1_tiktok_interaction_forward_post`
- Full contract: [`api-contracts/tiktok-interaction-api.md#post-api-u1-v1-tiktok-interaction-forward`](../api-contracts/tiktok-interaction-api.md#post-api-u1-v1-tiktok-interaction-forward)

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: `aweme_id`:string, `cookie`:string, `device_id`:string, `iid`:string, `proxy`:string

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| aweme_id | string | No | Video ID, which can be obtained from the sharing link, for example: https://www.tiktok.com/@username/video/741996634044… |
| cookie | string | No | User Cookie, you can log in to your TikTok account in the browser and then copy the Cookie information, please use URL-… |
| device_id | string | No | Device id, optional, if not filled in, it will be automatically generated, if you need to customize the device id, plea… |
| iid | string | No | Device install id, optional, if not filled in, it will be automatically generated, if you need to customize the device… |
| proxy | string | No | Proxy IP, optional, if not filled in, it will be automatically generated, if you need to customize the proxy IP, please… |

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

### `POST /api/u1/v1/tiktok/interaction/like`

- Summary: 点赞/Like
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `like_api_v1_tiktok_interaction_like_post`
- Full contract: [`api-contracts/tiktok-interaction-api.md#post-api-u1-v1-tiktok-interaction-like`](../api-contracts/tiktok-interaction-api.md#post-api-u1-v1-tiktok-interaction-like)

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: `aweme_id`:string, `cookie`:string, `device_id`:string, `iid`:string, `proxy`:string

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| aweme_id | string | No | Video ID, which can be obtained from the sharing link, for example: https://www.tiktok.com/@username/video/741996634044… |
| cookie | string | No | User Cookie, you can log in to your TikTok account in the browser and then copy the Cookie information, please use URL-… |
| device_id | string | No | Device id, optional, if not filled in, it will be automatically generated, if you need to customize the device id, plea… |
| iid | string | No | Device install id, optional, if not filled in, it will be automatically generated, if you need to customize the device… |
| proxy | string | No | Proxy IP, optional, if not filled in, it will be automatically generated, if you need to customize the proxy IP, please… |

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

### `POST /api/u1/v1/tiktok/interaction/post_comment`

- Summary: 发送评论/Post comment
- Capabilities: comments / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `post_comment_api_v1_tiktok_interaction_post_comment_post`
- Full contract: [`api-contracts/tiktok-interaction-api.md#post-api-u1-v1-tiktok-interaction-post-comment`](../api-contracts/tiktok-interaction-api.md#post-api-u1-v1-tiktok-interaction-post-comment)

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: `aweme_id`:string, `text`:string, `cookie`:string, `device_id`:string, `iid`:string, `proxy`:string

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| aweme_id | string | No | Video ID, which can be obtained from the sharing link, for example: https://www.tiktok.com/@username/video/741996634044… |
| text | string | No | Comment content, TikTok comment content needs to comply with the specifications, do not contain illegal keywords, other… |
| cookie | string | No | User Cookie, you can log in to your TikTok account in the browser and then copy the Cookie information, please use URL-… |
| device_id | string | No | Device id, optional, if not filled in, it will be automatically generated, if you need to customize the device id, plea… |
| iid | string | No | Device install id, optional, if not filled in, it will be automatically generated, if you need to customize the device… |
| proxy | string | No | Proxy IP, optional, if not filled in, it will be automatically generated, if you need to customize the proxy IP, please… |

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

### `POST /api/u1/v1/tiktok/interaction/reply_comment`

- Summary: 回复评论/Reply to comment
- Capabilities: comments / comment replies
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `reply_comment_api_v1_tiktok_interaction_reply_comment_post`
- Full contract: [`api-contracts/tiktok-interaction-api.md#post-api-u1-v1-tiktok-interaction-reply-comment`](../api-contracts/tiktok-interaction-api.md#post-api-u1-v1-tiktok-interaction-reply-comment)

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: `aweme_id`:string, `reply_id`:string, `text`:string, `cookie`:string, `device_id`:string, `iid`:string, `proxy`:string

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| aweme_id | string | No | Video ID, which can be obtained from the sharing link, for example: https://www.tiktok.com/@username/video/741996634044… |
| reply_id | string | No | Comment ID, which can be obtained from the comment data of the specified video. |
| text | string | No | Comment content, TikTok comment content needs to comply with the specifications, do not contain illegal keywords, other… |
| cookie | string | No | User Cookie, you can log in to your TikTok account in the browser and then copy the Cookie information, please use URL-… |
| device_id | string | No | Device id, optional, if not filled in, it will be automatically generated, if you need to customize the device id, plea… |
| iid | string | No | Device install id, optional, if not filled in, it will be automatically generated, if you need to customize the device… |
| proxy | string | No | Proxy IP, optional, if not filled in, it will be automatically generated, if you need to customize the proxy IP, please… |

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
