# Douyin-Xingtu-API 完整契约

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 回到路由详情：[`api-tags/douyin-xingtu-api.md`](../api-tags/douyin-xingtu-api.md)
- 当前契约文件：`api-contracts/douyin-xingtu-api.md`
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T04:31:58+00:00`
- 路由数：`22`
- 默认认证：请求头 `Authorization` Bearer
- 使用方式：当需要精确的认证说明、参数描述、默认值、示例或成功响应字段时，再读本文件。
- 标签说明：**(抖音星图数据接口/Douyin-Xingtu-API data endpoints)**

## 路由契约

<a id="get-api-u1-v1-douyin-xingtu-author-content-hot-comment-keywords-v1"></a>
### `GET /api/u1/v1/douyin/xingtu/author_content_hot_comment_keywords_v1`

- 摘要：获取kol热词分析内容V1/Get Author Content Hot Comment Keywords V1
- 能力：评论 / 热点/榜单 / 创作者
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`author_content_hot_comment_keywords_v1_api_v1_douyin_xingtu_author_content_hot_comment_keywords_v1_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取kol热词分析内容V1
> - 该接口数据使用企业账号进行请求，收费较贵。
> - 价格：0.02$ / 次
> ### 参数:
> - kolId: 用户的kolId, 可以从接口以下接口获取：
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id`
> ### 返回:
> - kol热词分析内容
>
> # [English]
> ### Purpose:
> - Get Author Content Hot Comment Keywords V1
> - The interface data is requested using an enterprise account, which is more expensive.
> - Price: 0.02$ / time
> ### Parameters:
> - kolId: User kolId, can be obtained from the following interfaces:
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id`
> ### Return:
> - Author Content Hot Comment Keywords
>
> # [示例/Example]
> kolId = "7048929565493690398"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| kolId | query | string | 是 | 用户的kolId/User kolId | 无 | 7048929565493690398 | 无 |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 | 200 | 无 | 无 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 | 无 | 无 | 无 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | 无 | 无 |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | 无 | 无 |
| support | string | 否 | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | 无 | 无 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 | 无 | 无 | 无 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 | 无 | 无 | 无 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | 无 | 无 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | 无 | 无 | 无 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | 无 | 无 |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | 无 | 无 |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL | 无 | 无 | 无 |
| router | string | 否 | The endpoint that generated this response \| 生成此响应的端点 | 无 | 无 | 无 |
| params | 动态对象 | 否 | The parameters used in the request \| 请求中使用的参数 | 无 | 无 | 无 |
| data | null | 否 | The response data \| 响应数据 | 无 | 无 | 无 |

<a id="get-api-u1-v1-douyin-xingtu-author-hot-comment-tokens-v1"></a>
### `GET /api/u1/v1/douyin/xingtu/author_hot_comment_tokens_v1`

- 摘要：获取kol热词分析评论V1/Get Author Hot Comment Tokens V1
- 能力：评论 / 热点/榜单 / 创作者
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`author_hot_comment_tokens_v1_api_v1_douyin_xingtu_author_hot_comment_tokens_v1_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取kol热词分析评论V1
> - 该接口数据使用企业账号进行请求，收费较贵。
> - 价格：0.02$ / 次
> ### 参数:
> - kolId: 用户的kolId, 可以从接口以下接口获取：
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id`
> ### 返回:
> - kol热词分析评论
>
> # [English]
> ### Purpose:
> - Get Author Hot Comment Tokens V1
> - The interface data is requested using an enterprise account, which is more expensive.
> - Price: 0.02$ / time
> ### Parameters:
> - kolId: User kolId, can be obtained from the following interfaces:
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id`
> ### Return:
> - Author Hot Comment Tokens
>
> # [示例/Example]
> kolId = "7048929565493690398"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| kolId | query | string | 是 | 用户的kolId/User kolId | 无 | 7048929565493690398 | 无 |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 | 200 | 无 | 无 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 | 无 | 无 | 无 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | 无 | 无 |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | 无 | 无 |
| support | string | 否 | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | 无 | 无 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 | 无 | 无 | 无 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 | 无 | 无 | 无 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | 无 | 无 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | 无 | 无 | 无 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | 无 | 无 |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | 无 | 无 |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL | 无 | 无 | 无 |
| router | string | 否 | The endpoint that generated this response \| 生成此响应的端点 | 无 | 无 | 无 |
| params | 动态对象 | 否 | The parameters used in the request \| 请求中使用的参数 | 无 | 无 | 无 |
| data | null | 否 | The response data \| 响应数据 | 无 | 无 | 无 |

<a id="get-api-u1-v1-douyin-xingtu-get-sign-image"></a>
### `GET /api/u1/v1/douyin/xingtu/get_sign_image`

- 摘要：获取加密图片解析/Get Sign Image
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_sign_image_api_v1_douyin_xingtu_get_sign_image_get`

#### 说明

> # [中文]
> ### 用途:
> - 解析星图加密图片，获取可访问的图片URL
> - 价格：0.001$ / 次
> ### 参数:
> - uri: 图片的uri，通常从其他星图接口返回的数据中获取
>     - 例如：`tos-cn-i-0813c000-ce/oMKzDA3A9QGAuebfsDIAwlDoAfCFEEzSEw8FQZ`
> - durationTS: 有效期时长（秒），默认86400（24小时）
> - format: 图片格式，默认webp，支持：webp、jpg、png等
> ### 返回:
> - 解析后的图片数据，包含可访问的图片URL
>
> # [English]
> ### Purpose:
> - Parse encrypted XingTu image and get accessible image URL
> - Price: 0.001$ / time
> ### Parameters:
> - uri: Image URI, usually obtained from other XingTu API responses
>     - Example: `tos-cn-i-0813c000-ce/oMKzDA3A9QGAuebfsDIAwlDoAfCFEEzSEw8FQZ`
> - durationTS: Duration in seconds, default 86400 (24 hours)
> - format: Image format, default webp, supports: webp, jpg, png, etc.
> ### Return:
> - Parsed image data with accessible image URL
>
> # [示例/Example]
> uri = "tos-cn-i-0813c000-ce/oMKzDA3A9QGAuebfsDIAwlDoAfCFEEzSEw8FQZ"
> durationTS = 86400
> format = "webp"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| uri | query | string | 是 | 图片的uri/Image URI | 无 | tos-cn-i-0813c000-ce/oMKzDA3A9QGAuebfsDIAwlDoAfCFEEzSEw8FQZ | 无 |
| durationTS | query | integer | 否 | 有效期时长（秒）/Duration in seconds | 86400 | 86400 | 无 |
| format | query | string | 否 | 图片格式/Image format | webp | webp | 无 |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 | 200 | 无 | 无 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 | 无 | 无 | 无 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | 无 | 无 |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | 无 | 无 |
| support | string | 否 | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | 无 | 无 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 | 无 | 无 | 无 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 | 无 | 无 | 无 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | 无 | 无 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | 无 | 无 | 无 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | 无 | 无 |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | 无 | 无 |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL | 无 | 无 | 无 |
| router | string | 否 | The endpoint that generated this response \| 生成此响应的端点 | 无 | 无 | 无 |
| params | 动态对象 | 否 | The parameters used in the request \| 请求中使用的参数 | 无 | 无 | 无 |
| data | null | 否 | The response data \| 响应数据 | 无 | 无 | 无 |

