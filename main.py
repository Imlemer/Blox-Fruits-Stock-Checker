import requests, re, datetime
from bs4 import BeautifulSoup

def main(userfruit: str):

    r = requests.get(f'https://blox-fruits.fandom.com/wiki/Blox_Fruits_%22Stock%22')

    current_stock_id: str = 'mw-customcollapsible-Current'

    soup = BeautifulSoup(r.content, 'html.parser')

    div_tags = soup.find_all('div', {'class': 'fruit-stock'})

    fruits = set()

    for div in div_tags:

        if current_stock_id in str(div.find_parent('div')):

            fruits.add(re.search(r'title=([^>]+)', str(div)).group(1))


    stock = ['rocket', 'spin']

    for fruit in fruits:

        a = str(fruit).replace('"', "")

        stock.append(a.lower())

    if str(userfruit).replace('"', "").lower() in stock:

        result = f'Fruit {userfruit} is in stock' 
        
    else:
        
        result = f'Fruit {userfruit} is not in stock'

    return '1. ' + result + '\n\n2. Fruits on stock: ' + ', '.join(x.title() for x in stock)


fruitinput = input('Type in the name of the fruit\n\nFruit: ')
print('\n' + main(fruitinput), '\n')
input()
