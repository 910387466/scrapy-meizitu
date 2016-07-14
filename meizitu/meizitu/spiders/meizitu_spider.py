# -*- coding: UTF-8 -*-
from meizitu.items import MeizituItem
import scrapy
import re

"""
默认不下载分辨率小于 480*480 的图片,在settings.py中可自行修改限制. (ノ=Д=)ノ┻━┻

author: whoami
"""


class MeizituSpider(scrapy.Spider):
    name = 'meizitu'
    start_urls = ["http://www.meizitu.com"]
    allowed_domain = ["www.meizitu.com"]

    def parse(self, response):
        item = MeizituItem()

        '''提取图片链接'''
        item["image_urls"] = response.xpath("//div[@id='maincontent']//img/@src").extract()

        '''Python不理你并向你扔了个item'''
        yield item

        '''提取网页链接'''
        for link in response.xpath("//a/@href").extract():
            '''正则匹配链接'''
            if re.findall("/a/.*?\.html|/tag/.*?\.html", link, re.IGNORECASE):
                if link[0] == '/':
                    link = self.start_urls[0] + link  # 链接补全
                if self.start_urls[0] in link:
                    yield self.get_request(link)  # 继续抓取

    '''Pycharm提示这个方法可以是静态的 (ノ=Д=)ノ┻━┻'''
    # @staticmethod
    def get_request(self, url):
        return scrapy.Request(url)
