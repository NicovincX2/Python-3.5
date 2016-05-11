# -*- coding: utf-8 -*-

import os
from math import cos,sin,pi
        
def arrondi(P):
    P=[round(z.real) for z in P]
    while P!=[] and P[-1]==0: P.pop()
    return P

def u(k,n):
    t=2*k*pi/n
    return complex(cos(t),sin(t))
    
def separe(t):
    t0,t1=[],[]
    i=0
    while i<len(t):
        t0.append(t[i]);i+=1
        t1.append(t[i]);i+=1
    return t0,t1
    
def z_wz(P,w):
    c=w
    for i in range(1,len(P)):
        P[i]*=c
        c*=w
    return P
    
def PtoY(P):
    if len(P)==1:
        return [P[0]]
    else:
        n=len(P);m=n//2
        P0,P1=separe(P)
        Y0=PtoY(P0);Y1=PtoY(P1)
        Y=n*[0]
        for j in range(m):
            tmp=u(j,n)*Y1[j]
            Y[j]=Y0[j]+tmp
            Y[m+j]=Y0[j]-tmp
        return Y

def YtoP(Y):
    if len(Y)==1:
        return [Y[0]]
    else:
        n=len(Y);m=n//2
        Y0,Y1=separe(Y)
        P0=YtoP(Y0);P1=YtoP(Y1)
        P1=z_wz(P1,u(-1,n))
        P=n*[0]
        for j in range(m):
            P[j]=0.5*(P0[j]+P1[j])
            P[m+j]=0.5*(P0[j]-P1[j])
        return P

def mult(A,B):
    dA=len(A)-1;dB=len(B)-1;d=dA+dB
    n=1
    while n<=d: n*=2
    for i in range(n-len(A)): A.append(0)
    for i in range(n-len(B)): B.append(0)
    YA=PtoY(A);YB=PtoY(B)
    return YtoP([YA[i]*YB[i] for i in range(n)])[:d+1]
    
print(arrondi(mult([1,2,1],[1,4,6,4,1])))

os.system("pause")