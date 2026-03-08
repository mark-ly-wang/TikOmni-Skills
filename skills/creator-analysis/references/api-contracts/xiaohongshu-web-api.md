# Xiaohongshu-Web-API 完整契约

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 回到路由详情：[`api-tags/xiaohongshu-web-api.md`](../api-tags/xiaohongshu-web-api.md)
- 当前契约文件：`api-contracts/xiaohongshu-web-api.md`
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T04:31:58+00:00`
- 路由数：`17`
- 默认认证：请求头 `Authorization` Bearer
- 使用方式：当需要精确的认证说明、参数描述、默认值、示例或成功响应字段时，再读本文件。
- 标签说明：**(小红书Web数据接口/Xiaohongshu-Web-API data endpoints)** - 第四优先/Fourth choice

## 路由契约

<a id="post-api-u1-v1-xiaohongshu-web-get-home-recommend"></a>
### `POST /api/u1/v1/xiaohongshu/web/get_home_recommend`

- 摘要：获取首页推荐/Get home recommend
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_home_recommend_api_v1_xiaohongshu_web_get_home_recommend_post`

#### 说明

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

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`feed_type`:string, `need_filter_image`:boolean, `cursor_score`:string, `cookie`:string, `proxy`:string

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| feed_type | string | 否 | 推荐类型/Feed type | 0 | 无 | 无 |
| need_filter_image | boolean | 否 | 是否只看图文笔记/Whether to view only image notes | false | 无 | 无 |
| cursor_score | string | 否 | 分页游标/Cursor for pagination | 无 | 无 | 无 |
| cookie | string | 否 | 用户自行提供的已登录的网页Cookie/User provided logged-in web Cookie | 无 | 无 | 无 |
| proxy | string | 否 | 代理，格式：http://用户名:密码@IP:端口/Proxy, format: http://username:password@IP:port | 无 | 无 | 无 |

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

<a id="get-api-u1-v1-xiaohongshu-web-get-note-comment-replies"></a>
### `GET /api/u1/v1/xiaohongshu/web/get_note_comment_replies`

- 摘要：获取笔记评论回复 V1/Get note comment replies V1
- 能力：评论 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_note_comment_replies_api_v1_xiaohongshu_web_get_note_comment_replies_get`

#### 说明

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

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| note_id | query | string | 是 | 笔记ID/Note ID | 无 | 6683b283000000001f0052bf | 无 |
| comment_id | query | string | 是 | 评论ID/Comment ID | 无 | 6683ec5b000000000303b91a | 无 |
| lastCursor | query | string | 否 | 上一页的游标/Last cursor | 无 | 无 | 无 |

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

<a id="get-api-u1-v1-xiaohongshu-web-get-note-comments"></a>
### `GET /api/u1/v1/xiaohongshu/web/get_note_comments`

- 摘要：获取笔记评论 V1/Get note comments V1
- 能力：评论 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_note_comments_api_v1_xiaohongshu_web_get_note_comments_get`

#### 说明

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

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| note_id | query | string | 是 | 笔记ID/Note ID | 无 | 6683b283000000001f0052bf | 无 |
| lastCursor | query | string | 否 | 上一页的游标/Last cursor | 无 | 无 | 无 |

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

<a id="get-api-u1-v1-xiaohongshu-web-get-note-id-and-xsec-token"></a>
### `GET /api/u1/v1/xiaohongshu/web/get_note_id_and_xsec_token`

- 摘要：通过分享链接获取小红书的Note ID 和 xsec_token/Get Xiaohongshu Note ID and xsec_token by share link
- 能力：作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_note_id_and_xsec_token_api_v1_xiaohongshu_web_get_note_id_and_xsec_token_get`

#### 说明

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

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| share_text | query | string | 是 | 分享链接/Share link | 无 | https://xhslink.com/a/EZ4M9TwMA6c3 | 无 |

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

<a id="get-api-u1-v1-xiaohongshu-web-get-note-info-v2"></a>
### `GET /api/u1/v1/xiaohongshu/web/get_note_info_v2`

- 摘要：获取笔记信息 V2/Get note info V2
- 能力：作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_note_info_v2_api_v1_xiaohongshu_web_get_note_info_v2_get`