<a id="get-api-u1-v1-douyin-xingtu-get-xingtu-kolid-by-sec-user-id"></a>
### `GET /api/u1/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`

- 摘要：根据抖音sec_user_id获取游客星图kolid/Get XingTu kolid by Douyin sec_user_id
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_xingtu_kolid_by_sec_user_id_api_v1_douyin_xingtu_get_xingtu_kolid_by_sec_user_id_get`

#### 说明

> # [中文]
> ### 用途:
> - 通过抖音sec_user_id获取游客星图kolid
> - 价格：0.001$ / 次
> ### 参数:
> - sec_user_id: sec_user_id, 可以从接口以下接口获取：
>     - `/api/v1/douyin/web/handler_user_profile`
>     - `/api/v1/douyin/web/handler_user_profile_v2`
>     - `/api/v1/douyin/web/handler_user_profile_v3`
>     - `/api/v1/douyin/app/v3/handler_user_profile`
> ### 返回:
> - 游客星图kolid
>
> # [English]
> ### Purpose:
> - Get XingTu kolid by Douyin sec_user_id
> - Price: 0.001$ / time
> ### Parameters:
> - sec_user_id: sec_user_id, can be obtained from the following interfaces:
>     - `/api/v1/douyin/web/handler_user_profile`
>     - `/api/v1/douyin/web/handler_user_profile_v2`
>     - `/api/v1/douyin/web/handler_user_profile_v3`
>     - `/api/v1/douyin/app/v3/handler_user_profile`
> ### Return:
> - XingTu kolid
>
> # [示例/Example]
> sec_user_id = "MS4wLjABAAAAoxwUZouIdKL6sZ8EB96KDjkrhfBMS1KbCgsMJR1kIUs"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| sec_user_id | query | string | 是 | 抖音用户sec_user_id/Douyin User sec_user_id | 无 | MS4wLjABAAAAoxwUZouIdKL6sZ8EB96KDjkrhfBMS1KbCgsMJR1kIUs | 无 |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 | 200 | 无 | 无 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 | 无 | 无 | 无 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | 无 | 无 |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | 无 | 无 |
| support | string | 否 | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | 无 | 无 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 | 无 | 无 | 无 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 | 无 | 无 | 无 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | 无 | 无 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | 无 | 无 | 无 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | 无 | 无 |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | 无 | 无 |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL | 无 | 无 | 无 |
| router | string | 否 | The endpoint that generated this response \| 生成此响应的端点 | 无 | 无 | 无 |
| params | 动态对象 | 否 | The parameters used in the request \| 请求中使用的参数 | 无 | 无 | 无 |
| data | null | 否 | The response data \| 响应数据 | 无 | 无 | 无 |

<a id="get-api-u1-v1-douyin-xingtu-get-xingtu-kolid-by-uid"></a>
### `GET /api/u1/v1/douyin/xingtu/get_xingtu_kolid_by_uid`

- 摘要：根据抖音用户ID获取游客星图kolid/Get XingTu kolid by Douyin User ID
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_xingtu_kolid_by_uid_api_v1_douyin_xingtu_get_xingtu_kolid_by_uid_get`

#### 说明

> # [中文]
> ### 用途:
> - 通过抖音用户ID获取游客星图kolid
> - 价格：0.001$ / 次
> ### 参数:
> - uid: 用户ID, 可以从接口以下接口获取：
>     - `/api/v1/douyin/web/fetch_user_profile_by_uid`
>     - `/api/v1/douyin/web/fetch_user_profile_by_short_id`
>     - `/api/v1/douyin/web/handler_user_profile`
>     - `/api/v1/douyin/web/handler_user_profile_v2`
>     - `/api/v1/douyin/web/handler_user_profile_v3`
>     - `/api/v1/douyin/app/v3/handler_user_profile`
> ### 返回:
> - 游客星图kolid
>
> # [English]
> ### Purpose:
> - Get XingTu kolid by Douyin User ID
> - Price: 0.001$ / time
> ### Parameters:
> - uid: User ID, can be obtained from the following interfaces:
>     - `/api/v1/douyin/web/fetch_user_profile_by_uid`
>     - `/api/v1/douyin/web/fetch_user_profile_by_short_id`
>     - `/api/v1/douyin/web/handler_user_profile`
>     - `/api/v1/douyin/web/handler_user_profile_v2`
>     - `/api/v1/douyin/web/handler_user_profile_v3`
>     - `/api/v1/douyin/app/v3/handler_user_profile`
> ### Return:
> - XingTu kolid
>
> # [示例/Example]
> uid = "70452002324"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| uid | query | string | 是 | 抖音用户ID/Douyin User ID | 无 | 70452002324 | 无 |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 | 200 | 无 | 无 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 | 无 | 无 | 无 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | 无 | 无 |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | 无 | 无 |
| support | string | 否 | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | 无 | 无 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 | 无 | 无 | 无 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 | 无 | 无 | 无 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | 无 | 无 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | 无 | 无 | 无 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | 无 | 无 |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | 无 | 无 |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL | 无 | 无 | 无 |
| router | string | 否 | The endpoint that generated this response \| 生成此响应的端点 | 无 | 无 | 无 |
| params | 动态对象 | 否 | The parameters used in the request \| 请求中使用的参数 | 无 | 无 | 无 |
| data | null | 否 | The response data \| 响应数据 | 无 | 无 | 无 |

<a id="get-api-u1-v1-douyin-xingtu-get-xingtu-kolid-by-unique-id"></a>
### `GET /api/u1/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id`

