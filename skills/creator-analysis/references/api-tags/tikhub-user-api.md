# TikHub-User-API Route Summary

- Back to index: [`api-capability-index.md`](../api-capability-index.md)
- Current tag file: `api-tags/tikhub-user-api.md`
- Full contract: [`api-contracts/tikhub-user-api.md`](../api-contracts/tikhub-user-api.md)
- Source: `https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- Fetched at: `2026-03-08T06:54:04+00:00`
- Route count: `6`
- Common capabilities: profiles / accounts
- Default auth: Header `Authorization` Bearer
- Common inputs: `endpoint`, `request_per_day`
- Tag description: **(TikHub用户数据接口/TikHub-User-API endpoints)**

## Routes

### `GET /api/u1/v1/tikhub/user/calculate_price`

- Summary: 计算价格/Calculate price
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `calculate_price_api_v1_tikhub_user_calculate_price_get`
- Full contract: [`api-contracts/tikhub-user-api.md#get-api-u1-v1-tikhub-user-calculate-price`](../api-contracts/tikhub-user-api.md#get-api-u1-v1-tikhub-user-calculate-price)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| endpoint | query | string | Yes | 请求的端点/Requested endpoint |
| request_per_day | query | integer | No | 每日请求次数/Request per day |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 |
| message | string | No | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | No | Support message \| 支持消息 |
| time | string | No | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL |

- Fields truncated: this layer shows only the first `12` rows.

### `GET /api/u1/v1/tikhub/user/get_all_endpoints_info`

- Summary: 获取所有端点信息/Get all endpoints information
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_all_endpoints_info_api_v1_tikhub_user_get_all_endpoints_info_get`
- Full contract: [`api-contracts/tikhub-user-api.md#get-api-u1-v1-tikhub-user-get-all-endpoints-info`](../api-contracts/tikhub-user-api.md#get-api-u1-v1-tikhub-user-get-all-endpoints-info)

#### Parameters

None

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 |
| message | string | No | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | No | Support message \| 支持消息 |
| time | string | No | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL |

- Fields truncated: this layer shows only the first `12` rows.

### `GET /api/u1/v1/tikhub/user/get_endpoint_info`

- Summary: 获取一个端点的信息/Get information of an endpoint
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_endpoint_info_api_v1_tikhub_user_get_endpoint_info_get`
- Full contract: [`api-contracts/tikhub-user-api.md#get-api-u1-v1-tikhub-user-get-endpoint-info`](../api-contracts/tikhub-user-api.md#get-api-u1-v1-tikhub-user-get-endpoint-info)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| endpoint | query | string | Yes | 请求的端点/Requested endpoint |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 |
| message | string | No | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | No | Support message \| 支持消息 |
| time | string | No | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL |

- Fields truncated: this layer shows only the first `12` rows.

### `GET /api/u1/v1/tikhub/user/get_tiered_discount_info`

- Summary: 获取阶梯式折扣百分比信息/Get tiered discount percentage information
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_tiered_discount_info_api_v1_tikhub_user_get_tiered_discount_info_get`
- Full contract: [`api-contracts/tikhub-user-api.md#get-api-u1-v1-tikhub-user-get-tiered-discount-info`](../api-contracts/tikhub-user-api.md#get-api-u1-v1-tikhub-user-get-tiered-discount-info)

#### Parameters

None

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 |
| message | string | No | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | No | Support message \| 支持消息 |
| time | string | No | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL |

- Fields truncated: this layer shows only the first `12` rows.

### `GET /api/u1/v1/tikhub/user/get_user_daily_usage`

- Summary: 获取用户每日使用情况/Get user daily usage
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_user_daily_usage_api_v1_tikhub_user_get_user_daily_usage_get`
- Full contract: [`api-contracts/tikhub-user-api.md#get-api-u1-v1-tikhub-user-get-user-daily-usage`](../api-contracts/tikhub-user-api.md#get-api-u1-v1-tikhub-user-get-user-daily-usage)

#### Parameters

None

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 |
| message | string | No | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | No | Support message \| 支持消息 |
| time | string | No | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL |

- Fields truncated: this layer shows only the first `12` rows.

### `GET /api/u1/v1/tikhub/user/get_user_info`

- Summary: 获取TikHub用户信息/Get TikHub user info
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_user_info_api_v1_tikhub_user_get_user_info_get`
- Full contract: [`api-contracts/tikhub-user-api.md#get-api-u1-v1-tikhub-user-get-user-info`](../api-contracts/tikhub-user-api.md#get-api-u1-v1-tikhub-user-get-user-info)

#### Parameters

None

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `router`:string, `api_key_data*`{`api_key_name*`:string, `api_key_scopes*`[Not declared], `created_at*`:string, `expires_at*`:string, `api_key_status*`:integer}, `user_data*`{`email*`:string, `balance*`:number, `free_credit*`:number, `email_verified*`:boolean, `account_disabled*`:boolean, `is_active*`:boolean}

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 |
| router | string | No | The endpoint that generated this response \| 生成此响应的端点 |
| api_key_data | object | Yes | None |
| api_key_data.api_key_name | string | Yes | None |
| api_key_data.api_key_scopes | array<Not declared> | Yes | None |
| api_key_data.created_at | string(date-time) | Yes | None |
| api_key_data.expires_at | string(date-time) | Yes | None |
| api_key_data.api_key_status | integer | Yes | None |
| user_data | object | Yes | None |
| user_data.email | string | Yes | None |
| user_data.balance | number | Yes | None |
| user_data.free_credit | number | Yes | None |

- Fields truncated: this layer shows only the first `12` rows.
