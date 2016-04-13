# -*- coding: utf-8 -*-

import os

from fractions import Fraction
 
def line(self, x0, y0, x1, y1):
    rev = reversed
    if abs(y1 - y0) <= abs(x1 - x0):
        x0, y0, x1, y1 = y0, x0, y1, x1
        rev = lambda x: x
    if x1 < x0:
        x0, y0, x1, y1 = x1, y1, x0, y0
    leny = abs(y1 - y0)
    for i in range(leny + 1):
        self.set(*rev((round(Fraction(i, leny) * (x1 - x0)) + x0, (1 if y1 > y0 else -1) * i + y0)))
 
Bitmap.line = line

bitmap = Bitmap(17,17)
for points in ((1,8,8,16),(8,16,16,8),(16,8,8,1),(8,1,1,8)):
    bitmap.line(*points)
bitmap.chardisplay()
 
'''
The origin, 0,0; is the lower left, with x increasing to the right,
and Y increasing upwards.
 
The chardisplay above produces the following output :
+-----------------+
|        @        |
|       @ @       |
|      @   @      |
|     @     @     |
|    @       @    |
|    @        @   |
|   @          @  |
|  @            @ |
| @              @|
|  @            @ |
|   @          @  |
|    @       @@   |
|     @     @     |
|      @   @      |
|       @ @       |
|        @        |
|                 |
+-----------------+
'''

os.system("pause")