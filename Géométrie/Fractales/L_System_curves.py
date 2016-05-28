# -*- coding: utf-8 -*-

"""
@author: hbouia (Created on Fri Apr 29 18:49:16 2016)
Lindenmayer System (https://en.wikipedia.org/wiki/L-system)
"""
import matplotlib.pyplot as plt
import numpy as np
import random as rnd
import os


def generation(axiom, rules, level):
    gen = axiom
    for n in range(1, level + 1):
        gen = ''.join([c if c not in rules.keys() else rules[c] for c in gen])
    return gen


def L_sys_curve(function, level):
    axiom, rules, angleL, angleR, angle0 = function()
    angleL, angleR, angle0 = np.array([angleL, angleR, angle0]) * np.pi / 180.
    gen = generation(axiom, rules, level)
    print(gen)
    deux_pi, radius = 2 * np.pi, 1.0
    x0, y0, angle, stack = 0., 0., angle0, []
    x, y = [x0], [y0]
    plt.clf()
    for c in gen:
        if c == '[':
            stack.append((x0, y0, angle))
        elif c == ']':
            plt.plot(x, y, 'g')
            x0, y0, angle = stack.pop()
            x, y = [x0], [y0]
        elif c == '+':
            angle = np.mod(angle + angleR, deux_pi)
        elif c == '-':
            angle = np.mod(angle + angleL, deux_pi)
        else:
            if c == 'f':  # jump
                plt.plot(x, y, 'b')
                x, y = [], []
            x0 = x0 + radius * np.cos(angle)
            y0 = y0 + radius * np.sin(angle)
            x.append(x0)
            y.append(y0)
    plt.axis('off')  # ,axisbg=(1, 1, 1))
    plt.plot(x, y, 'g')
    plt.show()
    return


def pythagore():
    axiom = '0'
    rules = {'0': '1[+0]-0', '1': '11'}
    angleL, angleR, angle0 = 45., -45., 90.
    return axiom, rules, angleL, angleR, angle0


def Sierpinski1():
    axiom = 'A'
    rules = {'A': '+B-A-B+', 'B': '-A+B+A-'}
    angleL, angleR, angle0 = 60., -60., 180.
    return axiom, rules, angleL, angleR, angle0


def Sierpinski2():
    axiom = 'F-G-G'
    rules = {'F': 'F-G+F+G-F', 'G': 'GG'}
    angleL, angleR, angle0 = 120., -120., 0.
    return axiom, rules, angleL, angleR, angle0


def dragon():
    axiom = 'FX'
    rules = {'F': 'F', 'X': 'X+YF+', 'Y': '-FX-Y'}
    angleL, angleR, angle0 = 90., -90., 90.
    return axiom, rules, angleL, angleR, angle0


def island():
    axiom = 'F+F+F+F'
    # rules={'F':('F+f-FF+F+FF+Ff+FF-f+FF-F-FF-Ff-FFF',0.,1.),'f':('ffffff',0.,1.),'+':('+',90.,0.),'-':('-',-90.,0.)}
    rules = {'F': 'F+f-FF+F+FF+Ff+FF-f+FF-F-FF-Ff-FFF', 'f': 'ffffff'}
    angleL, angleR, angle0 = 90., -90., 90.
    return axiom, rules, angleL, angleR, angle0


def Koch():
    axiom = 'F-F-F-F'
    rules = {'F': 'F+FF-FF-F-F+F+FF-F-F+F+FF+FF-F'}
    angleL, angleR, angle0 = 90., -90., 90.
    return axiom, rules, angleL, angleR, angle0


def Koch_square():
    axiom = 'F-F-F-F'
    rules = {'F': 'FF-F-F-F-FF'}
    angleL, angleR, angle0 = 90., -90., 90.
    return axiom, rules, angleL, angleR, angle0


def Koch_rect():
    axiom = 'F-F-F-F'
    rules = {'F': 'FF-F+F-F-FF'}
    angleL, angleR, angle0 = 90., -90., 90.
    return axiom, rules, angleL, angleR, angle0


def Koch_sing():
    axiom = 'F-F-F-F'
    rules = {'F': 'FF-F--F-F'}
    angleL, angleR, angle0 = 90., -90., 90.
    return axiom, rules, angleL, angleR, angle0


def FASS():
    axiom = 'F'
    rules = {'F': 'F+G++G-F--FF-G+', 'G': '-F+GG++G+F--F-G'}
    angleL, angleR, angle0 = 60., -60., 90.
    return axiom, rules, angleL, angleR, angle0


def FASS2():
    axiom = '-G'
    rules = {'F': 'FF-G-G+F+F-G-GF+G+FFG-F+G+FF+G-FG-G-F+F+GG-',
             'G': '+FF-G-G+F+FG+F-GG-F-G+FGG-F-GF+F+G-G-F+F+GG'}
    angleL, angleR, angle0 = 90., -90., 90.
    return axiom, rules, angleL, angleR, angle0


def plant0():
    axiom = 'F'
    rules = {'F': 'F[+F]F[-F]F'}
    angleL, angleR, angle0 = 20., -20., 90.
    return axiom, rules, angleL, angleR, angle0


def plant1():
    axiom = 'F'
    rules = {'F': 'F[+F]F[-F][F]'}
    angleL, angleR, angle0 = 25.7, -25.7, 90.
    return axiom, rules, angleL, angleR, angle0


def plant2():
    axiom = 'F'
    rules = {'F': 'FF-[-F+F+F]+[+F-F-F]'}
    angleL, angleR, angle0 = 22.5, -22.5, 90.
    return axiom, rules, angleL, angleR, angle0


def plant3():
    axiom = 'X'
    rules = {'X': 'F[+X]F[-X]+X', 'F': 'FF'}
    angleL, angleR, angle0 = 20.0, -20.0, 90.
    return axiom, rules, angleL, angleR, angle0


def plant4():
    axiom = 'X'
    rules = {'X': 'F[+X][-X]FX', 'F': 'FF'}
    angleL, angleR, angle0 = 25.7, -25.7, 90.
    return axiom, rules, angleL, angleR, angle0


def plant5():
    axiom = 'X'
    rules = {'X': 'F-[[X]+X]+F[+FX]-X', 'F': 'FF'}
    angleL, angleR, angle0 = 22.5, -22.5, 90.
    return axiom, rules, angleL, angleR, angle0


def flocon_de_Koch():
    axiom = 'F--F--F'
    rules = {'F': 'F+F--F+F'}
    angleL, angleR, angle0 = 60., -60., 180.
    return axiom, rules, angleL, angleR, angle0

choix = {1: (pythagore, 9), 2: (Sierpinski1, 6), 3: (Sierpinski2, 8), 4: (dragon, 10), 5: (island, 2), 6: (Koch, 2), 7: (Koch_square, 4), 8: (Koch_rect, 3), 9: (Koch_sing, 4), 10: (FASS, 4), 11: (FASS2, 2), 12: (plant0, 5), 13: (plant1, 5), 14: (plant2, 4), 15: (plant3, 5), 16: (plant4, 5), 17: (plant5, 5), 18: (flocon_de_Koch, 3)
         }

#plt.subplot(111, axisbg=(1, 1, 1))
ichoix = 8  # rnd.randint(1,17)
function = choix[ichoix][0]
L_sys_curve(*choix[ichoix])
plt.title(function.func_name)

os.system("pause")
