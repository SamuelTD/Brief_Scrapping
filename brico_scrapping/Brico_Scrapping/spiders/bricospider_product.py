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
        yield scrapy.Request(self.next_url, callback=self.parse_category, headers={"User-Agent": g.get_random_user_agent()}, 
                              cookies={'Cookie': "frz-referrer=https://www.bricodepot.fr/catalogue/amenagement-despaces/cuisine/meuble-de-cuisine/; frz-referrer=; f5avraaaaaaaaaaaaaaaa_session_=LCNLPDBFMDJCFIADBPNJMLLLKIALCKFJGHNBKCALPFNMKGIMPMKNOLPGDNBHMBMFBAGDLLDHBMEENEKMAACAJJHEAHLCFDJHBENLGNGGDECNKKMJBIOPDNGHLIPHJLMA; JSESSIONID=C441CF19BD40230C03F1F5204B256D0E.node21; BVImplmain_site=11355; cart=OaZhfMsHAeubCMtbGYDDKF4icTlvusiSPmJGqcixviEa/F2h+I6tiawxiUGA6cIKPV1Bf7WuBRcTs/r/hDHPaqRAK1xo5M+/cfrXKWbMSyc=; BVBRANDID=dada9131-3925-490f-bcbf-8bec57245977; BVBRANDSID=ca3e2cca-0f0a-471d-a24c-613f589aa029; didomi_token=eyJ1c2VyX2lkIjoiMTkzODZhZDktNTZhNS02MDRlLWEzNDUtODI0YWIwZjE2MTVhIiwiY3JlYXRlZCI6IjIwMjQtMTItMDJUMDk6MjI6MjMuMjEwWiIsInVwZGF0ZWQiOiIyMDI0LTEyLTAyVDA5OjIyOjI3LjUyOVoiLCJ2ZXJzaW9uIjoyLCJwdXJwb3NlcyI6eyJlbmFibGVkIjpbImRldmljZV9jaGFyYWN0ZXJpc3RpY3MiLCJjb29raWVzZGUtejZoWXhyenoiLCJmb25jdGlvbm5lLWVyQXFwR1dSIiwiY29va2llc2EtSlFGRUVkcjgiXX0sInZlbmRvcnMiOnsiZW5hYmxlZCI6WyJnb29nbGUiLCJjOmNvbmZpcm1pdCIsImM6Y2Fhc3QtRUx0V3JBUlgiLCJjOndlYmxveWFsdHktem1IblY2NGkiLCJjOmNvbnRlbnRzcXUtUGs5OW1RdDkiLCJjOmJyaWNvZGVwby1UN1kyak0yeiIsImM6Z29vZ2xlYW5hLXFRTjJOWEdkIiwiYzpzZW5zZWZ1ZWwtV2JDclZiQ24iLCJjOmR5bmF0cmFjZS1jajN5dHhSVSIsImM6Y29uZm9ybWl0LWhCR2ZpYncyIiwiYzpwaW50ZXJlc3QtV3FyZ0hwOFoiLCJjOmZhY2Vib29rLWtrbnFhS1BDIiwiYzpsZW5nb3ctZE5NcWR4ZXgiLCJjOmdvb2dsZWFuYS00VFhuSmlnUiIsImM6Y2Fhc3QtcEM3ckNwcUUiLCJjOmFkb3QtaWViTmVDTWIiLCJjOmJhemFhcnZvaWMtM3haZVlXaEoiLCJjOmJpbmctQk0ySmJnZEoiLCJjOmdvb2dsZWFkcy13aE40cnFlTCIsImM6Z29vZ2xlLTM4VHgzQ2hBIiwiYzpucDYtTmtoajJhRUQiLCJjOmNyaXRpenItVVpCSlBNR3EiLCJjOnRlZXN0ZXItYW5RWldqRGsiLCJjOmdvb2dsZWNhbS1tejJUV0hNVSIsImM6Y2l0cnVzYWQtV1E0WUZha1EiXX19; euconsent-v2=CQJAbUAQJAbUAAHABBENBRFkAP_gAAAAAAqIGMwE4AFgAYABAACoAGAAQAAyACaAFUALYAfAA_ACCAFCALgAYYBFgC-gLzAYyAAAAUpABgACCqBCADAAEFUCUAGAAIKoDoAMAAQVQCQAYAAgqgAA.f_wAAAAAAAAA; temporal_session=d5f02215-a1a7-4650-8782-35bf81e22545; _gcl_au=1.1.462174531.1733131348; fofirdId=a63f086e-0cc1-4de0-b701-aee2241cc9b2; ez=ok; _ga_YE2HN1H7M8=GS1.1.1733131348.1.0.1733131348.0.0.492986105; __rtbh.lid=%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22OfYH621INR9aBqh56HXa%22%2C%22expiryDate%22%3A%222025-12-02T09%3A22%3A28.103Z%22%7D; _ga_77PZGQW3LE=GS1.1.1733131348.1.1.1733131348.0.1.214431782; _cs_c=0; _cs_id=1c01927b-47f9-ae18-89cd-fa1c7a0a6571.1733131348.1.1733131348.1733131348.1.1767295348573.1; ry_ry-br1c0d3_so_realytics=eyJpZCI6InJ5XzVFREYxMzIwLTZEREEtNDRCNC04Q0JFLTVDMTExMDdCQTREOSIsImNpZCI6bnVsbCwib3JpZ2luIjpmYWxzZSwicmVmIjpudWxsLCJjb250IjpudWxsLCJucyI6dHJ1ZSwic2MiOiJvayIsInNwIjpudWxsfQ%3D%3D; ry_ry-br1c0d3_realytics=eyJpZCI6InJ5XzVFREYxMzIwLTZEREEtNDRCNC04Q0JFLTVDMTExMDdCQTREOSIsImNpZCI6bnVsbCwiZXhwIjoxNzY0NjY3MzQ4NjQxLCJjcyI6MX0%3D; _ga=GA1.2.1165802664.1733131348; _gid=GA1.2.1045313283.1733131349; spses.1bb1=*; spid.1bb1=543c20e4-2039-4400-9a28-abc3f68c3945.1733131349.1.1733131349..0aeb3bd1-6b3b-439a-b6c3-9fe22dded583..f5e04fa1-2935-4279-9bcf-6bbcc931b21f.1733131348765.1; t2s-analytics=7fec9023-722a-4c30-9d5f-3540934db510; t2s-p=7fec9023-722a-4c30-9d5f-3540934db510; _uetsid=f38b8f40b08e11ef838b450545cb0de7; _uetvid=f38c2520b08e11ef9f56ed9788bb3759; cto_bundle=bwfsUV9PUElJUjlMNUVOVlBRanoxaDI2SGJDQ1l3UiUyQnlROWFIODRTUER6Z1hvQ2wxalNRTFJTYmpRMklrTXI1TklmMUFjM2FsZHdrR2VHdjFMbWpCODhKcHhWb0w3WjBESTg4V0hXMnhUeWlRQ1U4b242MUZzYzdlbGRkOElqc0NIZUxk; _gat_prod=1; _fbp=fb.1.1733131349244.148936221959834320; __gads=ID=0380ac42d3784c23:T=1733131348:RT=1733131348:S=ALNI_MYapsAxs68tWLBfCR5qdsZ5V4anKg; __gpi=UID=00000fa5fb39988c:T=1733131348:RT=1733131348:S=ALNI_MbaS6n1cZlzvkQVaUCUU80EuRR1TA; __eoi=ID=d70b78ca116f6989:T=1733131348:RT=1733131348:S=AA-AfjZEqWT_Usw6_ba1r1UVBzvH; _cs_s=1.5.0.9.1733133150154"})
      
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
        
       
        
        