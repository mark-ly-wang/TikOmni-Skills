# xiaohongshu API Catalog

- operation_count: 68

| Method | Path | Summary | Required Params | Optional Params | Suggested Intent | Tags |
| --- | --- | --- | --- | --- | --- | --- |
| GET | /api/u1/v1/xiaohongshu/app_v2/get_creator_hot_inspiration_feed | 获取创作者热点灵感列表/Get creator hot inspiration feed | header:authorization | query:cursor | trend | Xiaohongshu-App-V2-API |
| GET | /api/u1/v1/xiaohongshu/app_v2/get_creator_inspiration_feed | 获取创作者推荐灵感列表/Get creator inspiration feed | header:authorization | query:cursor, query:tab, query:source | other | Xiaohongshu-App-V2-API |
| GET | /api/u1/v1/xiaohongshu/app_v2/get_image_note_detail | 获取图文笔记详情/Get image note detail | header:authorization | query:note_id, query:share_text | single_post | Xiaohongshu-App-V2-API |
| GET | /api/u1/v1/xiaohongshu/app_v2/get_mixed_note_detail | 获取首页推荐流笔记详情/Get mixed note detail from feed | header:authorization | query:note_id, query:share_text | single_post | Xiaohongshu-App-V2-API |
| GET | /api/u1/v1/xiaohongshu/app_v2/get_note_comments | 获取笔记评论列表/Get note comments | header:authorization | query:note_id, query:share_text, query:cursor, query:index, query:sort_strategy | comments | Xiaohongshu-App-V2-API |
| GET | /api/u1/v1/xiaohongshu/app_v2/get_note_sub_comments | 获取笔记二级评论列表/Get note sub comments | header:authorization, query:comment_id | query:note_id, query:share_text, query:cursor, query:index | comments | Xiaohongshu-App-V2-API |
| GET | /api/u1/v1/xiaohongshu/app_v2/get_product_detail | 获取商品详情/Get product detail | header:authorization, query:sku_id | query:source, query:pre_page | single_post | Xiaohongshu-App-V2-API |
| GET | /api/u1/v1/xiaohongshu/app_v2/get_product_recommendations | 获取商品推荐列表/Get product recommendations | header:authorization, query:sku_id | query:cursor_score, query:region | other | Xiaohongshu-App-V2-API |
| GET | /api/u1/v1/xiaohongshu/app_v2/get_product_review_overview | 获取商品评论总览/Get product review overview | header:authorization, query:sku_id | query:tab | other | Xiaohongshu-App-V2-API |
| GET | /api/u1/v1/xiaohongshu/app_v2/get_product_reviews | 获取商品评论列表/Get product reviews | header:authorization, query:sku_id | query:page, query:sort_strategy_type, query:share_pics_only, query:from_page | other | Xiaohongshu-App-V2-API |
| GET | /api/u1/v1/xiaohongshu/app_v2/get_topic_feed | 获取话题笔记列表/Get topic feed | header:authorization, query:page_id | query:sort, query:cursor_score, query:last_note_id, query:last_note_ct, query:session_id, query:first_load_time, query:source | other | Xiaohongshu-App-V2-API |
| GET | /api/u1/v1/xiaohongshu/app_v2/get_topic_info | 获取话题详情/Get topic info | header:authorization, query:page_id | query:source, query:note_id | other | Xiaohongshu-App-V2-API |
| GET | /api/u1/v1/xiaohongshu/app_v2/get_user_faved_notes | 获取用户收藏笔记列表/Get user faved notes | header:authorization | query:user_id, query:share_text, query:cursor | other | Xiaohongshu-App-V2-API |
| GET | /api/u1/v1/xiaohongshu/app_v2/get_user_info | 获取用户信息/Get user info | header:authorization | query:user_id, query:share_text | author_profile | Xiaohongshu-App-V2-API |
| GET | /api/u1/v1/xiaohongshu/app_v2/get_user_posted_notes | 获取用户笔记列表/Get user posted notes | header:authorization | query:user_id, query:share_text, query:cursor | other | Xiaohongshu-App-V2-API |
| GET | /api/u1/v1/xiaohongshu/app_v2/get_video_note_detail | 获取视频笔记详情/Get video note detail | header:authorization | query:note_id, query:share_text | single_post | Xiaohongshu-App-V2-API |
| GET | /api/u1/v1/xiaohongshu/app_v2/search_groups | 搜索群聊/Search groups | header:authorization, query:keyword | query:page_no, query:search_id, query:source, query:is_recommend | search | Xiaohongshu-App-V2-API |
| GET | /api/u1/v1/xiaohongshu/app_v2/search_images | 搜索图片/Search images | header:authorization, query:keyword | query:page, query:search_id, query:search_session_id, query:word_request_id, query:source | search | Xiaohongshu-App-V2-API |
| GET | /api/u1/v1/xiaohongshu/app_v2/search_notes | 搜索笔记/Search notes | header:authorization, query:keyword | query:page, query:sort_type, query:note_type, query:time_filter, query:search_id, query:search_session_id, query:source, query:ai_mode | search | Xiaohongshu-App-V2-API |
| GET | /api/u1/v1/xiaohongshu/app_v2/search_products | 搜索商品/Search products | header:authorization, query:keyword | query:page, query:search_id, query:source | search | Xiaohongshu-App-V2-API |
| GET | /api/u1/v1/xiaohongshu/app_v2/search_users | 搜索用户/Search users | header:authorization, query:keyword | query:page, query:search_id, query:source | search | Xiaohongshu-App-V2-API |
| GET | /api/u1/v1/xiaohongshu/app/extract_share_info | 提取分享链接信息/Extract share link info | header:authorization, query:share_link | - | other | Xiaohongshu-App-API |
| GET | /api/u1/v1/xiaohongshu/app/get_note_comments | 获取笔记评论/Get note comments | header:authorization, query:note_id | query:start, query:sort_strategy | comments | Xiaohongshu-App-API |
| GET | /api/u1/v1/xiaohongshu/app/get_note_info | 获取笔记信息 V1/Get note info V1 | header:authorization | query:note_id, query:share_text | single_post | Xiaohongshu-App-API |
| GET | /api/u1/v1/xiaohongshu/app/get_note_info_v2 | 获取笔记信息 V2 (蒲公英商家后台)/Get note info V2 (Pugongying Business Backend) | header:authorization | query:note_id, query:share_text | single_post | Xiaohongshu-App-API |
| GET | /api/u1/v1/xiaohongshu/app/get_notes_by_topic | [已弃用/Deprecated] 根据话题标签获取作品/Get notes by topic | header:authorization, query:page_id, query:first_load_time | query:sort, query:session_id, query:last_note_ct, query:last_note_id, query:cursor_score | other | Xiaohongshu-App-API |
| GET | /api/u1/v1/xiaohongshu/app/get_product_detail | 获取商品详情/Get product detail | header:authorization, query:sku_id | - | single_post | Xiaohongshu-App-API |
| GET | /api/u1/v1/xiaohongshu/app/get_sub_comments | 获取子评论/Get sub comments | header:authorization, query:note_id, query:comment_id | query:start | comments | Xiaohongshu-App-API |
| GET | /api/u1/v1/xiaohongshu/app/get_user_id_and_xsec_token | 从分享链接中提取用户ID和xsec_token/Extract user ID and xsec_token from share link | header:authorization, query:share_link | - | other | Xiaohongshu-App-API |
| GET | /api/u1/v1/xiaohongshu/app/get_user_info | 获取用户信息/Get user info | header:authorization, query:user_id | - | author_profile | Xiaohongshu-App-API |
| GET | /api/u1/v1/xiaohongshu/app/get_user_notes | 获取用户作品列表/Get user notes | header:authorization, query:user_id | query:cursor | home_posts | Xiaohongshu-App-API |
| GET | /api/u1/v1/xiaohongshu/app/search_notes | 搜索笔记/Search notes | header:authorization, query:keyword, query:page | query:search_id, query:session_id, query:sort_type, query:filter_note_type, query:filter_note_time | search | Xiaohongshu-App-API |
| GET | /api/u1/v1/xiaohongshu/app/search_products | 搜索商品/Search products | header:authorization, query:keyword, query:page | query:search_id, query:session_id, query:sort, query:scope, query:service_guarantee, query:min_price, query:max_price, query:super_promotion | search | Xiaohongshu-App-API |
| GET | /api/u1/v1/xiaohongshu/web_v2/fetch_feed_notes | 获取单一笔记和推荐笔记 V1 (已弃用)/Fetch one note and feed notes V1 (deprecated) | header:authorization, query:note_id | - | other | Xiaohongshu-Web-V2-API |
| GET | /api/u1/v1/xiaohongshu/web_v2/fetch_feed_notes_v2 | 获取单一笔记和推荐笔记 V2/Fetch one note and feed notes V2(v2稳定, 推荐使用此接口) | header:authorization, query:note_id | - | other | Xiaohongshu-Web-V2-API |
| GET | /api/u1/v1/xiaohongshu/web_v2/fetch_feed_notes_v3 | 获取单一笔记和推荐笔记 V3/Fetch one note and feed notes V3(通过短链获取笔记详情) | header:authorization, query:short_url | - | other | Xiaohongshu-Web-V2-API |
| GET | /api/u1/v1/xiaohongshu/web_v2/fetch_feed_notes_v4 | 获取单一笔记和推荐笔记 V4 (互动量有延迟)/Fetch one note and feed notes V4 (interaction volume has a delay) | header:authorization, query:note_id | - | other | Xiaohongshu-Web-V2-API |
| GET | /api/u1/v1/xiaohongshu/web_v2/fetch_feed_notes_v5 | 获取单一笔记和推荐笔记 V5 (互动量有缺失)/Fetch one note and feed notes V5 (interaction volume has a missing) | header:authorization, query:note_id | - | other | Xiaohongshu-Web-V2-API |
| GET | /api/u1/v1/xiaohongshu/web_v2/fetch_follower_list | 获取用户粉丝列表/Fetch follower list | header:authorization, query:user_id | query:cursor | other | Xiaohongshu-Web-V2-API |
| GET | /api/u1/v1/xiaohongshu/web_v2/fetch_following_list | 获取用户关注列表/Fetch following list | header:authorization, query:user_id | query:cursor | other | Xiaohongshu-Web-V2-API |
| GET | /api/u1/v1/xiaohongshu/web_v2/fetch_home_notes | 获取Web用户主页笔记/Fetch web user profile notes | header:authorization, query:user_id | query:cursor | home_posts | Xiaohongshu-Web-V2-API |
| GET | /api/u1/v1/xiaohongshu/web_v2/fetch_home_notes_app | 获取App用户主页笔记/Fetch App user home notes | header:authorization, query:user_id | query:cursor | home_posts | Xiaohongshu-Web-V2-API |
| GET | /api/u1/v1/xiaohongshu/web_v2/fetch_hot_list | 获取小红书热榜/Fetch Xiaohongshu hot list | header:authorization | - | trend | Xiaohongshu-Web-V2-API |
| GET | /api/u1/v1/xiaohongshu/web_v2/fetch_note_comments | 获取笔记评论/Fetch note comments | header:authorization, query:note_id | query:cursor | comments | Xiaohongshu-Web-V2-API |
| GET | /api/u1/v1/xiaohongshu/web_v2/fetch_note_image | 获取小红书笔记图片/Fetch Xiaohongshu note image | header:authorization, query:note_id | - | other | Xiaohongshu-Web-V2-API |
| GET | /api/u1/v1/xiaohongshu/web_v2/fetch_product_list | 获取小红书商品列表/Fetch Xiaohongshu product list | header:authorization, query:user_id | query:page | other | Xiaohongshu-Web-V2-API |
| GET | /api/u1/v1/xiaohongshu/web_v2/fetch_search_notes | 获取搜索笔记/Fetch search notes | header:authorization, query:keywords | query:page, query:sort_type, query:note_type | search | Xiaohongshu-Web-V2-API |
| GET | /api/u1/v1/xiaohongshu/web_v2/fetch_search_users | 获取搜索用户/Fetch search users | header:authorization, query:keywords | query:page | search | Xiaohongshu-Web-V2-API |
| GET | /api/u1/v1/xiaohongshu/web_v2/fetch_sub_comments | 获取子评论/Fetch sub comments | header:authorization, query:note_id, query:comment_id | query:cursor | comments | Xiaohongshu-Web-V2-API |
| GET | /api/u1/v1/xiaohongshu/web_v2/fetch_user_info | 获取用户信息/Fetch user info | header:authorization, query:user_id | - | author_profile | Xiaohongshu-Web-V2-API |
| GET | /api/u1/v1/xiaohongshu/web_v2/fetch_user_info_app | 获取App用户信息/Fetch App user info | header:authorization, query:user_id | - | author_profile | Xiaohongshu-Web-V2-API |
| POST | /api/u1/v1/xiaohongshu/web/get_home_recommend | 获取首页推荐/Get home recommend | header:authorization | body:feed_type, body:need_filter_image, body:cursor_score, body:cookie, body:proxy | home_posts | Xiaohongshu-Web-API |
| GET | /api/u1/v1/xiaohongshu/web/get_note_comment_replies | 获取笔记评论回复 V1/Get note comment replies V1 | header:authorization, query:note_id, query:comment_id | query:lastCursor | comments | Xiaohongshu-Web-API |
| GET | /api/u1/v1/xiaohongshu/web/get_note_comments | 获取笔记评论 V1/Get note comments V1 | header:authorization, query:note_id | query:lastCursor | comments | Xiaohongshu-Web-API |
| GET | /api/u1/v1/xiaohongshu/web/get_note_id_and_xsec_token | 通过分享链接获取小红书的Note ID 和 xsec_token/Get Xiaohongshu Note ID and xsec_token by share link | header:authorization, query:share_text | - | other | Xiaohongshu-Web-API |
| GET | /api/u1/v1/xiaohongshu/web/get_note_info_v2 | 获取笔记信息 V2/Get note info V2 | header:authorization | query:note_id, query:share_text | single_post | Xiaohongshu-Web-API |
| GET | /api/u1/v1/xiaohongshu/web/get_note_info_v4 | 获取笔记信息 V4/Get note info V4 | header:authorization | query:note_id, query:share_text | single_post | Xiaohongshu-Web-API |
| POST | /api/u1/v1/xiaohongshu/web/get_note_info_v5 | 获取笔记信息 V5 (自带Cookie)/Get note info V5 (Self-provided Cookie) | header:authorization | body:note_id, body:xsec_token, body:cookie, body:proxy | single_post | Xiaohongshu-Web-API |
| GET | /api/u1/v1/xiaohongshu/web/get_note_info_v7 | 获取笔记信息 V7/Get note info V7 | header:authorization | query:note_id, query:share_text | single_post | Xiaohongshu-Web-API |
| GET | /api/u1/v1/xiaohongshu/web/get_product_info | 获取小红书商品信息/Get Xiaohongshu product info | header:authorization | query:share_text, query:item_id, query:xsec_token | other | Xiaohongshu-Web-API |
| GET | /api/u1/v1/xiaohongshu/web/get_user_info | 获取用户信息 V1/Get user info V1 | header:authorization, query:user_id | - | author_profile | Xiaohongshu-Web-API |
| GET | /api/u1/v1/xiaohongshu/web/get_user_info_v2 | 获取用户信息 V2/Get user info V2 | header:authorization | query:user_id, query:share_text | author_profile | Xiaohongshu-Web-API |
| GET | /api/u1/v1/xiaohongshu/web/get_user_notes_v2 | 获取用户的笔记 V2/Get user notes V2 | header:authorization, query:user_id | query:lastCursor | home_posts | Xiaohongshu-Web-API |
| GET | /api/u1/v1/xiaohongshu/web/get_visitor_cookie | 获取游客Cookie/Get visitor cookie | header:authorization | query:proxy | other | Xiaohongshu-Web-API |
| GET | /api/u1/v1/xiaohongshu/web/search_notes | 搜索笔记/Search notes | header:authorization, query:keyword | query:page, query:sort, query:noteType, query:noteTime | search | Xiaohongshu-Web-API |
| GET | /api/u1/v1/xiaohongshu/web/search_notes_v3 | 搜索笔记 V3/Search notes V3 | header:authorization, query:keyword | query:page, query:sort, query:noteType, query:noteTime | search | Xiaohongshu-Web-API |
| GET | /api/u1/v1/xiaohongshu/web/search_users | 搜索用户/Search users | header:authorization, query:keyword | query:page | search | Xiaohongshu-Web-API |
| POST | /api/u1/v1/xiaohongshu/web/sign | 小红书Web签名/Xiaohongshu Web sign | header:authorization | body:path, body:data, body:cookie | other | Xiaohongshu-Web-API |

