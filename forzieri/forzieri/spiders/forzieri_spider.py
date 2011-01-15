#!/usr/bin/python
# -*- coding:Utf-8 -*-

'''
File: forzieri_spider.py
Author: Adrien Lemaire
Description: My first scrapy spider
'''

from scrapy.contrib.spiders import CrawlSpider
from scrapy.contrib.spiders import Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from forzieri.items import ForzieriItem


class MySpider(CrawlSpider):
    name = 'forzieri.com'
    allowed_domains = ['forzieri.com']
    start_urls = ['http://www.forzieri.com/usa/dept.asp' +\
        '?l=usa&c=usa&dept_id=999903']
    rules = (
        Rule(SgmlLinkExtractor(restrict_xpaths="id('sidebar-scroll-" +\
            "content')/ul/li/a"),
        callback='parse_item',
        follow=True),
    )

    def parse_item(self, response):
        self.log('Hi, this is an item page! %s' % response.url)
        hxs = HtmlXPathSelector(response)
        bags = hxs.select("//div[@class='data']")
        if len(bags) == 15:
            items = []
            for i in range(15):
                item = ForzieriItem()
                desc = bags[i].select("div[@id='desc_" + str(i + 1) + "']")
                item['designer'] = desc.select("h2/text()").extract()
                item['desc'] = desc.select("p/text()").extract()
                item['price'] = desc.select("h3/text()").extract()
                item['color'] = bags[i].select("div[color_" + str(i + 1) +\
                    "]/text()").extract()
                item['size'] = bags[i].select("div[size_" + str(i + 1) +\
                    "]/text()").extract()
                item['image_url'] = bags[i].select("../../a/img/@src")\
                    .extract()
                items.append(item)
            return items

SPIDER = MySpider()
