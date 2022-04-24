import scrapy


class Chinanatureresourcepart2proSpider(scrapy.Spider):
    name = 'ChinaNatureResourcePart2Pro'
    # allowed_domains = ['xxx.com']
    start_urls = ["http://ky.mnr.gov.cn/gkxm/qtckxm/index.htm"] + [
        'http://ky.mnr.gov.cn/gkxm/qtckxm/index_{}.htm'.format(i) for i in range(300)] + \
                 ["http://ky.mnr.gov.cn/gkxm/qthdxm/index.htm"] + [
                     "http://ky.mnr.gov.cn/gkxm/qthdxm/index_{}.htm".format(i) for i in range(300)]

    # def parse(self, response, /, **kwargs) -> dict:
    #     item = {}
    #     for tr in response.css("body > div.box > div:nth-child(3) > div > div.gu-kqfw-info > table  > tr"):
    #         item["申请人"] = tr.css("td:nth-child(1)::text").get()
    #         item["项目名称"] = tr.css("td:nth-child(2)::text").get()
    #         item["设计生产规模"] = tr.css("td:nth-child(3)::text").get()
    #         item["审批机关"] = tr.css("td:nth-child(4)::text").get()
    #         item["取得方式"] = tr.css("td:nth-child(5)::text").get()
    #         item["开采主矿种"] = tr.css("td:nth-child(6)::text").get()
    #         item["受理日期"] = tr.css("td:nth-child(7)::text").get()
    #         yield item
    def parse(self, response, /, **kwargs) -> dict:
        item = {}
        for tr in response.css("body > div.box > div:nth-child(3) > div > div.gu-kqfw-info > table  > tr"):
            item["applicator"] = tr.css("td:nth-child(1)::text").get()
            item["project_name"] = tr.css("td:nth-child(2)::text").get()
            item["produce_type"] = tr.css("td:nth-child(3)::text").get()
            item["examining"] = tr.css("td:nth-child(4)::text").get()
            item["get_type"] = tr.css("td:nth-child(5)::text").get()
            item["main_mine"] = tr.css("td:nth-child(6)::text").get()
            item["create_time"] = tr.css("td:nth-child(7)::text").get()
            yield item
