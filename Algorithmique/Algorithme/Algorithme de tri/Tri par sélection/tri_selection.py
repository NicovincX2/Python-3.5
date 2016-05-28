# -*- coding: utf-8 -*-

import os
from random import choice, randrange, seed
from time import process_time


def pp(x, y):
    global nbc
    nbc += 1
    return x < y


def indice_min(t, g, d):
    j = g
    for i in range(g + 1, d):
        if t[i] < t[j]:
            j = i
    return j


def tri_sel(t):
    n = len(t)
    for k in range(n - 1):
        j = indice_min(t, k, n)
        if k < j:
            t[k], t[j] = t[j], t[k]
    return t

n = 100
n_max = 10000
seed(77)
t = [randrange(n_max) for k in range(n)]
print(t)
nbc = 0
top = process_time()
tri_sel(t)
print(process_time() - top, ' s')
print('Nb de comparaisons/n² : ', nbc / n**2)
print(t)

os.system("pause")
