# -*- coding: utf-8 -*-

"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

import os

def special_pyt(n):
    for i in range(3, n):
        for j in range(i+1, n):
            c = calc_c(i,j)
            if i + j + c == n: 
                return i*j*c

def calc_c(a, b):
    return (a**2 + b**2)**0.5

def main():
    assert(special_pyt(3+4+5) == (3*4*5))
    print(special_pyt(1000))
    print('Tests Passed!')
                   
if __name__ == '__main__':
    main()

os.system("pause")