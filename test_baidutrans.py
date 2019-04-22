import requests
import json
url = "https://fanyi.baidu.com/sug"
# 定义请求的参数
beftrans = 'hello'
data = {'kw': beftrans}
# 创建请求， 发送请求， 爬取信息
res = requests.post(url, data=data)
# 解析结果
str_json = res.content.decode("utf-8")
# print(type(str_json))
myjson = json.loads(str_json)
# print(type(myjson))
print (beftrans)
print (myjson['data'][0]['v'])