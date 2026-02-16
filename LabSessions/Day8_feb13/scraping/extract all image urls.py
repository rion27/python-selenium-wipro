from bs4 import BeautifulSoup
import requests

url="https://books.toscrape.com"

headers={
    "User-Agent": "Chrome/121.0.0.0 Safari/537.36"
}

response=requests.get(url,headers=headers)
print(response.status_code)
#parsing
soup=BeautifulSoup(response.text,"html.parser")

images=soup.find_all("img")
for i in images:
    img_src=i.get('src')
    print(img_src)