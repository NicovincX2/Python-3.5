# -*- coding: utf-8 -*-

import os
from numpy import *
from numpy.linalg import eigh
from math import *
from matplotlib.pyplot import *


def Laplacian(x):
    h = x[1] - x[0]  # assume uniformly spaced points
    n = len(x)
    M = -2 * identity(n, 'd')
    for i in range(1, n):
        M[i, i - 1] = M[i - 1, i] = 1
    return M / h**2

x = linspace(-3, 3)
m = 1.0
ohm = 1.0
T = (-0.5 / m) * Laplacian(x)
V = 0.5 * (ohm**2) * (x**2)
H = T + diag(V)
E, U = eigh(H)
h = x[1] - x[0]

# Plot the Harmonic potential
plot(x, V, color='k')

for i in range(4):
    # For each of the first few solutions, plot the energy level:
    axhline(y=E[i], color='k', ls=":")
    # as well as the eigenfunction, displaced by the energy level so they don't
    # all pile up on each other:
    plot(x, -U[:, i] / sqrt(h) + E[i])
title("Eigenfunctions of the Quantum Harmonic Oscillator")
xlabel("Displacement (bohr)")
ylabel("Energy (hartree)")

os.system("pause")
