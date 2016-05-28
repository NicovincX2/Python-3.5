# -*- coding: utf-8 -*-

"""
    This module calculates the machine precision
    Marina von Steinkirch (based on Mike Zingale's code), spring 2013.
"""

import os


def calculatePrecision():

    x = 1.0
    epsilon = 1.0

    while (not x + epsilon == x):
        epsilon = epsilon / 2.0

    return 2 * epsilon

os.system("pause")
