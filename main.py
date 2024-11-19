import requests, re, datetime
from bs4 import BeautifulSoup

def main(userfruit: str):

    if userfruit.lower() == 'spin':

        return 'Fruit Spring is in stock'
    
    elif userfruit.lower() == 'rocket':

        return 'Fruit Rocket is in stock'

    r = requests.get(f'https://blox-fruits.fandom.com/wiki/Blox_Fruits_%22Stock%22')

    current_stock_id: str = 'mw-customcollapsible-Current'

    soup = BeautifulSoup(r.content, 'html.parser')

    div_tags = soup.find_all('div', {'class': 'fruit-stock'})

    fruits = set()

    money_b = '<span class="color-currency(Money)"> <a href="/wiki/Money" title="Money"><img alt="MoneyIcon" class="lazyload" data-image-key="MoneyIcon.png" data-image-name="MoneyIcon.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/roblox-blox-piece/images/4/47/MoneyIcon.png/revision/latest/scale-to-width-down/10?cb=20240729150529" decoding="async" height="20" loading="lazy" src="data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D" width="10"/></a> '
    money_a = "</span></div></div>"

    for div in div_tags:

        if current_stock_id in str(div.find_parent('div')):

            price = None
            
            p1 = str(div).split(money_b)[1]
            p2 = str(p1).split(money_a)[0]

            price = p2

            frt = str(re.search(r'title=([^>]+)', str(div)).group(1))

            fruits.add(frt + ' for ' + price + '$')


    stock = ['rocket for 5,000$', 'spin for 7,500$']

    for fruit in fruits:

        a = str(fruit).replace('"', "")

        stock.append(a)

    fruits_on_stock = '2. Fruits on stock: ' + ', '.join(x.title() for x in stock)

    fruits_lower = [x.lower() for x in stock]

    fruit_lower = str(userfruit).replace('"', "").lower()

    b = None

    for e in fruits_lower:

        if fruit_lower in e.split():

            b = e.split('for ')[1]

            result = f'Fruit {userfruit.capitalize()} is in stock for ' + b

            break
        
        else:
        
            result = f'Fruit {userfruit} is not in stock'

    return '1. ' + result + '\n\n2. Fruits in stock: ' + ', '.join(x.title().replace("For", "for") for x in stock)


fruitinput = input('Type in the name of the fruit\n\nFruit: ')
print('\n' + main(fruitinput), '\n')
input()
