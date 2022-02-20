import numpy as np
import pandas as pd

lowCase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upCase = list(map(lambda data: data.upper(), lowCase))

dataSize = 100
lenData = 10
heightData = int(dataSize/lenData)

def resizeData(arr,magnitude):
    newarr = []
    for i in range(magnitude):
        newarr.append(arr[i])
    return newarr

lowCase = resizeData(lowCase,lenData)
upCase = resizeData(upCase,heightData)

dataframe = pd.DataFrame(np.arange(0,dataSize).reshape(lenData,heightData),lowCase,upCase)

if __name__ == '__main__':
    print(dataframe)