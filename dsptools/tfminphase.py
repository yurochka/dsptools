# Created on Jun. 28, 2018
# Get a minimum-phase system with the equal frequency response to a given transfer function.
# Author: yurochka

import numpy as np
import scipy.signal as sg


def tfminphase(b, a):
    z, p, k = sg.tf2zpk(b, a)
    for i in range(len(z)):
        if np.abs(z[i]) > 1:
            k = k * z[i]
            z[i] = 1 / z[i]
    for i in range(len(p)):
        if np.abs(p[i]) > 1:
            k = k / p[i]
            p[i] = 1 / p[i]
    bn, an = sg.zpk2tf(z, p, k)
    return bn, an
