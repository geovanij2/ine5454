# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import Team


class TeamspiderSpider(CrawlSpider):
    name = 'teamSpider'
    allowed_domains = ['hltv.org']
    start_urls = ['http://hltv.org/results/']

    rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        team = Team()

        teamResponses = response.css('.team')

        for teamResponse in teamResponses:
            for name in set(self.parse_team(teamResponse)):
                team['name'] = name
                yield team

    def parse_team(self, response):
        return response.css('.teamName::text').extract()
