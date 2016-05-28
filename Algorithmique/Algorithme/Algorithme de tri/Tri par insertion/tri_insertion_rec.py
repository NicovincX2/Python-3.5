# -*- coding: utf-8 -*-

import os
from random import randrange
from time import perf_counter


def test(expr):
    global nbc
    nbc += 1
    return expr


def insere(x, t):
    if t == [] or test(x >= t[-1]):
        t.append(x)
        return t
    else:
        tt = insere(x, t[:-1])
        tt.append(t[-1])
        return tt


def tri_ins(t):
    if t == []:
        return []
    else:
        return insere(t[-1], tri_ins(t[:-1]))

n = 800
n_max = 100000
t = [randrange(n_max) for k in range(n)]
# print(t)
nbc = 0
top = perf_counter()
tt = tri_ins(t)
# print(tt)
print(perf_counter() - top, ' s')
print('Nb de comparaisons/n² : ', nbc / n**2)

os.system("pause")
