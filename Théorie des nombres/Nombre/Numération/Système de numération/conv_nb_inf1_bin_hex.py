# -*- coding: utf-8 -*-

import os


def decToBin(x, n):
    y = x
    s = "0b0."
    for k in range(n):
        y *= 2
        b = int(y)
        s += str(b)
        y -= b
    return s


def hstr(d):
    if d < 10:
        return str(d)
    elif d < 16:
        return chr(97 + d - 10)
    else:
        return (hstr(d // 16) + hstr(d % 16))


def decToHex(x, n):
    y = x
    s = "0x0."
    for k in range(n):
        y *= 16
        b = int(y)
        s += hstr(b)
        y -= b
    return s

print(hstr(1000))
print(decToBin(0.375, 10))
print(decToHex(0.90625, 3))

os.system("pause")
