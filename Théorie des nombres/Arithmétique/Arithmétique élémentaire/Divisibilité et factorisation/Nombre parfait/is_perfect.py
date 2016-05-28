# -*- coding: utf-8 -*-

import os


def is_perfect(n):
    '''
    is_perfect(integer) -> bool
    Return True iff n equals the sum of its divisors
    '''
    return n == sum(divisors(n))

help(is_perfect)


def divisors(n):
    '''
    divisors(integer) -> list of integers
    Return the proper divisors of n (numbers less than n that divide evenly into n).
    '''
    return [div for div in range(1, n) if n % div == 0]

print("perfect numbers in range(1,1000)\n")
print([n for n in range(1, 1001) if is_perfect(n)])

os.system("pause")