- 摘要：根据抖音号获取游客星图kolid/Get XingTu kolid by Douyin unique_id
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_xingtu_kolid_by_unique_id_api_v1_douyin_xingtu_get_xingtu_kolid_by_unique_id_get`

#### 说明

> # [中文]
> ### 用途:
> - 通过抖音号获取游客星图kolid
> - 价格：0.001$ / 次
> ### 参数:
> - unique_id: 抖音号, 可以从接口以下接口获取：
>     - `/api/v1/douyin/web/handler_user_profile`
>     - `/api/v1/douyin/web/handler_user_profile_v2`
>     - `/api/v1/douyin/web/handler_user_profile_v3`
>     - `/api/v1/douyin/app/v3/handler_user_profile`
> ### 返回:
> - 游客星图kolid
>
> # [English]
> ### Purpose:
> - Get XingTu kolid by Douyin unique_id
> - Price: 0.001$ / time
> ### Parameters:
> - unique_id: unique_id, can be obtained from the following interfaces:
>     - `/api/v1/douyin/web/handler_user_profile`
>     - `/api/v1/douyin/web/handler_user_profile_v2`
>     - `/api/v1/douyin/web/handler_user_profile_v3`
>     - `/api/v1/douyin/app/v3/handler_user_profile`
> ### Return:
> - XingTu kolid
>
> # [示例/Example]
> unique_id = "m6640150"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| unique_id | query | string | 是 | 抖音号/Douyin User unique_id | 无 | m6640150 | 无 |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 | 200 | 无 | 无 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 | 无 | 无 | 无 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | 无 | 无 |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | 无 | 无 |
| support | string | 否 | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | 无 | 无 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 | 无 | 无 | 无 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 | 无 | 无 | 无 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | 无 | 无 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | 无 | 无 | 无 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | 无 | 无 |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | 无 | 无 |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL | 无 | 无 | 无 |
| router | string | 否 | The endpoint that generated this response \| 生成此响应的端点 | 无 | 无 | 无 |
| params | 动态对象 | 否 | The parameters used in the request \| 请求中使用的参数 | 无 | 无 | 无 |
| data | null | 否 | The response data \| 响应数据 | 无 | 无 | 无 |

<a id="get-api-u1-v1-douyin-xingtu-kol-audience-portrait-v1"></a>
### `GET /api/u1/v1/douyin/xingtu/kol_audience_portrait_v1`

- 摘要：获取kol观众画像V1/Get kol Audience Portrait V1
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`kol_audience_portrait_v1_api_v1_douyin_xingtu_kol_audience_portrait_v1_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取kol观众画像V1
> - 该接口数据使用企业账号进行请求，收费较贵。
> - 价格：0.02$ / 次
> ### 参数:
> - kolId: 用户的kolId, 可以从接口以下接口获取：
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id`
> ### 返回:
> - kol观众画像
>
> # [English]
> ### Purpose:
> - Get kol Audience Portrait V1
> - The interface data is requested using an enterprise account, which is more expensive.
> - Price: 0.02$ / time
> ### Parameters:
> - kolId: User kolId, can be obtained from the following interfaces:
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id`
> ### Return:
> - kol Audience Portrait
>
> # [示例/Example]
> kolId = "7048929565493690398"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| kolId | query | string | 是 | 用户的kolId/User kolId | 无 | 7048929565493690398 | 无 |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 | 200 | 无 | 无 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 | 无 | 无 | 无 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | 无 | 无 |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | 无 | 无 |
| support | string | 否 | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | 无 | 无 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 | 无 | 无 | 无 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 | 无 | 无 | 无 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | 无 | 无 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | 无 | 无 | 无 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | 无 | 无 |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | 无 | 无 |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL | 无 | 无 | 无 |
| router | string | 否 | The endpoint that generated this response \| 生成此响应的端点 | 无 | 无 | 无 |
| params | 动态对象 | 否 | The parameters used in the request \| 请求中使用的参数 | 无 | 无 | 无 |
| data | null | 否 | The response data \| 响应数据 | 无 | 无 | 无 |

<a id="get-api-u1-v1-douyin-xingtu-kol-base-info-v1"></a>
### `GET /api/u1/v1/douyin/xingtu/kol_base_info_v1`

- 摘要：获取kol基本信息V1/Get kol Base Info V1
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`kol_base_info_v1_api_v1_douyin_xingtu_kol_base_info_v1_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取kol基本信息V1
> - 该接口数据使用企业账号进行请求，收费较贵。
> - 价格：0.02$ / 次
> ### 参数:
> - kolId: 用户的kolId, 可以从接口以下接口获取：
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id`
> - platformChannel:
>     - 平台渠道，支持以下参数:
>     - _1 :抖音短视频(Video)
>     - _10 :抖音直播(Live)
> ### 返回:
> - kol基本信息
>
> # [English]
> ### Purpose:
> - Get kol Base Info V1
> - The interface data is requested using an enterprise account, which is more expensive.
> - Price: 0.02$ / time
> ### Parameters:
> - kolId: User kolId, can be obtained from the following interfaces:
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id`
> - platformChannel:
>     - Platform channel, supports the following parameters:
>     - _1 :Douyin Video
>     - _10 :Douyin Live
> ### Return:
> - kol Base Info
>
> # [示例/Example]
> kolId = "7048929565493690398"
> platformChannel = "_1"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| kolId | query | string | 是 | 用户的kolId/User kolId | 无 | 7048929565493690398 | 无 |
| platformChannel | query | string | 是 | 平台渠道/Platform Channel | 无 | _1 | 无 |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 | 200 | 无 | 无 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 | 无 | 无 | 无 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | 无 | 无 |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | 无 | 无 |
| support | string | 否 | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | 无 | 无 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 | 无 | 无 | 无 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 | 无 | 无 | 无 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | 无 | 无 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | 无 | 无 | 无 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | 无 | 无 |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | 无 | 无 |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL | 无 | 无 | 无 |
| router | string | 否 | The endpoint that generated this response \| 生成此响应的端点 | 无 | 无 | 无 |
| params | 动态对象 | 否 | The parameters used in the request \| 请求中使用的参数 | 无 | 无 | 无 |
| data | null | 否 | The response data \| 响应数据 | 无 | 无 | 无 |

<a id="get-api-u1-v1-douyin-xingtu-kol-conversion-ability-analysis-v1"></a>
### `GET /api/u1/v1/douyin/xingtu/kol_conversion_ability_analysis_v1`

- 摘要：获取kol转化能力分析V1/Get kol Conversion Ability Analysis V1
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`kol_conversion_ability_analysis_v1_api_v1_douyin_xingtu_kol_conversion_ability_analysis_v1_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取kol转化能力分析V1
> - 该接口数据使用企业账号进行请求，收费较贵。
> - 价格：0.02$ / 次
> ### 参数:
> - kolId: 用户的kolId, 可以从接口以下接口获取：
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id`
> - _range: 时间范围, 支持以下参数:
>     - _1 :近7天(last 7 days)
>     - _2 :30天(last 30 days)
>     - _3 :90天(last 90 days)
> ### 返回:
> - kol转化能力分析
>
> # [English]
> ### Purpose:
> - Get kol Conversion Ability Analysis V1
> - The interface data is requested using an enterprise account, which is more expensive.
> - Price: 0.02$ / time
> ### Parameters:
> - kolId: User kolId, can be obtained from the following interfaces:
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id`
> - _range: Time range, supports the following parameters:
>     - _1 :Last 7 days
>     - _2 :Last 30 days
>     - _3 :Last 90 days
> ### Return:
> - kol Conversion Ability Analysis
>
> # [示例/Example]
> kolId = "7048929565493690398"
> _range = "_1"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| kolId | query | string | 是 | 用户的kolId/User kolId | 无 | 7048929565493690398 | 无 |
| _range | query | string | 是 | 时间范围/Time Range | 无 | _1 | 无 |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 | 200 | 无 | 无 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 | 无 | 无 | 无 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | 无 | 无 |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | 无 | 无 |
| support | string | 否 | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | 无 | 无 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 | 无 | 无 | 无 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 | 无 | 无 | 无 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | 无 | 无 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | 无 | 无 | 无 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | 无 | 无 |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | 无 | 无 |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL | 无 | 无 | 无 |
| router | string | 否 | The endpoint that generated this response \| 生成此响应的端点 | 无 | 无 | 无 |
| params | 动态对象 | 否 | The parameters used in the request \| 请求中使用的参数 | 无 | 无 | 无 |
| data | null | 否 | The response data \| 响应数据 | 无 | 无 | 无 |

<a id="get-api-u1-v1-douyin-xingtu-kol-convert-video-display-v1"></a>
### `GET /api/u1/v1/douyin/xingtu/kol_convert_video_display_v1`

