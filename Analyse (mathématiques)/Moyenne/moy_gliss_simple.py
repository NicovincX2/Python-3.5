# -*- coding: utf-8 -*-

import os

from collections import deque


def simplemovingaverage(period):
    assert period == int(period) and period > 0, "Period must be an integer >0"

    summ = n = 0.0
    values = deque([0.0] * period)     # old value queue

    def sma(x):
        nonlocal summ, n

        values.append(x)
        summ += x - values.popleft()
        n = min(n + 1, period)
        return summ / n

    return sma

if __name__ == '__main__':
    for period in [3, 5]:
        print("\nSIMPLE MOVING AVERAGE (procedural): PERIOD =", period)
        sma = simplemovingaverage(period)
        for i in range(1, 6):
            print("  Next number = %-2g, SMA = %g " % (i, sma(i)))
        for i in range(5, 0, -1):
            print("  Next number = %-2g, SMA = %g " % (i, sma(i)))
    for period in [3, 5]:
        print("\nSIMPLE MOVING AVERAGE (class based): PERIOD =", period)
        sma = Simplemovingaverage(period)
        for i in range(1, 6):
            print("  Next number = %-2g, SMA = %g " % (i, sma(i)))
        for i in range(5, 0, -1):
            print("  Next number = %-2g, SMA = %g " % (i, sma(i)))

os.system("pause")
