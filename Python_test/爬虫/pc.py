#!/usr/bin/env python3

# -*- coding: utf-8 -*-

'''
python爬虫

'''
from urllib import request
from urllib import parse
from urllib import error
from bs4 import BeautifulSoup
from bs4 import element
#import chardet
import json
#正则表达式
import re
from selenium import webdriver

if __name__ == "__main__":

    #*************************************
    # Selenium
    #*************************************
    browser = webdriver.Chrome()
    browser.get('http://www.baidu.com/')    







    # *************************************
    # # Baeutiful Soup爬语料 
    # # *************************************
    # html = """
    # <html>
    # <head>
    # <title>Zero_chen</title>
    # </head>
    # <body>
    # <p class="title" name="blog"><b>My Blog</b></p>
    # <li><!--注释--></li>
    # <a href="https://blog.csdn.net/Zero_chenda/article/details/82496883" class="sister" id="link1">python错误记录之代码缩进TAB和空格混用</a><br/>
    # <a href="https://blog.csdn.net/Zero_chenda/article/details/82455165" class="sister" id="link2">python3.6.5下安装Scrapy！！</a><br/>
    # <a href="https://blog.csdn.net/Zero_chenda/article/details/82147545" class="sister" id="link3">当在Linux下运行shell bash时，一直提示文件中存在“/r”的解决方法</a><br/>
    # </body>
    # </html>
    # """
    #创建Beautiful Soup对象
    #soup = BeautifulSoup(html,'lxml')
    #print(soup.prettify())
    #print(type(soup.title)) 
    #print(soup.title.name)
    #print(soup.title.string)
    # if type(soup.li.string) == element.Comment:
    # 	print(soup.li.string)
    #print(soup.li.string)
    #print(soup.a.attrs)
    #print(soup.a.get('class')) <=> print(soup.a['class'])
    #直接子节点(不包含孙节点)
    # print(soup.body.contents) <=> print(soup.find_all(recursive=False))
    # print(soup.body.contents[1])
    #遍历获取所有子节点，它是一个 list 生成器对象
    # for child in soup.body.children:
    # 	print(child)
    #find_all() 方法搜索当前tag的所有tag子节点
    #print(soup.find_all('a'))
    #传递正则表达式,寻找b开头的tag
    #for tag in soup.find_all(re.compile("^b")):
    	#print(tag.name)
    #找到文档中所有<title>标签和<b>标签
    #print(soup.find_all(['title','b']))
    #匹配任何值
    #for tag in soup.find_all(True):
    	#print(tag.name)
    #搜索包含特殊属性的tag
    #print(soup.find_all(attrs={"class":"title"}))
    #print(soup.find_all(text="python错误记录之代码缩进TAB和空格混用"))
    #限制了返回数量
    #print(soup.find_all("a",limit=2))



    # *************************************
    # urllib.error
    # *************************************
    #一个不存在的连接
    # url = "http://www.zero_chen.com"
    # req = request.Request(url)
    # try:
    #     response = request.urlopen(req)
    # except error.URLError as e:
    #     if hasattr(e,'code'):
    #         print("HTTPError")
    #         print(e.code)
    #     elif hasattr(e,'reason'):
    #         print("URLError")
    #         print(e.reason)
	#response = request.urlopen("http://fanyi.baidu.com")
	# req = request.Request("http://fanyi.baidu.com")
	# response=request.urlopen(req)
	# # html = response.read()
	# # html = html.decode("utf-8")
	# #判断网页的编码方式
	# # charset = chardet.detect(html)
	# # print(html)
	# print("geturl打印信息：%s"%(response.geturl()))
	# print('*********************************************')
	# print("info打印信息：%s"%(response.info()))
	# print('*********************************************')
	# print("getcode打印信息：%s"%(response.getcode()))
	# print('*********************************************')
	
	
	# #有道翻译
 #    Request_Url = 'http://fanyi.youdao.com/translate'
 #    #创建Form_Data字典，存储有道的Form Data
 #    Form_Data = {}
 #    Form_Data['i'] = 'hello'
 #    Form_Data['doctype'] = 'json'
 #    # Form_Data['from'] = 'AUTO'
 #    # Form_Data['to'] = 'AUTO'
 #    # Form_Data['smartresult'] = 'dict'
 #    # Form_Data['client'] = 'fanyideskweb'
 #    # Form_Data['salt'] = '1535611863002'
 #    # Form_Data['sign'] = 'a59fa061e81855f078d26797188b2942'
 #    # Form_Data['version'] = '2.1'
 #    # Form_Data['keyfrom'] = 'fanyi.web'
 #    # Form_Data['action'] = 'FY_BY_REALTIME'
 #    # Form_Data['typoResult'] = 'false'
 #    #使用urlencode方法转换标准格式
 #    data = parse.urlencode(Form_Data).encode('utf-8')
 #    #传递Request对象和转换完格式的数据
 #    response = request.urlopen(Request_Url,data)
 #    #读取信息并解码
 #    html=response.read().decode('utf-8')
 #    #print(html)
 #    #使用JSON
 #    translate_results = json.loads(html)
 #    #找到翻译结果
 #    translate_results = translate_results['translateResult'][0][0]['tgt']
 #    #打印翻译信息
 #    print("翻译结果是：%s"%translate_results)