- 摘要：获取kol转化视频展示V1/Get kol Convert Video Display V1
- 能力：作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`kol_convert_video_display_v1_api_v1_douyin_xingtu_kol_convert_video_display_v1_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取kol转化视频展示V1
> - 该接口数据使用企业账号进行请求，收费较贵。
> - 价格：0.02$ / 次
> ### 参数:
> - kolId: 用户的kolId, 可以从接口以下接口获取：
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id`
> - detailType: 详情类型, 支持以下参数:
>     - _1 :相关视频数据(Video Data)
>     - _2 :相关商品数据(Product Data)
> ### 返回:
> - kol转化视频展示
>
> # [English]
> ### Purpose:
> - Get kol Convert Video Display V1
> - The interface data is requested using an enterprise account, which is more expensive.
> - Price: 0.02$ / time
> ### Parameters:
> - kolId: User kolId, can be obtained from the following interfaces:
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id`
> - detailType: Detail type, supports the following parameters:
>     - _1 :Video Data
>     - _2 :Product Data
> - page: Page number, starting from 1
> ### Return:
> - kol Convert Video Display
>
> # [示例/Example]
> kolId = "7048929565493690398"
> detailType = "_1"
> page = 1

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| kolId | query | string | 是 | 用户的kolId/User kolId | 无 | 7048929565493690398 | 无 |
| detailType | query | string | 是 | 详情类型/Detail Type | 无 | _1 | 无 |
| page | query | integer | 是 | 页码/Page | 无 | 1 | 无 |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 | 200 | 无 | 无 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 | 无 | 无 | 无 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | 无 | 无 |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | 无 | 无 |
| support | string | 否 | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | 无 | 无 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 | 无 | 无 | 无 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 | 无 | 无 | 无 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | 无 | 无 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | 无 | 无 | 无 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | 无 | 无 |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | 无 | 无 |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL | 无 | 无 | 无 |
| router | string | 否 | The endpoint that generated this response \| 生成此响应的端点 | 无 | 无 | 无 |
| params | 动态对象 | 否 | The parameters used in the request \| 请求中使用的参数 | 无 | 无 | 无 |
| data | null | 否 | The response data \| 响应数据 | 无 | 无 | 无 |

<a id="get-api-u1-v1-douyin-xingtu-kol-cp-info-v1"></a>
### `GET /api/u1/v1/douyin/xingtu/kol_cp_info_v1`

- 摘要：获取kol性价比能力分析V1/Get kol Cp Info V1
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`kol_cp_info_v1_api_v1_douyin_xingtu_kol_cp_info_v1_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取kol性价比能力分析V1
> - 该接口数据使用企业账号进行请求，收费较贵。
> - 价格：0.02$ / 次
> ### 参数:
> - kolId: 用户的kolId, 可以从接口以下接口获取：
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id`
> ### 返回:
> - kol性价比能力分析
>
> # [English]
> ### Purpose:
> - Get kol Cp Info V1
> - The interface data is requested using an enterprise account, which is more expensive.
> - Price: 0.02$ / time
> ### Parameters:
> - kolId: User kolId, can be obtained from the following interfaces:
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id`
> ### Return:
> - kol Cp Info
>
> # [示例/Example]
> kolId = "7048929565493690398"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| kolId | query | string | 是 | 用户的kolId/User kolId | 无 | 7048929565493690398 | 无 |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 | 200 | 无 | 无 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 | 无 | 无 | 无 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | 无 | 无 |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | 无 | 无 |
| support | string | 否 | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | 无 | 无 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 | 无 | 无 | 无 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 | 无 | 无 | 无 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | 无 | 无 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | 无 | 无 | 无 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | 无 | 无 |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | 无 | 无 |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL | 无 | 无 | 无 |
| router | string | 否 | The endpoint that generated this response \| 生成此响应的端点 | 无 | 无 | 无 |
| params | 动态对象 | 否 | The parameters used in the request \| 请求中使用的参数 | 无 | 无 | 无 |
| data | null | 否 | The response data \| 响应数据 | 无 | 无 | 无 |

<a id="get-api-u1-v1-douyin-xingtu-kol-daily-fans-v1"></a>
### `GET /api/u1/v1/douyin/xingtu/kol_daily_fans_v1`

- 摘要：获取kol粉丝趋势V1/Get kol Daily Fans V1
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`kol_daily_fans_v1_api_v1_douyin_xingtu_kol_daily_fans_v1_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取kol粉丝趋势V1
> - 该接口数据使用企业账号进行请求，收费较贵。
> - 价格：0.02$ / 次
> ### 参数:
> - kolId: 用户的kolId, 可以从接口以下接口获取：
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id`
> - startDate: 开始日期，格式为：yyyy-MM-dd
> - endDate: 结束日期，格式为：yyyy-MM-dd
> ### 返回:
> - kol粉丝趋势
>
> # [English]
> ### Purpose:
> - Get kol Daily Fans V1
> - The interface data is requested using an enterprise account, which is more expensive.
> - Price: 0.02$ / time
> ### Parameters:
> - kolId: User kolId, can be obtained from the following interfaces:
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id`
> - startDate: Start date, format: yyyy-MM-dd
> - endDate: End date, format: yyyy-MM-dd
> ### Return:
> - kol Daily Fans
>
> # [示例/Example]
> kolId = "7048929565493690398"
> startDate = "2024-12-01"
> endDate = "2025-01-01"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| kolId | query | string | 是 | 用户的kolId/User kolId | 无 | 7048929565493690398 | 无 |
| startDate | query | string | 是 | 开始日期/Start Date | 无 | 2024-12-01 | 无 |
| endDate | query | string | 是 | 结束日期/End Date | 无 | 2025-01-01 | 无 |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 | 200 | 无 | 无 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 | 无 | 无 | 无 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | 无 | 无 |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | 无 | 无 |
| support | string | 否 | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | 无 | 无 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 | 无 | 无 | 无 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 | 无 | 无 | 无 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | 无 | 无 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | 无 | 无 | 无 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | 无 | 无 |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | 无 | 无 |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL | 无 | 无 | 无 |
| router | string | 否 | The endpoint that generated this response \| 生成此响应的端点 | 无 | 无 | 无 |
| params | 动态对象 | 否 | The parameters used in the request \| 请求中使用的参数 | 无 | 无 | 无 |
| data | null | 否 | The response data \| 响应数据 | 无 | 无 | 无 |

<a id="get-api-u1-v1-douyin-xingtu-kol-data-overview-v1"></a>
### `GET /api/u1/v1/douyin/xingtu/kol_data_overview_v1`

- 摘要：获取kol数据概览V1/Get kol Data Overview V1
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`kol_data_overview_v1_api_v1_douyin_xingtu_kol_data_overview_v1_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取kol数据概览V1
> - 该接口数据使用企业账号进行请求，收费较贵。
> - 价格：0.02$ / 次
> ### 参数:
> - kolId: 用户的kolId, 可以从接口以下接口获取：
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id`
> - _type: 类型, 支持以下参数:
>     - _1 :个人视频(personal video)
>     - _2 :星图视频(xingtu video)
> - _range: 范围, 支持以下参数:
>     - _2 :近30天(last 30 days)
>     - _3 :近90天(last 90 days)
> - flowType: 流量类型, 支持以下参数:
>     - 1 : 默认(default)
> - onlyAssign (可选): 是否指派，具体参数如下:
>     - 不传递 : 使用API默认行为
>     - false : 全部数据
>     - true : 仅指派数据
> ### 返回:
> - kol数据概览
>
> # [English]
> ### Purpose:
> - Get kol Data Overview V1
> - The interface data is requested using an enterprise account, which is more expensive.
> - Price: 0.02$ / time
> ### Parameters:
> - kolId: User kolId, can be obtained from the following interfaces:
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id`
> - _type: Type, supports the following parameters:
>     - _1 :Personal Video
>     - _2 :Xingtu Video
> - _range: Range, supports the following parameters:
>     - _2 :Last 30 days
>     - _3 :Last 90 days
> - flowType: Flow Type, supports the following parameters:
>     - 1 : Default
> - onlyAssign (optional): Whether assigned, the specific parameters are as follows:
>     - Not provided : Use API default behavior
>     - false : All data
>     - true : Only assigned data
> ### Return:
> - kol Data Overview
>
> # [示例/Example]
> kolId = "7048929565493690398"
> _type = "_1"
> _range = "_2"
> flowType = 1
> onlyAssign = None  # or True/False if needed

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| kolId | query | string | 是 | 用户的kolId/User kolId | 无 | 7048929565493690398 | 无 |
| _type | query | string | 是 | 类型/Type | 无 | _1 | 无 |
| _range | query | string | 是 | 范围/Range | 无 | _2 | 无 |
| flowType | query | integer | 是 | 流量类型/Flow Type | 无 | 1 | 无 |
| onlyAssign | query | boolean | 否 | 是否指派/Whether assigned (optional) | 无 | 无 | 无 |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 | 200 | 无 | 无 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 | 无 | 无 | 无 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | 无 | 无 |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | 无 | 无 |
| support | string | 否 | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | 无 | 无 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 | 无 | 无 | 无 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 | 无 | 无 | 无 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | 无 | 无 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | 无 | 无 | 无 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | 无 | 无 |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | 无 | 无 |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL | 无 | 无 | 无 |
| router | string | 否 | The endpoint that generated this response \| 生成此响应的端点 | 无 | 无 | 无 |
| params | 动态对象 | 否 | The parameters used in the request \| 请求中使用的参数 | 无 | 无 | 无 |
| data | null | 否 | The response data \| 响应数据 | 无 | 无 | 无 |

