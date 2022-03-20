import pandas as pd
import numpy as np
import string

l = list(string.ascii_uppercase)

a = 7
b = 6
nb = 2
a,sym = l[0:a],[]

for i in range(len(a)):
    for j in range(b):
        x = a[i] + str(j+nb)
        sym.append(x)

sym = np.array(sym).reshape(len(a),b).transpose()
df = pd.DataFrame(sym,index=np.arange(nb,nb+b),columns=a)

print(df)


