def get_data(search):
    from bs4 import BeautifulSoup
    import requests

    headers = {'User-Agent':'Mozilla/5.0'}

    url = 'https://www.zomato.com/hyderabad/mcdonalds-himayath-nagar/order'

    response = requests.get(url,headers=headers)

    soup = BeautifulSoup(response.content,'lxml')

    mcdonalds={}
    for item in soup.select('.sc-1s0saks-17.bGrnCu'):
        name=item.select('.sc-1s0saks-15.iSmBPS')[0].get_text()
        price=item.select('.sc-17hyc2s-1.cCiQWA')[0].get_text()
        mcdonalds[name]=price
    print(mcdonalds)
    return mcdonalds.get(search)

def get_data2(search):
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
        mcdonalds1[name]=price
    print(mcdonalds1)
    return mcdonalds1.get(search)

    # return mcdonalds1.get(search)    
