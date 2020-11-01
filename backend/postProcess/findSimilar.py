from urllib.parse import urlencode
from bs4 import BeautifulSoup
import json
import requests
import re
import pandas as pd

def getSimilar(url) :



    html = requests.get(url)
    soup = BeautifulSoup(html.text , 'html.parser')


    a = soup.find("a", {"class": "similar-listings-search-link__button"}).attrs['href']
    newhtml = requests.get(a)
    soup2 = BeautifulSoup(newhtml.text , 'html.parser')

    link = soup2.find("a", {"class": "result-type-toggle__link js-result-type-toggle-sold-link qa-result-type-toggle-sold-link"}).attrs['href']

    link = "https://www.hemnet.se" + link

    print(link)

    return link


if __name__ == "__main__":
    url = "https://www.hemnet.se/bostad/villa-4rum-slatbaken-husbyvik-soderkopings-kommun-husaby-strand-16-17083596"
    getSimilar(url)
    
