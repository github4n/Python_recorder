import requests
from requests import exceptions
import urllib.request
import gzip
import urllib.parse
import json
import time
import random
import hashlib
import sys
 
def translate(input,output):
		#定义变量
		with open(input,'r',encoding='utf-8') as rfile:
			lines = rfile.readlines()
			#print(lines)
			num = 1
			mynum = 0
			for content in lines:
				content = content.strip()
				#print(content)
				url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
				client = 'fanyideskweb'
				ctime = int(time.time() * 1000)
				salt = str(ctime + random.randint(1, 10))
				# key = 'rY0D^0\'nM0}g5Mm1z%1G4' 以前版本的秘钥
				key = 'aNPG!!u6sesA>hBAW1@(-'
				sign = hashlib.md5((client + content + salt + key).encode('utf-8')).hexdigest()
				#表单数据
				data = {}
				data['i'] = content
				data['from'] = 'zh-CHS'
				data['to'] = 'en'
				data['smartresult'] = 'dict'
				data['client'] = 'fanyideskweb'
				data['salt'] = salt
				data['sign'] = sign
				data['doctype'] = 'json'
				data['version'] = '2.1'
				data['keyfrom'] = 'fanyi.web'
				data['action'] = 'FY_BY_CL1CKBUTTON'
				data['typoResult'] = 'false'
				data = urllib.parse.urlencode(data).encode('utf-8')
				#请求头
				head = {}
				head['Accept'] = 'application/json, text/javascript, */*; q=0.01'
				head['Accept-Encoding'] = 'gzip, deflate'
				head['Accept-Language'] = 'zh-CN,zh;q=0.9'
				head['Connection'] = 'keep-alive'
				head['Content-Type'] = 'application/x-www-form-urlencoded; charset=UTF-8'
				head['Cookie'] = 'OUTFOX_SEARCH_USER_ID=-1645744815@10.169.0.84; JSESSIONID=aaa9_E-sQ3CQWaPTofjew; OUTFOX_SEARCH_USER_ID_NCOO=2007801178.0378454; fanyi-ad-id=39535; fanyi-ad-closed=1; ___rl__test__cookies=' + str(ctime)
				head['Host'] = 'fanyi.youdao.com'
				head['Origin'] = 'http://fanyi.youdao.com'
				head['Referer'] = 'http://fanyi.youdao.com/'
				# User_Agent_pool = ['Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070803 Firefox/1.5.0.12',' Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)']
				# User_Agent_pool_len = len(User_Agent_pool)
				# head[ 'User-Agent'] = User_Agent_pool[mynum]
				head[ 'User-Agent'] = 'Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070803 Firefox/1.5.0.12'
				head['X-Requested-With'] = 'XMLHttpRequest'
				#代理ip
				#iplist = ['124.243.226.18:8888','121.33.220.158:808','14.118.135.10:808','118.190.94.224:9001','222.94.147.105:808']
				#proxies = {'http': iplist[1]}

				# request = urllib.request.Request(url, data, head)
				# response = urllib.request.urlopen(request)
				# #print(response)
				# with gzip.open(response, 'rb') as f:
				# 	response = f.read()
				# 	#print(response)
				# target = json.loads(response)
				# result = target['translateResult'][0][0]['tgt']
				try:
					#response = requests.post(url,headers=head,data=data,proxies=proxies,timeout=5.1).json()
					response = requests.post(url,headers=head,data=data).json()
				except Exception as e:
					print(content)
					# print(str(e))
					# if mynum <= User_Agent_pool_len:
					# 	mynum+=1
					# else:
					# 	print("没有可用的User-Agent了！")
				# except exceptions.Timeout as e:
				# 	print(str(e))
				# 	if mynum <= User_Agent_pool_len:
				# 		mynum+=1
				# 	else:
				# 		print("没有可用的User-Agent了！")
				# except exceptions.HTTPError as e:
				# 	print(str(e))
				# 	if mynum <= User_Agent_pool_len:
				# 		mynum+=1
				# 	else:
				# 		print("没有可用的User-Agent了！")
				# except exceptions.ConnectionError as e:
				# 	print(str(e))
				# 	if mynum <= User_Agent_pool_len:
				# 		mynum+=1
				# 	else:
				# 		print("没有可用的User-Agent了！")
				else:
					result = response['translateResult'][0][0]['tgt']
					print('L[%d]:%s'%(num,result))
					num = num + 1
					with open(output,'a',encoding='utf-8') as wfile:
						wfile.write(result + '\n')
				time.sleep(5)
				#return result

				
if __name__== "__main__":
	#translate(sys.argv[1],sys.argv[2])
	translate('input.txt','output.txt') 