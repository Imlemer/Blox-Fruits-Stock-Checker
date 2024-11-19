import requests, re
from bs4 import BeautifulSoup
from config import ps, e, all_fruits
import smtplib
import time





def main():

    r = requests.get(f'https://blox-fruits.fandom.com/wiki/Blox_Fruits_%22Stock%22')

    current_stock_id: str = 'mw-customcollapsible-Current'

    soup = BeautifulSoup(r.content, 'html.parser')

    div_tags = soup.find_all('div', {'class': 'fruit-stock'})

    stock = ["rocket", "spin"]

    email = e
    receiver = None

    server = smtplib.SMTP('smtp.gmail.com', 587)

    server.starttls()

    server.login(email, ps)

    fruit = input('Please enter the fruit: ')


    if not fruit.lower().capitalize() in all_fruits:

        print('Fruit ' + fruit + ' does not exist. Make sure to check your spelling, maybe you made a typo?')
        return

    receiver = input('Please enter your email so we can notify you when your fruit is in stock: ')


    print('You can now minimize the window, we will send you an email when your fruit appears in stock!\nMake sure to check the "Spam" tab, since the email might go here\n')

    for div in div_tags:

        if current_stock_id in str(div.find_parent('div')):

            frt = str(re.search(r'title=([^>]+)', str(div)).group(1))

            stock.append(frt.lower().replace('"', ''))

    msg = f'Subject: Your fruit is in stock!\n\nThe {fruit} Blox Fruit is in stock! https://www.roblox.com/games/2753915549/Blox-Fruits'

    while True:

        if fruit in stock:

            server.sendmail(email, receiver, msg)
            break

        time.sleep(30)


if __name__ == '__main__':

    main()
