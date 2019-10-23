# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import Match


class MatchspiderSpider(CrawlSpider):
    name = 'matchSpider'
    allowed_domains = ['hltv.org']
    start_urls = ['https://www.hltv.org/results?startDate=all/']

    rules = (
        Rule(LinkExtractor(restrict_css=('.result-con a', '.pagination-component')), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        match = response.css('.match-page')
        if match:
            yield self.parse_match(match)

    def parse_match(self, response):
        match = Match()

        teamBox = response.css('.standard-box')

        teams = teamBox.css('.team')

        match['team1'] = teams[0].css('.teamName::text').extract_first()
        score = teams[0].css('.won::text').extract_first()
        if score is None:
            score = teams[0].css('.lost::text').extract_first()
        match['score1'] = score

        match['team2'] = teams[1].css('.teamName::text').extract_first()
        score = teams[1].css('.won::text').extract_first()
        if score is None:
            score = teams[1].css('.lost::text').extract_first()
        match['score2'] = score

        timeAndEvent = teamBox.css('.timeAndEvent')

        match['time'] = timeAndEvent.css('.time::text').extract_first()
        match['date'] = timeAndEvent.css('.date::text').extract_first()
        match['event'] = timeAndEvent.css('.event a::text').extract_first()

        return match
