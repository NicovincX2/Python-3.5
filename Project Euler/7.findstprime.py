# -*- coding: utf-8 -*-

"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""

import os
import math
   
def is_prime(number, prime_set):
    if number in prime_set: return True
    for i in range(2, int(math.sqrt(number)) + 1):
        if not number%i: return False
    return True
    
def findstprime(n):
    count = 0
    candidate = 1
    prime_set = set()
    while count < n: 
        candidate +=1 
        if is_prime(candidate, prime_set):
            prime_set.add(candidate)
            count += 1       
    return candidate

def main():
    assert(findstprime(6 == 13))
    print(findstprime(10001))
    print('Tests Passed!')
                   
if __name__ == '__main__':
    main()

os.system("pause")