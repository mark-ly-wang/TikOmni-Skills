# Douyin-Xingtu-V2-API Full Contract

- Back to index: [`api-capability-index.md`](../api-capability-index.md)
- Back to route summary: [`api-tags/douyin-xingtu-v2-api.md`](../api-tags/douyin-xingtu-v2-api.md)
- Current contract file: `api-contracts/douyin-xingtu-v2-api.md`
- Source: `https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- Fetched at: `2026-03-08T06:54:04+00:00`
- Route count: `21`
- Default auth: Header `Authorization` Bearer
- Read this file only when you need precise auth notes, parameter descriptions, defaults, examples, or success-response fields.
- Tag description: **(抖音星图V2数据接口/Douyin-Xingtu-V2-API data endpoints)**

## Route Contracts

<a id="get-api-u1-v1-douyin-xingtu-v2-get-author-base-info"></a>
### `GET /api/u1/v1/douyin/xingtu_v2/get_author_base_info`

- Summary: 获取创作者基本信息/Get Author Base Info
- Capabilities: creators
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_author_base_info_api_v1_douyin_xingtu_v2_get_author_base_info_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取创作者基本信息
> - 价格：0.001$ / 次
> ### 参数:
> - o_author_id: 创作者ID
> - platform_source: 平台来源，默认1
> - platform_channel: 平台渠道，默认1
> - recommend: 是否返回推荐信息，默认True
> - need_sec_uid: 是否返回sec_uid，默认True
> - need_linkage_info: 是否返回联动信息，默认True
> ### 返回:
> - 创作者基本信息数据
>
> # [English]
> ### Purpose:
> - Get creator/author base information
> - Price: 0.001$ / time
> ### Parameters:
> - o_author_id: Creator/author ID
> - platform_source: Platform source, default 1
> - platform_channel: Platform channel, default 1
> - recommend: Whether to return recommendation info, default True
> - need_sec_uid: Whether to return sec_uid, default True
> - need_linkage_info: Whether to return linkage info, default True
> ### Return:
> - Creator base info data
>
> # [示例/Example]
> o_author_id = "7589271892177518598"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| o_author_id | query | string | Yes | 创作者ID/Creator author ID | None | 7589271892177518598 | None |
| platform_source | query | integer | No | 平台来源/Platform source | 1 | 1 | None |
| platform_channel | query | integer | No | 平台渠道/Platform channel | 1 | 1 | None |
| recommend | query | boolean | No | 是否返回推荐信息/Whether to return recommendation info | true | true | None |
| need_sec_uid | query | boolean | No | 是否返回sec_uid/Whether to return sec_uid | true | true | None |
| need_linkage_info | query | boolean | No | 是否返回联动信息/Whether to return linkage info | true | true | None |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 | 200 | None | None |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 | None | None | None |
| message | string | No | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | None | None |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | None | None |
| support | string | No | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | None | None |
| time | string | No | The time the response was generated \| 生成响应的时间 | None | None | None |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 | None | None | None |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | None | None |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | None | None | None |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | None | None |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | None | None |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL | None | None | None |
| router | string | No | The endpoint that generated this response \| 生成此响应的端点 | None | None | None |
| params | dynamic object | No | The parameters used in the request \| 请求中使用的参数 | None | None | None |
| data | null | No | The response data \| 响应数据 | None | None | None |

<a id="get-api-u1-v1-douyin-xingtu-v2-get-author-business-card-info"></a>
### `GET /api/u1/v1/douyin/xingtu_v2/get_author_business_card_info`

- Summary: 获取创作者商业卡片信息/Get Author Business Card Info
- Capabilities: creators
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_author_business_card_info_api_v1_douyin_xingtu_v2_get_author_business_card_info_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取创作者商业卡片信息
> - 价格：0.001$ / 次
> ### 参数:
> - o_author_id: 创作者ID
> ### 返回:
> - 创作者商业卡片信息数据
>
> # [English]
> ### Purpose:
> - Get creator/author business card information
> - Price: 0.001$ / time
> ### Parameters:
> - o_author_id: Creator/author ID
> ### Return:
> - Creator business card info data
>
> # [示例/Example]
> o_author_id = "7589271892177518598"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| o_author_id | query | string | Yes | 创作者ID/Creator author ID | None | 7589271892177518598 | None |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 | 200 | None | None |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 | None | None | None |
| message | string | No | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | None | None |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | None | None |
| support | string | No | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | None | None |
| time | string | No | The time the response was generated \| 生成响应的时间 | None | None | None |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 | None | None | None |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | None | None |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | None | None | None |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | None | None |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | None | None |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL | None | None | None |
| router | string | No | The endpoint that generated this response \| 生成此响应的端点 | None | None | None |
| params | dynamic object | No | The parameters used in the request \| 请求中使用的参数 | None | None | None |
| data | null | No | The response data \| 响应数据 | None | None | None |

<a id="get-api-u1-v1-douyin-xingtu-v2-get-author-content-hot-keywords"></a>
### `GET /api/u1/v1/douyin/xingtu_v2/get_author_content_hot_keywords`

- Summary: 获取创作者内容热词/Get Author Content Hot Keywords
- Capabilities: trends / rankings / creators
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_author_content_hot_keywords_api_v1_douyin_xingtu_v2_get_author_content_hot_keywords_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取创作者内容热词
> - 价格：0.001$ / 次
> ### 参数:
> - author_id: 创作者ID
> - keyword_type: 热词类型，默认0
> ### 返回:
> - 创作者内容热词数据
>
> # [English]
> ### Purpose:
> - Get creator/author content hot keywords
> - Price: 0.001$ / time
> ### Parameters:
> - author_id: Creator/author ID
> - keyword_type: Keyword type, default 0
> ### Return:
> - Creator content hot keywords data
>
> # [示例/Example]
> author_id = "7589271892177518598"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| author_id | query | string | Yes | 创作者ID/Creator author ID | None | 7589271892177518598 | None |
| keyword_type | query | integer | No | 热词类型/Keyword type | 0 | 0 | None |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 | 200 | None | None |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 | None | None | None |
| message | string | No | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | None | None |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | None | None |
| support | string | No | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | None | None |
| time | string | No | The time the response was generated \| 生成响应的时间 | None | None | None |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 | None | None | None |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | None | None |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | None | None | None |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | None | None |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | None | None |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL | None | None | None |
| router | string | No | The endpoint that generated this response \| 生成此响应的端点 | None | None | None |
| params | dynamic object | No | The parameters used in the request \| 请求中使用的参数 | None | None | None |
| data | null | No | The response data \| 响应数据 | None | None | None |

<a id="get-api-u1-v1-douyin-xingtu-v2-get-author-hot-comment-tokens"></a>
### `GET /api/u1/v1/douyin/xingtu_v2/get_author_hot_comment_tokens`

- Summary: 获取创作者评论热词/Get Author Hot Comment Tokens
- Capabilities: comments / trends / rankings / creators
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_author_hot_comment_tokens_api_v1_douyin_xingtu_v2_get_author_hot_comment_tokens_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取创作者评论热词
> - 价格：0.001$ / 次
> ### 参数:
> - author_id: 创作者ID
> - num: 返回热词数量，默认10
> - without_emoji: 是否排除emoji，默认True
> ### 返回:
> - 创作者评论热词数据
>
> # [English]
> ### Purpose:
> - Get creator/author hot comment tokens/keywords
> - Price: 0.001$ / time
> ### Parameters:
> - author_id: Creator/author ID
> - num: Number of hot tokens, default 10
> - without_emoji: Whether to exclude emoji, default True
> ### Return:
> - Creator hot comment tokens data
>
> # [示例/Example]
> author_id = "7589271892177518598"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| author_id | query | string | Yes | 创作者ID/Creator author ID | None | 7589271892177518598 | None |
| num | query | integer | No | 返回热词数量/Number of hot tokens | 10 | 10 | None |
| without_emoji | query | boolean | No | 是否排除emoji/Whether to exclude emoji | true | true | None |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 | 200 | None | None |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 | None | None | None |
| message | string | No | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | None | None |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | None | None |
| support | string | No | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | None | None |
| time | string | No | The time the response was generated \| 生成响应的时间 | None | None | None |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 | None | None | None |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | None | None |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | None | None | None |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | None | None |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | None | None |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL | None | None | None |
| router | string | No | The endpoint that generated this response \| 生成此响应的端点 | None | None | None |
| params | dynamic object | No | The parameters used in the request \| 请求中使用的参数 | None | None | None |
| data | null | No | The response data \| 响应数据 | None | None | None |

<a id="get-api-u1-v1-douyin-xingtu-v2-get-author-local-info"></a>
### `GET /api/u1/v1/douyin/xingtu_v2/get_author_local_info`

- Summary: 获取创作者位置信息/Get Author Local Info
- Capabilities: creators
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_author_local_info_api_v1_douyin_xingtu_v2_get_author_local_info_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取创作者位置信息
> - 价格：0.001$ / 次
> ### 参数:
> - o_author_id: 创作者ID
> - platform_source: 平台来源，默认1
> - platform_channel: 平台渠道，默认1
> - time_range: 时间范围(天)，默认30
> ### 返回:
> - 创作者位置信息数据
>
> # [English]
> ### Purpose:
> - Get creator/author location information
> - Price: 0.001$ / time
> ### Parameters:
> - o_author_id: Creator/author ID
> - platform_source: Platform source, default 1
> - platform_channel: Platform channel, default 1
> - time_range: Time range in days, default 30
> ### Return:
> - Creator location info data
>
> # [示例/Example]
> o_author_id = "7146074596666507300"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| o_author_id | query | string | Yes | 创作者ID/Creator author ID | None | 7146074596666507300 | None |
| platform_source | query | integer | No | 平台来源/Platform source | 1 | 1 | None |
| platform_channel | query | integer | No | 平台渠道/Platform channel | 1 | 1 | None |
| time_range | query | integer | No | 时间范围(天)/Time range in days | 30 | 30 | None |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 | 200 | None | None |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 | None | None | None |
| message | string | No | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | None | None |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | None | None |
| support | string | No | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | None | None |
| time | string | No | The time the response was generated \| 生成响应的时间 | None | None | None |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 | None | None | None |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | None | None |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | None | None | None |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | None | None |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | None | None |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL | None | None | None |
| router | string | No | The endpoint that generated this response \| 生成此响应的端点 | None | None | None |
| params | dynamic object | No | The parameters used in the request \| 请求中使用的参数 | None | None | None |
| data | null | No | The response data \| 响应数据 | None | None | None |

<a id="get-api-u1-v1-douyin-xingtu-v2-get-author-market-fields"></a>
### `GET /api/u1/v1/douyin/xingtu_v2/get_author_market_fields`

- Summary: 获取达人广场筛选字段/Get Author Market Fields
- Capabilities: creators
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_author_market_fields_api_v1_douyin_xingtu_v2_get_author_market_fields_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取达人广场所有筛选字段选项
> - 价格：0.001$ / 次
> ### 参数:
> - market_scene: 市场场景，1=默认场景
> ### 返回:
> - 达人广场筛选字段数据
>
> # [English]
> ### Purpose:
> - Get all filter field options for the creator marketplace
> - Price: 0.001$ / time
> ### Parameters:
> - market_scene: Market scene, 1=default
> ### Return:
> - Creator marketplace filter fields data
>
> # [示例/Example]
> market_scene = 1

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| market_scene | query | integer | No | 市场场景，1=默认场景/Market scene, 1=default | 1 | 1 | None |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 | 200 | None | None |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 | None | None | None |
| message | string | No | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | None | None |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | None | None |
| support | string | No | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | None | None |
| time | string | No | The time the response was generated \| 生成响应的时间 | None | None | None |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 | None | None | None |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | None | None |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | None | None | None |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | None | None |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | None | None |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL | None | None | None |
| router | string | No | The endpoint that generated this response \| 生成此响应的端点 | None | None | None |
| params | dynamic object | No | The parameters used in the request \| 请求中使用的参数 | None | None | None |
| data | null | No | The response data \| 响应数据 | None | None | None |

<a id="get-api-u1-v1-douyin-xingtu-v2-get-author-show-items"></a>
### `GET /api/u1/v1/douyin/xingtu_v2/get_author_show_items`

- Summary: 获取创作者视频列表/Get Author Show Items
- Capabilities: creators
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_author_show_items_api_v1_douyin_xingtu_v2_get_author_show_items_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取创作者视频列表
> - 价格：0.001$ / 次
> ### 参数:
> - o_author_id: 创作者ID
> - platform_source: 平台来源，默认1
> - platform_channel: 平台渠道，默认1
> - limit: 返回数量，默认10
> - only_assign: 仅看指派视频（只针对星图视频生效），默认False
> - flow_type: 流量类型，默认0
> ### 返回:
> - 创作者视频列表数据
>
> # [English]
> ### Purpose:
> - Get creator/author video list
> - Price: 0.001$ / time
> ### Parameters:
> - o_author_id: Creator/author ID
> - platform_source: Platform source, default 1
> - platform_channel: Platform channel, default 1
> - limit: Result limit, default 10
> - only_assign: Only show assigned videos (only for XingTu videos), default False
> - flow_type: Flow type, default 0
> ### Return:
> - Creator video list data
>
> # [示例/Example]
> o_author_id = "7589271892177518598"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| o_author_id | query | string | Yes | 创作者ID/Creator author ID | None | 7589271892177518598 | None |
| platform_source | query | integer | No | 平台来源/Platform source | 1 | 1 | None |
| platform_channel | query | integer | No | 平台渠道/Platform channel | 1 | 1 | None |
| limit | query | integer | No | 返回数量/Result limit | 10 | 10 | None |
| only_assign | query | boolean | No | 仅看指派视频/Only show assigned videos | false | false | None |
| flow_type | query | integer | No | 流量类型/Flow type | 0 | 0 | None |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 | 200 | None | None |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 | None | None | None |
| message | string | No | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | None | None |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | None | None |
| support | string | No | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | None | None |
| time | string | No | The time the response was generated \| 生成响应的时间 | None | None | None |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 | None | None | None |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | None | None |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | None | None | None |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | None | None |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | None | None |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL | None | None | None |
| router | string | No | The endpoint that generated this response \| 生成此响应的端点 | None | None | None |
| params | dynamic object | No | The parameters used in the request \| 请求中使用的参数 | None | None | None |
| data | null | No | The response data \| 响应数据 | None | None | None |

<a id="get-api-u1-v1-douyin-xingtu-v2-get-author-spread-info"></a>
### `GET /api/u1/v1/douyin/xingtu_v2/get_author_spread_info`

- Summary: 获取创作者传播价值/Get Author Spread Info
- Capabilities: creators
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_author_spread_info_api_v1_douyin_xingtu_v2_get_author_spread_info_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取创作者商业能力的传播价值信息
> - 价格：0.001$ / 次
> ### 参数:
> - o_author_id: 创作者ID
> - platform_source: 平台来源，默认1
> - platform_channel: 平台渠道，默认1
> - type: 视频类型，1=个人视频
> - flow_type: 流量类型，默认0
> - only_assign: 仅看指派视频，默认False
> - range: 时间范围，2=近30天，3=近90天
> ### 返回:
> - 创作者传播价值数据
>
> # [English]
> ### Purpose:
> - Get creator/author spread value information (commercial capability)
> - Price: 0.001$ / time
> ### Parameters:
> - o_author_id: Creator/author ID
> - platform_source: Platform source, default 1
> - platform_channel: Platform channel, default 1
> - type: Video type, 1=personal video
> - flow_type: Flow type, default 0
> - only_assign: Only assigned videos, default False
> - range: Time range, 2=last 30 days, 3=last 90 days
> ### Return:
> - Creator spread value data
>
> # [示例/Example]
> o_author_id = "7589271892177518598"
> range = 2

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| o_author_id | query | string | Yes | 创作者ID/Creator author ID | None | 7589271892177518598 | None |
| platform_source | query | integer | No | 平台来源/Platform source | 1 | 1 | None |
| platform_channel | query | integer | No | 平台渠道/Platform channel | 1 | 1 | None |
| type | query | integer | No | 视频类型，1=个人视频/Video type, 1=personal video | 1 | 1 | None |
| flow_type | query | integer | No | 流量类型/Flow type | 0 | 0 | None |
| only_assign | query | boolean | No | 仅看指派视频/Only assigned videos | false | false | None |
| range | query | integer | No | 时间范围，2=近30天，3=近90天/Time range, 2=last 30 days, 3=last 90 days | 2 | 2 | None |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 | 200 | None | None |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 | None | None | None |
| message | string | No | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | None | None |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | None | None |
| support | string | No | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | None | None |
| time | string | No | The time the response was generated \| 生成响应的时间 | None | None | None |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 | None | None | None |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | None | None |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | None | None | None |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | None | None |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | None | None |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL | None | None | None |
| router | string | No | The endpoint that generated this response \| 生成此响应的端点 | None | None | None |
| params | dynamic object | No | The parameters used in the request \| 请求中使用的参数 | None | None | None |
| data | null | No | The response data \| 响应数据 | None | None | None |

<a id="get-api-u1-v1-douyin-xingtu-v2-get-content-trend-guide"></a>
### `GET /api/u1/v1/douyin/xingtu_v2/get_content_trend_guide`

- Summary: 获取内容趋势指南/Get Content Trend Guide
- Capabilities: trends / rankings
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_content_trend_guide_api_v1_douyin_xingtu_v2_get_content_trend_guide_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取内容趋势指南数据（CDN静态JSON，无需Cookie）
> - 价格：0.001$ / 次
> ### 返回:
> - 内容趋势指南数据
>
> # [English]
> ### Purpose:
> - Get content trend guide data (CDN static JSON, no cookie needed)
> - Price: 0.001$ / time
> ### Return:
> - Content trend guide data

#### Parameters

None

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 | 200 | None | None |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 | None | None | None |
| message | string | No | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | None | None |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | None | None |
| support | string | No | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | None | None |
| time | string | No | The time the response was generated \| 生成响应的时间 | None | None | None |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 | None | None | None |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | None | None |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | None | None | None |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | None | None |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | None | None |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL | None | None | None |
| router | string | No | The endpoint that generated this response \| 生成此响应的端点 | None | None | None |
| params | dynamic object | No | The parameters used in the request \| 请求中使用的参数 | None | None | None |
| data | null | No | The response data \| 响应数据 | None | None | None |

<a id="get-api-u1-v1-douyin-xingtu-v2-get-demander-mcn-list"></a>
### `GET /api/u1/v1/douyin/xingtu_v2/get_demander_mcn_list`

- Summary: 搜索MCN机构列表/Get Demander MCN List
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_demander_mcn_list_api_v1_douyin_xingtu_v2_get_demander_mcn_list_get`

