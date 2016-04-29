# -*- coding: utf-8 -*-

import os
import timeit

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

lst = [random.randint(0,100) for _ in range(100000)]
timeit -n 10 slowsort(lst)
timeit -n 10 quicksort(lst)

lst = [i for i in range(100)]
timeit -n 10 slowsort(lst)
timeit -n 10 quicksort(lst)

os.system("pause")

