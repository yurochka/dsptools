# Created on Jul. 14, 2018
# Fit given frequency response to an IIR filter
# Using impulse response method


from .stmcb import stmcb
from .tfminphase import tfminphase
import numpy as np
import scipy.signal as sg


# h - frequency response
# nb - numerator order
# na - denominator order
# worN - impulse response length
# hilb - Hilbert transfrom flag
def fitiir(h, nb, na, worN=400, hilb=True):
    if worN > len(h) * 2:
        worN = len(h) * 2
    if hilb:
        mag = np.log(np.abs(h))
        mag_ext = np.append(mag[::-1], mag[1:])
        hilb = sg.hilbert(mag_ext)
        phase = -np.imag(hilb[(len(mag) - 1):])
        h_new = np.exp(mag + 1j * phase)
    else:
        h_new = h
    h_fft = np.append(h_new, np.conj(h_new[::-1]))
    y = np.fft.ifft(h_fft)
    b0, a0 = stmcb(np.real(y[0:worN]), nb, na)
    b, a = tfminphase(b0, a0)
    return b, a
