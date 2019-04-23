import requests
from bs4 import BeautifulSoup
import os
import re
import time
import json

pagenum = 1

def grabSGdata():
    global pagenum
    commentnum = []
    if (pagenum == 2):
        os._exit(0)
    webstr = 'https://you.ctrip.com/sight/sanya61/s0-p' + str(pagenum) + '.html'
    wantwenturl = "https://you.ctrip.com/Destinationsite/SharedComm/ShowGowant"
    wantwentdata = {'Resource':'61',
            'pageType':'Place'}
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    response = requests.get(webstr, headers=headers)
    # # print (response)
    # print(response.status_code)  # 打印状态码
    # print(response.url)          # 打印请求url
    # print(response.headers)      # 打印头信息
    # print(response.cookies)      # 打印cookie信息
    # print(response.text)  #以文本形式打印网页源码
    # print(response.content) #以字节流形式打印
    stra = (response.content).decode('utf-8')
    soup = BeautifulSoup(stra, "html.parser")
    strb = soup.find('div', attrs={'class': 'list_wide_mod2'})
    strc = strb.findAll('a', attrs={'target': '_blank'})
    if pagenum == 1:
        wantwentres = requests.post(wantwenturl, headers=headers, data=wantwentdata)
        # # 解析结果
        str_json = wantwentres.content.decode("utf-8")
        wantwentdict = json.loads(str_json)
        print (wantwentdict['WentTimes'])
        print (wantwentdict['WantTimes'])
    # get name
    jumpflag = 0
    jumpflag2 = 0
    temp = []
    for strd in strc:
        jumpflag += 1
        if jumpflag == 1:
            continue
        elif jumpflag == 2:
            jumpflag2 += 1
            if jumpflag2 == 6:
                continue
            else:
                s = str(strd.text)
                temp.append(s)
        elif  jumpflag == 3:

            if jumpflag2 == 6:
                continue
            else:
                numtemp = re.findall('-?[1-9]\d*', str(strd.text))
                temp.append(int(numtemp[0]))
                commentnum.append(temp)
                temp = []    
            # continue
        elif  jumpflag == 4:
            jumpflag = 0
            continue
        
    print (commentnum)
    # get next page        
    pagenum += 1
    grabSGdata()

if __name__ == "__main__":
    grabSGdata()