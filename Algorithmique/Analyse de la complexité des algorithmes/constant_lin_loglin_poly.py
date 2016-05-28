# -*- coding: utf-8 -*-

import os
from math import log
import matplotlib

domain = range(1, 100)
const = [10 for x in domain]
lin = [x for x in domain]
loglin = [x * log(x) for x in domain]
poly = [x ** 2 for x in domain]

# these lines are the plotting directives
fig = figure(figsize=(16, 6))
ax = subplot(1, 3, 1)
ax.plot(domain, const)
ax.plot(domain, lin)
ax.legend(["const", "lin"], loc=2)
ax = subplot(1, 3, 2)
ax.plot(domain, lin)
ax.plot(domain, loglin)
ax.legend(["lin", "loglin"], loc=2)
ax = subplot(1, 3, 3)
ax.plot(domain, loglin)
ax.plot(domain, poly)
ax.legend(["loglin", "poly"], loc=2)


os.system("pause")
