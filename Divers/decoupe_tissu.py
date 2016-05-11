# -*- coding: utf-8 -*-

import os

def coutRuban2Produits(a0,v0,a1,v1,L):
    Mmax=0;
    for k0 in range(L//a0+1):
        k1=(L-k0*a0)//a1
        M=k0*v0+k1*v1
        if M>Mmax:
            Mmax=M
    return Mmax
    
def coutRuban3Produits(a0,v0,a1,v1,a2,v2,L):
    Mmax=0;
    for k0 in range(L//a0+1):
        k1=(L-k0*a0)//a1
        M=k0*v0+coutRuban2Produits(a1,v1,a2,v2,L-k0*v0)
        if M>Mmax:
            Mmax=M
    return Mmax

def coutRuban(a,v,n,L):
    M=[0]*(L+1)
    for x in range(1,L+1):
        for i in range(n):
            if a[i]<=x:
                Mi=v[i]+M[x-a[i]]
                if Mi>M[x]:
                    M[x]=Mi
    return M[L]
    
def decoupageRuban(a,v,n,L):
    M=[0]*(L+1)
    D=[-1]*(L+1)
    for x in range(1,L+1):
        for i in range(n):
            if a[i]<=x:
                Mi=v[i]+M[x-a[i]]
                if Mi>M[x]:
                    M[x]=Mi;D[x]=i
    x=L;decoupe=[]
    while D[x]>=0:
        decoupe.append(D[x])
        x -= a[D[x]]
    return decoupe

def coutRubanSansRepetitions(a,v,n,L):
    M=[[0]*(L+1)]*(n+1)
    for i in range(n):
        for x in range(L+1):
            if a[i]>x:
                M[i+1][x]=M[i][x]
            else:
                M[i+1][x]=max(v[i]+M[i][x-a[i]],M[i][x])
    return M[n][L]
                    
def coutRubanSansRepetitionsV2(a,v,n,L):
    M=[[0]*(L+1)]*2
    ic=0
    for i in range(n):
        ip=ic;ic=1-ip
        for x in range(L+1):
            if a[i]>x:
                M[ic][x]=M[ip][x]
            else:
                M[ic][x]=max(v[i]+M[ip][x-a[i]],M[ip][x])
    return M[ic][L]
    
print(coutRubanSansRepetitionsV2([6,8,10],[4,5,7],3,17))

os.system("pause")