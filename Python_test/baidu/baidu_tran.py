# -*- coding: utf-8 -*-

import requests
import pprint
import re
import json
import time
import sys


#翻译
def translate(infile, oufile, fromlanguage, tolanguage):
    with open(infile,'r',encoding ='utf-8') as rfile:
        lines = rfile.readlines()
        num = 1
        for line in lines:
            # 翻译url
            translate_url = 'https://fanyi.baidu.com/basetrans'
            headers = {
            'User-Agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1"
            }
            line = line.strip()
            data = {
            'from': fromlanguage,
            'to': tolanguage,
            'query': line,
            }
            resp = requests.post(url=translate_url, data=data, headers=headers, timeout=5.1).json()
            target = resp['trans'][0]['dst']
            with open(oufile,'a',encoding='utf-8') as wfile:
                wfile.write(target+'\n')
            print('L[%d]:%s'%(num,target))
            num = num + 1    
            time.sleep(3)
            #return eval(resp)




if __name__== "__main__":
    #translate(sys.argv[0], sys.argv[1], sys.argv[2])
    translate('input.txt','output.txt', 'zh', 'en')






















# def baidu_tran(infile):
#     with open(infile,'r',encoding ='utf-8') as rfile:
#         lines = rfile.readlines()
#         for line in lines:
#             line = line.strip()
#             print(line)
#             userAgent = "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"
#             header = {
#             "User-Agent": userAgent
#             }

#             postUrl="https://fanyi.baidu.com/basetrans"
#             mdata = {
#                     "from":"en",
#                     "to":"zh",
#                     "query" : line
#                     }
#             try:
#                 response = requests.post(postUrl, data = mdata, headers = header, timeout=5.1).json()
#                 target = response['trans'][0]['dst']
#                 print(target)
#             except:
#                 print('connect error!')
#                 return 1           
            
            






# if __name__== "__main__":
#     baidu_tran('input.txt')

