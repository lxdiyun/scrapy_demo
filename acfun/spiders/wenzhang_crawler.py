# -*- coding: utf-8 -*-
import re
import scrapy
from scrapy import log
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from html2text import HTML2Text

from acfun.items import AcfunItem



class WenzhangCrawlerSpider(CrawlSpider):
    name = 'wenzhang_crawler'
    allowed_domains = ['www.acfun.tv']
    start_urls = ['http://www.acfun.tv/v/list110/index.htm']

    rules = (
        Rule(LinkExtractor(allow=r'/a/ac\d+$'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'index_\d+.htm$'), callback='parse', follow=True),
    )

    def parse_item(self, response):
        log.msg(response.url, level=log.DEBUG)
        item = AcfunItem()
        converter = HTML2Text()
        id_r = re.compile('.*ac(\d+)$')

        item['id'] = id_r.sub(r"\1", response.url)
        item['id_n'] = int(id_r.sub(r"\1", response.url))
        item['url'] = response.url
        item['title'] = response.xpath('//h1[@id="txt-title-view"]/text()').extract()[0].strip()
        content_html = response.xpath('//div[@id="area-player"]').extract()[0]
        item['content'] = converter.handle(content_html)

        yield item
