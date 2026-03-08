# Demo-API Full Contract

- Back to index: [`api-capability-index.md`](../api-capability-index.md)
- Back to route summary: [`api-tags/demo-api.md`](../api-tags/demo-api.md)
- Current contract file: `api-contracts/demo-api.md`
- Source: `https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- Fetched at: `2026-03-08T06:54:04+00:00`
- Route count: `9`
- Default auth: Header `Authorization` Bearer
- Read this file only when you need precise auth notes, parameter descriptions, defaults, examples, or success-response fields.
- Tag description: **(TikHub API示例项目/Demo Project)**

## Route Contracts

<a id="get-api-u1-v1-demo-demo-cache-status"></a>
### `GET /api/u1/v1/demo/demo/cache_status`

- Summary: 查看Demo缓存状态/View Demo Cache Status
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `view_cache_status_api_v1_demo_demo_cache_status_get`

#### Notes

> # 查看所有Demo接口的缓存状态
>
> ## [中文]
> ### 用途:
> - 查看当前缓存的Demo数据
> - 了解缓存过期时间
>
> ## [English]
> ### Purpose:
> - View current cached Demo data
> - Check cache expiration times

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

<a id="get-api-u1-v1-demo-douyin-app-fetch-one-video"></a>
### `GET /api/u1/v1/demo/douyin/app/fetch_one_video`

- Summary: 【Demo】抖音APP获取固定作品数据（1小时缓存）/[Demo] Fetch Douyin APP Fixed Video Data with Cache
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `douyin_app_fetch_one_video_api_v1_demo_douyin_app_fetch_one_video_get`

#### Notes

> # 🎯 **这是一个DEMO接口**
>
> ## [中文]
> ### ⚠️ 重要说明:
> - **这是一个演示(Demo)接口，仅用于测试和展示功能**
> - **不允许修改aweme_id参数，始终返回固定作品的数据**
> - **数据缓存1小时**
>
> ### 用途:
> - 用于测试API连接和数据格式
> - 了解返回数据结构
> - 开发阶段的功能验证
>
> ### 特性:
> - ✅ 1小时数据缓存
> - ✅ 固定作品ID: 7534641277405531446
> - ✅ 固定作品的对应链接: https://www.douyin.com/video/7534641277405531446
> - ✅ 免费使用，无需计费
>
> ### 返回:
> - 固定作品的缓存数据
>
> ---
>
> ## [English]
> ### ⚠️ Important Notice:
> - **This is a DEMO endpoint for testing and demonstration only**
> - **The aweme_id parameter cannot be modified, always returns data for a fixed video**
> - **Data is cached for 1 hour**
>
> ### Purpose:
> - Test API connection and data format
> - Understand return data structure
> - Feature validation during development
>
> ### Features:
> - ✅ 1-hour data caching
> - ✅ Fixed video ID: 7534641277405531446
> - ✅ Fixed video link: https://www.douyin.com/video/7534641277405531446
> - ✅ Free to use, no billing
>
> ### Return:
> - Cached data for the fixed video
>
> ---
>
> # [示例/Example]
> ```
> # 无需参数，始终返回固定作品数据
> # No parameters needed, always returns fixed video data
> GET /api/v1/douyin/app/fetch_one_video
> ```

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

<a id="get-api-u1-v1-demo-douyin-web-fetch-one-video"></a>
### `GET /api/u1/v1/demo/douyin/web/fetch_one_video`

- Summary: 【Demo】抖音Web获取固定作品数据（1小时缓存）/[Demo] Fetch Douyin Web Fixed Video Data with Cache
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `douyin_web_fetchone_video_demo_api_v1_demo_douyin_web_fetch_one_video_get`

#### Notes

> # 🎯 **这是一个DEMO接口**
>
> ## [中文]
> ### ⚠️ 重要说明:
> - **这是一个演示(Demo)接口，仅用于测试和展示功能**
> - **不允许修改aweme_id参数，始终返回固定作品的数据**
> - **数据缓存1小时**
>
> ### 用途:
> - 用于测试API连接和数据格式
> - 了解返回数据结构
> - 开发阶段的功能验证
>
> ### 特性:
> - ✅ 1小时数据缓存
> - ✅ 固定作品ID: 7534641277405531446
> - ✅ 固定作品的对应链接: https://www.douyin.com/video/7534641277405531446
> - ✅ 免费使用，无需计费
>
> ### 返回:
> - 固定作品的缓存数据
>
> ---
>
> ## [English]
> ### ⚠️ Important Notice:
> - **This is a DEMO endpoint for testing and demonstration only**
> - **The aweme_id parameter cannot be modified, always returns data for a fixed video**
> - **Data is cached for 1 hour**
>
> ### Purpose:
> - Test API connection and data format
> - Understand return data structure
> - Feature validation during development
>
> ### Features:
> - ✅ 1-hour data caching
> - ✅ Fixed video ID: 7534641277405531446
> - ✅ Fixed video link: https://www.douyin.com/video/7534641277405531446
> - ✅ Free to use, no billing
>
> ### Return:
> - Cached data for the fixed video
>
> ---
>
> # [示例/Example]
> ```
> # 无需参数，始终返回固定作品数据
> # No parameters needed, always returns fixed video data
> GET /api/v1/douyin/web/fetch_one_video
> ```

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

<a id="get-api-u1-v1-demo-douyin-search-app-general-search"></a>
### `GET /api/u1/v1/demo/douyin_search/app/general_search`

- Summary: 【Demo】抖音搜索综合搜索（1小时缓存）/[Demo] Douyin General Search with Cache
- Capabilities: search
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `douyin_search_general_demo_api_v1_demo_douyin_search_app_general_search_get`

#### Notes

> # 🎯 **这是一个DEMO接口**
>
> ## [中文]
> ### ⚠️ 重要说明:
> - **这是一个演示接口，返回固定关键词的搜索结果**
> - **搜索关键词固定为"美食"**
> - **数据缓存1小时**
>
> ### 特性:
> - ✅ 1小时数据缓存
> - ✅ 固定搜索关键词: 美食
> - ✅ 免费使用
>
> ## [English]
> ### ⚠️ Important Notice:
> - **Demo endpoint returning fixed keyword search results**
> - **Search keyword fixed as "美食" (Food)**
> - **Data cached for 1 hour**
>
> ### Features:
> - ✅ 1-hour data caching
> - ✅ Fixed search keyword: 美食
> - ✅ Free to use
>
> ---
>
> # [示例/Example]
> ```
> # 无需参数，始终返回固定关键词搜索结果
> # No parameters needed, always returns fixed keyword search results
> GET /api/v1/douyin_search/app/general_search
> ```

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

<a id="get-api-u1-v1-demo-instagram-web-fetch-user-info"></a>
### `GET /api/u1/v1/demo/instagram/web/fetch_user_info`

- Summary: 【Demo】Instagram获取固定用户信息（1小时缓存）/[Demo] Instagram Fixed User Profile with Cache
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `instagram_web_fetch_user_info_api_v1_demo_instagram_web_fetch_user_info_get`

#### Notes

> # 🎯 **这是一个DEMO接口**
>
> ## [中文]
> ### ⚠️ 重要说明:
> - **返回固定Instagram用户信息**
> - **数据缓存1小时**
>
> ### 特性:
> - ✅ 1小时数据缓存
> - ✅ 固定用户: Instagram
> - ✅ 免费使用
>
> ## [English]
> ### ⚠️ Important Notice:
> - **Returns fixed Instagram user profile**
> - **Data cached for 1 hour**
>
> ### Features:
> - ✅ 1-hour data caching
> - ✅ Fixed user: Instagram
> - ✅ Free to use
>
> ---
>
> # [示例/Example]
> ```
> # 无需参数，始终返回固定用户数据
> # No parameters needed, always returns fixed user data
> GET /api/v1/instagram/web/fetch_user_info
> ```

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

<a id="get-api-u1-v1-demo-kuaishou-web-fetch-one-video"></a>
### `GET /api/u1/v1/demo/kuaishou/web/fetch_one_video`

- Summary: 【Demo】快手获取固定视频信息（1小时缓存）/[Demo] Kuaishou Fixed Video with Cache
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `kuaishou_web_fetch_one_video_api_v1_demo_kuaishou_web_fetch_one_video_get`

#### Notes

> # 🎯 **这是一个DEMO接口**
>
> ## [中文]
> ### ⚠️ 重要说明:
> - **返回固定快手视频信息**
> - **数据缓存1小时**
>
> ### 特性:
> - ✅ 1小时数据缓存
> - ✅ 固定视频数据，参数：https://www.kuaishou.com/short-video/3x73wr9tdt7nxqy
> - ✅ 免费使用
>
> ## [English]
> ### ⚠️ Important Notice:
> - **Returns fixed Kuaishou video info**
> - **Data cached for 1 hour**
>
> ### Features:
> - ✅ 1-hour data caching
> - ✅ Fixed video data, parameter: https://www.kuaishou.com/short-video/3x73wr9tdt7nxqy
> - ✅ Free to use
>
> ---
>
> # [示例/Example]
> ```
> # 无需参数，始终返回固定视频数据
> # No parameters needed, always returns fixed video data
> GET /api/v1/kuaishou/web/fetch_one_video
> ```

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

<a id="get-api-u1-v1-demo-tiktok-app-fetch-one-video"></a>
### `GET /api/u1/v1/demo/tiktok/app/fetch_one_video`

- Summary: 【Demo】TikTok APP获取固定视频详情（1小时缓存）/[Demo] TikTok APP Fixed Video Detail with Cache
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `tiktok_app_fetch_one_video_api_v1_demo_tiktok_app_fetch_one_video_get`

#### Notes

> # 🎯 **这是一个DEMO接口**
>
> ## [中文]
> ### ⚠️ 重要说明:
> - **返回固定TikTok视频详情**
> - **数据缓存1小时**
>
> ### 特性:
> - ✅ 1小时数据缓存
> - ✅ 固定视频详情，参数: 7319033421676653855
> - ✅ 免费使用
>
> ## [English]
> ### ⚠️ Important Notice:
> - **Returns fixed TikTok video detail**
> - **Data cached for 1 hour**
>
> ### Features:
> - ✅ 1-hour data caching
> - ✅ Fixed video detail, parameter: 7319033421676653855
> - ✅ Free to use
>
> ---
>
> # [示例/Example]
> ```
> # 无需参数，始终返回固定视频数据
> # No parameters needed, always returns fixed video data
> GET /api/v1/tiktok/app/fetch_one_video
> ```

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

<a id="get-api-u1-v1-demo-tiktok-web-fetch-user-profile"></a>
### `GET /api/u1/v1/demo/tiktok/web/fetch_user_profile`

- Summary: 【Demo】TikTok固定用户信息（1小时缓存）/[Demo] TikTok Fixed User Profile with Cache
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `tiktok_web_fetch_user_profile_api_v1_demo_tiktok_web_fetch_user_profile_get`

#### Notes

> # 🎯 **这是一个DEMO接口**
>
> ## [中文]
> ### ⚠️ 重要说明:
> - **返回固定TikTok用户信息**
> - **数据缓存1小时**
>
> ### 特性:
> - ✅ 1小时数据缓存
> - ✅ 固定用户: tiktok
> - ✅ 免费使用
>
> ## [English]
> ### ⚠️ Important Notice:
> - **Returns fixed TikTok user profile**
> - **Data cached for 1 hour**
>
> ### Features:
> - ✅ 1-hour data caching
> - ✅ Fixed user: tiktok
> - ✅ Free to use
>
> ---
>
> # [示例/Example]
> ```
> # 无需参数，始终返回固定用户数据
> # No parameters needed, always returns fixed user data
> GET /api/v1/tiktok/web/fetch_user_profile
> ```

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

<a id="get-api-u1-v1-demo-wechat-article-extract"></a>
### `GET /api/u1/v1/demo/wechat/article_extract`

- Summary: 【Demo】微信公众号文章提取（1小时缓存）/[Demo] WeChat Article Extract with Cache
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `wechat_article_extract_api_v1_demo_wechat_article_extract_get`

#### Notes

> # 🎯 **这是一个DEMO接口**
>
> ## [中文]
> ### ⚠️ 重要说明:
> - **这是一个演示(Demo)接口，仅用于测试和展示功能**
> - **不允许修改URL参数，始终返回固定文章的数据**
> - **数据缓存1小时**
>
> ### 用途:
> - 用于测试API连接和数据格式
> - 了解返回数据结构
> - 开发阶段的功能验证
>
> ### 特性:
> - ✅ 1小时数据缓存
> - ✅ 固定文章URL: https://mp.weixin.qq.com/s/c7_-h_3XJLpOBqpUfIlJ9w
> - ✅ 免费使用，无需计费
>
> ### 返回:
> - 固定文章的缓存数据
>
> ---
>
> ## [English]
> ### ⚠️ Important Notice:
> - **This is a DEMO endpoint for testing and demonstration only**
> - **The URL parameter cannot be modified, always returns data for a fixed article**
> - **Data is cached for 1 hour**
>
> ### Purpose:
> - Test API connection and data format
> - Understand return data structure
> - Feature validation during development
>
> ### Features:
> - ✅ 1-hour data caching
> - ✅ Fixed article URL: https://mp.weixin.qq.com/s/c7_-h_3XJLpOBqpUfIlJ9w
> - ✅ Free to use, no billing
>
> ### Return:
> - Cached data for the fixed article
>
> ---
>
> # [示例/Example]
> ```
> # 无需参数，始终返回固定文章数据
> # No parameters needed, always returns fixed article data
> GET /api/v1/wechat/article_extract
> ```

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
