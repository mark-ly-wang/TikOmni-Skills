# iOS-Shortcut Full Contract

- Back to index: [`api-capability-index.md`](../api-capability-index.md)
- Back to route summary: [`api-tags/ios-shortcut.md`](../api-tags/ios-shortcut.md)
- Current contract file: `api-contracts/ios-shortcut.md`
- Source: `https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- Fetched at: `2026-03-08T06:54:04+00:00`
- Route count: `1`
- Default auth: Header `Authorization` Bearer
- Read this file only when you need precise auth notes, parameter descriptions, defaults, examples, or success-response fields.
- Tag description: **(iOS快捷方式接口/iOS-Shortcut endpoints)**

## Route Contracts

<a id="get-api-u1-v1-ios-shortcut-shortcut"></a>
### `GET /api/u1/v1/ios_shortcut/shortcut`

- Summary: 用于iOS快捷指令的版本更新信息/Version update information for iOS shortcuts
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_shortcut_api_v1_ios_shortcut_shortcut_get`

#### Parameters

None

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `version*`:string, `update*`:string, `link*`:string, `link_en*`:string, `note*`:string, `note_en*`:string

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| version | string | Yes | None | None | None | None |
| update | string | Yes | None | None | None | None |
| link | string | Yes | None | None | None | None |
| link_en | string | Yes | None | None | None | None |
| note | string | Yes | None | None | None | None |
| note_en | string | Yes | None | None | None | None |
