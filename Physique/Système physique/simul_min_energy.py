# -*- coding: utf-8 -*-

import os
import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['savefig.dpi'] = matplotlib.rcParams['figure.dpi'] = 144

g = 9.81  # gravity of Earth
m = .1  # mass, in kg
n = 20  # number of masses
e = .1  # initial distance between the masses
l = e  # relaxed length of the springs
k = 10000  # spring stiffness

P0 = np.zeros((n, 2))
P0[:, 0] = np.repeat(e * np.arange(n // 2), 2)
P0[:, 1] = np.tile((0, -e), n // 2)

A = np.eye(n, n, 1) + np.eye(n, n, 2)

L = l * (np.eye(n, n, 1) + np.eye(n, n, 2))
for i in range(n // 2 - 1):
    L[2 * i + 1, 2 * i + 2] *= np.sqrt(2)

I, J = np.nonzero(A)

dist = lambda P: np.sqrt((P[:, 0] - P[:, 0][:, np.newaxis])**2 +
                         (P[:, 1] - P[:, 1][:, np.newaxis])**2)


def spring_color_map(c):
    min_c, max_c = -0.00635369422326, 0.00836362559722
    ratio = (max_c - c) / (max_c - min_c)
    color = plt.cm.coolwarm(ratio)
    shading = np.sqrt(abs(ratio - 0.5) * 2)
    return (shading * color[0], shading * color[1], shading * color[2], color[3])


def show_bar(P):
    plt.figure(figsize=(5, 4))
    # Wall.
    plt.axvline(0, color='k', lw=3)
    # Distance matrix.
    D = dist(P)
    # We plot the springs.
    for i, j in zip(I, J):
        # The color depends on the spring tension, which
        # is proportional to the spring elongation.
        c = D[i, j] - L[i, j]
        plt.plot(P[[i, j], 0], P[[i, j], 1],
                 lw=2, color=spring_color_map(c))
    # We plot the masses.
    plt.plot(P[[I, J], 0], P[[I, J], 1], 'ok',)
    # We configure the axes.
    plt.axis('equal')
    plt.xlim(P[:, 0].min() - e / 2, P[:, 0].max() + e / 2)
    plt.ylim(P[:, 1].min() - e / 2, P[:, 1].max() + e / 2)
    plt.xticks([])
    plt.yticks([])

show_bar(P0)
plt.title("Initial configuration")


def energy(P):
    # The argument P is a vector (flattened matrix).
    # We convert it to a matrix here.
    P = P.reshape((-1, 2))
    # We compute the distance matrix.
    D = dist(P)
    # The potential energy is the sum of the
    # gravitational and elastic potential energies.
    return (g * m * P[:, 1].sum() +
            .5 * (k * A * (D - L)**2).sum())

energy(P0.ravel())
bounds = np.c_[P0[:2, :].ravel(), P0[:2, :].ravel()].tolist() + \
    [[None, None]] * (2 * (n - 2))

P1 = opt.minimize(energy, P0.ravel(),
                  method='L-BFGS-B',
                  bounds=bounds).x.reshape((-1, 2))

show_bar(P1)
plt.title("Equilibrium configuration")

os.system("pause")
