# -*- coding: utf-8 -*-

import os
from time import perf_counter

def Partie(E,p):
    A=[]
    for k in range(len(E)):
        if p[k]==1: A.append(E[k])
    return A
    
def Ajoute1(p):
    k=0
    while p[k]==1:
        p[k]=0
        k+=1
    p[k]=1
    return p
    
def EnsPartiesI(E):
    n=len(E)
    p=n*[0]
    L=[[]]
    for j in range(1,2**n):
        p=Ajoute1(p)
        L.append(Partie(E,p))
    return L

def EnsPartiesR(E):
    def Aux(k):
        if k<0:
            L.append(Partie(E,p))
        else:
            p[k]=0;Aux(k-1)
            p[k]=1;Aux(k-1)
    
    n=len(E)
    p=n*[0]
    L=[]
    Aux(n-1)
    return L

top = perf_counter()
print(EnsPartiesR([1,2,3,4,5,6,7,8,9]))
print(perf_counter()-top)

top = perf_counter()
print(EnsPartiesI([1,2,3,4,5,6,7,8,9]))
print(perf_counter()-top)

os.system("pause")