# TikTok-Interaction-API 路由详情

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 当前 tag 文件：`api-tags/tiktok-interaction-api.md`
- 完整契约：[`api-contracts/tiktok-interaction-api.md`](../api-contracts/tiktok-interaction-api.md)
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T04:31:58+00:00`
- 路由数：`7`
- 常见能力：通用能力 / 评论 / 作品详情 / 评论回复
- 默认认证：请求头 `Authorization` Bearer
- 常见入参：`cookie`, `device_id`, `iid`, `proxy`, `aweme_id`, `text`, `api_key`, `invite_code`, `user_id`, `sec_user_id`
- 标签说明：**(TikTok交互类接口（不在提供该业务）/TikTok-Interaction-API (This service is no longer available))**

## 路由列表

### `GET /api/u1/v1/tiktok/interaction/apply`

- 摘要：申请使用TikTok交互API权限（Scope）/Apply for TikTok Interaction API permission (Scope)
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`apply_for_scope_api_v1_tiktok_interaction_apply_get`
- 完整契约：[`api-contracts/tiktok-interaction-api.md#get-api-u1-v1-tiktok-interaction-apply`](../api-contracts/tiktok-interaction-api.md#get-api-u1-v1-tiktok-interaction-apply)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| api_key | query | string | 是 | 无 |
| invite_code | query | string | 是 | 无 |

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

### `POST /api/u1/v1/tiktok/interaction/collect`

