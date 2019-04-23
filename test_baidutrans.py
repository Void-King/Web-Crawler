import requests
import json

# 定义请求的参数
beftrans = 'hello'
print (beftrans)
def apitrans():
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }
    url = "https://fanyi.baidu.com/transapi"# v2transapi fail
    data = {'from':'en',
            'to':'zh',
            'query':beftrans}
    res = requests.post(url, data=data, headers=headers)
    struncode = res.content
    strafcode = json.loads(struncode, encoding='utf8')
    print (strafcode['data'][0]['dst'])
def sugtrans():
    url = "https://fanyi.baidu.com/sug"
    data = {'kw': beftrans}
    # 创建请求， 发送请求， 爬取信息
    res = requests.post(url, data=data)
    # 解析结果
    str_json = res.content
    # print (str_json)
    # # print(type(str_json))
    myjson = json.loads(str_json, encoding='utf-8')
    # print (myjson)
    # # print(type(myjson))
    print (myjson['data'][0]['v'])

if __name__ == "__main__":
    apitrans()
    sugtrans()