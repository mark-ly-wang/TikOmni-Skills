# iOS-Shortcut 完整契约

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 回到路由详情：[`api-tags/ios-shortcut.md`](../api-tags/ios-shortcut.md)
- 当前契约文件：`api-contracts/ios-shortcut.md`
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T04:31:58+00:00`
- 路由数：`1`
- 默认认证：请求头 `Authorization` Bearer
- 使用方式：当需要精确的认证说明、参数描述、默认值、示例或成功响应字段时，再读本文件。
- 标签说明：**(iOS快捷方式接口/iOS-Shortcut endpoints)**

## 路由契约

<a id="get-api-u1-v1-ios-shortcut-shortcut"></a>
### `GET /api/u1/v1/ios_shortcut/shortcut`

- 摘要：用于iOS快捷指令的版本更新信息/Version update information for iOS shortcuts
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_shortcut_api_v1_ios_shortcut_shortcut_get`

#### 参数

无

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`version*`:string, `update*`:string, `link*`:string, `link_en*`:string, `note*`:string, `note_en*`:string

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| version | string | 是 | 无 | 无 | 无 | 无 |
| update | string | 是 | 无 | 无 | 无 | 无 |
| link | string | 是 | 无 | 无 | 无 | 无 |
| link_en | string | 是 | 无 | 无 | 无 | 无 |
| note | string | 是 | 无 | 无 | 无 | 无 |
| note_en | string | 是 | 无 | 无 | 无 | 无 |
