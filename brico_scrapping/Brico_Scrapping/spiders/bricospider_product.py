import scrapy
from Brico_Scrapping.items import ProductItem
from .. import general_func as g
import io
from math import ceil

class BricospiderSpider(scrapy.Spider):
    name = "bricospider_product"
    allowed_domains = ["www.bricodepot.fr"]
    # item = g.get_item()
    start_urls = ["https://www.bricodepot.fr/"]
    
    nb_pages = 0
    first_iteration = False
    recalc_nb_pages = True
    current_page = 1
    next_url = ""
    urls = []
    
    def parse(self, response):
        
        # self.urls = g.get_categories_url()   
        
        # self.urls.append("https://www.bricodepot.fr/catalogue/amenagement-despaces/cuisine/eclairage-de-cuisine/spot-led/")       
        # self.urls.append("https://www.bricodepot.fr/catalogue/outillage-quincaillerie/quincaillerie/signalisation-de-chantier/")
        # self.urls.append("https://www.bricodepot.fr/catalogue/outillage-quincaillerie/quincaillerie/pile-chargeur/")  
        
        # for url in self.urls:       
        self.next_url = "https://www.bricodepot.fr/catalogue/construction-renovation/materiau-gros-oeuvre/facade-et-bardage/bardage/"
        yield scrapy.Request(self.next_url, callback=self.parse_category, headers={"User-Agent": g.get_random_user_agent()})
      
            # yield response.follow(url, callback=self.parse_category, headers={"User-Agent": g.get_random_user_agent()})
            # self.recalc_nb_pages = True
            
    
    def parse_category(self, response):
        if self.recalc_nb_pages:
            self.recalc_nb_pages = False            
            if int(response.css("div.bd-Page-text.jsbd-Pagination-TotalCount span::text").get()) > 50:                
                self.current_page = 1
                self.nb_pages = int(ceil(int(response.css("div.bd-Page-text.jsbd-Pagination-TotalCount span::text").get())/50))
                # try:
                #     self.next_url = "https://www.bricodepot.fr/"+ response.css("div.bd-Box-paging div div a").attrib["href"].split("50")[0]
                # except:
                #     print("DEBUG =================== ", response.css("div.bd-Box-paging div div a"))
            else:
                self.current_page = 2
                self.nb_pages = 1
        
        # divs_pages = response.css('div.bd-Box-paging div div div')
        # netx_page = divs_pages[-1].css('a')
        
        # product_list = response.css('.bd-Products')
        # product_pages = response.xpath('/html/body/div[1]/div[2]/div/div/div[3]/div[3]/div[2]/div[4]/div/div[1]/div[3]/div/div')
        # with open("response.txt", "wb") as file :
        #     file.write(response.body)
        # print (response.body)
        product_pages = response.css(".bd-ProductsListItem-top--link")
        # product_pages= response.xpath("/html/body/div[1]/div[2]/div/div/div[3]/div[3]/div[2]/div[4]/div/div[1]/div[2]/div/div/div[3]/div")
        print("DEBUG================= ", product_pages)
        for product_page in product_pages:
        # for product_page in range(4):
            print("DEBUG================= ")
            print(response.css('div.r-Grid-cell').css('div div div a div div div div::attr(data-price)').get())
            # meta={
            #     'price' : response.css('div.r-Grid-cell').css('div div div a div div div div::attr(data-price)').get()
            # }
            
            #If there is no price, the product is not availlable so it is skipped
            # if meta["price"] is None :
            #     continue
            yield response.follow(product_page.css("a").attrib["href"], callback = self.parse_product, headers={"User-Agent": g.get_random_user_agent()}, meta=meta)    
            break     
            
        # if self.current_page <= (self.nb_pages):
        #     n_url = self.next_url+f"{self.current_page+1}/"
        #     self.current_page += 1             
        #     yield response.follow(n_url, callback = self.parse_category, headers={"User-Agent": g.get_random_user_agent()}) 
        
    def parse_product(self, response):
        
        product = ProductItem()
        product["name"] = response.css("h1.bd-ProductCard-title span::text").get()
        product["url"] = response.url
        product["isAvaillable"] = True  
        product["price"] = response.meta["price"]
        product["product_ref"] = response.css("span.bd-ProductDetails-tableDesc::text").getall()[0]
        product["product_code"] = response.css("span.bd-ProductDetails-tableDesc::text").getall()[1]
        product["brand"] = response.css('span.bd-ProductCard-brand-txt::text').get()                             
        
        yield product
        
       
        
        