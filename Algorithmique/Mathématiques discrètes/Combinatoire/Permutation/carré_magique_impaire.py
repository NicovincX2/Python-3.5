# -*- coding: utf-8 -*-

import os

"""
@author: hbouia (Created on Fri May 06 21:28:02 2016)
Carrés magiques d'ordre impair 
voir algorithme (MERCI à eux) sur http://lycees.ac-rouen.fr/bruyeres/maths/carimp.html
"""

import numpy as np

def afficher(m,n):
    fmt=('\n' + ('%'+'%dd ' % (np.log10(n*n)+1))*n )*n
    print (fmt % tuple((m[i,j] for i in range(n) for j in range(n))))

def MagicSquare(n):
    ms=np.zeros((n,n),int)    
    i,j=n-1,(n-1)/2
    ms[i,j]=1
    for k in range(1,n*n):
        i1,j1=(i+1)%n,(j+1)%n
        i,j=(i1,j1) if ms[i1,j1]==0 else ((i-1)%n,j)
        ms[i,j]=k+1
    return ms

# Exemples pour les carrés magiques d'ordre impairs de 3 à 25
for n in range(3,26,2):
    print (u"\nCarré magique d'ordre %d et de somme magique %d" % (n,n*(n*n+1)/2))
    afficher(MagicSquare(n),n)

os.system("pause")