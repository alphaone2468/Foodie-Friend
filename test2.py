
from bs4 import BeautifulSoup
import requests

headers = {'User-Agent':'Mozilla/5.0'}

url = 'https://www.swiggy.com/restaurants/mcdonalds-alto-trade-center-himayath-nagar-hyderabad-23707'

response = requests.get(url,headers=headers)

soup = BeautifulSoup(response.content,'lxml')

mcdonalds1={}
for item in soup.find_all(class_='styles_detailsContainer__22vh8'):
        name=item.find_all(class_='styles_itemNameText__3ZmZZ')[0].get_text()
        price=item.find_all(class_='rupee')[0].get_text()
        print(name)
        print(price)