# -*- coding: utf-8 -*-

import os

from math import sqrt
from time import perf_counter

def estPremier(n):
    if n%2 == 0: return 0
    for d in range(3,1+int(sqrt(n)),2):
        if n%d == 0: return 0
    return 1
    
def petitsPremiers(n):
    global premier
    premier=[2]
    for p in range(3,n+1,2):
        if estPremier(p) == 1:
            premier.append(p)
    return len(premier)
    
def estPremier2(p):
    global premier
    r=int(sqrt(p))
    for d in premier:
       if p%d == 0: return 0
       if d > r: return 1
    return 1
    
def petitsPremiers2(n):
    global premier
    premier=[2]
    for p in range(3,n+1,2):
        if estPremier2(p) == 1:
            premier.append(p)
    return len(premier)
    
def petitsPremiers2bis(n):
    def estPremier2bis(p):
        r=int(sqrt(p))
        for d in premier:
            if p%d == 0: return 0
            if d > r: return 1
        return 1
    premier=[2]
    for p in range(3,n+1,2):
        if estPremier2bis(p) == 1:
            premier.append(p)
    return len(premier)

def petitsPremiers3(n):
    global premier
    coche=[False]*(n+1)
    c1=1;fini=False
    while not fini:
        c1 += 1
        while c1<=n and coche[c1]: c1+=1
        c2=c1+c1;fini=True
        while c2<=n:
            if not coche[c2]:
                coche[c2]=True;fini=False
            c2+=c1
    premier=[]
    for i in range(2,n+1):
        if not coche[i]:premier.append(i)
    return len(premier)
                
def factoriser(n):
    global premier,facteur
    i=petitsPremiers3(n)
    m=n;i=0;facteur=[]
    while m>1:
        p=premier[i]
        while m%p==0:
            facteur.append(p)
            m=m//p
        i+=1
    return len(facteur)

def factoriser2(n):
    global facteur
    m=n;facteur=[]
    while m%2==0:
        facteur.append(2)
        m=m//2
    q=3
    while m>1:
        if q**2>m:
            facteur.append(m)
            return len(facteur)
        else:
            while m%q==0:
                facteur.append(q)
                m=m//q
        q+=2
    return len(facteur)

def calculerAlpha(n):
    global alpha
    m=n;alpha=[]
    a=0
    while m%2==0:
        a+=1
        m=m//2
    if a!=0: alpha.append(a)
    q=3
    while m>1:
        if q**2>m:
            alpha.append(1)
            return len(alpha)
        else:
            a=0
            while m%q==0:
                a+=1
                m=m//q
            if a!=0: alpha.append(a)
        q+=2
    return len(alpha)

def estPuissance(n,b):
    global alpha
    nb=calculerAlpha(n)
    for a in alpha:
        if a%b!=0: return 0
    return 1
    

def estCarmichael(c):
    m=c
    if m%2==0: return 0
    q=3
    while m>1:
        if q**2>m:
            if m==c:
                return 0
            elif (c-1)%(m-1)!=0:
                return 0
            else:
                return 1
        elif m%q==0:
            m=m//q
            if m%q==0 or (c-1)%(q-1)!=0: return 0
        q+=2
    return 1

def calculerCarmichael3(n):
    global premier,carmichael
    nb=petitsPremiers3(n-1)
    carmichael=[]
    for i1 in range(1,nb-2):
        p1=premier[i1]
        for i2 in range(i1+1,nb-1):
            p2=premier[i2]
            c2=p1*p2
            for i3 in range(i2+1,nb):
                p3=premier[i3]
                c=c2*p3
                if c<=n and (c-1)%(p1-1)==0 and (c-1)%(p2-1)==0 and (c-1)%(p3-1)==0:
                    carmichael.append(c)
    return len(carmichael)
    
def calculerCarmichael(n):
    global premier,carmichael
    nb=petitsPremiers3(int(sqrt(n))-1)
    t=list(range(n+1))
    for j in range(1,nb):
        p=premier[j];incr=p*(p-1)
        i=p**2
        while i<=n:
            t[i]=t[i]//p
            i+=incr
    carmichael=[]
    for j in range(3,n+1):
        if t[j]==1: carmichael.append(j)
    return len(carmichael)
            

top=perf_counter()
nb=calculerCarmichael3(5000)
print(perf_counter()-top)
top=perf_counter()
nb=calculerCarmichael(5000)
print(perf_counter()-top)

os.system("pause")