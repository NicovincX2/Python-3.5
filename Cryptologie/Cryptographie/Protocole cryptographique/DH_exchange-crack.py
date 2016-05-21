# -*- coding: utf-8 -*-

import os
from random import randrange

def DH_exchange(p):
    """ generates a shared DH key """
    g = randrange(1,p-1)
    a = randrange(1,p-1) # Alice's secret
    b = randrange(1,p-1) # Bob's secret
    x = pow(g,a,p)
    y = pow(g,b,p)
    key_A = pow(y,a,p)
    key_B = pow(x,b,p)
    return g, a, b, x, y, key_A, key_B

DH_exchange(190125101)
DH_exchange(833648000993161193752610727299)

def crack_DH(p, g, x):
    """find secret "a" that satisfies g**a%p == x
    Not feasible for large p"""
    for a in range(1,p-1):
        if a % 100000 == 0:
            print("Iteration",a) # progress bar
        if pow(g,a,p) == x:
            return a
    return None

def is_prime(p):
    """probabilistic test for p's compositeness"""
    for i in range(100):
        a = randrange(1, p - 1) # a is a random integer in [1..p-1]
        if pow(a, p - 1, p) != 1: # this takes O(n^3) = O((log2 p)^3)
            return False
    return True # we get here if no compositeness witness was found

def find_prime(n):
    """ find random n-bit long prime (no leading zeros: 2**(n-1)<= N < 2**n )"""
    while True: #here we're optimistic, but actually we have a good reason to be:
                 # after O(1/n) iterations we expect to find a prime and halt
        candidate = randrange(2**(n - 1), 2**n)
        if is_prime(candidate):
            return candidate

from math import log

p = find_prime(10)
print(p,log(p,2))
g,a,b,x,y,key_A,key_B = DH_exchange(p)
print('g',g,'a',a,'b',b,'x',x,'y',y,'key_A',key_A,'key_B',key_B)
print('a',crack_DH(p,g,x))

p = find_prime(16)
print(p,log(p,2))
g,a,b,x,y,key_A,key_B = DH_exchange(p)
print('g',g,'a',a,'b',b,'x',x,'y',y,'key_A',key_A,'key_B',key_B)
print('a',crack_DH(p,g,x))

p = find_prime(128)
print(p,log(p,2))
g,a,b,x,y,key_A,key_B = DH_exchange(p)
print('g',g,'a',a,'b',b,'x',x,'y',y,'key_A',key_A,'key_B',key_B)
print('a',crack_DH(p,g,x))

os.system("pause")
