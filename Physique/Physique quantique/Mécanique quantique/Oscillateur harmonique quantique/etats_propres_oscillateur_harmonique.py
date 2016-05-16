# -*- coding: utf-8 -*-

import os

"""

Travail de Pierre Chary (PC, ENCPB-Lycée Pierre Gilles de Gennes, Paris) pour 
représenter les fonctions d'ondes correspondant aux premiers états propres de 
l'oscillateur harmonique quantique.

"""


from math import factorial, pi, sqrt
import numpy
from numpy.polynomial.hermite import hermval
import matplotlib.pyplot as plt

# Mettre la variable suivante à 'None' pour affichage via plt.show()
out_file = 'PNG/S06_etats_propres_oscillateur_harmonique.png' 

n_states = 6
states = range(n_states)
energylevels = [s + 0.5 for s in states]
x_max = sqrt(2*n_states + 1) + 1.5
xs = numpy.linspace(-x_max,x_max,200)
ys = xs**2 / 2

def psi(n,xs):
    return 0.4*sqrt(1./(2**n * factorial(n)) * sqrt(pi)) \
           * numpy.exp(-xs**2/2) \
           * hermval(xs,[0]*n+[1])

plt.figure(figsize=(7,5))
plt.plot(xs, ys, linewidth=2)
plt.xticks(range(-int(x_max) + 1, int(x_max)),
           ["$%d$" % (i) for i in range(-int(x_max) + 1, int(x_max))])
plt.yticks(energylevels, ["$%d/2$" % (2*s + 1) for s in states])
plt.hlines(energylevels, -x_max, x_max, linestyles='dashed')

for state in states:
    plt.plot(xs, psi(state, xs) + state + 0.5, linewidth=2)

plt.title("%d premiers etats propres d'energie pour l'OH quantique" % (n_states))
plt.xlabel('$x$')
plt.ylabel('$\psi_n(x),\ E_n$', fontsize=14)
plt.xlim([-x_max,x_max])
plt.ylim([0, max(energylevels) + 1])
if out_file: plt.savefig(out_file)
else :       plt.show()

os.system("pause")