import pandas as pd
import numpy as np
from DataFrameTable import *

groups = 4
number = 5

def split(g,n):
    indx = np.arange(n)+1
    multdx = np.arange(g)+1
    for i in range(n):
        indx[i] = int(indx[i])
    newindx = np.array([])
    newmultdx = np.array([])
    for i in range(g):
        newindx = np.append(newindx,indx)
    for i in range(n):
        newmultdx = np.append(newmultdx,multdx)
    newmultdx.sort()
    return list(zip(newmultdx.astype(int),newindx.astype(int)))

n = split(groups,number)

def multitable(arr,g,n):
    arr = pd.MultiIndex.from_tuples(arr)
    df = pd.DataFrame(np.arange(1,g*n*10+1).reshape(g*n,10),index=arr,columns=np.arange(1,10+1))
    return df

r = multitable(n,groups,number)
print(r)





