# -*- coding: utf-8 -*-

"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""

import os

def mul3and5(n):
    result = 0
    for num in range(1, n):
        if num%3 == 0 or num%5 == 0:
            result += num
    return result
      
def test_():
    assert(mul3and5(10) == 23)
    print(mul3and5(1000))
    print('Tests Passed!')
            
if __name__ == '__main__':
    test_()

os.system("pause")