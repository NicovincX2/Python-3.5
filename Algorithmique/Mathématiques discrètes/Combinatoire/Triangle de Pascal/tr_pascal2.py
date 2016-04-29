# -*- coding: utf-8 -*-

import os

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

def pascal(n):
    for i in range(n + 1):
        for j in range(i + 1):
            print(binom_mem(i,j), end="\t")
        print()

pascal(4)
pascal(7)

os.system("pause")

