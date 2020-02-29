from urllib import request
from bs4 import BeautifulSoup

def getDf (url):

    html = request.urlopen(url)

    soup = BeautifulSoup(html , 'html.parser')

if __name__ == '__main__':
    url ="https://www.citya.com/annonces/vente/appartement,maison/nice-06088?sort=b.dateMandat&direction=desc&prixMin=0&prixMax=100000&nbrePiecesMin=0&nbrePiecesMax=10&surfaceMin=0&surfaceMax=111"
    getDf(url)