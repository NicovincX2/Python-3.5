# -*- coding: utf-8 -*-

import os
import scipy
from scipy.special import airy, jn, eval_chebyt, eval_legendre

subplot(2, 2, 3)
x = linspace(-1, 1)
for i in range(6):
    plot(x, eval_chebyt(i, x))
title("Chebyshev polynomials of the first kind")

os.system("pause")
