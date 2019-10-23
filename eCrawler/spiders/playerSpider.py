# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import Player


class PlayerspiderSpider(CrawlSpider):
    name = 'playerSpider'
    allowed_domains = ['hltv.org']
    start_urls = [
        'https://www.hltv.org/stats/teams?startDate=all'
        ]

    rules = (
        Rule(LinkExtractor(restrict_css=('.player-holder','.teamCol-teams-overview', '.image-and-label', '.go-to-profile-button')), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        # playerProfile
        playerProfiles = response.css('.playerContainer')

        for playerProfile in playerProfiles:
            yield self.parse_player(playerProfile)

    def parse_player(self, response):
        player = Player()

        playerName = response.css('.playerName')
        player['nick'] = playerName.css('.playerNickname::text').extract_first().strip()
        player['name'] = playerName.css('.playerRealname::text').extract_first().strip()
        player['country'] = playerName.css('.playerRealname .flag').xpath('@title').extract_first().strip()

        playerInfo = response.css('.playerInfo')
        player['age'] = playerInfo.css('.playerAge .listRight::text').extract_first().strip()
        player['team'] = playerInfo.css('.playerTeam .listRight a::text').extract_first()
        if player['team'] is not None:
            player['team'] = player['team'].strip()

        return player

    def parse_team(self, response):
        return response.css('.teamName::text').extract()