# -*- coding: utf-8 -*-

import os
# import cython
from time import perf_counter

def primes1(n):
    primes = [False, False] + [True] * (n - 2)
    i = 2
    while i < n:
        # we do not deal with composite numbers
        if not primes[i]:
            i += 1
            continue
        k = i * i
        # mark multiples of i as composite numbers
        while k < n:
            primes[k] = False
            k += i
        i += 1
    return [i for i in range(2, n) if primes[i]]

n = 10000

top = perf_counter()
print (primes1(20))
print(perf_counter()-top)
top = perf_counter()
primes1(n)
print(perf_counter()-top)

def primes2(n):
    primes = [False, False] + [True] * (n - 2)
    i = 2
    while i < n:
        if not primes[i]:
            i += 1
            continue
        k = i * i
        while k < n:
            primes[k] = False
            k += i
        i += 1
    return [i for i in range(2, n) if primes[i]]

top = perf_counter()
print (primes2(20))
print(perf_counter()-top)
top = perf_counter()
primes2(n)
print(perf_counter()-top)

"""
def primes3(int n):
    primes = [False, False] + [True] * (n - 2)
    cdef int i = 2
    cdef int k = 0
    while i < n:
        if not primes[i]:
            i += 1
            continue
        k = i * i
        while k < n:
            primes[k] = False
            k += i
        i += 1
    return [i for i in range(2, n) if primes[i]]

top = perf_counter()
print (primes3(20))
print(perf_counter()-top)
top = perf_counter()
primes3(n)
print(perf_counter()-top)
"""

os.system("pause")

