import scrapy
from Brico_Scrapping.items import ProductItem
from .. import general_func as g
from math import ceil

class BricospiderSpider(scrapy.Spider):
    name = "bricospider_product"
    allowed_domains = ["www.bricodepot.fr"]
    start_urls = ["https://www.bricodepot.fr/"]
    
    nb_pages = 0
    recalc_nb_pages = True
    current_page = 1
    next_url = ""
    urls = []
    
    def parse(self, response):
        
        #Get all product pages from categories
        urls = g.get_categories_url()

        for url in urls:     
            self.next_url = url 
            yield response.follow(url, callback=self.parse_category)
            self.recalc_nb_pages = True         
    
    def parse_category(self, response):
        
        #Calculate the number of availlable pages for this category based on the number of availlable products.
        #Each page can show at maximum 50 products.
        if self.recalc_nb_pages:
            self.recalc_nb_pages = False   
            #If there is more than 50 products, there are multiple pages and we calculate the amount         
            if int(response.css("div.bd-Page-text.jsbd-Pagination-TotalCount span::text").get()) > 50:                
                self.current_page = 1
                self.nb_pages = int(ceil(int(response.css("div.bd-Page-text.jsbd-Pagination-TotalCount span::text").get())/50))
            #Else we'll only look at the first one.
            else:
                self.current_page = 2
                self.nb_pages = 1
        
        #Get all products on the product page
        product_pages = response.css(".bd-ProductsListItem-top--link")
        for product_page in product_pages:
            meta={
                'price' : response.css('div.r-Grid-cell').css('div div div a div div div div::attr(data-price)').get()
            }
            
            #If there is no price, the product is not availlable so it is skipped
            if meta["price"] is None :
                continue
            yield response.follow(product_page.css("a").attrib["href"], callback = self.parse_product, meta=meta )      

        #If there are more pages, continue to the next.    
        if self.current_page <= (self.nb_pages):
            
            n_url = self.next_url+f"{self.current_page+1}/"
            self.current_page += 1             
            yield response.follow(n_url, callback = self.parse_category) 
        
    def parse_product(self, response):
        
        product = ProductItem()
        product["name"] = response.css("h1.bd-ProductCard-title span::text").get()
        product["url"] = response.url 
        product["price"] = response.meta["price"]
        product["product_ref"] = response.css("span.bd-ProductDetails-tableDesc::text").getall()[0]
        product["product_code"] = response.css("span.bd-ProductDetails-tableDesc::text").getall()[1]
        product["brand"] = response.css('span.bd-ProductCard-brand-txt::text').get()                             
        
        yield product
        
       
        
        