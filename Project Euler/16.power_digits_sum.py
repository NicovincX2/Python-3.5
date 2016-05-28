# -*- coding: utf-8 -*-

"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2^1000?
"""

import os


def power_digit_sum(n):
    number = str(2**n)
    sum_res = 0
    for i in number:
        sum_res += int(i)
    return sum_res


def test_():
    assert(power_digit_sum(15) == 26)
    print(power_digit_sum(1000))
    print('Tests Passed!')

if __name__ == '__main__':
    test_()

os.system("pause")
