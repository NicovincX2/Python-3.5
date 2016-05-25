# -*- coding: utf-8 -*-

import os

from turtle import*
def K(s):
    if s>10:
        for a in[60,-120,60,0]:K(s/3);lt(a)
    else:fd(s)
for i in range(3):K(400);rt(120)

os.system("pause")