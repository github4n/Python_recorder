# -*- coding:UTF-8 -*-

import requests
import random
from requests.exceptions import RequestException


url = "https://baidu.com/"
iplist = ['221.6.138.154:30893','106.75.164.15:3128','106.75.226.36:808','116.1.11.19:80','60.208.32.201:80']
#proxies ={'http':random.choice(iplist)}
proxies = {'https': iplist[1]}
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.103 Safari/537.36', 'Connection':'keep-alive'}
try:
	response = requests.get(url = url,proxies=proxies,headers=headers,timeout=10)
	#response.encode("utf-8")
	html = response.text
	print(html)
	#print(proxies['http'])
except RequestException as e:
	print('爬虫错误，错误原因：',e)
