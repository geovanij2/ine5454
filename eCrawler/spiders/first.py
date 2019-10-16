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
    start_urls = ['https://www.gosugamers.net/','https://watch.lolesports.com/', 'https://liquipedia.net/','https://www.espn.com/esports/']
    rules = (Rule(LinkExtractor(), callback = 'parse_page', follow=True),)

    def parse_page(self, response):

        #teamRegex = r'"[>]*team[^"]*?">([^<]*)'
        #teamRegex2 = r'"[>]*team[\d\D]*?name[^>]*?>([^<]*)'
        

        #groupsolt = response.xpath('//[@class="grouptableslot"]').extract()
        body = response.body
        body = body.decode('utf-8')
        data = re.findall(r'"[>]*team[^"]*?">([^<]*)', body)
        data2 = re.findall(r'"[>]*team[\d\D]*?name[^>]*?>([^<]*)', body)
        results = re.findall(r'"[>]*score[\d\D]*?[^>]*?>[\d\D]*?(loss?t?)[\d\D]*?<\/', body)
        prize = re.findall(r'prize[^$]*(\$[\d\,\.]*)', body)
        participants = re.findall(r'"[>]*name[^>]*?">([^<]*)[\d\D]*(vs)[\d\D]*"[>]*name[^>]*?">([^<]*)', body)
        game = re.findall(r'(counterstrike)?(l?L?eague O?o?f l?L?egends)?(h?H?earthstone)?(C?c?ounter S?s?trike)?', body)
        date = re.findall(r'match[\d\D]*datetime="([^"]*)', body)
        
        

        with open('teams1.csv', 'a') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for teamName in data2:
                spamwriter.writerow([teamName])

        with open('teams2.csv', 'a') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for teamName in data2:
                spamwriter.writerow([teamName])

        with open('prize.csv', 'a') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for teamName in prize:
                spamwriter.writerow([teamName])
                
        with open('participants.csv', 'a') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for teamName in participants:
                spamwriter.writerow([teamName])
                
        with open('results.csv', 'a') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for teamName in results:
                spamwriter.writerow([teamName])
                
        with open('game.csv', 'a') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for teamName in game:
                spamwriter.writerow([teamName])
                
        with open('date.csv', 'a') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for teamName in date:
                spamwriter.writerow([teamName])




        print('Ctrl + C')
        time.sleep(5)

        yield {'teamName':teamNames}
