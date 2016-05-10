# -*- coding: utf-8 -*-

import os

def fib1(n,a=1,b=1):
    if n==0:
        return a
    elif n==1:
        return b
    else:
        for k in range(n-1):
            a,b=b,a+b
        return b
    
def fib(n,a=1,b=1):
    if n==0:
        return a
    elif n==1:
        return b
    else:
        return fib(n-1,b,a+b)

def fib2(n,a=1,b=1):
    if n==0:
        return a
    elif n==1:
        return b
    else:
        return fib2(n-1,a,b)+fib2(n-2,a,b)
    
def fib_mem(n,a=1,b=1):
    table={0:a,1:b}
    def fibo(n):
        if n in table:
            return table[n]
        else:
            table[n]=fibo(n-1)+fibo(n-2)
            return table[n]
    return fibo(n)

from time import perf_counter

n=50

top=perf_counter()
print(fib1(n,1,1))
print(perf_counter()-top)

top=perf_counter()
print(fib_mem(n,1,1))
print(perf_counter()-top)

os.system("pause")