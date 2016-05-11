# -*- coding: utf-8 -*-

import os
import numpy as np

def Prod_mat(A,B):
    p,q,r=len(A),len(B),len(B[0])
    C=np.zeros((p,r))
    for i in range(p):
        for j in range(r):
            for k in range(q):
                C[i,j]+=A[i,k]*B[k,j]
    return C

def Cout_min(d):
    def m(i,j):
        if i==j:
            return 0
        else:
            dd=d[i-1]*d[j]
            min=m(i+1,j)+dd*d[i]
            for k in range(i+1,j):
                essai=m(i,k)+m(k+1,j)+dd*d[k]
                if essai<min:
                    min=essai
            return min

    return m(1,len(d)-1)

def Tableau_m(d):
    n=len(d)-1
    m=np.zeros((n+1,n+1),dtype=int)
    # kop=np.zeros((n+1,n+1),dtype=int)
    for h in range(1,n):
        for i in range(1,n-h+1):
            j=i+h
            dd=d[i-1]*d[j]
            m[i,j]=m[i+1,j]+dd*d[i]
            # kop[i,j]=i
            for k in range(i+1,j):
                essai=m[i,k]+m[k+1,j]+dd*d[k]
                if essai<m[i,j]:
                    m[i,j]=essai
                    # kop[i,j]=k
    return m #,kop
    
def Parenthesage(kop):
    def Aux(i,j):
        if i==j:
            return 'A['+str(i)+']'
        else:
            return '('+Aux(i,kop[i,j])+Aux(kop[i,j]+1,j)+')'
    
    return Aux(1,len(kop)-1)

print(Parenthesage(Tableau_m([10,5,100,3,50])[1]))

os.system("pause")