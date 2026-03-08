# TikHub-User-API Full Contract

- Back to index: [`api-capability-index.md`](../api-capability-index.md)
- Back to route summary: [`api-tags/tikhub-user-api.md`](../api-tags/tikhub-user-api.md)
- Current contract file: `api-contracts/tikhub-user-api.md`
- Source: `https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- Fetched at: `2026-03-08T06:54:04+00:00`
- Route count: `6`
- Default auth: Header `Authorization` Bearer
- Read this file only when you need precise auth notes, parameter descriptions, defaults, examples, or success-response fields.
- Tag description: **(TikHub用户数据接口/TikHub-User-API endpoints)**

## Route Contracts

<a id="get-api-u1-v1-tikhub-user-calculate-price"></a>
### `GET /api/u1/v1/tikhub/user/calculate_price`

- Summary: 计算价格/Calculate price
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `calculate_price_api_v1_tikhub_user_calculate_price_get`

#### Notes

> # [中文]
> ### 用途:
> - 根据用户输入的每日请求次数以及端点信息计算最终价格。
> ### 参数:
> - endpoint: 请求的端点，用于查询端点的原始请求单价
> - request_per_day: 每日请求次数，用于计算价格，将自动根据阶梯式计费的折扣百分比计算最终价格
> ### 计算公式:
> - 总成本 = ∑ (阶梯内请求次数 * 阶梯折后单价)
> - 其中，阶梯折后单价 = 基础价格 * (1 - 折扣)
> ### 详细计算步骤:
> 1. **初始化总成本**：
>    总成本=0
> 2. **遍历每个阶梯**：
>    * 对于每个阶梯，计算该阶梯内的请求次数。
>    * 计算该阶梯内的折后单价。
>    * 计算该阶梯内的总费用，并累加到总成本中。
>    * 更新剩余的请求次数。
> ### 数学表示:
> > 设有 𝑛 个阶梯，每个阶梯的参数为：
> * min_rpd𝑖: 第 𝑖 个阶梯的最小请求次数
> * max_rpd𝑖: 第 𝑖 个阶梯的最大请求次数
> * discount𝑖: 第 𝑖 个阶梯的折扣（百分比形式）
> * base_price：基础价格
> * request_per_day：每日请求次数
> > 那么，总成本的计算公式如下：
> - 总成本 = Σ𝑖=1𝑛（阶梯𝑖中的请求数量 * 阶梯𝑖中的折扣单价）
> - 其中，阶梯折扣单价 𝑖 = base_price * (1 - 折扣𝑖/100)
> - 该阶梯中的请求数 𝑖 = min(request_per_day - 累计付费请求数, max_rpd𝑖 - min_rpd𝑖)
> ### 示例
> > 假设有以下定价阶梯：
> * 第 1 阶梯：0 ≤ rpd < 1000，折扣 0%
> * 第 2 阶梯：1000 ≤ rpd < 5000，折扣 10%
> * 第 3 阶梯：5000 ≤ rpd < 10000，折扣 20%
> * 第 4 阶梯：10000 ≤ rpd < 20000，折扣 30%
> * 第 5 阶梯：20000 ≤ rpd < 30000，折扣 40%
> * 第 6 阶梯：30000 ≤ rpd，折扣 50%
> > 假设基础价格为 0.001 USD，每日请求次数为 12000，则计算过程如下：
> 1. **第 1 阶梯**（0 ≤ rpd < 1000）：
>    * 阶梯内请求次数=1000−0=1000
>    * 阶梯折后单价=0.001×(1−0/100)=0.001
>    * 总成本=1000×0.001=1
> 2. **第 2 阶梯**（1000 ≤ rpd < 5000）：
>    * 阶梯内请求次数=5000−1000=4000
>    * 阶梯折后单价=0.001×(1−10/100)=0.0009
>    * 总成本=4000×0.0009=3.6
> 3. **第 3 阶梯**（5000 ≤ rpd < 10000）：
>    * 阶梯内请求次数=10000−5000=5000
>    * 阶梯折后单价=0.001×(1−20/100)=0.0008
>    * 总成本=5000×0.0008=4
> 4. **第 4 阶梯**（10000 ≤ rpd < 20000）：
>    * 阶梯内请求次数=12000−10000=2000
>    * 阶梯折后单价=0.001×(1−30/100)=0.0007
>    * 总成本=2000×0.0007=1.4
> 5. **累加总成本**：
>    * 总成本=1+3.6+4+1.4=10
> ### 返回:
> - 端点uri
> - 每日请求次数
> - 端点原始请求单价
> - 总价格
> - 货币单位
> - 阶梯式计费的折扣百分比信息
>
> # [English]
> ### Purpose:
> - Calculate the final price based on the user's input of the number of daily requests and endpoint information.
> - Price calculation formula: Price = Number of daily requests * (Original request unit price of the endpoint * (1 - discount percentage of tiered billing))
> ### Parameters:
> - endpoint: Requested endpoint, used to query the original request unit price of the endpoint
> - request_per_day: Number of daily requests, used to calculate the price, the final price will be calculated automatically based on the discount percentage of the tiered billing
> ### Calculation formula:
> - Total cost = ∑ (Number of requests in the tier * Discounted unit price in the tier)
> - Where, Discounted unit price in the tier = Base price * (1 - Discount)
> ### Detailed calculation steps:
> 1. **Initialize the total cost**:
>      Total cost = 0
> 2. **Traverse each tier**:
>         * For each tier, calculate the number of requests in the tier.
>         * Calculate the discounted unit price in the tier.
>         * Calculate the total cost in the tier and add it to the total cost.
>         * Update the remaining number of requests.
> ### Mathematical representation:
> Suppose there are 𝑛 tiers, and the parameters of each tier are:
> * min_rpd𝑖: The minimum number of requests in the 𝑖-th tier
> * max_rpd𝑖: The maximum number of requests in the 𝑖-th tier
> * discount𝑖: The discount of the 𝑖-th tier (in percentage form)
> * base_price: Base price
> * request_per_day: Number of daily requests
> > Then, the formula for calculating the total cost is as follows:
> - Total cost = ∑𝑖=1𝑛(Number of requests in the tier 𝑖 * Discounted unit price in the tier 𝑖)
> - Where, Discounted unit price in the tier 𝑖 = base_price * (1 - discount𝑖/100)
> - Number of requests in the tier 𝑖 = min(request_per_day - accumulated number of paid requests, max_rpd𝑖 - min_rpd𝑖)
> ### Example
> Suppose there are the following pricing tiers:
> * Tier 1: 0 ≤ rpd < 1000, discount 0%
> * Tier 2: 1000 ≤ rpd < 5000, discount 10%
> * Tier 3: 5000 ≤ rpd < 10000, discount 20%
> * Tier 4: 10000 ≤ rpd < 20000, discount 30%
> * Tier 5: 20000 ≤ rpd < 30000, discount 40%
> * Tier 6: 30000 ≤ rpd, discount 50%
> > Suppose the base price is 0.001 USD and the number of daily requests is 12000, the calculation process is as follows:
> 1. **Tier 1** (0 ≤ rpd < 1000):
>      - Number of requests in the tier 1 = 1000 - 0 = 1000
>      - Discounted unit price in the tier 1 = 0.001 * (1 - 0/100) = 0.001
>      - Total cost 1 = 1000 * 0.001 = 1
> 2. **Tier 2** (1000 ≤ rpd < 5000):
>     - Number of requests in the tier 2 = 5000 - 1000 = 4000
>     - Discounted unit price in the tier 2 = 0.001 * (1 - 10/100) = 0.0009
>     - Total cost 2 = 4000 * 0.0009 = 3.6
> 3. **Tier 3** (5000 ≤ rpd < 10000):
>     - Number of requests in the tier 3 = 10000 - 5000 = 5000
>     - Discounted unit price in the tier 3 = 0.001 * (1 - 20/100) = 0.0008
>     - Total cost 3 = 5000 * 0.0008 = 4
> 4. **Tier 4** (10000 ≤ rpd < 20000):
>     - Number of requests in the tier 4 = 12000 - 10000 = 2000
>     - Discounted unit price in the tier 4 = 0.001 * (1 - 30/100) = 0.0007
>     - Total cost 4 = 2000 * 0.0007 = 1.4
> 5. **Accumulated total cost**:
>     - Total cost = 1 + 3.6 + 4 + 1.4 = 10
> ### Return:
> - Endpoint uri
> - Number of daily requests
> - Original request unit price of the endpoint
> - Total price
> - Currency unit
> - Discount percentage information of tiered billing

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| endpoint | query | string | Yes | 请求的端点/Requested endpoint | None | /api/v1/douyin/app/v1/fetch_one_video | None |
| request_per_day | query | integer | No | 每日请求次数/Request per day | 1 | 100000 | None |

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

<a id="get-api-u1-v1-tikhub-user-get-all-endpoints-info"></a>
### `GET /api/u1/v1/tikhub/user/get_all_endpoints_info`

- Summary: 获取所有端点信息/Get all endpoints information
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_all_endpoints_info_api_v1_tikhub_user_get_all_endpoints_info_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取所有端点信息
> ### 返回:
> - 所有端点信息
>
> # [English]
> ### Purpose:
> - Get all endpoints information
> ### Return:
> - All endpoints information

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

<a id="get-api-u1-v1-tikhub-user-get-endpoint-info"></a>
### `GET /api/u1/v1/tikhub/user/get_endpoint_info`

- Summary: 获取一个端点的信息/Get information of an endpoint
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_endpoint_info_api_v1_tikhub_user_get_endpoint_info_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取一个端点的信息
> ### 参数:
> - endpoint: 请求的端点
> ### 返回:
> - 端点信息
>
> # [English]
> ### Purpose:
> - Get information of an endpoint
> ### Parameters:
> - endpoint: Requested endpoint
> ### Return:
> - Endpoint information

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| endpoint | query | string | Yes | 请求的端点/Requested endpoint | None | /api/v1/douyin/app/v1/fetch_one_video | None |

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

<a id="get-api-u1-v1-tikhub-user-get-tiered-discount-info"></a>
### `GET /api/u1/v1/tikhub/user/get_tiered_discount_info`

- Summary: 获取阶梯式折扣百分比信息/Get tiered discount percentage information
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_tiered_discount_info_api_v1_tikhub_user_get_tiered_discount_info_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取阶梯式折扣百分比信息
> ### 返回:
> - 阶梯式折扣百分比信息
>
> # [English]
> ### Purpose:
> - Get tiered discount percentage information
> ### Return:
> - Tiered discount percentage information

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

<a id="get-api-u1-v1-tikhub-user-get-user-daily-usage"></a>
### `GET /api/u1/v1/tikhub/user/get_user_daily_usage`

- Summary: 获取用户每日使用情况/Get user daily usage
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_user_daily_usage_api_v1_tikhub_user_get_user_daily_usage_get`

