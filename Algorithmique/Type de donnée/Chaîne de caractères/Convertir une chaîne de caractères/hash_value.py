# -*- coding: utf-8 -*-

import os


def hash_value(s, base):
    """Calculate the hash value of a string using base.
    Example: 'abc' = 97 x base^2 + 98 x base^1 + 99 x base^0
    @param s string to compute hash value for
    @param base base to use to compute hash value
    @return hash value
    """
    v = 0
    p = len(s) - 1
    for i in range(p + 1):
        v += ord(s[i]) * (base ** p)
        p -= 1

    return v

os.system("pause")
