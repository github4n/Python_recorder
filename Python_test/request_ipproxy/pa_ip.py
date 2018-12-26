# -*- coding:UTF-8 -*-

import requests
from bs4 import BeautifulSoup
from lxml import etree
import subprocess as sp
import re
import sys
import random
import socket
import time
from multiprocessing import Pool

# ---------多进程爬IP，并检测该ip是否有用------------



def get_proxys(page):
	file = open("ip_log.txt","w",encoding="UTF-8")
	tag_url = "http://www.xicidaili.com/nn/%d" % page
	head = {'user-agent':'Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070803 Firefox/1.5.0.12'}
	response = requests.get(url = tag_url,headers = head)
	response_content = response.text
	tag_soup = BeautifulSoup(response_content,'lxml')
	tag_content = BeautifulSoup(str(tag_soup.find_all(id = 'ip_list')),'lxml')
	tag_iplist = tag_content.find_all('tr')
	#print(tag_iplist)
	proxys_list = []
	#找出带有IP的tr，便利tr列表
	for child in tag_iplist:
	# 	#print(child)
		tag_class = child.get('class')
	# 	#print(tag_class)
		#当tag_class不为空时
		if tag_class:
			tag_class = tag_class[0]
			if(tag_class != None):
				tag_td = child.find_all('td')
				file.write(tag_td[1].text +':'+ tag_td[2].text + '\n')
				proxy_item = tag_td[1].text + ':' + tag_td[2].text
				proxys_list.append(proxy_item)
				#判断是否为https协议并且存活时间大于三天
				# if(tag_td[5].text == 'HTTPS'):
				#     #print(tag_td[1])
				#     #将ip写入文档
				#     file.write(tag_td[1].text +':'+ tag_td[2].text + ':' +tag_td[8].text+ '\n')
				#     proxys_list.append(tag_td[1].text + ':' + tag_td[2].text)
	file.close()
	return proxys_list



# -----------------------------检测ip是否可用-----------

def checkIP(proxy):
	url = "https://www.baidu.com"
	wfile = open("ip_use.txt","r+",encoding="UTF-8")
	wtxt = wfile.read()
	rfile = open("ip_log.txt","r",encoding="UTF-8")
	#添加延时
	socket.setdefaulttimeout(5)
	proxys = rfile.readlines()
	#print(proxys)
	for proxy in proxys:
		proxy = proxy.strip('\n')
		#print(proxy)
		try:
			proxies = {'https': proxy}
			response = requests.get(url = url,proxies=proxies,timeout=10)
			html = response.text
			if html:
				print("代理ip：" + proxy + "可用")
				wfile.write('\n' + proxy + '\n')
			else:
				print("代理ip：" + proxy + "不可用")
		except Exception as e:
			print(e)
	wfile.close()
	rfile.close()





if __name__ == '__main__':
	proxy = get_proxys(1)
	time1 = time.time()
	for item in proxy:
		#print(item)
		checkIP(item)
	time2 = time.time()
	print('singleprocess needs '+str(time2-time1)+' s')
	
	# #进程pool
	# pool = Pool()
	# time3 = time.time()
	# for item in proxy:
	# 	pool.apply_async(checkIP,args=(item,))
	# pool.close()
	# pool.join()
	# time4 = time.time()
	# print('multiprocess needs '+str(time4-time3)+' s')


	
		