# -*- coding: utf-8 -*-

import os

def hanoi(n,D,I,A):
    if n>0:
        hanoi(n-1,D,A,I)
        print(D,"->",A)
        hanoi(n-1,I,D,A)

hanoi(3,1,2,3)

os.system("pause")