# -*- coding: utf-8 -*-

import os
import numpy
import timeit


def sample(n):
    return (rand(n) ** 2 + rand(n) ** 2 <= 1).sum()

n = 1000000.
4 * sample(n) / n

os.system("pause")
