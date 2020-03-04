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


    # list of area + nbr de room
    areaArray = []
    nbrRoomArray = []
    area = soup.find_all( "h4" , attrs = { "class" : "detail_vignette"})

    for a in area : 
        temp2, temp3, temp4 = re.findall(r"[-+]?\d*\.\d+|\d+", a.get_text()) # getting ['240', '000']
        temp2 = temp2+"."+temp3
        temp2 = float(temp2)
        areaArray.append(temp2)
        nbrRoomArray.append(temp4)
    

    #list of price per square meters
    pricePerSquareMeterArray = []
    for i in range(len(priceArray)):
        pricePerSquareMeterArray.append(float(priceArray[i]/areaArray[i]))
        
    #print(priceArray)
    #print(areaArray)
    #print(nbrRoomArray)
    
    # Create the pandas DataFrame
    
    data = { 
        "area":areaArray,
        "nbrRoom": nbrRoomArray,
        "price": priceArray,
        "price/m2": pricePerSquareMeterArray, #TODO normalize df columns names
    }
    return  pd.DataFrame(data)
    


if __name__ == '__main__':
    url = "https://www.century21.fr/annonces/achat-maison/v-toulon"
    print(getDf(url))