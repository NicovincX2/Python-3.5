# -*- coding: utf-8 -*-

import os
from turtle import*

def T(l):
    if l>4:pensize(l/6);fd(l);rt(33);T(l*.7);lt(66);T(l*.7);rt(33);bk(l)
seth(90)
goto(0,-99)
T(99)

os.system("pause")