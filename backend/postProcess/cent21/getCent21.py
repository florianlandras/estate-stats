#import post process

from urllib import request
from urllib.parse import urlencode
from bs4 import BeautifulSoup
# TODO process multiple pages



def get (dictionnaire) :
    """in dictionnaire
       out url
    """
    baseUrl = "https://www.century21.fr/annonces/"

    if dictionnaire["achatmaison"] == "oui" and dictionnaire["achatappart"] == "non" :
        txtBien = "achat-maison/"
    if dictionnaire["achatappart"] == "oui" and dictionnaire["achatmaison"] == "non": 
        txtBien = "achat-appart/"
    if dictionnaire["achatappart"] == "oui" and dictionnaire["achatmaison"] == "oui":
        txtBien = "achat-maison-appartement/"
    
    ville = "v-" + dictionnaire["ville"]
    urlCent21 = baseUrl + txtBien + ville
    return urlCent21
    


#https://www.century21.fr/annonces/achat-maison-appartement/v-toulon/alentours-15/s-0-/st-0-/b-0-/page-1/
if __name__ == '__main__':
    dictionnaire = {
        "achatmaison":"oui",
        "achatappart":"non",
        "ville" : "toulon",


    }
    print(get(dictionnaire))

    
    
    