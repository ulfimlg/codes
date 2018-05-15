import scrapy
import pandas as pd

class BrickSetSpider(scrapy.Spider):
    name = "brickset_spider"
    start_urls = ['http://www.moneycontrol.com/india/stockpricequote/banks-public-sector/andhrabank/AB14']
    def parse(self, response):
        SET_SELECTOR = 'dt'#.pcContainer #floating-box'
        csv_input = pd.read_csv('ittt.csv')
        i=0
        for brickset in response.css(SET_SELECTOR):
            i=i+1
            if i==3:
                NAME_SELECTOR = 'a ::attr(href)'
                name=brickset.css(NAME_SELECTOR).extract_first(),
                p=name

        pl=[p for x in range (501)]       
        csv_input['MoneyControl_link']=pl
        csv_input.to_csv('ittt.csv', index=False)
