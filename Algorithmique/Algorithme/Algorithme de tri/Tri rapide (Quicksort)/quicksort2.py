# -*- coding: utf-8 -*-

import os
from time import perf_counter


def slowsort(lst):
    """quicksort of list lst"""
    if len(lst) <= 1:
        return lst
    pivot = lst[0]      # select first element from list
    smaller = [elem for elem in lst if elem < pivot]
    equal = [elem for elem in lst if elem == pivot]
    greater = [elem for elem in lst if elem > pivot]
    return slowsort(smaller) + equal + slowsort(greater)

import random


def quicksort(lst):
    """quicksort of list lst"""
    if len(lst) <= 1:
        return lst
    pivot = random.choice(lst)  # select a random element from list
    smaller = [elem for elem in lst if elem < pivot]
    equal = [elem for elem in lst if elem == pivot]
    greater = [elem for elem in lst if elem > pivot]
    return quicksort(smaller) + equal + quicksort(greater)

lst = [random.randint(0, 100) for i in range(100000)]
top = perf_counter()
slowsort(lst)
print(perf_counter() - top, ' s')
top = perf_counter()
quicksort(lst)
print(perf_counter() - top, ' s')

lst = [i for i in range(100)]
top = perf_counter()
slowsort(lst)
print(perf_counter() - top, ' s')
top = perf_counter()
quicksort(lst)
print(perf_counter() - top, ' s')

os.system("pause")
