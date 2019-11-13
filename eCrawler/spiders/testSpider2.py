# -*- coding: utf-8 -*-
import scrapy
# http://www.hltv.org/matches/2337808/havu-vs-cr4zy-esea-mdl-season-32-europe//

class Testspider2Spider(scrapy.Spider):
    name = 'testSpider2'
    start_urls = ['http://www.hltv.org/matches/2337808/havu-vs-cr4zy-esea-mdl-season-32-europe//']

    def parse(self, response):
        div_3_divs = []

        divs = response.xpath('//div[count(div) = 3]').extract()

        print(len(divs))

        file1 = open('test.txt','w+', encoding='utf-8')

        i = 0
        for div in divs:
            if div is not None:
                file1.write( \
                    '\n-------------------------------------------------- \n' +\
                    '    DIV # ' + str(i) + \
                    '\n-------------------------------------------------- \n' \
                    + div)
            i += 1
        file1.close()