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
    name = scrapy.Field()

class Player(scrapy.Item):
    nick = scrapy.Field()
    name = scrapy.Field()
    age = scrapy.Field()
    team = scrapy.Field()
    country = scrapy.Field()

class Match(scrapy.Item):
    team1 = scrapy.Field()
    score1 = scrapy.Field()
    team2 = scrapy.Field()
    score2 = scrapy.Field()
    date = scrapy.Field()
    time = scrapy.Field()
    event = scrapy.Field()
	