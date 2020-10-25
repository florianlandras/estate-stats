
from urllib.parse import urlencode
from urllib import request
from bs4 import BeautifulSoup
import re
import pandas as pd

def get (dictionnaire) :

    """
    In : dictionary with query words
    Out: Url string


    Base Url : https://www.citya.com/annonces/vente/

    + type separated by ","
        modificator : appartement,maison/ or appartement/ or maison/

    + locations separated by "," and mandatory postal code separate by "-"
        locations : nice-06088,paris-75000/

    + "?sort=b.dateMandat&direction=desc&"

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
    
    ex:
    https://www.citya.com/annonces/vente/appartement,maison/nice-06088,paris-75000?prixMin=0&prixMax=555555&nbrePiecesMin=0&nbrePiecesMax=10&surfaceMin=0&surfaceMax=111
    
    #TODO get the right postal code by requesting with a generic postal code ex :

    To process be processed, the url need to carry the city name + a postal code specific for citya like this :
    https://www.citya.com/annonces/vente/appartement,maison/nice-06088

    We know that if we request this :
    https://www.citya.com/annonces/vente/appartement,maison/nice-06000


    The website will change its url by:
    https://www.citya.com/annonces/vente/appartement,maison/nice-06088

    We can find the new url in html at this line : 
    <link rel="canonical" href="https://www.citya.com/annonces/vente/nice-06088" />

    So if we can get the postal code after a request with a generic (but valid) postal code we will be able to get the right page. 
    
    """

    baseUrl = "https://www.citya.com/annonces/vente/appartement,maison/"

    url = baseUrl + dictionnaire["ville"] + "?sort=b.dateMandat&direction=desc&" #TODO Better url construction

    del dictionnaire["ville"] #Now delete key pair "ville" to encode query words
    maQuery = urlencode(dictionnaire)

    url = url + maQuery #Now add encoded Query to url

    return url



if __name__ == '__main__':
    
    ville = 'nice'        #TODO integrer la fonction de verification des villes dans un fichier a part
    df=pd.read_csv('villes_france.csv')
    df.info
    dfVille = df['Ozan']
    dfVille = dfVille.str.lower()
    if dfVille.str.contains(ville).any() :
        dictionnaire = {          #TODO Need to normalize user input between each post process scrapping
        "ville":ville,        
        "prixMin":"0",
        "prixMax":"100000",
        "nbrePiecesMin":"0",
        "nbrePiecesMax":"10",
        "surfaceMin":"0",
        "surfaceMax":"111",  
        }
        print(get(dictionnaire)) 

    else :
        print("This city don't exist")
    



    
