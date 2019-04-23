import requests as webRequest
from bs4 import BeautifulSoup
import os
import re
import time
import json
import threadpool

name = ['test']

def grabdata(webID):
    global name
    # print(webID)
    webstr = 'http://www.win4000.com/mobile_detail_' + str(webID) + '.html'
    # webstr = 'http://www.win4000.com/wallpaper_detail_' + str(webID) + '.html'
    # webstr = 'http://www.win4000.com/meinv' + str(webID) + '.html'
    webResponse = webRequest.get(webstr)
    stra = webResponse.content
    stra = stra.decode('utf-8')
    soup = BeautifulSoup(stra, "html.parser")
    strb = soup.find('title')
    print (strb)
    
    # print (strc)
    for singleName in name:
        if (re.search(singleName, str(strb)) != None):
            print (str(webID) + "     " + str(strb))
            # print (webstr)
            strc = soup.find('img', attrs={'class': 'pic-large'})
            # print (strc)
            imgSrc = re.search('src=".*jpg"', str(strc)).group()
            imgSrc = imgSrc[5:]
            imgSrc = imgSrc[:-1]
            print (imgSrc)
            imgReponse = webRequest.get(imgSrc)
            open('.\\pics\\'+ singleName + '\\' + str(webID) + '.jpg', 'wb').write(imgReponse.content)

if __name__ == "__main__":
    for singleName in name:
        if (os.path.exists('.\\pics\\' + singleName) == False):
            os.mkdir('.\\pics\\' + singleName) 
    pool = threadpool.ThreadPool(5)
    idSet = [160000]
    for i in range(210001, 217916):
        idSet.append(i)
    requests = threadpool.makeRequests(grabdata, idSet)
    [pool.putRequest(req) for req in requests]
    pool.wait()

    # grabdata(177921)