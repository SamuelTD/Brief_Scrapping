# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TutoScrappingItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    pass

# def serialize_price(value):
#     return f'£ {str(value)}'

class SubCategoryItem(scrapy.Item):
    name = scrapy.Field()
    product_list_url = scrapy.Field()
    availlable_products = scrapy.Field()
    
class CategoryItem(scrapy.Item):
    name = scrapy.Field()
    sub_cat_url = scrapy.Field()
    sub_categories = scrapy.Field()

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
