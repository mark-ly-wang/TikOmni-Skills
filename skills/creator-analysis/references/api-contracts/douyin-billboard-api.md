# Douyin-Billboard-API Full Contract

- Back to index: [`api-capability-index.md`](../api-capability-index.md)
- Back to route summary: [`api-tags/douyin-billboard-api.md`](../api-tags/douyin-billboard-api.md)
- Current contract file: `api-contracts/douyin-billboard-api.md`
- Source: `https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- Fetched at: `2026-03-08T06:54:04+00:00`
- Route count: `31`
- Default auth: Header `Authorization` Bearer
- Read this file only when you need precise auth notes, parameter descriptions, defaults, examples, or success-response fields.
- Tag description: **(抖音热点榜数据接口/Douyin-Billboard-API data endpoints)**

## Route Contracts

<a id="get-api-u1-v1-douyin-billboard-fetch-city-list"></a>
### `GET /api/u1/v1/douyin/billboard/fetch_city_list`

- Summary: 获取中国城市列表/Fetch Chinese city list
- Capabilities: trends / rankings
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_city_list_api_v1_douyin_billboard_fetch_city_list_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取城市列表
> ### 参数:
> - 无
> ### 返回:
> - 中国城市列表
>
> # [English]
> ### Purpose:
> - Get city list
> ### Parameters:
> - None
> ### Return:
> - Chinese city list

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

<a id="get-api-u1-v1-douyin-billboard-fetch-content-tag"></a>
### `GET /api/u1/v1/douyin/billboard/fetch_content_tag`

- Summary: 获取垂类内容标签/Fetch vertical content tags
- Capabilities: trends / rankings
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_content_tag_api_v1_douyin_billboard_fetch_content_tag_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取垂类内容标签
> ### 参数:
> - 无
> ### 返回:
> - 垂类内容标签
> ### 注意:
> - 该接口用于获取垂类内容标签，用于query_tag参数构建
> ### 示例:
> 已知顶级垂类内容标签 `美食`，它的顶级垂类id为 `628`；`美食` 的子垂类标签 `品酒教学`，它的子垂类id为 `62802`。
> 那么构建标签查询参数为 `{"value": 628, "children": [{"value": 62808}]}`
>
> 如果需要多个子垂类标签，所有的美食子垂类标签为 `{"value":628,"children":[{"value":62808},{"value":62804},{"value":62806},{"value":62803},{"value":62802},{"value":62801},{"value":62811},{"value":62807},{"value":62805},{"value":62810}]}`
>
> # [English]
> ### Purpose:
> - Get vertical content tags
> ### Parameters:
> - None
> ### Return:
> - Vertical content tags
> ### Note:
> - This interface is used to obtain vertical content tags, used to construct the query_tag parameter
> ### Example:
> Given the top-level vertical content tag `Food`, its top-level vertical id is `628`; `Food`'s sub-vertical tag `Wine Tasting`, its sub-vertical id is `62802`.
> Then the constructed tag query parameter is `{"value": 628, "children": [{"value": 62808}]}`
>
> If you need multiple sub-vertical tags, all food sub-vertical tags are `{"value":628,"children":[{"value":62808},{"value":62804},{"value":62806},{"value":62803},{"value":62802},{"value":62801},{"value":62811},{"value":62807},{"value":62805},{"value":62810}]}`

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

<a id="get-api-u1-v1-douyin-billboard-fetch-hot-account-fans-interest-account-list"></a>
### `GET /api/u1/v1/douyin/billboard/fetch_hot_account_fans_interest_account_list`

- Summary: 获取粉丝兴趣作者 20个用户/Fetch fan interest author 20 users
- Capabilities: trends / rankings
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_hot_account_fans_interest_account_list_api_v1_douyin_billboard_fetch_hot_account_fans_interest_account_list_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取粉丝兴趣作者 20个用户
> ### 参数:
> - sec_uid: 用户sec_id
> ### 返回:
> - 粉丝兴趣作者 20个用户
>
> # [English]
> ### Purpose:
> - Get the fan interest author 20 users
> ### Parameters:
> - sec_uid: User sec_id
> ### Return:
> - Fan interest author 20 users

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| sec_uid | query | string | Yes | 用户sec_id | None | MS4wLjABAAAA8U_l6rBzmy7bcy6xOJel4v0RzoR_wfAubGPeJimN__4 | None |

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

<a id="get-api-u1-v1-douyin-billboard-fetch-hot-account-fans-interest-search-list"></a>
### `GET /api/u1/v1/douyin/billboard/fetch_hot_account_fans_interest_search_list`

- Summary: 获取粉丝近3天搜索词 10个搜索词/Fetch fan interest search term in the last 3 days 10 search terms
- Capabilities: search / trends / rankings
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_hot_account_fans_interest_search_list_api_v1_douyin_billboard_fetch_hot_account_fans_interest_search_list_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取粉丝近3天搜索词 10个搜索词
> ### 参数:
> - sec_uid: 用户sec_id
> ### 返回:
> - 粉丝近3天搜索词 10个搜索词
>
> # [English]
> ### Purpose:
> - Get the fan interest search term in the last 3 days 10 search terms
> ### Parameters:
> - sec_uid: User sec_id
> ### Return:
> - Fan interest search term in the last 3 days 10 search terms

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| sec_uid | query | string | Yes | 用户sec_id | None | MS4wLjABAAAA8U_l6rBzmy7bcy6xOJel4v0RzoR_wfAubGPeJimN__4 | None |

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

<a id="get-api-u1-v1-douyin-billboard-fetch-hot-account-fans-interest-topic-list"></a>
### `GET /api/u1/v1/douyin/billboard/fetch_hot_account_fans_interest_topic_list`

- Summary: 获取粉丝近3天感兴趣的话题 10个话题/Fetch fan interest topic in the last 3 days 10 topics
- Capabilities: trends / rankings / topics
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_hot_account_fans_interest_topic_list_api_v1_douyin_billboard_fetch_hot_account_fans_interest_topic_list_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取粉丝近3天感兴趣的话题 10个话题
> ### 参数:
> - sec_uid: 用户sec_id
> ### 返回:
> - 粉丝近3天感兴趣的话题 10个话题
>
> # [English]
> ### Purpose:
> - Get the fan interest topic in the last 3 days 10 topics
> ### Parameters:
> - sec_uid: User sec_id
> ### Return:
> - Fan interest topic in the last 3 days 10 topics

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| sec_uid | query | string | Yes | 用户sec_id | None | MS4wLjABAAAA8U_l6rBzmy7bcy6xOJel4v0RzoR_wfAubGPeJimN__4 | None |

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

<a id="get-api-u1-v1-douyin-billboard-fetch-hot-account-fans-portrait-list"></a>
### `GET /api/u1/v1/douyin/billboard/fetch_hot_account_fans_portrait_list`

- Summary: 获取粉丝画像/Fetch fan portrait
- Capabilities: trends / rankings
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_hot_account_fans_portrait_list_api_v1_douyin_billboard_fetch_hot_account_fans_portrait_list_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取粉丝画像
> ### 参数:
> - sec_uid: 用户sec_id
> - option: 选项，默认值为：1 手机价格分布
>     - `1` = 手机价格分布
>     - `2` = 性别分布
>     - `3` = 年龄分布
>     - `4` = 地域分布-省份
>     - `5` = 地域分布-城市
>     - `6` = 城市等级
>     - `7` = 手机品牌分布
>     - `8` = 兴趣标签分析 百分比
> ### 返回:
> - 粉丝画像
>
> # [English]
> ### Purpose:
> - Get the fan portrait
> ### Parameters:
> - sec_uid: User sec_id
> - option: Option
>     - 1 Mobile price
>     - 2 Gender distribution
>     - 3 Age distribution
>     - 4 Regional distribution - province
>     - 5 Regional distribution - city
>     - 6 City level
>     - 7 Mobile brand distribution
>     - 8 Interest tag analysis percentage
> ### Return:
> - Fan portrait

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| sec_uid | query | string | Yes | 用户sec_id | None | MS4wLjABAAAA8U_l6rBzmy7bcy6xOJel4v0RzoR_wfAubGPeJimN__4 | None |
| option | query | integer | No | 选项，1 手机价格分布 2 性别分布 3 年龄分布 4 地域分布-省份 5 地域分布-城市 6 城市等级 7 手机品牌分布 8 兴趣标签分析 百分比 | 1 | 1 | None |

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

<a id="get-api-u1-v1-douyin-billboard-fetch-hot-account-item-analysis-list"></a>
### `GET /api/u1/v1/douyin/billboard/fetch_hot_account_item_analysis_list`

- Summary: 获取账号作品分析-上周/Fetch account work analysis - last week
- Capabilities: trends / rankings
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_hot_account_item_analysis_list_api_v1_douyin_billboard_fetch_hot_account_item_analysis_list_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取账号作品分析
> ### 参数:
> - sec_uid: 用户sec_id
> - day: 天数，默认7天
> ### 返回:
> - 账号作品分析
>
> # [English]
> ### Purpose:
> - Get the account work analysis
> ### Parameters:
> - sec_uid: User sec_id
> - day: Number of days, default 7 days
> ### Return:
> - Account work analysis

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| sec_uid | query | string | Yes | 用户sec_id | None | MS4wLjABAAAA8U_l6rBzmy7bcy6xOJel4v0RzoR_wfAubGPeJimN__4 | None |

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

<a id="post-api-u1-v1-douyin-billboard-fetch-hot-account-list"></a>
### `POST /api/u1/v1/douyin/billboard/fetch_hot_account_list`

- Summary: 获取热门账号/Fetch hot account list
- Capabilities: trends / rankings
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_hot_account_list_api_v1_douyin_billboard_fetch_hot_account_list_post`

