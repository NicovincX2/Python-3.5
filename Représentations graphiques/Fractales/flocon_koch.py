#-*- coding: utf-8 -*-

from turtle import *
import os

def koch(n, longueur):
    if n == 0:
        forward(longueur)
    else:
        koch(n-1,longueur/3)
        left(60)
        koch(n-1,longueur/3)
        right(120)
        koch(n-1,longueur/3)
        left(60)
        koch(n-1,longueur/3)


for i in range(10):
    penup()
    goto(-200, 70*i)
    pendown()
    koch(i,300)

mainloop()

os.system("pause")