#### Notes

> # [中文]
> ### 用途:
> - 搜索MCN机构列表
> - 价格：0.001$ / 次
> ### 参数:
> - mcn_name: MCN机构名称，支持模糊搜索
> - page: 页码，默认1
> - limit: 每页数量，默认20
> - order_by: 排序方式，`platform_scores`=平台评分
> ### 返回:
> - MCN机构列表数据
>
> # [English]
> ### Purpose:
> - Search MCN organization list
> - Price: 0.001$ / time
> ### Parameters:
> - mcn_name: MCN name, supports fuzzy search
> - page: Page number, default 1
> - limit: Page size, default 20
> - order_by: Sort by, `platform_scores`=platform scores
> ### Return:
> - MCN organization list data
>
> # [示例/Example]
> mcn_name = ""
> page = 1
> limit = 20

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| mcn_name | query | string | No | MCN机构名称，支持模糊搜索/MCN name, supports fuzzy search | None | None | None |
| page | query | integer | No | 页码/Page number | 1 | 1 | None |
| limit | query | integer | No | 每页数量/Page size | 20 | 20 | None |
| order_by | query | string | No | 排序方式/Sort by | platform_scores | platform_scores | None |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 | 200 | None | None |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 | None | None | None |
| message | string | No | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | None | None |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | None | None |
| support | string | No | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | None | None |
| time | string | No | The time the response was generated \| 生成响应的时间 | None | None | None |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 | None | None | None |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | None | None |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | None | None | None |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | None | None |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | None | None |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL | None | None | None |
| router | string | No | The endpoint that generated this response \| 生成此响应的端点 | None | None | None |
| params | dynamic object | No | The parameters used in the request \| 请求中使用的参数 | None | None | None |
| data | null | No | The response data \| 响应数据 | None | None | None |

