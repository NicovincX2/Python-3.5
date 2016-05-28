# -*- coding: utf-8 -*-

"""
n! means n × (n − 1) × ... × 3 × 2 × 1
For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800, and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
Find the sum of the digits in the number 100!
"""

import os


def factorial(n):
    prod = 1
    for i in range(1, n):
        prod *= i
    return prod


def find_sum(n):
    sum_ = 0
    fact = factorial(n)
    number = str(fact)
    for i in number:
        sum_ += int(i)
    return sum_


def main():
    import time
    start = time.time()

    assert(find_sum(10) == 27)
    print(find_sum(100))

    elapsed = (time.time() - start)
    print('Tests Passed!\n It took %s seconds to run them.' % (elapsed))

if __name__ == '__main__':
    main()

os.system("pause")
