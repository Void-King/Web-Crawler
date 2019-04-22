import requests
from bs4 import BeautifulSoup
import os
location = '海南'
pagenum = 1
webstr = 'http://piao.qunar.com/ticket/list.htm?keyword=' + location + '&page='
# response = requests.get('http://piao.qunar.com/ticket/list.htm?keyword=海口&')

def grabdata():
    global webstr
    global pagenum
    if (pagenum == 2):
        os._exit(0)
    response = requests.get(webstr + str(pagenum))
    stra = response.content
    stra = stra.decode('utf-8')
    soup = BeautifulSoup(stra, "html.parser")
    strb = soup.find('div', attrs={'id': 'search-list'})
    strc = strb.findAll('div', attrs={'class': 'sight_item'})

    for sight_item in strc:
        name=sight_item['data-sight-name']
        districts=sight_item['data-districts']
        point=sight_item['data-point']
        address=sight_item['data-address']
        data_id=sight_item['data-id']
        sale=sight_item['data-sale-count']
        level=sight_item.find('span',attrs={'class':'level'})
        if level:
            level=level.text
        else:
            level="暂无"
        

        # progress 处理数据程序
        print (name,sale,level)
        print (address + '\n')
    pagenum += 1
    grabdata()
if __name__ == "__main__":
    grabdata()