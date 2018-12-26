# coding=utf-8

import requests
import sys
from bs4 import BeautifulSoup
import re



def ted_data(numpage,zhfile,enfile):
	for num in range(2,numpage+1):

		#进入ted的视频列表页

		f_url = 'https://www.ted.com/talks' + '?page=' + str(num)
		print(f_url)

		header = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
		f_response = requests.get(f_url,headers=header)
		f_content = f_response.text
		#print(f_content)
		f_content_soup = BeautifulSoup(f_content,'lxml')
		f_div_tag = f_content_soup.find_all("div",class_='talk-link')
		f_div_tag_soup = BeautifulSoup(str(f_div_tag),'lxml')
		#print(f_div_tag_soup)


		for tag in f_div_tag_soup.find_all("div",class_="media__message"):

			#获取每个视频的class_=" ga-link"的a标签
			a_link = tag.find("a",class_=" ga-link")
			content_title = a_link.get('href')
			# author_name = tag.find("h4",class_="talk-link__speaker")
			# content_author = author_name.text

			#获取每个视频的连接地址，该视频的详情页
			tag_url = 'https://www.ted.com' + content_title
			#print(tag_url)
			url = tag_url
			header = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
			response = requests.get(url,headers=header)
			content = response.text
			content_soup = BeautifulSoup(content,'lxml')

            #网页<html>页头部的link标签的“hreflang”表明了该视频的文字所有的译文语种，而且link的“href”属性值也可以让你跳转到该视频（我们要先判断是否存在某种译文语种才决定要不要跳进（也算用一个新连接打开同一个视频）该视频去获取相应数据）

			#新建一个字典用于存放link的内容
			hreflang_dict = {}

            #获取link元素中的自定义属性“hreflang”
			for link_tag in content_soup.find_all("link",attrs={"hreflang":True}):
				#print(link_tag)
				hreflang_text = link_tag.get('hreflang')
				#打印出来可用于查看语种缩写，不要想当然的以为某种语种的缩写是你想的那样			
				#print("@1:", hreflang_text)

				href_text = link_tag.get('href')
				#print("@2:", href_text)

				hreflang_dict[hreflang_text] = href_text
				
			#print(hreflang_dict)

			#判断该视频的译文语种有没有你想要的，如果有，才对它进行爬取，此处的“zh-Hans”可以换成任何你想要的语言种类

			#获取中文数据
			#判断字典的key中是否包含“zh-cn”
			if 'zh-Hans' in hreflang_dict.keys():
				print(hreflang_dict['zh-Hans'])

				#此处因为刚进入“tag_url”时，有一个默认界面，这个默认界面中没有需要的文本内容，所以还要对获取到的“href_text”进行解析 

				str_url1 = hreflang_dict['zh-Hans'].split('?')
				zh_data_url = str_url1[0] + '/transcript?' + str_url1[1]
				#print(zh_data_url)
				zh_response = requests.get(zh_data_url,headers=header)
				zh_content = zh_response.text
				zh_content_soup = BeautifulSoup(zh_content,'lxml')
				#print(zh_content_soup)			
				div_tag = zh_content_soup.find_all(class_='Grid Grid--with-gutter d:f@md p-b:4')
				#print(div_tag)
				div_tag_soup = BeautifulSoup(str(div_tag),'lxml')
				#print(div_tag_soup)

				#找到div_tag_soup中的p标签，并获取p标签中的文本
				for p_tag in div_tag_soup.find_all(re.compile('^p')):
					#print(type(p_tag))
					p_text = p_tag.text
					p_text = p_text.replace("\t","")
					p_text = p_text.replace("\n","")
					#print(p_text)
					with open(zhfile,'a+',encoding='utf-8') as zfile:
						zfile.write(p_text + '\n')
				
			#获取英文数据
				#print(hreflang_dict['en'])
				str_url2 = hreflang_dict['en'].split('?')
				en_data_url = str_url2[0] + '/transcript?' + str_url2[1]

				#为了防止意外情况发生，获取英文数据的“user-agent”换成火狐浏览器

				header2 = {'user-agent':'Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070803 Firefox/1.5.0.12'}
				en_response = requests.get(en_data_url,headers=header2)
				en_content = en_response.text
				en_content_soup = BeautifulSoup(en_content,'lxml')
				#print(en_content_soup)
				div_tag = en_content_soup.find_all(class_='Grid Grid--with-gutter d:f@md p-b:4')
				#print(div_tag)
				div_tag_soup = BeautifulSoup(str(div_tag),'lxml')

				#找到div_tag_soup中的p标签，并获取p标签中的文本
				for p_tag in div_tag_soup.find_all(re.compile('^p')):
					#print(type(p_tag))
					p_text = p_tag.text
					p_text = p_text.replace("\t","")
					p_text = p_text.replace("\n","")
					#print(p_text)
					with open(enfile,'a+',encoding='utf-8') as efile:
						efile.write(p_text + '\n')


			else:
				print("该篇没有中文翻译")


if __name__ == '__main__':
	ted_data(4,'zh','en')