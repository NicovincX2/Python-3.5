# -*- coding: utf-8 -*-

import os
from math import log2
from random import randrange

def afficher(t):
    n=len(t)-1 #tas indexé de 1 à n
    h=int(log2(n)) #hauteur de l'arbre
    nbsc=[1] #nb d'espaces sur les côtés
    for i in range(h):
        nbsc=[2*nbsc[0]+1]+nbsc
    nbsi=[1] #nb d'espaces intermédiaires
    for i in range(h):
        nbsi=[2*nbsi[0]+3]+nbsi
    for i in range(h+1):
        ligne=' '*nbsc[i]
        for j in range(2**i,min(2**(i+1),n+1)):
            ligne=ligne+'{:^3}'.format(t[j])+' '*nbsi[i]
        print(ligne)

def entasser(x,t):
    t.append(x)
    i=len(t)-1 #l'indice de cette dernière valeur
    p=i//2 #le père
    while i>1 and t[i]<t[p]:
        t[i],t[p]=t[p],t[i]
        i,p=p,p//2

def suppr_min(t):
    t[1]=t[-1]
    t.pop()
    n=len(t)-1
    i=1
    while i<=n//2:
        if 2*i==n or t[2*i]<t[2*i+1]:
            f=2*i
        else:
            f=2*i+1
        if t[i]>t[f]:
            t[i],t[f]=t[f],t[i]
            i=f
        else:
            break

def tri_tas1(ti):
    tas=[0]
    for x in ti:
        entasser(x,tas)
    ti=[]
    while len(tas)>1:
        ti.append(tas[1])
        suppr_min(tas)
    return ti
        
    
ti=[3,5,9,6,8,11,10,12,18,14]
n=12
ti=[randrange(1000) for k in range(n)]
print(ti)
print(tri_tas1(ti))

os.system("pause")