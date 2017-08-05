import scrapy
from scrapy_splash import SplashRequest


class SpiderS1(scrapy.Spider):
    name = "s1_spider"

    def start_requests(self):

        urls = ['http://www.nasdaq.com/earnings/earnings-calendar.aspx']
        #urls = ['http://car.autohome.com.cn/price/brand-15.html']
        requests = []
        for url in urls:
            url = url.strip()
            request = SplashRequest(url, callback=self.parse, args={'wait': 3})
            requests.append(request)
        return requests

    def parse(self, response):
        html = response.body
        print(html)
        table=response.xpath('//table[@id="ECCompaniesTable"]').extract_first()
        print(table)