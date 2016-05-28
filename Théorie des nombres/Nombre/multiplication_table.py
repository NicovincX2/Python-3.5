# -*- coding: utf-8 -*-

import os
from numpy import *
from time import perf_counter


def mul1(n):
    return array([[(i + 1) * (j + 1) for i in range(n)] for j in range(n)])

top = perf_counter()
print(mul1(4))
print(perf_counter() - top)
top = perf_counter()
mul1(100)
print(perf_counter() - top)


def mul2(n):
    M = arange(1, n + 1).reshape((-1, 1))
    M = tile(M, (1, n))
    N = arange(1, n + 1).reshape((1, -1))
    N = tile(N, (n, 1))
    return M * N

top = perf_counter()
print(mul2(4))
print(perf_counter() - top)
top = perf_counter()
mul2(100)
print(perf_counter() - top)


def mul3(n):
    M = arange(1, n + 1).reshape((-1, 1))
    N = arange(1, n + 1).reshape((1, -1))
    return M * N

top = perf_counter()
print(mul3(4))
print(perf_counter() - top)
top = perf_counter()
mul3(100)
print(perf_counter() - top)

os.system("pause")
