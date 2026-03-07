# 抖音 Creator 指引

## 作者侧优先资源

- 昵称：`nickname`
- handle：`short_id` / `unique_id`
- IP 属地
- 头像
- 粉丝数、累计获赞数、作品数

## 作品侧优先资源

- 作品 ID：`aweme_id`
- 标题 / 文案：`title` / `desc`
- 视频下载链接：优先无水印路径
- 互动指标：点赞、评论、收藏、分享、播放

## 当前参考实现

- `skills/tikomni-skill/scripts/author_home/adapters/platform_adapters.py`
- `skills/tikomni-skill/scripts/author_home/orchestrator/run_author_analysis.py`
