import scrapy
import pandas as pd
csv_input = pd.read_csv('loll.csv')
content=csv_input['news'][0:2]
links=[company for company in content]
l=[]
class BrickSetSpider(scrapy.Spider):
    csv_input = pd.read_csv('loll.csv')
    content=csv_input['news'][0:2]
    links=[company for company in content]
    name = ".FL .FL"
    start_urls = ["http://www.moneycontrol.com/company-article/srf/news/SRF#SRF"]#'http://www.moneycontrol.com/company-article/punjabnationalbank/news/PNB05']
    def parse(self, response):
        SET_SELECTOR = '.MT15.PT10.PB10'#.pcContainer #floating-box'
        i,j=0,0
        for brickset in response.css(SET_SELECTOR):
            i=i+1
            j=j+1
            if i==1:
                NAME_SELECTOR = 'a ::attr(href)'
                name=brickset.css(NAME_SELECTOR).extract_first()
                print(name)
                #print(i)
                l.append(name)
                if j==2:
                    print(len(l))
                    print(l)
#        csv_input['cnews']=l
#        csv_input.to_csv('ittt.csv', index=False)
#    print(csv_input['cnews'])
    print(len(csv_input['cnews']))
    print(len(l))