<a id="get-api-u1-v1-douyin-xingtu-v2-get-excellent-case-category-list"></a>
### `GET /api/u1/v1/douyin/xingtu_v2/get_excellent_case_category_list`

- Summary: 获取优秀行业分类列表/Get Excellent Case Category List
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_excellent_case_category_list_api_v1_douyin_xingtu_v2_get_excellent_case_category_list_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取连接用户漏斗中的优秀行业分类列表
> - 价格：0.001$ / 次
> ### 参数:
> - platform_source: 平台来源，默认1
> ### 返回:
> - 优秀行业分类列表数据
>
> # [English]
> ### Purpose:
> - Get the excellent case category list in the user connection funnel
> - Price: 0.001$ / time
> ### Parameters:
> - platform_source: Platform source, default 1
> ### Return:
> - Excellent case category list data
>
> # [示例/Example]
> platform_source = 1

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| platform_source | query | integer | No | 平台来源/Platform source | 1 | 1 | None |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 | 200 | None | None |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 | None | None | None |
| message | string | No | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | None | None |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | None | None |
| support | string | No | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | None | None |
| time | string | No | The time the response was generated \| 生成响应的时间 | None | None | None |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 | None | None | None |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | None | None |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | None | None | None |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | None | None |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | None | None |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL | None | None | None |
| router | string | No | The endpoint that generated this response \| 生成此响应的端点 | None | None | None |
| params | dynamic object | No | The parameters used in the request \| 请求中使用的参数 | None | None | None |
| data | null | No | The response data \| 响应数据 | None | None | None |

