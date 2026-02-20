# xiaohongshu API Catalog

- operation_count: 50

| Method | Path | Summary | Required Params | Optional Params | Suggested Intent | Tags |
| --- | --- | --- | --- | --- | --- | --- |
| GET | /api/u1/v1/xiaohongshu/app/extract_share_info | 提取分享链接信息/Extract share link info | query:share_link | - | other | Xiaohongshu-App-API |
| GET | /api/u1/v1/xiaohongshu/app/get_note_comments | 获取笔记评论/Get note comments | query:note_id | query:start, query:sort_strategy | comments | Xiaohongshu-App-API |
| GET | /api/u1/v1/xiaohongshu/app/get_note_info | 获取笔记信息 V1/Get note info V1 | - | query:note_id, query:share_text, query:force_video_enabled | single_post | Xiaohongshu-App-API |
| GET | /api/u1/v1/xiaohongshu/app/get_note_info_v2 | 获取笔记信息 V2 (蒲公英商家后台)/Get note info V2 (Pugongying Business Backend) | - | query:note_id, query:share_text | single_post | Xiaohongshu-App-API |
| GET | /api/u1/v1/xiaohongshu/app/get_notes_by_topic | 根据话题标签获取作品/Get notes by topic | query:page_id, query:first_load_time | query:sort, query:session_id, query:last_note_ct, query:last_note_id, query:cursor_score | other | Xiaohongshu-App-API |
| GET | /api/u1/v1/xiaohongshu/app/get_product_detail | 获取商品详情/Get product detail | query:sku_id | - | single_post | Xiaohongshu-App-API |
| GET | /api/u1/v1/xiaohongshu/app/get_sub_comments | 获取子评论/Get sub comments | query:note_id, query:comment_id | query:start | comments | Xiaohongshu-App-API |
| GET | /api/u1/v1/xiaohongshu/app/get_user_id_and_xsec_token | 从分享链接中提取用户ID和xsec_token/Extract user ID and xsec_token from share link | query:share_link | - | other | Xiaohongshu-App-API |
| GET | /api/u1/v1/xiaohongshu/app/get_user_info | 获取用户信息/Get user info | query:user_id | - | author_profile | Xiaohongshu-App-API |
| GET | /api/u1/v1/xiaohongshu/app/get_user_notes | 获取用户作品列表/Get user notes | query:user_id | query:cursor | home_posts | Xiaohongshu-App-API |
| GET | /api/u1/v1/xiaohongshu/app/get_video_note_info | 获取视频笔记信息 V1/ Get video note info V1 | - | query:note_id, query:share_text | single_post | Xiaohongshu-App-API |
| GET | /api/u1/v1/xiaohongshu/app/search_notes | 搜索笔记/Search notes | query:keyword, query:page | query:search_id, query:session_id, query:sort_type, query:filter_note_type, query:filter_note_time | search | Xiaohongshu-App-API |
| GET | /api/u1/v1/xiaohongshu/app/search_notes_v2 | 搜索笔记 V2/Search notes V2 | query:keyword | query:page, query:sort, query:noteType, query:noteTime | search | Xiaohongshu-App-API |
| GET | /api/u1/v1/xiaohongshu/app/search_products | 搜索商品/Search products | query:keyword, query:page | query:search_id, query:session_id, query:sort, query:scope, query:service_guarantee, query:min_price, query:max_price, query:super_promotion | search | Xiaohongshu-App-API |
| GET | /api/u1/v1/xiaohongshu/app/search_users | 搜索用户/Search users | query:keyword, query:page | - | search | Xiaohongshu-App-API |
| GET | /api/u1/v1/xiaohongshu/web_v2/fetch_feed_notes | 获取单一笔记和推荐笔记 V1 (已弃用)/Fetch one note and feed notes V1 (deprecated) | query:note_id | - | other | Xiaohongshu-Web-V2-API |
| GET | /api/u1/v1/xiaohongshu/web_v2/fetch_feed_notes_v2 | 获取单一笔记和推荐笔记 V2/Fetch one note and feed notes V2(v2稳定, 推荐使用此接口) | query:note_id | - | other | Xiaohongshu-Web-V2-API |
| GET | /api/u1/v1/xiaohongshu/web_v2/fetch_feed_notes_v3 | 获取单一笔记和推荐笔记 V3/Fetch one note and feed notes V3(通过短链获取笔记详情) | query:short_url | - | other | Xiaohongshu-Web-V2-API |
| GET | /api/u1/v1/xiaohongshu/web_v2/fetch_feed_notes_v4 | 获取单一笔记和推荐笔记 V4 (互动量有延迟)/Fetch one note and feed notes V4 (interaction volume has a delay) | query:note_id | - | other | Xiaohongshu-Web-V2-API |
| GET | /api/u1/v1/xiaohongshu/web_v2/fetch_feed_notes_v5 | 获取单一笔记和推荐笔记 V5 (互动量有缺失)/Fetch one note and feed notes V5 (interaction volume has a missing) | query:note_id | - | other | Xiaohongshu-Web-V2-API |
| GET | /api/u1/v1/xiaohongshu/web_v2/fetch_follower_list | 获取用户粉丝列表/Fetch follower list | query:user_id | query:cursor | other | Xiaohongshu-Web-V2-API |
| GET | /api/u1/v1/xiaohongshu/web_v2/fetch_following_list | 获取用户关注列表/Fetch following list | query:user_id | query:cursor | other | Xiaohongshu-Web-V2-API |
| GET | /api/u1/v1/xiaohongshu/web_v2/fetch_home_notes | 获取Web用户主页笔记/Fetch web user profile notes | query:user_id | query:cursor | home_posts | Xiaohongshu-Web-V2-API |
| GET | /api/u1/v1/xiaohongshu/web_v2/fetch_home_notes_app | 获取App用户主页笔记/Fetch App user home notes | query:user_id | query:cursor | home_posts | Xiaohongshu-Web-V2-API |
| GET | /api/u1/v1/xiaohongshu/web_v2/fetch_hot_list | 获取小红书热榜/Fetch Xiaohongshu hot list | - | - | trend | Xiaohongshu-Web-V2-API |
| GET | /api/u1/v1/xiaohongshu/web_v2/fetch_note_comments | 获取笔记评论/Fetch note comments | query:note_id | query:cursor | comments | Xiaohongshu-Web-V2-API |
| GET | /api/u1/v1/xiaohongshu/web_v2/fetch_note_image | 获取小红书笔记图片/Fetch Xiaohongshu note image | query:note_id | - | other | Xiaohongshu-Web-V2-API |
| GET | /api/u1/v1/xiaohongshu/web_v2/fetch_product_list | 获取小红书商品列表/Fetch Xiaohongshu product list | query:user_id | query:page | other | Xiaohongshu-Web-V2-API |
| GET | /api/u1/v1/xiaohongshu/web_v2/fetch_search_notes | 获取搜索笔记/Fetch search notes | query:keywords | query:page, query:sort_type, query:note_type | search | Xiaohongshu-Web-V2-API |
| GET | /api/u1/v1/xiaohongshu/web_v2/fetch_search_users | 获取搜索用户/Fetch search users | query:keywords | query:page | search | Xiaohongshu-Web-V2-API |
| GET | /api/u1/v1/xiaohongshu/web_v2/fetch_sub_comments | 获取子评论/Fetch sub comments | query:note_id, query:comment_id | query:cursor | comments | Xiaohongshu-Web-V2-API |
| GET | /api/u1/v1/xiaohongshu/web_v2/fetch_user_info | 获取用户信息/Fetch user info | query:user_id | - | author_profile | Xiaohongshu-Web-V2-API |
| GET | /api/u1/v1/xiaohongshu/web_v2/fetch_user_info_app | 获取App用户信息/Fetch App user info | query:user_id | - | author_profile | Xiaohongshu-Web-V2-API |
| POST | /api/u1/v1/xiaohongshu/web/get_home_recommend | 获取首页推荐/Get home recommend | - | body:feed_type, body:need_filter_image, body:cursor_score, body:cookie, body:proxy | home_posts | Xiaohongshu-Web-API |
| GET | /api/u1/v1/xiaohongshu/web/get_note_comment_replies | 获取笔记评论回复 V1/Get note comment replies V1 | query:note_id, query:comment_id | query:lastCursor | comments | Xiaohongshu-Web-API |
| GET | /api/u1/v1/xiaohongshu/web/get_note_comments | 获取笔记评论 V1/Get note comments V1 | query:note_id | query:lastCursor | comments | Xiaohongshu-Web-API |
| GET | /api/u1/v1/xiaohongshu/web/get_note_id_and_xsec_token | 通过分享链接获取小红书的Note ID 和 xsec_token/Get Xiaohongshu Note ID and xsec_token by share link | query:share_text | - | other | Xiaohongshu-Web-API |
| GET | /api/u1/v1/xiaohongshu/web/get_note_info_v2 | 获取笔记信息 V2/Get note info V2 | - | query:note_id, query:share_text | single_post | Xiaohongshu-Web-API |
| GET | /api/u1/v1/xiaohongshu/web/get_note_info_v4 | 获取笔记信息 V4/Get note info V4 | - | query:note_id, query:share_text | single_post | Xiaohongshu-Web-API |
| POST | /api/u1/v1/xiaohongshu/web/get_note_info_v5 | 获取笔记信息 V5 (自带Cookie)/Get note info V5 (Self-provided Cookie) | - | body:note_id, body:xsec_token, body:cookie, body:proxy | single_post | Xiaohongshu-Web-API |
| GET | /api/u1/v1/xiaohongshu/web/get_note_info_v7 | 获取笔记信息 V7/Get note info V7 | - | query:note_id, query:share_text | single_post | Xiaohongshu-Web-API |
| GET | /api/u1/v1/xiaohongshu/web/get_product_info | 获取小红书商品信息/Get Xiaohongshu product info | - | query:share_text, query:item_id, query:xsec_token | other | Xiaohongshu-Web-API |
| GET | /api/u1/v1/xiaohongshu/web/get_user_info | 获取用户信息 V1/Get user info V1 | query:user_id | - | author_profile | Xiaohongshu-Web-API |
| GET | /api/u1/v1/xiaohongshu/web/get_user_info_v2 | 获取用户信息 V2/Get user info V2 | - | query:user_id, query:share_text | author_profile | Xiaohongshu-Web-API |
| GET | /api/u1/v1/xiaohongshu/web/get_user_notes_v2 | 获取用户的笔记 V2/Get user notes V2 | query:user_id | query:lastCursor | home_posts | Xiaohongshu-Web-API |
| GET | /api/u1/v1/xiaohongshu/web/get_visitor_cookie | 获取游客Cookie/Get visitor cookie | - | query:proxy | other | Xiaohongshu-Web-API |
| GET | /api/u1/v1/xiaohongshu/web/search_notes | 搜索笔记/Search notes | query:keyword | query:page, query:sort, query:noteType, query:noteTime | search | Xiaohongshu-Web-API |
| GET | /api/u1/v1/xiaohongshu/web/search_notes_v3 | 搜索笔记 V3/Search notes V3 | query:keyword | query:page, query:sort, query:noteType, query:noteTime | search | Xiaohongshu-Web-API |
| GET | /api/u1/v1/xiaohongshu/web/search_users | 搜索用户/Search users | query:keyword | query:page | search | Xiaohongshu-Web-API |
| POST | /api/u1/v1/xiaohongshu/web/sign | 小红书Web签名/Xiaohongshu Web sign | - | body:path, body:data, body:cookie | other | Xiaohongshu-Web-API |

