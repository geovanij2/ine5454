# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import Match
from bs4 import BeautifulSoup
import time

def divs_with_3_children(tag):
    return len(tag.contents) == 3

class MatchspiderSpider(CrawlSpider):
    name = 'matchSpider'
    allowed_domains = ['hltv.org']
    start_urls = ['https://www.hltv.org/results?startDate=all/']

    rules = (
        Rule(LinkExtractor(restrict_css=('.result-con a', '.pagination-component')), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        soup = BeautifulSoup(response.css("body").extract_first())
        possible_matches = soup.find_all(divs_with_3_children)
        for possible_match in possible_matches:
            yield self.parse_match(possible_match)

    def parse_match(self, tag):
        match = Match()
        print(tag)
        time.sleep(10)

        for string in tag.contents[0].strings:
            if re.fullmatch(r'\d', string):
                match['team1'] = string

        return match
