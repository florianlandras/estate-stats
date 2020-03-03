import pandas as pd
import math

def jsonToDf(orpiJson):
    """
    In : Json["items"] from orpi page
    out : DataFrame of that Json
    """
    #Need to do some cleaning here with cleanData.py

    return pd.DataFrame(orpiJson)