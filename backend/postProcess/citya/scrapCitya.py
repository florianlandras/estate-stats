from urllib import request
from bs4 import BeautifulSoup
import re
import pandas as pd

def getDf (url):

    html = request.urlopen(url)

    soup = BeautifulSoup(html , 'html.parser')

    areaArray = []
    nbrRoomArray = []
    priceArray = []
    pricePerSquareMeterArray = []
    
    #find all area and room number
    areaP = soup.find_all("p", class_="title color-main")

    for sentence in areaP:
        nbrRoom, area = re.findall(r"[-+]?\d*\.\d+|\d+", sentence.get_text()) #get int and float from string

        area = float(area) #converting to float
        nbrRoom = int(nbrRoom) #converting to int

        areaArray.append(area)
        nbrRoomArray.append(nbrRoom)

    #find all price
    priceP = soup.find_all("div", class_="button reverse-button border-color-ven")

    for sentence in priceP:
        price = re.findall(r"[-+]?\d*\.\d+|\d+", sentence.get_text()) #get int and float from string

        price = int(price[0]+price[1]) # concat string and convert in int
        
        priceArray.append(price)

    #calculate pricePerSquareMeterArray 
    for i in range(len(priceArray)):
        pricePerSquareMeterArray.append(float(priceArray[i]/areaArray[i]))

   # Create the pandas DataFrame #TODO normalize name of column in dataframe
    data = { 
        "area":areaArray,
        "nbrRoom": nbrRoomArray,
        "price": priceArray,
        "pricePerSquareMeter": pricePerSquareMeterArray,
    }
    return  pd.DataFrame(data)
    

if __name__ == '__main__':
    url ="https://www.citya.com/annonces/vente/appartement,maison/nice-06088?sort=b.dateMandat&direction=desc&prixMin=0&prixMax=1000000&nbrePiecesMin=0&nbrePiecesMax=10&surfaceMin=0&surfaceMax=111"
    print(getDf(url))