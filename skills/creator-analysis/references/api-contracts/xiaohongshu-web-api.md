# Xiaohongshu-Web-API Full Contract

- Back to index: [`api-capability-index.md`](../api-capability-index.md)
- Back to route summary: [`api-tags/xiaohongshu-web-api.md`](../api-tags/xiaohongshu-web-api.md)
- Current contract file: `api-contracts/xiaohongshu-web-api.md`
- Source: `https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- Fetched at: `2026-03-08T06:54:04+00:00`
- Route count: `17`
- Default auth: Header `Authorization` Bearer
- Read this file only when you need precise auth notes, parameter descriptions, defaults, examples, or success-response fields.
- Tag description: **(小红书Web数据接口/Xiaohongshu-Web-API data endpoints)** - 第四优先/Fourth choice

## Route Contracts

<a id="post-api-u1-v1-xiaohongshu-web-get-home-recommend"></a>
### `POST /api/u1/v1/xiaohongshu/web/get_home_recommend`

- Summary: 获取首页推荐/Get home recommend
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_home_recommend_api_v1_xiaohongshu_web_get_home_recommend_post`

#### Notes

> # [中文]
> ### 用途:
> - 获取首页推荐
> ### 接口优先级:
> - 小红书接口推荐优先级: `App V2` > `App` > `Web V2` > `Web（本接口）`
> ### 参数:
> - feed_type: 推荐类型
>     - 全部: 0
>     - 穿搭: 1
>     - 美食: 2
>     - 彩妆: 3
>     - 影视: 4
>     - 职场: 5
>     - 情感: 6
>     - 家居: 7
>     - 游戏: 8
>     - 旅行: 9
>     - 健身: 10
> - need_filter_image: 是否只看图文笔记，默认为 False
> - cookie: 可选参数，用户自行提供的已登录的网页Cookie获取个性化推荐，如果不提供，则使用游客模式
> - proxy: 可选参数，网络代理，可降低封号概率，格式：http://用户名:密码@IP:端口/Proxy, format: http://username:password@IP:port
> ### 返回:
> - 推荐列表
>
> # [English]
> ### Purpose:
> - Get home recommend
> ### API Priority:
> - Xiaohongshu API priority: `App V2` > `App` > `Web V2` > `Web (this)`
> ### Parameters:
> - feed_type: Feed type
>     - Dress: 1
>     - Food: 2
>     - Makeup: 3
>     - Film: 4
>     - Workplace: 5
>     - Emotion: 6
>     - Home: 7
>     - Game: 8
>     - Travel: 9
>     - Fitness: 10
> - need_filter_image: Whether to view only image notes, default is False
> - cookie: Optional parameter, user-provided logged-in web Cookie to get personalized recommendations, if not provided, use visitor mode
> - proxy: Optional parameter, network proxy, can reduce the probability of account ban, format: http://username:password@IP:port
> ### Return:
> - Recommend list
>
> # [示例/Example]
> feed_type="0"
> need_filter_image=False

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: `feed_type`:string, `need_filter_image`:boolean, `cursor_score`:string, `cookie`:string, `proxy`:string

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| feed_type | string | No | 推荐类型/Feed type | 0 | None | None |
| need_filter_image | boolean | No | 是否只看图文笔记/Whether to view only image notes | false | None | None |
| cursor_score | string | No | 分页游标/Cursor for pagination | None | None | None |
| cookie | string | No | 用户自行提供的已登录的网页Cookie/User provided logged-in web Cookie | None | None | None |
| proxy | string | No | 代理，格式：http://用户名:密码@IP:端口/Proxy, format: http://username:password@IP:port | None | None | None |

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

<a id="get-api-u1-v1-xiaohongshu-web-get-note-comment-replies"></a>
### `GET /api/u1/v1/xiaohongshu/web/get_note_comment_replies`