#### Notes

> # [中文]
> ### 用途:
> - 请求头中携带API Key请求此端点可以查询当前账户每日使用情况。
> ### 参数:
> - 请求头：{'Authorization': 'Bearer API Key'}
> ### 返回:
> - 用户每日使用情况
>
> # [English]
> ### Purpose:
> - Request this endpoint with API Key in the header to query the current account daily usage.
> ### Parameters:
> - Headers: {'Authorization': 'Bearer API Key'}
> ### Return:
> - User daily usage

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

<a id="get-api-u1-v1-tikhub-user-get-user-info"></a>
### `GET /api/u1/v1/tikhub/user/get_user_info`

- Summary: 获取TikHub用户信息/Get TikHub user info
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_user_info_api_v1_tikhub_user_get_user_info_get`

#### Notes

> # [中文]
> ### 用途:
> - 请求头中携带API Key请求此端点可以查询当前账户信息。
> ### 参数:
> - 请求头：{'Authorization': 'Bearer API_KEY'}
> ### 返回:
> - 用户信息
>
> # [English]
> ### Purpose:
> - Request this endpoint with API Key in the header to query the current account information.
> ### Parameters:
> - Headers: {'Authorization': 'Bearer API_KEY'}
> ### Return:
> - User information
>
> # [示例/Example]
> ```python
> response = {
>       "code": 200,
>       "router": "/api/v1/tikhub/user/get_user_info",
>       "api_key_data": {
>         "api_key_name": "Develop Test",
>         "api_key_scopes": [
>           "/api/v1/tikhub/user/"
>         ],
>         "created_at": "2024-05-22T06:07:12.495520",
>         "expires_at": null,
>         "api_key_status": 1
>       },
>       "user_data": {
>         "email": "example@example.com",
>         "balance": 100,
>         "free_credit": 100,
>         "email_verified": true,
>         "account_disabled": false,
>         "is_active": true
>       }
>     }
> ```

#### Parameters

None

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `router`:string, `api_key_data*`{`api_key_name*`:string, `api_key_scopes*`[Not declared], `created_at*`:string, `expires_at*`:string, `api_key_status*`:integer}, `user_data*`{`email*`:string, `balance*`:number, `free_credit*`:number, `email_verified*`:boolean, `account_disabled*`:boolean, `is_active*`:boolean}

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 | 200 | None | None |
| router | string | No | The endpoint that generated this response \| 生成此响应的端点 | None | None | None |
| api_key_data | object | Yes | None | None | None | None |
| api_key_data.api_key_name | string | Yes | None | None | None | None |
| api_key_data.api_key_scopes | array<Not declared> | Yes | None | None | None | None |
| api_key_data.created_at | string(date-time) | Yes | None | None | None | None |
| api_key_data.expires_at | string(date-time) | Yes | None | None | None | None |
| api_key_data.api_key_status | integer | Yes | None | None | None | None |
| user_data | object | Yes | None | None | None | None |
| user_data.email | string | Yes | None | None | None | None |
| user_data.balance | number | Yes | None | None | None | None |
| user_data.free_credit | number | Yes | None | None | None | None |
| user_data.email_verified | boolean | Yes | None | None | None | None |
| user_data.account_disabled | boolean | Yes | None | None | None | None |
| user_data.is_active | boolean | Yes | None | None | None | None |
