 # -*- coding: utf-8 -*-

from scrapy import signals
#导入随机模块
import random
#导入有关ip池的模块
from scrapy.downloadermiddlewares.httpproxy import HttpProxyMiddleware
#导入有关用户代理的模块
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware


#设置IP池
IPPOOL = [
{"ipaddr":"59.32.37.134:8010"},
{"ipaddr":"61.157.206.175:41669"},
{"ipaddr":"116.62.134.173:9999"}
]

 #设置用户代理池
# UPPOOL = [
# " Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
# " Mozilla/5.0 (Windows NT 10.0; Win64; x64 ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36 " , 
# " Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393 " 
# ]

class PcScrSpiderMiddleware(object):
    @classmethod
    def from_crawler(cls, crawler):
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        return None

    def process_spider_output(self, response, result, spider):
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        pass

    def process_start_requests(self, start_requests, spider):     
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

class MyMiddleware(object):
    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s


    #ip
    def __init__(self,ip=''):
        self.ip=ip
    def process_request(self, request, spider):
        item = random.choice(IPPOOL)
        try:
            print("当前的IP是：" + item["ipaddr"])
            request.meta["proxy"] = "https://" +item["ipaddr"]
        except Exception as e:
            print(e)
            pass
        return None
    

    #uesr_agent
    # def __init__(self,user_agent = ''):
    #     self.user_agent = user_agent
    # def process_request(self,request,spider):
    #     item = random.choice(UPPOOL)
    #     try:
    #         print("当前的User—Agent是：" + item)
    #         request.headers.setdefault('User—Agent',item)
    #     except Exception as e:
    #         print(e)
    #         pass        
    #     return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
