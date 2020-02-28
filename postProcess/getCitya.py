
from urllib import request
from urllib.parse import urlencode
from bs4 import BeautifulSoup
import json


def scrapping () :

    """

    Base Url : https://www.citya.com/annonces/vente/

    + type separated by ","
        modificator : appartement,maison/ or appartement/ or maison/

    + locations separated by ","
        locations : nice-06088,paris-75000/

    + "?"

    + Query:
        Query key/value for citya:

        {
            "prixMin":"0",
            "prixMax":"100000",
            "nbrePiecesMin":"0",
            "nbrePiecesMax":"10",
            "surfaceMin":"0",
            "surfaceMax":"111",
        }
    
    = https://www.citya.com/annonces/vente/appartement,maison/nice-06088,paris-75000?prixMin=0&prixMax=555555&nbrePiecesMin=0&nbrePiecesMax=10&surfaceMin=0&surfaceMax=111
    """

    baseUrl = "https://www.citya.com/annonces/vente"

    url = baseUrl 

    html = request.urlopen(url)





if __name__ == '__main__':
    scrapping()  # Put the a call to the main function in the file.    
        
