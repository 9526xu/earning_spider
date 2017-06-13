import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, create_engine, Integer, String, DATETIME
from sqlalchemy.engine.url import URL
from earning_spider.settings import DATABASE

Base = declarative_base()


def _get_date():
    return datetime.datetime.now()


class NASDAQ_earning(Base):
    """nqsdaq财报表"""
    __tablename__ = 'nasdq_earning'
#     `earning_id` bigint(11) unsigned NOT NULL AUTO_INCREMENT,
#   `gmt_create` datetime DEFAULT NULL,
#   `gmt_modified` datetime DEFAULT NULL,
#   `is_deleted` tinyint(4) DEFAULT 0 COMMENT '是否删除',
#   `publish_time` datetime DEFAULT NULL,
#   `company` varchar(200) DEFAULT NULL COMMENT'公司',
#   `code` varchar(200) DEFAULT NULL COMMENT'美股股票代码',
#   `capital_amount` varchar(200) DEFAULT NULL COMMENT'资本总值',
#   `expect_date` varchar(200) DEFAULT NULL COMMENT'预期报告日',
#   `deadline_date` varchar(200) DEFAULT NULL COMMENT '财季截止',
#   `per_share_earnings_expect` varchar(200) DEFAULT NULL COMMENT'平均每股收益',
#   `expect_num` varchar(200) DEFAULT NULL COMMENT'预测数',
#   `last_year_report_date` varchar(200) DEFAULT NULL COMMENT'去年报告日'，
#   `last_year_per_share_earnings` varchar(200) DEFAULT NULL COMMENT'去年每股收益',
    earning_id = Column(Integer, primary_key=True)
    gmt_create = Column(DATETIME, default=_get_date)
    gmt_modified = Column(DATETIME, default=_get_date)
    is_deleted = Column(Integer, default=0)
    company = Column(String(200))
    code = Column(String(200))
    capital_amount = Column(String(200))
    expect_date = Column(String(200))
    deadline_date = Column(String(200))
    per_share_earnings_expect = Column(String(200))
    expect_num = Column(String(200))
    last_year_report_date = Column(String(200))
    last_year_per_share_earnings = Column(String(200))
    publish_time = Column(String(200))
    title = Column(String(200))
