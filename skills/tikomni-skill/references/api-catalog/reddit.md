# reddit API Catalog

- operation_count: 24

| Method | Path | Summary | Required Params | Optional Params | Suggested Intent | Tags |
| --- | --- | --- | --- | --- | --- | --- |
| GET | /api/u1/v1/reddit/app/check_subreddit_muted | 检查版块是否静音/Check if Subreddit is Muted | query:subreddit_id | query:need_format | other | Reddit-APP-API |
| GET | /api/u1/v1/reddit/app/fetch_comment_replies | 获取Reddit APP评论回复（二级评论）/Fetch Reddit APP Comment Replies (Sub-comments) | query:post_id, query:cursor | query:sort_type, query:need_format | comments | Reddit-APP-API |
| GET | /api/u1/v1/reddit/app/fetch_community_highlights | 获取Reddit APP社区亮点/Fetch Reddit APP Community Highlights | query:subreddit_id | query:need_format | other | Reddit-APP-API |
| GET | /api/u1/v1/reddit/app/fetch_dynamic_search | 获取Reddit APP动态搜索结果/Fetch Reddit APP Dynamic Search Results | query:query | query:search_type, query:sort, query:time_range, query:safe_search, query:allow_nsfw, query:after, query:need_format | search | Reddit-APP-API |
| GET | /api/u1/v1/reddit/app/fetch_games_feed | 获取Reddit APP游戏推荐内容/Fetch Reddit APP Games Feed | - | query:sort, query:time, query:after, query:need_format | other | Reddit-APP-API |
| GET | /api/u1/v1/reddit/app/fetch_home_feed | 获取Reddit APP首页推荐内容/Fetch Reddit APP Home Feed | - | query:sort, query:filter_posts, query:after, query:need_format | home_posts | Reddit-APP-API |
| GET | /api/u1/v1/reddit/app/fetch_news_feed | 获取Reddit APP资讯推荐内容/Fetch Reddit APP News Feed | - | query:subtopic_ids, query:after, query:need_format | other | Reddit-APP-API |
| GET | /api/u1/v1/reddit/app/fetch_popular_feed | 获取Reddit APP流行推荐内容/Fetch Reddit APP Popular Feed | - | query:sort, query:time, query:filter_posts, query:after, query:need_format | other | Reddit-APP-API |
| GET | /api/u1/v1/reddit/app/fetch_post_comments | 获取Reddit APP帖子评论/Fetch Reddit APP Post Comments | query:post_id | query:sort_type, query:after, query:need_format | comments | Reddit-APP-API |
| GET | /api/u1/v1/reddit/app/fetch_post_details | 获取单个Reddit帖子详情/Fetch Single Reddit Post Details | query:post_id | query:include_comment_id, query:comment_id, query:need_format | single_post | Reddit-APP-API |
| GET | /api/u1/v1/reddit/app/fetch_post_details_batch | 批量获取Reddit帖子详情(最多5条)/Fetch Reddit Post Details in Batch (Max 5) | query:post_ids | query:include_comment_id, query:comment_id, query:need_format | single_post | Reddit-APP-API |
| GET | /api/u1/v1/reddit/app/fetch_post_details_batch_large | 大批量获取Reddit帖子详情(最多30条)/Fetch Reddit Post Details in Large Batch (Max 30) | query:post_ids | query:include_comment_id, query:comment_id, query:need_format | single_post | Reddit-APP-API |
| GET | /api/u1/v1/reddit/app/fetch_search_typeahead | 获取Reddit APP搜索自动补全建议/Fetch Reddit APP Search Typeahead Suggestions | query:query | query:safe_search, query:allow_nsfw, query:need_format | search | Reddit-APP-API |
| GET | /api/u1/v1/reddit/app/fetch_subreddit_feed | 获取Reddit APP版块Feed内容/Fetch Reddit APP Subreddit Feed | query:subreddit_name | query:sort, query:filter_posts, query:after, query:need_format | other | Reddit-APP-API |
| GET | /api/u1/v1/reddit/app/fetch_subreddit_info | 获取Reddit APP版块信息/Fetch Reddit APP Subreddit Info | - | query:subreddit_name, query:need_format | other | Reddit-APP-API |
| GET | /api/u1/v1/reddit/app/fetch_subreddit_post_channels | 获取Reddit APP版块帖子频道信息/Fetch Reddit APP Subreddit Post Channels | - | query:subreddit_name, query:sort, query:range, query:need_format | other | Reddit-APP-API |
| GET | /api/u1/v1/reddit/app/fetch_subreddit_settings | 获取Reddit APP版块设置/Fetch Reddit APP Subreddit Settings | query:subreddit_id | query:need_format | other | Reddit-APP-API |
| GET | /api/u1/v1/reddit/app/fetch_subreddit_style | 获取Reddit APP版块规则样式信息/Fetch Reddit APP Subreddit Rules and Style Info | - | query:subreddit_name, query:need_format | other | Reddit-APP-API |
| GET | /api/u1/v1/reddit/app/fetch_trending_searches | 获取Reddit APP今日热门搜索/Fetch Reddit APP Trending Searches | - | query:need_format | search | Reddit-APP-API |
| GET | /api/u1/v1/reddit/app/fetch_user_active_subreddits | 获取用户活跃的社区列表/Fetch User's Active Subreddits | query:username | query:need_format | other | Reddit-APP-API |
| GET | /api/u1/v1/reddit/app/fetch_user_comments | 获取用户评论列表/Fetch User Comments | query:username | query:sort, query:page_size, query:after, query:need_format | comments | Reddit-APP-API |
| GET | /api/u1/v1/reddit/app/fetch_user_posts | 获取用户发布的帖子列表/Fetch User Posts | query:username | query:sort, query:after, query:need_format | other | Reddit-APP-API |
| GET | /api/u1/v1/reddit/app/fetch_user_profile | 获取Reddit APP用户资料信息/Fetch Reddit APP User Profile | query:username | query:need_format | author_profile | Reddit-APP-API |
| GET | /api/u1/v1/reddit/app/fetch_user_trophies | 获取用户公开奖杯/Fetch User Public Trophies | query:username | query:need_format | other | Reddit-APP-API |

