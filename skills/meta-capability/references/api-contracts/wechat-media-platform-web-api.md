# WeChat-Media-Platform-Web-API Full Contract

- Back to index: [`api-capability-index.md`](../api-capability-index.md)
- Back to route summary: [`api-tags/wechat-media-platform-web-api.md`](../api-tags/wechat-media-platform-web-api.md)
- Current contract file: `api-contracts/wechat-media-platform-web-api.md`
- Source: `https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- Fetched at: `2026-03-08T06:54:04+00:00`
- Route count: `10`
- Default auth: Header `Authorization` Bearer
- Read this file only when you need precise auth notes, parameter descriptions, defaults, examples, or success-response fields.
- Tag description: **(微信公众号Web数据接口/WeChat-Media-Platform-Web-API data endpoints)**

## Route Contracts

<a id="get-api-u1-v1-wechat-mp-web-fetch-mp-article-ad"></a>
### `GET /api/u1/v1/wechat_mp/web/fetch_mp_article_ad`

- Summary: 获取微信公众号广告/Get Wechat MP Article Ad
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_mp_article_ad_api_v1_wechat_mp_web_fetch_mp_article_ad_get`

#### Notes

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

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| url | query | string | Yes | 文章链接/Article URL | None | https://mp.weixin.qq.com/s/hrTDuwh0pWyJFYC93kKCrg | None |

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

<a id="get-api-u1-v1-wechat-mp-web-fetch-mp-article-comment-list"></a>
### `GET /api/u1/v1/wechat_mp/web/fetch_mp_article_comment_list`

- Summary: 获取微信公众号文章评论列表/Get Wechat MP Article Comment List
- Capabilities: comments / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_mp_article_comment_list_api_v1_wechat_mp_web_fetch_mp_article_comment_list_get`

#### Notes

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

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| url | query | string | Yes | 文章链接/Article URL | None | https://mp.weixin.qq.com/s/Iv-xRzL7WzbL0dUUIgi3Nw | None |
| comment_id | query | string | No | 评论ID/Comment ID | None | None | None |
| buffer | query | string | No | 偏移量/Offset | None | None | None |

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

<a id="get-api-u1-v1-wechat-mp-web-fetch-mp-article-comment-reply-list"></a>
### `GET /api/u1/v1/wechat_mp/web/fetch_mp_article_comment_reply_list`

- Summary: 获取微信公众号文章评论回复列表/Get Wechat MP Article Comment Reply List
- Capabilities: comments / comment replies / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_mp_article_comment_reply_list_api_v1_wechat_mp_web_fetch_mp_article_comment_reply_list_get`

#### Notes

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

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| url | query | string | No | 文章链接/Article URL | https://mp.weixin.qq.com/s/Ko5V9jw9kwL8TO6Q7J3UqQ | None | None |
| comment_id | query | string | Yes | 评论ID/Comment ID | None | 3601466901697855492 | None |
| content_id | query | string | Yes | 内容ID/Content ID | None | 6387234930341970671 | None |
| offset | query | string | No | 偏移量/Offset | 0 | None | None |

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

<a id="get-api-u1-v1-wechat-mp-web-fetch-mp-article-detail-html"></a>
### `GET /api/u1/v1/wechat_mp/web/fetch_mp_article_detail_html`

- Summary: 获取微信公众号文章详情的HTML/Get Wechat MP Article Detail HTML
- Capabilities: content details / details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_mp_article_detail_html_api_v1_wechat_mp_web_fetch_mp_article_detail_html_get`

#### Notes

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

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| url | query | string | Yes | 文章链接/Article URL | None | https://mp.weixin.qq.com/s/TSNQKkRpN1qbKsT7BvzqIw | None |

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

<a id="get-api-u1-v1-wechat-mp-web-fetch-mp-article-detail-json"></a>
### `GET /api/u1/v1/wechat_mp/web/fetch_mp_article_detail_json`

- Summary: 获取微信公众号文章详情的JSON/Get Wechat MP Article Detail JSON
- Capabilities: content details / details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_mp_article_detail_json_api_v1_wechat_mp_web_fetch_mp_article_detail_json_get`

#### Notes

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

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| url | query | string | Yes | 文章链接/Article URL | None | https://mp.weixin.qq.com/s/TSNQKkRpN1qbKsT7BvzqIw | None |

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

<a id="get-api-u1-v1-wechat-mp-web-fetch-mp-article-list"></a>
### `GET /api/u1/v1/wechat_mp/web/fetch_mp_article_list`

- Summary: 获取微信公众号文章列表/Get Wechat MP Article List
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_mp_article_list_api_v1_wechat_mp_web_fetch_mp_article_list_get`

#### Notes

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

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ghid | query | string | Yes | 公众号ID/MP ID | None | gh_a3d35d4c9d3f | None |
| offset | query | string | No | 偏移量/Offset | None | None | None |

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

<a id="get-api-u1-v1-wechat-mp-web-fetch-mp-article-read-count"></a>
### `GET /api/u1/v1/wechat_mp/web/fetch_mp_article_read_count`

- Summary: 获取微信公众号文章阅读量/Get Wechat MP Article Read Count
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_mp_article_read_count_api_v1_wechat_mp_web_fetch_mp_article_read_count_get`

#### Notes

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

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| url | query | string | Yes | 文章链接/Article URL | None | https://mp.weixin.qq.com/s/hrTDuwh0pWyJFYC93kKCrg | None |
| comment_id | query | string | Yes | 评论ID/Comment ID | None | None | None |

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

<a id="get-api-u1-v1-wechat-mp-web-fetch-mp-article-url"></a>
### `GET /api/u1/v1/wechat_mp/web/fetch_mp_article_url`

- Summary: 获取微信公众号文章永久链接/Get Wechat MP Article URL
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_mp_article_url_api_v1_wechat_mp_web_fetch_mp_article_url_get`

#### Notes

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

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| sogou_url | query | string | Yes | 搜狗链接/Sogou URL | None | https://weixin.sogou.com/link?url=dn9a_-gY295K0Rci_xozVXfdMkSQTLW6cwJThYulHEtVj… | None |

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

<a id="get-api-u1-v1-wechat-mp-web-fetch-mp-article-url-conversion"></a>
### `GET /api/u1/v1/wechat_mp/web/fetch_mp_article_url_conversion`

- Summary: 获取微信公众号长链接转短链接/Get Wechat MP Long URL to Short URL
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_mp_article_url_conversion_api_v1_wechat_mp_web_fetch_mp_article_url_conversion_get`

#### Notes

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

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| url | query | string | Yes | 文章链接/Article URL | None | http://mp.weixin.qq.com/s?__biz=MzIyMDQzMTM4Mg==&mid=2247504868&idx=1&sn=37ee48… | None |

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

<a id="get-api-u1-v1-wechat-mp-web-fetch-mp-related-articles"></a>
### `GET /api/u1/v1/wechat_mp/web/fetch_mp_related_articles`

- Summary: 获取微信公众号关联文章/Get Wechat MP Related Articles
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_mp_related_articles_api_v1_wechat_mp_web_fetch_mp_related_articles_get`

#### Notes

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

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| url | query | string | Yes | 文章链接/Article URL | None | https://mp.weixin.qq.com/s/Ko5V9jw9kwL8TO6Q7J3UqQ | None |

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
