# -*- coding: utf-8 -*-

import os

try:
    raw_input
except:
    raw_input = input

print(sum(map(int, raw_input().split())))

import sys

for line in sys.stdin:
    print(sum(map(int, line.split())))

os.system("pause")
