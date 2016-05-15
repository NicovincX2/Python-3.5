# -*- coding: utf-8 -*-

"""
On lance 10 fois de suite une pièce de monnaie et on voudrait observer la moyenne du nombre maximal de résultats consécutifs égaux.
"""

import os
from collections import Counter
from itertools import groupby
from numpy.random import randint

def plus_gd_paquet(liste):
    return max([len(list(groupe)) for cle, groupe in groupby(liste)])

def dic_paquet(n):
    s = [plus_gd_paquet(randint(0,2,size = 10) ) for k in range(n)]
    return  Counter(s)

def moyenne_paquet(n):
    c = dic_paquet(n)
    return sum([k * c[k] for k in c]) / n

print(dic_paquet(100000))
print(moyenne_paquet(100000))

os.system("pause")
