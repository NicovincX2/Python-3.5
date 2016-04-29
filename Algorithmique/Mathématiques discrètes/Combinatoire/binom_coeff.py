# -*- coding: utf-8 -*-

import os
import timeit

def binom_naive(n, k):
    if k == n or k == 0:
        return 1
    if n < k or n < 0 or k < 0:
        return 0
    return binom_naive(n - 1, k - 1) + binom_naive(n - 1, k)

def binom_formula(n,k):
    return factorial(n) // (factorial(k) * factorial(n - k))

def factorial(n):
    if n == 0: 
        return 1
    return n * factorial(n - 1)

binom_memory = {}

def binom_mem(n, k):
    if k == n or k == 0:
        return 1
    if k > n or n < 0 or k < 0:
        return 0
    key = (n,k)
    if key not in binom_memory:
        binom_memory[key] =  binom_mem(n - 1, k - 1) + binom_mem(n - 1, k)
    return binom_memory[key]
	
timeit -n 100 binom_naive(14,5)
timeit -n 1000 binom_formula(14,5)
timeit -n 1000 binom_mem(14,5)

timeit -n 1 binom_naive(24,8)
timeit -n 10 binom_formula(24,8)
timeit -n 10 binom_mem(24,8)

os.system("pause")

