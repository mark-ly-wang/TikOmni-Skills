# 清洗规则

## 1. 目标

统一输出为 `raw + normalized`，降低上游结构波动对下游流程的影响。

## 2. 包络兼容

1. 兼容 `payload.data` 结构。
2. 兼容 Tikomni 在非 2xx 下将 detail 字段拉平到顶层的结构。
3. 兼容 TikHub 风格包络：`code/message/request_id/router/data`。

## 3. 统一字段建议

```json
{
  "meta": {
    "platform": "",
    "intent": "",
    "endpoint": "",
    "request_id": ""
  },
  "status": {
    "http_status": 200,
    "code": 200,
    "message": "",
    "message_zh": ""
  },
  "normalized": {
    "author": {},
    "items": [],
    "text": "",
    "raw_data": {}
  }
}
```

## 4. 主页提取关键字段

1. 抖音作者：`sec_uid`、`unique_id`、`nickname`、`signature`、`follower_count`。
2. 抖音作品：`platform_work_id`、`title/desc`、`duration_ms`、`video_down_url`、互动数据。
3. 小红书作者：`user_id/red_id/xsec_token`、`nickname`、`fans/follows`。
4. 小红书作品：`note_id`、`title/desc`、`subtitle_url`、`duration_ms`、互动数据。
