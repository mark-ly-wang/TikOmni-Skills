# Health-Check 路由详情

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 当前 tag 文件：`api-tags/health-check.md`
- 完整契约：[`api-contracts/health-check.md`](../api-contracts/health-check.md)
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T04:31:58+00:00`
- 路由数：`1`
- 常见能力：通用能力
- 默认认证：请求头 `Authorization` Bearer
- 常见入参：无
- 标签说明：**(服务器健康检查/Server Health Check)**

## 路由列表

### `GET /api/u1/v1/health/check`

- 摘要：检查服务器是否正确响应请求 / Check if the server responds to requests correctly
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`health_check_api_v1_health_check_get`
- 完整契约：[`api-contracts/health-check.md#get-api-u1-v1-health-check`](../api-contracts/health-check.md#get-api-u1-v1-health-check)

#### 参数

无

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`status`:string

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| status | string | 否 | 无 |
