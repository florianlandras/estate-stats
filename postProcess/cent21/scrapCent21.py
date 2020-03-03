from urllib import request
from bs4 import BeautifulSoup
import re
import pandas as pd

def getDf (url) : 
    """
    in : url
    out : dataframe
    """
    html = request.urlopen(url)

    soup = BeautifulSoup(html , 'html.parser')

   # list of prices
    priceArray = []
    price = soup.find_all( "div" , attrs = { "class" : "price"})
    for p in price : 
        temp = re.findall(r"[-+]?\d*\.\d+|\d+", p.get_text()) # getting ['240', '000']
        temp = temp[0]+temp[1]
        temp = float(temp)

        priceArray.append(temp)


    # list of area
    areaArray = []
    
    #list of price per square meters
    pricePerSquareMeterArray = []
        
    print(priceArray)


    



    


if __name__ == '__main__':
    url = "https://www.century21.fr/annonces/achat-maison/v-toulon"
    print(getDf(url))