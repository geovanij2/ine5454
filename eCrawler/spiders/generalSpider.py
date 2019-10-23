# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import Match, Player, Team


class GeneralspiderSpider(CrawlSpider):
    name = 'generalSpider'
    allowed_domains = ['hltv.org']
    start_urls = [
        'https://www.hltv.org/',
        'https://www.hltv.org/results?startDate=all/',
        'https://www.hltv.org/stats/teams?startDate=all',
        'http://hltv.org/results/'
        ]

    rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        matches = response.css('.match-page')
        for match in matches:
            found = self.parse_match(match)
            if found:
                yield found

        # playerProfile
        playerProfiles = response.css('.playerContainer')

        for playerProfile in playerProfiles:
            found = self.parse_player(playerProfile)
            if found:
                yield found

        teamResponses = response.css('.team')

        for teamResponse in teamResponses:
            found = self.parse_team(teamResponse)
            if found:
                yield found



    def parse_match(self, response):
        match = Match()

        teamBox = response.css('.standard-box')
        if not teamBox:
            return False

        teams = teamBox.css('.team')
        if not teams:
            return False

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
        team = Team()
        team['name'] = response.css('.teamName::text').extract()
        if team['name']:
            return team
        return False
