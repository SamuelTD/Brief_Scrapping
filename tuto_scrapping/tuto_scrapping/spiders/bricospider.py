import scrapy
from tuto_scrapping.items import SubCategoryItem, CategoryItem
from .. import general_func as g

class BricospiderSpider(scrapy.Spider):
    name = "bricospider"
    allowed_domains = ["www.bricodepot.fr"]
    start_urls = ["https://www.bricodepot.fr/"]
    current_url = ""
    
    def parse(self, response):
        
        categories = response.css('li.bd-MenuLink-item')
        
        for category in categories:
            
            if "--title" in category.css("::attr(class)").get():
                continue
            else:                                
                self.current_url = self.start_urls[0].rstrip("/")+(category.css("span").attrib["data-href"])
                yield response.follow(self.current_url, callback = self.parse_sub_category, headers={"User-Agent": g.get_random_user_agent()})
                
                # yield{
                # 'Category': category.css('a').attrib["data-label"],
                # 'Url': url
                # }  
 
    # def parse_category(self, response):
        
    #     categories = response.css("a.bd-CategoryItem-link")
    #     for category in categories:
            
        
    def parse_sub_category(self, response):
        
        subcategories = response.css("a.bd-CategoryItem-link")
        category_item = CategoryItem()
        category_item["name"] = response.css("h1.bd-CategoryBanner-title--univers.bd-Strong::text").get()
        category_item["sub_cat_url"] = self.current_url
        category_item["sub_categories"] = []
        for subcategory in subcategories:
            sub_category_item = SubCategoryItem()
            
            sub_category_item["name"] = subcategory.css("a.bd-CategoryItem-link").attrib["title"]
            sub_category_item["product_list_url"] = self.start_urls[0].rstrip("/")+subcategory.css("a.bd-CategoryItem-link").attrib["href"]
            sub_category_item["availlable_products"] = subcategory.css("p.bd-CategoryItem-stock::text").get()
            
            category_item["sub_categories"].append(sub_category_item)
        
        yield category_item
        



           # yield{
            #     'Article': product.css('div.pc-produit-text-ambi2 p strong::text').get(),
            #     'Prix': product.css('div.pc-prix::text').get()
            # }