# -*- coding: utf-8 -*-

"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""

import os
from findstprime import is_prime
   
def summation_primes(n):
    candidate = 2
    prime_set = set()
    while candidate < n:    
        if is_prime(candidate, prime_set):
            prime_set.add(candidate)
        candidate +=1 
    return sum(prime_set)              

def main():
    assert(summation_primes(10) == 17)
    print(summation_primes(2000000))
    print('Tests Passed!')
                   
if __name__ == '__main__':
    main()

os.system("pause")