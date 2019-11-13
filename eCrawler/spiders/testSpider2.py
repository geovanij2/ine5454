# -*- coding: utf-8 -*-
import scrapy


class Testspider2Spider(scrapy.Spider):
    name = 'testSpider2'
    start_urls = ['http://www.hltv.org/matches/2337808/havu-vs-cr4zy-esea-mdl-season-32-europe//']

    def parse(self, response):
        div_3_divs = []

        divs = response.xpath('//div')

        for div in divs:
            if (len(div.xpath('./div').extract()) == 3):
            	div_3_divs.append(div.xpath('*').extract_first())

        print(div_3_divs)
        print(len(div_3_divs))

        file1 = open('test.txt','w+', encoding='utf-8')
        for div in div_3_divs:
        	if div is not None:
        		file1.write('\n\n\n\n\n\n\n\n\n\n\n' + div)
        file1.close()