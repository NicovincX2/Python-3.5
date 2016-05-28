# -*- coding: utf-8 -*-

import os
import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return 0.5 - np.exp(-x)

x = np.linspace(0, 4, 100)
y = f(x)
plt.plot(x, y)
plt.axhline(0, color='r', ls='--')


def bisection(func, x1, x2, tol=1e-3, nmax=10):
    f1 = func(x1)
    f2 = func(x2)
    assert f1 * f2 < 0, 'Error: zero not in interval x1-x2'
    for i in range(nmax):
        xm = 0.5 * (x1 + x2)
        fm = func(xm)
        if fm * f2 < 0:
            x1 = xm
            f1 = fm
        else:
            x2 = xm
            f2 = fm
        print(x1, x2, f1, f2)
        if abs(x1 - x2) < tol:
            return x1
    print('Maximum number of iterations reached')
    return x1

xzero = bisection(f, 0, 4, nmax=20)
print('zero of function and function value: ', xzero, f(xzero))

xzero = bisection(np.cos, 0, 3, tol=1e-6, nmax=30)
print('cos(x) is zero between 0 and pi at:', xzero)
print('relative error:', (xzero - np.pi / 2) / (np.pi / 2))

os.system("pause")
