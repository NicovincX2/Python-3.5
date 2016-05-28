# -*- coding: utf-8 -*-

import os
from time import perf_counter, clock


def divisors(n):
    '''
    divisors(integer) -> list of integers
    Return the proper divisors of n (numbers less than n that divide evenly into n).
    '''
    return [div for div in range(1, n) if n % div == 0]

from math import ceil


def divisors2(n):
    divs = [1]
    for m in range(2, ceil(n ** 0.5)):  # 1 and n**0.5 will be handled separately. why?
        if n % m == 0:
            divs += [m, n // m]
    if n % n ** 0.5 == 0:
        divs += [int(n ** 0.5)]
    return divs

print(divisors(36))
print(sorted(divisors2(36)))

top = perf_counter()
divisors(10**4)
print(perf_counter() - top)
top = perf_counter()
divisors2(10**4)
print(perf_counter() - top)

n = 1234567890
tic = clock()
divisors(n)
toc = clock()
print("divisors: ", (toc - tic))
tic = clock()
divisors2(n)
toc = clock()
print("divisors2:", (toc - tic))

os.system("pause")
