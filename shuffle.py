from pandas import DataFrame
from DataFrameTable import *

values = dataframe.values.ravel()
ranarr = np.array([])

for i in range(values.size):
    n = np.random.choice(values)
    ranarr = np.append(ranarr,n)
    values = values[values != n]

ranarr = ranarr.reshape(10,10)
rantable = pd.DataFrame(ranarr)

print(rantable)


