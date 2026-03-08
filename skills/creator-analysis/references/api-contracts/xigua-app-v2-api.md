# Xigua-App-V2-API Full Contract

- Back to index: [`api-capability-index.md`](../api-capability-index.md)
- Back to route summary: [`api-tags/xigua-app-v2-api.md`](../api-tags/xigua-app-v2-api.md)
- Current contract file: `api-contracts/xigua-app-v2-api.md`
- Source: `https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- Fetched at: `2026-03-08T06:54:04+00:00`
- Route count: `7`
- Default auth: Header `Authorization` Bearer
- Read this file only when you need precise auth notes, parameter descriptions, defaults, examples, or success-response fields.
- Tag description: **(西瓜视频App V2数据接口/Xigua-App-V2-API data endpoints)**

## Route Contracts

<a id="get-api-u1-v1-xigua-app-v2-fetch-one-video"></a>
### `GET /api/u1/v1/xigua/app/v2/fetch_one_video`

- Summary: 获取单个作品数据/Get single video data
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_one_video_api_v1_xigua_app_v2_fetch_one_video_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取单个作品数据（信息较少，不包含标题等信息，但是包含相关视频的信息）
> ### 参数:
> - item_id: 作品id
> ### 返回:
> - 作品数据，其中包含视频链接的Base64编码播放地址，需要前端解码后使用，或者使用 /fetch_one_video_play_url 获取播放链接。
>
> # [English]
> ### Purpose:
> - Get single video data (less information, does not include title and other information, but includes information about related videos)
> ### Parameters:
> - item_id: Video id
> ### Return:
> - Video data, which contains the Base64 encoded playback address of the video link, which needs to be decoded and used by the front end, or use /fetch_one_video_play_url to get the playback link.
>
> # [示例/Example]
> item_id: "7354954305222377999"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| item_id | query | string | Yes | 作品id/Video id | None | 7354954305222377999 | None |

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

<a id="get-api-u1-v1-xigua-app-v2-fetch-one-video-play-url"></a>
### `GET /api/u1/v1/xigua/app/v2/fetch_one_video_play_url`

- Summary: 获取单个作品的播放链接/Get single video play URL
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_one_video_play_url_api_v1_xigua_app_v2_fetch_one_video_play_url_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取单个作品的播放链接，此接口返回的是已经解码后的播放链接，可以直接使用。
> ### 参数:
> - item_id: 作品id
> ### 返回:
> - 作品的播放链接的明文链接。
>
> # [English]
> ### Purpose:
> - Get single video play URL, the interface returns the decoded play URL, which can be used directly.
> ### Parameters:
> - item_id: Video id
> ### Return:
> - Play URL of the video, plaintext link.
>
> # [示例/Example]
> item_id: "7354954305222377999"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| item_id | query | string | Yes | 作品id/Video id | None | 7354954305222377999 | None |

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

<a id="get-api-u1-v1-xigua-app-v2-fetch-one-video-v2"></a>
### `GET /api/u1/v1/xigua/app/v2/fetch_one_video_v2`

- Summary: 获取单个作品数据 V2/Get single video data V2
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_one_video_v2_api_v1_xigua_app_v2_fetch_one_video_v2_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取单个作品数据（信息全面，包含标题等信息，但是不包含相关视频推荐信息）
> ### 参数:
> - item_id: 作品id
> ### 返回:
> - 作品数据，其中包含视频链接的Base64编码播放地址，需要前端解码后使用，或者使用 /fetch_one_video_play_url 获取播放链接。
>
> # [English]
> ### Purpose:
> - Get single video data (more comprehensive information, including title and other information, but not including information about related video recommendations)
> ### Parameters:
> - item_id: Video id
> ### Return:
> - Video data, which contains the Base64 encoded playback address of the video link, which needs to be decoded and used by the front end, or use /fetch_one_video_play_url to get the playback link.
>
> # [示例/Example]
> item_id: "7354954305222377999"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| item_id | query | string | Yes | 作品id/Video id | None | 7354954305222377999 | None |

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

<a id="get-api-u1-v1-xigua-app-v2-fetch-user-info"></a>
### `GET /api/u1/v1/xigua/app/v2/fetch_user_info`

- Summary: 个人信息/Personal information
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_info_api_v1_xigua_app_v2_fetch_user_info_get`

#### Notes

> # [中文]
> ### 用途:
> - 个人信息
> ### 参数:
> - user_id: 用户id
> ### 返回:
> - 个人信息
>
> # [English]
> ### Purpose:
> - Personal information
> ### Parameters:
> - user_id: User id
> ### Return:
> - Personal information
>
> # [示例/Example]
> user_id: "52712347586"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| user_id | query | string | Yes | 用户id/User id | None | 52712347586 | None |

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

