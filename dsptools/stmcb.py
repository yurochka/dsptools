# Created on Jul. 12, 2018
# An implementation of the homonymous Matlab function
# Find the coefficients of IIR system with impulse response approximately
# Author: yurochka


import numpy as np
import scipy.signal as sg
from .convmtx import convmtx
from .prony import prony


def stmcb(h, nb, na, niter=5, ain=None):
    if ain is None:
        ain, _ = prony(h, 0, na)
    uin = np.zeros_like(h)
    uin[0] = 1
    a = ain
    N = len(h)
    for i in range(niter):
        u = sg.lfilter([1], a, h)
        v = sg.lfilter([1], a, uin)
        C1 = np.mat(convmtx(u, na + 1)).T
        C2 = np.mat(convmtx(v, nb + 1)).T
        T = np.hstack((-C1[0:N, :], C2[0:N, :]))
        c = (T[:, 1:(nb + na + 2)]).I * (-T[:, 0])
        a = np.vstack((np.mat(1), c[0:na, 0]))
        b = c[na:(nb + na + 1), 0]
        a = a.T.getA()[0]
    b = b.T.getA()[0]
    return b, a
