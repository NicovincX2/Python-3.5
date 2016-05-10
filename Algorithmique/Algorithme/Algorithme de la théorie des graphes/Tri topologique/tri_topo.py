# -*- coding: utf-8 -*-

import os
import sys
sys.path.append(r'D:')

from files import *

def TriTopo(L):
    def Visiter(u):
        c[u]='gris'
        for v in L[u]:
            if c[v]=='blanc':
                Visiter(v)
        c[u]='noir'
        empiler(u,T)

    n=len(L)
    c=n*['blanc']
    T=pile_vide()
    for u in range(n):
        if c[u]=='blanc':
            Visiter(u)
    return [depiler(T) for k in range(n)]

L=[[3,4],[4],[],[4,5],[],[8],[5,7],[8],[]]
print(TriTopo(L))

os.system("pause")