<a id="get-api-u1-v1-xigua-app-v2-fetch-user-post-list"></a>
### `GET /api/u1/v1/xigua/app/v2/fetch_user_post_list`

- Summary: 获取个人作品列表/Get user post list
- Capabilities: profiles / accounts / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_post_list_api_v1_xigua_app_v2_fetch_user_post_list_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取个人作品列表
> ### 参数:
> - user_id: 用户id
> - max_behot_time: 最大行为时间，默认空，第一次请求传空，后续请求传上一次请求返回数据中的JSON中的值。
> - max_behot_time的值可以是JSON路径为：$.data.data.[-1].behot_time
> - 也就是data中的最后一个元素的cursor值
> ### 返回:
> - 作品列表
>
> # [English]
> ### Purpose:
> - Get user post list
> ### Parameters:
> - user_id: User id
> - max_behot_time: Maximum behavior time, default empty, pass empty for the first request, pass the max_behot_time returned by the previous request for subsequent requests
> - The value of max_behot_time can be the JSON path: $.data.data.[-1].behot_time
> - That is, the cursor value of the last element in data
> ### Return:
> - Post list
>
> # [示例/Example]
> user_id = "1922379661976311"
> max_behot_time = ""

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| user_id | query | string | Yes | 用户id/User id | None | 1922379661976311 | None |
| max_behot_time | query | string | No | 最大行为时间/Maximum behavior time | None | None | None |

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

<a id="get-api-u1-v1-xigua-app-v2-fetch-video-comment-list"></a>
### `GET /api/u1/v1/xigua/app/v2/fetch_video_comment_list`

- Summary: 视频评论列表/Video comment list
- Capabilities: comments / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_video_comment_list_api_v1_xigua_app_v2_fetch_video_comment_list_get`

#### Notes

> # [中文]
> ### 用途:
> - 视频评论列表
> ### 参数:
> - item_id: 作品id
> - offset: 偏移量，第一次请求传0，后续请求传上一次请求返回的offset
> - count: 数量，默认20，建议保持默认。
> ### 返回:
> - 评论列表
>
> # [English]
> ### Purpose:
> - Video comment list
> ### Parameters:
> - item_id: Video id
> - offset: Offset, pass 0 for the first request, pass the offset returned by the previous request for subsequent requests
> - count: Quantity, default 20, it is recommended to keep the default.
> ### Return:
> - Comment list
>
> # [示例/Example]
> item_id: "7354954305222377999"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| item_id | query | string | Yes | 作品id/Video id | None | 7354954305222377999 | None |
| offset | query | integer | No | 偏移量/Offset | 0 | None | None |
| count | query | integer | No | 数量/Count | 20 | None | None |

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

<a id="get-api-u1-v1-xigua-app-v2-search-video"></a>
### `GET /api/u1/v1/xigua/app/v2/search_video`

- Summary: 搜索视频/Search video
- Capabilities: search / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `search_video_api_v1_xigua_app_v2_search_video_get`

#### Notes

> # [中文]
> ### 用途:
> - 搜索视频
> ### 参数:
> - keyword: 关键词
> - offset: 偏移量，第一次请求传0，后续请求传上一次请求返回的offset
> - order_type: 排序方式，为空时按照默认排序，以下为可选排序方式。
>     - 最新: publish_time
>     - 最热: play_count
> - min_duration: 最小时长，默认空，单位秒。
> - max_duration: 最大时长，默认空，单位秒。
> ### 返回:
> - 视频列表
>
> # [English]
> ### Purpose:
> - Search video
> ### Parameters:
> - keyword: Keyword
> - offset: Offset, pass 0 for the first request, pass the offset returned by the previous request for subsequent requests
> - order_type: Order type, empty for default sorting, the following are optional sorting methods.
>     - Newest: publish_time
>     - Hottest: play_count
> - min_duration: Minimum duration, default empty, in seconds.
> - max_duration: Maximum duration, default empty, in seconds.
> ### Return:
> - Video list
>
> # [示例/Example]
> > 搜索关键字为“抖音”的视频，按照播放量排序，时长1-180秒(1-3分钟)
> > Search for videos with the keyword "抖音", sorted by play count, duration 1-180 seconds (1-3 minutes)
> keyword: "抖音"
> order_type: "play_count"
> min_duration: 1
> max_duration: 180

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| keyword | query | string | Yes | 关键词/Keyword | None | 抖音 | None |
| offset | query | integer | No | 偏移量/Offset | 0 | None | None |
| order_type | query | string | No | 排序方式/Order type | None | None | None |
| min_duration | query | integer | No | 最小时长/Minimum duration | None | None | None |
| max_duration | query | integer | No | 最大时长/Maximum duration | None | None | None |

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
