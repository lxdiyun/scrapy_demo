# -*- coding: utf-8 -*-
import re
import scrapy
from scrapy import log
from scrapy.utils.response import get_base_url
from scrapy.utils.url import urljoin_rfc
from html2text import HTML2Text

from acfun.items import AcfunItem


class WenzhangSpider(scrapy.Spider):
    name = "wenzhang"
    allowed_domains = ["acfun.tv"]
    start_urls = (
        'http://www.acfun.tv/v/list110/index.htm',
    )

    def parse(self, response):
        base_url = get_base_url(response)
        page_hrefs = response.xpath(
            '//div[@class="area-pager"]/a/@href').extract()
        item_hrefs = response.xpath(
            '//div[@class="item"]/a[@class="title"]/@href').extract()

        for href in page_hrefs:
            url = urljoin_rfc(response.url, href)
            log.msg(url, level=log.DEBUG)
            yield scrapy.Request(url)

        for href in item_hrefs:
            yield scrapy.Request(urljoin_rfc(base_url, href),
                                 callback=self.parse_item)

    def parse_item(self, response):
        log.msg(response.url, level=log.DEBUG)
        item = AcfunItem()
        converter = HTML2Text()
        id_r = re.compile('.*ac(\d+)$')

        item['id'] = id_r.sub(r"\1", response.url)
        item['url'] = response.url
        item['title'] = response.xpath('//h1[@id="txt-title-view"]/text()').extract()[0].strip()
        content_html = response.xpath('//div[@id="area-player"]').extract()[0]
        item['content'] = converter.handle(content_html)

        yield item

