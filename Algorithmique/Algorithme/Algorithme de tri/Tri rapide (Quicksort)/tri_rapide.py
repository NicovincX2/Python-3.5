# -*- coding: utf-8 -*-

import os
from random import choice,randrange,seed
from time import perf_counter
from math import log

def test(expr):
    global nbc
    nbc+=1
    return expr

def quicksort1(t):
    if t == []:
        return []
    else:
        pivot = t[0]
        pivot_occ = t.count(pivot)
        t1 = [ e for e in t if test(e<pivot) ]
        t2 = [ e for e in t if test(e>pivot) ]
        return quicksort1(t1) + [pivot] * pivot_occ + quicksort1(t2)

def quicksort2(t):
    if t == []:
        return []
    else:
        pivot = t[0]
        t1 = []
        t2 = []
        nbp=0
        for x in t:
            if test(x<pivot):
                t1.append(x)
            elif test(pivot<x):
                t2.append(x)
            else:
                nbp+=1
        return quicksort2(t1) + [pivot] * nbp + quicksort2(t2)

def quicksort3(t):
    if len(t)<2:
        return t
    else:
        pivot=t[0]
        t1=[]
        t2=[]
        for x in t[1:]:
            if test(x<pivot):
                t1.append(x)
            else:
                t2.append(x)
        tt=quicksort3(t1)
        tt.append(pivot)
        tt.extend(quicksort3(t2))
        return tt
#        return quicksort3(t1) + [pivot] + quicksort3(t2)

def partition(t,g,d):
    p=g
    pivot=t[g]
    for k in range(g+1,d):
        if test(t[k]<pivot):
            p+=1
            t[p],t[k]=t[k],t[p]
    t[p],t[g]=t[g],t[p]
    return p

def quicksort(t):
    def tri(g,d):
        if g<d:
            p=partition(t,g,d)
            tri(g,p)
            tri(p+1,d)

    tri(0,len(t))
    return t

n=100000
n_max=1000
t=[randrange(n_max) for k in range(n)]
#print(t)
print('quicksort1 :')
nbc=0
top=perf_counter()
try:
    tt=quicksort1(t)
except RuntimeError:
    print('Erreur')
else:
    print(perf_counter()-top,' s')
    print('Nb de comparaisons/(n*ln(n)) : ',nbc/n/log(n))
#print(tt)
print('\nquicksort2 :')
nbc=0
top=perf_counter()
try:
    tt=quicksort2(t)
except RuntimeError:
    print('Erreur')
else:
    print(perf_counter()-top,' s')
    print('Nb de comparaisons/(n*ln(n)) : ',nbc/n/log(n))
print('\nquicksort3 :')
nbc=0
top=perf_counter()
try:
    tt=quicksort3(t)
except RuntimeError:
    print('Erreur')
else:
    print(perf_counter()-top,' s')
    print('Nb de comparaisons/(n*ln(n)) : ',nbc/n/log(n))
print('\nquicksort :')
nbc=0
top=perf_counter()
try:
    tt=quicksort(t)
except RuntimeError:
    print('Erreur')
else:
    print(perf_counter()-top,' s')
    print('Nb de comparaisons/(n*ln(n)) : ',nbc/n/log(n))

os.system("pause")