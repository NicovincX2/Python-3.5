# -*- coding: utf-8 -*-

import os
from random import randrange
from time import perf_counter
from math import log


def test(expr):
    global nbc
    nbc += 1
    return expr


def quicksort1(t):
    if t == []:
        return []
    else:
        pivot = t[0]
        pivot_occ = t.count(pivot)
        t1 = [e for e in t if pp(e, pivot)]
        t2 = [e for e in t if pp(pivot, e)]
        return quicksort1(t1) + [pivot] * pivot_occ + quicksort1(t2)


def quicksort2(t):
    if t == []:
        return []
    else:
        pivot = t[0]
        t1 = []
        t2 = []
        nbp = 0
        for x in t:
            if test(x < pivot):
                t1.append(x)
            elif test(pivot < x):
                t2.append(x)
            else:
                nbp += 1
        return quicksort2(t1) + [pivot] * nbp + quicksort2(t2)


def quicksort3(t):
    if len(t) < 2:
        return t
    else:
        pivot = t[0]
        t1 = []
        t2 = []
        for x in t[1:]:
            if x < pivot:
                t1.append(x)
            else:
                t2.append(x)
        return quicksort3(t1) + [pivot] + quicksort3(t2)


def partition(t, g, d):
    p = randrange(g, d)
    t[p], t[g] = t[g], t[p]
    pivot = t[g]
    p = g
    for k in range(g + 1, d):
        if test(t[k] < pivot):
            p += 1
            t[p], t[k] = t[k], t[p]
    t[p], t[g] = t[g], t[p]
    return p


def quicksort(t):
    def tri(g, d):
        if g < d:
            p = partition(t, g, d)
            tri(g, p)
            tri(p + 1, d)

    tri(0, len(t))


def quicksortS2(t):
    def tri(g, d):
        if g < d:
            p = partition(t, g, d)
            tri(g, p)
            tri(p + 1, d)

    if len(t) == 2:
        if test(t[0] > t[1]):
            t = [t[1], t[0]]
    elif len(t) > 2:
        tri(0, len(t))


def quicksortS3(t):
    def tri(g, d):
        if g < d:
            p = partition(t, g, d)
            tri(g, p)
            tri(p + 1, d)

    if len(t) == 2:
        if test(t[0] > t[1]):
            t = [t[1], t[0]]
    elif len(t) == 3:
        if test(t[0] <= t[1]):
            if test(t[1] > t[2]):
                if test(t[0] <= t[2]):
                    t = [t[0], t[2], t[1]]
                else:
                    t = [t[2], t[0], t[1]]
        else:
            if test(t[0] <= t[2]):
                t = [t[1], t[0], t[2]]
            elif test(t[1] <= t[2]):
                t = [t[1], t[2], t[0]]
            else:
                t = [t[2], t[1], t[0]]
    elif len(t) > 3:
        tri(0, len(t))

n = 100000
n_max = 10000000
t = [randrange(n_max) for k in range(n)]
# print(t)
tt = t.copy()
nbc = 0
top = perf_counter()
quicksort(tt)
top = perf_counter() - top
# print(tt)
print('Seuil 1')
print(top, 's')
print('Nb de comparaisons : ', nbc)
print('Nb de comparaisons/(n*ln(n)) : ', nbc / (n * log(n)))
tt = t.copy()
nbc = 0
top = perf_counter()
quicksortS2(tt)
top = perf_counter() - top
# print(tt)
print('Seuil 2')
print(top, 's')
print('Nb de comparaisons : ', nbc)
print('Nb de comparaisons/(n*ln(n)) : ', nbc / (n * log(n)))
tt = t.copy()
nbc = 0
top = perf_counter()
quicksortS3(tt)
top = perf_counter() - top
# print(tt)
print('Seuil 3')
print(top, 's')
print('Nb de comparaisons : ', nbc)
print('Nb de comparaisons/(n*ln(n)) : ', nbc / (n * log(n)))

os.system("pause")
