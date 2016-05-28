# -*- coding: utf-8 -*-

import os


def selection_sort(lst):
    for i, e in enumerate(lst):
        mn = min(range(i, len(lst)), key=lst.__getitem__)
        lst[i], lst[mn] = lst[mn], e
    return lst

os.system("pause")
