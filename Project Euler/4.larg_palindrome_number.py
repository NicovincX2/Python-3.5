# -*- coding: utf-8 -*-

"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""

import os


def is_palindrome(s):
    return s == reverse(s)


def reverse(s):
    rev = 0
    while s > 0:
        rev = 10 * rev + s % 10
        s = s // 10
    return rev


def is_palindrome_2(s):
    # to use it you need to cast str() first
    while s:
        if s[0] != s[-1]:
            return False
        else:
            s = s[1:-1]
            is_palindrome(s)
    return True


def larg_palind_product(n):
    nmax, largpal = 9, 0
    for i in range(1, n):
        nmax += 9 * 10**i
    for i in range(nmax, nmax // 2, -1):
        for j in range(i - 1, (i - 1) // 2, -1):
            candidate = i * j
            if is_palindrome(candidate) and candidate > largpal:
                largpal = candidate
    return largpal


def test_larg_palind_product():
    assert(larg_palind_product(2) == 9009)
    print(larg_palind_product(3))
    print('Tests Passed!')

if __name__ == '__main__':
    test_larg_palind_product()

os.system("pause")
