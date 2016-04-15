# -*- coding: utf-8 -*-

import os

def str_to_int(s):
    """Convert string to integer without doing int(s).
    '123' -> 123
    @param s string to convert.
    @returns integer
    """
    if not s:
        raise ValueError
    i = 0
    idx = 0
    neg = False
    if s[0] == '-':
        neg = True
        idx += 1

    for c in s[idx:]:
        i *= 10
        i += int(c)

    if neg:
        i = -i

    return i

os.system("pause")