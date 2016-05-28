# -*- coding: utf-8 -*-

"""
Spyder Editor

This temporary script file is located here:
/home/greg/.spyder2/.temp.py
"""

import os
import numpy as np
from scipy.special import gamma
from scipy.linalg import solve


def ufdwt(pts, order):
    """ Compute the uniform finite difference weights """

    n = 2 * pts - 1
    A = np.tile(np.arange(pts), (n, 1)).T
    B = np.tile(np.arange(1 - pts, pts), (pts, 1))
    M = (B**A) / gamma(A + 1)
    r = np.zeros(pts)
    r[order] = 1            # determines which order derivative to approximate
    D = np.zeros((pts, pts))

    for k in xrange(pts):
        dex = k + np.arange(pts)
        D[:, k] = solve(M[:, dex], r)

    return np.flipud(D)

if __name__ == '__main__':

    pts = 3
    order = 1

    D = ufdwt(pts, order)

    print(D)

os.system("pause")
