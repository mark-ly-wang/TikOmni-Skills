# Media-Ingest-API 路由详情

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 当前 tag 文件：`api-tags/media-ingest-api.md`
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T03:50:06+00:00`
- 路由数：`2`
- 常见能力：媒体上传/公网URL
- 常见入参：`provider`, `file_name`, `content_type`, `size_bytes`, `upload_id`
- 标签说明：**(媒体中转接口 / media ingest endpoints)**
- 相关组合 guide：[`service-guides/asr-u2-u3-fallback.md`](../service-guides/asr-u2-u3-fallback.md)

## 路由列表

### `POST /api/u3/v1/uploads`

- 能力：媒体上传/公网URL
- 入参：无
- 请求体：application/json: `provider*`:string, `file_name*`:string, `content_type*`:string, `size_bytes*`:integer
- 成功响应：200 application/json: `time*`:string, `time_stamp*`:integer, `time_zone*`:string, `params*`{`provider*`:string, `file_name*`:string, `content_type*`:string, `size_bytes*`:integer}, `data*`{`upload_id*`:string, `provider*`:string, `upload_method*`:string, `upload_url*`:string, `upload_headers*`{...}, `upload_expires_at*`:string, `file_ttl_seconds*`:integer}, `code*`:integer, `request_id*`:string, `message*`:string, ...
- operationId：`u3CreateUpload`

### `POST /api/u3/v1/uploads/{upload_id}/complete`

- 能力：媒体上传/公网URL
- 入参：path: `upload_id*`
- 请求体：application/json: 动态对象
- 成功响应：200 application/json: `time*`:string, `time_stamp*`:integer, `time_zone*`:string, `params*`{`upload_id*`:string}, `data*`{`upload_id*`:string, `provider*`:string, `file_url*`:string, `file_expires_at*`:string}, `code*`:integer, `request_id*`:string, `message*`:string, ...
- operationId：`u3CompleteUpload`
