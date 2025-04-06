from pathlib import Path

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        '''
        '''
        for i in range(1, 10):
            url = f"https://quotes.toscrape.com/page/{i}/"
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        print(response.url)
        page = response.url.split("/")[-2]
        # filename = f"quotes-{page}.html"
        filename = f"Output/quotes-{page}.html"
        Path(filename).write_bytes(response.body)