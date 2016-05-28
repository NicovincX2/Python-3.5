# -*- coding: utf-8 -*-

import os


def indeuler_recur(n):
    if (n == 1):
        return 1
    d = 2
    stop = n + 1
    while (d < stop):
        if ((n % (d * d)) == 0):
            return d * indeuler_recur(n / d)
        elif ((n % d) == 0):
            return (d - 1) * indeuler_recur(n / d)
        d = d + 1

print(indeuler_recur(1))
print(indeuler_recur(2))
print(indeuler_recur(8))

os.system("pause")
