import scrapy
from myntra.items import MyntraItem
import scrapy
import json
class MyntraSpider(scrapy.Spider):
    name = 'Myntra'
    allowed_domains = ['Myntra.com']
    start_urls=['https://www.myntra.com/shoes']
    
    def parse(self, response):
        item=MyntraItem()
        prod =response.xpath("//script/text()")[9].getall()
        x=''.join(map(str,prod))
        x=x.replace('window.__myx = ','') 
        x=json.loads(x)
        for i in range(1,50):
            item['landingpageurl']=x['searchData']['results']['products'][i]['landingPageUrl']
            item['p_id']=x['searchData']['results']['products'][i]['productId']
            item['Product']=x['searchData']['results']['products'][i]['product']
            item['Productname']=x['searchData']['results']['products'][i]['productName']
            item['ratings']=x['searchData']['results']['products'][i]['rating']
            item['Brand']=x['searchData']['results']['products'][i]['brand']
            item['Searchimage']=x['searchData']['results']['products'][i]['searchImage']
            item['colour']=x['searchData']['results']['products'][i]['primaryColour']
            item['Category']=x['searchData']['results']['products'][i]['category']
            item['Mrp']=x['searchData']['results']['products'][i]['mrp']
            item['Price']=x['searchData']['results']['products'][i]['price']

            yield(item)

    
            




        