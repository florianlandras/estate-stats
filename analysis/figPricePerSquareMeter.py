import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

def DataFrameFig(*args):

    """
    In : DataFrame ex : dfAppart["pricePerSquareMeter"]
    out : Nothing

    This function plot figure depending on the data frame
    """

    for dataFrame in args:
        nbrOfData = dataFrame.describe()
        sns.distplot(dataFrame, label = ("# of data : " + str(int(nbrOfData["count"]))))

    plt.legend()
    plt.show()