#### Notes

> # [中文]
> ### 用途:
> - 获取热门账号
> ### 参数:
> - date_window: 时间窗口，格式 小时，默认24小时
> - page_num: 页码，默认1
> - page_size: 每页数量，默认20
> - query_tag: 子级垂类标签，空则为全部，多个标签需传入
> {"value": "{顶级垂类标签id}", "children": [
>     {"value": "{子级垂类标签id}"},
>     {"value": "{子级垂类标签id}"}
> ]}
> ### 返回:
> - 热门账号
>
> # [English]
> ### Purpose:
> - Get the hot account
> ### Parameters:
> - date_window: Time window, format hour, default 24 hours
> - page_num: Page number, default 1
> - page_size: Number of items per page, default 20
> - query_tag: Sub-level vertical category tag, empty for all, multiple tags need to be passed in
> {"value": "{top-level vertical category id}", "children": [
>     {"value": "{sub-level vertical category id}"},
>     {"value": "{sub-level vertical category id}"}
> ]}
> ### Return:
> - Hot account

#### Parameters

None

#### Request Body

- required: No

##### `application/json`

- Schema summary: `date_window`:integer, `page_num`:integer, `page_size`:integer, `query_tag`{...}

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| date_window | integer | No | 时间窗口，格式 小时，默认24小时 | 24 | None | None |
| page_num | integer | No | 页码，默认1 | 1 | None | None |
| page_size | integer | No | 每页数量，默认10 | 10 | None | None |
| query_tag | object | No | 子级垂类标签，空则为全部，多个标签需传入{"value": "{顶级垂类标签id}", "children": [{"value": "{子级垂类标签id}"}, {"value": "{子级垂类标签id}"}]} | None | None | None |

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

<a id="get-api-u1-v1-douyin-billboard-fetch-hot-account-search-list"></a>
### `GET /api/u1/v1/douyin/billboard/fetch_hot_account_search_list`

- Summary: 搜索用户名或抖音号/Fetch account search list
- Capabilities: search / trends / rankings
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_hot_account_search_list_api_v1_douyin_billboard_fetch_hot_account_search_list_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取搜索用户名或抖音号
> ### 参数:
> - keyword: 搜索的用户名或抖音号
> - cursor: 游标，默认空
> ### 返回:
> - 搜索结果
>
> # [English]
> ### Purpose:
> - Get the search username or Douyin number
> ### Parameters:
> - keyword: Search username or Douyin number
> - cursor: Cursor, default empty
> ### Return:
> - Search result

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| keyword | query | string | Yes | 搜索的用户名或抖音号 | None | rmrbxmt | None |
| cursor | query | integer | Yes | 游标，默认空 | None | 0 | None |

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