<a id="get-api-u1-v1-douyin-xingtu-v2-get-ip-activity-detail"></a>
### `GET /api/u1/v1/douyin/xingtu_v2/get_ip_activity_detail`

- Summary: 获取星图IP活动详情/Get IP Activity Detail
- Capabilities: details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_ip_activity_detail_api_v1_douyin_xingtu_v2_get_ip_activity_detail_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取星图IP日历活动详情
> - 价格：0.001$ / 次
> ### 参数:
> - id: 活动ID，从`get_ip_activity_list`获取
> ### 返回:
> - IP活动详情数据
>
> # [English]
> ### Purpose:
> - Get XingTu IP calendar activity detail
> - Price: 0.001$ / time
> ### Parameters:
> - id: Activity ID, from `get_ip_activity_list`
> ### Return:
> - IP activity detail data
>
> # [示例/Example]
> id = 347

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | query | integer | Yes | 活动ID，从get_ip_activity_list获取/Activity ID from get_ip_activity_list | None | 347 | None |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 | 200 | None | None |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 | None | None | None |
| message | string | No | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | None | None |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | None | None |
| support | string | No | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | None | None |
| time | string | No | The time the response was generated \| 生成响应的时间 | None | None | None |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 | None | None | None |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | None | None |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | None | None | None |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | None | None |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | None | None |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL | None | None | None |
| router | string | No | The endpoint that generated this response \| 生成此响应的端点 | None | None | None |
| params | dynamic object | No | The parameters used in the request \| 请求中使用的参数 | None | None | None |
| data | null | No | The response data \| 响应数据 | None | None | None |