#### 说明

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

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| note_id | query | string | 否 | 笔记ID/Note ID | 无 | 665f95200000000006005624 | 无 |
| share_text | query | string | 否 | 分享链接/Share link | 无 | https://xhslink.com/a/EZ4M9TwMA6c3 | 无 |

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

<a id="get-api-u1-v1-xiaohongshu-web-get-note-info-v4"></a>
### `GET /api/u1/v1/xiaohongshu/web/get_note_info_v4`

- 摘要：获取笔记信息 V4/Get note info V4
- 能力：作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_note_info_v4_api_v1_xiaohongshu_web_get_note_info_v4_get`

#### 说明

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

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| note_id | query | string | 否 | 笔记ID/Note ID | 无 | 665f95200000000006005624 | 无 |
| share_text | query | string | 否 | 分享链接/Share link | 无 | https://xhslink.com/a/EZ4M9TwMA6c3 | 无 |

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

<a id="post-api-u1-v1-xiaohongshu-web-get-note-info-v5"></a>
### `POST /api/u1/v1/xiaohongshu/web/get_note_info_v5`

- 摘要：获取笔记信息 V5 (自带Cookie)/Get note info V5 (Self-provided Cookie)
- 能力：作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_note_info_v5_api_v1_xiaohongshu_web_get_note_info_v5_post`

#### 说明

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

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`note_id`:string, `xsec_token`:string, `cookie`:string, `proxy`:string

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| note_id | string | 否 | 笔记ID/Note ID | 67855d09000000001703d449 | 无 | 无 |
| xsec_token | string | 否 | X-Sec-Token，可以从搜索接口中获取/X-Sec-Token, can be obtained from the search interface | ABfpRSESmZDRbX-EX7lzEztktMngxPVC9kU-dgQmuQoNo= | 无 | 无 |
| cookie | string | 否 | 用户自行提供的已登录的网页Cookie/User provided logged-in web Cookie | 无 | 无 | 无 |
| proxy | string | 否 | 代理，格式：http://用户名:密码@IP:端口/Proxy, format: http://username:password@IP:port | 无 | 无 | 无 |

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

<a id="get-api-u1-v1-xiaohongshu-web-get-note-info-v7"></a>
### `GET /api/u1/v1/xiaohongshu/web/get_note_info_v7`

- 摘要：获取笔记信息 V7/Get note info V7
- 能力：作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_note_info_v7_api_v1_xiaohongshu_web_get_note_info_v7_get`

#### 说明

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

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| note_id | query | string | 否 | 笔记ID/Note ID | 无 | 665f95200000000006005624 | 无 |
| share_text | query | string | 否 | 分享链接/Share link | 无 | https://xhslink.com/a/EZ4M9TwMA6c3 | 无 |

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

<a id="get-api-u1-v1-xiaohongshu-web-get-product-info"></a>
### `GET /api/u1/v1/xiaohongshu/web/get_product_info`

- 摘要：获取小红书商品信息/Get Xiaohongshu product info
- 能力：电商
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_product_info_api_v1_xiaohongshu_web_get_product_info_get`

#### 说明

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

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| share_text | query | string | 否 | 分享链接/Share link | 无 | 无 | 无 |
| item_id | query | string | 否 | 商品ID/Item ID | 无 | 65fc2e6d6b92310001d24efb | 无 |
| xsec_token | query | string | 否 | X-Sec-Token | 无 | XBC6LTqeaEDeJETMoXo436Eg-74GxFemVnNHeONYobv7k= | 无 |

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

<a id="get-api-u1-v1-xiaohongshu-web-get-user-info"></a>
### `GET /api/u1/v1/xiaohongshu/web/get_user_info`

- 摘要：获取用户信息 V1/Get user info V1
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_user_info_api_v1_xiaohongshu_web_get_user_info_get`

#### 说明

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

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| user_id | query | string | 是 | 用户ID/User ID | 无 | 5f4a10070000000001006fc7 | 无 |

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

<a id="get-api-u1-v1-xiaohongshu-web-get-user-info-v2"></a>
### `GET /api/u1/v1/xiaohongshu/web/get_user_info_v2`

- 摘要：获取用户信息 V2/Get user info V2
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_user_info_v2_api_v1_xiaohongshu_web_get_user_info_v2_get`

