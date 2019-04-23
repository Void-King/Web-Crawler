import requests as webRequest
from bs4 import BeautifulSoup
import os
import re
import time
import json
import threadpool

def grabdata():
    old_cookies = r'session-id=457-8087383-5014609; ubid-acbcn=461-6718238-8083321; x-acbcn="zqCavlFB9@MFODmbGOV134TfaXy2I95P5ZddoIbM3tRexXyWlIhB215@hF?mgHyW"; at-main=Atza|IwEBIOAev6nFh_90kWgWeUe46V1c-tBXGKlMQJ3wmUMg5WwZFTCs2W0W5Tb8GbOjFc7quC8OhMU90j0P6EthIxWO-SX1SR1NMLuS-PgmKI8Kz3d0YuiC7U85aSJn-qwOlz1I7jLIdA8vxKLn_3SszrfN5wgijvvfGexEAh39sd9pPmmi0NhInVW5yp3isyGYS_HDFDjGk3IuU6TrXI98uDEOQmrV5vMZOW1CFlZmjEG1buk8KA; sess-at-main="LM4qU+XyiAZKrjyqqThmjnQ/EL1JNmjlWiPTOV7rcEA="; sst-main=Sst1|PQHrrU7u7sKKCqCDz_3fSNtDC-NDRQBTLYKR-vhpROCiK6tLEqg-MHDX_m2-nESqDMeOFoK3G7QgFlQKdXo_CWNnCb9UkSLT5FSmCtkMELddv6fE94Ya7qC9J3U11aPG7sazYJsiNvmF3zbAKlauKWRsNNVqHWyiYIriS6qUPlQhjDAMj8uh2UYZpFT1lQ4d2IVscH7Bfbb7DkKCaMrRGhslmTB2AvZCHyx0uG_Op3gKn-Pq4a0rxEB9LMF9e_oCJnm_3ihtr_bcAmog9ksSbmXicc4oYV_hp8CZraYXNvy63jNuVHiU_m6q1WUrjl-AsUPqEq70e1-rRa_Rxhk3I69XtQ; lc-acbcn=zh_CN; i18n-prefs=CNY; s_vnum=2030750837179%26vn%3D2; s_nr=1602892539214-Repeat; s_dslv=1602892539216; session-token="7QB9U79SZHzjzRXzPHJX+U2NnviE1CjxZFEzZ+lum2VWFe3rbZZBlQNAILuMobEpcJoGodaxURtLFlLttva4i+vc9R5RV5eNIEcdLG6fKKHMWB09TSwMNscL56AgIZ+smXkMSLRQOTczzWU1l5UtHX4ACFPgZKTiMe4P0rKyKgq8Zl8mFedMjd02xt2z8/eRG77skD6GQB+jYUuqDiw+3w=="; session-id-time=2082729601l; csm-hit=tb:B218Z37Z9MNXCC5JK4E8+s-B218Z37Z9MNXCC5JK4E8|1603337311791&t:1603337311791&adb:adblk_no'
    # print(webID)
    
    headers = {
        'User-Agent': r'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'Cookie': old_cookies
        }

    webstr = 'https://www.amazon.cn/dp/B01JOOK4AI'

    # r = webRequest.get(webstr, cookies=headers)

    # print (r)

    # new_cookies = r.cookies

    # print (new_cookies)

    webResponse = webRequest.get(webstr, headers=headers)
    stra = webResponse.content
    stra = stra.decode('utf-8')
    soup = BeautifulSoup(stra, "html.parser")
    # print (stra)
    strc = soup.findAll('span', attrs={'class': r'a-size-mini twisterSwatchPrice'})
    for strd in strc:
        print (strd.text)
    
if __name__ == "__main__":
    grabdata()