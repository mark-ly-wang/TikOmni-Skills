# sora2 API Catalog

- operation_count: 17

| Method | Path | Summary | Required Params | Optional Params | Suggested Intent | Tags |
| --- | --- | --- | --- | --- | --- | --- |
| POST | /api/u1/v1/sora2/create_video | 文本/图片生成视频/Create video from text or image | body:prompt | body:orientation, body:media_id | other | Sora2-API |
| GET | /api/u1/v1/sora2/get_cameo_leaderboard | 获取 Cameo 出镜秀达人排行榜/Fetch Cameo leaderboard | - | query:cursor | other | Sora2-API |
| GET | /api/u1/v1/sora2/get_comment_replies | 获取评论的回复/Fetch comment replies | query:comment_id | query:cursor | comments | Sora2-API |
| GET | /api/u1/v1/sora2/get_feed | 获取Feed流（热门/推荐视频）/Fetch feed | - | query:cursor, query:eager_views | other | Sora2-API |
| GET | /api/u1/v1/sora2/get_post_comments | 获取作品一级评论/Fetch post comments | query:post_id | query:cursor | comments | Sora2-API |
| GET | /api/u1/v1/sora2/get_post_detail | 获取单一作品详情/Fetch single post detail | - | query:post_id, query:post_url | single_post | Sora2-API |
| GET | /api/u1/v1/sora2/get_post_remix_list | 获取作品的 Remix 列表/Fetch post remix list | - | query:post_id, query:post_url, query:cursor | other | Sora2-API |
| GET | /api/u1/v1/sora2/get_task_detail | 获取任务生成的作品详情（无水印版本）/Get task-generated post detail (watermark-free) | - | query:task_id, query:generation_id | single_post | Sora2-API |
| GET | /api/u1/v1/sora2/get_task_status | 查询任务状态/Get task status | query:task_id | - | other | Sora2-API |
| GET | /api/u1/v1/sora2/get_user_cameo_appearances | 获取用户Cameo出镜秀列表/Fetch user cameo appearances | query:user_id | query:cursor | other | Sora2-API |
| GET | /api/u1/v1/sora2/get_user_followers | 获取用户粉丝列表/Fetch user followers | query:user_id | query:cursor | other | Sora2-API |
| GET | /api/u1/v1/sora2/get_user_following | 获取用户关注列表/Fetch user following | query:user_id | query:cursor | other | Sora2-API |
| GET | /api/u1/v1/sora2/get_user_posts | 获取用户发布的帖子列表/Fetch user posts | query:user_id | query:cursor | other | Sora2-API |
| GET | /api/u1/v1/sora2/get_user_profile | 获取用户信息档案/Fetch user profile | query:user_id | - | author_profile | Sora2-API |
| GET | /api/u1/v1/sora2/get_video_download_info | 获取无水印视频下载信息/Fetch none watermark video download info | - | query:post_id, query:post_url | other | Sora2-API |
| GET | /api/u1/v1/sora2/search_users | 搜索用户/Search users | query:username | - | search | Sora2-API |
| POST | /api/u1/v1/sora2/upload_image | 上传图片获取media_id/Upload image to get media_id | body:file | - | other | Sora2-API |

