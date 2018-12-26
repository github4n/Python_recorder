# coding=utf-8

import requests
import re
from bs4 import BeautifulSoup


def get_corpus(url_content,numpage,outfile):
	for num in range(2,numpage+1):
		print(num)
		#url = url_content
		url = url_content + 'xinwen/' + 'page'+ str(num) + '/'
		print(url)
		headers= {'user-agent':'Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070803 Firefox/1.5.0.12'}
		response = requests.get(url,headers=headers)
		content = response.text
		#print(content)
		content_soup = BeautifulSoup(content,'lxml')
		#print(content_soup)
		#找到包含a链接的li标签
		li_tag = content_soup.find_all(class_='article-item')
		li_tag_soup = BeautifulSoup(str(li_tag),'lxml')
		#print(li_tag_soup)
		#找到a标签
		for tag in li_tag_soup.find_all(class_='big-link title-article'):
			#找到存放数据的地址
			url_id = tag.get('href').split('/')
			#print(url_id)
			data_url = url_content + url_id[2] + '/'
			#print(data_url)
			data_response = requests.get(data_url,headers=headers)
			data_content = data_response.text
			data_content_soup = BeautifulSoup(data_content,'lxml')
			#print(data_content_soup)
			data_texts_soup = BeautifulSoup(str(data_content_soup.find_all(class_ = 'article-content')),'lxml')
			#print(data_texts_soup)
			#爬取数据
			for tag in data_content_soup.find_all(re.compile('^d')):
				tag_class = tag.get('class')
				if tag_class:
					tag_class = " ".join(tag_class)
					#print(tag_class)
					if(tag_class == 'langs_en' or tag_class == 'langs_cn'):
						tag_text = tag.text
						print(tag_text)
						with open(outfile,'a+',encoding='utf-8') as file:
							file.write(tag_text + '\n')





if __name__ == '__main__':
	get_corpus('https://jp.hjenglish.com/new/',5,'output.txt') 

