# -*- coding: utf-8 -*-

import os
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

data = np.arange(9).reshape(3,3)
print (data)

data.sum()
data.sum(axis=0)
data.sum(axis=1)

def show_array_aggregation(data, axis, filename=None):
    """Visualize indexing of arrays"""
   
    fig, axes = plt.subplots(2, 1, figsize=(4, 8))

    
    ax = axes[0]
    ax.patch.set_facecolor('black')
    #ax.set_aspect('equal', 'box')
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
        if axis is None:
            color = '#1199ff'
        elif axis == 1:
            color = colors[m]
        else:
            color = colors[n]
            
        size = 0.8
        rect = plt.Rectangle([n - size / 2, m - size / 2],
                             size, size,
                             facecolor=color,
                             edgecolor=color)
        ax.add_patch(rect)

        ax.text(n, m, "%d" % data[m, n], ha='center', va='center', fontsize=12)
        
    ax.autoscale_view()
    ax.invert_yaxis()
    ax.set_title("data", fontsize=12)

    if False:
        ax = axes[1]
        ax.set_frame_on(False)
        ax.patch.set_facecolor('white')
        ax.xaxis.set_major_locator(plt.NullLocator())
        ax.yaxis.set_major_locator(plt.NullLocator())
        ax.set_xlim(0, 3)
        ax.set_ylim(0, 3)

        if axis is not None:
            ax.text(1.5, 1.5, "data.sum(axis=%d)" % axis, ha='center', va='center', fontsize=18)        
        else:
            ax.text(1.5, 1.5, "data.sum()", ha='center', va='center', fontsize=18)        

        ax.arrow(0.3, 1.25, 2.1, 0.0, head_width=0.1, head_length=0.2, fc='k', ec='k')

    if axis == 0:
        adata = data.sum(axis=axis)[:, np.newaxis]
    elif axis == 1:
        adata = data.sum(axis=axis)[:, np.newaxis]
    else:
        adata = np.atleast_2d(data.sum(axis=axis))
        
    ax = axes[1]
    ax.set_frame_on(False)
    ax.patch.set_facecolor('white')
    ax.xaxis.set_major_locator(plt.NullLocator())
    ax.yaxis.set_major_locator(plt.NullLocator())
    
    
    colors = ['#1199ff', '#ee3311', '#66ff22']
    
    for (m, n), w in np.ndenumerate(data):
        size = 1.0
        color = '#ffffff'
        rect = plt.Rectangle([n - size / 2, m - size / 2],
                         size, size,
                         facecolor=color,
                         edgecolor=color)
        ax.add_patch(rect)        
    
    for (m, n), w in np.ndenumerate(adata):

        if axis is None:
            size = 1.0
            color = '#000000'
            rect = plt.Rectangle([1+m - size / 2, 0 + n - size / 2],
                             size, size,
                             facecolor=color,
                             edgecolor=color)
            ax.add_patch(rect)        
            size = 0.97
            color = '#eeeeee'

            
            rect = plt.Rectangle([1+m - size / 2, 0 + n - size / 2],
                                 size, size,
                                 facecolor=color,
                                 edgecolor=color)
            ax.add_patch(rect)

            
            if axis is None:
                color = '#1199ff'
            elif axis == 1:
                color = colors[n]
            else:
                color = colors[m]

            size = 0.8
            rect = plt.Rectangle([1+m - size / 2, 0 + n - size / 2],
                                 size, size,
                                 facecolor=color,
                                 edgecolor=color)
            ax.add_patch(rect)

            
            if n == 0:
                ax.text(1+m, n+0, "%d" % adata[m, n], ha='center', va='center', fontsize=10)

            
        if axis == 0:
            size = 1.0
            color = '#000000'
            rect = plt.Rectangle([m - size / 2, 0 + n - size / 2],
                             size, size,
                             facecolor=color,
                             edgecolor=color)
            ax.add_patch(rect)        
            size = 0.97
            color = '#eeeeee'

            
            rect = plt.Rectangle([m - size / 2, 0 + n - size / 2],
                                 size, size,
                                 facecolor=color,
                                 edgecolor=color)
            ax.add_patch(rect)

            
            if axis is None:
                color = '#1199ff'
            elif axis == 1:
                color = colors[n]
            else:
                color = colors[m]

            size = 0.8
            rect = plt.Rectangle([m - size / 2, 0 + n - size / 2],
                                 size, size,
                                 facecolor=color,
                                 edgecolor=color)
            ax.add_patch(rect)

            
            if n == 0:
                ax.text(m, n+0, "%d" % adata[m, n], ha='center', va='center', fontsize=10)

        if axis == 1:
            size = 1.0
            color = '#000000'
            rect = plt.Rectangle([0 + m - size / 2, n - size / 2],
                             size, size,
                             facecolor=color,
                             edgecolor=color)
            ax.add_patch(rect)        
            size = 0.97
            color = '#eeeeee'

            rect = plt.Rectangle([0 + m - size / 2, n - size / 2],
                                 size, size,
                                 facecolor=color,
                                 edgecolor=color)

            ax.add_patch(rect)

            if axis is None:
                color = '#1199ff'
            elif axis == 1:
                color = colors[m]
            else:
                color = colors[m]

            size = 0.8
            rect = plt.Rectangle([0 + m - size / 2, n - size / 2],
                                 size, size,
                                 facecolor=color,
                                 edgecolor=color)
            ax.add_patch(rect)
            
            if axis == 0 and m == 0:
                ax.text(m+0, n, "%d" % adata[m, n], ha='center', va='center', fontsize=12)
            if axis == 1 and n == 0:
                ax.text(m, n+0, "%d" % adata[m, n], ha='center', va='center', fontsize=10)

    ax.autoscale_view()
    ax.invert_yaxis()
    if axis is not None:
        ax.set_title("data.sum(axis=%d)" % axis, fontsize=12)
    else:
        ax.set_title("data.sum()", fontsize=12)
    
    fig.tight_layout()
    
    if filename:
        fig.savefig(filename + ".png", dpi=200)
        fig.savefig(filename + ".svg")
        fig.savefig(filename + ".pdf")

data = np.arange(1,10).reshape(3,3)
print (data)

show_array_aggregation(data, None, filename="array_aggregation_1")
show_array_aggregation(data, 0, filename="array_aggregation_2")
show_array_aggregation(data, 1, filename="array_aggregation_3")

os.system("pause")

