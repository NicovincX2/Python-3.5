# -*- coding: utf-8 -*-

import os
import matplotlib as mpl
mpl.rcParams["font.family"] = "serif"
mpl.rcParams["font.size"] = "12"
import numpy as np
from numpy import polynomial as P
from scipy import interpolate
import matplotlib.pyplot as plt
from scipy import linalg


def runge(x):
    return 1 / (1 + 25 * x**2)

    def runge_interpolate(n):
        x = np.linspace(-1, 1, n + 1)
        p = P.Polynomial.fit(x, runge(x), deg=n)
        return x, p

xx = np.linspace(-1, 1, 250)

fig, ax = plt.subplots(1, 1, figsize=(8, 4))

ax.plot(xx, runge(xx), 'k', lw=2, label="Runge's function")

n = 13
x, p = runge_interpolate(n)
ax.plot(x, runge(x), 'ro')
ax.plot(xx, p(xx), 'r', label='interp. order %d' % n)

n = 14
x, p = runge_interpolate(n)
ax.plot(x, runge(x), 'go')
ax.plot(xx, p(xx), 'g', label='interp. order %d' % n)

ax.legend(loc=8)
ax.set_xlim(-1.1, 1.1)
ax.set_ylim(-1, 2)
ax.set_xticks([-1, -0.5, 0, 0.5, 1])
ax.set_ylabel(r"$y$", fontsize=18)
ax.set_xlabel(r"$x$", fontsize=18)

fig.tight_layout()
fig.savefig('ch7-polynomial-interpolation-runge.pdf')

os.system("pause")
