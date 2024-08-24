# bili2bili

`bili2bili` 能够获取用户的关注列表，并通过 Bilibili API 批量关注/拉黑 这些用户。

## 功能

- 获取你在 Bilibili 上关注的用户列表。
- 批量关注/拉黑 从列表中获取的用户。
- 可配置请求之间的延时以避免触发速率限制。

## 需求

- Python 3.x
- `requests` 库（可以通过 `pip install requests` 安装）

## 配置

在运行脚本之前，你需要设置以下变量：

- `sessdata1` : 用于获取关注列表的 Bilibili 会话数据 Cookie。
- `sessdata2` : 用于执行批量操作的 Bilibili 会话数据 Cookie。
- `csrf_token` : 批量操作所需的 CSRF Token。
- `vmid` : 要获取关注列表的用户 ID。

## 使用方法

1. **配置你的凭据：**
   替换占位符值为你的实际 `sessdata1`、`sessdata2`、`csrf_token` 和 `vmid`。

2. **运行脚本：**
   ```bash
   python b2b.py
   ```
