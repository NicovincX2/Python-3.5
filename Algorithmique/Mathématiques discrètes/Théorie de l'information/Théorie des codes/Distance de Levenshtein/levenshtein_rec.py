# -*- coding: utf-8 -*-

import os
from collections import Counter

def call_counter(func):
    def helper(*args, **kwargs):
        helper.calls += 1
        key = str(args) + str(kwargs)
        helper.c[key] += 1
        return func(*args, **kwargs)
    helper.c = Counter()
    helper.calls = 0
    helper.__name__= func.__name__
    return helper
@call_counter
def LD(s, t):
    if s == "":
        return len(t)
    if t == "":
        return len(s)
    if s[-1] == t[-1]:
        cost = 0
    else:
        cost = 1
       
    res = min([LD(s[:-1], t)+1,
               LD(s, t[:-1])+1, 
               LD(s[:-1], t[:-1]) + cost])
    return res
print(LD("Python", "Peithen"))
print("LD was called " + str(LD.calls) + " times!")
print(LD.c.most_common())

os.system("pause")