# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

# def serialize_price(value):
#     return f'£ {str(value)}'

class CategoryItem(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()
    is_page_list = scrapy.Field()
    

class ProductItem(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()
    isAvaillable = scrapy.Field()
    price = scrapy.Field()
    product_ref = scrapy.Field()
    product_code = scrapy.Field()
    brand = scrapy.Field()
    # rating = scrapy.Field()
    # nb_reviews = scrapy.Field()

class BookItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    upc = scrapy.Field()
    product_type = scrapy.Field()
    price_excl_tax = scrapy.Field()
    price_incl_tax = scrapy.Field()
    tax = scrapy.Field()
    availability = scrapy.Field()
    num_reviews = scrapy.Field()
    stars = scrapy.Field()
    category = scrapy.Field()
    description = scrapy.Field()
    price = scrapy.Field()
