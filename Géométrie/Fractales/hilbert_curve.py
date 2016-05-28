# -*- coding: utf-8 -*-

import os

#   Hilbert curve using L-system
#   Authour: Alan Richmond, Python3.codes
#   https://en.wikipedia.org/wiki/L-system
#   Uses Lindenmayer System

from turtle import*


def A(n):
    if n > 0:
        L("-BF+AFA+FB-", n)


def B(n):
    if n > 0:
        L("+AF-BFB-FA+", n)


def L(s, n):
    for c in s:
        if c == '-':
            lt(90)
        elif c == '+':
            rt(90)
        elif c == 'A':
            A(n - 1)
        elif c == 'B':
            B(n - 1)
        elif c == 'F':
            fd(9)

penup()
goto(0, -100)
pendown()
A(4)

os.system("pause")
