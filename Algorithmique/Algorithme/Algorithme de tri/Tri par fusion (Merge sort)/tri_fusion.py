# -*- coding: utf-8 -*-

import os
from random import choice,randrange,seed
from time import perf_counter
from math import log2
from sys import setrecursionlimit

def test(expr):
    global nbc
    nbc+=1
    return expr

def fusionR(t1,t2):
    if t1==[]:
        return t2
    elif t2==[]:
        return t1
    elif t1[0]<t2[0]:
        t=[t1[0]]
        t.extend(fusionR(t1[1:],t2))
        return t
    else:
        t=[t2[0]]
        t.extend(fusionR(t1,t2[1:]))
        return t
    
def fusion(t1,t2):
    i1,i2,n1,n2=0,0,len(t1),len(t2)
    t=[]
    while i1<n1 and i2<n2:
        if test(t1[i1]<t2[i2]):
            t.append(t1[i1])
            i1+=1
        else:
            t.append(t2[i2])
            i2+=1
    if i1==n1:
        t.extend(t2[i2:])
    else:
        t.extend(t1[i1:])
    return t

def tri(t):
    if len(t)<2:
        return t
    else:
        m=len(t)//2
        return fusion(tri(t[:m]),tri(t[m:]))

n=100000
n_max=1000000
#seed(7)
t=[randrange(n_max) for k in range(n)]
#print(t)
nbc=0
top=perf_counter()
tt=tri(t)
top=perf_counter()-top
#print(tt)
print(top,'s')
print('Nb de comparaisons/(n*log2(n)) : ',nbc/(n*log2(n)))        

os.system("pause")