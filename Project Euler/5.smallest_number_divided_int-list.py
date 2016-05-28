# -*- coding: utf-8 -*-

"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

import os


def smallest_multiple(n):
    set1 = set([x for x in range(1, n + 1)])
    set2 = set()
    for i in range(len(set1), 0, -1):
        for j in range(1, i):
            if i % j == 0:
                set2.add(j)
    set1 = set1 - set2
    res_num = n * n
    while True:
        for i in set1:
            missing_div = False
            if res_num % i:
                missing_div = True
                shift = res_num % i
                break
        if not missing_div:
            return res_num
        res_num += 1 or shift
        shift = 0


def test_():
    assert(smallest_multiple(10) == 2520)
    print(smallest_multiple(20))
    print('Tests Passed!')

if __name__ == '__main__':
    test_()

os.system("pause")
