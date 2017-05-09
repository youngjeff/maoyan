# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CralerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field() # 电影的id
    #cover = scrapy.Field()
    name = scrapy.Field()
    score = scrapy.Field()
    #url = scrapy.Field()
    tags = scrapy.Field() # 电影的类型
    countries = scrapy.Field()
    duration = scrapy.Field() # 电影的时长
    time = scrapy.Field()
    
