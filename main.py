#import process
import math

# import our fonctions
from postProcess.getOrpi import dataJson
from process.processOrpi import jsonToDf
from analysis.figPricePerSquareMeter import dataFrameFig


# Orpi informations ------------------------

# Dictionnaire clés/valeurs adapté en fonction du site.
# TODO normalize user input in a dictionary
dictionnaire = {
    "realEstateTypes[0]":"appartement",
    "locations[0][value]":"hyeres",
    #"locations[0][label]":"Nice (06000) - Ville",
    "realEstateTypes[1]":"maison"
    
}
#-----------------------------------

#Post process Orpi------------------
monJson = dataJson(dictionnaire)
#-----------------------------------


#Process Orpi-----------------------
df = jsonToDf(monJson["items"])

dfAppart = df.loc[df['type'] == 'appartement']
dfAppart['pricePerSquareMeter'].mean()

dfMaison = df.loc[df['type'] == 'maison']
# ecart type
ecartType = math.sqrt(dfAppart['pricePerSquareMeter'].var())
#-----------------------------------


#Analysis Orpi----------------------
# affichage 
dataFrameFig(dfAppart['pricePerSquareMeter'], dfMaison['pricePerSquareMeter'])
#-----------------------------------