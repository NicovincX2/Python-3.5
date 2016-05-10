# -*- coding: utf-8 -*-

import os
import numpy as np

def binom_a(n,p):
    if p>n:
        return 0
    elif p==0:
        return 1
    else:
        return binom_a(n-1,p-1)+binom_a(n-1,p)
        
def binom_b(n,p):
    if n-p<p: p=n-p
    if p<0:
        return 0
    else:
        t=np.zeros((n+1,p+1),dtype=int)
        t[0,0]=1
        for i in range(1,n+1):
            t[i,0]=1
            for j in range(1,p+1):
                t[i,j]=t[i-1,j-1]+t[i-1,j]
        return t[n,p]

def binom_b2(n,p):
    if n-p<p: p=n-p
    if p<0:
        return 0
    else:
        t=np.zeros((n+1,p+1),dtype=int)
        for i in range(n-p+1):
            t[i,0]=1
        for j in range(1,p+1):
            t[j,j]=1
            for i in range(j+1,n-p+j+1):
                t[i,j]=t[i-1,j-1]+t[i-1,j]
        return t[n,p]

def binom_c(n,p):
    if n-p<p: p=n-p
    if p<0:
        return 0
    else:
        c=np.ones(n-p+1,dtype=int)
        for j in range(1,p+1):
            for k in range(1,n-p+1):
                c[k]+=c[k-1]
        return c[n-p]
    
def binom_c2(n,p):
    if n-p<p: p=n-p
    if p<0:
        return 0
    else:
        L=np.zeros(p+1,dtype=int)
        L[0]=1
        for i in range(1,n+1):
            for j in range(p,0,-1):
                L[j]+=L[j-1]
        return L[p]
    

print(binom_c2(30,15))
    

os.system("pause")