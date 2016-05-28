# -*- coding: utf-8 -*-

import os
from functools import reduce


def fact(n):
    result = 1
    for k in range(2, n + 1):
        result = result * k
    return result


def fact_bis(n):
    assert n >= 0, 'factorielle définie sur N'
    acc = 1
    for k in range(1, n + 1):
        acc *= k
    return acc


def fact2(n):
    assert n >= 0, 'factorielle définie sur N'
    if n == 0:
        return 1
    return n * fact2(n - 1)


def fact3(n):
    assert n >= 0, 'factorielle définie sur N'
    return reduce(lambda acc, k: acc * k, range(1, n + 1), 1)

print(fact(5))
print(fact_bis(5))
print(fact2(5))
print(fact3(5))


def est_divisible(n):
    return fact(n) % (n + 1) == 0

os.system("pause")
