# -*- coding: utf-8 -*-

import os

def bitwise(a, b):
        print 'a and b:', a & b
        print 'a or b:', a | b
        print 'a xor b:', a ^ b
        print 'not a:', ~a
        print 'a << b:', a << b # left shift
        print 'a >> b:', a >> b # arithmetic right shift
        
        print 'a and b:', a and b
        print 'a or b:' , a or b
        print 'not a:'  , not a
        
# 8-bit bounded shift:
x = x << n & 0xff
# ditto for 16 bit:
x = x << n & 0xffff
# ... and 32-bit:
x = x << n & 0xffffffff
# ... and 64-bit:
x = x << n & 0xffffffffffffffff

os.system("pause")