# -*- coding: utf-8 -*-

import os


def merge_sort(l):
    """Sort list using merge sort.
    Complexity: O(n log n)
    @param l list to sort.
    @returns sorted list.
    """
    def merge(l1, l2):
        """Merge sorted lists l1 and l2.
        [1, 2, 4], [1, 3, 4, 5] -> [1, 1, 2, 3, 4, 5]
        @param l1 sorted list
        @param l2 sorted list
        @returns merge sorted list
        """
        res = []
        i = 0
        j = 0
        while i < len(l1) and j < len(l2):
            if l1[i] <= l2[j]:
                res.append(l1[i])
                i += 1
            elif l2[j] < l1[i]:
                res.append(l2[j])
                j += 1

        while i < len(l1):
            res.append(l1[i])
            i += 1

        while j < len(l2):
            res.append(l2[j])
            j += 1

        return res

    length = len(l)
    if length <= 1:
        return l
    mid = length // 2
    h1 = merge_sort(l[:mid])
    h2 = merge_sort(l[mid:])

    return merge(h1, h2)

if __name__ == '__main__':
    array = [3, 1, 6, 0, 7, 19, 7, 2, 22]
    sorted = [0, 1, 2, 3, 6, 7, 7, 19, 22]
    assert(merge_sort(array) == sorted)

    array = []
    assert(merge_sort(array) == array)

    array = [1]
    assert(merge_sort(array) == array)

os.system("pause")
