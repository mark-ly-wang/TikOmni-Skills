# twitter API Catalog

- operation_count: 13

| Method | Path | Summary | Required Params | Optional Params | Suggested Intent | Tags |
| --- | --- | --- | --- | --- | --- | --- |
| GET | /api/u1/v1/twitter/web/fetch_latest_post_comments | 获取最新的推文评论/Get the latest tweet comments | query:tweet_id | query:cursor | comments | Twitter-Web-API |
| GET | /api/u1/v1/twitter/web/fetch_post_comments | 获取评论/Get comments | query:tweet_id | query:cursor | comments | Twitter-Web-API |
| GET | /api/u1/v1/twitter/web/fetch_retweet_user_list | 转推用户列表/ReTweet User list | query:tweet_id | query:cursor | other | Twitter-Web-API |
| GET | /api/u1/v1/twitter/web/fetch_search_timeline | 搜索/Search | query:keyword | query:search_type, query:cursor | home_posts | Twitter-Web-API |
| GET | /api/u1/v1/twitter/web/fetch_trending | 趋势/Trending | - | query:country | trend | Twitter-Web-API |
| GET | /api/u1/v1/twitter/web/fetch_tweet_detail | 获取单个推文数据/Get single tweet data | query:tweet_id | - | single_post | Twitter-Web-API |
| GET | /api/u1/v1/twitter/web/fetch_user_followers | 用户粉丝/User Followers | query:screen_name | query:cursor | other | Twitter-Web-API |
| GET | /api/u1/v1/twitter/web/fetch_user_followings | 用户关注/User Followings | query:screen_name | query:cursor | other | Twitter-Web-API |
| GET | /api/u1/v1/twitter/web/fetch_user_highlights_tweets | 获取用户高光推文/Get user highlights tweets | query:userId | query:count, query:cursor | other | Twitter-Web-API |
| GET | /api/u1/v1/twitter/web/fetch_user_media | 获取用户媒体/Get user media | query:screen_name | query:rest_id, query:cursor | other | Twitter-Web-API |
| GET | /api/u1/v1/twitter/web/fetch_user_post_tweet | 获取用户发帖/Get user post | - | query:screen_name, query:rest_id, query:cursor | other | Twitter-Web-API |
| GET | /api/u1/v1/twitter/web/fetch_user_profile | 获取用户资料/Get user profile | - | query:screen_name, query:rest_id | author_profile | Twitter-Web-API |
| GET | /api/u1/v1/twitter/web/fetch_user_tweet_replies | 获取用户推文回复/Get user tweet replies | query:screen_name | query:cursor | other | Twitter-Web-API |

