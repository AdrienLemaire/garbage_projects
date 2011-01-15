#!/usr/bin/python
# -*- coding:Utf-8 -*-

'''
File: settings.py
Author: Adrien Lemaire
Description: Scrapy settings for forzieri project
'''

BOT_NAME = 'forzieri'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['forzieri.spiders']
NEWSPIDER_MODULE = 'forzieri.spiders'
DEFAULT_ITEM_CLASS = 'forzieri.items.ForzieriItem'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

# Images
ITEM_PIPELINES = [
    'forzieri.pipelines.MyImagesPipeline',
    'forzieri.pipelines.XmlExportPipeline'
]
IMAGES_STORE = 'img'
IMAGES_THUMBS = {
    'small': (50, 50),
    'big': (270, 270),
}
