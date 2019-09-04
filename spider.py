import scrapy


class MovieSpider(scrapy.Spider):
    name = 'Movies'
    movie=[]
    allowed_domains = ["www.rottentomatoes.com"]
    start_urls = ['https://www.rottentomatoes.com']

    def parse(self, response):
        for movie in response.css('[id="Top-Box-Office"] [class="sidebarInTheaterOpening"]'):
            item = {
                'Top-Ten': movie.css('[class="middle_col"] a ::text').extract(),
                'Score': movie.css('[class="left_col"] span ::text').extract()
            }
            yield item
