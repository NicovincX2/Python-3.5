# -*- coding: utf-8 -*-

import os

"""
    Approximate Cumulative Distribution Function
    --------------------------------------------
    Calculates the cumulative distribution function (CDF)
    of the normal distribution based on an approximation by George Marsaglia:
    Marsaglia, George (2004). "Evaluating the Normal Distribution".
    Journal of Statistical Software 11 (4).
    16 digit precision for 300 iterations when x = 10.
    Equation:
    f(x) = 1/2 + pdf(x) * (x + (x^3/3) + (x^5/3*5) + (x^7/3*7) + ...)
"""

"""
    Standard Normal Probability Density Function
    --------------------------------------------
    Calculates the normal distribution's probability density
    function (PDF).
    Calculates Standard normal pdf for mean=0, std_dev=1.

    Equation:
    f(x) = 1 / sqrt(2*pi) * e^(-(x-mean)^2/ 2*std_dev^2)
"""


def pdf(x, mean=0, std_dev=1):
    """
    Calculates the normal distribution's probability density
    function.

    :param x: An integer.
    :param mean: An integer.
    :param std_dev: An integer.
    :rtype: The normal distribution
    """
    PI = 3.141592653589793
    E = 2.718281828459045
    term1 = 1.0 / ((2 * PI)**0.5)
    term2 = E**(-1.0 * (x - mean)**2.0 / 2.0 * (std_dev**2.0))

    return term1 * term2


def cdf(x, iterations=300):
    """
    Calculates the cumulative distribution function of the normal distribution.
    Uses a taylor exponent to calculate this.
    :param x: An integer that represents the taylor exponent.
    :param iterations: An integer representing the number of iterations.
    :rtype: The normal distribution
    """
    product = 1.0
    taylor_exp = [x]
    for i in range(3, iterations, 2):
        product *= i
        taylor_exp.append(float(x**i) / product)
    taylor_fact = sum(taylor_exp)

    return (0.5 + (taylor_fact * pdf(x, mean=0, std_dev=1)))

os.system("pause")
