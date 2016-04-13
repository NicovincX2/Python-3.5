# -*- coding: utf-8 -*-

import os

def find_int(i, l):
    """Find integer in a sorted list.
    Example: 4 in [1, 3, 4, 6, 7, 9] -> 2
    @param i integer to find.
    @param l sorted list.
    @returns index if found, None if not.
    """
    if l:
        p_idx = len(l) / 2
        p = l[p_idx]
        if i == p:
            return p_idx
        elif len(l) == 1:
            return
        elif i < p:
            res = find_int(i, l[:p_idx])
            if res:
                return res
        elif i > p:
            res = find_int(i, l[p_idx:])
            if res:
                return res + p_idx

os.system("pause")