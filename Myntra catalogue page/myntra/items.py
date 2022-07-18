# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MyntraItem(scrapy.Item):

    landingpageurl=scrapy.Field()
    p_id=scrapy.Field()
    Product=scrapy.Field()
    Productname=scrapy.Field()
    ratings=scrapy.Field()
    Brand=scrapy.Field()
    Searchimage=scrapy.Field()
    colour=scrapy.Field()
    Category=scrapy.Field()
    Mrp=scrapy.Field()
    Price=scrapy.Field()

    
