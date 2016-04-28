# -*- coding: utf-8 -*-

import os
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

def show_array_broadcasting(a, b, filename=None):
    """Visualize broadcasting of arrays"""

    c = a + b
    
    fig, axes = plt.subplots(1, 3, figsize=(12, 4))

    data = a
    ax = axes[0]
    ax.patch.set_facecolor('black')
    ax.xaxis.set_major_locator(plt.NullLocator())
    ax.yaxis.set_major_locator(plt.NullLocator())
    colors = ['#1199ff', '#ee3311', '#66ff22']
    for (m, n), w in np.ndenumerate(data):
        size = 0.97
        color = '#1199ff'
        rect = plt.Rectangle([n - size / 2, m - size / 2],
                             size, size,
                             facecolor=color,
                             edgecolor=color)
        ax.add_patch(rect)
        ax.text(m, n, "%d" % data[n, m], ha='center', va='center', fontsize=12)        
    ax.text(2.8, 1, "+", ha='center', va='center', fontsize=22)        
    ax.autoscale_view()
    ax.invert_yaxis()
    
    data = np.zeros_like(a) + b
    ax = axes[1]
    ax.patch.set_facecolor('black')
    ax.xaxis.set_major_locator(plt.NullLocator())
    ax.yaxis.set_major_locator(plt.NullLocator())
    colors = ['#1199ff', '#ee3311', '#66ff22']
    for (m, n), w in np.ndenumerate(data):
        size = 0.97
        color = '#eeeeee'
        rect = plt.Rectangle([n - size / 2, m - size / 2],
                             size, size,
                             facecolor=color,
                             edgecolor=color)
        ax.add_patch(rect)
        if (np.argmax(b.T.shape) == 0 and m == 0) or (np.argmax(b.T.shape) == 1 and n == 0):
            color = '#1199ff'
            #size = 0.8
            rect = plt.Rectangle([n - size / 2, m - size / 2],
                                 size, size,
                                 facecolor=color,
                                 edgecolor=color)
            ax.add_patch(rect)
        ax.text(m, n, "%d" % data[n, m], ha='center', va='center', fontsize=12)        
    ax.text(2.8, 1, "=", ha='center', va='center', fontsize=22)        
    ax.autoscale_view()
    ax.invert_yaxis()

    
    data = c
    ax = axes[2]
    ax.patch.set_facecolor('black')
    ax.xaxis.set_major_locator(plt.NullLocator())
    ax.yaxis.set_major_locator(plt.NullLocator())
    colors = ['#1199ff', '#ee3311', '#66ff22']
    for (m, n), w in np.ndenumerate(data):
        size = 0.97
        color = '#1199ff' if w > 0 else '#eeeeee'
        color = '#eeeeee'
        rect = plt.Rectangle([n - size / 2, m - size / 2],
                             size, size,
                             facecolor=color,
                             edgecolor=color)
        ax.add_patch(rect)
        color = '#1199ff'
        #size = 0.8
        rect = plt.Rectangle([n - size / 2, m - size / 2],
                             size, size,
                             facecolor=color,
                             edgecolor=color)
        ax.add_patch(rect)
        ax.text(m, n, "%d" % data[n, m], ha='center', va='center', fontsize=12)        
    ax.autoscale_view()
    ax.invert_yaxis()
    
    #fig.tight_layout()
        
    if filename:
        fig.savefig(filename + ".png", dpi=200)
        fig.savefig(filename + ".svg")
        fig.savefig(filename + ".pdf")

a = np.array([[11, 12, 13], [21, 22, 23], [31, 32, 33]])
b = np.array([[1, 2, 3]])

show_array_broadcasting(a, b, filename="array_broadcasting_1")
show_array_broadcasting(a, b.T, filename="array_broadcasting_2")

os.system("pause")

