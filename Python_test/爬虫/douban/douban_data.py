# coding=utf-8
from urllib import request
import requests
from bs4 import BeautifulSoup
import re
import sys

def get_data():
	file = open('output.txt','r+',encoding='utf-8')
	txt = file.read()
	url = 'https://www.douban.com/note/696411423/'
	headers = {'user-agent':'Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.194.iOS'}
	response = requests.get(url,headers=headers)
	print(response.text)
	content = response.text
	content_soup = BeautifulSoup(content,'lxml') 
	print(content_soup)
	content_text = content_soup.find_all(id='content')
	print("----------------------------------------------------------------------------------------------")
	print(content_text)
	texts_soup = BeautifulSoup(str(content_text),'lxml')
	for tag in texts_soup.find_all(re.compile("^p")):
			print(tag.text)
			file.write(tag.text.replace('。','\n'))
	file.close()
if __name__ == '__main__':
	get_data()