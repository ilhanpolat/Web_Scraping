import requests
from bs4 import BeautifulSoup
import pandas as pd

page = 0
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

book_names = list()
book_prices = list()

for i in range(0,5):
    page += 1
    url = f"https://www.kitapyurdu.com/index.php?route=product/best_sellers&page={page}&list_id=18&filter_in_stock=1&filter_in_stock=1&limit=100"
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, "html.parser")
    books = soup.find_all("div", {"class", "product-cr"})

    
    for book in books:
        try:
            book_names.append(book.find("div", {"class", "name"}).text)
        except:
            book_names.append(None)

   
    for book in books:
        try:
            book_prices.append(float(book.find("div", {"class", "price-new"}).find("span", {"class", "value"}).text.strip().replace(",",".")))
        except:
            book_prices.append(None) 
    print(f"{page}. sayfa başarıyla scrape edildi.")
df = pd.DataFrame({"book_name":book_names, "price":book_prices})
df.to_csv("books.csv", index=False, encoding="utf-8")