<a id="get-api-u1-v1-douyin-xingtu-v2-get-ip-activity-industry-list"></a>
### `GET /api/u1/v1/douyin/xingtu_v2/get_ip_activity_industry_list`

- Summary: 获取星图IP日历行业列表/Get IP Activity Industry List
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_ip_activity_industry_list_api_v1_douyin_xingtu_v2_get_ip_activity_industry_list_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取星图IP日历的行业列表
> - 价格：0.001$ / 次
> ### 返回:
> - 行业列表数据
>
> # [English]
> ### Purpose:
> - Get the industry list for XingTu IP calendar
> - Price: 0.001$ / time
> ### Return:
> - Industry list data

#### Parameters

None

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 | 200 | None | None |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 | None | None | None |
| message | string | No | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | None | None |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | None | None |
| support | string | No | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | None | None |
| time | string | No | The time the response was generated \| 生成响应的时间 | None | None | None |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 | None | None | None |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | None | None |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | None | None | None |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | None | None |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | None | None |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL | None | None | None |
| router | string | No | The endpoint that generated this response \| 生成此响应的端点 | None | None | None |
| params | dynamic object | No | The parameters used in the request \| 请求中使用的参数 | None | None | None |
| data | null | No | The response data \| 响应数据 | None | None | None |

<a id="post-api-u1-v1-douyin-xingtu-v2-get-ip-activity-list"></a>
### `POST /api/u1/v1/douyin/xingtu_v2/get_ip_activity_list`

- Summary: 获取星图IP日历活动列表/Get IP Activity List
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_ip_activity_list_api_v1_douyin_xingtu_v2_get_ip_activity_list_post`

#### Notes

> # [中文]
> ### 用途:
> - 获取星图IP日历活动列表
> - 价格：0.001$ / 次
> ### 参数:
> - query_start_time: 查询开始时间戳，如`1767196800`
> - query_end_time: 查询结束时间戳，如`1774972799`
> - industry_id_list (可选): 行业ID列表，从`get_ip_activity_industry_list`获取
>     - 例：`["1930"]`=美妆, `["1901"]`=3C及电器, `["1903"]`=食品饮料
> - category_list (可选): IP类型列表
>     - 1=星图大事件, 2=电商节点, 3=情绪节点, 4=创意营销, 5=行业活动
> - status_list (可选): IP状态列表
>     - 40=筹备中, 50=招商中, 30=资源上线, 20=已结束
> ### 返回:
> - IP日历活动列表数据
>
> # [English]
> ### Purpose:
> - Get XingTu IP calendar activity list
> - Price: 0.001$ / time
> ### Parameters:
> - query_start_time: Query start timestamp, e.g. `1767196800`
> - query_end_time: Query end timestamp, e.g. `1774972799`
> - industry_id_list (optional): Industry ID list from `get_ip_activity_industry_list`
>     - Example: `["1930"]`=Beauty, `["1901"]`=3C & Electronics, `["1903"]`=Food & Beverage
> - category_list (optional): IP category list
>     - 1=XingTu Big Event, 2=E-commerce Node, 3=Emotion Node, 4=Creative Marketing, 5=Industry Activity
> - status_list (optional): IP status list
>     - 40=Preparing, 50=Recruiting, 30=Resources Online, 20=Ended
> ### Return:
> - IP calendar activity list data
>
> # [示例/Example]
> query_start_time = "1767196800"
> query_end_time = "1774972799"

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: `query_start_time*`:string, `query_end_time*`:string, `industry_id_list`[string], `category_list`[integer], `status_list`[integer]

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| query_start_time | string | Yes | 查询开始时间戳/Query start timestamp | None | None | None |
| query_end_time | string | Yes | 查询结束时间戳/Query end timestamp | None | None | None |
| industry_id_list | array<string> | No | 行业ID列表/Industry ID list | None | None | None |
| category_list | array<integer> | No | IP类型列表/IP category list | None | None | None |
| status_list | array<integer> | No | IP状态列表/IP status list | None | None | None |

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 | 200 | None | None |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 | None | None | None |
| message | string | No | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | None | None |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | None | None |
| support | string | No | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | None | None |
| time | string | No | The time the response was generated \| 生成响应的时间 | None | None | None |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 | None | None | None |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | None | None |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | None | None | None |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | None | None |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | None | None |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL | None | None | None |
| router | string | No | The endpoint that generated this response \| 生成此响应的端点 | None | None | None |
| params | dynamic object | No | The parameters used in the request \| 请求中使用的参数 | None | None | None |
| data | null | No | The response data \| 响应数据 | None | None | None |

<a id="post-api-u1-v1-douyin-xingtu-v2-get-playlet-actor-rank-catalog"></a>
### `POST /api/u1/v1/douyin/xingtu_v2/get_playlet_actor_rank_catalog`

- Summary: 获取短剧演员热榜分类/Get Playlet Actor Rank Catalog
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_playlet_actor_rank_catalog_api_v1_douyin_xingtu_v2_get_playlet_actor_rank_catalog_post`

