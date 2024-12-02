import items
import general_func as g
import io


def write_text(txt):
    with open("text.txt", "w") as file:
        file.write(txt)

if __name__ == "__main__":
    item = g.get_categories_url()
    start_urls = item["product_list_url"]
    print(start_urls)