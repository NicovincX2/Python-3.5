# -*- coding: utf-8 -*-

import os
import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(6, 3))
plt.plot([0, 2], [1, 1], 'k')
plt.plot([1, 1], [0, 1], 'k')
plt.plot([0, 1, 2, 1], [1, 1, 1, 0], 'ko', markersize=10)
plt.text(1.1, 0.1, 'T[n,j]')
plt.text(0.1, 1.1, 'T[n+1,j-1]')
plt.text(1.1, 1.1, 'T[n+1,j]')
plt.text(2.1, 1.1, 'T[n+1,j+1]')
plt.xlabel('space')
plt.ylabel('time')
plt.axis('equal')
plt.yticks([0.0, 1.0], [])
plt.xticks([0.0, 1.0], [])
plt.title('Laasonen scheme', fontsize=12)
plt.axis([-0.5, 2.5, -0.5, 1.5])

plt.figure(figsize=(6, 3))
plt.plot([0, 4, 4, 0], [0, 0, 1, 1], 'k')
for i in range(0, 4):
    plt.plot([i, i], [0, 1], 'k')
plt.plot([0, 1, 2, 3, 4, 0, 4], [0, 0, 0, 0, 0, 1, 1], 'ko', markersize=10)
plt.plot([1, 2, 3], [1, 1, 1], 'ro', markersize=10)
for i in range(0, 5):
    plt.text(i + 0.1, 0.1, 'T[0,' + str(i) + ']')
    plt.text(i + 0.1, 1.1, 'T[1,' + str(i) + ']')
plt.xlabel('space')
plt.ylabel('time')
plt.axis('equal')
plt.yticks([0.0, 1.0], ['0', '1'])
plt.title('first two time steps on a 1D grid of five points', fontsize=12)
plt.axis([-0.5, 4.8, -0.5, 1.5])

from scipy.sparse import diags


def diffusion_Laasonen(dt, dy, t_max, y_max, viscosity, V0, V1):
    s = viscosity * dt / dy**2  # diffusion number
    y = np.arange(0, y_max + dy, dy)
    t = np.arange(0, t_max + dt, dt)
    nt = len(t)  # number of time steps
    ny = len(y)  # number of dy steps
    V = np.zeros((ny,))  # initial condition
    V[0] = V0  # boundary condition on left side
    V[-1] = V1  # boundary condition on right side
    A = diags([-s, 1 + 2 * s, -s], [-1, 0, 1], shape=(ny - 2, ny - 2)
              ).toarray()  # create coefficient matrix
    for n in range(nt):  # time is going from second time step to last
        Vn = V  # .copy()
        B = Vn[1:-1]  # create matrix of knowns on the RHS of the equation
        B[0] = B[0] + s * V0
        B[-1] = B[-1] + s * V1
        V[1:-1] = np.linalg.solve(A, B)  # solve the equation using numpy
    return y, t, V, s

dt = 0.01  # grid size for time (s)
dy = 0.0005  # grid size for space (m)
viscosity = 2 * 10**(-4)  # kinematic viscosity of oil (m2/s)
y_max = 0.04  # in m
V0 = 10.0  # velocity in m/s
V1 = 0.0  # velocity in m/s

plt.figure(figsize=(7, 5))
for time in np.linspace(0, 1.0, 10):
    y, t, V, s = diffusion_Laasonen(dt, dy, time, y_max, viscosity, V0, V1)
    plt.plot(y, V, 'k')
plt.xlabel('distance from wall (m)', fontsize=12)
plt.ylabel('velocity (m/s)', fontsize=12)
plt.axis([0, y_max, 0, V0])
plt.title('Laasonen implicit scheme', fontsize=14)

dt = 0.01  # grid size for time (s)
dy = 0.0005  # grid size for space (m)
viscosity = 2 * 10**(-4)  # kinematic viscosity of oil (m2/s)
y_max = 0.04  # in m
V0 = 10.0  # velocity in m/s
V1 = 5.0  # velocity in m/s

plt.figure(figsize=(7, 5))
for time in np.linspace(0, 1.0, 10):
    y, t, V, s = diffusion_Laasonen(dt, dy, time, y_max, viscosity, V0, V1)
    plt.plot(y, V, 'k')
plt.xlabel('distance from wall (m)', fontsize=12)
plt.ylabel('velocity (m/s)', fontsize=12)
plt.axis([0, y_max, 0, V0])
plt.title('Laasonen implicit scheme', fontsize=14)

os.system("pause")
