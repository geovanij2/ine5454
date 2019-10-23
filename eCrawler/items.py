# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class EcrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class Team(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()

class Player(scrapy.Item):
    # define the fields for your item here like:
    nick = scrapy.Field()
    name = scrapy.Field()
    age = scrapy.Field()
    team = scrapy.Field()
    country = scrapy.Field()