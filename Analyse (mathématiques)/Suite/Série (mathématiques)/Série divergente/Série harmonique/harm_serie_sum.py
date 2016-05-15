# -*- coding: utf-8 -*-

import os

# Croissant
def somme1(n):
    S = 0
    for k in range(1,n+1):
        S += 1.0 / k
    return S

# Décroissant
def somme2(n):
    S = 0
    for k in range(n,0,-1):
        S += 1.0 / k
    return S
	
print(somme1(100000))
print(somme2(100000))

def Fast2Sum(a,b):
    if a >= b:
        s = a + b
        z = s - a
        return (s, b - z)
    else:
        return Fast2Sum(b,a)
 
def Pichat(liste):
    accS = 0
    accE = 0
    for k in liste:
        s,e = Fast2Sum(accS,k)
        accS  = s
        accE += e
    return accS + accE
	
os.system("pause")

