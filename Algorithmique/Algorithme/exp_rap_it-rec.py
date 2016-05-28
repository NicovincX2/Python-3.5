# -*- coding: utf-8 -*-

import os


def puiss(x, n):
    result = 1
    for k in range(n):
        result *= x
    return result


def expRapI(x, n):
    result = 1
    while n != 0:
        if n % 2 == 1:
            result *= x
        x *= x
        n //= 2
    return result


def expRapR(x, n):
    if n == 0:
        return 1
    else:
        if n % 2 == 0:
            return expRapR(x * x, n // 2)
        else:
            return x * expRapR(x * x, n // 2)


def puiss1(x, n):
    if n == 0:
        return 1
    else:
        return x * puiss1(x, n - 1)

print(expRapI(2, 10))

os.system("pause")