- Summary: 获取笔记评论回复 V1/Get note comment replies V1
- Capabilities: comments / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_note_comment_replies_api_v1_xiaohongshu_web_get_note_comment_replies_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取笔记评论回复 V1
> ### 参数:
> - note_id: 笔记ID，可以从小红书的分享链接中获取
> - comment_id: 评论ID
> - lastCursor: 第一次请求时为空，之后请求时使用上一次请求响应中返回的游标
> ### 返回:
> - 笔记评论回复列表
>
> # [English]
> ### Purpose:
> - Get note comment replies V1
> ### Parameters:
> - note_id: Note ID, can be obtained from the sharing link of Xiaohongshu website.
> - comment_id: Comment ID
> - lastCursor: Last cursor, empty for the first request, use the cursor returned in the last response for subsequent requests
> ### Return:
> - Note comment replies list
>
> # [示例/Example]
> note_id="6683b283000000001f0052bf"
> comment_id="6683ec5b000000000303b91a"
> lastCursor=None

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| note_id | query | string | Yes | 笔记ID/Note ID | None | 6683b283000000001f0052bf | None |
| comment_id | query | string | Yes | 评论ID/Comment ID | None | 6683ec5b000000000303b91a | None |
| lastCursor | query | string | No | 上一页的游标/Last cursor | None | None | None |

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

<a id="get-api-u1-v1-xiaohongshu-web-get-note-comments"></a>
### `GET /api/u1/v1/xiaohongshu/web/get_note_comments`

- Summary: 获取笔记评论 V1/Get note comments V1
- Capabilities: comments / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_note_comments_api_v1_xiaohongshu_web_get_note_comments_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取笔记评论 V1
> ### 参数:
> - note_id: 笔记ID，可以从小红书的分享链接中获取
> - lastCursor: 第一次请求时为空，之后请求时使用上一次请求响应中返回的游标
> ### 返回:
> - 笔记评论列表
>
> # [English]
> ### Purpose:
> - Get note comments V1
> ### Parameters:
> - note_id: Note ID, can be obtained from the sharing link of Xiaohongshu website.
> - lastCursor: Last cursor, empty for the first request, use the cursor returned in the last response for subsequent requests
> ### Return:
> - Note comments list
>
> # [示例/Example]
> note_id="6683b283000000001f0052bf"
> lastCursor=None

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| note_id | query | string | Yes | 笔记ID/Note ID | None | 6683b283000000001f0052bf | None |
| lastCursor | query | string | No | 上一页的游标/Last cursor | None | None | None |

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

<a id="get-api-u1-v1-xiaohongshu-web-get-note-id-and-xsec-token"></a>
### `GET /api/u1/v1/xiaohongshu/web/get_note_id_and_xsec_token`

