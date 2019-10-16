import scrapy
from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

import csv
import time
import re


class FirstSpider(CrawlSpider):
    name = 'first'

    #allowed_domains = ['https://liquipedia.net/']

    #urls para startar o crawler
    start_urls = ['https://www.gosugamers.net/','https://watch.lolesports.com/', 'https://hltv.org/','https://www.espn.com/esports/']
    rules = (Rule(LinkExtractor(), callback = 'parse_page', follow=True),)

    with open('Results.csv', 'w') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(['URL', 'Tipo de Dado', 'Dado'])

    def parse_page(self, response):

        body = response.body
        body = body.decode('utf-8')

        teamNames = self.search_teams(body)

        with open('Results.csv', 'a') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)

            # Write URL
            spamwriter.writerow([response.request.url])

            # Write Teams
            for teamName in teamNames:
                spamwriter.writerow(['','Team Name', teamName])

        yield {'teamName':teamNames}

    def search_teams(self, body):
        # Team Regex
        # teamNames = re.findall(r'"[>]*team[^"]*?">([^<]*)', body)
        teamNames = re.findall(r'"[>]*team[\d\D]*?name[^>]*?>([^<]*)', body)

        return self.clean_list(teamNames)

    def clean_list(self, data):
        return list(set(data) - {'|','Unknown'})
