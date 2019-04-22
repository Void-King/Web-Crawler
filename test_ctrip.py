import requests
from bs4 import BeautifulSoup
import os
location = '海南'
pagenum = 5
# webstr = 'http://piao.qunar.com/ticket/list.htm?keyword=' + location + '&page='
def grabdata():
    global pagenum
    commentnum = []
    # if (pagenum == 6):
    #     os._exit(0)
    webstr = 'https://you.ctrip.com/sight/sanya61/s0-p' + str(pagenum) + '.html'
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
    # strb = soup.find('div', attrs={'class': 'list_wide_mod2'})
    # strc = strb.findAll('dd', attrs={'class': 'ellipsis'})
    strb = soup.find('div', attrs={'class': 'list_wide_mod2'})
    strc = strb.findAll('a', attrs={'target': '_blank'})
    # print (strc)


    # get name
    jumpflag = 0
    jumpflag2 = 0
    temp = []
    for strd in strc:
        # print (strd)
        # print ('\n\n\n\n\n\n\n\n\n')
        jumpflag += 1
        if jumpflag == 1:
            continue
        elif jumpflag == 2:
            jumpflag2 += 1
            if jumpflag2 == 6:
                continue
            else:
                s = str(strd.text)
                # print (s)
                temp.append(s)
        elif  jumpflag == 3:
        #     jumpflag2 += 1
            if jumpflag2 == 6:
                continue
            else:
                try:
                    c = int(str(strd.text)[34:37])
                    # print(c)
                    temp.append(c)
                except:
                    try:
                        c = int(str(strd.text)[34:36])
                        # print(c)
                        temp.append(c)
                    except:
                        c = int(str(strd.text)[34:35])
                        # print(c)
                        temp.append(c)
                commentnum.append(temp)
                temp = []    
            # continue
        elif  jumpflag == 4:
            jumpflag = 0
            continue
        
    for row in commentnum:
        print (row)
    # get next page        
    # pagenum += 1
    # grabdata()

if __name__ == "__main__":
    grabdata()