import requests as webRequest
from bs4 import BeautifulSoup
import os
import re
import time
import json
import threadpool
import hashlib

def md5(strOld):
    md=hashlib.md5()   #将hashlib.md5的算法赋值给md
    md.update(strOld.encode('utf-8'))   #先将你好这个字符串以utf-8编码转换成bytes(字节)格式，再存入到md变量中，因为update中只能存入bytes(字节)
    md=md.hexdigest() 
    return md

def grabdata(webstr):
    webResponse = webRequest.get(webstr)
    stra = webResponse.content
    stra = stra.decode('utf-8')
    soup = BeautifulSoup(stra, "html.parser")
    strb = soup.find('div', attrs={'class': 'n-conflmt mg2'})
    # print (strb)
    reResult = re.search(r'/[0-9]+.jpg', str(strb))
    reResultSec = re.search(r'upload/[0-9]{6}/[0-9]{2}/', str(strb))
    
    if reResult:
        imgName = reResult.group()
        imgName = imgName[1:]
        imgName = imgName[:-4]
        # print (imgName)
        imgName = md5(imgName)
        if reResultSec:
            downWebStr = r"https://images1.h128.com/" \
                + reResultSec.group() + imgName + '.jpg'
            print (downWebStr)
            imgReponse = webRequest.get(downWebStr)
            open('.\\pics\\h128\\' + \
                str(imgName) + '.jpg', 'wb').write(imgReponse.content)
    

if __name__ == "__main__":
    webstr = input("webstr:")
    grabdata(webstr)