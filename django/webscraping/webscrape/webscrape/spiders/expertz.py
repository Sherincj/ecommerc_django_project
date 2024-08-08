import scrapy
from bs4 import BeautifulSoup as bs
from ..items import WebscrapeItem


class ExpertzSpider(scrapy.Spider):
    name = "expertz"
    allowed_domains = ["www.expertzlab.com"]
    start_urls = ["https://www.expertzlab.com"]

    # def parse(self, response):
    #         course=(response.xpath('//div[@class="course"]/h4/a/text()').getall())
    #         print(course)


    # def parse(self, response):
    #     val=bs(response.text)
    #     new=val.findAll('div',attrs={'class':"course"})
    #     for crs in new:
    #         yield scrapy.Request(self.start_urls[0]+crs.h4.a['href'],callback=self.cousedet)



    # def cousedet(self,response):
    #     print(response.xpath('//div[@class="row"]/div/div[@class="col-lg-12 col-md-12 col-sm-12"]/h2/text()').get())
    
















# def parse(self, response):
#         course=(response.xpath('div[@class="course"]/h4/a/text()').getall())
#         print(course)




    # def parse(self, response):
    #     val=bs(response.text)
    #     new=val.findAll('div',attrs={'class':"course"})
    #     for crs in new:
    #        item=WebscrapeItem()
    #        item['name']=crs.h4.a.text
    #        item['desc']=crs.ul.li.text
    #        item['duration']="7months"
    #        yield item
