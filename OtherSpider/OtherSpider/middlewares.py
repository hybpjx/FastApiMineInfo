# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import random

import httpx
from scrapy import signals, Selector
from fake_useragent import UserAgent

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
from scrapy.http import HtmlResponse


class OtherspiderSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class OtherspiderDownloaderMiddleware:

    @staticmethod
    def Proxies() -> str:
        """
        获取代理网站的源码
        :return:
        """
        with httpx.Client() as client:
            response = client.get(
                "http://222.186.42.15:7772/laofu.aspx?OrderNumber=c0b9e7d1920c4db0fa8f410ec0498ab5&qty=1")
            text = response.text
            # 选择器
            selector = Selector(text=text)
            proxyServerIp = selector.xpath("/html/body//text()").get()
            return proxyServerIp

    def process_request(self, request, spider):
        request.headers['User-Agent'] = UserAgent(use_cache_server=False, verify_ssl=False).random
        # request.meta['proxy'] = 'http://' + self.Proxies()
        # request.meta['proxy'] = 'http://42.56.239.29:4278'

    def process_response(self, request, response, spider):

        if spider.name == "QCCinfoUrl":
            return self.Selenium_Chrome(request, spider)

        elif spider.name=="QCCinfoName":
            return self.Selenium_Chrome(request, spider)

        else:
            return response

    def Selenium_Chrome(self, request, spider):
        bro = spider.bro
        bro.get(request.url)
        source_page = bro.page_source
        new_response = HtmlResponse(url=request.url, body=source_page, request=request, encoding='utf-8')
        return new_response

    def process_exception(self, request, exception, spider):
        pass

    # def spider_opened(self, spider):
    #     bro = spider.bro
    #     bro.close()


if __name__ == '__main__':
    print(OtherspiderDownloaderMiddleware().Proxies())
