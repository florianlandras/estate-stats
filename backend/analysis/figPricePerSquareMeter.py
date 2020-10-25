import seaborn as sns
import matplotlib.pyplot as plt

def dataFrameFig(*args):

    """
    In : DataFrame ex : dfAppart["pricePerSquareMeter"]
    out : Nothing

    This function plot figure depending on the data frame
    """

    for dataFrame in args:
        nbrOfData = dataFrame.describe() #get the DF info to get number of element
        sns.distplot(dataFrame, label = ("# of data : " + str(int(nbrOfData["count"]))))

    plt.legend()
    plt.show()
