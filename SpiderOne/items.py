# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SpideroneItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    count = scrapy.Field()
    subject = scrapy.Field()
    xml_url = scrapy.Field()
    text_url = scrapy.Field()
    abstract = scrapy.Field()
    introduction = scrapy.Field()
    methods = scrapy.Field()
    results = scrapy.Field()
    discussion = scrapy.Field()
