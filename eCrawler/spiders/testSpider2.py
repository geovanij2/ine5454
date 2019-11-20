# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
# http://www.hltv.org/matches/2337808/havu-vs-cr4zy-esea-mdl-season-32-europe//

def contains_vs_icon(div):
    for string in div.strings:
        if string in {'vs'}:
            return True
    return False

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
            soup = BeautifulSoup(div, "html.parser")
            children = soup.div.contents
            print('-------------------------------------------------\n')
            while '\n' in children:
                children.remove('\n')
            if len(children) == 3 and contains_vs_icon(children[1]):
                file1.write('+++++++++')
                for string in children[0].strings:
                    file1.write(string)
                file1.write('+++++++++')
                # for string in children[1].strings:
                #     file1.write(string)
                # file1.write('+++++++++')
                for string in children[2].strings:
                    file1.write(string)
                file1.write('+++++++++')
            print('-------------------------------------------------\n')
            # if div is not None:
            #     file1.write( \
            #         '\n-------------------------------------------------- \n' +\
            #         '    DIV # ' + str(i) + \
            #         '\n-------------------------------------------------- \n' \
            #         + div)
            i += 1
        file1.close()