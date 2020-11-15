from urllib.parse import urlencode
import requests
import pandas as pd
import numpy as np
import targetData
import getSimilar
import getTrain


url = "https://www.hemnet.se/bostad/villa-4rum-slatbaken-husbyvik-soderkopings-kommun-husaby-strand-16-17083596"

# Get the Dataframe for the target price
df = targetData.dfData(url)

# Get the train Dataset

url2 = getSimilar.getLink(url)
dfTrain = getTrain(url2)



