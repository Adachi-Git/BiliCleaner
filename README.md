# BiliCleaner

Bilibili 追番 / 关注的批量清理与同步工具集。

## 组件

- `BiliFollowCleaner.py`：批量取消 Bilibili 追番 / 追剧
- `BiliFollowSync`：关注同步
- `BiliFavoritesSync`：收藏同步

## 使用（BiliFollowCleaner.py）

1. 填写脚本顶部的 `SESSDATA`、`csrf_token`、`vmid`（目标用户 MID）
2. 运行 `python BiliFollowCleaner.py`
3. 脚本会拉取追番列表并逐个取消

## 说明

- `type` 参数：`1` 为追番、`2` 为追剧
- 需要有效的 Bilibili 登录 Cookie（`SESSDATA`）
