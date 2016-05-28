# -*- coding: utf-8 -*-

import os

'''
Illustration du phénomène de propagation vers la droite d'une onde de forme 
quelconque à la fois au cours du temps dans un profil spatial, et spatialement 
dans un profil temporel.
'''

import numpy as np               # Pour np.linspace, np.exp et np.cos
import matplotlib.pyplot as plt  # Pour les dessins


def f(u, k=10):
    '''Le profil de l'onde à propager: une gaussienne multipliée par un cosinus.'''
    return np.exp(-3 * u**2) * np.cos(k * u - 5)

nb_points = 1000   # Le nombre de points d'échantillonnage du graphe
nb_courbes = 3      # Le nombre de courbes à représenter

# Tout d'abord la visualisation spatiale

x = np.linspace(-2, 2, nb_points)   # Echantillonnage en position
t = np.linspace(0, 5, nb_courbes)  # On regarde le profil à différents temps
c = 0.2  # Vitesse de propagation de l'onde

for ti in t:
    fi = f(x - c * ti)  # Echantillonnage du profil pour les différents x
    plt.plot(x, fi, label='$t={}$'.format(round(ti, 1)))  # Affichage

# La cosmétique

plt.title('Profil spatial pour differents temps')
plt.xlabel('Position $x$')
plt.ylabel("Profil de l'onde")
plt.legend()
plt.savefig('PNG/S02_onde_progressive_spatial.png')
plt.clf()

# Tout d'abord la visualisation spatiale

t = np.linspace(0, 10, nb_points)  # Echantillonnage en temps
# On regarde le profil à différentes positions
x = np.linspace(0, 0.6, nb_courbes)
c = 0.2  # Vitesse de propagation de l'onde

for xi in x:
    fi = f(xi - c * t)  # Echantillonnage du profil pour les différents t
    plt.plot(t, fi, label='$x={}$'.format(round(xi, 1)))  # Affichage

# La cosmétique

plt.title('Profil temporel pour differente positions')
plt.xlabel('Temps $t$')
plt.ylabel("Profil de l'onde")
plt.legend()
plt.savefig('PNG/S02_onde_progressive_temporel.png')
plt.clf()

os.system("pause")