<a id="get-api-u1-v1-douyin-xingtu-kol-fans-portrait-v1"></a>
### `GET /api/u1/v1/douyin/xingtu/kol_fans_portrait_v1`

- 摘要：获取kol粉丝画像V1/Get kol Fans Portrait V1
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`kol_fans_portrait_v1_api_v1_douyin_xingtu_kol_fans_portrait_v1_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取kol粉丝画像V1
> - 该接口数据使用企业账号进行请求，收费较贵。
> - 价格：0.02$ / 次
> ### 参数:
> - kolId: 用户的kolId, 可以从接口以下接口获取：
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id`
> - fansType: 粉丝类型，支持以下参数:
>     - _1: 粉丝画像 (Fans Portrait) - 默认值
>     - _2: 粉丝团画像 (Fans Group Portrait)
>     - _5: 铁粉画像 (Iron Fans Portrait)
> ### 返回:
> - kol粉丝画像
>
> # [English]
> ### Purpose:
> - Get kol Fans Portrait V1
> - The interface data is requested using an enterprise account, which is more expensive.
> - Price: 0.02$ / time
> ### Parameters:
> - kolId: User kolId, can be obtained from the following interfaces:
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id`
> - fansType: Fans Type, supports the following parameters:
>     - _1: Fans Portrait - Default
>     - _2: Fans Group Portrait
>     - _5: Iron Fans Portrait
> ### Return:
> - kol Fans Portrait
>
> # [示例/Example]
> kolId = "7048929565493690398"
> fansType = "_1"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| kolId | query | string | 是 | 用户的kolId/User kolId | 无 | 7048929565493690398 | 无 |
| fansType | query | string | 否 | 粉丝类型/Fans Type | _1 | _1 | 无 |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 | 200 | 无 | 无 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 | 无 | 无 | 无 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | 无 | 无 |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | 无 | 无 |
| support | string | 否 | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | 无 | 无 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 | 无 | 无 | 无 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 | 无 | 无 | 无 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | 无 | 无 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | 无 | 无 | 无 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | 无 | 无 |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | 无 | 无 |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL | 无 | 无 | 无 |
| router | string | 否 | The endpoint that generated this response \| 生成此响应的端点 | 无 | 无 | 无 |
| params | 动态对象 | 否 | The parameters used in the request \| 请求中使用的参数 | 无 | 无 | 无 |
| data | null | 否 | The response data \| 响应数据 | 无 | 无 | 无 |

<a id="get-api-u1-v1-douyin-xingtu-kol-link-struct-v1"></a>
### `GET /api/u1/v1/douyin/xingtu/kol_link_struct_v1`

- 摘要：获取kol连接用户V1/Get kol Link Struct V1
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`kol_link_struct_v1_api_v1_douyin_xingtu_kol_link_struct_v1_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取kol连接用户V1
> - 该接口数据使用企业账号进行请求，收费较贵。
> - 价格：0.02$ / 次
> ### 参数:
> - kolId: 用户的kolId, 可以从接口以下接口获取：
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id`
> ### 返回:
> - kol连接用户
>
> # [English]
> ### Purpose:
> - Get kol Link Struct V1
> - The interface data is requested using an enterprise account, which is more expensive.
> - Price: 0.02$ / time
> ### Parameters:
> - kolId: User kolId, can be obtained from the following interfaces:
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id`
> ### Return:
> - kol Link Struct
>
> # [示例/Example]
> kolId = "7048929565493690398"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| kolId | query | string | 是 | 用户的kolId/User kolId | 无 | 7048929565493690398 | 无 |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 | 200 | 无 | 无 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 | 无 | 无 | 无 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | 无 | 无 |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | 无 | 无 |
| support | string | 否 | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | 无 | 无 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 | 无 | 无 | 无 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 | 无 | 无 | 无 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | 无 | 无 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | 无 | 无 | 无 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | 无 | 无 |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | 无 | 无 |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL | 无 | 无 | 无 |
| router | string | 否 | The endpoint that generated this response \| 生成此响应的端点 | 无 | 无 | 无 |
| params | 动态对象 | 否 | The parameters used in the request \| 请求中使用的参数 | 无 | 无 | 无 |
| data | null | 否 | The response data \| 响应数据 | 无 | 无 | 无 |

<a id="get-api-u1-v1-douyin-xingtu-kol-rec-videos-v1"></a>
### `GET /api/u1/v1/douyin/xingtu/kol_rec_videos_v1`

