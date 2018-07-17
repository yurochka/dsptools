# Created on Jul. 8, 2018
# An implementation of the homonymous Matlab function.
# Prony's method for time-domain IIR filter design.
# Author: yurochka

import numpy as np
from scipy.linalg import toeplitz


def prony(h, nb, na):
    k = len(h) - 1
    if k <= max(nb, na):
        k = max(nb, na) + 1
        h = np.append(h, np.zeros(k + 1 - len(h)))
    c = h[0]
    if c == 0:
        c = 1
    H = np.mat(toeplitz(np.array(h) / c, np.append([1], np.zeros(k))))
    if k > na:
        H = H[:, 0:(na+1)]
    H1 = H[0:(nb+1), :]
    h1 = H[(nb+1):(k+1), 0]
    H2 = H[(nb+1):(k+1), 1:(na+1)]
    a = np.vstack((np.mat(1), -H2.I * h1))
    aT = a.T
    b = c * aT * H1.T
    return b.getA()[0], aT.getA()[0]
