import scrapy


class BrickSetSpider(scrapy.Spider):
    name = "brickset_spider"
    start_urls = ['https://www.google.co.in/search?rlz=1C1CHBD_enIN778IN778&ei=EqWtWq7xIo28vwSci4uIDA&q=andhra+bank+moneycontrol&oq=Abbott+India+Ltd+money&gs_l=psy-ab.3.0.0i22i30k1.1269.3349.0.4759.6.4.0.2.2.0.99.363.4.4.0....0...1c.1.64.psy-ab..0.6.392...0.0.FYomETIfA2o']

    def parse(self, response):
        SET_SELECTOR = '.r'
        i=0
        for brickset in response.css('.slider'):
                print(i)
                i=i+1
                yield {
                    'name1': brickset.css('dt a::attr(href)').extract_first()
                }