<a id="get-api-u1-v1-douyin-billboard-fetch-hot-account-trends-list"></a>
### `GET /api/u1/v1/douyin/billboard/fetch_hot_account_trends_list`

- Summary: 获取账号粉丝数据趋势/Fetch account fan data trend
- Capabilities: trends / rankings
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_hot_account_trends_list_api_v1_douyin_billboard_fetch_hot_account_trends_list_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取账号粉丝数据趋势
> ### 参数:
> - sec_uid: 用户sec_id
> - option: 选项，2 新增点赞量 3 新增作品量 4 新增评论量 5 新增分享量
> - date_window: 时间窗口，1 按小时 2 按天
> ### 返回:
> - 账号粉丝数据趋势
>
> # [English]
> ### Purpose:
> - Get the account fan data trend
> ### Parameters:
> - sec_uid: User sec_id
> - option: Option, 2 New like 3 New work 4 New comment 5 New share
> - date_window: Time window, 1 by hour 2 by day
> ### Return:
> - Account fan data trend

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| sec_uid | query | string | Yes | 用户sec_id | None | MS4wLjABAAAA8U_l6rBzmy7bcy6xOJel4v0RzoR_wfAubGPeJimN__4 | None |
| option | query | integer | No | 选项，2 新增点赞量 3 新增作品量 4 新增评论量 5 新增分享量 | 2 | None | None |
| date_window | query | integer | No | 时间窗口，1 按小时 2 按天 | 24 | 24 | None |

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

<a id="get-api-u1-v1-douyin-billboard-fetch-hot-calendar-detail"></a>
### `GET /api/u1/v1/douyin/billboard/fetch_hot_calendar_detail`

- Summary: 获取活动日历详情/Fetch activity calendar detail
- Capabilities: trends / rankings / details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_hot_calendar_detail_api_v1_douyin_billboard_fetch_hot_calendar_detail_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取活动日历详情
> ### 参数:
> - calendar_id: 活动id
> ### 返回:
> - 活动日历详情
>
> # [English]
> ### Purpose:
> - Get the activity calendar details
> ### Parameters:
> - calendar_id: Activity id
> ### Return:
> - Activity calendar details

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| calendar_id | query | string | Yes | 活动id | None | 1720 | None |

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

<a id="post-api-u1-v1-douyin-billboard-fetch-hot-calendar-list"></a>
### `POST /api/u1/v1/douyin/billboard/fetch_hot_calendar_list`

