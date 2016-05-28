# -*- coding: utf-8 -*-

import os
from functools import reduce


def flaviusPyth2(nSinistre, nbPers):
    """Version directement pythonesque du problème de Flavius"""
    surv = ["No " + str(k) for k in range(1, nbPers + 1)]
    noVictime = 0
    while len(surv) > 1:
        noVictime = (noVictime + nSinistre - 1) % len(surv)
        print(surv.pop(noVictime))
    return("Et le survivant est le " + surv[0])


def flaviusPyth(nSinistre, nbPers):
    vivant, mort = 1, 0
    cercle = [vivant] * nbPers
    noVictime = 0
    for nbVictimes in range(nbPers):
        avance = 0
        while avance < 7:
            noVictime = (noVictime + 1) % nbPers
            avance += cercle[noVictime]
        cercle[noVictime] = mort
        print(noVictime)
    print("Et le survivant est le No " + str(noVictime))


def flaviusPyth3(nSinistre, nbPers):
    """ Par pliage, avec X = (surv,noVictime)"""
    def reduit(X, NbTues):
        print(X[0].pop(X[1]))
        return (X[0], (X[1] + nSinistre - 1) % (nbPers - NbTues))
    return reduce(reduit, range(1, nbPers),  (["No " + str(k) for k in range(1, nbPers + 1)], nSinistre - 1))

print(flaviusPyth2(7, 400))
print(flaviusPyth(7, 400))
print(flaviusPyth3(7, 400))

os.system("pause")
