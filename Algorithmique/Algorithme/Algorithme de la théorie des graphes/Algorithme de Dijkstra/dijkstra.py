# -*- coding: utf-8 -*-

import os
from numpy import inf


def Dijkstra(L, s):
    def Extraire_min():
        nonlocal E
        u_min = E[0]
        e_min = e[u_min]
        for u in E[1:]:
            if e[u] < e_min:
                e_min = e[u]
                u_min = u
        E = [u for u in E if u != u_min]
        return u_min

    n = len(L)
    e = n * [inf]
    p = n * [-1]
    E = list(range(n))
    e[s] = 0
    while E != []:
        u = Extraire_min()
        for (v, V) in L[u]:
            if e[u] + V < e[v]:
                e[v] = e[u] + V
                p[v] = u
    print(e)
    print(p)

L = [[(1, 10), (3, 5)], [(2, 1), (3, 2)], [(4, 4)],
     [(1, 3), (2, 9), (4, 2)], [(0, 7), (2, 6)]]
Dijkstra(L, 1)

os.system("pause")
