import scrapy


class BrickSetSpider(scrapy.Spider):
    name = 'brick_spider'
    start_urls = ['https://www.google.co.in/search?q=ACC+moneycontrol']

    def parse(self, response):
        SET_SELECTOR = '.rc'
        for brickset in response.css(SET_SELECTOR):

            NAME_SELECTOR = 'h3 a ::text'
            yield {
                'name': brickset.css(NAME_SELECTOR).extract_first(),
            }
