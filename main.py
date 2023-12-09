import requests
from bs4 import BeautifulSoup
import sqlite3

def parse_and_store_data(url: str) -> None:
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "lxml")
    products = soup.find_all("div", class_="ty-column5")
    
    urls = [product.find("a", class_="product-title").get("href") for product in products]
    
    data = []
    for url in urls:
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, "lxml")
        name = soup.select_one("h1").text
        description =  soup.select_one("div.ty-product-block__description").text
        data.append((name, description))

    conn = sqlite3.connect("mydata.db")

    cursor = conn.cursor()

    cursor.executemany("INSERT INTO blocks VALUES (?, ?)", data)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    parse_and_store_data(url="https://fabrika-betonov.ru/catalog/")