# -*- coding: utf-8 -*-

import os

def convert_base(n,b):
    '''convert_base(integer, integer) -> string
    Return the textual representation of n (decimal) in base 2 <= b <= 10.
    '''
    result = ''
    while n > 0:
        digit = n % b
        n = n // b
        print(digit)
        result = str(digit) + result
    return result

convert_base(23,12)
convert_base(10,16)
	
def convert_base1(n,b):
    '''convert_base(integer, integer) -> string
    Return the textual representation of n (decimal) in base 2 <= b <= 10.
    '''
    assert 2 <= b <= 36
    
    if n == 0:
        result = '0'
    elif n < 0:
        result = '-'
    else:
        result = ''
    n = abs(n)
    while n > 0:
        digit = n % b
        n = n // b
        # str(digit) only works for b <= 10
        result = '0123456789abcdefghijklmnopqrstuvwxyz'[digit] + result 
    return result

convert_base1(23,12)
convert_base1(10,6)
convert_base1(10,16)
convert_base1(40,32)
convert_base1(0,5)
convert_base1(100,55)

os.system("pause")

