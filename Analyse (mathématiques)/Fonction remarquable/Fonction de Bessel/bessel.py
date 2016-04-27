# -*- coding: utf-8 -*-

import os
import scipy
from scipy.special import airy,jn,eval_chebyt,eval_legendre

subplot(2,2,2)
x = linspace(0,10)
for i in range(4):
    plot(x,jn(i,x))
title("Bessel functions")
    
os.system("pause")