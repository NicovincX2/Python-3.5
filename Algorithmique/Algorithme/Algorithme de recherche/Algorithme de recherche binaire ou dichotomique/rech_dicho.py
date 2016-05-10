# -*- coding: utf-8 -*-

import os

from random import randrange,seed

def ChercheI(x,t):
    i=0
    j=len(t)
    while j-i>1:
        m=(i+j)//2
        if t[m]<=x:
            i=m
        else:
            j=m
    return t[i]==x

def ChercheR(x,t):
    if len(t)==1:
        return t[0]==x
    else:
        m=len(t)//2
        if t[m]<=x:
            return ChercheR(x,t[m:])
        else:
            return ChercheR(x,t[:m])

n=60
n_max=100
seed(77)
t=[randrange(n_max) for k in range(n)]
t.sort()
print(t)
x=-5
print(ChercheR(x,t))

os.system("pause")