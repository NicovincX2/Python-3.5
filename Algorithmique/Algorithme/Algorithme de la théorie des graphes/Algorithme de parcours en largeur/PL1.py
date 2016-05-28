# -*- coding: utf-8 -*-

import os
import queue

#------------------------
# Parcours en largeur


def Parcours_PL(G, s):
    Couleur = {}
    Pred = {}
    Dist = {}
    for x in G[0]:
        Couleur[x] = 0
        Pred[x] = None
        Dist[x] = None
    Couleur[s] = 1
    Dist[s] = 0
    F = Queue.Queue()
    F.put(s)
    while not F.empty():
        x = F.get()
        for y in G[1][x]:
            if Couleur[y] == 0:
                Couleur[y] = 1
                Dist[y] = Dist[x] + 1
                Pred[y] = x
                F.put(y)
        Couleur[x] = 2

    return (Dist, Pred)

os.system("pause")
