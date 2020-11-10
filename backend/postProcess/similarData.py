from urllib.parse import urlencode
from bs4 import BeautifulSoup
import json
import requests
import re
import pandas as pd
from urllib import request
import numpy as np


def getTrain(url) :
    """[summary]

    Args:
        url ([type]): [description]
    """

    html = requests.get(url)
    soup = BeautifulSoup(html.text , 'html.parser')

    areaArray = []
    nbrRoomArray = []
    priceArray = []
    slutArray = []
    pricePerSquareMeterArray = []
    adressArray = []
    tomtArray = []


    # a / Tomt
    a = soup.find_all('div', class_ = "sold-property-listing__land-area sold-property-listing--left")
    for elem in a :
        temp1 = re.findall(r"[-+]?\d*\.\d+|\d+", elem.get_text())
        tomtArray.append(temp1)
      
    df = pd.DataFrame(data=tomtArray, columns=["1","2"])
    df.replace(to_replace=[None], value=np.nan, inplace=True)
    df["Tomt"] = df["1"] + df["2"].fillna('')
    df = df.drop(df.columns[[0, 1]], axis=1)

    


    # Room and size

    b = soup.find_all('div', class_ = "sold-property-listing__subheading sold-property-listing--left")
    for elem in b :
        temp1 = re.findall(r"[-+]?\d*\.\d+|\d+", elem.get_text())
        areaArray.append(temp1)

    df2 = pd.DataFrame(data=areaArray , columns = ['Area', 'Rooms', 'extra'])
    df2.replace(to_replace=[None], value=np.nan, inplace=True)
    df['Area'] = df2['Area']
    df['Rooms'] = df2['Rooms']


    # SlutPrice
    b = soup.find_all('span', class_ = "sold-property-listing__subheading sold-property-listing--left")
    for elem in b :
        temp1 = re.findall(r"[-+]?\d*\.\d+|\d+", elem.get_text())
        slutArray.append(temp1)

    df3 = pd.DataFrame(data=slutArray , columns = ['1', '2', '3'])
    df3.replace(to_replace=[None], value=np.nan, inplace=True)
    df3['SlutPrice'] = df3['1'] + df3['2'] + df3['3'].fillna('')
    df['SlutPrice'] = df3['SlutPrice']

    #print(df)


    # More infos link :
    linkArray = []
    tableArray =[]
    tArray = []
    # charges par mois
    driftArray =[]
    # surface non comptabilisée.
    biareaArray =[]

    for elem in soup.find_all('a',class_="item-link-container", href=True): 
        if elem.text: 
            linkArray.append(elem['href'])
    """ 
    for elem in linkArray :
        html = requests.get(elem)
        soup = BeautifulSoup(html.text , 'html.parser')
        #driftkosnad
        table = soup.find_all('dd', class_ = "sold-property__attribute-value")
        for line in table :
            #temp1 = re.findall(r"[-+]?\d*\.\d+|\d+", line.get_text())
            #tArray.append(temp1)
            tArray.append(line.text.replace(u'\xa0', u'').split("\n"))
    
         
        for line in table : 
            tableArray.append(line.text.replace(u'\xa0', u'').split("\n"))
            #print(line.text)
        for i in tableArray :
            i = list(filter(None, i))
            tArray.append(i)
        """
    #print(tArray)
    return df

if __name__ == "__main__":
    url =  "https://www.hemnet.se/salda/bostader?housing_form_groups%5B%5D=houses&location_ids%5B%5D=17774"
    df = getTrain(url)
    print(df)