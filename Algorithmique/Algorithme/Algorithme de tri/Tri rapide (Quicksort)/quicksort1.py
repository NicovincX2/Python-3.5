# -*- coding: utf-8 -*-

import os

def quicksort(l):
    """Sort list using quick sort.
    Complexity: O(n log n).  Worst: O(n2)
    @param l list to sort.
    @returns sorted list.
    """
    if len(l) <= 1:
        return l

    pivot = l[0]
    less = []
    equal = []
    greater = []
    for e in l:
        if e < pivot:
            less.append(e)
        elif e == pivot:
            equal.append(e)
        else:
            greater.append(e)

    return quicksort(less) + equal + quicksort(greater)

if __name__ == '__main__':
    array = [3, 1, 6, 0, 7, 19, 7, 2, 22]
    sorted = [0, 1, 2, 3, 6, 7, 7, 19, 22]
    assert(quicksort(array) == sorted)
    
    array = []
    assert(quicksort(array) == array)

    array = [1]
    assert(quicksort(array) == array)

os.system("pause")