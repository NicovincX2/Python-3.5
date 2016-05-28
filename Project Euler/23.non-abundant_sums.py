# -*- coding: utf-8 -*-

'''
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
'''

import os


def find_sum_proper_div(n):
    sum_proper_div = 0
    for i in range(1, n):
        if n % i == 0:
            sum_proper_div += i
    return sum_proper_div


def find_all_abund(n):
    sum_div_list = [find_sum_proper_div(i) for i in range(n)]
    abu = set()
    for i in range(n):
        if i < sum_div_list[i]:
            abu.add(i)
    return abu


def non_abund_sums(n):
    abu = find_all_abund(n)
    sum_nom_abu = 0

    for i in range(n):
        if not any((i - a in abu) for a in abu):
            sum_nom_abu += i

    return sum_nom_abu


def test_():
    r = set([i for i in range(25)])
    r_abu = {24}
    r = r - r_abu
    assert(non_abund_sums(25) == sum(r))
    print(non_abund_sums(28123))
    print('Tests Passed!')

if __name__ == '__main__':
    test_()

os.system("pause")
