# -*- coding: utf-8 -*-

import os

def fact(n):
    result=1
    for k in range(2,n+1) :
        result=result*k
    return result
    
print(fact(5))

os.system("pause")