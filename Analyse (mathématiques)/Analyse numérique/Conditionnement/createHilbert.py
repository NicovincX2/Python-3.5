# -*- coding: utf-8 -*-

"""
    This module creates the Hilbert matrix system.
    Marina von Steinkirch, spring 2013.
"""

import numpy as npy
import os


def createHilbert(N):

    # generating H^N
    H = npy.zeros((N, N), dtype=npy.float64)

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            Hij = 1.0 / (i + j - 1.0)
            H[i - 1, j - 1] = Hij

    # generating x^n
    xt = npy.zeros((N), dtype=npy.float64)

    for i in range(0, N):
        xt[i] = i

    x = npy.transpose(xt)

    return H, x

os.system("pause")
