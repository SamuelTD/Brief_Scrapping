import items
import general_func as g
import io
import requests

# Initialisez une session
session = requests.Session()

# Première requête pour obtenir les cookies
url_homepage = "https://www.bricodepot.fr"
response = session.get(url_homepage, headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
})

# Affiche les cookies reçus
print(session.cookies.get_dict())

# Utilisez la session pour d'autres requêtes
# url_products = "https://www.bricodepot.fr/catalogue/amenagement-despaces/cuisine/eclairage-de-cuisine/spot-led/"
# response_products = session.get(url_products, headers={
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
# })

# print(response_products.text)

# def write_text(txt):
#     with open("text.txt", "w") as file:
#         file.write(txt)

# if __name__ == "__main__":
#     item = g.get_categories_url()
#     start_urls = item["product_list_url"]
#     print(start_urls)