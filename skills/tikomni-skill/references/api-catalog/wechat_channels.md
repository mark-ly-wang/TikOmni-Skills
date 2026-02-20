# wechat_channels API Catalog

- operation_count: 9

| Method | Path | Summary | Required Params | Optional Params | Suggested Intent | Tags |
| --- | --- | --- | --- | --- | --- | --- |
| GET | /api/u1/v1/wechat_channels/fetch_comments | 微信视频号评论/WeChat Channels Comments | query:id | query:lastBuffer, query:comment_id | comments | WeChat-Channels-API |
| GET | /api/u1/v1/wechat_channels/fetch_default_search | 微信视频号默认搜索/WeChat Channels Default Search | query:keywords | query:session_buffer | search | WeChat-Channels-API |
| GET | /api/u1/v1/wechat_channels/fetch_home_page | 微信视频号主页/WeChat Channels Home Page | query:username | query:last_buffer | home_posts | WeChat-Channels-API |
| GET | /api/u1/v1/wechat_channels/fetch_hot_words | 微信视频号热门话题/WeChat Channels Hot Topics | - | - | trend | WeChat-Channels-API |
| GET | /api/u1/v1/wechat_channels/fetch_live_history | 微信视频号直播回放/WeChat Channels Live History | query:username | - | other | WeChat-Channels-API |
| GET | /api/u1/v1/wechat_channels/fetch_search_latest | 微信视频号搜索最新视频/WeChat Channels Search Latest Videos | query:keywords | - | search | WeChat-Channels-API |
| GET | /api/u1/v1/wechat_channels/fetch_search_ordinary | 微信视频号综合搜索/WeChat Channels Comprehensive Search | query:keywords | - | search | WeChat-Channels-API |
| GET | /api/u1/v1/wechat_channels/fetch_user_search | 微信视频号用户搜索/WeChat Channels User Search | query:keywords | query:page | search | WeChat-Channels-API |
| GET | /api/u1/v1/wechat_channels/fetch_video_detail | 微信视频号视频详情/WeChat Channels Video Detail | - | query:id, query:exportId | single_post | WeChat-Channels-API |

