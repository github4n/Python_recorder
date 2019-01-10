# -*- coding:UTF-8 -*-

import requests
import random
from requests.exceptions import RequestException


url = "https://baidu.com/"
iplist = ['221.6.201.18:9999','119.176.80.220:9999','119.101.114.234:9999','119.101.115.113:9999','119.101.116.219:9999',
        "112.115.57.20:3128"]
#proxies ={'http':random.choice(iplist)}
proxies = {'https': iplist[5]}
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.103 Safari/537.36', 'Connection':'keep-alive'}
try:
  response = requests.get(url = url,proxies=proxies,headers=headers,timeout=10)
  #response.encode("utf-8")
  html = response.text
  print(html)
  #print(proxies['http'])
except RequestException as e:
  print('爬虫错误，错误原因：',e)