- Summary: 获取活动日历/Fetch activity calendar
- Capabilities: trends / rankings
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_hot_calendar_list_api_v1_douyin_billboard_fetch_hot_calendar_list_post`

#### Notes

> # [中文]
> ### 用途:
> - 获取活动日历
> ### 参数:
> - city_code: 城市编码，从城市列表获取，空为全部
> - category_code: 热点榜分类编码，从热点榜分类获取，空为全部
> - end_date: 快照结束时间 格式10位时间戳
> - start_date: 快照开始时间 格式10位时间戳
> ### 返回:
> - 活动日历
>
> # [English]
> ### Purpose:
> - Get the activity calendar
> ### Parameters:
> - city_code: City code, get from city list, empty for all
> - category_code: Hot list category code, get from hot list category, empty for all
> - end_date: Snapshot end time format 10 digit timestamp
> - start_date: Snapshot start time format 10 digit timestamp
> ### Return:
> - Activity calendar

#### Parameters

None

#### Request Body

- required: No

##### `application/json`

- Schema summary: `city_code`:string, `category_code`:string, `end_date`:integer, `start_date`:integer

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| city_code | string | No | 城市编码，从城市列表获取，空为全部 | None | None | None |
| category_code | string | No | 热点榜分类编码，从热点榜分类获取，空为全部 | None | None | None |
| end_date | integer | No | 快照结束时间 格式10位时间戳 | 1735488000 | None | None |
| start_date | integer | No | 快照开始时间 格式10位时间戳 | 1734902400 | None | None |

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

<a id="get-api-u1-v1-douyin-billboard-fetch-hot-category-list"></a>
### `GET /api/u1/v1/douyin/billboard/fetch_hot_category_list`

- Summary: 获取热点榜分类/Fetch hot list category
- Capabilities: trends / rankings
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_hot_category_list_api_v1_douyin_billboard_fetch_hot_category_list_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取热点榜分类的id与热度
> - 注意：使用start_date和end_date参数需要移除snapshot_time参数才可以生效
> ### 参数:
> - billboard_type: 榜单类型
>     - rise 上升热点榜
>     - city 城市热点榜
>     - total 热点总榜
> - snapshot_time: 快照时间
> - start_date: 快照开始时间
> - end_date: 快照结束时间
> - keyword: 热点搜索词
> ### 返回:
> - 热点榜分类
>
> # [English]
> ### Purpose:
> - Get the id and popularity of the hot list category
> - Note: Using start_date and end_date parameters requires removing the snapshot_time parameter
> - Note: snapshot_time and start_date, end_date parameters cannot be empty at the same time
> ### Parameters:
> - billboard_type: Billboard type
>     - rise Rising hot list
>     - city City hot list
>     - total Total hot list
> - snapshot_time: Snapshot time
> - start_date: Snapshot start time
> - end_date: Snapshot end time
> - keyword: Hot search term
> ### Return:
> - Hot category list

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| billboard_type | query | string | Yes | 榜单类型 | None | rise | None |
| snapshot_time | query | string | No | 快照时间 格式yyyyMMddHHmmss | 20250106151500 | None | None |
| start_date | query | string | No | 快照开始时间 格式yyyyMMdd | None | None | None |
| end_date | query | string | No | 快照结束时间 格式yyyyMMdd | None | None | None |
| keyword | query | string | No | 热点搜索词 | None | None | None |

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

<a id="get-api-u1-v1-douyin-billboard-fetch-hot-challenge-list"></a>
### `GET /api/u1/v1/douyin/billboard/fetch_hot_challenge_list`

- Summary: 获取挑战热榜/Fetch hot challenge list
- Capabilities: trends / rankings / topics
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_hot_challenge_list_api_v1_douyin_billboard_fetch_hot_challenge_list_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取挑战榜
> ### 参数:
> - page: 页码
> - page_size: 每页数量
> - keyword: 热点搜索词
> ### 返回:
> - 挑战榜
>
> # [English]
> ### Purpose:
> - Get the challenge list
> ### Parameters:
> - page: Page number
> - page_size: Number of items per page
> - keyword: Hot search term
> ### Return:
> - Challenge list

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| page | query | integer | Yes | 页码 | None | 1 | None |
| page_size | query | integer | Yes | 每页数量 | None | 10 | None |
| keyword | query | string | No | 热点搜索词 | None | None | None |

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

<a id="get-api-u1-v1-douyin-billboard-fetch-hot-city-list"></a>
### `GET /api/u1/v1/douyin/billboard/fetch_hot_city_list`

- Summary: 获取同城热点榜/Fetch city hot list
- Capabilities: trends / rankings
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_hot_city_list_api_v1_douyin_billboard_fetch_hot_city_list_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取同城热点榜
> ### 参数:
> - page: 页码
> - page_size: 每页数量
> - order: 排序方式
>     - rank 按热度排序
>     - rank_diff 按排名变化
> - city_code: 城市编码，从城市列表获取，空为全部
> - sentence_tag: 热点分类标签，从热点榜分类获取，多个分类用逗号分隔，空为全部
> - keyword: 热点搜索词
> ### 返回:
> - 同城热点榜
>
> # [English]
> ### Purpose:
> - Get the city hot list
> ### Parameters:
> - page: Page number
> - page_size: Number of items per page
> - order: Sorting method
>     - rank Sort by popularity
>     - rank_diff Sort by ranking change
> - city_code: City code, get from city list, empty for all
> - sentence_tag: Hot category tag, get from hot list category, multiple categories separated by commas, empty for all
> - keyword: Hot search term
> ### Return:
> - City hot list

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| page | query | integer | Yes | 页码 | None | 1 | None |
| page_size | query | integer | Yes | 每页数量 | None | 10 | None |
| order | query | string | Yes | 排序方式 | None | None | None |
| city_code | query | string | No | 城市编码，从城市列表获取，空为全部 | None | None | None |
| sentence_tag | query | string | No | 热点分类标签，从热点榜分类获取，多个分类用逗号分隔，空为全部 | None | None | None |
| keyword | query | string | No | 热点搜索词 | None | None | None |

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

<a id="get-api-u1-v1-douyin-billboard-fetch-hot-comment-word-list"></a>
### `GET /api/u1/v1/douyin/billboard/fetch_hot_comment_word_list`

- Summary: 获取作品评论分析-词云权重/Fetch work comment analysis word cloud weight
- Capabilities: comments / trends / rankings
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_hot_comment_word_list_api_v1_douyin_billboard_fetch_hot_comment_word_list_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取作品评论分析-词云权重
> ### 参数:
> - aweme_id: 作品id
> ### 返回:
> - 作品评论分析-词云权重
>
> # [English]
> ### Purpose:
> - Get the work comment analysis word cloud weight
> ### Parameters:
> - aweme_id: Work id
> ### Return:
> - Work comment analysis word cloud weight

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| aweme_id | query | string | Yes | 作品id | None | 7456035425539329340 | None |

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

<a id="get-api-u1-v1-douyin-billboard-fetch-hot-item-trends-list"></a>
### `GET /api/u1/v1/douyin/billboard/fetch_hot_item_trends_list`

- Summary: 获取作品数据趋势/Fetch post data trend
- Capabilities: trends / rankings
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_hot_item_trends_list_api_v1_douyin_billboard_fetch_hot_item_trends_list_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取作品数据趋势
> ### 参数:
> - aweme_id: 作品id
> - option: 选项，7 点赞量 8 分享量 9 评论量
> - date_window: 时间窗口，1 按小时 2 按天
> ### 返回:
> - 作品数据趋势
>
> # [English]
> ### Purpose:
> - Get the work data trend
> ### Parameters:
> - aweme_id: Work id
> - option: Option, 7 Like 8 Share 9 Comment
> - date_window: Time window, 1 by hour 2 by day
> ### Return:
> - Work data trend

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| aweme_id | query | string | No | 作品id | None | None | None |
| option | query | integer | No | 选项，7 点赞量 8 分享量 9 评论量 | 7 | None | None |
| date_window | query | integer | No | 时间窗口，1 按小时 2 按天 | 1 | None | None |

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

<a id="get-api-u1-v1-douyin-billboard-fetch-hot-rise-list"></a>
### `GET /api/u1/v1/douyin/billboard/fetch_hot_rise_list`

- Summary: 获取上升热点榜/Fetch rising hot list
- Capabilities: trends / rankings
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_hot_rise_list_api_v1_douyin_billboard_fetch_hot_rise_list_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取上升热点榜
> ### 参数:
> - page: 页码
> - page_size: 每页数量
> - order: 排序方式
>     - rank 按热度排序
>     - rank_diff 按排名变化
> - sentence_tag: 热点分类标签，从热点榜分类获取，多个分类用逗号分隔，空为全部
> - keyword: 热点搜索词
> ### 返回:
> - 上升热点榜
>
> # [English]
> ### Purpose:
> - Get the rising hot list
> ### Parameters:
> - page: Page number
> - page_size: Number of items per page
> - order: Sorting method
>     - rank Sort by popularity
>     - rank_diff Sort by ranking change
> - sentence_tag: Hot category tag, get from hot list category, multiple categories separated by commas, empty for all
> - keyword: Hot search term
> ### Return:
> - Rising hot list

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| page | query | integer | Yes | 页码 | None | 1 | None |
| page_size | query | integer | Yes | 每页数量 | None | 10 | None |
| order | query | string | Yes | 排序方式 | None | rank | None |
| sentence_tag | query | string | No | 热点分类标签，从热点榜分类获取，多个分类用逗号分隔，空为全部 | None | None | None |
| keyword | query | string | No | 热点搜索词 | None | None | None |

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

<a id="post-api-u1-v1-douyin-billboard-fetch-hot-total-high-fan-list"></a>
### `POST /api/u1/v1/douyin/billboard/fetch_hot_total_high_fan_list`

- Summary: 获取高涨粉率榜/Fetch high fan rate list
- Capabilities: trends / rankings
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_hot_total_high_fan_list_api_v1_douyin_billboard_fetch_hot_total_high_fan_list_post`

