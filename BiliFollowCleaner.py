import requests

# 需要填写的内容
SESSDATA = ''  # 填写你的 SESSDATA
csrf_token = ''  # 填写你的 CSRF Token
vmid = ''  # 填写你要查询的用户的 MID
page_size = 30  # 每页返回的数量

# API的URL
url = 'https://api.bilibili.com/x/space/bangumi/follow/list'
cancel_url = 'https://api.bilibili.com/pgc/web/follow/del'

# 请求头
headers = {
    'Cookie': f'SESSDATA={SESSDATA}',
    'Referer': f'https://space.bilibili.com/{vmid}/bangumi',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}

def get_following_bangumi(page_num):
    # 查询参数
    params = {
        'vmid': vmid,
        'pn': page_num,
        'ps': page_size,
        'type': 1  # 1 表示追番，2 表示追剧
    }
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        data = response.json()
        if data['code'] == 0:
            return data['data']['list']
        else:
            print(f"获取追番列表失败，错误信息: {data['message']}")
            return None
    else:
        print(f"请求失败，状态码: {response.status_code}")
        return None

def cancel_following_bangumi(season_id):
    # 请求参数
    data_cancel = {
        'season_id': season_id,
        'csrf': csrf_token
    }
    
    # 发送POST请求取消追番
    response = requests.post(cancel_url, headers=headers, data=data_cancel)
    
    # 打印请求信息以调试
    print(f"请求 URL: {cancel_url}")
    print(f"请求参数: {data_cancel}")
    print(f"请求头: {headers}")
    print(f"响应状态码: {response.status_code}")
    print(f"响应内容: {response.text}")
    
    # 处理响应
    if response.status_code == 200:
        data = response.json()
        if data['code'] == 0:
            print(f"已成功取消追番 season_id: {season_id}")
        else:
            print(f"取消追番失败，错误信息: {data['message']}")
    else:
        print(f"请求失败，状态码: {response.status_code}")

# 主程序：获取所有追番并取消
page_num = 1
while True:
    bangumi_list = get_following_bangumi(page_num)
    
    if bangumi_list:
        for bangumi in bangumi_list:
            print(f"标题: {bangumi['title']}, season_id: {bangumi['season_id']}")
            cancel_following_bangumi(bangumi['season_id'])
        page_num += 1
    else:
        # 如果当前页没有数据，说明已经遍历完所有追番
        break

print("所有追番/剧已取消。")
