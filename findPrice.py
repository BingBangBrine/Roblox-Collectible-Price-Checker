import requests
from bs4 import BeautifulSoup
import webbrowser
import time


def searchFunction(cookie, URL):
    requestSession = requests.Session()
    requestSession.cookies[".ROBLOSECURITY"] = cookie

    price = 9993550599999999
    page = requestSession.get(URL)
    # print(f'requestSession {requestSession}')
    # print(f'page {page}')

    soup = BeautifulSoup(page.content, 'html.parser')
    if soup is not None:
        info = soup.find('div', class_='page-content')
        if info is not None:
            price = int(info.get('data-expected-price'))
            return price

    return price


itemID = 1029025  # example item
URL = 'https://www.roblox.com/catalog/' + str(itemID)
balance = 500  # enter your balance
purchasable = False

# the cookie can be found in inspect element, application cookies, .roblosecurity and you can use any account to do it
file = open("cookie.txt", 'r')
cookie = file.read()
file.close()

# prevPrice = 592135928351235
while not purchasable:
    startTime = time.perf_counter()

    price = searchFunction(cookie, URL)
    if price != 0 and price <= balance:
        webbrowser.open(URL, new=1, autoraise=True)
        purchasable = True

    # if prevPrice < price:  #opens new window each time the price lowers
    #     webbrowser.open(URL, new=1, autoraise=True)

    endTime = time.perf_counter()
    timeTaken = int((endTime - startTime) * 1000)

    print(price, str(timeTaken) + "ms")

    delay = 1  # time in seconds to take for the total request time and time to wait afterwards

    if timeTaken < (delay * 1000):  # so it doesnt overflow the url, can set delay
        print(f'waiting for {(delay - (timeTaken / 1000)) * 1000:.0f}ms\n')
        time.sleep(delay - (timeTaken / 1000))

    # prevPrice = price