#### Notes

> # [中文]
> ### 用途:
> - 获取高涨粉率榜
> ### 参数:
> - page: 页码
> - page_size: 每页数量
> - date_window: 时间窗口，1 按小时 2 按天
> - tags: 子级垂类标签，空则为全部，多个标签需传入
>     {"value": "{顶级垂类标签id}", "children": [
>         {"value": "{子级垂类标签id}"},
>         {"value": "{子级垂类标签id}"}
>     ]}
> ### 返回:
> - 高涨粉率榜
>
> # [English]
> ### Purpose:
> - Get the high fan rate list
> ### Parameters:
> - page: Page number
> - page_size: Number of items per page
> - date_window: Time window, 1 by hour 2 by day
> - tags: Sub-level vertical category tag, empty for all, multiple tags need to be passed in
>     {"value": "{top-level vertical category id}", "children": [
>         {"value": "{sub-level vertical category id}"},
>         {"value": "{sub-level vertical category id}"}
>     ]}
> ### Return:
> - High fan rate list

#### Parameters

None

#### Request Body

- required: No

##### `application/json`

- Schema summary: `page`:integer, `page_size`:integer, `date_window`:integer, `tags`[object]

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| page | integer | No | 页码 | 1 | None | None |
| page_size | integer | No | 每页数量 | 10 | None | None |
| date_window | integer | No | 时间窗口，1 按小时 2 按天 | 24 | None | None |
| tags | array<object> | No | 子级垂类标签，空则为全部，多个标签需传入{"value": "{顶级垂类标签id}", "children": [{"value": "{子级垂类标签id}"}, {"value": "{子级垂类标签id}"}]} | None | None | None |
| tags[] | object | Yes | None | None | None | None |

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

<a id="post-api-u1-v1-douyin-billboard-fetch-hot-total-high-like-list"></a>
### `POST /api/u1/v1/douyin/billboard/fetch_hot_total_high_like_list`

- Summary: 获取高点赞率榜/Fetch high like rate list
- Capabilities: trends / rankings
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_hot_total_high_like_list_api_v1_douyin_billboard_fetch_hot_total_high_like_list_post`

#### Notes

> # [中文]
> ### 用途:
> - 获取高点赞率榜
> ### 参数:
> - page: 页码
> - page_size: 每页数量
> - date_window: 时间窗口，1 按小时 2 按天
> - tags: 子级垂类标签，空则为全部，多个标签需传入
>     {"value": "{顶级垂类标签id}", "children": [
>         {"value": "{子级垂类标签id}"},
>         {"value": "{子级垂类标签id}"}
>     ]}
> ### 返回:
> - 高点赞率榜
>
> # [English]
> ### Purpose:
> - Get the high like rate list
> ### Parameters:
> - page: Page number
> - page_size: Number of items per page
> - date_window: Time window, 1 by hour 2 by day
> - tags: Sub-level vertical category tag, empty for all, multiple tags need to be passed in
>     {"value": "{top-level vertical category id}", "children": [
>         {"value": "{sub-level vertical category id}"},
>         {"value": "{sub-level vertical category id}"}
>     ]}
> ### Return:
> - High like rate list

#### Parameters

None

#### Request Body

- required: No

##### `application/json`

- Schema summary: `page`:integer, `page_size`:integer, `date_window`:integer, `tags`[object]

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| page | integer | No | 页码 | 1 | None | None |
| page_size | integer | No | 每页数量 | 10 | None | None |
| date_window | integer | No | 时间窗口，1 按小时 2 按天 | 24 | None | None |
| tags | array<object> | No | 子级垂类标签，空则为全部，多个标签需传入{"value": "{顶级垂类标签id}", "children": [{"value": "{子级垂类标签id}"}, {"value": "{子级垂类标签id}"}]} | None | None | None |
| tags[] | object | Yes | None | None | None | None |

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

<a id="post-api-u1-v1-douyin-billboard-fetch-hot-total-high-play-list"></a>
### `POST /api/u1/v1/douyin/billboard/fetch_hot_total_high_play_list`

- Summary: 获取高完播率榜/Fetch high completion rate list
- Capabilities: trends / rankings
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_hot_total_high_play_list_api_v1_douyin_billboard_fetch_hot_total_high_play_list_post`

#### Notes

> # [中文]
> ### 用途:
> - 获取高完播率榜
> ### 参数:
> - page: 页码
> - page_size: 每页数量
> - date_window: 时间窗口，1 按小时 2 按天
> - tags: 子级垂类标签，空则为全部，多个标签需传入
>     {"value": "{顶级垂类标签id}", "children": [
>         {"value": "{子级垂类标签id}"},
>         {"value": "{子级垂类标签id}"}
>     ]}
> ### 返回:
> - 高完播率榜
>
> # [English]
> ### Purpose:
> - Get the high completion rate list
> ### Parameters:
> - page: Page number
> - page_size: Number of items per page
> - date_window: Time window, 1 by hour 2 by day
> - tags: Sub-level vertical category tag, empty for all, multiple tags need to be passed in
>     {"value": "{top-level vertical category id}", "children": [
>         {"value": "{sub-level vertical category id}"},
>         {"value": "{sub-level vertical category id}"}
>     ]}
> ### Return:
> - High completion rate list

#### Parameters

None

#### Request Body

- required: No

##### `application/json`

- Schema summary: `page`:integer, `page_size`:integer, `date_window`:integer, `tags`[object]

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| page | integer | No | 页码 | 1 | None | None |
| page_size | integer | No | 每页数量 | 10 | None | None |
| date_window | integer | No | 时间窗口，1 按小时 2 按天 | 24 | None | None |
| tags | array<object> | No | 子级垂类标签，空则为全部，多个标签需传入{"value": "{顶级垂类标签id}", "children": [{"value": "{子级垂类标签id}"}, {"value": "{子级垂类标签id}"}]} | None | None | None |
| tags[] | object | Yes | None | None | None | None |

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

