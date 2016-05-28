# -*- coding: utf-8 -*-

import os


def somme_chiffres(n):
    s = 0
    while n > 0:
        c = n % 10
        s += c
        n //= 10
    return s


def somme_chiffres_rec(n):
    if n < 10:
        return n
    return n % 10 + somme_chiffres_rec(n // 10)

os.system("pause")
