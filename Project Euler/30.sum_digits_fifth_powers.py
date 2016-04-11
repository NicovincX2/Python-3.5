# -*- coding: utf-8 -*-

'''
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
    1634 = 1^4 + 6^4 + 3^4 + 4^4
    8208 = 8^4 + 2^4 + 0^4 + 8^4
    9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.
The sum of these numbers is 1634 + 8208 + 9474 = 19316.
Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
'''

import os

def digit_fifth_pow(n):
    lnum = []   
    for num in range(10**(2), 10**(n+2)):
        sum_here = 0
        num_str = str(num)
        for i in num_str:
            num_int = int(i)
            num_int_pow = num_int**n
            sum_here += num_int_pow 
        if sum_here == num:
            lnum.append(num)
    return lnum, sum(lnum)  

def main():
    import time
    start = time.time() 
    
    print(digit_fifth_pow(5))
    
    elapsed = (time.time() - start)
    print('Tests Passed!\n It took %s seconds to run them.' % (elapsed))   
                   
if __name__ == '__main__':
    main()

os.system("pause")