<a id="post-api-u1-v1-douyin-billboard-fetch-hot-total-high-search-list"></a>
### `POST /api/u1/v1/douyin/billboard/fetch_hot_total_high_search_list`

- Summary: 获取热度飙升的搜索榜/Fetch search list with rising popularity
- Capabilities: search / trends / rankings
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_hot_total_high_search_list_api_v1_douyin_billboard_fetch_hot_total_high_search_list_post`

#### Notes

> # [中文]
> ### 用途:
> - 获取热度飙升的搜索榜
> ### 参数:
> - page_num: 页码
> - page_size: 每页数量
> - date_window: 时间窗口，1 按小时 2 按天
> - keyword: 搜索关键字
> ### 返回:
> - 热度飙升的搜索榜
>
> # [English]
> ### Purpose:
> - Get the search list with rising popularity
> ### Parameters:
> - page_num: Page number
> - page_size: Number of items per page
> - date_window: Time window, 1 by hour 2 by day
> - keyword: Search keyword
> ### Return:
> - Search list with rising popularity

#### Parameters

None

#### Request Body

- required: No

##### `application/json`

- Schema summary: `page_num`:integer, `page_size`:integer, `date_window`:integer, `keyword`:string

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| page_num | integer | No | 页码 | 1 | None | None |
| page_size | integer | No | 每页数量 | 10 | None | None |
| date_window | integer | No | 时间窗口，1 按小时 2 按天 | 24 | None | None |
| keyword | string | No | 搜索关键字 | 抖音 | None | None |

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

<a id="post-api-u1-v1-douyin-billboard-fetch-hot-total-high-topic-list"></a>
### `POST /api/u1/v1/douyin/billboard/fetch_hot_total_high_topic_list`

- Summary: 获取热度飙升的话题榜/Fetch topic list with rising popularity
- Capabilities: trends / rankings / topics
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_hot_total_high_topic_list_api_v1_douyin_billboard_fetch_hot_total_high_topic_list_post`

#### Notes

> # [中文]
> ### 用途:
> - 获取热度飙升的话题榜
> ### 参数:
> - page: 页码
> - page_size: 每页数量
> - date_window: 时间窗口，1 按小时 2 按天
> - tags: 子级垂类标签，空则为全部，多个标签需传入
>     {"value": "{顶级垂类标签id}", "children": [
>         {"value": "{子级垂类标签id}"},
>         {"value": "{子级垂类标签id}"}
>     ]}
> ### 返回:
> - 热度飙升的话题榜
>
> # [English]
> ### Purpose:
> - Get the topic list with rising popularity
> ### Parameters:
> - page: Page number
> - page_size: Number of items per page
> - date_window: Time window, 1 by hour 2 by day
> - tags: Sub-level vertical category tag, empty for all, multiple tags need to be passed in
>     {"value": "{top-level vertical category id}", "children": [
>         {"value": "{sub-level vertical category id}"},
>         {"value": "{sub-level vertical category id}"}
>     ]}
> ### Return:
> - Topic list with rising popularity

#### Parameters

None

#### Request Body

- required: No

##### `application/json`

- Schema summary: `page`:integer, `page_size`:integer, `date_window`:integer, `tags`[object]

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| page | integer | No | 页码 | 1 | None | None |
| page_size | integer | No | 每页数量 | 10 | None | None |
| date_window | integer | No | 时间窗口，1 按小时 2 按天 | 24 | None | None |
| tags | array<object> | No | 子级垂类标签，空则为全部，多个标签需传入{"value": "{顶级垂类标签id}", "children": [{"value": "{子级垂类标签id}"}, {"value": "{子级垂类标签id}"}]} | None | None | None |
| tags[] | object | Yes | None | None | None | None |

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

<a id="get-api-u1-v1-douyin-billboard-fetch-hot-total-hot-word-detail-list"></a>
### `GET /api/u1/v1/douyin/billboard/fetch_hot_total_hot_word_detail_list`

- Summary: 获取内容词详情/Fetch content word details
- Capabilities: trends / rankings / details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_hot_total_hot_word_detail_list_api_v1_douyin_billboard_fetch_hot_total_hot_word_detail_list_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取内容词详情
> ### 参数:
> - keyword: 搜索关键字
> - word_id: 内容词id
> - query_day: 查询日期，格式为YYYYMMDD
> ### 返回:
> - 内容词详情
>
> # [English]
> ### Purpose:
> - Get the details of content words
> ### Parameters:
> - keyword: Search keyword
> - word_id: Content word id
> - query_day: Query date, format is YYYYMMDD
> ### Return:
> - Details of content words

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| keyword | query | string | Yes | 搜索关键字 | None | None | None |
| word_id | query | string | Yes | 内容词id | None | None | None |
| query_day | query | integer | Yes | 查询日期，格式为YYYYMMDD，需为当日 | None | 20250105 | None |

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

<a id="post-api-u1-v1-douyin-billboard-fetch-hot-total-hot-word-list"></a>
### `POST /api/u1/v1/douyin/billboard/fetch_hot_total_hot_word_list`

