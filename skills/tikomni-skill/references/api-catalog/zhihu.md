# zhihu API Catalog

- operation_count: 32

| Method | Path | Summary | Required Params | Optional Params | Suggested Intent | Tags |
| --- | --- | --- | --- | --- | --- | --- |
| GET | /api/u1/v1/zhihu/web/fetch_ai_search | 获取知乎AI搜索/Get Zhihu AI Search | query:message_content | - | search | Zhihu-Web-API |
| GET | /api/u1/v1/zhihu/web/fetch_ai_search_result | 获取知乎AI搜索结果/Get Zhihu AI Search Result | query:message_id | - | search | Zhihu-Web-API |
| GET | /api/u1/v1/zhihu/web/fetch_article_search_v3 | 获取知乎文章搜索V3/Get Zhihu Article Search V3 | query:keyword | query:offset, query:limit, query:show_all_topics, query:search_source, query:search_hash_id, query:vertical, query:sort, query:time_interval, ...(+1) | search | Zhihu-Web-API |
| GET | /api/u1/v1/zhihu/web/fetch_column_article_detail | 获取知乎专栏文章详情/Get Zhihu Column Article Detail | query:article_id | - | single_post | Zhihu-Web-API |
| GET | /api/u1/v1/zhihu/web/fetch_column_articles | 获取知乎专栏文章列表/Get Zhihu Column Articles | query:column_id | query:limit, query:offset | other | Zhihu-Web-API |
| GET | /api/u1/v1/zhihu/web/fetch_column_comment_config | 获取知乎专栏评论区配置/Get Zhihu Column Comment Config | query:article_id | - | comments | Zhihu-Web-API |
| GET | /api/u1/v1/zhihu/web/fetch_column_recommend | 获取知乎相似专栏推荐/Get Zhihu Similar Column Recommend | query:article_id | query:limit, query:offset | other | Zhihu-Web-API |
| GET | /api/u1/v1/zhihu/web/fetch_column_relationship | 获取知乎专栏文章互动关系/Get Zhihu Column Article Relationship | query:article_id | - | other | Zhihu-Web-API |
| GET | /api/u1/v1/zhihu/web/fetch_column_search_v3 | 获取知乎专栏搜索V3/Get Zhihu Column Search V3 | query:keyword | query:offset, query:limit, query:search_hash_id | search | Zhihu-Web-API |
| GET | /api/u1/v1/zhihu/web/fetch_comment_v5 | 获取知乎评论区V5/Get Zhihu Comment V5 | query:answer_id | query:order_by, query:limit, query:offset | comments | Zhihu-Web-API |
| GET | /api/u1/v1/zhihu/web/fetch_ebook_search_v3 | 获取知乎电子书搜索V3/Get Zhihu Ebook Search V3 | query:keyword | query:offset, query:limit, query:search_hash_id | search | Zhihu-Web-API |
| GET | /api/u1/v1/zhihu/web/fetch_hot_list | 获取知乎首页热榜/Get Zhihu Hot List | - | query:limit, query:desktop | trend | Zhihu-Web-API |
| GET | /api/u1/v1/zhihu/web/fetch_hot_recommend | 获取知乎首页推荐/Get Zhihu Hot Recommend | - | query:offset, query:page_number, query:session_token | trend | Zhihu-Web-API |
| GET | /api/u1/v1/zhihu/web/fetch_preset_search | 获取知乎搜索预设词/Get Zhihu Preset Search | - | - | search | Zhihu-Web-API |
| GET | /api/u1/v1/zhihu/web/fetch_question_answers | 获取知乎问题回答列表/Get Zhihu Question Answers | query:question_id | query:cursor, query:limit, query:offset, query:order, query:session_id | other | Zhihu-Web-API |
| GET | /api/u1/v1/zhihu/web/fetch_recommend_followees | 获取知乎推荐关注列表/Get Zhihu Recommend Followees | - | - | other | Zhihu-Web-API |
| GET | /api/u1/v1/zhihu/web/fetch_salt_search_v3 | 获取知乎盐选内容搜索V3/Get Zhihu Salt Search V3 | query:keyword | query:offset, query:limit, query:search_hash_id | search | Zhihu-Web-API |
| POST | /api/u1/v1/zhihu/web/fetch_scholar_search_v3 | 获取知乎论文搜索V3/Get Zhihu Scholar Search V3 | query:keyword | query:offset, query:limit, body | search | Zhihu-Web-API |
| GET | /api/u1/v1/zhihu/web/fetch_search_recommend | 获取知乎搜索发现/Get Zhihu Search Recommend | - | - | search | Zhihu-Web-API |
| GET | /api/u1/v1/zhihu/web/fetch_search_suggest | 知乎搜索预测词/Get Zhihu Search Suggest | query:keyword | - | search | Zhihu-Web-API |
| GET | /api/u1/v1/zhihu/web/fetch_sub_comment_v5 | 获取知乎子评论区V5/Get Zhihu Sub Comment V5 | query:comment_id | query:order_by, query:limit, query:offset | comments | Zhihu-Web-API |
| GET | /api/u1/v1/zhihu/web/fetch_topic_search_v3 | 获取知乎话题搜索V3/Get Zhihu Topic Search V3 | query:keyword | query:offset, query:limit | search | Zhihu-Web-API |
| GET | /api/u1/v1/zhihu/web/fetch_user_follow_collections | 获取知乎用户关注的收藏/Get Zhihu User Follow Collections | query:user_url_token | query:offset, query:limit | other | Zhihu-Web-API |
| GET | /api/u1/v1/zhihu/web/fetch_user_follow_columns | 获取知乎用户订阅的专栏/Get Zhihu User Columns | query:user_url_token | query:offset, query:limit | other | Zhihu-Web-API |
| GET | /api/u1/v1/zhihu/web/fetch_user_follow_questions | 获取知乎用户关注的问题/Get Zhihu User Follow Questions | query:user_url_token | query:offset, query:limit | other | Zhihu-Web-API |
| GET | /api/u1/v1/zhihu/web/fetch_user_follow_topics | 获取知乎用户关注的话题/Get Zhihu User Follow Topics | query:user_url_token | query:offset, query:limit | other | Zhihu-Web-API |
| GET | /api/u1/v1/zhihu/web/fetch_user_followees | 获取知乎用户关注列表/Get Zhihu User Following | query:user_url_token | query:offset, query:limit | other | Zhihu-Web-API |
| GET | /api/u1/v1/zhihu/web/fetch_user_followers | 获取知乎用户粉丝列表/Get Zhihu User Followers | query:user_url_token | query:offset, query:limit | other | Zhihu-Web-API |
| GET | /api/u1/v1/zhihu/web/fetch_user_info | 获取知乎用户信息/Get Zhihu User Info | query:user_url_token | - | author_profile | Zhihu-Web-API |
| GET | /api/u1/v1/zhihu/web/fetch_user_search_v3 | 获取知乎用户搜索V3/Get Zhihu User Search V3 | query:keyword | query:offset, query:limit | search | Zhihu-Web-API |
| GET | /api/u1/v1/zhihu/web/fetch_video_list | 获取知乎首页视频榜/Get Zhihu Video List | - | query:offset, query:limit | other | Zhihu-Web-API |
| GET | /api/u1/v1/zhihu/web/fetch_video_search_v3 | 获取知乎视频搜索V3/Get Zhihu Video Search V3 | query:keyword | query:limit, query:offset, query:search_hash_id | search | Zhihu-Web-API |

