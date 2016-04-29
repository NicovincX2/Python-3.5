# -*- coding: utf-8 -*-

import os
import numpy
import timeit

def mul1(n):
    return array([[(i + 1) * (j + 1) for i in xrange(n)] for j in xrange(n)])

mul1(4)
timeit mul1(100)

def mul2(n):
    M = arange(1, n + 1).reshape((-1, 1))
    M = tile(M, (1, n))
    N = arange(1, n + 1).reshape((1, -1))
    N = tile(N, (n, 1))
    return M * N

mul2(4)
timeit mul2(100)

def mul3(n):
    M = arange(1, n + 1).reshape((-1, 1))
    N = arange(1, n + 1).reshape((1, -1))
    return M * N

mul3(4)
timeit mul3(100)

os.system("pause")

