#!/usr/bin/python
# -*- coding:Utf-8 -*-

'''
File: pipelines.py
Author: Adrien Lemaire
Description: Pipeline file to store data
'''

from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.core.exceptions import DropItem
from scrapy.http import Request
from scrapy.xlib.pydispatch import dispatcher
from scrapy.core import signals
from scrapy.contrib.exporter import XmlItemExporter


class ForzieriPipeline(object):

    def process_item(self, spider, item):
        return item


class MyImagesPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        yield Request(item['image_url'][0])

    def item_completed(self, results, item, info):
        image_path = [info['path'] for success, info in results if success]
        if not image_path:
            raise DropItem("Item contains no image")
        item['image_path'] = image_path
        return item


class XmlExportPipeline(object):

    def __init__(self):
        dispatcher.connect(self.spider_opened, signals.spider_opened)
        dispatcher.connect(self.spider_closed, signals.spider_closed)
        self.files = {}

    def spider_opened(self, spider):
        file = open('%s_products.xml' % spider.name, 'w+b')
        self.files[spider] = file
        self.exporter = XmlItemExporter(file)
        self.exporter.start_exporting()

    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        file = self.files.pop(spider)
        file.close()

    def process_item(self, spider, item):
        self.exporter.export_item(item)
        return item
