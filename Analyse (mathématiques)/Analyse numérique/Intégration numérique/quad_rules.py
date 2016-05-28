# -*- coding: utf-8 -*-

import os
import matplotlib.pyplot as plt
import numpy as np
import sympy
from numpy import polynomial
from scipy import integrate
from scipy import interpolate

a = 0
b = 1.0


def f(x):
    return np.exp(-x**2)

a = 0.0
b = 1.0


def f(x):
    return 3 + x + x**2 + x**3 + x**4

x = np.linspace(a, b, 100)
xx = np.linspace(a - 0.2, b + 0.2, 100)

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(16, 4))

npoints = 2
npoints = 5

X = np.linspace(a, b, npoints)

ax1.plot(xx, f(xx), lw=1, color='k')
ax1.fill_between(x, f(x), color='lightgreen', alpha=0.9)

for n in range(len(X) - 1):
    f_mid = f(X[n:n + 2].mean())
    ax1.plot([X[n], X[n]], [0, f_mid], 'b')
    ax1.plot([X[n + 1], X[n + 1]], [0, f_mid], 'b')
    ax1.plot(X[n:n + 2], [f_mid] * 2, 'b')
    ax1.plot(X[n:n + 2].mean(), f_mid, 'xk')

i = (b - a) * f_mid
#ax1.text(-1, 7, r'$\int_{-1}^{\,1} f(x)dx \approx %f$' % i, fontsize=18)
ax1.plot(X, f(X), 'ro')
ax1.set_xlim(xx.min(), xx.max())
ax1.set_title('Mid-point rule')
ax1.set_xticks([-1, 0, 1])
ax1.set_xlabel(r'$x$', fontsize=18)
ax1.set_ylabel(r'$f(x)$', fontsize=18)

names = ["Trapezoid rule", "Simpson's rule"]
for idx, ax in enumerate([ax2, ax3]):
    ax.plot(xx, f(xx), lw=1, color='k')
    ax.fill_between(x, f(x), color='lightgreen', alpha=0.9)

    i = 0
    for n in range(len(X) - 1):
        XX = np.linspace(X[n], X[n + 1], idx + 2)

        f_interp = polynomial.Polynomial.fit(XX, f(XX), len(XX) - 1)
        ax.plot([X[n], X[n]], [0, f(X[n])], 'b')
        ax.plot([X[n + 1], X[n + 1]], [0, f(X[n + 1])], 'b')
        XXX = np.linspace(X[n], X[n + 1], 50)
        ax.plot(XXX, f_interp(XXX), 'b')

        F = f_interp.integ()
        i += F(X[n + 1]) - F(X[n])
    ax.text(-1, 0.5, r'$\int_a^{\,b} f(x)dx \approx %f$' % i, fontsize=18)
    ax.plot(X, f(X), 'ro')
    ax.set_xlabel(r'$x$', fontsize=18)
    ax.set_ylabel(r'$f(x)$', fontsize=18)
    ax.set_xlim(xx.min(), xx.max())
    ax.set_title(names[idx])
    ax.set_xticks([-1, 0, 1])

fig.tight_layout()
fig.savefig('ch8-quadrature-rules-%d.pdf' % npoints)


os.system("pause")
