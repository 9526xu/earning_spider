from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


def crawlByName():
    process=CrawlerProcess(get_project_settings())
    process.crawl('earning')
    process.start()


if __name__=='__main__':
    crawlByName()