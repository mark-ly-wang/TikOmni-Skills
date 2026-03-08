# Health-Check Route Summary

- Back to index: [`api-capability-index.md`](../api-capability-index.md)
- Current tag file: `api-tags/health-check.md`
- Full contract: [`api-contracts/health-check.md`](../api-contracts/health-check.md)
- Source: `https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- Fetched at: `2026-03-08T06:54:04+00:00`
- Route count: `1`
- Common capabilities: general
- Default auth: Header `Authorization` Bearer
- Common inputs: None
- Tag description: **(服务器健康检查/Server Health Check)**

## Routes

### `GET /api/u1/v1/health/check`

- Summary: 检查服务器是否正确响应请求 / Check if the server responds to requests correctly
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `health_check_api_v1_health_check_get`
- Full contract: [`api-contracts/health-check.md#get-api-u1-v1-health-check`](../api-contracts/health-check.md#get-api-u1-v1-health-check)

#### Parameters

None

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `status`:string

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| status | string | No | None |
