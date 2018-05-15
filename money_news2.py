import scrapy
import pandas as pd
csv_input = pd.read_csv('loll.csv')
content=csv_input['moneycontrol_link'][0:200]
links=[company for company in content]
l=[]
print(len(csv_input['moneycontrol_link'][0:200]))
class BrickSetSpider(scrapy.Spider):
    name='sd'
    start_urls = links
    for company in content:
        def parse(self, response):
            SET_SELECTOR = 'dt'#.pcContainer #floating-box'
            i=0
            j=0
            for brickset in response.css(SET_SELECTOR):
                i=i+1
                if i==3:
                    j=j+1
                    print(j)
                    NAME_SELECTOR = 'a ::attr(href)'
                    name=brickset.css(NAME_SELECTOR).extract_first()
                    l.append('http://www.moneycontrol.com'+name)
            if len(l)==200:
                print(l)
                csv_input['news'][0:200]=l
                csv_input.to_csv('loll.csv', index=False)
