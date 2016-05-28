# -*- coding: utf-8 -*-

import os
import scipy
from scipy.special import airy, jn, eval_chebyt, eval_legendre

subplot(2, 2, 1)
x = linspace(-1, 1)
Ai, Aip, Bi, Bip = airy(x)
plot(x, Ai)
plot(x, Aip)
plot(x, Bi)
plot(x, Bip)
title("Airy functions")

os.system("pause")
