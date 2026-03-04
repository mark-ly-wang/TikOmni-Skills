# 路由规则

## 1. 通用选型优先级

1. 同平台同意图多接口时，优先 `app > web_v2 > web`。
2. 核心字段缺失视为失败（即使 HTTP 2xx），进入 fallback。
3. 默认 fallback 链路上限为 3。

## 2. 主页提取固定路由

1. 抖音主页提取命中后，固定使用：
   - `GET /api/u1/v1/douyin/app/v3/handler_user_profile`
   - `GET /api/u1/v1/douyin/app/v3/fetch_user_post_videos`
2. 小红书主页提取命中后，固定使用：
   - `GET /api/u1/v1/xiaohongshu/web_v2/fetch_user_info_app`
   - `GET /api/u1/v1/xiaohongshu/web_v2/fetch_home_notes_app`

## 3. 默认参数

1. 抖音主页默认最新排序：`sort_type=0`。
2. 默认抓取边界：`limit=20`、`pages_max=50`。
3. 用户提供数量约束时，优先透传用户数量并做安全上限裁剪。

## 4. 单视频与其他任务

1. 单视频提取不走固定 playbook。
2. 单视频提取由 LLM 基于 `api-catalog` 自由路由，但必须记录路由与 fallback 轨迹。
