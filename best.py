from bs4 import BeautifulSoup
import requests
import html5lib
url="https://www.zomato.com/hyderabad/mcdonalds-himayath-nagar/order"

response=requests.get(url)
soup = BeautifulSoup(response.content,html5lib)
spans=soup.find_all('span','sc-17hyc2s-1.cCiQWA')
for span in spans:
    print(span.text)