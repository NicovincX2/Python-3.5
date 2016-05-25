# -*- coding: utf-8 -*-

import os

#   Dragon curve using L-system
#   Authour:Alan Richmond, Python3.codes
#   https://en.wikipedia.org/wiki/L-system

from turtle import*

def X(n):
    if n>0:    L("X+YF+",n)
def Y(n):
    if n>0:    L("-FX-Y",n)
    
def L(s,n):
    for c in s:
        if   c=='-': lt(90)
        elif c=='+': rt(90)
        elif c=='X': X(n-1)
        elif c=='Y': Y(n-1)
        elif c=='F': fd(16)
            
X(8)

os.system("pause")