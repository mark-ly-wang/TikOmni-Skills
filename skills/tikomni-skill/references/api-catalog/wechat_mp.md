# wechat_mp API Catalog

- operation_count: 10

| Method | Path | Summary | Required Params | Optional Params | Suggested Intent | Tags |
| --- | --- | --- | --- | --- | --- | --- |
| GET | /api/u1/v1/wechat_mp/web/fetch_mp_article_ad | 获取微信公众号广告/Get Wechat MP Article Ad | query:url | - | other | WeChat-Media-Platform-Web-API |
| GET | /api/u1/v1/wechat_mp/web/fetch_mp_article_comment_list | 获取微信公众号文章评论列表/Get Wechat MP Article Comment List | query:url | query:comment_id, query:buffer | comments | WeChat-Media-Platform-Web-API |
| GET | /api/u1/v1/wechat_mp/web/fetch_mp_article_comment_reply_list | 获取微信公众号文章评论回复列表/Get Wechat MP Article Comment Reply List | query:comment_id, query:content_id | query:url, query:offset | comments | WeChat-Media-Platform-Web-API |
| GET | /api/u1/v1/wechat_mp/web/fetch_mp_article_detail_html | 获取微信公众号文章详情的HTML/Get Wechat MP Article Detail HTML | query:url | - | single_post | WeChat-Media-Platform-Web-API |
| GET | /api/u1/v1/wechat_mp/web/fetch_mp_article_detail_json | 获取微信公众号文章详情的JSON/Get Wechat MP Article Detail JSON | query:url | - | single_post | WeChat-Media-Platform-Web-API |
| GET | /api/u1/v1/wechat_mp/web/fetch_mp_article_list | 获取微信公众号文章列表/Get Wechat MP Article List | query:ghid | query:offset | other | WeChat-Media-Platform-Web-API |
| GET | /api/u1/v1/wechat_mp/web/fetch_mp_article_read_count | 获取微信公众号文章阅读量/Get Wechat MP Article Read Count | query:url, query:comment_id | - | other | WeChat-Media-Platform-Web-API |
| GET | /api/u1/v1/wechat_mp/web/fetch_mp_article_url | 获取微信公众号文章永久链接/Get Wechat MP Article URL | query:sogou_url | - | other | WeChat-Media-Platform-Web-API |
| GET | /api/u1/v1/wechat_mp/web/fetch_mp_article_url_conversion | 获取微信公众号长链接转短链接/Get Wechat MP Long URL to Short URL | query:url | - | other | WeChat-Media-Platform-Web-API |
| GET | /api/u1/v1/wechat_mp/web/fetch_mp_related_articles | 获取微信公众号关联文章/Get Wechat MP Related Articles | query:url | - | other | WeChat-Media-Platform-Web-API |

