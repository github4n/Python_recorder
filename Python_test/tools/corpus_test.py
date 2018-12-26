#!/usr/bin/env python3

# -*- coding: utf-8 -*-
import requests
import json
import os
import time
import sys


#读取译文
def parse(json_data):
    json_data = json_data['translation'][0]['translated']
    result = []
    for trans in json_data:
        result.append(trans['text'])
    #print("R:", result)
    #将译文衔接在一起
    #result = " ".join(result)
    return result

#url=''
#url=''

url=sys.argv[1]
print ("翻译环境：%s" % url)
headers={'','Content-Type':'application/x-www-form-urlencoded'}

#设置文件对象并读取每一行文件加入到data中
# data=[]
# for line in open('E:\\online_test\\Src_txt.txt','r'):
#   data.append(line)
# print(data[0])

#fs=open('/home/shuping/tmp/mt-test/common/common-en-zh.en','r')
#fs=open('/home/shuping/tmp/mt-test/news/news-en-zh.zh','r')
fs=open(sys.argv[2],'r',encoding='utf-8')
ft=open(sys.argv[3],'w',encoding='utf-8')
# 清空ft中的内容
ft.truncate()
lines=fs.readlines()
num = 1
for line in lines:
    #去掉首尾的空白部分
    #line = line.strip()
    j_data = {'text' : line}
    r=requests.post(url,data=j_data,headers=headers)
        #print("JSON:", tmp_j)
    # 判断状态码是否为200
    if r.status_code==200:
        tmp_j =json.loads(r.text)
        tmp_j = parse(tmp_j) 
    else:
        tmp_j =json.loads(r.text)
    
    #将列表转成字符串形式，并移除字符串头尾空格
    line = " ".join(tmp_j).strip()
    print ("L[%d]:%s" % (num, line))
    num += 1
    #将翻译内容写入文件中
    ft.write(line + "\n")
    # print ("L:", line)
    # for t in tmp_j:
    #     if 'mt-api' in url:
    #         ft.write(t)
    #     else:
    #         ft.write(t+'\n')
fs.close()
ft.close()
