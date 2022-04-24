"""

鞍山市公共资源交易中心

"""
import operator

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re


# http://www.asggzyjy.cn/
class AnshancitypublicresourceproSpider(CrawlSpider):
    name = 'AnShanCityPublicResourcePro'
    # allowed_domains = ['xxx.com']
    start_urls = ['http://www.asggzyjy.cn/zjjy/029003/about.html',
                  'http://www.asggzyjy.cn/zjjy/029001/about.html',
                  'http://www.asggzyjy.cn/zfcg/015002/about.html',
                  'http://www.asggzyjy.cn/zfcg/015001/about.html',
                  'http://www.asggzyjy.cn/tdjy/016003/about.html',
                  'http://www.asggzyjy.cn/tdjy/016001/about.html',
                  'http://www.asggzyjy.cn/kqjy/018002/about.html',
                  'http://www.asggzyjy.cn/kqjy/018001/about.html',
                  'http://www.asggzyjy.cn/gcjs/014003/about.html',
                  'http://www.asggzyjy.cn/gcjs/014001/about.html',
                  ]

    rules = (
        Rule(LinkExtractor(allow=r'http://www.asggzyjy.cn/zjjy/\d+\/\d+\.html'), follow=True),
        Rule(LinkExtractor(allow=r'http://www.asggzyjy.cn/zjjy/\d{8}\/.*'), callback='parse_item'),

        # Rule(LinkExtractor(allow=r'http://www.asggzyjy.cn/zjjy/029001/\d+\.html'), follow=True),
        # Rule(LinkExtractor(allow=r'http://www.asggzyjy.cn/zjjy/029001/.*'), callback='parse_item'),
        #
        # Rule(LinkExtractor(allow=r'http://www.asggzyjy.cn/zjjy/015002/\d+\.html'), follow=True),
        # Rule(LinkExtractor(allow=r'http://www.asggzyjy.cn/zjjy/015002/.*'), callback='parse_item'),
        #
        # Rule(LinkExtractor(allow=r'http://www.asggzyjy.cn/zjjy/015001/\d+\.html'), follow=True),
        # Rule(LinkExtractor(allow=r'http://www.asggzyjy.cn/zjjy/015001/.*'), callback='parse_item'),
        #
        # Rule(LinkExtractor(allow=r'http://www.asggzyjy.cn/zjjy/016003/\d+\.html'), follow=True),
        # Rule(LinkExtractor(allow=r'http://www.asggzyjy.cn/zjjy/016003/.*'), callback='parse_item'),
        #
        # Rule(LinkExtractor(allow=r'http://www.asggzyjy.cn/zjjy/016001/\d+\.html'), follow=True),
        # Rule(LinkExtractor(allow=r'http://www.asggzyjy.cn/zjjy/016001/.*'), callback='parse_item'),
        #
        # Rule(LinkExtractor(allow=r'http://www.asggzyjy.cn/zjjy/018002/\d+\.html'), follow=True),
        # Rule(LinkExtractor(allow=r'http://www.asggzyjy.cn/zjjy/018002/.*'), callback='parse_item'),
        #
        # Rule(LinkExtractor(allow=r'http://www.asggzyjy.cn/zjjy/018001/\d+\.html'), follow=True),
        # Rule(LinkExtractor(allow=r'http://www.asggzyjy.cn/zjjy/018001/.*'), callback='parse_item'),
        #
        # Rule(LinkExtractor(allow=r'http://www.asggzyjy.cn/zjjy/014003/\d+\.html'), follow=True),
        # Rule(LinkExtractor(allow=r'http://www.asggzyjy.cn/zjjy/014003/.*'), callback='parse_item'),
        #
        # Rule(LinkExtractor(allow=r'http://www.asggzyjy.cn/zjjy/014001/\d+\.html'), follow=True),
        # Rule(LinkExtractor(allow=r'http://www.asggzyjy.cn/zjjy/014001/.*'), callback='parse_item'),

    )

    # jincheng人民政府门户网站 梅州市生态环境局 部门文件
    def parse_item(self, response):
        # 调用item
        item = {}
        # 写入链接提取器中获取到的url
        item['title_url'] = response.url
        # 标题名字
        item['title_name'] = response.css('.ewb-info h2::text').get()

        title_date:str = response.css("div.ewb-sources > span::text").get()

        item['title_date'] = title_date.split('：')[1]

        if operator.contains(str(item["title_url"]),"029003"):
            item['site_path_url'] = self.start_urls[0]
        elif operator.contains(str(item["title_url"]),"029001"):
            item['site_path_url'] = self.start_urls[1]
        elif operator.contains(str(item["title_url"]),"015002"):
            item['site_path_url'] = self.start_urls[2]
        elif operator.contains(str(item["title_url"]),"015001"):
            item['site_path_url'] = self.start_urls[3]
        elif operator.contains(str(item["title_url"]),"016003"):
            item['site_path_url'] = self.start_urls[4]
        elif operator.contains(str(item["title_url"]),"016001"):
            item['site_path_url'] = self.start_urls[5]
        elif operator.contains(str(item["title_url"]),"018002"):
            item['site_path_url'] = self.start_urls[6]
        elif operator.contains(str(item["title_url"]),"018001"):
            item['site_path_url'] = self.start_urls[7]
        elif operator.contains(str(item["title_url"]),"014003"):
            item['site_path_url'] = self.start_urls[8]
        elif operator.contains(str(item["title_url"]),"014001"):
            item['site_path_url'] = self.start_urls[9]
        else:
            yield None
        # 内容提取 含源码
        item['content_html'] = response.css('.ewb-info').get()

        # 交给item处理
        yield item
