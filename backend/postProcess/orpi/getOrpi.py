#import post process

from urllib import request
from urllib.parse import urlencode
from bs4 import BeautifulSoup
import json


def dataJson (dictionnaire) :

    baseUrl = 'https://www.orpi.com/recherche/buy?'
    maQuery = urlencode(dictionnaire)
    url = baseUrl + maQuery

    html = request.urlopen(url)

    soup = BeautifulSoup(html , 'html.parser')


    # cibler le json dans le html qui est dans un attribut de Div et le mettre dans un container
    jsonContainer = soup.find_all("div",attrs={"data-result" : True})

    # charger le json avec la library standard json et le mettre dans monJson
    # jsoncontainer est un array, a cause du soup.find_all
    # nous savons qu'il existe qu'un seul element, donc jsoncontainer[0] contient l'element
    # le json est contenu dans la valeur de l'attribut data-result ( Le data-result est la clé de la valeur du json )
    # Donc on accede a la valeur avec jsoncontainer[0][data-result]

    monJson = json.loads(jsonContainer[0]["data-result"])
    return monJson

        
