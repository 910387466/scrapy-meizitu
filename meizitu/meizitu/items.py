# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MeizituItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    """Scrapy自带的图片下载 参考官方文档"""
    image_urls = scrapy.Field()
    images = scrapy.Field()

