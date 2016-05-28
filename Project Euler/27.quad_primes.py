# -*- coding: utf-8 -*-

'''
Euler discovered the remarkable quadratic formula:
n² + n + 41
It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41² + 41 + 41 is clearly divisible by 41.
The incredible formula  n² − 79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79. The product of the coefficients, −79 and 1601, is −126479.
Considering quadratics of the form:
    n² + an + b, where |a| < 1000 and |b| < 1000
    where |n| is the modulus/absolute value of n
    e.g. |11| = 11 and |−4| = 4
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.
'''

import os


def quad_form(n, a, b):
    return n**2 + a * n + b


def isPrime(n):
    n = abs(int(n))
    if n < 2:
        return False
    if n == 2:
        return True
    if not n & 1:
        return False
    for x in range(3, int(n**0.5) + 1, 2):
        if n % x == 0:
            return False
    return True


def quad_primes(a, b):
    count_max = 0
    coef = ()
    for aa in range(-a, a):
        for bb in range(-b, b):
            n = 0
            while True:
                number = quad_form(n, aa, bb)
                if isPrime(number):
                    n += 1
                else:
                    if n > count_max:
                        count_max = n
                        coef = (aa, bb)
                    break
    return coef(0) * coef(1), coef


def main():
    import time
    start = time.time()

    print(quad_primes(1000, 1000))

    elapsed = (time.time() - start)
    print('Tests Passed!\n It took %s seconds to run them.' % (elapsed))

if __name__ == '__main__':
    main()

os.system("pause")
