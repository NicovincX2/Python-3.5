# -*- coding: utf-8 -*-

import os
from random import choice, randrange, seed
from time import process_time


def pp(x, y):
    global nbc
    nbc += 1
    return x < y


def indice_min(t):
    if len(t) == 1:
        return 0
    else:
        j = 1 + indice_min(t[1:])
        if t[0] < t[j]:
            return 0
        else:
            return j


def tri_sel(t):
    if t == []:
        return []
    else:
        j = indice_min(t)
        return [t[j]] + tri_sel(t[:j] + t[j + 1:])

n = 100
n_max = 10000
seed(77)
t = [randrange(n_max) for k in range(n)]
print(t)
nbc = 0
top = process_time()
tt = tri_sel(t)
print(process_time() - top, ' s')
print('Nb de comparaisons/n² : ', nbc / n**2)
print(tt)

os.system("pause")
