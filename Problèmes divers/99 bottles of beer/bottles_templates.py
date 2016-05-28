# -*- coding: utf-8 -*-

import os

verse = '''\
%i bottles of beer on the wall
%i bottles of beer
Take one down, pass it around
%i bottles of beer on the wall
'''

for bottles in range(99, 0, -1):
    print(verse % (bottles, bottles, bottles - 1))

verse = '''\
{some} bottles of beer on the wall
{some} bottles of beer
Take one down, pass it around
{less} bottles of beer on the wall
'''

for bottles in range(99, 0, -1):
    print(verse.format(some=bottles, less=bottles - 1))

os.system("pause")
