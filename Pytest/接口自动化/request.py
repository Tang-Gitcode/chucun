import requests
import json

# 请求头内容，键值对用字典表示
data=json.dumps({
  "account": "13530600569",
  "password": "560d4d8b173df72e813f0f1914aeb5df3240b53457000c55a1baa84fc389fa1e"
})

# 请求方式和地址
response = requests.post("http://t-admin.helitong.cn/api/v1/sign/in", data=data)

# 打印响应数据
print(response.json())

