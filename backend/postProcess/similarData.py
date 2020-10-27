from urllib.parse import urlencode
from bs4 import BeautifulSoup
import json
import requests
import re
import pandas as pd
from urllib import request
import numpy as np

def getdef(url) :
    """[summary]

    Args:
        url ([type]): [description]
    """

    html = requests.get(url)
    soup = BeautifulSoup(html.text , 'html.parser')

    areaArray = []
    nbrRoomArray = []
    priceArray = []
    priceFinalArray = []
    pricePerSquareMeterArray = []
    adressArray = []


# a / area + nbr of room
    a = soup.find_all('div', class_ = "sold-property-listing__subheading sold-property-listing--left" )
    for elem in a :
        temp1 = re.findall(r"[-+]?\d*\.\d+|\d+", elem.get_text())
        areaArray.append(temp1)
    
    df = pd.DataFrame(data=areaArray, columns=["Area","Rooms", "Rooms2"])
    df.replace(to_replace=[None], value=np.nan, inplace=True)
    df = df.fillna(0)
    del df['Rooms2']

    
    # b /adress
    b = soup.find_all('span', class_ = "item-result-meta-attribute-is-bold item-link" )
    #b2 / adress city
    b2 = soup.find_all('span', class_ = "item-link" )
    
    # c / final price
    c = soup.find_all('span', class_ = "sold-property-listing__subheading sold-property-listing--left" )
    
    for elem in c :
        temp1 = re.findall(r"[-+]?\d*\.\d+|\d+", elem.get_text())
        priceFinalArray.append(temp1)
        
    df2 = pd.DataFrame(data=priceFinalArray, columns=["1","2", "3"])
    df2.replace(to_replace=[None], value=np.nan, inplace=True)
    df2 = df2.fillna("")
    df2["Final Price"] = df2["1"] + df2["2"] + df2["3"]
    df["Final Price"] = df2["Final Price"]
    
    # d / % difference between market entrance price and final price
    d = soup.find_all('div', class_ = "sold-property-listing__price-change" )
    # e / date de la vente
    e = soup.find_all('div', class_ = "sold-property-listing__sold-date sold-property-listing--left" )
    #f / pricePerMeterSquare
    f = soup.find_all('div', class_ = "sold-property-listing__price-per-m2 sold-property-listing--left" )
    # g/ surface non habitable
    g = soup.find_all('div', class_ = "sold-property-listing__supplemental-area sold-property-listing--left" )
    # h/surface du terrain
    h = soup.find_all('div', class_ = "sold-property-listing__land-area sold-property-listing--left" )
    # i / type de bien
    i =  soup.find_all('span', class_ = "hide-element" )
    #j charge ???
    j =  soup.find_all('div', class_ = "sold-property-listing__fee" )
    # k/ lien du bien immobilier pour plus d'infos
    k = soup.find_all('a', class_ = "item-link-container" )
    
    # Convert values to float
    
    df["Area"] = df["Area"].astype(float)
    df["Rooms"] = df["Rooms"].astype(float)
    df["Final Price"] = df["Final Price"].astype(float)



    return df

if __name__ == "__main__":
    baseUrl = 'https://www.hemnet.se/salda/'
    city = 'soderkopings-kommun'
    url = baseUrl + city
    df = getdef(url)
    print(df)