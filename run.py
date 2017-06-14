from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from earning_spider.spiders.earningSpider import EarningSpider



def crawlByName():
    print(get_project_settings())
    process = CrawlerProcess(get_project_settings())

    process.crawl(EarningSpider)
    process.start()



if __name__ == '__main__':
    crawlByName()
