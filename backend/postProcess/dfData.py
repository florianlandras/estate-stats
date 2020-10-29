from urllib.parse import urlencode
from bs4 import BeautifulSoup
import json
import requests
import re
import pandas as pd
from urllib import request
import numpy as np

def dfData(url) :

    html = requests.get(url)
    soup = BeautifulSoup(html.text , 'html.parser')

    # Get Price

    price = soup.find('p', class_ = "property-info__price qa-property-price" ).text
    price = price.split()
    # join, entre guillement sepâration avec le caractere que l'on veut, et entre crochet ce qu'on veut omettre.
    price = "".join(price[:-1])
    price = int(price)

    # Get size

    # Get Nbr de chambre

    # Get size terrain

    # Get annee de construction

    # charges
    return price

if __name__ == "__main__":
    url = 'https://www.hemnet.se/bostad/villa-4rum-slatbaken-husbyvik-soderkopings-kommun-husaby-strand-16-17083596'
    print(dfData(url))
