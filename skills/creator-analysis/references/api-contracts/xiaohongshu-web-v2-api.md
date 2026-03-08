# Xiaohongshu-Web-V2-API Full Contract

- Back to index: [`api-capability-index.md`](../api-capability-index.md)
- Back to route summary: [`api-tags/xiaohongshu-web-v2-api.md`](../api-tags/xiaohongshu-web-v2-api.md)
- Current contract file: `api-contracts/xiaohongshu-web-v2-api.md`
- Source: `https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- Fetched at: `2026-03-08T06:54:04+00:00`
- Route count: `18`
- Default auth: Header `Authorization` Bearer
- Read this file only when you need precise auth notes, parameter descriptions, defaults, examples, or success-response fields.
- Tag description: **(小红书Web V2数据接口/Xiaohongshu-Web-V2-API data endpoints)** - 第三优先/Third choice

## Route Contracts

<a id="get-api-u1-v1-xiaohongshu-web-v2-fetch-feed-notes"></a>
### `GET /api/u1/v1/xiaohongshu/web_v2/fetch_feed_notes`

- Summary: 获取单一笔记和推荐笔记 V1 (已弃用)/Fetch one note and feed notes V1 (deprecated)
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_feed_notes_api_v1_xiaohongshu_web_v2_fetch_feed_notes_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取单一笔记和推荐笔记
> ### 接口优先级:
> - 小红书接口推荐优先级: `App V2` > `App` > `Web V2（本接口）` > `Web`
> ### 参数:
> - note_id: 笔记ID，可以从小红书的分享链接中获取
> ### 返回:
> - 单一笔记和推荐笔记
>
> # [English]
> ### Purpose:
> - Get one note and feed notes
> ### API Priority:
> - Xiaohongshu API priority: `App V2` > `App` > `Web V2 (this)` > `Web`
> ### Parameters:
> - note_id: Note ID, can be obtained from the sharing link of Xiaohongshu website.
> ### Return:
> - One note and feed notes
>
> # [示例/Example]
> note_id = "66c9cc31000000001f03a4bc"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| note_id | query | string | Yes | 笔记ID/Note ID | None | 66c9cc31000000001f03a4bc | None |

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

<a id="get-api-u1-v1-xiaohongshu-web-v2-fetch-feed-notes-v2"></a>
### `GET /api/u1/v1/xiaohongshu/web_v2/fetch_feed_notes_v2`

- Summary: 获取单一笔记和推荐笔记 V2/Fetch one note and feed notes V2(v2稳定, 推荐使用此接口)
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_feed_notes_v2_api_v1_xiaohongshu_web_v2_fetch_feed_notes_v2_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取单一笔记和推荐笔记
> ### 接口优先级:
> - 小红书接口推荐优先级: `App V2` > `App` > `Web V2（本接口）` > `Web`
> ### 参数:
> - note_id: 笔记ID，可以从小红书的分享链接中获取
> ### 返回:
> - 单一笔记和推荐笔记
>
> # [English]
> ### Purpose:
> - Get one note and feed notes
> ### API Priority:
> - Xiaohongshu API priority: `App V2` > `App` > `Web V2 (this)` > `Web`
> ### Parameters:
> - note_id: Note ID, can be obtained from the sharing link of Xiaohongshu website.
> ### Return:
> - One note and feed notes
>
> # [示例/Example]
> note_id = "66c9cc31000000001f03a4bc"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| note_id | query | string | Yes | 笔记ID/Note ID | None | 66c9cc31000000001f03a4bc | None |

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

<a id="get-api-u1-v1-xiaohongshu-web-v2-fetch-feed-notes-v3"></a>
### `GET /api/u1/v1/xiaohongshu/web_v2/fetch_feed_notes_v3`

- Summary: 获取单一笔记和推荐笔记 V3/Fetch one note and feed notes V3(通过短链获取笔记详情)
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_feed_notes_v3_api_v1_xiaohongshu_web_v2_fetch_feed_notes_v3_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取单一笔记和推荐笔记
> ### 参数:
> - short_url: 短链，可以从小红书的分享链接中获取
> ### 返回:
> - 单一笔记和推荐笔记
>
> # [English]
> ### Purpose:
> - Get one note and feed notes
> ### Parameters:
> - short_url: Short URL, can be obtained from the sharing link of Xiaohongshu website.
> ### Return:
> - One note and feed notes
>
> # [示例/Example]
> short_url = "http://xhslink.com/a/tyoREa3ciaAeb"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| short_url | query | string | Yes | 短链/Short URL | None | http://xhslink.com/a/tyoREa3ciaAeb | None |

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

<a id="get-api-u1-v1-xiaohongshu-web-v2-fetch-feed-notes-v4"></a>
### `GET /api/u1/v1/xiaohongshu/web_v2/fetch_feed_notes_v4`

- Summary: 获取单一笔记和推荐笔记 V4 (互动量有延迟)/Fetch one note and feed notes V4 (interaction volume has a delay)
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_feed_notes_v4_api_v1_xiaohongshu_web_v2_fetch_feed_notes_v4_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取单一笔记和推荐笔记，结构不同互动量有延时
> ### 参数:
> - note_id: 笔记ID，可以从小红书的分享链接中获取
> ### 返回:
> - 单一笔记和推荐笔记
>
> # [English]
> ### Purpose:
> - Get one note and feed notes, the structure is different and the interaction volume has a delay
> ### Parameters:
> - note_id: Note ID, can be obtained from the sharing link of Xiaohongshu website.
> ### Return:
> - One note and feed notes
>
> # [示例/Example]
> note_id = "66c9cc31000000001f03a4bc"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| note_id | query | string | Yes | 笔记ID/Note ID | None | 66c9cc31000000001f03a4bc | None |

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

<a id="get-api-u1-v1-xiaohongshu-web-v2-fetch-feed-notes-v5"></a>
### `GET /api/u1/v1/xiaohongshu/web_v2/fetch_feed_notes_v5`

- Summary: 获取单一笔记和推荐笔记 V5 (互动量有缺失)/Fetch one note and feed notes V5 (interaction volume has a missing)
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_feed_notes_v5_api_v1_xiaohongshu_web_v2_fetch_feed_notes_v5_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取单一笔记和推荐笔记，结构不同互动量有缺失
> ### 参数:
> - note_id: 笔记ID，可以从小红书的分享链接中获取
> ### 返回:
> - 单一笔记和推荐笔记
> ### 备注:
> - 互动数据仅有点赞数，没有评论数与收藏数
>
> # [English]
> ### Purpose:
> - Get one note and feed notes, the structure is different and the interaction volume has a missing
> ### Parameters:
> - note_id: Note ID, can be obtained from the sharing link of Xiaohongshu website.
> ### Return:
> - One note and feed notes
> ### Notes:
> - Interaction data only includes likes, without comments and favorites.
>
> # [示例/Example]
> note_id = "66c9cc31000000001f03a4bc"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| note_id | query | string | Yes | 笔记ID/Note ID | None | 66c9cc31000000001f03a4bc | None |

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

<a id="get-api-u1-v1-xiaohongshu-web-v2-fetch-follower-list"></a>
### `GET /api/u1/v1/xiaohongshu/web_v2/fetch_follower_list`

- Summary: 获取用户粉丝列表/Fetch follower list
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_follower_list_api_v1_xiaohongshu_web_v2_fetch_follower_list_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取用户粉丝列表
> ### 参数:
> - user_id: 用户ID
> - cursor: 游标
> ### 返回:
> - 用户粉丝列表
>
> # [English]
> ### Purpose:
> - Get follower list
> ### Parameters:
> - user_id: User ID
> - cursor: Cursor
> ### Return:
> - Follower list
>
> # [示例/Example]
> user_id = "604a28420000000001005211"
> cursor = ""

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| user_id | query | string | Yes | 用户ID/User ID | None | 604a28420000000001005211 | None |
| cursor | query | string | No | 游标/Cursor | None | None | None |

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

<a id="get-api-u1-v1-xiaohongshu-web-v2-fetch-following-list"></a>
### `GET /api/u1/v1/xiaohongshu/web_v2/fetch_following_list`

- Summary: 获取用户关注列表/Fetch following list
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_following_list_api_v1_xiaohongshu_web_v2_fetch_following_list_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取用户关注列表
> ### 参数:
> - user_id: 用户ID
> - cursor: 游标
> ### 返回:
> - 用户关注列表
>
> # [English]
> ### Purpose:
> - Get following list
> ### Parameters:
> - user_id: User ID
> - cursor: Cursor
> ### Return:
> - Following list
>
> # [示例/Example]
> user_id = "604a28420000000001005211"
> cursor = ""

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| user_id | query | string | Yes | 用户ID/User ID | None | 604a28420000000001005211 | None |
| cursor | query | string | No | 游标/Cursor | None | None | None |

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

<a id="get-api-u1-v1-xiaohongshu-web-v2-fetch-home-notes"></a>
### `GET /api/u1/v1/xiaohongshu/web_v2/fetch_home_notes`

- Summary: 获取Web用户主页笔记/Fetch web user profile notes
- Capabilities: profiles / accounts / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_home_notes_api_v1_xiaohongshu_web_v2_fetch_home_notes_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取主页笔记
> ### 参数:
> - user_id: 用户ID
> - cursor: 游标
> ### 返回:
> - 主页笔记
>
> # [English]
> ### Purpose:
> - Get home notes
> ### Parameters:
> - user_id: User ID
> - cursor: Cursor
> ### Return:
> - Home notes
>
> # [示例/Example]
> user_id = "5f3e0d00000000001f03a4bc"
> cursor = ""

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| user_id | query | string | Yes | 用户ID/User ID | None | 5e3a8ee700000000010070c6 | None |
| cursor | query | string | No | 游标/Cursor | None | None | None |

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

<a id="get-api-u1-v1-xiaohongshu-web-v2-fetch-home-notes-app"></a>
### `GET /api/u1/v1/xiaohongshu/web_v2/fetch_home_notes_app`

- Summary: 获取App用户主页笔记/Fetch App user home notes
- Capabilities: profiles / accounts / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_home_notes_app_api_v1_xiaohongshu_web_v2_fetch_home_notes_app_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取App主页笔记
> ### 参数:
> - user_id: 用户ID
> - cursor: 游标
> ### 返回:
> - 主页笔记
>
> # [English]
> ### Purpose:
> - Get home notes
> ### Parameters:
> - user_id: User ID
> - cursor: Cursor
> ### Return:
> - Home notes
>
> # [示例/Example]
> user_id = "5f3e0d00000000001f03a4bc"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| user_id | query | string | Yes | 用户ID/User ID | None | 5e3a8ee700000000010070c6 | None |
| cursor | query | string | No | 游标/Cursor | None | None | None |

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

<a id="get-api-u1-v1-xiaohongshu-web-v2-fetch-hot-list"></a>
### `GET /api/u1/v1/xiaohongshu/web_v2/fetch_hot_list`

- Summary: 获取小红书热榜/Fetch Xiaohongshu hot list
- Capabilities: trends / rankings
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_hot_list_api_v1_xiaohongshu_web_v2_fetch_hot_list_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取小红书热榜
> ### 返回:
> - 小红书热榜
>
> # [English]
> ### Purpose:
> - Get Xiaohongshu hot list
> ### Return:
> - Xiaohongshu hot list
>
> # [示例/Example]

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

<a id="get-api-u1-v1-xiaohongshu-web-v2-fetch-note-comments"></a>
### `GET /api/u1/v1/xiaohongshu/web_v2/fetch_note_comments`

- Summary: 获取笔记评论/Fetch note comments
- Capabilities: comments / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_note_comments_api_v1_xiaohongshu_web_v2_fetch_note_comments_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取笔记评论
> ### 参数:
> - note_id: 笔记ID
> - cursor: 游标
> ### 返回:
> - 笔记评论
>
> # [English]
> ### Purpose:
> - Get note comments
> ### Parameters:
> - note_id: Note ID
> - cursor: Cursor
> ### Return:
> - Note comments
>
> # [示例/Example]
> note_id = "651ccaa9000000001f03d7f7"
> cursor = ""

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| note_id | query | string | Yes | 笔记ID/Note ID | None | 651ccaa9000000001f03d7f7 | None |
| cursor | query | string | No | 游标/Cursor | None | None | None |

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

<a id="get-api-u1-v1-xiaohongshu-web-v2-fetch-note-image"></a>
### `GET /api/u1/v1/xiaohongshu/web_v2/fetch_note_image`

- Summary: 获取小红书笔记图片/Fetch Xiaohongshu note image
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_note_image_api_v1_xiaohongshu_web_v2_fetch_note_image_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取小红书笔记图片
> ### 参数:
> - note_id: 笔记ID，可以从小红书的分享链接中获取
> ### 返回:
> - 小红书笔记图片
>
> # [English]
> ### Purpose:
> - Get Xiaohongshu note image
> ### Parameters:
> - note_id: Note ID, can be obtained from the sharing link of Xiaohongshu website.
> ### Return:
> - Xiaohongshu note image
>
> # [示例/Example]
> note_id = "66c9cc31000000001f03a4bc"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| note_id | query | string | Yes | 笔记ID/Note ID | None | 66c9cc31000000001f03a4bc | None |

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

<a id="get-api-u1-v1-xiaohongshu-web-v2-fetch-product-list"></a>
### `GET /api/u1/v1/xiaohongshu/web_v2/fetch_product_list`

- Summary: 获取小红书商品列表/Fetch Xiaohongshu product list
- Capabilities: commerce
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_product_list_api_v1_xiaohongshu_web_v2_fetch_product_list_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取小红书商品列表
> ### 参数:
> - user_id: 用户ID
> - page: 页码
> ### 返回:
> - 小红书商品列表
>
> # [English]
> ### Purpose:
> - Get Xiaohongshu product list
> ### Parameters:
> - user_id: User ID
> - page: Page number
> ### Return:
> - Xiaohongshu product list
>
> # [示例/Example]
> user_id = "627e35aa00000000210275ae"
> page = "1"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| user_id | query | string | Yes | 用户ID/User ID | None | 627e35aa00000000210275ae | None |
| page | query | string | No | 页码/Page number | 1 | None | None |

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

<a id="get-api-u1-v1-xiaohongshu-web-v2-fetch-search-notes"></a>
### `GET /api/u1/v1/xiaohongshu/web_v2/fetch_search_notes`

- Summary: 获取搜索笔记/Fetch search notes
- Capabilities: search / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_search_notes_api_v1_xiaohongshu_web_v2_fetch_search_notes_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取搜索笔记
> ### 参数:
> - keywords：搜索关键词
> - sort_type：排序方式
>     - general：综合
>     - time_descending：最新
>     - popularity_descending：最热
> - note_type: 笔记类型
>     - 0：全部
>     - 1：视频
>     - 2：图文
> ### 返回:
> - 搜索笔记
>
> # [English]
> ### Purpose:
> - Get search notes
> ### Parameters:
> - keywords: Search keywords
> - sort_type: Sort type
>     - general: General
>     - time_descending: Latest
>     - popularity_descending: Popular
> - note_type: Note type
>     - 0: All
>     - 1: Video
>     - 2: Note
> ### Return:
> - Search notes
>
> # [示例/Example]
> keywords = "口红"
> page = 1
> sort_type = "general"
> note_type = "1"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| keywords | query | string | Yes | 搜索关键词/Search keywords | None | 口红 | None |
| page | query | integer | No | 页码/Page number | 1 | None | None |
| sort_type | query | string | No | 排序方式/Sort type | general | None | None |
| note_type | query | string | No | 笔记类型/Note type | 0 | None | None |

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

<a id="get-api-u1-v1-xiaohongshu-web-v2-fetch-search-users"></a>
### `GET /api/u1/v1/xiaohongshu/web_v2/fetch_search_users`

- Summary: 获取搜索用户/Fetch search users
- Capabilities: search / profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_search_notes_api_v1_xiaohongshu_web_v2_fetch_search_users_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取搜索用户
> ### 参数:
> - keywords：搜索关键词
> - page：页码
> ### 返回:
> - 搜索用户
>
> # [English]
> ### Purpose:
> - Get search users
> ### Parameters:
> - keywords: Search keywords
> - page: Page number
> ### Return:
> - Search users
>
> # [示例/Example]
> keywords = "口红"
> page = 1

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| keywords | query | string | Yes | 搜索关键词/Search keywords | None | 口红 | None |
| page | query | integer | No | 页码/Page number | 1 | None | None |

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

<a id="get-api-u1-v1-xiaohongshu-web-v2-fetch-sub-comments"></a>
### `GET /api/u1/v1/xiaohongshu/web_v2/fetch_sub_comments`

- Summary: 获取子评论/Fetch sub comments
- Capabilities: comments
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_sub_comments_api_v1_xiaohongshu_web_v2_fetch_sub_comments_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取子评论
> ### 参数:
> - note_id: 笔记ID
> - comment_id: 评论ID
> - cursor: 游标
> ### 返回:
> - 子评论
>
> # [English]
> ### Purpose:
> - Get sub comments
> ### Parameters:
> - note_id: Note ID
> - comment_id: Comment ID
> - cursor: Cursor
> ### Return:
> - Sub comments
>
> # [示例/Example]
> note_id = "673c894c0000000007033f92"
> comment_id = "673ecdfc000000001503bf8b"
> cursor = ""

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| note_id | query | string | Yes | 笔记ID/Note ID | None | 673c894c0000000007033f92 | None |
| comment_id | query | string | Yes | 评论ID/Comment ID | None | 673ecdfc000000001503bf8b | None |
| cursor | query | string | No | 游标/Cursor | None | None | None |

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

<a id="get-api-u1-v1-xiaohongshu-web-v2-fetch-user-info"></a>
### `GET /api/u1/v1/xiaohongshu/web_v2/fetch_user_info`

- Summary: 获取用户信息/Fetch user info
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_info_api_v1_xiaohongshu_web_v2_fetch_user_info_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取用户信息
> ### 参数:
> - user_id: 用户ID
> ### 返回:
> - 用户信息
>
> # [English]
> ### Purpose:
> - Get user info
> ### Parameters:
> - user_id: User ID
> ### Return:
> - User info
>
> # [示例/Example]
> user_id = "5e3a8ee700000000010070c6"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| user_id | query | string | Yes | 用户ID/User ID | None | 5e3a8ee700000000010070c6 | None |

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

<a id="get-api-u1-v1-xiaohongshu-web-v2-fetch-user-info-app"></a>
### `GET /api/u1/v1/xiaohongshu/web_v2/fetch_user_info_app`

- Summary: 获取App用户信息/Fetch App user info
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_info_api_v1_xiaohongshu_web_v2_fetch_user_info_app_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取用户信息
> ### 参数:
> - user_id: 用户ID
> ### 返回:
> - 用户信息
>
> # [English]
> ### Purpose:
> - Get user info
> ### Parameters:
> - user_id: User ID
> ### Return:
> - User info
>
> # [示例/Example]
> user_id = "5e3a8ee700000000010070c6"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| user_id | query | string | Yes | 用户ID/User ID | None | 5e3a8ee700000000010070c6 | None |

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