- Summary: 通过分享链接获取小红书的Note ID 和 xsec_token/Get Xiaohongshu Note ID and xsec_token by share link
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_note_id_and_xsec_token_api_v1_xiaohongshu_web_get_note_id_and_xsec_token_get`

#### Notes

> # [中文]
> ### 用途:
> - 通过分享链接获取小红书的Note ID 和 xsec_token
> ### 参数:
> - share_text: 小红书分享链接（支持APP和Web端分享链接）
> ### 返回:
> - Note ID 和 xsec_token
>
> # [English]
> ### Purpose:
> - Get Xiaohongshu Note ID and xsec_token by share link
> ### Parameters:
> - share_text: Xiaohongshu sharing link (support APP and Web sharing link)
> ### Return:
> - Note ID and xsec_token
>
> # [示例/Example]
> share_text="https://xhslink.com/a/EZ4M9TwMA6c3"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| share_text | query | string | Yes | 分享链接/Share link | None | https://xhslink.com/a/EZ4M9TwMA6c3 | None |

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

<a id="get-api-u1-v1-xiaohongshu-web-get-note-info-v2"></a>
### `GET /api/u1/v1/xiaohongshu/web/get_note_info_v2`

- Summary: 获取笔记信息 V2/Get note info V2
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_note_info_v2_api_v1_xiaohongshu_web_get_note_info_v2_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取笔记信息 V2
> ### 参数:
> - note_id: 笔记ID，可以从小红书的分享链接中获取
> - share_text: 小红书分享链接（支持APP和Web端分享链接）
> - 优先使用`note_id`，如果没有则使用`share_text`，两个参数二选一，如都携带则以`note_id`为准。
> ### 返回:
> - 笔记信息
>
> # [English]
> ### Purpose:
> - Get note info V2
> ### Parameters:
> - note_id: Note ID, can be obtained from the sharing link of Xiaohongshu website.
> - share_text: Xiaohongshu sharing link (support APP and Web sharing link)
> - Prefer to use `note_id`, if not, use `share_text`, one of the two parameters is required, if both are carried, `note_id` shall prevail.
> ### Return:
> - Note info
>
> # [示例/Example]
> note_id="665f95200000000006005624"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| note_id | query | string | No | 笔记ID/Note ID | None | 665f95200000000006005624 | None |
| share_text | query | string | No | 分享链接/Share link | None | https://xhslink.com/a/EZ4M9TwMA6c3 | None |

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

<a id="get-api-u1-v1-xiaohongshu-web-get-note-info-v4"></a>
### `GET /api/u1/v1/xiaohongshu/web/get_note_info_v4`

- Summary: 获取笔记信息 V4/Get note info V4
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_note_info_v4_api_v1_xiaohongshu_web_get_note_info_v4_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取笔记信息V4
> ### 参数:
> - note_id: 笔记ID，可以从小红书的分享链接中获取
> - share_text: 小红书分享链接（支持APP和Web端分享链接）
> - 优先使用`note_id`，如果没有则使用`share_text`，两个参数二选一，如都携带则以`note_id`为准。
> ### 返回:
> - 笔记信息
>
> # [English]
> ### Purpose:
> - Get note info V4
> ### Parameters:
> - note_id: Note ID, can be obtained from the sharing link of Xiaohongshu website.
> - share_text: Xiaohongshu sharing link (support APP and Web sharing link)
> - Prefer to use `note_id`, if not, use `share_text`, one of the two parameters is required, if both are carried, `note_id` shall prevail.
> ### Return:
> - Note info
>
> # [示例/Example]
> note_id="665f95200000000006005624"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| note_id | query | string | No | 笔记ID/Note ID | None | 665f95200000000006005624 | None |
| share_text | query | string | No | 分享链接/Share link | None | https://xhslink.com/a/EZ4M9TwMA6c3 | None |

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

<a id="post-api-u1-v1-xiaohongshu-web-get-note-info-v5"></a>
### `POST /api/u1/v1/xiaohongshu/web/get_note_info_v5`

- Summary: 获取笔记信息 V5 (自带Cookie)/Get note info V5 (Self-provided Cookie)
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_note_info_v5_api_v1_xiaohongshu_web_get_note_info_v5_post`

#### Notes

> # [中文]
> ### 用途:
> - 获取笔记信息V5，用户自行提供Cookie来获取笔记信息
> - 此接口收费0.001$
> ### 参数:
> - note_id: 笔记ID，可以从小红书的分享链接中获取
> - xsec_token: X-Sec-Token，可以从搜索接口中获取，分享链接中也有/X-Sec-Token, can be obtained from the search interface, also in the sharing link
> - cookie: 用户自行提供的已登录的网页Cookie
> - proxy: 代理，格式：http://用户名:密码@IP:端口/Proxy, format: http://username:password@IP:port
> - 最好使用代理，避免被封号或其他未知问题。
>
> ### 返回:
> - 笔记信息
>
> # [English]
> ### Purpose:
> - Get note info V5, user provides Cookie to get note info
> - This interface charges 0.001$
> ### Parameters:
> - note_id: Note ID, can be obtained from the sharing link of Xiaohongshu website.
> - xsec_token: X-Sec-Token, can be obtained from the search interface, also in the sharing link
> - cookie: User provided logged-in web Cookie
> - proxy: Proxy, format: http://username:password@IP:port
> - It is recommended to use a proxy to avoid being banned or other unknown issues.
> ### Return:
> - Note info
>
> # [示例/Example]
> note_id = "67855d09000000001703d449"
> xsec_token = "ABfpRSESmZDRbX-EX7lzEztktMngxPVC9kU-dgQmuQoNo="
> cookie = "Your Cookie"
> proxy = "http://username:password@IP:port"

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: `note_id`:string, `xsec_token`:string, `cookie`:string, `proxy`:string

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| note_id | string | No | 笔记ID/Note ID | 67855d09000000001703d449 | None | None |
| xsec_token | string | No | X-Sec-Token，可以从搜索接口中获取/X-Sec-Token, can be obtained from the search interface | ABfpRSESmZDRbX-EX7lzEztktMngxPVC9kU-dgQmuQoNo= | None | None |
| cookie | string | No | 用户自行提供的已登录的网页Cookie/User provided logged-in web Cookie | None | None | None |
| proxy | string | No | 代理，格式：http://用户名:密码@IP:端口/Proxy, format: http://username:password@IP:port | None | None | None |

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

