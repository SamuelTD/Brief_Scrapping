# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class CategoryItem(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()
    is_page_list = scrapy.Field()
    

class ProductItem(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()
    price = scrapy.Field()
    product_ref = scrapy.Field()
    product_code = scrapy.Field()
    brand = scrapy.Field()