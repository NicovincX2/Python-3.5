# -*- coding: utf-8 -*-

import os
from random import randrange


def is_prime(p):
    """probabilistic test for p's compositeness"""
    for i in range(100):
        a = randrange(1, p - 1)  # a is a random integer in [1..p-1]
        if pow(a, p - 1, p) != 1:  # this takes O(n^3) = O((log2 p)^3)
            return False
    return True  # we get here if no compositeness witness was found

is_prime(11)
is_prime(190125101)

os.system("pause")
