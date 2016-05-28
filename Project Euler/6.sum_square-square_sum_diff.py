# -*- coding: utf-8 -*-

"""
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

import os


def sum_square_diff(n):
    sq_sum, sum_sq = 0, 0
    for i in range(1, n + 1):
        sum_sq += i**2
        sq_sum += i
    sq_sum = sq_sum ** 2
    return sq_sum - sum_sq


def main():
    assert(sum_square_diff(10) == 2640)
    print(sum_square_diff(100))
    print('Tests Passed!')

if __name__ == '__main__':
    main()

os.system("pause")
