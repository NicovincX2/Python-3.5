# -*- coding: utf-8 -*-

import os


def fib_gen(n):
    """Generator for Fibonacci serie.
    Example: for i in fib_gen(5): print i
    @param n fib range upper bound
    """
    if not n:
        return
    a, b = 0, 1
    yield a
    i = 0
    while i < n - 1:
        yield b
        a, b = b, a + b
        i += 1

for i in fib_gen(5):
    print(i)

os.system("pause")
