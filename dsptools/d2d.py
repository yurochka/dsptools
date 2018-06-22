# Created on Jun. 22, 2018
# An implementation of the homonymous Matlab function, using Bilinear transform
# Author: yurochka

from numpy.polynomial.polynomial import polyadd, polymul, polypow


def d2d(b, a, T):
    nb = len(b)
    na = len(a)
    b_new = _polytustin(b, T)
    a_new = _polytustin(a, T)
    if nb > na:
        a_new = polymul(a_new, polypow([1, (T-1)/(T+1)], nb - na))
    elif na > nb:
        b_new = polymul(b_new, polypow([1, (T-1)/(T+1)], na - nb))
    return b_new / a_new[0], a_new / a_new[0]


def _polytustin(a, T):
    n = len(a)
    a_new = 0
    num = [(T-1)/(T+1), 1]
    den = [1, (T-1)/(T+1)]
    for i in range(n):
        pnum = polypow(num, i)
        pden = polypow(den, n-1-i)
        a_new = polyadd(a_new, a[i] * polymul(pnum, pden))
    return a_new
