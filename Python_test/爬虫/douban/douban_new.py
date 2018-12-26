# coding=utf-8
from urllib import request
import requests
from bs4 import BeautifulSoup
import re
import sys

def get_data():
	url = 'https://www.douban.com/explore/'
	headers = {'user-agent':'Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.194.iOS'}
	response = requests.get(url,headers=headers)
	#print(response.text)
	content = response.text
	content_soup = BeautifulSoup(content,'lxml') 
	#print(content_soup)
	content_text = content_soup.find_all(class_='title')
	#print("----------------------------------------------------------------------------------------------")
	#print(content_text)
	texts_soup = BeautifulSoup(str(content_text),'lxml')
	for tag1 in texts_soup.find_all(re.compile("^a")):
			data_url = tag1.get('href')
			#print(data_url)
			data_response = requests.get(data_url,headers=headers).text
			#print(data_response)
			data_soup = BeautifulSoup(data_response,'lxml')
			#print(data_soup)
			data_text = data_soup.find_all(id='content')
			#print(data_text)
			data_texts_soup=BeautifulSoup(str(data_text),'lxml')
			file = open('output2.txt','r+',encoding='utf-8')
			txt = file.read()
			for tag2 in data_texts_soup.find_all(re.compile("^p")):
				text = tag2.text
				print(text)
				file.write(text.replace('。','\n'))
			file.close()
if __name__ == '__main__':
	get_data()