# -*- coding: utf-8 -*-

import os
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

def test(b):
    global nb
    nb+=1
    return b

def entasser(i,t): #entasse t[i] parmi t[1],…,t[i-1]
    p=i//2 #le père
    while i>1 and test(t[i]>t[p]):
        t[i],t[p]=t[p],t[i]
        i,p=p,p//2

def suppr_min(t,n): #échange t[1] et t[n] et
                    #refait un tas avec les n-1 premières valeurs
    t[1],t[n]=t[n],t[1]
    n-=1
    i=1
    while i<=n//2:
        if 2*i==n or test(t[2*i]>t[2*i+1]):
            f=2*i
        else:
            f=2*i+1
        if test(t[i]<t[f]):
            t[i],t[f]=t[f],t[i]
            i=f
        else:
            break

def tri_tas2(ti):
    n=len(ti)
    ti=[0]+ti
    for i in range(2,n+1):
        entasser(i,ti)
    for i in range(n,1,-1):
        suppr_min(ti,i)
    return ti[1:]

def ordonner(t,r):
    n=len(t)-1
    if 2*r==n or test(t[2*r]>t[2*r+1]):
        f=2*r
    else:
        f=2*r+1
    if test(t[r]<t[f]):
        t[r],t[f]=t[f],t[r]
        if f<=n//2:
            ordonner(t,f)
      
def tri_tas3(ti):
    n=len(ti)
    ti=[0]+ti
    d=n//2
    for r in range(d,0,-1):
        ordonner(ti,r)
    for i in range(n,1,-1):
        suppr_min(ti,i)
    return ti[1:]        
    
n=50
n_max=1000000
t1=[randrange(n_max) for k in range(n)]
t2=t1.copy()
nb=0
tri_tas2(t1)
print('Avec tri_tas2 : ',nb,' comparaisons')
nb2=nb
nb=0
tri_tas3(t2)
print('Avec tri_tas3 : ',nb,' comparaisons')
print('Gain : ','{:%}'.format(1-nb/nb2))

os.system("pause")