#### 说明

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

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| user_id | query | string | 否 | 用户ID/User ID | 无 | 5f4a10070000000001006fc7 | 无 |
| share_text | query | string | 否 | 分享文本或链接/Share text or link | 无 | 示例: @Noo 在小红书收获了15.3万次赞与收藏，查看Ta的主页>> https://xhslink.com/m/7XkrlCXbL38 | 无 |

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

<a id="get-api-u1-v1-xiaohongshu-web-get-user-notes-v2"></a>
### `GET /api/u1/v1/xiaohongshu/web/get_user_notes_v2`

- 摘要：获取用户的笔记 V2/Get user notes V2
- 能力：主页/账号 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_user_notes_api_v1_xiaohongshu_web_get_user_notes_v2_get`

#### 说明

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

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| user_id | query | string | 是 | 用户ID/User ID | 无 | 5f4a10070000000001006fc7 | 无 |
| lastCursor | query | string | 否 | 上一页的游标/Last cursor | 无 | 无 | 无 |

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

<a id="get-api-u1-v1-xiaohongshu-web-get-visitor-cookie"></a>
### `GET /api/u1/v1/xiaohongshu/web/get_visitor_cookie`

- 摘要：获取游客Cookie/Get visitor cookie
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_visitor_cookie_api_v1_xiaohongshu_web_get_visitor_cookie_get`

#### 说明

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

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| proxy | query | string | 否 | 代理/Proxy | 无 | 无 | 无 |

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

<a id="get-api-u1-v1-xiaohongshu-web-search-notes"></a>
### `GET /api/u1/v1/xiaohongshu/web/search_notes`

- 摘要：搜索笔记/Search notes
- 能力：搜索 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`search_notes_api_v1_xiaohongshu_web_search_notes_get`

#### 说明

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

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| keyword | query | string | 是 | 搜索关键词/Keyword | 无 | 美食 | 无 |
| page | query | integer | 否 | 页码/Page | 1 | 1 | 无 |
| sort | query | string | 否 | 排序方式/Sort | general | general | 无 |
| noteType | query | string | 否 | 笔记类型/Note type | _0 | _0 | 无 |
| noteTime | query | string | 否 | 发布时间/Release time | 无 | 无 | 无 |

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

<a id="get-api-u1-v1-xiaohongshu-web-search-notes-v3"></a>
### `GET /api/u1/v1/xiaohongshu/web/search_notes_v3`

- 摘要：搜索笔记 V3/Search notes V3
- 能力：搜索 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`search_notes_v3_api_v1_xiaohongshu_web_search_notes_v3_get`

#### 说明

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

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| keyword | query | string | 是 | 搜索关键词/Keyword | 无 | 美食 | 无 |
| page | query | integer | 否 | 页码/Page | 1 | 1 | 无 |
| sort | query | string | 否 | 排序方式/Sort | general | general | 无 |
| noteType | query | string | 否 | 笔记类型/Note type | _0 | _0 | 无 |
| noteTime | query | string | 否 | 发布时间/Release time | 无 | 无 | 无 |

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

<a id="get-api-u1-v1-xiaohongshu-web-search-users"></a>
### `GET /api/u1/v1/xiaohongshu/web/search_users`

- 摘要：搜索用户/Search users
- 能力：搜索 / 主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`search_users_api_v1_xiaohongshu_web_search_users_get`

#### 说明

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

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| keyword | query | string | 是 | 搜索关键词/Keyword | 无 | 美食 | 无 |
| page | query | integer | 否 | 页码/Page | 1 | 1 | 无 |

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

<a id="post-api-u1-v1-xiaohongshu-web-sign"></a>
### `POST /api/u1/v1/xiaohongshu/web/sign`

- 摘要：小红书Web签名/Xiaohongshu Web sign
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`sign_api_v1_xiaohongshu_web_sign_post`

#### 说明

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

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`path`:string, `data`{...}, `cookie`:string

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| path | string | 否 | 请求接口的路径/Request API path | /api/sns/web/v1/homefeed | 无 | 无 |
| data | object | 否 | 请求API的荷载数据/Payload data of request API | {"cursor_score": "", "num": 35, "refresh_type": 1, "note_index": 35, "unread_be… | 无 | 无 |
| cookie | string | 否 | 请求接口的Cookie/Request API cookie | web_session=030037a04eafd37791e6e4bd05204a8cf2af05;acw_tc=0a00d79f1736309667934… | 无 | 无 |

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
