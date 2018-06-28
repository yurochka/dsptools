# Created on Jun. 28, 2018
# An implementation of the homonymous Matlab function.
# Author: yurochka

import numpy as np


def polystab(a):
    if len(a) <= 1:
        return a
    else:
        v = np.roots(a)
        for i in range(len(v)):
            if v[i] != 0:
                vs = 0.5 * (np.sign(abs(v[i]) - 1) + 1)
                v[i] = (1 - vs) * v[i] + vs / v[i].conj()
        ind = np.nonzero(v)
        b = a[ind[0][0]] * np.poly(v)
        if np.iscomplex(b).any():
            b = np.real(b)
        return b
