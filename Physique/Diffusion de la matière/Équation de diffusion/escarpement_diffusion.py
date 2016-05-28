# -*- coding: utf-8 -*-

import os
import numpy as np
import matplotlib.pyplot as plt
import sympy
from sympy import init_printing
from scipy.sparse import diags

init_printing(use_latex=True)
x, t, Y1, a, K = sympy.symbols('x t Y1 a K')
y = (1 / 2.0) * Y1 * (sympy.erf((a - x) / (2 * sympy.sqrt(K * t))) +
                      sympy.erf((a + x) / (2 * sympy.sqrt(K * t))))
print(y)

from sympy.utilities.lambdify import lambdify
f = lambdify((x, t, Y1, a, K), y)  # function for analytic solution

dt = 2.5  # time step (years)
dy = 0.1  # grid size for space (m)
D = 50E-4  # diffusion coefficient in m2/yr - e.g., Fernandes and Dietrich, 1997
h = 10  # height of fault scarp in m
y_max = 20  # length of domain in m
t_max = 500  # total time in years
y = np.arange(0, y_max + dy, dy)
ny = len(y)
nt = int(t_max / dt)
V = np.zeros((ny,))  # initial condition
V[:round(ny / 2.0)] = h  # initial condition


def diffusion_Crank_Nicolson(dy, ny, dt, nt, D, V, ntout):
    Vout = []  # list for storing V arrays at certain time steps
    V0 = V[0]  # boundary condition on left side
    V1 = V[-1]  # boundary condition on right side
    s = D * dt / dy**2  # diffusion number
    A = diags([-0.5 * s, 1 + s, -0.5 * s], [-1, 0, 1],
              shape=(ny - 2, ny - 2)).toarray()  # create coefficient matrix
    B1 = diags([0.5 * s, 1 - s, 0.5 * s], [-1, 0, 1],
               shape=(ny - 2, ny - 2)).toarray()
    for n in range(1, nt):  # time is going from second time step to last
        Vn = V
        B = np.dot(Vn[1:-1], B1)
        B[0] = B[0] + 0.5 * s * (V0 + V0)
        B[-1] = B[-1] + 0.5 * s * (V1 + V1)
        V[1:-1] = np.linalg.solve(A, B)
        if n % int(nt / float(ntout)) == 0 or n == nt - 1:
            # numpy arrays are mutable, so we need to write out a copy of V,
            # not V itself
            Vout.append(V.copy())
    return Vout, s

Vout, s = diffusion_Crank_Nicolson(dy, ny, dt, nt, D, V, 20)

plt.figure(figsize=(10, 5.2))
for V in Vout:
    plt.plot(y, V, 'gray')

plt.xlabel('distance (m)', fontsize=12)
plt.ylabel('height (m)', fontsize=12)
plt.axis([0, y_max, 0, 10])
plt.title('fault scarp diffusion', fontsize=14)
plt.plot(y, np.asarray([f(x0, t_max, h, y_max / 2.0, D)
                        for x0 in y]), 'r--', linewidth=2)

dt = 2.5  # time step (years)
dy = 0.1  # grid size for space (m)
D = 50E-4  # diffusion coefficient in m2/yr - e.g., Fernandes and Dietrich, 1997
h = 10  # height of fault scarp in m
y_max = 20  # length of domain in m
t_max = 5000  # total time in years
y = np.arange(0, y_max + dy, dy)
ny = len(y)
nt = int(t_max / dt)
V = np.zeros((ny,))  # initial condition
V[:round(ny / 2.0)] = h  # initial condition

Vout, s = diffusion_Crank_Nicolson(dy, ny, dt, nt, D, V, 20)

plt.figure(figsize=(10, 5.2))
for V in Vout:
    plt.plot(y, V, 'gray')

plt.xlabel('distance (m)', fontsize=12)
plt.ylabel('height (m)', fontsize=12)
plt.axis([0, y_max, 0, 10])
plt.title('fault scarp diffusion', fontsize=14)
plt.plot(y, np.asarray([f(x0, t_max, h, y_max / 2.0, D)
                        for x0 in y]), 'r--', linewidth=2)

dt = 2.5  # time step (years)
dy = 0.1  # grid size for space (m)
D = 50E-4  # diffusion coefficient in m2/yr - e.g., Fernandes and Dietrich, 1997
h = 10  # height of fault scarp in m
y_max = 40  # length of domain in m
t_max = 5000  # total time in years
y = np.arange(0, y_max + dy, dy)
ny = len(y)
nt = int(t_max / dt)
V = np.zeros((ny,))  # initial condition
V[:round(ny / 2.0)] = h  # initial condition

Vout, s = diffusion_Crank_Nicolson(dy, ny, dt, nt, D, V, 20)

plt.figure(figsize=(10, 5.2))
for V in Vout:
    plt.plot(y, V, 'gray')

plt.xlabel('distance (m)', fontsize=12)
plt.ylabel('height (m)', fontsize=12)
plt.axis([0, y_max, 0, 10])
plt.title('fault scarp diffusion', fontsize=14)
plt.plot(y, np.asarray([f(x0, t_max, h, y_max / 2.0, D)
                        for x0 in y]), 'r--', linewidth=2)

os.system("pause")
