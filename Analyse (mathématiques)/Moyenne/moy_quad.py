# -*- coding: utf-8 -*-

import os

from math import sqrt


def qmean(num):
    return sqrt(sum(n * n for n in num) / len(num))

qmean(range(1, 11))

os.system("pause")
