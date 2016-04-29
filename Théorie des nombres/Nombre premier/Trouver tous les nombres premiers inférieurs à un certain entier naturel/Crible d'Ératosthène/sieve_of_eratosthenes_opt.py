# -*- coding: utf-8 -*-

import os
import cython
import timeit

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
    return [i for i in xrange(2, n) if primes[i]]

n = 10000

primes1(20)
timeit primes1(n)

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
    return [i for i in xrange(2, n) if primes[i]]

primes2(20)
timeit primes2(n)

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
    return [i for i in xrange(2, n) if primes[i]]

prime3(20)
timeit primes3(n)

os.system("pause")

