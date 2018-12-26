# -*- coding:UFT-8 -*-
import scrapy


class google_jk_spider(scrapy.Spider):
	name = "google_jk"
	allowed_domains = ['translate.google.cn']
	headers = {
	'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
	'User-Agent':'Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.194.iOS'
	}
	def start_requests(self):
		url = r'https://translate.google.cn/translate_a/single?client=t&sl=en&tl=zh-CN&hl=en&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&source=btn&ssel=3&tsel=0&kc=0&tk=643902.1005513&q=hello%20world%EF%BC%81'
		
		yield Request(url,headers=self.headers,data)

	def parse(self,reponse):

