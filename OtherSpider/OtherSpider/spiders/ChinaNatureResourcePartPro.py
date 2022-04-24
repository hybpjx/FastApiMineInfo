import scrapy


class ChinanatureresourcepartproSpider(scrapy.Spider):
    name = 'ChinaNatureResourcePartPro'
    # allowed_domains = ['xxx.com']
    start_urls = ["http://ky.mnr.gov.cn/dj/ck/index.htm"]+["http://ky.mnr.gov.cn/dj/ck/index_{}.htm".format(i)for i in range(1,200)]

    # def parse(self, response,**kwargs):
    #     item={}
    #     for tr in response.css("body > div.box > div:nth-child(3) > div > div.gu-kqfw-info > table  > tr"):
    #         item["许可证号"]=tr.css("td:nth-child(1)::text").get()
    #         item["采矿权人"]=tr.css("td:nth-child(2)::text").get()
    #         item["矿山名称"]=tr.css("td:nth-child(3)::text").get()
    #         item["项目类型"]=tr.css("td:nth-child(4)::text").get()
    #         item["开采主矿种"]=tr.css("td:nth-child(5)::text").get()
    #         item["开采方式"]=tr.css("td:nth-child(6)::text").get()
    #         item["设计生产规模"]=tr.css("td:nth-child(7)::text").get()
    #         item["面积(km²)"]=tr.css("td:nth-child(8)::text").get()
    #         item["有效期)"]=tr.css("td:nth-child(9)::text").get()
    #         item["发证机关)"]=tr.css("td:nth-child(10)::text").get()
    #         item["公告日期)"]=tr.css("td:nth-child(11)::text").get()
    #         yield item
    def parse(self, response,**kwargs):
        item={}
        for tr in response.css("body > div.box > div:nth-child(3) > div > div.gu-kqfw-info > table  > tr"):
            item["许可证号"]=tr.css("td:nth-child(1)::text").get()
            item["采矿权人"]=tr.css("td:nth-child(2)::text").get()
            item["矿山名称"]=tr.css("td:nth-child(3)::text").get()
            item["项目类型"]=tr.css("td:nth-child(4)::text").get()
            item["开采主矿种"]=tr.css("td:nth-child(5)::text").get()
            item["开采方式"]=tr.css("td:nth-child(6)::text").get()
            item["设计生产规模"]=tr.css("td:nth-child(7)::text").get()
            item["面积(km²)"]=tr.css("td:nth-child(8)::text").get()
            item["有效期)"]=tr.css("td:nth-child(9)::text").get()
            item["发证机关)"]=tr.css("td:nth-child(10)::text").get()
            item["公告日期)"]=tr.css("td:nth-child(11)::text").get()
            yield item
