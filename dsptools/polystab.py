# Created on Jun. 28, 2018
# An implementation of the homonymous Matlab function.

import numpy as np


def polystab(a):
    if len(a) <= 1:
        return a
    else:
        v = np.roots(a)
        for vi in v:
            if vi != 0:
                vs = 0.5 * (np.sign(abs(vi) - 1) + 1)
                vi = (1 - vs) * vi + vs / vi.conj()
        ind = np.nonzero(v)
        b = a[ind[0][0]] * np.poly(v)
        if np.iscomplex(b).any():
            b = np.real(b)
        return b
