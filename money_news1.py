import scrapy
import pandas as pd
csv_input = pd.read_csv('lol.csv')
content=csv_input['moneycontrol_link'][:3]
links=[company for company in content]
l=[]
class BrickSetSpider(scrapy.Spider):
    name = "h2"
    start_urls = ['http://www.moneycontrol.com/india/stockpricequote/computers-software/tataconsultancyservices/TCS']
    def parse(self, response):
        SET_SELECTOR = 'dt'#.pcContainer #floating-box'
        csv_input = pd.read_csv('ittt.csv')
        i=0
        for brickset in response.css(SET_SELECTOR):
            i=i+1
            if i==3:
                NAME_SELECTOR = 'a ::attr(href)'
                name=brickset.css(NAME_SELECTOR).extract_first()
                print('fghjk'+name)
