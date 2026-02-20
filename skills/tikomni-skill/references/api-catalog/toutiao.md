# toutiao API Catalog

- operation_count: 7

| Method | Path | Summary | Required Params | Optional Params | Suggested Intent | Tags |
| --- | --- | --- | --- | --- | --- | --- |
| GET | /api/u1/v1/toutiao/app/get_article_info | 获取指定文章的信息/Get information of specified article | query:group_id | - | other | Toutiao-App-API |
| GET | /api/u1/v1/toutiao/app/get_comments | 获取指定作品的评论/Get comments of specified post | query:group_id, query:offset | - | comments | Toutiao-App-API |
| GET | /api/u1/v1/toutiao/app/get_user_id | 从头条用户主页获取用户user_id/Get user_id from user profile | query:user_profile_url | - | author_profile | Toutiao-App-API |
| GET | /api/u1/v1/toutiao/app/get_user_info | 获取指定用户的信息/Get information of specified user | query:user_id | - | author_profile | Toutiao-App-API |
| GET | /api/u1/v1/toutiao/app/get_video_info | 获取指定视频的信息/Get information of specified video | query:group_id | - | other | Toutiao-App-API |
| GET | /api/u1/v1/toutiao/web/get_article_info | 获取指定文章的信息/Get information of specified article | query:aweme_id | - | other | Toutiao-Web-API |
| GET | /api/u1/v1/toutiao/web/get_video_info | 获取指定视频的信息/Get information of specified video | query:aweme_id | - | other | Toutiao-Web-API |

