# -*- coding: utf-8 -*-

import os
import matplotlib.pyplot as plt
import pylab
import scipy.stats
import numpy as np

rv = scipy.stats.exponweib(1, 2, scale=10, floc=0)
x_range = np.arange(0, 30, 0.1)

fig, ax = plt.subplots()
ax.plot(x_range, rv.pdf(x_range))

def rstyle(ax): 
    '''Styles x,y axes to appear like ggplot2
    Must be called after all plot and axis manipulation operations have been 
    carried out (needs to know final tick spacing)
    '''
    #Set the style of the major and minor grid lines, filled blocks
    ax.grid(True, 'major', color='w', linestyle='-', linewidth=1.4)
    ax.grid(True, 'minor', color='0.99', linestyle='-', linewidth=0.7)
    ax.patch.set_facecolor('0.90')
    ax.set_axisbelow(True)
    
    #Set minor tick spacing to 1/2 of the major ticks
    ax.xaxis.set_minor_locator((pylab.MultipleLocator((plt.xticks()[0][1]
                                -plt.xticks()[0][0]) / 2.0 )))
    ax.yaxis.set_minor_locator((pylab.MultipleLocator((plt.yticks()[0][1]
                                -plt.yticks()[0][0]) / 2.0 )))
    
    #Remove axis border
    for child in ax.get_children():
        if isinstance(child, matplotlib.spines.Spine):
            child.set_alpha(0)
       
    #Restyle the tick lines
    for line in ax.get_xticklines() + ax.get_yticklines():
        line.set_markersize(5)
        line.set_color("gray")
        line.set_markeredgewidth(1.4)
    
    #Remove the minor tick lines    
    for line in (ax.xaxis.get_ticklines(minor=True) + 
                 ax.yaxis.get_ticklines(minor=True)):
        line.set_markersize(0)
    
    #Only show bottom left ticks, pointing out of axis
    plt.rcParams['xtick.direction'] = 'out'
    plt.rcParams['ytick.direction'] = 'out'
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
   
rv = scipy.stats.exponweib(1, 2, scale=10, floc=0)
x_range = np.arange(0, 30, 0.1)
fig, ax = plt.subplots()
ax.plot(x_range, rv.pdf(x_range))
rstyle(ax)

import husl

def husl_gen():
    '''Generate random set of HUSL colors, one dark, one light'''
    hue = np.random.randint(0, 360)
    saturation, lightness = np.random.randint(0, 100, 2)
    husl_dark = husl.husl_to_hex(hue, saturation, lightness/3)
    husl_light = husl.husl_to_hex(hue, saturation, lightness)
    return husl_dark, husl_light

def rfill(ax, x_range, dist, **kwargs):
    '''Create a distribution fill with default parameters to resemble ggplot2
    kwargs can be passed to change other parameters
    '''
    husl_dark_hex, husl_light_hex = husl_gen()
    defaults = {'color': husl_dark_hex,
                'facecolor': husl_light_hex,
                'linewidth' : 2.0, 
                'alpha': 0.2}
                
    for x,y in defaults.iteritems():
        kwargs.setdefault(x, y)
    
    return ax.fill(x_range, dist, **kwargs)

rv = scipy.stats.exponweib(1, 2, scale=10, floc=0)
x_range = np.arange(0, 30, 0.1)
fig, ax = plt.subplots()
rfill(ax, x_range, rv.pdf(x_range))
rstyle(ax)

#Lets try a few distributions
rv1 = scipy.stats.exponweib(1, 1.5, scale=7, floc=0)
rv2 = scipy.stats.exponweib(1, 2.8, scale=6, floc=0)
fig2, ax2 = plt.subplots()
rfill(ax2, x_range, rv.pdf(x_range))
rfill(ax2, x_range, rv1.pdf(x_range))
rfill(ax2, x_range, rv2.pdf(x_range))
rstyle(ax2)

def rhist(ax, data, **kwargs):
    '''Creates a hist plot with default style parameters to look like ggplot2
    kwargs can be passed to changed other parameters
    '''
    defaults = {'facecolor' : '0.15',
                'edgecolor' : '0.28',
                'linewidth' : 1, 
                'rwidth': 1}
                            
    for x,y in defaults.iteritems():
        kwargs.setdefault(x, y)
    
    return ax.hist(data, **kwargs)

R = scipy.stats.exponweib.rvs(1, 2.0, scale=10, loc=0, size=5000)
fig, ax = plt.subplots()
_ = rhist(ax, R, bins=30)
rstyle(ax)

fig, ax = plt.subplots()
_ = rhist(ax, R, bins=30)
rstyle(ax)
ax2 = twinx()
rfill(ax2, x_range, rv.pdf(x_range))
ax.set_ylabel('Frequency')
ax2.set_ylabel('PDF')

import climatic as cl

wind_direction_freqs = [0.059, 0.048, 0.091, 0.142, 0.25, 0.129, 0.014,
                        0.013, 0.09, 0.044, 0.03, 0.09]
cl.wind_rose(wind_direction_freqs)

os.system("pause")