- Summary: 获取全部热门内容词/Fetch all hot content words
- Capabilities: trends / rankings
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_hot_total_hot_word_list_api_v1_douyin_billboard_fetch_hot_total_hot_word_list_post`

#### Notes

> # [中文]
> ### 用途:
> - 获取全部内容词
> ### 参数:
> - page_num: 页码
> - page_size: 每页数量
> - date_window: 时间窗口，1 按小时 2 按天
> - keyword: 搜索关键字
> ### 返回:
> - 全部内容词
>
> # [English]
> ### Purpose:
> - Get the list of all content words
> ### Parameters:
> - page_num: Page number
> - page_size: Number of items per page
> - date_window: Time window, 1 by hour 2 by day
> - keyword: Search keyword
> ### Return:
> - List of all content words

#### Parameters

None

#### Request Body

- required: No

##### `application/json`

- Schema summary: `page_num`:integer, `page_size`:integer, `date_window`:integer, `keyword`:string

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| page_num | integer | No | 页码 | 1 | None | None |
| page_size | integer | No | 每页数量 | 10 | None | None |
| date_window | integer | No | 时间窗口，1 按小时 2 按天 | 24 | None | None |
| keyword | string | No | 搜索关键字 | 抖音 | None | None |

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

<a id="get-api-u1-v1-douyin-billboard-fetch-hot-total-list"></a>
### `GET /api/u1/v1/douyin/billboard/fetch_hot_total_list`

- Summary: 获取热点总榜/Fetch total hot list
- Capabilities: trends / rankings
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_hot_total_list_api_v1_douyin_billboard_fetch_hot_total_list_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取热点总榜
> ### 参数:
> - page: 页码
> - page_size: 每页数量
> - type: 快照类型 snapshot 按时刻查看 range 按时间范围。
>     - 备注：snapshot_time 在 snapshot时有效，start_date 和 end_date 在 range 时有效
> - snapshot_time: 快照时间 格式yyyyMMddHHmmss
> - start_date: 快照开始时间 格式yyyyMMdd
> - end_date: 快照结束时间 格式yyyyMMdd
> - sentence_tag: 热点分类标签，从热点榜分类获取，多个分类用逗号分隔，空为全部
> - keyword: 热点搜索词
> ### 返回:
> - 热点总榜
>
> # [English]
> ### Purpose:
> - Get the total hot list
> ### Parameters:
> - page: Page number
> - page_size: Number of items per page
> - type: Snapshot type snapshot view by time range view by time range.
>     - Note: snapshot_time is valid when snapshot, start_date and end_date are valid when range
> - snapshot_time: Snapshot time format yyyyMMddHHmmss
> - start_date: Snapshot start time format yyyyMMdd
> - end_date: Snapshot end time format yyyyMMdd
> - sentence_tag: Hot category tag, get from hot list category, multiple categories separated by commas, empty for all
> - keyword: Hot search term
> ### Return:
> - Total hot list

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| page | query | integer | Yes | 页码 | None | 1 | None |
| page_size | query | integer | Yes | 每页数量 | None | 10 | None |
| type | query | string | Yes | 快照类型 snapshot 按时刻查看 range 按时间范围 | None | None | None |
| snapshot_time | query | string | No | 快照时间 格式yyyyMMddHHmmss | 20250106151500 | None | None |
| start_date | query | string | No | 快照开始时间 格式yyyyMMdd | None | None | None |
| end_date | query | string | No | 快照结束时间 格式yyyyMMdd | None | None | None |
| sentence_tag | query | string | No | 热点分类标签，从热点榜分类获取，多个分类用逗号分隔，空为全部 | None | None | None |
| keyword | query | string | No | 热点搜索词 | None | None | None |

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

<a id="post-api-u1-v1-douyin-billboard-fetch-hot-total-low-fan-list"></a>
### `POST /api/u1/v1/douyin/billboard/fetch_hot_total_low_fan_list`

- Summary: 获取低粉爆款榜/Fetch low fan explosion list
- Capabilities: trends / rankings
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_hot_total_low_fan_list_api_v1_douyin_billboard_fetch_hot_total_low_fan_list_post`

#### Notes

> # [中文]
> ### 用途:
> - 获取低粉爆款榜
> ### 参数:
> - page: 页码
> - page_size: 每页数量
> - date_window: 时间窗口，1 按小时 2 按天
> - tags: 子级垂类标签，空则为全部，多个标签需传入
>     {"value": "{顶级垂类标签id}", "children": [
>         {"value": "{子级垂类标签id}"},
>         {"value": "{子级垂类标签id}"}
>     ]}
> ### 返回:
> - 低粉爆款榜
>
> # [English]
> ### Purpose:
> - Get the low fan explosion list
> ### Parameters:
> - page: Page number
> - page_size: Number of items per page
> - date_window: Time window, 1 by hour 2 by day
> - tags: Sub-level vertical category tag, empty for all, multiple tags need to be passed in
>     {"value": "{top-level vertical category id}", "children": [
>         {"value": "{sub-level vertical category id}"},
>         {"value": "{sub-level vertical category id}"}
>     ]}
> ### Return:
> - Low fan explosion list

#### Parameters

None

#### Request Body

- required: No

##### `application/json`

- Schema summary: `page`:integer, `page_size`:integer, `date_window`:integer, `tags`[object]

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| page | integer | No | 页码 | 1 | None | None |
| page_size | integer | No | 每页数量 | 10 | None | None |
| date_window | integer | No | 时间窗口，1 按小时 2 按天 | 24 | None | None |
| tags | array<object> | No | 子级垂类标签，空则为全部，多个标签需传入{"value": "{顶级垂类标签id}", "children": [{"value": "{子级垂类标签id}"}, {"value": "{子级垂类标签id}"}]} | None | None | None |
| tags[] | object | Yes | None | None | None | None |

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

<a id="post-api-u1-v1-douyin-billboard-fetch-hot-total-search-list"></a>
### `POST /api/u1/v1/douyin/billboard/fetch_hot_total_search_list`

- Summary: 获取搜索热榜/Fetch search hot list
- Capabilities: search / trends / rankings
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_hot_total_search_list_api_v1_douyin_billboard_fetch_hot_total_search_list_post`

#### Notes

> # [中文]
> ### 用途:
> - 获取搜索榜
> ### 参数:
> - page_num: 页码
> - page_size: 每页数量
> - date_window: 时间窗口，1 按小时 2 按天
> - keyword: 搜索关键字
> ### 返回:
> - 搜索榜
>
> # [English]
> ### Purpose:
> - Get the search list
> ### Parameters:
> - page_num: Page number
> - page_size: Number of items per page
> - date_window: Time window, 1 by hour 2 by day
> - keyword: Search keyword
> ### Return:
> - Search list

#### Parameters

None

#### Request Body

- required: No

##### `application/json`

- Schema summary: `page_num`:integer, `page_size`:integer, `date_window`:integer, `keyword`:string

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| page_num | integer | No | 页码 | 1 | None | None |
| page_size | integer | No | 每页数量 | 10 | None | None |
| date_window | integer | No | 时间窗口，1 按小时 2 按天 | 24 | None | None |
| keyword | string | No | 搜索关键字 | 抖音 | None | None |

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

<a id="post-api-u1-v1-douyin-billboard-fetch-hot-total-topic-list"></a>
### `POST /api/u1/v1/douyin/billboard/fetch_hot_total_topic_list`

- Summary: 获取话题热榜/Fetch topic hot list
- Capabilities: trends / rankings / topics
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_hot_total_topic_list_api_v1_douyin_billboard_fetch_hot_total_topic_list_post`

