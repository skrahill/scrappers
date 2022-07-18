import scrapy
url='https://www.nykaa.com/brands/{brandname}/c/{catid}?page_no={pgno}'
catid=2674
#catid should be change depending on which category you want to scrape
brandname='nykaa-wanderlust-collection'
#brandname should also be change if brand is changed

class NykaaSpider(scrapy.Spider):
    name = 'nykaa'
    allowed_domains = ['nykaa.com']
    
    def start_requests(self):
        pg=1
        #pg value should be changed depending upon the no of products. divide no of products by 22 for pg value
        while(pg<=45):

            localurl=url.format(pgno=pg,catid=catid,brandname=brandname)
            pg=pg+1
        
            yield scrapy.Request(url=localurl,callback=self.parse)

    def parse(self, response):
        products = response.xpath("//div[@class='productWrapper css-xin9gt']")
        for product in products:
            urls=product.xpath("//div[@class='css-d5z3ro']/a/@href").extract()
       
        for i in urls:

            producturl=f"https://www.nykaa.com{i}"
       

            yield scrapy.Request(producturl,callback=self.parse_product_page,meta={'producturl':producturl})

    def parse_product_page(self,response):
        producturl=response.meta['producturl']
        title=response.xpath("//div[@class='css-1d5wdox']/h1/text()").get()
        mrp=response.xpath("//div/span[@class='css-u05rr']/span/text()").get()
        price=response.xpath("//div/span[@class='css-1jczs19']/text()").get()

        #similary other information according to your need you can scrape using xpath selector



        yield({'producturl':producturl,'title':title,'mrp':mrp,'price':price})

        #if you want save scrape item in database then you have to create pipelines and items for that you can refer jiomart scrapper
            

        
           
           
            
            