- 摘要：收藏/Collect
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`collect_api_v1_tiktok_interaction_collect_post`
- 完整契约：[`api-contracts/tiktok-interaction-api.md#post-api-u1-v1-tiktok-interaction-collect`](../api-contracts/tiktok-interaction-api.md#post-api-u1-v1-tiktok-interaction-collect)

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`aweme_id`:string, `cookie`:string, `device_id`:string, `iid`:string, `proxy`:string

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| aweme_id | string | 否 | Video ID, which can be obtained from the sharing link, for example: https://www.tiktok.com/@username/video/741996634044… |
| cookie | string | 否 | User Cookie, you can log in to your TikTok account in the browser and then copy the Cookie information, please use URL-… |
| device_id | string | 否 | Device id, optional, if not filled in, it will be automatically generated, if you need to customize the device id, plea… |
| iid | string | 否 | Device install id, optional, if not filled in, it will be automatically generated, if you need to customize the device… |
| proxy | string | 否 | Proxy IP, optional, if not filled in, it will be automatically generated, if you need to customize the proxy IP, please… |

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

### `POST /api/u1/v1/tiktok/interaction/follow`

- 摘要：关注/Follow
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`follow_api_v1_tiktok_interaction_follow_post`
- 完整契约：[`api-contracts/tiktok-interaction-api.md#post-api-u1-v1-tiktok-interaction-follow`](../api-contracts/tiktok-interaction-api.md#post-api-u1-v1-tiktok-interaction-follow)

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`user_id`:string, `sec_user_id`:string, `cookie`:string, `device_id`:string, `iid`:string, `proxy`:string

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| user_id | string | 否 | Video ID, which can be obtained from the sharing link, for example: https://www.tiktok.com/@username/video/741996634044… |
| sec_user_id | string | 否 | User sec_id, which can be obtained from the sharing link, for example: https://www.tiktok.com/@username/video/741996634… |
| cookie | string | 否 | User Cookie, you can log in to your TikTok account in the browser and then copy the Cookie information, please use URL-… |
| device_id | string | 否 | Device id, optional, if not filled in, it will be automatically generated, if you need to customize the device id, plea… |
| iid | string | 否 | Device install id, optional, if not filled in, it will be automatically generated, if you need to customize the device… |
| proxy | string | 否 | Proxy IP, optional, if not filled in, it will be automatically generated, if you need to customize the proxy IP, please… |

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

### `POST /api/u1/v1/tiktok/interaction/forward`

- 摘要：转发/Forward
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`forward_api_v1_tiktok_interaction_forward_post`
- 完整契约：[`api-contracts/tiktok-interaction-api.md#post-api-u1-v1-tiktok-interaction-forward`](../api-contracts/tiktok-interaction-api.md#post-api-u1-v1-tiktok-interaction-forward)

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`aweme_id`:string, `cookie`:string, `device_id`:string, `iid`:string, `proxy`:string

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| aweme_id | string | 否 | Video ID, which can be obtained from the sharing link, for example: https://www.tiktok.com/@username/video/741996634044… |
| cookie | string | 否 | User Cookie, you can log in to your TikTok account in the browser and then copy the Cookie information, please use URL-… |
| device_id | string | 否 | Device id, optional, if not filled in, it will be automatically generated, if you need to customize the device id, plea… |
| iid | string | 否 | Device install id, optional, if not filled in, it will be automatically generated, if you need to customize the device… |
| proxy | string | 否 | Proxy IP, optional, if not filled in, it will be automatically generated, if you need to customize the proxy IP, please… |

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

### `POST /api/u1/v1/tiktok/interaction/like`

- 摘要：点赞/Like
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`like_api_v1_tiktok_interaction_like_post`
- 完整契约：[`api-contracts/tiktok-interaction-api.md#post-api-u1-v1-tiktok-interaction-like`](../api-contracts/tiktok-interaction-api.md#post-api-u1-v1-tiktok-interaction-like)

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`aweme_id`:string, `cookie`:string, `device_id`:string, `iid`:string, `proxy`:string

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| aweme_id | string | 否 | Video ID, which can be obtained from the sharing link, for example: https://www.tiktok.com/@username/video/741996634044… |
| cookie | string | 否 | User Cookie, you can log in to your TikTok account in the browser and then copy the Cookie information, please use URL-… |
| device_id | string | 否 | Device id, optional, if not filled in, it will be automatically generated, if you need to customize the device id, plea… |
| iid | string | 否 | Device install id, optional, if not filled in, it will be automatically generated, if you need to customize the device… |
| proxy | string | 否 | Proxy IP, optional, if not filled in, it will be automatically generated, if you need to customize the proxy IP, please… |

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

### `POST /api/u1/v1/tiktok/interaction/post_comment`

- 摘要：发送评论/Post comment
- 能力：评论 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`post_comment_api_v1_tiktok_interaction_post_comment_post`
- 完整契约：[`api-contracts/tiktok-interaction-api.md#post-api-u1-v1-tiktok-interaction-post-comment`](../api-contracts/tiktok-interaction-api.md#post-api-u1-v1-tiktok-interaction-post-comment)

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`aweme_id`:string, `text`:string, `cookie`:string, `device_id`:string, `iid`:string, `proxy`:string

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| aweme_id | string | 否 | Video ID, which can be obtained from the sharing link, for example: https://www.tiktok.com/@username/video/741996634044… |
| text | string | 否 | Comment content, TikTok comment content needs to comply with the specifications, do not contain illegal keywords, other… |
| cookie | string | 否 | User Cookie, you can log in to your TikTok account in the browser and then copy the Cookie information, please use URL-… |
| device_id | string | 否 | Device id, optional, if not filled in, it will be automatically generated, if you need to customize the device id, plea… |
| iid | string | 否 | Device install id, optional, if not filled in, it will be automatically generated, if you need to customize the device… |
| proxy | string | 否 | Proxy IP, optional, if not filled in, it will be automatically generated, if you need to customize the proxy IP, please… |

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

### `POST /api/u1/v1/tiktok/interaction/reply_comment`

- 摘要：回复评论/Reply to comment
- 能力：评论 / 评论回复
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`reply_comment_api_v1_tiktok_interaction_reply_comment_post`
- 完整契约：[`api-contracts/tiktok-interaction-api.md#post-api-u1-v1-tiktok-interaction-reply-comment`](../api-contracts/tiktok-interaction-api.md#post-api-u1-v1-tiktok-interaction-reply-comment)

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`aweme_id`:string, `reply_id`:string, `text`:string, `cookie`:string, `device_id`:string, `iid`:string, `proxy`:string

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| aweme_id | string | 否 | Video ID, which can be obtained from the sharing link, for example: https://www.tiktok.com/@username/video/741996634044… |
| reply_id | string | 否 | Comment ID, which can be obtained from the comment data of the specified video. |
| text | string | 否 | Comment content, TikTok comment content needs to comply with the specifications, do not contain illegal keywords, other… |
| cookie | string | 否 | User Cookie, you can log in to your TikTok account in the browser and then copy the Cookie information, please use URL-… |
| device_id | string | 否 | Device id, optional, if not filled in, it will be automatically generated, if you need to customize the device id, plea… |
| iid | string | 否 | Device install id, optional, if not filled in, it will be automatically generated, if you need to customize the device… |
| proxy | string | 否 | Proxy IP, optional, if not filled in, it will be automatically generated, if you need to customize the proxy IP, please… |

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
