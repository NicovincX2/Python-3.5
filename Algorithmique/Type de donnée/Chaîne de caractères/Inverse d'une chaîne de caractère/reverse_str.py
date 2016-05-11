# -*- coding: utf-8 -*-

import os

__author__ = "bt3"

def reverse_str_inplace(_str):
    if len(_str) < 2:
        return _str
    return _str[-1] + reverse_str(_str[1:-1]) + _str[0]
    
def reverse_str(_str):
    result = ''
    j = len(_str) - 1

    while j >= 0:
        result += _str[j]
    
    return result
    
if __name__ == '__main__':
    _str = ''
    result = ''
    assert(reverse_str(_str) == result)
    assert(reverse_str_inplace(_str) == result)

    _str1 = 'a'
    result1 = 'a'
    #assert(reverse_str(_str1) == result1)
    #assert(reverse_str_inplace(_str1) == result1)

    _str2 = 'abcde'
    result2 = 'edcba'
    #assert(reverse_str(_str2) == result2)
    #assert(reverse_str_inplace(_str2) == result2)

    _str3 = 'abcdef'
    result3 = 'fedcba'
    #assert(reverse_str(_str3) == result3)
    #assert(reverse_str_inplace(_str3) == result3)

os.system("pause")