# -*- coding: utf-8 -*-

import os
from numpy import inf
import numpy as np


def PP(L):
    def Visiter(u):
        nonlocal instant
        c[u] = 'gris'
        d[u] = instant
        instant += 1
        for v in L[u]:
            if c[v] == 'blanc':
                Visiter(v)
        c[u] = 'noir'
        f[u] = instant
        instant += 1

    n = len(L)
    c = n * ['blanc']
    d = n * [0]
    f = n * [0]
    instant = 1
    for u in range(n):
        if c[u] == 'blanc':
            Visiter(u)
    print(d)
    print(f)

L = [[1, 3], [4], [4, 5], [1], [3], []]
PP(L)

os.system("pause")
