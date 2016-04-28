# -*- coding: utf-8 -*-

import os
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

def show_array(shape, sel, filename=None):
    """Visualize indexing of arrays"""

    data = np.zeros(shape)
    exec("data[%s] = 1" % sel)

    fig, ax = plt.subplots(1, 1, figsize=shape)

    ax.patch.set_facecolor('black')
    ax.set_aspect('equal', 'box')
    ax.xaxis.set_major_locator(plt.NullLocator())
    ax.yaxis.set_major_locator(plt.NullLocator())

    size = 0.97
    for (m, n), w in np.ndenumerate(data):
        color = '#1199ff' if w > 0 else '#eeeeee'
        rect = plt.Rectangle([n - size / 2, m - size / 2],
                             size, size,
                             facecolor=color,
                             edgecolor=color)
        ax.add_patch(rect)
        ax.text(m, n, "(%d, %d)" % (n, m), ha='center', va='center', fontsize=12)
        
    ax.autoscale_view()
    ax.invert_yaxis()

    if sel == ":, :":
        ax.set_title("data\n", fontsize=12)
    else:
        ax.set_title("data[%s]\n" % sel, fontsize=12)
    
    #fig.tight_layout()
    
    if filename:
        fig.savefig(filename + ".png", dpi=200)
        fig.savefig(filename + ".svg")
        fig.savefig(filename + ".pdf")

show_array((4, 4), ":, :", "array_indexing_1")
show_array((4, 4), "0", "array_indexing_2")
show_array((4, 4), "1, :", "array_indexing_3")
show_array((4, 4), ":, 2", "array_indexing_4")
show_array((4, 4), "0:2, 0:2", "array_indexing_5")
show_array((4, 4), "0:2, 2:4", "array_indexing_6")
show_array((4, 4), "::2, ::2", "array_indexing_7")
show_array((4, 4), "1::2, 1::2", "array_indexing_8")
show_array((4, 4), ":,[0,3]", "array_indexing_9")
show_array((4, 4), "[1,3],[0,3]", "array_indexing_10")
show_array((4, 4), ":,np.array([False, True, True, False])", "array_indexing_11")
show_array((4, 4), ":,np.array([False, True, True, False])", "array_indexing_12")
show_array((4, 4), "1:3,np.array([False, True, True, False])", "array_indexing_12")

os.system("pause")

