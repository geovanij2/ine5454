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
    start_urls = ['https://www.gosugamers.net/']#,'https://watch.lolesports.com/', 'https://liquipedia.net/','https://www.espn.com/esports/']
    rules = (Rule(LinkExtractor(), callback = 'parse_page', follow=True),)

    def parse_page(self, response):

        #teamRegex = r'"[>]*team[^"]*?">([^<]*)'
        #teamRegex2 = r'"[>]*team[\d\D]*?name[^>]*?>([^<]*)'
        

        #groupsolt = response.xpath('//[@class="grouptableslot"]').extract()
        teamNames = response.xpath('//div[contains(@class, "team-name")]/text()').extract()
        body = response.body
        body = body.decode('utf-8')
        data = re.findall(r'"[>]*team[^"]*?">([^<]*)', body)
        data2 = re.findall(r'"[>]*team[\d\D]*?name[^>]*?>([^<]*)', body)

        with open('teams.csv', 'w') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow(['Team Name'])
            for teamName in teamNames:
                spamwriter.writerow([teamName])

        with open('data1.csv', 'w') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow(['Team Name'])
            for teamName in data2:
                spamwriter.writerow([teamName])

        with open('data2.csv', 'w') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow(['Team Name'])
            for teamName in data2:
                spamwriter.writerow([teamName])

                

        print(data)
        print(data2)
        #print(body)

        print('Ctrl + C')
        time.sleep(5)

        yield {'teamName':teamNames}
