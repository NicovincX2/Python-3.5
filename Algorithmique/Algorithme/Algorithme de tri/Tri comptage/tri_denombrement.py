# -*- coding: utf-8 -*-

import os
from random import randrange

def tab_alea(n,v_max):
    return [randrange(v_max) for k in range(n)]

def tri_den(t,val_max):
    occur=[0]*val_max
    for v in t:
        occur[v]+=1
    tt=[]
    for v in range(val_max):
        tt.extend([v]*occur[v])
    return tt
    

n=20
v_max=10
t=tab_alea(n,v_max)
print(t)
tt=tri_den(t,v_max)
print(tt)

os.system("pause")