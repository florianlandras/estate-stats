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

    
    tableArray =[]
    # Get size
    table = soup.find('div', class_ = "property-attributes-table" )
    table = table.find_all('div')
    for line in table : 
        tableArray.append(line.text.replace(u'\xa0', u'').split("\n"))
    #print(line.text)
    tArray = []
    for elem in tableArray :
        elem = list(filter(None, elem))
        tArray.append(elem)

    tDict = {}
    tArray.pop()
    for x in tArray:
        tDict[x[0]] = x[1]
    
    
    price = soup.find('p', class_ = "property-info__price qa-property-price" ).text
    price = re.sub("\D","",price)
    

    df = pd.DataFrame([tDict])
    df = df[['Antal rum', 'Boarea', 'Tomtarea', 'Byggår', 'Driftkostnad']]
    df['pris'] = int(price)
    df.to_csv(r'/Users/florianlandras/Documents/GitHub/estate-stats/backend/postProcess/\dataToCompare.csv', index = False)
    
    return df

if __name__ == "__main__":
    url = 'https://www.hemnet.se/bostad/villa-3rum-snovelstorp-soderkopings-kommun-grenstigen-10-17051696'
    print(dfData(url))