#### Notes

> # [中文]
> ### 用途:
> - 获取短剧演员热榜分类列表
> - 价格：0.001$ / 次
> ### 返回:
> - 短剧演员热榜分类数据
>
> # [English]
> ### Purpose:
> - Get XingTu playlet actor ranking catalog
> - Price: 0.001$ / time
> ### Return:
> - Playlet actor ranking catalog data

#### Parameters

None

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 | 200 | None | None |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 | None | None | None |
| message | string | No | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | None | None |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | None | None |
| support | string | No | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | None | None |
| time | string | No | The time the response was generated \| 生成响应的时间 | None | None | None |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 | None | None | None |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | None | None |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | None | None | None |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | None | None |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | None | None |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL | None | None | None |
| router | string | No | The endpoint that generated this response \| 生成此响应的端点 | None | None | None |
| params | dynamic object | No | The parameters used in the request \| 请求中使用的参数 | None | None | None |
| data | null | No | The response data \| 响应数据 | None | None | None |

<a id="get-api-u1-v1-douyin-xingtu-v2-get-playlet-actor-rank-list"></a>
### `GET /api/u1/v1/douyin/xingtu_v2/get_playlet_actor_rank_list`

- Summary: 获取短剧演员热榜/Get Playlet Actor Rank List
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_playlet_actor_rank_list_api_v1_douyin_xingtu_v2_get_playlet_actor_rank_list_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取短剧演员热榜数据
> - 价格：0.001$ / 次
> ### 参数:
> - category: 分类，默认`playlet_actor_list`
> - name: 榜单名称，`playlet_actor_composite_list`=综合榜
> - qualifier: 达人类型，空字符串=不限
> - period: 统计周期，7=周榜，30=月榜
> - date: 统计日期，格式YYYYMMDD
> - limit: 返回数量，默认100
> ### 返回:
> - 短剧演员热榜数据
>
> # [English]
> ### Purpose:
> - Get XingTu playlet actor ranking list data
> - Price: 0.001$ / time
> ### Parameters:
> - category: Category, default `playlet_actor_list`
> - name: Ranking name, `playlet_actor_composite_list`=composite list
> - qualifier: Actor type, empty=all
> - period: 7=weekly, 30=monthly
> - date: Date, format YYYYMMDD
> - limit: Result limit, default 100
> ### Return:
> - Playlet actor ranking data
>
> # [示例/Example]
> category = "playlet_actor_list"
> name = "playlet_actor_composite_list"
> period = 30
> date = "20251130"
> limit = 100

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| category | query | string | No | 分类/Category | playlet_actor_list | playlet_actor_list | None |
| name | query | string | No | 榜单名称/Ranking name | playlet_actor_composite_list | playlet_actor_composite_list | None |
| qualifier | query | string | No | 达人类型，空字符串=不限/Actor type, empty=all | None | None | None |
| period | query | integer | No | 统计周期，7=周榜，30=月榜/Period, 7=weekly, 30=monthly | 30 | 30 | None |
| date | query | string | No | 统计日期，格式YYYYMMDD/Date, format YYYYMMDD | 20251130 | 20251130 | None |
| limit | query | integer | No | 返回数量/Result limit | 100 | 100 | None |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 | 200 | None | None |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 | None | None | None |
| message | string | No | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | None | None |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | None | None |
| support | string | No | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | None | None |
| time | string | No | The time the response was generated \| 生成响应的时间 | None | None | None |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 | None | None | None |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | None | None |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | None | None | None |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | None | None |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | None | None |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL | None | None | None |
| router | string | No | The endpoint that generated this response \| 生成此响应的端点 | None | None | None |
| params | dynamic object | No | The parameters used in the request \| 请求中使用的参数 | None | None | None |
| data | null | No | The response data \| 响应数据 | None | None | None |

<a id="get-api-u1-v1-douyin-xingtu-v2-get-ranking-list-catalog"></a>
### `GET /api/u1/v1/douyin/xingtu_v2/get_ranking_list_catalog`

