#!/usr/bin/env python3

# -*- coding: utf-8 -*-

import requests
import json
import xlrd
import os
from xlutils.copy import copy
import time


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

excel='E:\\zero\\8.20\\unk_test.xls'
data=xlrd.open_workbook('E:\\zero\\8.20\\unk_test.xls')
host=''
headers={'apikey':'','Content-Type':'application/x-www-form-urlencoded'}

#用于判断返回状态是否为200，若是往result中填入true，否则填入false
result=[]

#用于存放接口调用时间
responseTime=[]

#用于存放译文
responseText=[]

#用于存放错误信息
responseMessage=[]

table=data.sheet_by_index(0)
nrow=table.nrows

for i in range(1,nrow):
    url=host+table.cell(i,1).value
    requestMethod=table.cell(i,2).value

    #读取原文
    payload=table.cell_value(i,3).encode('utf-8')
    #print("P:", payload)
    j_data = {'text' : payload}

    ex_num=table.cell(i,5).value

    t1 = time.time()
    if requestMethod=='get':
        r=requests.get(url,headers=headers)
    elif requestMethod=='post':
        r=requests.post(url,data=j_data,headers=headers)
    if r.status_code==ex_num:
        result.append('true')

        #获取返回时间
        # responseTime.append(r.elapsed.microseconds/1000)
        responseTime.append((time.time() - t1)*1000)

        # loading body into json object
        #r.json()
        tmp_j =json.loads(r.text)
        #print("JSON:", tmp_j)
        tmp_j = parse(tmp_j)
        responseText.append(tmp_j)
        responseMessage.append('')
        # if 'message' in r.json().keys():
        #     responseMessage.append(r.json()['message'])
        # else:
        #     responseMessage.append('')
    else:
        result.append('false')
        responseText.append('')
        responseTime.append((time.time() - t1)*1000)
        responseMessage.append(r.text)
        #if 'message' in r.json().keys():
            #responseMessage.append(r.json()['message'])

        #else:responseMessage.append(json.dumps(r.json(),ensure_ascii=False))
    r.close()
    print('共有%d个url，当第%d个执行完毕' %(nrow-1,i))
book=copy(data)
sheet1=book.get_sheet(0)
for j in range(1,nrow):
    sheet1.write(j,4,responseText[j-1])
    sheet1.write(j,6,result[j-1])
    sheet1.write(j,7,responseTime[j-1])
    sheet1.write(j,8,responseMessage[j-1])
os.remove(excel)
book.save(excel)
