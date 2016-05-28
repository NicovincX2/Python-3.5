# -*- coding: utf-8 -*-

import os

a, b, c, s = " bottles of beer", " on the wall\n", "Take one down, pass it around\n", str
print("\n".join(s(x) + a + b + s(x) + a + "\n" + c +
                s(x - 1) + a + b for x in xrange(99, 0, -1)))

a = lambda n: "%u bottle%s of beer on the wall\n" % (n, "s"[n == 1:])
print("\n".join(a(x) + a(x)
                [:-13] + "\nTake one down, pass it around\n" + a(x - 1) for x in xrange(99, 0, -1)))

"""\
{0} {2} of beer on the wall
{0} {2} of beer
Take one down, pass it around
{1} {3} of beer on the wall
"""
print("\n".join(
    __doc__.format(
        i, i - 1,
        "bottle" if i == 1 else "bottles",
        "bottle" if i - 1 == 1 else "bottles"
    ) for i in range(99, 0, -1)
), end="")

os.system("pause")
