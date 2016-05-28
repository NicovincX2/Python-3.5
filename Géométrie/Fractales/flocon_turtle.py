# -*- coding: utf-8 -*-

import os
from turtle import *


def flocon(a):
    if a > 5:
        flocon(a / 3)
        left(60)
        flocon(a / 3)
        right(120)
        flocon(a / 3)
        left(60)
        flocon(a / 3)
    else:
        forward(a)

speed(0)
a = 400
flocon(a)
right(120)
flocon(a)
right(120)
flocon(a)
hideturtle()


os.system("pause")