- 摘要：获取kol内容表现V1/Get kol Rec Videos V1
- 能力：作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`kol_rec_videos_v1_api_v1_douyin_xingtu_kol_rec_videos_v1_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取kol内容表现V1
> - 该接口数据使用企业账号进行请求，收费较贵。
> - 价格：0.02$ / 次
> ### 参数:
> - kolId: 用户的kolId, 可以从接口以下接口获取：
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id`
> ### 返回:
> - kol内容表现
>
> # [English]
> ### Purpose:
> - Get kol Rec Videos V1
> - The interface data is requested using an enterprise account, which is more expensive.
> - Price: 0.02$ / time
> ### Parameters:
> - kolId: User kolId, can be obtained from the following interfaces:
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id`
> ### Return:
> - kol Rec Videos
>
> # [示例/Example]
> kolId = "7048929565493690398"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| kolId | query | string | 是 | 用户的kolId/User kolId | 无 | 7048929565493690398 | 无 |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 | 200 | 无 | 无 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 | 无 | 无 | 无 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | 无 | 无 |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | 无 | 无 |
| support | string | 否 | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | 无 | 无 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 | 无 | 无 | 无 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 | 无 | 无 | 无 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | 无 | 无 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | 无 | 无 | 无 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | 无 | 无 |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | 无 | 无 |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL | 无 | 无 | 无 |
| router | string | 否 | The endpoint that generated this response \| 生成此响应的端点 | 无 | 无 | 无 |
| params | 动态对象 | 否 | The parameters used in the request \| 请求中使用的参数 | 无 | 无 | 无 |
| data | null | 否 | The response data \| 响应数据 | 无 | 无 | 无 |

<a id="get-api-u1-v1-douyin-xingtu-kol-service-price-v1"></a>
### `GET /api/u1/v1/douyin/xingtu/kol_service_price_v1`

- 摘要：获取kol服务报价V1/Get kol Service Price V1
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`kol_service_price_v1_api_v1_douyin_xingtu_kol_service_price_v1_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取kol服务报价V1
> - 该接口数据使用企业账号进行请求，收费较贵。
> - 价格：0.02$ / 次
> ### 参数:
> - kolId: 用户的kolId, 可以从接口以下接口获取：
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id`
> - platformChannel:
>     - 平台渠道，支持以下参数:
>     - _1: 抖音短视频(Video)
>     - _10: 抖音直播(Live)
> ### 返回:
> kol服务报价
>
> # [English]
> ### Purpose:
> - Get kol Service Price V1
> - The interface data is requested using an enterprise account, which is more expensive.
> - Price: 0.02$ / time
> ### Parameters:
> - kolId: User kolId, can be obtained from the following interfaces:
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id`
> - platformChannel:
>     - Platform channel, supports the following parameters:
>     - _1: Douyin Video
>     - _10: Douyin Live
> ### Return:
> - kol Service Price
>
> # [示例/Example]
> kolId = "7048929565493690398"
> platformChannel = "_1"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| kolId | query | string | 是 | 用户的kolId/User kolId | 无 | 7048929565493690398 | 无 |
| platformChannel | query | string | 是 | 平台渠道/Platform Channel | 无 | _1 | 无 |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 | 200 | 无 | 无 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 | 无 | 无 | 无 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | 无 | 无 |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | 无 | 无 |
| support | string | 否 | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | 无 | 无 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 | 无 | 无 | 无 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 | 无 | 无 | 无 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | 无 | 无 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | 无 | 无 | 无 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | 无 | 无 |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | 无 | 无 |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL | 无 | 无 | 无 |
| router | string | 否 | The endpoint that generated this response \| 生成此响应的端点 | 无 | 无 | 无 |
| params | 动态对象 | 否 | The parameters used in the request \| 请求中使用的参数 | 无 | 无 | 无 |
| data | null | 否 | The response data \| 响应数据 | 无 | 无 | 无 |

<a id="get-api-u1-v1-douyin-xingtu-kol-touch-distribution-v1"></a>
### `GET /api/u1/v1/douyin/xingtu/kol_touch_distribution_v1`

- 摘要：获取kol连接用户来源V1/Get kol Touch Distribution V1
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`kol_touch_distribution_v1_api_v1_douyin_xingtu_kol_touch_distribution_v1_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取kol连接用户来源V1
> - 该接口数据使用企业账号进行请求，收费较贵。
> - 价格：0.02$ / 次
> ### 参数:
> - kolId: 用户的kolId, 可以从接口以下接口获取：
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id`
> ### 返回:
> - kol连接用户来源
>
> # [English]
> ### Purpose:
> - Get kol Touch Distribution V1
> - The interface data is requested using an enterprise account, which is more expensive.
> - Price: 0.02$ / time
> ### Parameters:
> - kolId: User kolId, can be obtained from the following interfaces:
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id`
> ### Return:
> - kol Touch Distribution
>
> # [示例/Example]
> kolId = "7048929565493690398"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| kolId | query | string | 是 | 用户的kolId/User kolId | 无 | 7048929565493690398 | 无 |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 | 200 | 无 | 无 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 | 无 | 无 | 无 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | 无 | 无 |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | 无 | 无 |
| support | string | 否 | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | 无 | 无 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 | 无 | 无 | 无 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 | 无 | 无 | 无 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | 无 | 无 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | 无 | 无 | 无 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | 无 | 无 |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | 无 | 无 |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL | 无 | 无 | 无 |
| router | string | 否 | The endpoint that generated this response \| 生成此响应的端点 | 无 | 无 | 无 |
| params | 动态对象 | 否 | The parameters used in the request \| 请求中使用的参数 | 无 | 无 | 无 |
| data | null | 否 | The response data \| 响应数据 | 无 | 无 | 无 |

<a id="get-api-u1-v1-douyin-xingtu-kol-video-performance-v1"></a>
### `GET /api/u1/v1/douyin/xingtu/kol_video_performance_v1`

- 摘要：获取kol视频表现V1/Get kol Video Performance V1
- 能力：作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`kol_video_performance_v1_api_v1_douyin_xingtu_kol_video_performance_v1_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取kol视频表现V1
> - 该接口数据使用企业账号进行请求，收费较贵。
> - 价格：0.02$ / 次
> ### 参数:
> - kolId: 用户的kolId, 可以从接口以下接口获取：
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id`
> - onlyAssign: 是否只显示分配作品，具体参数如下:
>     - false : 显示全部，包括个人作品和分配作品，默认值。
>     - true : 只显示来自星图的分配作品。
> ### 返回:
> - kol视频表现
>
> # [English]
> ### Purpose:
> - Get kol Video Performance V1
> - The interface data is requested using an enterprise account, which is more expensive.
> - Price: 0.02$ / time
> ### Parameters:
> - kolId: User kolId, can be obtained from the following interfaces:
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id`
> - onlyAssign: Whether to display only assigned works, the specific parameters are as follows:
>     - false : Show all, including personal works and assigned works, default value.
>     - true : Only display assigned works from XingTu.
> ### Return:
> - kol Video Performance
>
> # [示例/Example]
> kolId = "7048929565493690398"
> onlyAssign = False

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| kolId | query | string | 是 | 用户的kolId/User kolId | 无 | 7048929565493690398 | 无 |
| onlyAssign | query | boolean | 是 | 是否只显示分配作品/Whether to display only assigned works | 无 | false | 无 |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 | 200 | 无 | 无 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 | 无 | 无 | 无 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | 无 | 无 |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | 无 | 无 |
| support | string | 否 | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | 无 | 无 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 | 无 | 无 | 无 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 | 无 | 无 | 无 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | 无 | 无 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | 无 | 无 | 无 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | 无 | 无 |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | 无 | 无 |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL | 无 | 无 | 无 |
| router | string | 否 | The endpoint that generated this response \| 生成此响应的端点 | 无 | 无 | 无 |
| params | 动态对象 | 否 | The parameters used in the request \| 请求中使用的参数 | 无 | 无 | 无 |
| data | null | 否 | The response data \| 响应数据 | 无 | 无 | 无 |

