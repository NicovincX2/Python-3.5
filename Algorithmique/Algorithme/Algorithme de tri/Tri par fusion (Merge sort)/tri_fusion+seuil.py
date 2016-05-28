# -*- coding: utf-8 -*-

import os
from random import randrange
from time import perf_counter
from math import log2


def test(expr):
    global nbc
    nbc += 1
    return expr


def fusion(t1, t2):
    i1, i2, n1, n2 = 0, 0, len(t1), len(t2)
    t = []
    while i1 < n1 and i2 < n2:
        if test(t1[i1] < t2[i2]):
            t.append(t1[i1])
            i1 += 1
        else:
            t.append(t2[i2])
            i2 += 1
    if i1 == n1:
        t.extend(t2[i2:])
    else:
        t.extend(t1[i1:])
    return t


def tri(t):
    if len(t) < 2:
        return t
    else:
        m = len(t) // 2
        return fusion(tri(t[:m]), tri(t[m:]))


def tri2(t):
    if len(t) < 2:
        return t
    elif len(t) == 2:
        if test(t[0] <= t[1]):
            return t
        else:
            return [t[1], t[0]]
    else:
        m = len(t) // 2
        return fusion(tri(t[:m]), tri(t[m:]))


def tri3(t):
    if len(t) < 2:
        return t
    elif len(t) == 2:
        if test(t[0] <= t[1]):
            return t
        else:
            return [t[1], t[0]]
    elif len(t) == 3:
        if test(t[0] <= t[1]):
            if test(t[1] <= t[2]):
                return t
            elif test(t[0] <= t[2]):
                return [t[0], t[2], t[1]]
            else:
                return [t[2], t[0], t[1]]
        else:
            if test(t[0] <= t[2]):
                return [t[1], t[0], t[2]]
            elif test(t[1] <= t[2]):
                return [t[1], t[2], t[0]]
            else:
                return [t[2], t[1], t[0]]
    else:
        m = len(t) // 2
        return fusion(tri(t[:m]), tri(t[m:]))

n = 100000
n_max = 100
# seed(77)
t = [randrange(n_max) for k in range(n)]
# print(t)
nbc = 0
top = perf_counter()
tt = tri(t)
top = perf_counter() - top
# print(tt)
print('Seuil 1')
print(top, 's')
print('Nb de comparaisons : ', nbc)
print('Nb de comparaisons/(n*log2(n)) : ', nbc / (n * log2(n)))
nbc = 0
top = perf_counter()
tt = tri2(t)
top = perf_counter() - top
# print(tt)
print('Seuil 2')
print(top, 's')
print('Nb de comparaisons : ', nbc)
print('Nb de comparaisons/(n*log2(n)) : ', nbc / (n * log2(n)))
nbc = 0
top = perf_counter()
tt = tri3(t)
top = perf_counter() - top
# print(tt)
print('Seuil 3')
print(top, 's')
print('Nb de comparaisons : ', nbc)
print('Nb de comparaisons/(n*log2(n)) : ', nbc / (n * log2(n)))

os.system("pause")
