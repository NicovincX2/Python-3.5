# -*- coding: utf-8 -*-

import os
from fermat_little_theorem import isPrime
from random import randrange

def prob_prime(n):
    """evaluate the probability of an n-bit long integer to be prime"""
    count = 0
    sample_size = 10 ** 5
    for i in range(sample_size):
        p = randrange(2 ** (n - 1), 2 ** n - 1)
        count += isPrime(p)
    return count / sample_size

print(prob_prime(20))
print(1 / 20)
print((0.07423 - 0.05) / 0.05)

os.system("pause")

