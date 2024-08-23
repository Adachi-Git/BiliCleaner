import requests
import time

# SESSDATA Cookies
sessdata1 = ""
vmid = ""   
sessdata2 = "" 
csrf_token = ""  

# API URL
followings_url = "https://api.bilibili.com/x/relation/followings"
batch_modify_url = "https://api.bilibili.com/x/relation/batch/modify"

# 请求头部信息
headers = {
    "Referer": "https://www.bilibili.com/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
}

# 请求头部信息（用于获取关注列表）
headers1 = headers.copy()
headers1["Cookie"] = f"SESSDATA={sessdata1}"

# 请求头部信息（用于批量加关注）
headers2 = headers.copy()
headers2["Cookie"] = f"SESSDATA={sessdata2}"

# 请求参数
params = {
    "vmid": vmid,
    "order_type": "",  # 按照关注顺序排列
    "ps": 50,  # 每页项数
    "pn": 1    # 页码，从第一页开始
}

# 初始化关注列表
all_followings = []

# 获取关注列表
while True:
    response = requests.get(followings_url, headers=headers1, params=params)
    data = response.json()

    # 检查请求是否成功
    if data['code'] != 0:
        print(f"Error: {data['message']}")
        break

    # 获取当前页的关注列表
    followings = data['data']['list']
    if not followings:
        break  # 如果没有更多的关注者，跳出循环

    # 添加到总列表
    all_followings.extend(followings)

    # 获取总关注人数并打印
    total_followings = data['data']['total']
    print(f"Total followings: {total_followings}")

    # 判断是否为最后一页
    if len(all_followings) >= total_followings:
        break

    # 下一页
    params['pn'] += 1

# 输出关注列表，包括 MID 和用户名
for idx, user in enumerate(all_followings, start=1):
    print(f"{idx}: MID: {user['mid']} - Username: {user['uname']}")

# 批量关注操作
def batch_follow(followings):
    # 批量关注操作
    while followings:
        # 获取50个用户的MID
        current_batch = followings[:50]
        followings = followings[50:]

        # 拼接关注用户的 MID 列表
        fids = ",".join(str(user['mid']) for user in current_batch)
        
        # 请求正文参数
        data = {
            "fids": fids,
            "act": 1,  # 批量关注 仅可为 1 或 5，故只能进行批量关注和拉黑
            "re_src": 11,
            "csrf": csrf_token
        }
        
        # 执行批量关注操作
        response = requests.post(batch_modify_url, headers=headers2, data=data)
        result = response.json()

        # 检查请求是否成功
        if result['code'] == 0:
            print("批量关注操作成功!")
            failed_fids = result['data'].get('failed_fids', [])
            if failed_fids:
                print(f"操作失败的用户MID: {failed_fids}")
        else:
            print(f"操作失败: {result['message']}")

        # 延时3秒
        time.sleep(1)

# 执行批量关注操作
batch_follow(all_followings)
