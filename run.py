import subprocess
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from earning_spider.spiders.earningSpider import EarningSpider
from apscheduler.schedulers.blocking import BlockingScheduler


def crawlByName():
    print(get_project_settings())
    process = CrawlerProcess(get_project_settings())

    process.crawl(EarningSpider)
    process.start()

# 采用命令的方法来调用Scrapy http://gogit.itfanr.cc/xueer/CodeArticle/src/f2cfe75270a732e6298bc3567c8ee855a4453b08/Subject/Scrapy/Scrapy%E7%88%AC%E8%99%AB%E5%A6%82%E4%BD%95%E5%AE%9A%E6%97%B6%E6%89%A7%E8%A1%8C%E4%B9%8B%E4%B8%80.md
def spider_comm():
    # (a, b) = commands.getstatusoutput("scrapy crawl cnblog")
    print('爬取程序开始')
    out_bytes = subprocess.check_output("scrapy crawl earning", shell=True)
    out_text = out_bytes.decode('utf-8')
    print(out_text)


def earning_scheduler():
    print('开始执行')
    scheduler = BlockingScheduler()
    scheduler.add_job(spider_comm, 'interval',hour=1)
    scheduler.start()

if __name__ == '__main__':
    earning_scheduler()
    # crawlByName()
