from bs4 import BeautifulSoup
import requests
url="http://books.toscrape.com/"

headers={
    "User-Agent": "Chrome/121.0.0.0 Safari/537.36"
}

response=requests.get(url,headers=headers)
print(response.status_code)
#parsing the html
soup=BeautifulSoup(response.text,"html.parser")

#finding all product containers
products=soup.find_all("article",class_="product_pod")
for product in products:
    #name
    name=product.h3.a.get("title")

    #price
    price=product.find("p",class_="price_color").text

    #rating
    rating=product.find("p",class_="star-rating")["class"][1]

    #availability
    availability=product.find("p",class_="instock availability").text.strip()

    print("Name:", name)
    print("Price:", price)
    print("Rating:", rating)
    print("Availability:", availability)
    print("-" * 40)