# -*- coding: utf-8 -*-

import os

import fibo_example

fibo_example.fib(1000)

fibList = fibo_example.fib2(100)

print(fibList)

# can assign the function name to a variable to make it easier to call
f = fibo_example.fib2
print(f(100))


# find out the names that a module defines
print(dir(fibo_example))

os.system("pause")
