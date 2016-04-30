# -*- coding: utf-8 -*-

import os
from timeit import Timer

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
    pivot = random.choice(lst) # select a random element from list
    smaller = [elem for elem in lst if elem < pivot]
    equal = [elem for elem in lst if elem == pivot]
    greater = [elem for elem in lst if elem > pivot]
    return quicksort(smaller) + equal + quicksort(greater)

lst = [random.randint(0,100) for i in range(100000)]
t1 = Timer(lambda: slowsort(lst))
t2 = Timer(lambda: quicksort(lst))
t1.timeit()
t2.timeit()

lst = [i for i in range(100)]
t3 = Timer(lambda: slowsort(lst))
t4 = Timer(lambda: quicksort(lst))
t3.timeit()
t4.timeit()

os.system("pause")
