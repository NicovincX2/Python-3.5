# -*- coding: utf-8 -*-

import os

"""
Implementation of Sieve of Eratosthenes algorithm to generate all the primes upto N.
Algorithm :
 * We have a list of numbers from 1 to N.
 * Initially, all the numbers are marked as primes.
 * We go to every prime number in the list (<= N ^ 1/2) and mark all the multiples 
   of this prime number which are bigger than the number itself as non-primes.
"""

from math import sqrt, ceil


def generate_primes(n):
    # start with all values as True, except 0 and 1
    bool_array = [False, False] + [True] * n
    for i in range(2, int(ceil(sqrt(n)))):                # only go to till square root of n
        if bool_array[i]:                                 # if the number is marked as prime
            # iterate through all its multiples
            for j in range(i * i, n + 1, i):
                # and mark them as False
                bool_array[j] = False
    # return all numbers which are marked as True
    primes = [i for i in range(n + 1) if bool_array[i]]
    return primes

os.system("pause")
