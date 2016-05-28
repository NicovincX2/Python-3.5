# -*- coding: utf-8 -*-

import os

import numpy as np

# example from scipy.org NumPy tutorial


def f(x, y):
    return 10 * x + y

a = np.fromfunction(f, (5, 4), dtype=int)

print(a)

print(a[0:2, 0:2])

print(a[:, 1])

print(a.flatten())


for row in a:   # iteration is done over fiest axis
    print(row)


for element in a.flat:
    print(element)

os.system("pause")
