# -*- coding: utf-8 -*-

import os
from time import perf_counter


def som_max1(t):
    n = len(t)
    s_max = t[0]
    for g in range(n):
        for d in range(g + 1, n + 1):
            s = t[g]
            for k in range(g + 1, d):
                s += t[k]
            s_max = max(s_max, s)
    return s_max


def som_max2(t):
    n = len(t)
    s_max = t[0]
    for g in range(n):
        s = t[g]
        s_max = max(s_max, s)
        for k in range(g + 1, n):
            s += t[k]
            s_max = max(s_max, s)
    return s_max


def som_max3(t):
    if len(t) == 1:
        return t[0]
    else:
        s_max = t[0]
        s = t[0]
        for k in range(1, len(t)):
            s += t[k]
            s_max = max(s_max, s)
        return max(s_max, som_max3(t[1:]))


def som_max4(t):
    sigma = t[0]
    delta = t[0]
    for p in range(1, len(t)):
        delta = max(t[p], delta + t[p])
        sigma = max(sigma, delta)
    return sigma

t1 = [-4, 8, -1, -3, 5, 25]
t2 = [-4, -1, -3, -2, -7, -5]

print("Som_max1")
top = perf_counter()
print(som_max1(t1))
print(perf_counter() - top)
top = perf_counter()
print(som_max1(t2))
print(perf_counter() - top)

print("Som_max2")
top = perf_counter()
print(som_max2(t1))
print(perf_counter() - top)
top = perf_counter()
print(som_max2(t2))
print(perf_counter() - top)

print("Som_max3")
top = perf_counter()
print(som_max3(t1))
print(perf_counter() - top)
top = perf_counter()
print(som_max3(t2))
print(perf_counter() - top)

print("Som_max4")
top = perf_counter()
print(som_max4(t1))
print(perf_counter() - top)
top = perf_counter()
print(som_max4(t2))
print(perf_counter() - top)

os.system("pause")
