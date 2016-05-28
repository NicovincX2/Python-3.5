# -*- coding: utf-8 -*-

import os
import random
import matplotlib

npts = 5000
xs = 2 * rand(npts) - 1
ys = 2 * rand(npts) - 1
r = xs**2 + ys**2
ninside = (r < 1).sum()
figsize(6, 6)  # make the figure square
title("Approximation to pi = %f" % (4 * ninside / float(npts)))
plot(xs[r < 1], ys[r < 1], 'b.')
plot(xs[r > 1], ys[r > 1], 'r.')
figsize(8, 6)  # change the figsize back to 4x3 for the rest of the notebook

os.system("pause")
