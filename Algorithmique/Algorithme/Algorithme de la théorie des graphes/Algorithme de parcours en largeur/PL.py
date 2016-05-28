# -*- coding: utf-8 -*-

import os
import sys
sys.path.append(r'D:')

from files import *
from numpy import inf


def PL(L, s):
    n = len(L)
    c = n * ['blanc']
    d = n * [inf]
    p = n * [-1]
    F = file_vide()
    c[s] = 'gris'
    d[s] = 0
    ajouter(s, F)
    while not est_file_vide(F):
        u = suivant(F)
        for v in L[u]:
            if c[v] == 'blanc':
                c[v] = 'gris'
                ajouter(v, F)
                d[v] = d[u] + 1
                p[v] = u
        c[u] = 'noir'
    print(d)
    print(p)

L = [[1, 4], [0, 5], [3, 5, 6], [2, 7], [0], [1, 2, 6], [2, 5, 7], [3, 6]]
PL(L, 1)

os.system("pause")
