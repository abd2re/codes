from DataFrameTable import *

#print(dataframe.loc['a','A'])
#print(dataframe.loc['a','B'])
#print(dataframe.loc['b','A'])
#print(dataframe.loc['b','B'])

db = np.array([])

for i in range(len(dataframe.columns)):
    for j in range(len(dataframe.index)):
        db = np.append(db,dataframe.iloc[i,j]+1)

pdb = db.copy()
pdb = pdb[pdb%2==0]

#print(db.reshape(10,10))
#print(pdb.reshape(10,5))

print(dataframe[dataframe%2==0])

