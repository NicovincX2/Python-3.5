# -*- coding: utf-8 -*-

import os

m = 100  # integer to apply the conjecture on

n = m
while n != 1:
    print(n, end=", ")
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
print(1)  # 1 was not printed
print(m, "is OK")

limit = 10
m = 1
while m <= limit:
    n = m
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    print(m, "is OK")
    m += 1

start, stop = 99, 110
for m in range(start, stop + 1):
    n = m
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    print(m, "is OK")

os.system("pause")
