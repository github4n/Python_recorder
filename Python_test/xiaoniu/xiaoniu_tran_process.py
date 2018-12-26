import requests
from requests import exceptions
import multiprocessing
from multiprocessing import Pool
import urllib.request
import gzip
import urllib.parse
import json
import time
import random
import hashlib
import sys

#新建字典用于存放被打乱了顺序的原文和译文
all_translation = {}
def translate(lines_content):
	global all_translation
	#print(lines)
	#print(all_lines[:5])
	#print("I:", i)
	#num = 1
	#mynum = 0
	print(lines_content)
	for content in range(len(lines_content)):
		# print ("A")
		content = lines_content[content].strip()
		#print(content)
		apikey = '3aec701a3e5a5f0614df795eeffa67e8'
		translate_url = 'http://api.niutrans.vip/NiuTransServer/translation'
		#print ("B")
		headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1'}
		#print ("C")
		data = {
		'src_text':content,
		'from':'zh',
		'to':'en', 
		'apikey':apikey
		}
		#print ("D") 
		try:
			#print ("E")					
			response = requests.post(url=translate_url, data=data, headers=headers).json()
			#print(response)
			#print ("F")
		except Exception as e:
			#print ("G")
			print(e)				
		else:
			# print ("H")
			result = response['tgt_text']			
			all_translation[content] = result

			# print('L[%d]:%s'%(num,result))
			# num = num + 1
			# with open(sys.argv[2],'a',encoding='utf-8') as wfile:
			# 	wfile.write(result + '\n')
		time.sleep(1)
	#all_translation = str(all_translation)
	for key, value in all_translation.items():
		with open(sys.argv[2],'a',encoding='utf-8') as wfile:
			wfile.write(key+'\n')
		with open(sys.argv[3],'a',encoding='utf-8') as wfile:
			value = value.strip()
			wfile.write(value+'\n')
	#print("*****************************************************************************",all_translation)
	print("END")

				
if __name__== "__main__":
	# 读取原文文件
	with open(sys.argv[1],'r',encoding='utf-8') as rfile:
		lines = rfile.readlines()
	# print("LEN:", len(lines))

	#根据将它分为5个进程，每个进程跑prviot句
	print(len(lines))
	prviot = int(len(lines) / 5)
	# print("PR:", prviot)
	prev = 0

    #用于存放每个进程要跑的东西
	all_lines = []

	for i in range(1, 6):
		print("开始行:",prev* prviot)
		print("结束行:",i * prviot + 1)
		#print(lines[prev* prviot + 1:i * prviot])

		#说明一下lines[num1,num2]是指从第num1+1行，到第num2-1行
		all_lines.append(lines[prev* prviot:i * prviot])
		#print(type(lines[prev* prviot + 1:i * prviot]))
		prev = i
		#print(i)
		
    #新建五个进程
	for i in range(5):
		p = multiprocessing.Process(target = translate, args = (all_lines[i],))
		#print(len(all_lines[i]))
		p.start()
		p.join()