<a id="get-api-u1-v1-xiaohongshu-web-get-note-info-v7"></a>
### `GET /api/u1/v1/xiaohongshu/web/get_note_info_v7`

- Summary: 获取笔记信息 V7/Get note info V7
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_note_info_v7_api_v1_xiaohongshu_web_get_note_info_v7_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取笔记信息V7
> ### 参数:
> - note_id: 笔记ID，可以从小红书的分享链接中获取
> - share_text: 小红书分享链接（支持APP和Web端分享链接）
> - 优先使用`note_id`，如果没有则使用`share_text`，两个参数二选一，如都携带则以`note_id`为准。
> ### 返回:
> - 笔记信息
>
> # [English]
> ### Purpose:
> - Get note info V7
> ### Parameters:
> - note_id: Note ID, can be obtained from the sharing link of Xiaohongshu website.
> - share_text: Xiaohongshu sharing link (support APP and Web sharing link)
> - Prefer to use `note_id`, if not, use `share_text`, one of the two parameters is required, if both are carried, `note_id` shall prevail.
> ### Return:
> - Note info
>
> # [示例/Example]
> note_id="665f95200000000006005624"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| note_id | query | string | No | 笔记ID/Note ID | None | 665f95200000000006005624 | None |
| share_text | query | string | No | 分享链接/Share link | None | https://xhslink.com/a/EZ4M9TwMA6c3 | None |

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

<a id="get-api-u1-v1-xiaohongshu-web-get-product-info"></a>
### `GET /api/u1/v1/xiaohongshu/web/get_product_info`

