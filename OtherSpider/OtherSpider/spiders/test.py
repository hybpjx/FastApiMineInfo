"""
大观区人民政府


selenium 爬取

"""
import copy
import re
import scrapy
import scrapy_splash


class AnqingdaguanguanareagovproSpider(scrapy.Spider):
    name = 'test'
    # allowed_domains = ['xxx.com']
    start_urls = ['http://www.aqdgq.gov.cn/zwdt/ztzl/hjbhzt/hjyw/index.html']

    def start_requests(self):
        url_list = ["https://www.aqdgq.gov.cn/content/column/2000015051?pageIndex={}".format(i + 2) for i in
                    range(23)] + self.start_urls

        for url in url_list:
            yield scrapy.Request(
                url=url,
                callback=self.parse,
                headers={
                    "host":"www.aqdgq.gov.cn"
                },
            )

    def parse(self, response, **kwargs):
        item = {}
        for li in response.xpath('//*[@id="container"]/div[3]/div[2]/div[2]/div[3]/div[2]/ul/li'):
            item["title_url"] = li.xpath('./a/@href').extract_first()
            item['title_name'] = li.xpath('./a/@title').extract_first()
            item['title_date'] = li.xpath('./span/text()').extract_first()
            item['site_path_url'] = self.start_urls[0]
            yield scrapy.Request(
                url=item['title_url'],
                callback=self.parse_detail,
                headers={
                    "host": "www.aqdgq.gov.cn"
                },
                meta={'item': copy.deepcopy(item)},
            )

    def parse_detail(self, response):
        item = response.meta['item']

        item["content_html"] = response.xpath('//*[@id="color_printsssss"]').extract_first()

        if item['content_html'] is None:
            item['content_html'] = response.text
        print(item['title_name'], item['title_url'], item['title_date'])
