#import process
import pandas as pd
import math

# import our fonctions
from postProcess.getOrpi import dataJson
from analysis.figPricePerSquareMeter import dataFrameFig

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
dataFrameFig(dfAppart['pricePerSquareMeter'], dfMaison['pricePerSquareMeter'])
