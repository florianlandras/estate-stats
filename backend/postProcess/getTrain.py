from urllib.parse import urlencode
from bs4 import BeautifulSoup
import json
import requests
import re
import pandas as pd
from urllib import request
import numpy as np
import getSimilar
import datetime

def getTrain(url) :
    
    # Parse the html
    html = requests.get(url)
    soup = BeautifulSoup(html.text , 'html.parser')

    # Requirements
    linkArray = []
    first = True
    compt = 2

    # Get all the links in array
    for elem in soup.find_all('a',class_="item-link-container", href=True): 
        if elem.text: 
            linkArray.append(elem['href'])

   # Create the dataframe from Json

    for elem in linkArray :
        html = requests.get(elem)
        soup = BeautifulSoup(html.text , 'html.parser')

        # Create the DataFrame
        if first :
        #json
            jsonContainer = soup.find_all("div",attrs={"data-initial-data" : True})
            monJson = json.loads(jsonContainer[0]["data-initial-data"])
            dfJson = pd.DataFrame(monJson)
            dfJson = dfJson["listing"].T
            first = False
    
        # Append next element to the dataframe
        else :
        
            jsonContainer = soup.find_all("div",attrs={"data-initial-data" : True})
            monJson = json.loads(jsonContainer[0]["data-initial-data"])
            dfTemp = pd.DataFrame(monJson)
            dfTemp = dfTemp["listing"].T
            dfJson = pd.concat([dfJson, dfTemp], axis=1, sort=False)
    
    # Rearrange the dataframe
    dfJson = dfJson.T

    # Remake an index
    df = dfJson.reset_index(drop = True)

    # Clean the dataframe and put all numbers in float

    df = df.rename(columns={"asked_price": "begartPris", "typeSummary": "typ", "land_area": "tomt", "living_space" : "boarea", "price" : "slutPris", "price_per_area" : "prisPerM2", "rooms" : "rum", "supplemental_area": "biarea" })

    df = df[['begartPris','tomt','boarea', 'slutPris', 'prisPerM2', 'rum', 'biarea', 'typ']]

    df['begartPris'] = df.begartPris.str.replace(r"[a-zA-Zä]",'')
    df['begartPris'] = df['begartPris'].str.replace('\xa0', '')
    df["begartPris"] = pd.to_numeric(df["begartPris"])
    df['slutPris'] = df.slutPris.str.replace(r"[a-zA-Zä<=>.'--'-/-]",'')
    df['slutPris'] = df['slutPris'].str.replace('\xa0', '')
    df["slutPris"] = pd.to_numeric(df["slutPris"])
    df['tomt'] = df.tomt.str.replace(r"[a-zA-Zm²]",'')
    df['tomt'] = df['tomt'].str.replace('\xa0', '')
    df["tomt"] = pd.to_numeric(df["tomt"])
    df['boarea'] = df.boarea.str.replace(r"[a-zA-Zm²]",'')
    df['boarea'] = df['boarea'].str.replace('\xa0', '')
    df["boarea"] = pd.to_numeric(df["boarea"])
    df['prisPerM2'] = df.prisPerM2.str.replace(r"[a-zA-Zkr/m²]",'')
    df['prisPerM2'] = df['prisPerM2'].str.replace('\xa0', '')
    df["prisPerM2"] = pd.to_numeric(df["prisPerM2"])
    df['biarea'] = df.biarea.str.replace(r"[a-zA-Zm²]",'')
    df['biarea'] = df['biarea'].str.replace('\xa0', '')
    df["biarea"] = pd.to_numeric(df["biarea"])
    df['rum'] = df.rum.str.replace(r"[a-zA-Z]",'')
    df['rum'] = df['rum'].str.replace('\xa0', '')
    df['rum'] = df['rum'].str.replace(',', '.')
    df["rum"] = pd.to_numeric(df["rum"])
    


    
    return df

if __name__ == "__main__":
    t = datetime.datetime.now()
    url = "https://www.hemnet.se/bostad/villa-4rum-slatbaken-husbyvik-soderkopings-kommun-husaby-strand-16-17083596"
    url2 = getSimilar.getLink(url)
    df = getTrain(url2)
    print(df)
    t1 = datetime.datetime.now()
    print(t1.second - t.second)