- Summary: 获取星图热榜分类/Get Ranking List Catalog
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_ranking_list_catalog_api_v1_douyin_xingtu_v2_get_ranking_list_catalog_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取星图热榜分类列表，返回qualifier_id等分类信息
> - 价格：0.001$ / 次
> ### 参数:
> - codes: 分类代码，默认为空字符串
> - biz_scene: 业务场景
>     - `douyin_flow_split_video_author_ranks`: 短视频达人热榜
>     - `douyin_flow_split_live_author_ranks`: 直播达人热榜
> ### 返回:
> - 热榜分类数据
>
> # [English]
> ### Purpose:
> - Get XingTu hot ranking list catalog, returns qualifier_id and other category information
> - Price: 0.001$ / time
> ### Parameters:
> - codes: Classification codes, default is empty string
> - biz_scene: Business scene
>     - `douyin_flow_split_video_author_ranks`: Video creator ranking
>     - `douyin_flow_split_live_author_ranks`: Live streamer ranking
> ### Return:
> - Hot ranking catalog data
>
> # [示例/Example]
> codes = ""
> biz_scene = "douyin_flow_split_video_author_ranks"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| codes | query | string | No | 分类代码，默认为空字符串/Classification codes, default is empty string | None | None | None |
| biz_scene | query | string | No | 业务场景/Business scene | douyin_flow_split_video_author_ranks | douyin_flow_split_video_author_ranks | None |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 | 200 | None | None |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 | None | None | None |
| message | string | No | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | None | None |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | None | None |
| support | string | No | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | None | None |
| time | string | No | The time the response was generated \| 生成响应的时间 | None | None | None |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 | None | None | None |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | None | None |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | None | None | None |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | None | None |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | None | None |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL | None | None | None |
| router | string | No | The endpoint that generated this response \| 生成此响应的端点 | None | None | None |
| params | dynamic object | No | The parameters used in the request \| 请求中使用的参数 | None | None | None |
| data | null | No | The response data \| 响应数据 | None | None | None |

<a id="get-api-u1-v1-douyin-xingtu-v2-get-ranking-list-data"></a>
### `GET /api/u1/v1/douyin/xingtu_v2/get_ranking_list_data`

- Summary: 获取星图达人商业榜数据/Get Ranking List Data
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_ranking_list_data_api_v1_douyin_xingtu_v2_get_ranking_list_data_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取星图达人商业榜数据
> - qualifier可以从`get_ranking_list_catalog`接口获取
> - 价格：0.001$ / 次
> ### 参数:
> - code: 榜单类型代码
>     - 短视频-达人商业榜: 1=品牌优选榜, 2=A3种草榜, 3=看后搜榜, 4=带货榜, 5=投流榜, 6=高潜榜
>     - 短视频-达人内容榜: 17=涨粉黑马榜, 18=头部必选榜
>     - 直播达人榜-主播类型: 23=游戏主播, 30=其他主播, 37=带货主播 (version=base)
>     - 直播达人榜-榜单类型: 23=游戏行业品牌优选榜, 24=非游戏行业品牌优选榜, 25=组件点击榜, 26=下载转化榜, 27=线索收集榜, 28=投流榜, 29=高潜榜
> - qualifier: 榜单分类ID，从`get_ranking_list_catalog`获取
> - version: 版本，`flow_split`=短视频榜单默认，`base`=直播榜单常用
> - period: 统计周期，7=周榜，30=月榜
> - date: 统计日期，格式YYYYMMDD
> - limit: 返回数量，默认100
> ### 返回:
> - 达人商业榜数据
>
> # [English]
> ### Purpose:
> - Get XingTu creator business ranking list data
> - qualifier can be obtained from `get_ranking_list_catalog` API
> - Price: 0.001$ / time
> ### Parameters:
> - code: Ranking type code
>     - Video business ranking: 1=Brand Premium, 2=A3 Seeding, 3=Search After Watch, 4=E-commerce, 5=Ad Flow, 6=High Potential
>     - Video content ranking: 17=Follower Growth Dark Horse, 18=Top Must-Pick
>     - Live streamer type: 23=Game Streamer, 30=Other Streamer, 37=E-commerce Streamer (version=base)
>     - Live ranking type: 23=Game Brand Premium, 24=Non-game Brand Premium, 25=Component Click, 26=Download Conversion, 27=Lead Collection, 28=Ad Flow, 29=High Potential
> - qualifier: Category qualifier_id from `get_ranking_list_catalog`
> - version: `flow_split`=default for video rankings, `base`=commonly used for live rankings
> - period: 7=weekly, 30=monthly
> - date: Date, format YYYYMMDD
> - limit: Result limit, default 100
> ### Return:
> - Creator business ranking data
>
> # [示例/Example]
> code = 1
> qualifier = "1901"
> version = "flow_split"
> period = 30
> date = "20260131"
> limit = 100

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| code | query | integer | No | 榜单类型代码/Ranking type code | 1 | 1 | None |
| qualifier | query | string | No | 榜单分类ID，从get_ranking_list_catalog获取/Category qualifier_id | 1901 | 1901 | None |
| version | query | string | No | 版本/Version | flow_split | flow_split | None |
| period | query | integer | No | 统计周期，7=周榜，30=月榜/Period, 7=weekly, 30=monthly | 30 | 30 | None |
| date | query | string | No | 统计日期，格式YYYYMMDD/Date, format YYYYMMDD | 20260131 | 20260131 | None |
| limit | query | integer | No | 返回数量/Result limit | 100 | 100 | None |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 | 200 | None | None |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 | None | None | None |
| message | string | No | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | None | None |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | None | None |
| support | string | No | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | None | None |
| time | string | No | The time the response was generated \| 生成响应的时间 | None | None | None |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 | None | None | None |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | None | None |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | None | None | None |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | None | None |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | None | None |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL | None | None | None |
| router | string | No | The endpoint that generated this response \| 生成此响应的端点 | None | None | None |
| params | dynamic object | No | The parameters used in the request \| 请求中使用的参数 | None | None | None |
| data | null | No | The response data \| 响应数据 | None | None | None |

<a id="post-api-u1-v1-douyin-xingtu-v2-get-recommend-for-star-authors"></a>
### `POST /api/u1/v1/douyin/xingtu_v2/get_recommend_for_star_authors`

