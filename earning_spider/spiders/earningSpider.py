import scrapy
from earning_spider.items import EarnItenm


class EarningSpider(scrapy.Spider):
    name = "earning"

    def start_requests(self):
        urls = ['http://m.nasdaq.com/zh/earnings']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        self.log("crawl na")
        trs = response.xpath(
            '//div[@class="stock-tab _tab-1 active"]//table[@id="table-saw"]/tbody/tr')

        trs2 = response.xpath(
            '//div[@class="stock-tab _tab-2"]//table[@id="table-saw"]/tbody/tr')
        for tr_html in trs:
            yield self.parseTable(tr_html)
        for tr_html in trs2:
            yield self.parseTable(tr_html)

    def parseTable(self, tr_html):
        item = EarnItenm()
        item['time'] = tr_html.xpath(
            './td[1]//a/@title').extract_first().strip()
        item['company'] = tr_html.xpath(
            './td[2]//a/text()').extract_first().strip()
        # item['market_cap'] = tr_html.xpath(
        #     './td[2]/a///b/text()').extract_first()
        item['company_url'] = tr_html.xpath(
            './/td[2]/a/@href').extract_first().strip()
        item['expect_report_date'] = tr_html.xpath(
            './td[3]/text()').extract_first().strip()
        item['fiscal_quarter_ending'] = tr_html.xpath(
            './td[4]/text()').extract_first().strip()
        item['consensus'] = tr_html.xpath(
            './td[5]/text()').extract_first().strip()
        item['ests'] = tr_html.xpath('./td[6]/text()').extract_first().strip()
        item['last_yeat_report_date'] = tr_html.xpath(
            './td[7]/text()').extract_first().strip()
        item['last_year_eps'] = tr_html.xpath(
            './td[8]/text()').extract_first().strip()
        # print(item['company'])
        return item
