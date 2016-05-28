# -*- coding: utf-8 -*-

import os

"""
    Quick Sort
    ----------
    Uses partitioning to recursively divide and sort the list
    Time Complexity: O(n**2) worst case
    Space Complexity: O(n**2) this version
    Stable: No
    Psuedo Code: CLRS. Introduction to Algorithms. 3rd ed.
"""


def sort(seq):
    """
    Takes a list of integers and sorts them in ascending order. This sorted
    list is then returned.
    :param seq: A list of integers
    :rtype: A list of sorted integers
    """
    if len(seq) <= 1:
        return seq
    else:
        pivot = seq[0]
        left, right = [], []
        for x in seq[1:]:
            if x < pivot:
                left.append(x)
            else:
                right.append(x)
        return sort(left) + [pivot] + sort(right)

if __name__ == '__main__':
    array = [3, 1, 6, 0, 7, 19, 7, 2, 22]
    sorted = [0, 1, 2, 3, 6, 7, 7, 19, 22]
    assert(sort(array) == sorted)

    array = []
    assert(sort(array) == array)

    array = [1]
    assert(sort(array) == array)

os.system("pause")
