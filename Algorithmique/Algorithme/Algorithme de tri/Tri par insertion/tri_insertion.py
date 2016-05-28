# -*- coding: utf-8 -*-

import os
from random import randrange
from time import perf_counter


def test(expr):
    global nbc
    nbc += 1
    return expr


def tab_alea(n, v_max):
    return [randrange(v_max) for k in range(n)]


def tri_ins(t):
    for k in range(1, len(t)):
        temp = t[k]
        j = k
        while j > 0 and test(temp < t[j - 1]):
            t[j] = t[j - 1]
            j -= 1
        t[j] = temp
    return t


n = 100
v_max = 100000
t = tab_alea(n, v_max)
# print(t)
nbc = 0
top = perf_counter()
tt = tri_ins(t)
# print(tt)
print(perf_counter() - top, ' s')
print('Nb de comparaisons/n² : ', nbc / n**2)

os.system("pause")
