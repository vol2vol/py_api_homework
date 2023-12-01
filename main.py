import requests
from bs4 import BeautifulSoup
import sqlite3

def parser(url:str):
    response = requests.get(url=url)
    html = response.text
    soup = BeautifulSoup(html, "lxml")
    products = soup.find_all("div", class_="ty-column5")
    
    urls = []
    for product in products:
        name_elem = product.find("a", class_="product-title")
        link = name_elem.get("href")
        urls.append(link)
    
    args = []
    for url in urls:
        response = requests.get(url=url)
        html = response.text
        soup = BeautifulSoup(html, "lxml")
        name = soup.select_one("h1").text
        #price = soup.select_one("span.ty-product-block__price-actual").get('content')
        description =  soup.select_one("div.ty-product-block__description").text
        args.append((name, description))

    conn = sqlite3.connect("mydata.db")

    cursor = conn.cursor()

    cursor.executemany("INSERT INTO blocks VALUES (?,?)", args)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    parser(url="https://fabrika-betonov.ru/catalog/")