<a id="get-api-u1-v1-douyin-xingtu-kol-xingtu-index-v1"></a>
### `GET /api/u1/v1/douyin/xingtu/kol_xingtu_index_v1`

- 摘要：获取kol星图指数V1/Get kol Xingtu Index V1
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`kol_xingtu_index_v1_api_v1_douyin_xingtu_kol_xingtu_index_v1_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取kol星图指数V1
> - 该接口数据使用企业账号进行请求，收费较贵。
> - 价格：0.02$ / 次
> ### 参数:
> - kolId: 用户的kolId, 可以从接口以下接口获取：
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id`
> ### 返回:
> - kol星图指数
>
> # [English]
> ### Purpose:
> - Get kol Xingtu Index V1
> - The interface data is requested using an enterprise account, which is more expensive.
> - Price: 0.02$ / time
> ### Parameters:
> - kolId: User kolId, can be obtained from the following interfaces:
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`
>     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id`
> ### Return:
> - kol Xingtu Index
>
> # [示例/Example]
> kolId = "7048929565493690398"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| kolId | query | string | 是 | 用户的kolId/User kolId | 无 | 7048929565493690398 | 无 |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 | 200 | 无 | 无 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 | 无 | 无 | 无 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | 无 | 无 |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | 无 | 无 |
| support | string | 否 | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | 无 | 无 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 | 无 | 无 | 无 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 | 无 | 无 | 无 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | 无 | 无 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | 无 | 无 | 无 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | 无 | 无 |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | 无 | 无 |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL | 无 | 无 | 无 |
| router | string | 否 | The endpoint that generated this response \| 生成此响应的端点 | 无 | 无 | 无 |
| params | 动态对象 | 否 | The parameters used in the request \| 请求中使用的参数 | 无 | 无 | 无 |
| data | null | 否 | The response data \| 响应数据 | 无 | 无 | 无 |

<a id="get-api-u1-v1-douyin-xingtu-search-kol-v1"></a>
### `GET /api/u1/v1/douyin/xingtu/search_kol_v1`

- 摘要：关键词搜索kol V1/Search Kol V1
- 能力：搜索
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`search_kol_v1_api_v1_douyin_xingtu_search_kol_v1_get`

#### 说明

> # [中文]
> ### 用途:
> - 关键词搜索kol V1
> - 该接口数据使用企业账号进行请求，收费较贵。
> - 价格：0.02$ / 次
> ### 参数:
> - keyword: 关键词
> - platformSource:
>     - 平台来源，支持以下参数:
>     - _1 :抖音(douyin)
>     - _2 :头条(toutiao)
>     - _3 :西瓜(xigua)
> - page: 页码，从1开始
> ### 返回:
> - kol列表
>
> # [English]
> ### Purpose:
> - Search Kol V1
> - The interface data is requested using an enterprise account, which is more expensive.
> - Price: 0.02$ / time
> ### Parameters:
> - keyword: Keyword
> - platformSource:
>     - Platform source, supports the following parameters:
>     - _1 :Douyin
>     - _2 :Toutiao
>     - _3 :Xigua
> - page: Page number, starting from 1
> ### Return:
> - Kol List
>
> # [示例/Example]
> keyword = "人工智能"
> platformSource = "_1"
> page = 1

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| keyword | query | string | 是 | 关键词/Keyword | 无 | 抖音 | 无 |
| platformSource | query | string | 是 | 平台来源/Platform Source | 无 | _1 | 无 |
| page | query | integer | 是 | 页码/Page | 无 | 1 | 无 |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 | 200 | 无 | 无 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 | 无 | 无 | 无 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | 无 | 无 |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | 无 | 无 |
| support | string | 否 | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | 无 | 无 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 | 无 | 无 | 无 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 | 无 | 无 | 无 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | 无 | 无 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | 无 | 无 | 无 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | 无 | 无 |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | 无 | 无 |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL | 无 | 无 | 无 |
| router | string | 否 | The endpoint that generated this response \| 生成此响应的端点 | 无 | 无 | 无 |
| params | 动态对象 | 否 | The parameters used in the request \| 请求中使用的参数 | 无 | 无 | 无 |
| data | null | 否 | The response data \| 响应数据 | 无 | 无 | 无 |

<a id="get-api-u1-v1-douyin-xingtu-search-kol-v2"></a>
### `GET /api/u1/v1/douyin/xingtu/search_kol_v2`

- 摘要：高级搜索kol V2/Search Kol Advanced V2
- 能力：搜索
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`search_kol_v2_api_v1_douyin_xingtu_search_kol_v2_get`

#### 说明

