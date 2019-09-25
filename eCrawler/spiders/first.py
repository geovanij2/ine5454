# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class FirstSpider(CrawlSpider):
    name = 'first'
    
    #allowed_domains = ['https://liquipedia.net']

    #urls para startar o crawler
    start_urls = ('https://liquipedia.net/counterstrike/ESL/One/2019/New_York',)
    rules = (Rule(LinkExtractor(), callback = 'parse_page', follow=True),)

    def parse_page(self, response):

        groupsolt = response.xpath('//*[@class="grouptableslot"]').extract()
        teamName = response.xpath('//*[@class="team-template-text"]').extract()
        teamLogo = response.xpath('//*[@class="team-template-image"]').extract()

        yield {'teamName':teamName, 'teamlogo': teamLogo}

            

    
