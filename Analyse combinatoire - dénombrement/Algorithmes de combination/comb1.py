# -*- coding: utf-8 -*-

import os

def comb(m, lst):
    if m == 0: return [[]]
    return [[x] + suffix for i, x in enumerate(lst)
            for suffix in comb(m - 1, lst[i + 1:])]

comb(3, range(5))

os.system("pause")