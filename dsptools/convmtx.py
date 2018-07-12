# Created on Jul. 12, 2018
# An implementation of the homonymous Matlab function
# Author: yurochka


import numpy as np

# a - array-like
# n - integer
def convmtx(a, n):
    l = len(a)
    m = np.zeros((n, l + n - 1))
    for i in range(n):
        m[i][i:(i + l)] = a
    return m
