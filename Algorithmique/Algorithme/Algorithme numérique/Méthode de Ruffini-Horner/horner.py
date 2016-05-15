# -*- coding: utf-8 -*-

import os

def HornerI(p,x):
    n=len(p)-1
    y=p[n]
    for i in range(1,n+1):
        y*=x
        y+=p[n-i]
    return y

def HornerR(p,x):
    if len(p)==1:
        return p[0]
    else:
        return p[0]+x*HornerR(p[1:],x)

p,x=[1,2,3,4,5,6,7],3

print(HornerI(p,x))
print(HornerR(p,x))

os.system("pause")