- Summary: 获取小红书商品信息/Get Xiaohongshu product info
- Capabilities: commerce
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_product_info_api_v1_xiaohongshu_web_get_product_info_get`

#### Notes

> # [中文]
> ### 用途:
> - 通过分享链接获取小红书的商品信息
> ### 参数:
> - share_text: 小红书分享链接（支持APP和Web端分享链接）
> - item_id: 商品ID
> - xsec_token: X-Sec-Token
> - 如果share_text不为空，则item_id和xsec_token会被忽略
> - 如果share_text为空，则item_id和xsec_token不能为空
> ### 返回:
> - 商品信息
>
> # [English]
> ### Purpose:
> - Get Xiaohongshu product info by share link
> ### Parameters:
> - share_text: Xiaohongshu sharing link (support APP and Web sharing link)
> - item_id: Item ID
> - xsec_token: X-Sec-Token
> - If share_text is not empty, item_id and xsec_token will be ignored
> - If share_text is empty, item_id and xsec_token cannot be empty
> ### Return:
> - Product info
>
> # [示例/Example]
> item_id="65fc2e6d6b92310001d24efb"
> xsec_token="XBC6LTqeaEDeJETMoXo436Eg-74GxFemVnNHeONYobv7k="

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| share_text | query | string | No | 分享链接/Share link | None | None | None |
| item_id | query | string | No | 商品ID/Item ID | None | 65fc2e6d6b92310001d24efb | None |
| xsec_token | query | string | No | X-Sec-Token | None | XBC6LTqeaEDeJETMoXo436Eg-74GxFemVnNHeONYobv7k= | None |

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

<a id="get-api-u1-v1-xiaohongshu-web-get-user-info"></a>
### `GET /api/u1/v1/xiaohongshu/web/get_user_info`

- Summary: 获取用户信息 V1/Get user info V1
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_user_info_api_v1_xiaohongshu_web_get_user_info_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取用户信息 V1
> ### 参数:
> - user_id: 用户ID，可以从小红书的分享链接中获取
> ### 返回:
> - 用户信息
>
> # [English]
> ### Purpose:
> - Get user info V1
> ### Parameters:
> - user_id: User ID, can be obtained from the sharing link of Xiaohongshu website.
> ### Return:
> - User info
>
> # [示例/Example]
> user_id="5f4a10070000000001006fc7"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| user_id | query | string | Yes | 用户ID/User ID | None | 5f4a10070000000001006fc7 | None |

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

<a id="get-api-u1-v1-xiaohongshu-web-get-user-info-v2"></a>
### `GET /api/u1/v1/xiaohongshu/web/get_user_info_v2`

- Summary: 获取用户信息 V2/Get user info V2
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_user_info_v2_api_v1_xiaohongshu_web_get_user_info_v2_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取用户信息 V2
> ### 参数:
> - user_id: 用户ID，可以从小红书的分享链接中获取
> - share_text: 小红书分享文本或链接（支持APP和Web端分享链接）
> - 优先使用`user_id`，如果没有则使用`share_text`，两个参数二选一，如都携带则以`user_id`为准。
> ### 返回:
> - 用户信息
>
> # [English]
> ### Purpose:
> - Get user info V2
> ### Parameters:
> - user_id: User ID, can be obtained from the sharing link of Xiaohongshu website.
> - share_text: Xiaohongshu sharing text or link (support APP and Web sharing link)
> - Prefer to use `user_id`, if not, use `share_text`, one of the two parameters is required, if both are carried, `user_id` shall prevail.
> ### Return:
> - User info
>
> # [示例/Example]
> user_id = "5f4a10070000000001006fc7"
> share_text = "@Noo 在小红书收获了15.3万次赞与收藏，查看Ta的主页>> https://xhslink.com/m/7XkrlCXbL38"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| user_id | query | string | No | 用户ID/User ID | None | 5f4a10070000000001006fc7 | None |
| share_text | query | string | No | 分享文本或链接/Share text or link | None | 示例: @Noo 在小红书收获了15.3万次赞与收藏，查看Ta的主页>> https://xhslink.com/m/7XkrlCXbL38 | None |

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

<a id="get-api-u1-v1-xiaohongshu-web-get-user-notes-v2"></a>
### `GET /api/u1/v1/xiaohongshu/web/get_user_notes_v2`

- Summary: 获取用户的笔记 V2/Get user notes V2
- Capabilities: profiles / accounts / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_user_notes_api_v1_xiaohongshu_web_get_user_notes_v2_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取用户的笔记
> ### 参数:
> - user_id: 用户ID，可以从小红书的分享链接中获取
> - lastCursor: 第一次请求时为空，之后请求时使用上一次请求响应中返回的最后一个NoteID
>     - 例如: "662908190000000001007366"
>     - JSON Path: $.data.data.notes.[-1].id
> ### 返回:
> - 用户的笔记列表
>
> # [English]
> ### Purpose:
> - Get user notes
> ### Parameters:
> - user_id: User ID, can be obtained from the sharing link of Xiaohongshu website.
> - lastCursor: Last cursor, empty for the first request, use the last NoteID returned in the last response for subsequent requests
>     - Example: "662908190000000001007366"
>     - JSON Path: $.data.data.notes.[-1].id
> ### Return:
> - User notes list
>
> # [示例/Example]
> user_id="5f4a10070000000001006fc7"
> lastCursor=None

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| user_id | query | string | Yes | 用户ID/User ID | None | 5f4a10070000000001006fc7 | None |
| lastCursor | query | string | No | 上一页的游标/Last cursor | None | None | None |

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

<a id="get-api-u1-v1-xiaohongshu-web-get-visitor-cookie"></a>
### `GET /api/u1/v1/xiaohongshu/web/get_visitor_cookie`

- Summary: 获取游客Cookie/Get visitor cookie
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_visitor_cookie_api_v1_xiaohongshu_web_get_visitor_cookie_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取小红书网页版的游客Cookie，可以用于爬取小红书的一些数据。
> ### 参数:
> - proxy: 代理，例如: http://username:password@host:port
> - 代理格式支持HTTP和SOCKS5，若不需要代理则留空
> ### 返回:
> - 游客Cookie
>
> # [English]
> ### Purpose:
> - Get Xiaohongshu web visitor cookie, which can be used to crawl some data of Xiaohongshu.
> ### Parameters:
> - proxy: Proxy, e.g. http://username:password@host:port
> ### Return:
> - Visitor cookie

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| proxy | query | string | No | 代理/Proxy | None | None | None |

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

<a id="get-api-u1-v1-xiaohongshu-web-search-notes"></a>
### `GET /api/u1/v1/xiaohongshu/web/search_notes`

- Summary: 搜索笔记/Search notes
- Capabilities: search / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `search_notes_api_v1_xiaohongshu_web_search_notes_get`

#### Notes

> # [中文]
> ### 用途:
> - 搜索笔记
> ### 参数:
> - keyword: 搜索关键词
> - page: 页码，默认为1
> - sort: 排序方式
>     - 综合排序（默认参数）: general
>     - 最热排序: popularity_descending
>     - 最新排序: time_descending
>     - 最多评论: comment_descending
>     - 最多收藏: collect_descending
> - noteType: 笔记类型
>     - 综合笔记（默认参数）: _0
>     - 视频笔记: _1
>     - 图文笔记: _2
>     - 直播: _3
> - noteTime: 发布时间
>     - 不限: ""
>     - 一天内 :一天内
>     - 一周内 :一周内
>     - 半年内 :半年内
> ### 返回:
> - 笔记列表
>
> # [English]
> ### Purpose:
> - Search notes
> ### Parameters:
> - keyword: Keyword
> - page: Page, default is 1
> - sort: Sort
>     - General sort (default): general
>     - Popularity sort: popularity_descending
>     - Latest sort: time_descending
>     - Most comments: comment_descending
>     - Most favorites: collect_descending
> - noteType: Note type
>     - General note (default): _0
>     - Video note: _1
>     - Image note: _2
>     - Live: _3
> - noteTime: Release time
>     - No limit: ""
>     - Within one day: 一天内
>     - Within one week: 一周内
>     - Within half a year: 半年内
> ### Return:
> - Note list
>
> # [示例/Example]
> keyword="美食"
> page=1
> sort="general"
> noteType="_0"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| keyword | query | string | Yes | 搜索关键词/Keyword | None | 美食 | None |
| page | query | integer | No | 页码/Page | 1 | 1 | None |
| sort | query | string | No | 排序方式/Sort | general | general | None |
| noteType | query | string | No | 笔记类型/Note type | _0 | _0 | None |
| noteTime | query | string | No | 发布时间/Release time | None | None | None |

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

<a id="get-api-u1-v1-xiaohongshu-web-search-notes-v3"></a>
### `GET /api/u1/v1/xiaohongshu/web/search_notes_v3`

- Summary: 搜索笔记 V3/Search notes V3
- Capabilities: search / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `search_notes_v3_api_v1_xiaohongshu_web_search_notes_v3_get`

#### Notes

> # [中文]
> ### 用途:
> - 搜索笔记 V3
> ### 参数:
> - keyword: 搜索关键词
> - page: 页码，默认为1
> - sort: 排序方式
>     - 综合排序（默认参数）: general
>     - 最热排序: popularity_descending
>     - 最新排序: time_descending
>     - 最多评论: comment_descending
>     - 最多收藏: collect_descending
> - noteType: 笔记类型
>     - 综合笔记（默认参数）: _0
>     - 视频笔记: _1
>     - 图文笔记: _2
>     - 直播: _3
> - noteTime: 发布时间
>     - 不限: ""
>     - 一天内 :一天内
>     - 一周内 :一周内
>     - 半年内 :半年内
> ### 返回:
> - 笔记列表
>
> # [English]
> ### Purpose:
> - Search notes V3
> ### Parameters:
> - keyword: Keyword
> - page: Page, default is 1
> - sort: Sort
>     - General sort (default): general
>     - Popularity sort: popularity_descending
>     - Latest sort: time_descending
>     - Most comments: comment_descending
>     - Most favorites: collect_descending
> - noteType: Note type
>     - General note (default): _0
>     - Video note: _1
>     - Image note: _2
>     - Live: _3
> - noteTime: Release time
>     - No limit: ""
>     - Within one day: 一天内
>     - Within one week: 一周内
>     - Within half a year: 半年内
> ### Return:
> - Note list
>
> # [示例/Example]
> keyword="美食"
> page=1
> sort="general"
> noteType="_0"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| keyword | query | string | Yes | 搜索关键词/Keyword | None | 美食 | None |
| page | query | integer | No | 页码/Page | 1 | 1 | None |
| sort | query | string | No | 排序方式/Sort | general | general | None |
| noteType | query | string | No | 笔记类型/Note type | _0 | _0 | None |
| noteTime | query | string | No | 发布时间/Release time | None | None | None |

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

<a id="get-api-u1-v1-xiaohongshu-web-search-users"></a>
### `GET /api/u1/v1/xiaohongshu/web/search_users`

- Summary: 搜索用户/Search users
- Capabilities: search / profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `search_users_api_v1_xiaohongshu_web_search_users_get`

#### Notes

> # [中文]
> ### 用途:
> - 搜索用户
> ### 参数:
> - keyword: 搜索关键词
> - page: 页码，默认为1
> ### 返回:
> - 用户列表
>
> # [English]
> ### Purpose:
> - Search users
> ### Parameters:
> - keyword: Keyword
> - page: Page, default is 1
> ### Return:
> - User list
>
> # [示例/Example]
> keyword="美食"
> page=1

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| keyword | query | string | Yes | 搜索关键词/Keyword | None | 美食 | None |
| page | query | integer | No | 页码/Page | 1 | 1 | None |

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

<a id="post-api-u1-v1-xiaohongshu-web-sign"></a>
### `POST /api/u1/v1/xiaohongshu/web/sign`

- Summary: 小红书Web签名/Xiaohongshu Web sign
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `sign_api_v1_xiaohongshu_web_sign_post`

#### Notes

> # [中文]
> ### 用途:
> - 小红书Web签名，用于获取小红书的一些数据。
> - 生成 `X-s`, `X-t`, `X-s-common` 等签名参数。
> - 价格：0.001$/次
> ### 参数:
> - sign_request: 签名请求模型
>     - path: 请求接口的路径，例如: `/api/sns/web/v1/homefeed`
>     - data: 请求API的荷载数据
>     - cookie: 请求接口的Cookie
> ### 返回:
> - 签名参数(X-s, X-t, X-s-common等)
>
> # [English]
> ### Purpose:
> - Xiaohongshu Web sign, used to get some data of Xiaohongshu.
> - Generate `X-s`, `X-t`, `X-s-common` and other signature parameters.
> - Price: 0.001$/time
> ### Parameters:
> - sign_request: Sign request model
>     - path: Request API path, e.g. `/api/sns/web/v1/homefeed`
>     - data: Payload data of request API
>     - cookie: Request API cookie
> ### Return:
> - Signature parameters(X-s, X-t, X-s-common, etc.)
>
> # [示例/Example]
> {
>     "path": "/api/sns/web/v1/homefeed",
>     "data": {
>         "cursor_score": "",
>         "num": 35,
>         "refresh_type": 1,
>         "note_index": 35,
>         "unread_begin_note_id": "",
>         "unread_end_note_id": "",
>         "unread_note_count": 0,
>         "category": "homefeed_recommend",
>         "search_key": "",
>         "need_num": 10,
>         "image_formats": [
>             "jpg",
>             "webp",
>             "avif"
>         ],
>         "need_filter_image": False
>     },
>     "cookie": "web_session=030037a04eafd37791e6e4bd05204a8cf2af05;acw_tc=0a00d79f17363096679345838efb77751cc087fb039dd1691dc954824410f6;abRequestId=384480ae-5196-5818-a835-42e6278de9f0;webBuild=4.47.1;xsecappid=xhs-pc-web;a1=194441ef694PayUbdUvgp0dSHfIcACsNsLud0Lgru50000354513;webId=6cf10a564b9b07d129729b65e0d1785a;sec_poison_id=32964532-d414-4beb-914f-98811853b75f"
> }

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: `path`:string, `data`{...}, `cookie`:string

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| path | string | No | 请求接口的路径/Request API path | /api/sns/web/v1/homefeed | None | None |
| data | object | No | 请求API的荷载数据/Payload data of request API | {"cursor_score": "", "num": 35, "refresh_type": 1, "note_index": 35, "unread_be… | None | None |
| cookie | string | No | 请求接口的Cookie/Request API cookie | web_session=030037a04eafd37791e6e4bd05204a8cf2af05;acw_tc=0a00d79f1736309667934… | None | None |

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
