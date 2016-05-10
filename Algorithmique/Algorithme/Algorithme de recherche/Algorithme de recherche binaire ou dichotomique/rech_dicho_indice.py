# -*- coding: utf-8 -*-

import os

from random import randrange,seed

def ChercheI(x,t):
    i=0
    j=len(t)
    while i<j-1:
        m=(i+j)//2
        if t[m]<=x:
            i=m
        else:
            j=m
    if t[i]==x:
        return i
    else:
        return -1


def ChercheR1(x,t,i=0):
    if len(t)==1:
        if t[0]==x:
            return i
        else:
            return -1
    else:
        m=len(t)//2
        if t[m]<=x:
            return ChercheR1(x,t[m:],i+m)
        else:
            return ChercheR1(x,t[:m],i)


def ChercheR2(x,t):
    def indice(i,j):
        if i==j-1:
            if t[i]==x:
                return i
            else:
                return -1
        else:
            m=(i+j)//2
        if t[m]<=x:
            return indice(m,j)
        else:
            return indice(i,m)

    return indice(0,len(t))


n=60
n_max=1000
seed(77)
t=[randrange(n_max) for k in range(n)]
t.sort()
print(t)
x=1170
print(ChercheR1(x,t))
print(ChercheR2(x,t))

os.system("pause")