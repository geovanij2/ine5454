# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class TestspiderSpider(CrawlSpider):
    name = 'testSpider'
    start_urls = ['http://www.hltv.org/matches/2337808/havu-vs-cr4zy-esea-mdl-season-32-europe/']

    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        div_3_divs = []
        divs = response.xpath('//div')

        for div in divs:
            if (len(div.xpath('/div').extract()) == 3):
                print('-----------------------------------------------------------')
        
        print('-----------------------------------------------------------')