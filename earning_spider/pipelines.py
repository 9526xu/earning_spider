# -*- coding: utf-8 -*-


import datetime
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re
from contextlib import contextmanager

from sqlalchemy import DATETIME, and_, create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker

# Define your item pipelines here
#
from earning_spider.model import NASDAQ_earning
from earning_spider.settings import DATABASE
from scrapy.exceptions import DropItem


@contextmanager
def session_scope(session):
    """Provide a transactional scope around a series of operations."""
    print("事务开始")
    sess = session()
    try:
        yield sess
        sess.commit()
    except:
        print("事务回滚")
        sess.rollback()
        raise
    finally:
        print("事务结束")
        sess.close()


class EarningPipline(object):

    def __init__(self):
        engine = create_engine(URL(**DATABASE))
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        # 去重，已时间与 code 去重
        session = self.Session()

        now = datetime.datetime.now().strftime('%Y-%m-%d')
        tomorrow = (datetime.timedelta(days=1) +
                    datetime.datetime.now()).strftime('%Y-%m-%d')

        total = item['company']
        # 资本值
        capital_amount = re.search(r'\$\w+\.\w+', total).group()
        # 公司
        company = total[:total.find('(')].strip()
        # 股票代码
        url = item['company_url']
        code = url.split('/')[-1]
        expectDate = item['expect_report_date']
        # 根据期望日期与 code 去重
        query = session.query(NASDAQ_earning).filter(and_(
            NASDAQ_earning.code == code, NASDAQ_earning.expect_date == expectDate))
        count = query.count()

        if(count >= 1):
            raise DropItem('已经存在这个公司财报信息%s' % item)

        # 构建数据库对象
        earning = NASDAQ_earning(
            company=company, code=code,
            capital_amount=capital_amount, expect_date=expectDate,
            deadline_date=item['fiscal_quarter_ending'], per_share_earnings_expect=item['consensus'],
            expect_num=item['ests'], last_year_report_date=item['last_yeat_report_date'],
            last_year_per_share_earnings=item['last_year_eps'],
            publish_time=item['time'], title=item['company'])
        # session 对象
        with session_scope(self.Session) as sess:
            sess.add(earning)
