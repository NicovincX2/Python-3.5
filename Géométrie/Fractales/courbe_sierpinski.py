# -*- coding: utf-8 -*-

import os
from turtle import*

def S(n,s):
    if n:n-=1;S(n,-s);lt(s*60);S(n,s);lt(s*60);S(n,-s)
    else:fd(2)
lt(60);S(7,1)

os.system("pause")