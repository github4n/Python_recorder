# -*- coding:UTF-8 -*-

from scrapy import Request
import scrapy
from pc_scr.items import DoubanMovieItem

class DoubamMovieTop250Spider(scrapy.Spider):
	name = "douban_movie_top250"
	allowed_domains = ["movie.douban.com"]
	headers = {
	'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
	'User-Agent':'Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.194.iOS'
	}
	def start_requests(self):
		url = "https://movie.douban.com/top250"
		yield Request(url,headers=self.headers)


	def parse(self,response):
		item = DoubanMovieItem()
		movies = response.xpath('//ol[@class = "grid_view"]/li')
		for movie in movies:
			item['ranking'] = movie.xpath('.//div[@class ="pic"]/em/text()').extract()[0]
			item['movie_name'] = movie.xpath('.//div[@class ="hd"]/a/span[1]/text()').extract()[0]
			item['score'] = movie.xpath('.//div[@class ="star"]/span[@class="rating_num"]/text()').extract()[0]
			item['score_num'] = movie.xpath('.//div[@class="star"]/span[4]/text()').extract()[0]
			yield item
		#下一页
		next_url = response.xpath('//span[@class ="next"]/a/@href').extract()
		if next_url:
			next_url = "https://movie.douban.com/top250" + next_url[0]
			yield Request(next_url,headers=self.headers)
