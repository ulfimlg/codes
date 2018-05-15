import scrapy


class BrickSetSpider(scrapy.Spider):
    name = "brickset_spider"
    with open('beneficiary.txt') as f:
        content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]
    for company in content:
        print(company)
        start_urls = ['https://www.moneycontrol.com/']
        def parse(self, response):
            i=0
            SET_SELECTOR = '.r'
            for brickset in response.css(SET_SELECTOR):
                i=i+1
                if i==1:
                    NAME_SELECTOR = 'a ::attr(href)'
                    print(i)
                    yield {
                        'name': brickset.css(NAME_SELECTOR).extract_first()[7:]
                        }
#        i=0
#        for brickset in response.css(SET_SELECTOR):
#            print(i)
#            i=i+1
#            if i==1:
#            yield {
#            'name':brickset.css('a ::text').extract_first()
#            }
