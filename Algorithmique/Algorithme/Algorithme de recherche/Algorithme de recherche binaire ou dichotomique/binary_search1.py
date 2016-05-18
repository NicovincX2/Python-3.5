# -*- coding: utf-8 -*-

import os
from merge_sort import merge_sort

def search(arr, item):
    """Performs binary search on an array
    with the given item and returns True or
    False.
>>> search([5, 4, 1, 6, 2, 3, 9, 7], 2)
    True
>>> search([5, 4, 1, 6, 2, 3, 9, 7], 8)
    False
    """

    arr1 = merge_sort(arr)

    first = 0
    last = len(arr1) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if arr1[midpoint] == item:
            found = True
        else:
            if item < arr1[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    return found


print (search([5, 4, 1, 6, 2, 3, 9, 7], 2))
print (search([5, 4, 1, 6, 2, 3, 9, 7], 8))

os.system("pause")