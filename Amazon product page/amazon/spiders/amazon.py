from scraper_api import ScraperAPIClient
client = ScraperAPIClient('de226d8a5a6cf7719bd4e6ca42277347')


import scrapy
class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['amazon.in','scraperapi.com']
    
    def start_requests(self):
        url='https://www.amazon.in/s?k=earphones'
        url=client.scrapyGet(url)
        print(url)
        yield scrapy.Request(url=url,callback=self.parse)
    def parse(self, response):
        products = response.xpath('//*[@data-asin]')
        for product in products:
        
            asin = product.xpath('@data-asin').extract_first()
            product_url = f"https://www.amazon.in/dp/{asin}"
            
            
            product_url=client.scrapyGet(product_url)
            yield scrapy.Request(url=product_url,callback=self.parse_product_page,meta={'asin': asin})
        
    def parse_product_page(self, response):
        
        asin = response.meta['asin']
        title = response.xpath('//*[@id="productTitle"]/text()').extract_first()
        #image = re.search('"large":"(.*?)"',response.text).groups()[0]
        rating = response.xpath('//*[@id="acrPopover"]/@title').extract_first()
        number_of_reviews = response.xpath('//*[@id="acrCustomerReviewText"]/text()').extract_first()
        bullet_points = response.xpath('//*[@id="feature-bullets"]//li/span/text()').extract()
        seller_rank = response.xpath('//*[text()="Amazon Best Sellers Rank:"]/parent::*//text()[not(parent::style)]').extract()

        yield({'asin':asin,'title':title,'rating':rating,'number_of_reviews':number_of_reviews,'bullet_points':bullet_points,'seller_rank':seller_rank})

        
    