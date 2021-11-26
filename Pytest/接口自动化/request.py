import requests

import json

# 请求头内容，键值对用字典表示
# data = json.dumps({
#   "account": "13530600566",
#   "password": "560d4d8b173df72e813f0f1914aeb5df3240b53457000c55a1baa84fc389fa1e"
# })
files = json.dumps({"file": open("C:/Users/administered/Desktop/login.xls", "rb")})

# 请求方式和地址
response = requests.post("http://t-channel.helitong.cn/api/v1/dealer/sign/in", files=files)

# 打印响应数据
print(response.json())

# 打印状态码
print(response.status_code)

print(response.cookies)

# 重定向
print(response.history)

# 打印文本形式响应
print(response.text)

