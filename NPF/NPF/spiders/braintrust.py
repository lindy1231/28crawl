import scrapy


class BraintrustSpider(scrapy.Spider):
    name = 'braintrust'
    allowed_domains = ['braintrust.tw']
    start_urls = ['http://braintrust.tw/']

    def parse(self, response):
        pass
