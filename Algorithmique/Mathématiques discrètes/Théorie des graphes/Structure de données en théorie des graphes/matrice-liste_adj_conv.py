# -*- coding: utf-8 -*-

import os
import numpy as np

def GtoM(n,A):
    M=np.zeros((n,n))
    for a in A:
        M[a]=1
    return M

def GtoL(n,A):
    L=[[] for k in range(n)]
    for (i,j) in A:
        L[i].append(j)
    return L

def MtoL(M):
    n=len(M)
    L=[[] for k in range(n)]
    for i in range(n):
        for j in range(n):
            if M[i,j]==1:
                L[i].append(j)
    return L

def LtoM(L):
    n=len(L)
    M=np.zeros((n,n))
    for i in range(n):
        for j in L[i]:
            M[i,j]=1
    return M

L=[[1,4],[0,5],[3,5,6],[2,7],[0],[1,2,6],[2,5,7],[3,6]]
A=[(0,1),(0,3),(1,4),(2,4),(2,5),(3,1),(4,3)]
print(LtoM(GtoL(6,A)))

os.system("pause")