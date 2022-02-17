import numpy as np
import math as m

arr = np.arange(0,101)
arr2 = np.arange(0,101,2)
arr3 = np.array([173,147,140,163,146,161])
arr4 = np.array([21,50,62,85,90])


def mean(lst):
    return np.sum(lst)/lst.shape

def st_deviation(lst):
    n = np.array([])
    for i in lst:
        n = np.append(n,(i-mean(lst))**2)

    return m.sqrt(np.sum(n)/lst.shape)

print(st_deviation(arr))
print(st_deviation(arr2))
print(st_deviation(arr3))
print(st_deviation(arr4))




