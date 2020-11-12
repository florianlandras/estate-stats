from urllib.parse import urlencode
from bs4 import BeautifulSoup
import json
import requests
import re
import pandas as pd
from urllib import request
import numpy as np


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
            dfJson.rename({'listing': "0"}, inplace=True)
            first = False
    
        # Append next element to the dataframe
        else :
        
            jsonContainer = soup.find_all("div",attrs={"data-initial-data" : True})
            monJson = json.loads(jsonContainer[0]["data-initial-data"])
            dfTemp = pd.DataFrame(monJson)
            dfTemp = dfTemp["listing"].T
            dfTemp.rename({'listing': compt}, inplace=True)
            dfJson = pd.concat([dfJson, dfTemp], axis=1, sort=False)
    
    # Rearrange the dataframe
    dfJson = dfJson.T

    # Remake an index
    dfJson = dfJson.reset_index(drop = True)
    


    
    return dfJson

if __name__ == "__main__":
    url =  "https://www.hemnet.se/salda/bostader?housing_form_groups%5B%5D=houses&location_ids%5B%5D=17774"
    df = getTrain(url)
    print(df)