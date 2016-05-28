# -*- coding: utf-8 -*-

import os

x_bin = "11110"
x_bin = x_bin[::-1]  # reverse it so that LSB is on the left for the iteration
x_dec = 0
for k in range(len(x_bin)):
    bit = int(x_bin[k])
    print(k, bit)
    x_dec += bit * 2**k
print(x_dec)

x_dec = 42
x_bin = ''
while x_dec > 0:
    bit = x_dec % 2
    x_bin = str(bit) + x_bin
    x_dec = x_dec // 2
print(x_bin)

bin(42)
int('101010', 2)
hex(42)
int('2a', 16)

os.system("pause")
