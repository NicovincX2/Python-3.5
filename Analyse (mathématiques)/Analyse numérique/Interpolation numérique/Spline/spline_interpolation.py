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

x = np.linspace(-1, 1, 11)

y = runge(x)

f = interpolate.interp1d(x, y, kind=3)

xx = np.linspace(-1, 1, 100)

fig, ax = plt.subplots(figsize=(8, 4))

ax.plot(xx, runge(xx), 'k', lw=1, label="Runge's function")
ax.plot(x, y, 'ro', label='sample points')
ax.plot(xx, f(xx), 'r--', lw=2, label='spline order 3')

ax.legend()
ax.set_ylim(0, 1.1)
ax.set_xticks([-1, -0.5, 0, 0.5, 1])
ax.set_ylabel(r"$y$", fontsize=18)
ax.set_xlabel(r"$x$", fontsize=18)

fig.tight_layout()
fig.savefig('ch7-spline-interpolation-runge.pdf')

x = np.array([0, 1, 2, 3, 4, 5, 6, 7])

y = np.array([3, 4, 3.5, 2, 1, 1.5, 1.25, 0.9])

xx = np.linspace(x.min(), x.max(), 100)

fig, ax = plt.subplots(figsize=(8, 4))

ax.scatter(x, y)

for n in [1, 2, 3, 6]:
    f = interpolate.interp1d(x, y, kind=n)
    ax.plot(xx, f(xx), label='order %d' % n)

ax.legend()
ax.set_ylabel(r"$y$", fontsize=18)
ax.set_xlabel(r"$x$", fontsize=18)

fig.tight_layout()
fig.savefig('ch7-spline-interpolation-orders.pdf')

os.system("pause")
