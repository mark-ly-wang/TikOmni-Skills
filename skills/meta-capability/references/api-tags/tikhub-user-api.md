# TikHub-User-API 路由详情

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 当前 tag 文件：`api-tags/tikhub-user-api.md`
- 完整契约：[`api-contracts/tikhub-user-api.md`](../api-contracts/tikhub-user-api.md)
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T04:31:58+00:00`
- 路由数：`6`
- 常见能力：主页/账号
- 默认认证：请求头 `Authorization` Bearer
- 常见入参：`endpoint`, `request_per_day`
- 标签说明：**(TikHub用户数据接口/TikHub-User-API endpoints)**

## 路由列表

### `GET /api/u1/v1/tikhub/user/calculate_price`

- 摘要：计算价格/Calculate price
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`calculate_price_api_v1_tikhub_user_calculate_price_get`
- 完整契约：[`api-contracts/tikhub-user-api.md#get-api-u1-v1-tikhub-user-calculate-price`](../api-contracts/tikhub-user-api.md#get-api-u1-v1-tikhub-user-calculate-price)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| endpoint | query | string | 是 | 请求的端点/Requested endpoint |
| request_per_day | query | integer | 否 | 每日请求次数/Request per day |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | 否 | Support message \| 支持消息 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL |

- 字段已截断：当前层仅展示前 `12` 行。

### `GET /api/u1/v1/tikhub/user/get_all_endpoints_info`

- 摘要：获取所有端点信息/Get all endpoints information
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_all_endpoints_info_api_v1_tikhub_user_get_all_endpoints_info_get`
- 完整契约：[`api-contracts/tikhub-user-api.md#get-api-u1-v1-tikhub-user-get-all-endpoints-info`](../api-contracts/tikhub-user-api.md#get-api-u1-v1-tikhub-user-get-all-endpoints-info)

#### 参数

无

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | 否 | Support message \| 支持消息 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL |

- 字段已截断：当前层仅展示前 `12` 行。

### `GET /api/u1/v1/tikhub/user/get_endpoint_info`

- 摘要：获取一个端点的信息/Get information of an endpoint
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_endpoint_info_api_v1_tikhub_user_get_endpoint_info_get`
- 完整契约：[`api-contracts/tikhub-user-api.md#get-api-u1-v1-tikhub-user-get-endpoint-info`](../api-contracts/tikhub-user-api.md#get-api-u1-v1-tikhub-user-get-endpoint-info)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| endpoint | query | string | 是 | 请求的端点/Requested endpoint |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | 否 | Support message \| 支持消息 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL |

- 字段已截断：当前层仅展示前 `12` 行。

### `GET /api/u1/v1/tikhub/user/get_tiered_discount_info`

- 摘要：获取阶梯式折扣百分比信息/Get tiered discount percentage information
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_tiered_discount_info_api_v1_tikhub_user_get_tiered_discount_info_get`
- 完整契约：[`api-contracts/tikhub-user-api.md#get-api-u1-v1-tikhub-user-get-tiered-discount-info`](../api-contracts/tikhub-user-api.md#get-api-u1-v1-tikhub-user-get-tiered-discount-info)

#### 参数

无

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | 否 | Support message \| 支持消息 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL |

- 字段已截断：当前层仅展示前 `12` 行。

### `GET /api/u1/v1/tikhub/user/get_user_daily_usage`

- 摘要：获取用户每日使用情况/Get user daily usage
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_user_daily_usage_api_v1_tikhub_user_get_user_daily_usage_get`
- 完整契约：[`api-contracts/tikhub-user-api.md#get-api-u1-v1-tikhub-user-get-user-daily-usage`](../api-contracts/tikhub-user-api.md#get-api-u1-v1-tikhub-user-get-user-daily-usage)

#### 参数

无

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | 否 | Support message \| 支持消息 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL |

- 字段已截断：当前层仅展示前 `12` 行。

### `GET /api/u1/v1/tikhub/user/get_user_info`

- 摘要：获取TikHub用户信息/Get TikHub user info
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_user_info_api_v1_tikhub_user_get_user_info_get`
- 完整契约：[`api-contracts/tikhub-user-api.md#get-api-u1-v1-tikhub-user-get-user-info`](../api-contracts/tikhub-user-api.md#get-api-u1-v1-tikhub-user-get-user-info)

#### 参数

无

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `router`:string, `api_key_data*`{`api_key_name*`:string, `api_key_scopes*`[未声明], `created_at*`:string, `expires_at*`:string, `api_key_status*`:integer}, `user_data*`{`email*`:string, `balance*`:number, `free_credit*`:number, `email_verified*`:boolean, `account_disabled*`:boolean, `is_active*`:boolean}

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 |
| router | string | 否 | The endpoint that generated this response \| 生成此响应的端点 |
| api_key_data | object | 是 | 无 |
| api_key_data.api_key_name | string | 是 | 无 |
| api_key_data.api_key_scopes | array<未声明> | 是 | 无 |
| api_key_data.created_at | string(date-time) | 是 | 无 |
| api_key_data.expires_at | string(date-time) | 是 | 无 |
| api_key_data.api_key_status | integer | 是 | 无 |
| user_data | object | 是 | 无 |
| user_data.email | string | 是 | 无 |
| user_data.balance | number | 是 | 无 |
| user_data.free_credit | number | 是 | 无 |

- 字段已截断：当前层仅展示前 `12` 行。
