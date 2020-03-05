import pandas as pd



def cityaFormat(ville) :
    """
    In = Nom de la ville
    Out = Nom de la ville + code postal generic format for citya
    """

    df =pd.read_csv('ressources/ville_code.csv')


    ville = 'Paris'
    ville = ville.lower()

    if df['Ville'].str.contains(Ville).any() :
        a = df.loc[df['Ville'] == ville]
        ville = a['Ville+Code'].values[0]
        ville
    else :
        print("Ville n'existe pas")
    
    return ville
        
