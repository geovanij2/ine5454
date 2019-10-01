# -- coding: utf-8 --
import scrapy
from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

import csv
import time


class FirstSpider(CrawlSpider):
    name = 'first'

    #allowed_domains = ['https://liquipedia.net/']

    #urls para startar o crawler
    start_urls = ['https://www.hltv.org/team/9215/mibr']
    rules = (Rule(LinkExtractor(), callback = 'parse_page', follow=True),)

    def parse_page(self, response):

        #groupsolt = response.xpath('//[@class="grouptableslot"]').extract()
        teamNames = response.xpath('//div[contains(@class, "team-name")]/text()').extract()
        teamNames = set(map(lambda x: x.strip(), teamNames)) - {''}

        with open('teams.csv', 'w') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow(['Team Name'])
            for teamName in teamNames:
                spamwriter.writerow([teamName])

        print('Ctrl + C')
        time.sleep(5000)

        yield {'teamName':teamNames}