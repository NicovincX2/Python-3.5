# -*- coding: utf-8 -*-

import os


def count_change(amount, coins):
    if amount == 0:
        return 1
    if amount < 0 or len(coins) == 0:
        return 0
    without_large_coint = count_change(amount, coins[:-1])
    with_large_coin = count_change(amount - coins[-1], coins)
    return without_large_coint + with_large_coin

count_change(5, [1, 2, 3])

os.system("pause")
