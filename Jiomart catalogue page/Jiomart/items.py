# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JiomartItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    productcode=scrapy.Field()
    displayname=scrapy.Field()
    mrp=scrapy.Field()
    availablility_status=scrapy.Field()
    urlpath=scrapy.Field()
    imageurl=scrapy.Field()
