import scrapy
import pandas as pd
csv_input = pd.read_csv('ittt.csv')
content=csv_input['Name']
links=['https://www.google.com/search?q='+company for company in content]
l=[]
class BrickSetSpider(scrapy.Spider):
# you may also want to remove whitespace characters like `\n` at the end of each line
    name = "brickset_spider"
    for company in content:
        start_urls = links
        def parse(self, response):
            i=0
            SET_SELECTOR = '.r'
            for brickset in response.css(SET_SELECTOR):
                i=i+1
                if i==1:
                    NAME_SELECTOR = 'a ::attr(href)'
                    ppp=brickset.css(NAME_SELECTOR).extract_first()[7:]
                    l.append(ppp)
#                    link.append(brickset.css(NAME_SELECTOR).extract_first()[7:])
                    print(ppp)
            csv_input['MoneyControl_link']=l
            csv_input.to_csv('ittt.csv', index=False)
#        for brickset in response.css(SET_SELECTOR):
#            print(i)
#            i=i+1
#            if i==1:
#            yield {
#            'name':brickset.css('a ::text').extract_first()
#            }
