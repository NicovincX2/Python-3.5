# -*- coding: utf-8 -*-

import os


def PGCDi(a, b):
    while b > 0:
        a, b = b, a % b
    return a

print(PGCDi(72, 48))


def PGCDr(a, b):
    if b == 0:
        return a
    else:
        return PGCDr(b, a % b)

print(PGCDr(72, 48))

os.system("pause")
