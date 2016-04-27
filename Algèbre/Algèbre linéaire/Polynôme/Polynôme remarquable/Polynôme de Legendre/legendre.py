# -*- coding: utf-8 -*-

import os
import scipy
from scipy.special import airy,jn,eval_chebyt,eval_legendre

subplot(2,2,4)
x = linspace(-1,1)
for i in range(6):
    plot(x,eval_legendre(i,x))
title("Legendre polynomials")
    
os.system("pause")