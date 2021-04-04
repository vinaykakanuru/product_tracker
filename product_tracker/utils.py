import os

import environ
import lxml
import requests
from bs4 import BeautifulSoup

environ.Env.read_env()
env = environ.Env(DEBUG=(bool, False),)


def get_link_data(url):

    headers = {
        "User-Agent": os.environ.get('User-Agent'),
        "Accept-Language": 'en',
    }

    r = requests.get(url, headers=headers)

    soup = BeautifulSoup(r.text, "lxml")

    product_name = soup.select_one(selector="#productTitle").getText().strip()

    product_price = soup.select_one(selector="#priceblock_ourprice").getText()
    product_price = float(product_price[2:].replace(',', ''))

    return (product_name, product_price)