#### Notes

> # [中文]
> ### 用途:
> - 获取话题榜
> ### 参数:
> - page: 页码
> - page_size: 每页数量
> - date_window: 时间窗口，1 按小时 2 按天
> - tags: 子级垂类标签，空则为全部，多个标签需传入
>     {"value": "{顶级垂类标签id}", "children": [
>         {"value": "{子级垂类标签id}"},
>         {"value": "{子级垂类标签id}"}
>     ]}
> ### 返回:
> - 话题榜
>
> # [English]
> ### Purpose:
> - Get the topic list
> ### Parameters:
> - page: Page number
> - page_size: Number of items per page
> - date_window: Time window, 1 by hour 2 by day
> - tags: Sub-level vertical category tag, empty for all, multiple tags need to be passed in
>     {"value": "{top-level vertical category id}", "children": [
>         {"value": "{sub-level vertical category id}"},
>         {"value": "{sub-level vertical category id}"}
>     ]}
> ### Return:
> - Topic list

#### Parameters

None

#### Request Body

- required: No

##### `application/json`

- Schema summary: `page`:integer, `page_size`:integer, `date_window`:integer, `tags`[object]

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| page | integer | No | 页码 | 1 | None | None |
| page_size | integer | No | 每页数量 | 10 | None | None |
| date_window | integer | No | 时间窗口，1 按小时 2 按天 | 24 | None | None |
| tags | array<object> | No | 子级垂类标签，空则为全部，多个标签需传入{"value": "{顶级垂类标签id}", "children": [{"value": "{子级垂类标签id}"}, {"value": "{子级垂类标签id}"}]} | None | None | None |
| tags[] | object | Yes | None | None | None | None |

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

<a id="post-api-u1-v1-douyin-billboard-fetch-hot-total-video-list"></a>
### `POST /api/u1/v1/douyin/billboard/fetch_hot_total_video_list`

- Summary: 获取视频热榜/Fetch video hot list
- Capabilities: trends / rankings / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_hot_total_video_list_api_v1_douyin_billboard_fetch_hot_total_video_list_post`

#### Notes

> # [中文]
> ### 用途:
> - 获取视频榜
> ### 参数:
> - page: 页码，默认1
> - page_size: 每页数量，默认10
> - date_window: 时间窗口，1 按小时 2 按天
> - sub_type: 榜单分类，1001 视频总榜 1002 低粉爆款 1003 高完播率 1004 高涨粉率 1005 高点赞率
> - tags: 子级垂类标签，空则为全部，多个标签需传入
>     {"value": "{顶级垂类标签id}", "children": [
>         {"value": "{子级垂类标签id}"},
>         {"value": "{子级垂类标签id}"}
>     ]}
> ### 返回:
> - 视频榜
>
> # [English]
> ### Purpose:
> - Get the video list
> ### Parameters:
> - page: Page number
> - page_size: Number of items per page
> - date_window: Time window, 1 by hour 2 by day
> - sub_type: List category, 1001 Video total list 1002 Low fan explosion 1003 High completion rate 1004 High fan growth rate 1005 High like rate
> - tags: Sub-level vertical category tag, empty for all, multiple tags need to be passed in
>     {"value": "{top-level vertical category id}", "children": [
>         {"value": "{sub-level vertical category id}"},
>         {"value": "{sub-level vertical category id}"}
>     ]}
> ### Return:
> - Video list

#### Parameters

None

#### Request Body

- required: No

##### `application/json`

- Schema summary: `page`:integer, `page_size`:integer, `date_window`:integer, `sub_type`:integer, `tags`[object]

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| page | integer | No | 页码，默认1 | 1 | None | None |
| page_size | integer | No | 每页数量，默认10 | 10 | None | None |
| date_window | integer | No | 时间窗口，1 按小时 2 按天 | 24 | None | None |
| sub_type | integer | No | 榜单分类，1001 视频总榜 1002 低粉爆款 1003 高完播率 1004 高涨粉率 1005 高点赞率 | 1001 | None | None |
| tags | array<object> | No | 子级垂类标签，空则为全部，多个标签需传入{"value": "{顶级垂类标签id}", "children": [{"value": "{子级垂类标签id}"}, {"value": "{子级垂类标签id}"}]} | None | None | None |
| tags[] | object | Yes | None | None | None | None |

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

<a id="get-api-u1-v1-douyin-billboard-fetch-hot-user-portrait-list"></a>
### `GET /api/u1/v1/douyin/billboard/fetch_hot_user_portrait_list`

- Summary: 获取作品点赞观众画像-仅限热门榜/Fetch work like audience portrait - hot list only
- Capabilities: trends / rankings / profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_hot_user_portrait_list_api_v1_douyin_billboard_fetch_hot_user_portrait_list_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取作品点赞观众画像
> ### 参数:
> - aweme_id: 作品id
> - option: 选项，1 手机价格分布 2 性别分布 3 年龄分布 4 地域分布-省份 5 地域分布-城市 6 城市等级 7 手机品牌分布
> ### 返回:
> - 作品点赞观众画像
>
> # [English]
> ### Purpose:
> - Get the work like audience portrait
> ### Parameters:
> - aweme_id: Work id
> - option: Option
>     - 1 Mobile price
>     - 2 Gender distribution
>     - 3 Age distribution
>     - 4 Regional distribution - province
>     - 5 Regional distribution - city
>     - 6 City level
>     - 7 Mobile brand distribution
> ### Return:
> - Work like audience portrait

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| aweme_id | query | string | Yes | 作品id | None | 7456035425539329340 | None |
| option | query | integer | No | 选项，1 手机价格分布 2 性别分布 3 年龄分布 4 地域分布-省份 5 地域分布-城市 6 城市等级 7 手机品牌分布 | 4 | None | None |

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
