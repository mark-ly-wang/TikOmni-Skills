# WeChat-Media-Platform-Web-API 完整契约

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 回到路由详情：[`api-tags/wechat-media-platform-web-api.md`](../api-tags/wechat-media-platform-web-api.md)
- 当前契约文件：`api-contracts/wechat-media-platform-web-api.md`
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T04:31:58+00:00`
- 路由数：`10`
- 默认认证：请求头 `Authorization` Bearer
- 使用方式：当需要精确的认证说明、参数描述、默认值、示例或成功响应字段时，再读本文件。
- 标签说明：**(微信公众号Web数据接口/WeChat-Media-Platform-Web-API data endpoints)**

## 路由契约

<a id="get-api-u1-v1-wechat-mp-web-fetch-mp-article-ad"></a>
### `GET /api/u1/v1/wechat_mp/web/fetch_mp_article_ad`

- 摘要：获取微信公众号广告/Get Wechat MP Article Ad
- 能力：作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_mp_article_ad_api_v1_wechat_mp_web_fetch_mp_article_ad_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取微信公众号广告
> ### 参数:
> - url: 文章链接
> ### 返回:
> - 广告
>
> # [English]
> ### Purpose:
> - Get Wechat MP Article Ad
> ### Parameters:
> - url: Article URL
> ### Returns:
> - Ad
>
> # [示例/Example]
> url = "https://mp.weixin.qq.com/s/hrTDuwh0pWyJFYC93kKCrg"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| url | query | string | 是 | 文章链接/Article URL | 无 | https://mp.weixin.qq.com/s/hrTDuwh0pWyJFYC93kKCrg | 无 |

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

<a id="get-api-u1-v1-wechat-mp-web-fetch-mp-article-comment-list"></a>
### `GET /api/u1/v1/wechat_mp/web/fetch_mp_article_comment_list`

- 摘要：获取微信公众号文章评论列表/Get Wechat MP Article Comment List
- 能力：评论 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_mp_article_comment_list_api_v1_wechat_mp_web_fetch_mp_article_comment_list_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取微信公众号文章评论列表
> ### 参数:
> - url: 文章链接
> - comment_id: 评论ID，可以不传获取评论用的id，默认传空字符串
> - buffer: 偏移量，第一次传空字符串，后续传上次返回的buffer值
> ### 返回:
> - 评论列表
>
> # [English]
> ### Purpose:
> - Get Wechat MP Article Comment List
> ### Parameters:
> - url: Article URL
> - comment_id: Comment ID, can be empty to get the comment ID, default is an empty string
> - buffer: Offset, first time is an empty string, then pass the buffer value returned last time
> ### Returns:
> - Comment List
>
> # [示例/Example]
> url = "https://mp.weixin.qq.com/s/Iv-xRzL7WzbL0dUUIgi3Nw"
> comment_id = ""
> buffer = "0"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| url | query | string | 是 | 文章链接/Article URL | 无 | https://mp.weixin.qq.com/s/Iv-xRzL7WzbL0dUUIgi3Nw | 无 |
| comment_id | query | string | 否 | 评论ID/Comment ID | 无 | 无 | 无 |
| buffer | query | string | 否 | 偏移量/Offset | 无 | 无 | 无 |

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

<a id="get-api-u1-v1-wechat-mp-web-fetch-mp-article-comment-reply-list"></a>
### `GET /api/u1/v1/wechat_mp/web/fetch_mp_article_comment_reply_list`

- 摘要：获取微信公众号文章评论回复列表/Get Wechat MP Article Comment Reply List
- 能力：评论 / 评论回复 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_mp_article_comment_reply_list_api_v1_wechat_mp_web_fetch_mp_article_comment_reply_list_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取微信公众号文章评论回复列表
> ### 参数:
> - url: 文章链接
> - comment_id: 评论ID
> - content_id: 内容ID
> - offset: 偏移量
> ### 返回:
> - 评论回复列表
>
> # [English]
> ### Purpose:
> - Get Wechat MP Article Comment Reply List
> ### Parameters:
> - url: Article URL
> - comment_id: Comment ID
> - content_id: Content ID
> - offset: Offset
> ### Returns:
> - Comment Reply List
>
> # [示例/Example]
> url = "https://mp.weixin.qq.com/s/RCjkQlkRS4oKZ0GAT9slzA"
> comment_id = "3601466901697855492"
> content_id = "6387234930341970671"
> offset = "0"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| url | query | string | 否 | 文章链接/Article URL | https://mp.weixin.qq.com/s/Ko5V9jw9kwL8TO6Q7J3UqQ | 无 | 无 |
| comment_id | query | string | 是 | 评论ID/Comment ID | 无 | 3601466901697855492 | 无 |
| content_id | query | string | 是 | 内容ID/Content ID | 无 | 6387234930341970671 | 无 |
| offset | query | string | 否 | 偏移量/Offset | 0 | 无 | 无 |

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

<a id="get-api-u1-v1-wechat-mp-web-fetch-mp-article-detail-html"></a>
### `GET /api/u1/v1/wechat_mp/web/fetch_mp_article_detail_html`

- 摘要：获取微信公众号文章详情的HTML/Get Wechat MP Article Detail HTML
- 能力：作品详情 / 详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_mp_article_detail_html_api_v1_wechat_mp_web_fetch_mp_article_detail_html_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取微信公众号文章详情的HTML，如果你需要获取详细的JSON格式数据，请使用`/api/v1/wechat_mp/web/fetch_mp_article_detail_json`接口
> - 此接口收费贵，价格：0.01$/次
> ### 参数:
> - url: 文章链接
> ### 返回:
> - 文章详情的HTML
>
> # [English]
> ### Purpose:
> - Get WeChat MP Article Detail, if you need detailed JSON format data, please use the `/api/v1/wechat_mp/web/fetch_mp_article_detail_json` interface
> - This interface is more expensive, price: 0.01$/time
> ### Parameters:
> - url: Article URL
> ### Returns:
> - Article Detail HTML
>
> # [示例/Example]
> url = "https://mp.weixin.qq.com/s/TSNQKkRpN1qbKsT7BvzqIw"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| url | query | string | 是 | 文章链接/Article URL | 无 | https://mp.weixin.qq.com/s/TSNQKkRpN1qbKsT7BvzqIw | 无 |

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

<a id="get-api-u1-v1-wechat-mp-web-fetch-mp-article-detail-json"></a>
### `GET /api/u1/v1/wechat_mp/web/fetch_mp_article_detail_json`

- 摘要：获取微信公众号文章详情的JSON/Get Wechat MP Article Detail JSON
- 能力：作品详情 / 详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_mp_article_detail_json_api_v1_wechat_mp_web_fetch_mp_article_detail_json_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取微信公众号文章详情的JSON格式数据
> - 此接口收费便宜，如果你需要获取详细的HTML格式数据，请使用`/api/v1/wechat_mp/web/fetch_mp_article_detail_html`接口，但是此接口收费更贵。
> - 价格：0.001$/次
> ### 参数:
> - url: 文章链接
> ### 返回:
> - 文章详情的HTML
>
> # [English]
> ### Purpose:
> - Get WeChat MP Article Detail in JSON format
> - This interface is cheaper, if you need detailed HTML format data, please use the `/api/v1/wechat_mp/web/fetch_mp_article_detail_html` interface, but this interface is more expensive.
> - Price: 0.001$/time
> ### Parameters:
> - url: Article URL
> ### Returns:
> - Article Detail HTML
>
> # [示例/Example]
> url = "https://mp.weixin.qq.com/s/TSNQKkRpN1qbKsT7BvzqIw"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| url | query | string | 是 | 文章链接/Article URL | 无 | https://mp.weixin.qq.com/s/TSNQKkRpN1qbKsT7BvzqIw | 无 |

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

<a id="get-api-u1-v1-wechat-mp-web-fetch-mp-article-list"></a>
### `GET /api/u1/v1/wechat_mp/web/fetch_mp_article_list`

- 摘要：获取微信公众号文章列表/Get Wechat MP Article List
- 能力：作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_mp_article_list_api_v1_wechat_mp_web_fetch_mp_article_list_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取微信公众号文章列表
> ### 参数:
> - ghid: 公众号ID
> - offset: 偏移量
> ### 返回:
> - 文章列表
>
> # [English]
> ### Purpose:
> - Get Wechat MP Article List
> ### Parameters:
> - ghid: MP ID
> - offset: Offset
> ### Returns:
> - Article List
>
> # [示例/Example]
> ghid = "gh_a3d35d4c9d3f"
> offset = ""

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ghid | query | string | 是 | 公众号ID/MP ID | 无 | gh_a3d35d4c9d3f | 无 |
| offset | query | string | 否 | 偏移量/Offset | 无 | 无 | 无 |

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

<a id="get-api-u1-v1-wechat-mp-web-fetch-mp-article-read-count"></a>
### `GET /api/u1/v1/wechat_mp/web/fetch_mp_article_read_count`

- 摘要：获取微信公众号文章阅读量/Get Wechat MP Article Read Count
- 能力：作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_mp_article_read_count_api_v1_wechat_mp_web_fetch_mp_article_read_count_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取微信公众号文章阅读量
> ### 参数:
> - url: 文章链接
> - comment_id: 评论ID
> ### 返回:
> - 阅读量
>
> # [English]
> ### Purpose:
> - Get Wechat MP Article Read Count
> ### Parameters:
> - url: Article URL
> - comment_id: Comment ID
> ### Returns:
> - Read Count
>
> # [示例/Example]
> url = "https://mp.weixin.qq.com/s/hrTDuwh0pWyJFYC93kKCrg"
> comment_id = "3363399664632332289"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| url | query | string | 是 | 文章链接/Article URL | 无 | https://mp.weixin.qq.com/s/hrTDuwh0pWyJFYC93kKCrg | 无 |
| comment_id | query | string | 是 | 评论ID/Comment ID | 无 | 无 | 无 |

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

<a id="get-api-u1-v1-wechat-mp-web-fetch-mp-article-url"></a>
### `GET /api/u1/v1/wechat_mp/web/fetch_mp_article_url`

- 摘要：获取微信公众号文章永久链接/Get Wechat MP Article URL
- 能力：作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_mp_article_url_api_v1_wechat_mp_web_fetch_mp_article_url_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取微信公众号文章永久链接
> ### 参数:
> - sogou_url: 搜狗链接
> ### 返回:
> - 永久链接
>
> # [English]
> ### Purpose:
> - Get Wechat MP Article URL
> ### Parameters:
> - sogou_url: Sogou URL
> ### Returns:
> - Article URL
>
> # [示例/Example]
> sogou_url = "https://weixin.sogou.com/link?url=dn9a_-gY295K0Rci_xozVXfdMkSQTLW6cwJThYulHEtVjXrGTiVgS5mzcw64XRlRaPIdMgILsPEBI9djq3byAlqXa8Fplpd9bV3r44ewJj5IFttt-prmTSHShu8JtNlpDYR_z_1xvD2J_XrGTUriRYOOY2mt9pZSIUQEepUVTybxAOW4P5fEPd23R0CgK6W3KEODtIkcv1U5w5VkZ8a7_lyyAqreiCgr1YH9mz_7mzFDl6rX6ZnkVYNsUHV_OmaXBUCqpZ1Pa6YO8fIRwtipOg..&type=2&query=deepseek&token=C2E90D2050EB6EA5C2C4EDB1541D855FC322013E67C5DC5A&k=4&h=k"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| sogou_url | query | string | 是 | 搜狗链接/Sogou URL | 无 | https://weixin.sogou.com/link?url=dn9a_-gY295K0Rci_xozVXfdMkSQTLW6cwJThYulHEtVj… | 无 |

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

<a id="get-api-u1-v1-wechat-mp-web-fetch-mp-article-url-conversion"></a>
### `GET /api/u1/v1/wechat_mp/web/fetch_mp_article_url_conversion`

- 摘要：获取微信公众号长链接转短链接/Get Wechat MP Long URL to Short URL
- 能力：作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_mp_article_url_conversion_api_v1_wechat_mp_web_fetch_mp_article_url_conversion_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取微信公众号长链接转短链接
> ### 参数:
> - url: 文章链接
> ### 返回:
> - 短链接
>
> # [English]
> ### Purpose:
> - Get Wechat MP Long URL to Short URL
> ### Parameters:
> - url: Article URL
> ### Returns:
> - Short URL
>
> # [示例/Example]
> url = "http://mp.weixin.qq.com/s?__biz=MzIyMDQzMTM4Mg==&mid=2247504868&idx=1&sn=37ee48875df1be54cb766783177ce61d"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| url | query | string | 是 | 文章链接/Article URL | 无 | http://mp.weixin.qq.com/s?__biz=MzIyMDQzMTM4Mg==&mid=2247504868&idx=1&sn=37ee48… | 无 |

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

<a id="get-api-u1-v1-wechat-mp-web-fetch-mp-related-articles"></a>
### `GET /api/u1/v1/wechat_mp/web/fetch_mp_related_articles`

- 摘要：获取微信公众号关联文章/Get Wechat MP Related Articles
- 能力：作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_mp_related_articles_api_v1_wechat_mp_web_fetch_mp_related_articles_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取微信公众号关联文章
> ### 参数:
> - url: 文章链接
> ### 返回:
> - 关联文章
>
> # [English]
> ### Purpose:
> - Get Wechat MP Related Articles
> ### Parameters:
> - url: Article URL
> ### Returns:
> - Related Articles
>
> # [示例/Example]
> url = "https://mp.weixin.qq.com/s/Ko5V9jw9kwL8TO6Q7J3UqQ"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| url | query | string | 是 | 文章链接/Article URL | 无 | https://mp.weixin.qq.com/s/Ko5V9jw9kwL8TO6Q7J3UqQ | 无 |

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
