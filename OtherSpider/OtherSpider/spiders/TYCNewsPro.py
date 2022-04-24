import scrapy


class TycnewsproSpider(scrapy.Spider):
    name = 'TYCNewsPro'
    # allowed_domains = ['xxx.com']
    start_urls = ['https://www.tianyancha.com/company/27061777', 'https://www.tianyancha.com/company/684138533',
                  'https://www.tianyancha.com/company/2358171976', 'https://www.tianyancha.com/company/2362161647',
                  'https://www.tianyancha.com/company/2362161378', 'https://www.tianyancha.com/company/2362162514',
                  'https://www.tianyancha.com/company/2362161059', 'https://www.tianyancha.com/company/2362163897',
                  'https://www.tianyancha.com/company/2357919359', 'https://www.tianyancha.com/company/2362160431',
                  'https://www.tianyancha.com/company/2362160496', 'https://www.tianyancha.com/company/2362160496',
                  'https://www.tianyancha.com/company/2362166244', 'https://www.tianyancha.com/company/2362165590',
                  'https://www.tianyancha.com/company/2362162501', 'https://www.tianyancha.com/company/4669437011',
                  'https://www.tianyancha.com/company/2315025987', 'https://www.tianyancha.com/company/3014992090',
                  'https://www.tianyancha.com/company/3014992135', 'https://www.tianyancha.com/company/3014992169',
                  'https://www.tianyancha.com/company/689746786', 'https://www.tianyancha.com/company/2319763932',
                  'https://www.tianyancha.com/company/239298932', 'https://www.tianyancha.com/company/239301199',
                  'https://www.tianyancha.com/company/324151981', 'https://www.tianyancha.com/company/324152341',
                  'https://www.tianyancha.com/company/324152147', 'https://www.tianyancha.com/company/324152016',
                  'https://www.tianyancha.com/company/324152042', 'https://www.tianyancha.com/company/3464825017',
                  'https://www.tianyancha.com/company/850428664', 'https://www.tianyancha.com/company/758122337',
                  'https://www.tianyancha.com/company/456521453', 'https://www.tianyancha.com/company/447644584',
                  'https://www.tianyancha.com/company/300349877', 'https://www.tianyancha.com/company/449374649',
                  'https://www.tianyancha.com/company/254266832', 'https://www.tianyancha.com/company/435124314',
                  'https://www.tianyancha.com/company/809120109', 'https://www.tianyancha.com/company/2848789746',
                  'https://www.tianyancha.com/company/413041358', 'https://www.tianyancha.com/company/726213583',
                  'https://www.tianyancha.com/company/1574995556', 'https://www.tianyancha.com/company/265160608',
                  'https://www.tianyancha.com/company/707641328', 'https://www.tianyancha.com/company/24485663',
                  'https://www.tianyancha.com/company/835172543', 'https://www.tianyancha.com/company/382703140',
                  'https://www.tianyancha.com/company/2358818085', 'https://www.tianyancha.com/company/980981012',
                  'https://www.tianyancha.com/company/453246868', 'https://www.tianyancha.com/company/857967543',
                  'https://www.tianyancha.com/company/299265935', 'https://www.tianyancha.com/company/238121499',
                  'https://www.tianyancha.com/company/364961550', 'https://www.tianyancha.com/company/265231798',
                  'https://www.tianyancha.com/company/440306833', 'https://www.tianyancha.com/company/252722115',
                  'https://www.tianyancha.com/company/3043493831', 'https://www.tianyancha.com/company/449157666',
                  'https://www.tianyancha.com/company/625502355', 'https://www.tianyancha.com/company/833844057']

    def parse(self, response):
        item = {}
        item["公司名"] = response.css("#company_web_top > div.box.-company-box > div.content > div.header > span > span > h1::text").get()
        item["公司url地址"] = response.url
        for tr in response.xpath('//*[@id="_container_findNewsCount"]/div[1]/div'):
            item["标题"] = tr.xpath('./div/div[1]/a/text()').get()
            item["详细内容"] = tr.xpath('./div/div[3]/text()').get()
            item["来源"] = tr.xpath('./div/div[4]/span[1]/text()').get()
        yield item
