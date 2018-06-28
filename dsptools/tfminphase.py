# Created on Jun. 28, 2018
# Get a minimum-phase system with the equal frequency response to a given transfer function.
# Author: yurochka

import numpy as np
import scipy.signal as sg


def tfminphase(b, a):
    z, p, k = sg.tf2zpk(b, a)
    print(z,p,k)
    for zi in z:
        if np.abs(zi) > 1:
            k = k * zi
            zn = 1 / zi
            zi = zn
    for pi in p:
        if np.abs(pi) > 1:
            k = k / pi
            pi = 1 / pi
    bn, an = sg.zpk2tf(z, p, k)
    print(z,p,k)
    return bn, an
