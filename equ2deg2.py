#-*- coding: utf-8 -*-

import os

def equ2deg(a,b,c):
    import math
    if a==0:
        print ('a doit être différent de 0')
    else:
        D = -(4*a*c)+b**2
        print ('Delta =',D)
        if D==0:
            print ('Il existe donc une solution:')
            print ('x=', -b/2*a)
        elif D<0:
            print ('Delta < 0')
            print ('Il n\'existe donc pas de solution.')
        else:
            x1 = -b-math.sqrt(D)/(2*a)
            x2 = -b+math.sqrt(D)/(2*a)
            print ('Delta > 0')
            print ('Il existe donc deux solutions:')
            print ('x1=', x1)
            print ('x2=', x2)
            if x1!=int(x1):
                print ('x1=', '(', -b, '- racine carrée de', D, ')/', 2*a)
                print ('x2=', '(', -b, '+ racine carrée de', D, ')/', 2*a)

equ2deg(3,5,2)
equ2deg(10,20,5)
equ2deg(5,6,8)

os.system("pause")
