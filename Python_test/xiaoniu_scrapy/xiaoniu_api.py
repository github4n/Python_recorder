# -*- coding:utf-8 -*-

import json
import time
import requests
import random
from requests import exceptions
import multiprocessing
from multiprocessing import Pool
import sys


#新建字典用于存放被打乱了顺序的原文和译文
all_translation = {}
def translate(lines_content):
	#print(lines_content)
	for content_num in range(len(lines_content)):
		content = lines_content[content_num]
		#print(content)
		#用于代理ip
		num = 0
		url = 'https://test.niutrans.vip/NiuTransServer/testtrans?'
		d = content
		url_flag = ""
		# 由于网页是用的js的时间戳(毫秒)跟python(秒)的时间戳不在一个级别，所以需要*1000
		m = random.random()
		data= {
			'src_text':d,
			'from':'zh',
			'to':'ti',
			#当前时间戳
			'm':m,
			'url':url_flag
		}

		headers = {
		#'Accept': 'application/json, text/javascript, */*; q=0.01',
		#'Accept-Encoding': 'gzip, deflate, br',
		#'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7,hi;q=0.6,ja;q=0.5',
		#'Cache-Control': 'no-cache',
		#'Connection': 'keep-alive',
		#'Host': 'test.niutrans.vip',
		#'Pragma': 'no-cache',
		'Origin': 'https://niutrans.vip', 
		'Referer':'https://niutrans.vip/index/niutrans/index.html',
		'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
		}
		#print(data)
		#代理ip
		iplist = ['221.6.201.18:9999','119.176.80.220:9999','119.101.114.234:9999','119.101.115.113:9999','119.101.116.219:9999']
		proxies = {'https': iplist[0]}
		#接口
		try:
			xiaoniures= requests.get(url,headers = headers,data=data,proxies=proxies)
		except Exception as e:
			print(e)
			print("--------------------------------------")
			if num <= len(iplist):
				proxies = {'https': iplist[num+1]}
				num = num + 1
			else:
				print("没有可用的IP了！" + num)
		else:
			#print(xiaoniures.text)
			xiaoniujson = xiaoniures.json()
			print(xiaoniujson)
			result = xiaoniujson['tgt_text']
			all_translation[content] = result	   
			#print(result)
		time.sleep(3)
	for key, value in all_translation.items():
		with open(sys.argv[2],'a',encoding='utf-8') as wfile:
			print(key)
			wfile.write(key+'\n')
		with open(sys.argv[3],'a',encoding='utf-8') as wfile:
			value = value.strip()
			print(value)
			wfile.write(value+'\n')
		
	print("hehehe")

if __name__== "__main__":
	with open(sys.argv[1],'r',encoding='utf-8') as rfile:
		lines = rfile.readlines()
	#分成六个进程
	part = int(len(lines)/6)
	#all_lines用于存放6个分好的部分
	all_lines = []
	for i in range(1,7):
		# print("开始行:",strat*part+1)
		# print("结束行:",i * part)
		# print("------------------------")
		# print((i-1)*part)
		# print(i*part)
		#说明一下lines[num1,num2]是指从第num1+1行，到第num2-1行
		all_lines.append(lines[(i-1)*part:i*part])

	#新建六个进程
	for i in range(6):
		p = multiprocessing.Process(target = translate, args = (all_lines[i],))
		#print(len(all_lines[i]))
		p.start()
		p.join()

