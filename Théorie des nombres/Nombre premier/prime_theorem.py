# -*- coding: utf-8 -*-

import os
import fermat_little_theorem

def prob_prime(n):
    """evaluate the probability of an n-bit long integer to be prime"""
    count = 0
    sample_size = 10 ** 5
    for i in range(sample_size):
        p = randrange(2 ** (n - 1), 2 ** n - 1)
        count += is_prime(p)
    return count / sample_size

prob_prime(20)
1 / 20
(0.07423 - 0.05) / 0.05

os.system("pause")

