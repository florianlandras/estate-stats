
#import post process

from urllib import request
from urllib.parse import urlencode
from bs4 import BeautifulSoup
import json
#import process
import pandas as pd
import math
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_pdf import PdfPages


# Dictionnaire clés/valeurs adapté en fonction du site.
dictionnaire = {
    "realEstateTypes[0]":"appartement",
    "locations[0][value]":"hyeres",
    #"locations[0][label]":"Nice (06000) - Ville",
    "realEstateTypes[1]":"maison"
    
}

baseUrl = 'https://www.orpi.com/recherche/buy?'
maQuery = urlencode(dictionnaire)
url = baseUrl + maQuery
print(url)

html = request.urlopen(url)

soup = BeautifulSoup(html , 'html.parser')
test = soup.find_all("div", class_="o-container")

# cibler le json dans le html qui est dans un attribut de Div et le mettre dans un container
jsonContainer = soup.find_all("div",attrs={"data-result" : True})

# charger le json avec la library standard json et le mettre dans monJson
# jsoncontainer est un array, a cause du soup.find_all
# nous savons qu'il existe qu'un seul element, donc jsoncontainer[0] contient l'element
# le json est contenu dans la valeur de l'attribut data-result ( Le data-result est la clé de la valeur du json )
# Donc on accede a la valeur avec jsoncontainer[0][data-result]

monJson = json.loads(jsonContainer[0]["data-result"])

df = pd.DataFrame(monJson["items"])

dfAppart = df.loc[df['type'] == 'appartement']
dfAppart['pricePerSquareMeter'].mean()

dfMaison = df.loc[df['type'] == 'maison']
# ecart type
ecartType = math.sqrt(dfAppart['pricePerSquareMeter'].var())

# affichage 

print(dfAppart['pricePerSquareMeter'].describe())
print(dfMaison['pricePerSquareMeter'].describe())

nbrMaison = dfMaison['pricePerSquareMeter'].describe()
nbrAppart = dfAppart['pricePerSquareMeter'].describe()

sns.distplot(dfAppart['pricePerSquareMeter'], label = ('appart ' + str(int(nbrAppart['count']))) )
sns.distplot(dfMaison['pricePerSquareMeter'], label = ('maison ' + str(int(nbrMaison['count']))) )
plt.legend()
plt.show()