> # [中文]
> ### 用途:
> - 高级搜索kol V2，支持粉丝范围和内容标签筛选
> - 该接口数据使用企业账号进行请求，收费较贵。
> - 价格：0.02$ / 次
> ### 参数:
> - keyword: 关键词
> - followerRange (可选): 粉丝范围，格式：最小值-最大值
>     - 例如：10-100 表示粉丝范围在 10万-100万 之间
>     - 不传递此参数则不限制粉丝范围
> - contentTag (可选): 内容标签，支持以下格式:
>     - tag-{id}: 一级标签，例如 tag-1 (美妆)
>     - tag_level_two-{id}: 二级标签，例如 tag_level_two-7 (穿搭)
>     - 标签列表参考文档中的 contentTag 映射表
>     - 不传递此参数则不限制内容标签
> ### 返回:
> - kol列表（支持高级筛选）
>
> # [English]
> ### Purpose:
> - Advanced Search Kol V2, supports follower range and content tag filtering
> - The interface data is requested using an enterprise account, which is more expensive.
> - Price: 0.02$ / time
> ### Parameters:
> - keyword: Keyword
> - followerRange (optional): Follower range, format: min-max
>     - Example: 10-100 indicates follower range between 100,000 and 1,000,000
>     - Do not pass this parameter to not limit the follower range
> - contentTag (optional): Content tag, supports the following formats:
>     - tag-{id}: First-level tag, e.g., tag-1 (Beauty)
>     - tag_level_two-{id}: Second-level tag, e.g., tag_level_two-7 (Outfit)
>     - Refer to the contentTag mapping table in the documentation
>     - Do not pass this parameter to not limit content tags
> ### Return:
> - Kol List (with advanced filtering)
>
> # [示例/Example]
> keyword = "美妆"
> followerRange = "10-100"  # 10万-100万粉丝
> contentTag = "tag-1"  # 美妆一级标签
> contentTag = "tag_level_two-2"  # 美妆教程二级标签
>
> # [内容标签映射表/Content Tag Mapping]
>
> ## 一级标签 (First-level tags) - 格式: tag-{id}
>
> | 参数 | 分类 | 参数 | 分类 | 参数 | 分类 |
> |------|------|------|------|------|------|
> | tag-1 | 美妆 | tag-6 | 时尚 | tag-11 | 萌宠 |
> | tag-15 | 测评 | tag-23 | 游戏 | tag-25 | 二次元 |
> | tag-27 | 旅行 | tag-31 | 汽车 | tag-36 | 生活 |
> | tag-41 | 音乐 | tag-46 | 舞蹈* | tag-48 | 美食 |
> | tag-55 | 母婴亲子 | tag-60 | 运动健身 | tag-64 | 科技数码 |
> | tag-68 | 教育培训 | tag-72 | 颜值达人 | tag-79 | 才艺技能 |
> | tag-85 | 影视娱乐 | tag-87 | 艺术文化 | tag-91 | 财经投资 |
> | tag-95 | 三农* | tag-97 | 剧情搞笑 | tag-100 | 情感* |
> | tag-102 | 园艺* | tag-130 | 随拍* | tag-139 | 房产 |
> | tag-1001 | 生活家居 | tag-1002 | 媒体号* | | |
>
> *注: 标记*的分类无二级标签
>
> ## 二级标签 (Second-level tags) - 格式: tag_level_two-{id}
>
> ### 美妆 (tag-1)
> - tag_level_two-2: 美妆教程
> - tag_level_two-3: 妆容展示
> - tag_level_two-4: 护肤保养
> - tag_level_two-5: 美妆测评种草
>
> ### 时尚 (tag-6)
> - tag_level_two-7: 穿搭
> - tag_level_two-8: 街拍
> - tag_level_two-10: 造型
> - tag_level_two-135: 时尚媒体
>
> ### 萌宠 (tag-11)
> - tag_level_two-12: 日常宠物
> - tag_level_two-13: 特别宠物
> - tag_level_two-14: 宠物周边
>
> ### 测评 (tag-15)
> - tag_level_two-16: 美妆测评
> - tag_level_two-17: 3C数码测评
> - tag_level_two-18: 汽车测评
> - tag_level_two-19: 美食产品测评
> - tag_level_two-20: 母婴产品测评
> - tag_level_two-21: 综合测评
> - tag_level_two-132: 酒店测评
>
> ### 游戏 (tag-23)
> - tag_level_two-121: 游戏剧情
> - tag_level_two-122: 游戏解说
> - tag_level_two-123: 游戏资讯
> - tag_level_two-124: 游戏其他
> - tag_level_two-440: 游戏录屏
> - tag_level_two-441: 游戏集锦
>
> ### 二次元 (tag-25)
> - tag_level_two-125: 二次元真人
> - tag_level_two-126: 动画漫画
> - tag_level_two-127: 配音声优
> - tag_level_two-128: 宅物手办
>
> ### 旅行 (tag-27)
> - tag_level_two-28: 旅行记录
> - tag_level_two-29: 旅行攻略
> - tag_level_two-30: 旅行推荐
> - tag_level_two-442: 户外生活
>
> ### 汽车 (tag-31)
> - tag_level_two-32: 汽车测评
> - tag_level_two-33: 汽车知识
> - tag_level_two-34: 汽车周边
>
> ### 生活 (tag-36)
> - tag_level_two-37: 生活记录
> - tag_level_two-39: 生活小窍门
> - tag_level_two-40: 好物推荐
> - tag_level_two-118: 健康养生
> - tag_level_two-422: 婚恋
>
> ### 音乐 (tag-41)
> - tag_level_two-42: 歌曲演唱
> - tag_level_two-43: 乐器演奏
> - tag_level_two-44: 音乐教学
> - tag_level_two-45: 音乐其他
> - tag_level_two-136: 音乐剪辑
>
> ### 美食 (tag-48)
> - tag_level_two-49: 美食教程
> - tag_level_two-50: 美食探店
> - tag_level_two-52: 美食产品测评
> - tag_level_two-53: 乡村野食
> - tag_level_two-54: 美食其他
> - tag_level_two-423: 酒类
>
> ### 母婴亲子 (tag-55)
> - tag_level_two-56: 育儿科普
> - tag_level_two-57: 萌娃日常
> - tag_level_two-58: 亲子互动
> - tag_level_two-59: 测评种草
>
> ### 运动健身 (tag-60)
> - tag_level_two-61: 健身
> - tag_level_two-63: 极限运动
> - tag_level_two-424: 体育资讯
> - tag_level_two-443: 冰雪
> - tag_level_two-444: 垂钓
> - tag_level_two-445: 格斗
> - tag_level_two-446: 球类项目
> - tag_level_two-447: 综合体育
>
> ### 科技数码 (tag-64)
> - tag_level_two-65: 3C数码
> - tag_level_two-66: 家居电器
> - tag_level_two-133: 科技
>
> ### 教育培训 (tag-68)
> - tag_level_two-69: 考学培训
> - tag_level_two-70: 语言教学
> - tag_level_two-71: 个人管理
> - tag_level_two-425: 职业教育
>
> ### 颜值达人 (tag-72)
> - tag_level_two-73: 美女
> - tag_level_two-74: 帅哥
>
> ### 才艺技能 (tag-79)
> - tag_level_two-80: 创意才能
> - tag_level_two-81: 手工
> - tag_level_two-82: 摄影
> - tag_level_two-83: 绘画
> - tag_level_two-84: 其他才艺
>
> ### 影视娱乐 (tag-85)
> - tag_level_two-413: 影视解说
> - tag_level_two-414: 影视混剪
> - tag_level_two-415: 明星资讯
> - tag_level_two-416: 综艺解说
> - tag_level_two-417: 综艺混剪
>
> ### 艺术文化 (tag-87)
> - tag_level_two-88: 传统文化
> - tag_level_two-89: 人文科普
> - tag_level_two-90: 自然科学
>
> ### 财经投资 (tag-91)
> - tag_level_two-92: 传统金融
> - tag_level_two-93: 互联网金融
> - tag_level_two-94: 财经知识
>
> ### 剧情搞笑 (tag-97)
> - tag_level_two-98: 剧情
> - tag_level_two-99: 搞笑
>
> ### 生活家居 (tag-1001)
> - tag_level_two-100101: 硬装
> - tag_level_two-100102: 软装
> - tag_level_two-100103: 生活技巧
> - tag_level_two-100104: 家居氛围
>
> ### 房产 (tag-139)
> - tag_level_two-140: 其他房产
> - tag_level_two-437: 房产知识
> - tag_level_two-439: 房产及投资
> - tag_level_two-448: 楼盘评测
> - tag_level_two-449: 楼市资讯
> - tag_level_two-450: 租房

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| keyword | query | string | 是 | 关键词/Keyword | 无 | 美妆 | 无 |
| followerRange | query | string | 否 | 粉丝范围(可选)/Follower Range (optional), 例如 10-100 表示10万-100万粉丝 | 无 | 10-100 | 无 |
| contentTag | query | string | 否 | 内容标签(可选)/Content Tag (optional), 例如 tag-1 或 tag_level_two-7 | 无 | tag-1 | 无 |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 | 200 | 无 | 无 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 | 无 | 无 | 无 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | 无 | 无 |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | 无 | 无 |
| support | string | 否 | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | 无 | 无 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 | 无 | 无 | 无 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 | 无 | 无 | 无 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | 无 | 无 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | 无 | 无 | 无 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | 无 | 无 |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | 无 | 无 |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL | 无 | 无 | 无 |
| router | string | 否 | The endpoint that generated this response \| 生成此响应的端点 | 无 | 无 | 无 |
| params | 动态对象 | 否 | The parameters used in the request \| 请求中使用的参数 | 无 | 无 | 无 |
| data | null | 否 | The response data \| 响应数据 | 无 | 无 | 无 |
