# -*- coding: utf-8 -*-
import scrapy


class CpwsSpider(scrapy.Spider):
    name = 'cpws'
    allowed_domains = ['wenshu.court.gov.cn']
    start_urls = ['http://wenshu.court.gov.cn/']

    def parse(self, response):
        pass
