#!/usr/bin/python
# -*- coding:Utf-8 -*-

'''
File: items.py
Author: Adrien Lemaire
Description: file with ForzieriItem class to store bags
'''

from scrapy.item import Item
from scrapy.item import Field


class ForzieriItem(Item):
    #name = Field()
    #url = Field()
    designer = Field()
    desc = Field()
    price = Field()
    color = Field()
    size = Field()
    image_url = Field()
    image_path = Field()
