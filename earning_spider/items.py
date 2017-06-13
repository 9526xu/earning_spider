# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class EarningSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
import scrapy


class EarnItenm(scrapy.Item):
    # Time
    time = scrapy.Field()
    # company
    company = scrapy.Field()
    # Expected Report Date
    expect_report_date = scrapy.Field()
    # Fiscal Quarter Ending
    fiscal_quarter_ending = scrapy.Field()
    # Consensus EPS* Forecast
    consensus = scrapy.Field()
    #  of Ests
    ests = scrapy.Field()
    # Last Year's Report Date
    last_yeat_report_date = scrapy.Field()
    # Last Year's EPS
    last_year_eps = scrapy.Field()
    #market cap
    market_cap=scrapy.Field()
    # company_url
    company_url=scrapy.Field()