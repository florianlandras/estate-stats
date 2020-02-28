
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

# import our fonctions
from postProcess.getOrpi import dataJson

# Orpi informations ------------------------

# Dictionnaire clés/valeurs adapté en fonction du site.
dictionnaire = {
    "realEstateTypes[0]":"appartement",
    "locations[0][value]":"hyeres",
    #"locations[0][label]":"Nice (06000) - Ville",
    "realEstateTypes[1]":"maison"
    
}
#-----------------------------------

monJson = dataJson(dictionnaire)

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
