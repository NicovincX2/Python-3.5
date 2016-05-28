#-*- coding: utf-8 -*-

# http://codes-sources.commentcamarche.net/source/view/42267/1099070#browser
# https://fr.wikipedia.org/wiki/Arbre_de_Pythagore

from turtle import *
from math import radians, cos, sin
import os


def arbre(n, t, a):
    if n == 1:
        left(90)
        forward(t)
        right(90 - a)
        forward(t * cos(radians(a)))
        right(90)
        forward(t * sin(radians(a)))
        right(a)
        forward(t)
    else:
        left(90)
        forward(t)
        right(90 - a)
        n1 = n - 1
        d1 = t * cos(radians(a))
        arbre(n1, d1, a)
        d2 = t * sin(radians(a))
        arbre(n1, d2, a)
        left(90 - a)
        forward(t)


up()
forward(150)
right(90)
forward(250)
left(90)
down()
arbre(14, 45, 30)

os.system("pause")
