#!/usr/bin/env python3

# -*- coding: utf-8 -*-
import requests
import json
import os
import time
import sys

#读取json格式的译文
def parse(json_data):
    json_data = json_data['translation'][0]['translated']
    result = []
    for trans in json_data:
        result.append(trans['text'])
    #将译文衔接在一起
    #result = " ".join(result)
    return result

#线上翻译地址
#url=''

#测试环境下翻译地址
url=''


headers={'','Content-Type':'application/x-www-form-urlencoded'}

#设置文件对象并读取每一行文件加入到data中
# data=[]
# for line in open('E:\\online_test\\Src_txt.txt','r'):
#   data.append(line)
# print(data[0])

fs=open('E:/mt-test/mt-test/common/origin/en-zh.en','r',encoding='utf-8')
#fs=open(sys.argv[1],'r',encoding='utf-8')
ft=open('E:/mt-test/mt-test/common/tran/en-zh.tran','w',encoding='utf-8')
# 清空ft中的内容
ft.truncate()
lines=fs.readlines()
for line in lines:
    j_data = {'text' : line}
    r=requests.post(url,data=j_data,headers=headers)
    # 判断状态码是否为200
    if r.status_code==200:
        tmp_j =json.loads(r.text)
        tmp_j = parse(tmp_j)
        #print(type(tmp_j))   
    else:
        tmp_j =json.loads(r.text)
    #将list类型转为字符串类型，并去掉首尾的空白部分
    tmp_j = ''.join(tmp_j).strip()
    print(tmp_j)
    #写入文件中
    ft.write(tmp_j + '\n')
    # 打开翻译文件，并将翻译内容写入文件中的两种方法：
    #1.ft=open('E:\\online_test\\Trans_txt.txt','a')

    #2. with open('Trans_txt.txt','w') as t:
    #     t.writelines(tmp_j)
fs.close()
ft.close()
