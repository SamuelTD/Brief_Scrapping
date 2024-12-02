import scrapy
from Brico_Scrapping.items import CategoryItem
from .. import general_func as g

class BricospiderSpider(scrapy.Spider):
    name = "bricospider_categories"
    allowed_domains = ["www.bricodepot.fr"]
    start_urls = ["https://www.bricodepot.fr/"]
    current_url = ""
    list_subsub_category = []
    
    def parse(self, response):
     
        categories = response.css('ul.bd-MenuLink-subList > li')
        
        for category in categories:
            
            if "--title" in category.css("::attr(class)").get():
                continue
            else:                     
                self.current_url = self.start_urls[0].rstrip("/")+(category.css("span").attrib["data-href"])
                meta = {
                    'name': category.css('a::attr(data-label)').get(),
                    'url' : self.current_url
                }              
                yield response.follow(self.current_url, callback = self.parse_sub_category, headers={"User-Agent": g.get_random_user_agent()}, meta=meta)
                
        
   
 
        
    def parse_sub_category(self, response):
        
        subcategories = response.css("a.bd-CategoryItem-link")
        for subcategory in subcategories: 
                meta = {
                    'name': subcategory.css("a.bd-CategoryItem-link").attrib["title"],
                    'url' : self.start_urls[0].rstrip("/")+subcategory.css("a.bd-CategoryItem-link").attrib["href"]
                }          
                yield response.follow(self.start_urls[0].rstrip("/")+subcategory.css("a.bd-CategoryItem-link").attrib["href"], callback=self.parse_sub_category, headers={"User-Agent": g.get_random_user_agent()}, meta=meta)
        category_item = CategoryItem()            
        category_item["name"] = response.meta["name"]
        category_item["url"] = response.meta["url"]
        category_item["is_page_list"] = subcategories == [] and response.css("div.bd-Page-text") != []
        yield category_item
            
       
        
        