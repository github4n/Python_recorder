# -*- coding:UTF-8 -*-
from urllib import request
from bs4 import BeautifulSoup
import re
import sys


if __name__ == '__main__':
    #创建txt文件
    file = open('Corpus.txt','r+',encoding='utf-8')
    txt = file.read()
    #Corpus的地址
    target_url = 'http://www.hjenglish.com/yingyugushi/p1218680/'
    #User-Agent
    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.194.iOS'
    target_req = request.Request(url = target_url, headers = head)
    target_response = request.urlopen(target_req)
    target_html = target_response.read().decode(encoding = 'UTF-8',errors = 'strict')
    #创建BeautifulSoup对象
    content_soup = BeautifulSoup(target_html,'lxml')
    #print(content_soup)
    #搜索文档树,找出div标签中class为article-content的所有子标签
    content = content_soup.find_all(class_ = 'article-content')
    #使用查询结果再创建一个BeautifulSoup对象,对其继续进行解析
    texts_soup = BeautifulSoup(str(content),'lxml')
    #print(texts_soup)
    for tag in texts_soup.find_all(re.compile("^d")):
        tag_class = tag.get('class')
        tag_class = " ".join(tag_class)
        #print(tag_class)       
        #print(type(tag_class))
        if(tag_class == 'langs_en' or tag_class == 'langs_cn' ):
            print(tag.text + '\n\n')
            file.write(tag.text + '\n')
    file.close()

    # texts = texts_soup.find_all(re.compile("^d"))
    # print(texts)
    # for each in texts:
    #     #print(type(each))
    #     print(each.text + '\n\n')