- Summary: 获取相似创作者推荐/Get Recommend Similar Star Authors
- Capabilities: creators
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_recommend_for_star_authors_api_v1_douyin_xingtu_v2_get_recommend_for_star_authors_post`

#### Notes

> # [中文]
> ### 用途:
> - 获取相似创作者推荐
> - 价格：0.001$ / 次
> ### 参数:
> - author_ids: 创作者ID列表
> - similar_type: 相似类型
>     - `comprehension`: 综合相似
>     - `content`: 内容相似
>     - `audience`: 用户相似
>     - `commercial`: 商业能力相似
> - page: 页码，默认1
> - limit: 每页数量，默认12
> ### 返回:
> - 相似创作者推荐数据
>
> # [English]
> ### Purpose:
> - Get similar creator recommendation
> - Price: 0.001$ / time
> ### Parameters:
> - author_ids: List of creator/author IDs
> - similar_type: Similarity type
>     - `comprehension`: Comprehensive similarity
>     - `content`: Content similarity
>     - `audience`: Audience similarity
>     - `commercial`: Commercial capability similarity
> - page: Page number, default 1
> - limit: Page size, default 12
> ### Return:
> - Similar creator recommendation data
>
> # [示例/Example]
> author_ids = ["7589271892177518598"]
> similar_type = "content"

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: `author_ids*`[string], `similar_type`:string, `page`:integer, `limit`:integer

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| author_ids | array<string> | Yes | 创作者ID列表/List of creator author IDs | None | None | None |
| similar_type | string | No | 相似类型/Similarity type | content | None | None |
| page | integer | No | 页码/Page number | 1 | None | None |
| limit | integer | No | 每页数量/Page size | 12 | None | None |

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 | 200 | None | None |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 | None | None | None |
| message | string | No | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | None | None |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | None | None |
| support | string | No | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | None | None |
| time | string | No | The time the response was generated \| 生成响应的时间 | None | None | None |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 | None | None | None |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | None | None |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | None | None | None |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | None | None |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | None | None |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL | None | None | None |
| router | string | No | The endpoint that generated this response \| 生成此响应的端点 | None | None | None |
| params | dynamic object | No | The parameters used in the request \| 请求中使用的参数 | None | None | None |
| data | null | No | The response data \| 响应数据 | None | None | None |

<a id="get-api-u1-v1-douyin-xingtu-v2-get-resource-list"></a>
### `GET /api/u1/v1/douyin/xingtu_v2/get_resource_list`

- Summary: 获取营销活动案例/Get Resource List
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_resource_list_api_v1_douyin_xingtu_v2_get_resource_list_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取营销活动案例列表
> - 价格：0.001$ / 次
> ### 参数:
> - resource_id: 资源ID
> ### 返回:
> - 营销活动案例数据
>
> # [English]
> ### Purpose:
> - Get marketing activity resource list
> - Price: 0.001$ / time
> ### Parameters:
> - resource_id: Resource ID
> ### Return:
> - Marketing activity resource data
>
> # [示例/Example]
> resource_id = 1052

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| resource_id | query | integer | Yes | 资源ID/Resource ID | None | 1052 | None |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 | 200 | None | None |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 | None | None | None |
| message | string | No | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | None | None |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | None | None |
| support | string | No | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | None | None |
| time | string | No | The time the response was generated \| 生成响应的时间 | None | None | None |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 | None | None | None |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | None | None |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | None | None | None |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | None | None |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | None | None |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL | None | None | None |
| router | string | No | The endpoint that generated this response \| 生成此响应的端点 | None | None | None |
| params | dynamic object | No | The parameters used in the request \| 请求中使用的参数 | None | None | None |
| data | null | No | The response data \| 响应数据 | None | None | None |

<a id="get-api-u1-v1-douyin-xingtu-v2-get-user-profile-qrcode"></a>
### `GET /api/u1/v1/douyin/xingtu_v2/get_user_profile_qrcode`

- Summary: 获取用户主页二维码/Get User Profile QRCode
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_user_profile_qrcode_api_v1_douyin_xingtu_v2_get_user_profile_qrcode_get`

#### Notes

> # [中文]
> ### 用途:
> - 生成用户主页二维码
> - core_user_id和sec_uid二选一传入即可
> - 价格：0.001$ / 次
> ### 参数:
> - core_user_id: 用户核心ID（与sec_uid二选一）
> - sec_uid: 用户sec_uid（与core_user_id二选一）
> ### 返回:
> - 用户主页二维码数据
>
> # [English]
> ### Purpose:
> - Generate user profile QR code
> - Either core_user_id or sec_uid is required
> - Price: 0.001$ / time
> ### Parameters:
> - core_user_id: User core ID (pick one with sec_uid)
> - sec_uid: User sec_uid (pick one with core_user_id)
> ### Return:
> - User profile QR code data
>
> # [示例/Example]
> core_user_id = "1113181577281568"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| core_user_id | query | string | No | 用户核心ID(与sec_uid二选一)/User core ID (pick one with sec_uid) | None | 1113181577281568 | None |
| sec_uid | query | string | No | 用户sec_uid(与core_user_id二选一)/User sec_uid (pick one with core_user_id) | None | None | None |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 | 200 | None | None |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 | None | None | None |
| message | string | No | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | None | None |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | None | None |
| support | string | No | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | None | None |
| time | string | No | The time the response was generated \| 生成响应的时间 | None | None | None |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 | None | None | None |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | None | None |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | None | None | None |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | None | None |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | None | None |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL | None | None | None |
| router | string | No | The endpoint that generated this response \| 生成此响应的端点 | None | None | None |
| params | dynamic object | No | The parameters used in the request \| 请求中使用的参数 | None | None | None |
| data | null | No | The response data \| 响应数据 | None | None | None |
