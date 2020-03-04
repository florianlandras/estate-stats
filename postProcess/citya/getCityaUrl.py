from urllib.parse import urlencode

def get (dictionnaire) :

    """
    In : dictionary with query words
    Out: Url string


    Base Url : https://www.citya.com/annonces/vente/

    + type separated by ","
        modificator : appartement,maison/ or appartement/ or maison/

    + locations separated by ","
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
    """

    baseUrl = "https://www.citya.com/annonces/vente/appartement,maison/"

    url = baseUrl + "?sort=b.dateMandat&direction=desc&" + dictionnaire["ville"]  #TODO Better url construction

    del dictionnaire["ville"] #Now delete key pair "ville" to encode query words
    maQuery = urlencode(dictionnaire)

    url = url + maQuery #Now add encoded Query to url

    return url



if __name__ == '__main__':
    dictionnaire = {          #TODO Need to normalize user input between each post process scrapping
        "ville":"nice-06088", #FIXME The name of the city need to be exact to be processed or other query will be ignored
        "prixMin":"0",
        "prixMax":"100000",
        "nbrePiecesMin":"0",
        "nbrePiecesMax":"10",
        "surfaceMin":"0",
        "surfaceMax":"111",      
    }
    print(get(dictionnaire))    
        
