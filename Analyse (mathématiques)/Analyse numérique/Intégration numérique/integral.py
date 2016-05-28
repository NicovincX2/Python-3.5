# -*- coding: utf-8 -*-

import os
import matplotlib.pyplot as plt
import numpy as np
import sympy

x, x0 = sympy.symbols("x, x_0")

f = (x + 0.5) ** 3 - 3.5 * (x + 0.5) ** 2 + x + 3

f.subs(x, x0) + f.diff(x).subs(x, x0) * (x - x0)

f_func = sympy.lambdify(x, f, 'numpy')


def arrowify(fig, ax):
    xmin, xmax = ax.get_xlim()
    ymin, ymax = ax.get_ylim()

    # removing the default axis on all sides:
    for side in ['bottom', 'right', 'top', 'left']:
        ax.spines[side].set_visible(False)

    # removing the axis labels and ticks
    ax.set_xticks([])
    ax.set_yticks([])
    ax.xaxis.set_ticks_position('none')
    ax.yaxis.set_ticks_position('none')

    # wider figure for demonstration
    # fig.set_size_inches(4,2.2)

    # get width and height of axes object to compute
    # matching arrowhead length and width
    dps = fig.dpi_scale_trans.inverted()
    bbox = ax.get_window_extent().transformed(dps)
    width, height = bbox.width, bbox.height

    # manual arrowhead width and length
    hw = 1. / 25. * (ymax - ymin)
    hl = 1. / 25. * (xmax - xmin)
    lw = 0.5  # axis line width
    ohg = 0.3  # arrow overhang

    # compute matching arrowhead length and width
    yhw = hw / (ymax - ymin) * (xmax - xmin) * height / width
    yhl = hl / (xmax - xmin) * (ymax - ymin) * width / height

    # draw x and y axis
    ax.arrow(xmin, 0, xmax - xmin, 0., fc='k', ec='k', lw=lw,
             head_width=hw, head_length=hl, overhang=ohg,
             length_includes_head=True, clip_on=False)

    ax.arrow(0, ymin, 0., ymax - ymin, fc='k', ec='k', lw=lw,
             head_width=yhw, head_length=yhl, overhang=ohg,
             length_includes_head=True, clip_on=False)

    ax.text(xmax * 0.95, ymin * 0.25, r'$x$', fontsize=22)
    ax.text(xmin * 0.35, ymax * 0.9, r'$f(x)$', fontsize=22)

fig, ax = plt.subplots(1, 1, figsize=(8, 4))

xvec = np.linspace(-1.75, 3.0, 100)
ax.plot(xvec, f_func(xvec), 'k', lw=2)

xvec = np.linspace(-0.8, 0.85, 100)
ax.fill_between(xvec, f_func(xvec), color='lightgreen', alpha=0.9)
xvec = np.linspace(0.85, 2.31, 100)
ax.fill_between(xvec, f_func(xvec), color='red', alpha=0.5)
xvec = np.linspace(2.31, 2.6, 100)
ax.fill_between(xvec, f_func(xvec), color='lightgreen', alpha=0.99)

ax.text(0.6, 3.5, r"$\int_a^b\!f(x){\rm d}x$", fontsize=22)
ax.text(-0.88, -0.85, r"$a$", fontsize=18)
ax.text(2.55, -0.85, r"$b$", fontsize=18)
ax.axis('tight')

arrowify(fig, ax)
fig.savefig("ch8-illustration-integral.pdf")

os.system("pause")
