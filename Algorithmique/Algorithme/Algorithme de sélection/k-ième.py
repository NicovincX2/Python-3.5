# -*- coding: utf-8 -*-

import os

from random import choice,randrange,seed
from time import process_time
from math import log

def pp(x,y):
    global nbc
    nbc+=1
    return x<y

def quicksort3(t):
    if len(t)<2:
        return t
    else:
        pivot = t[0]
        t1 = []
        t2 = []
        for x in t[1:]:
            if x<pivot:
                t1.append(x)
            else:
                t2.append(x)
        return quicksort3(t1) + [pivot] + quicksort3(t2)

def partition(t,g,d):
    p=g
    pivot=t[g]
    for k in range(g+1,d):
        if pp(t[k],pivot):
            p+=1
            t[p],t[k]=t[k],t[p]
    t[p],t[g]=t[g],t[p]
    return p

def quick_ieme(t,k):
    def k_ieme(g,d):
        p=partition(t,g,d)
        if p==k:
            return t[p]
        elif p>k:
            return k_ieme(g,p)
        else:            
            return k_ieme(p+1,d)

    return k_ieme(0,len(t))

n=100000
n_max=10000
seed(77)
t=[randrange(n_max) for k in range(n)]
#print(t)
nbc=0
#print(quicksort3(t[:]))
print(quick_ieme(t,n//2))
print('Nbc/n : ',nbc/n)

os.system("pause")