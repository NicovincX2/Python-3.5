# -*- coding: utf-8 -*-

import os


def perm1(n):
    a = list(range(n))

    def sub(i):
        if i == n - 1:
            yield tuple(a)
        else:
            for k in range(i, n):
                a[i], a[k] = a[k], a[i]
                yield from sub(i + 1)
                a[i], a[k] = a[k], a[i]
    yield from sub(0)

for u in perm1(3):
    print(u)

os.system("pause")
