# -*- coding: utf-8 -*-

import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['text.usetex'] = True
import sympy
from scipy import integrate

t = sympy.symbols("t", positive=True)
s, Y = sympy.symbols("s, Y", real=True)
y = sympy.Function("y")
ode = y(t).diff(t, 2) + 2 * y(t).diff(t) + 10 * y(t) - 2 * sympy.sin(3*t)
print (ode)
L_y = sympy.laplace_transform(y(t), t, s)
print (L_y)
L_ode = sympy.laplace_transform(ode, t, s, noconds=True)
print (L_ode)

def laplace_transform_derivatives(e):
    """
    Evaluate the unevaluted laplace transforms of derivatives
    of functions
    """
    if isinstance(e, sympy.LaplaceTransform):
        if isinstance(e.args[0], sympy.Derivative):
            d, t, s = e.args
            n = len(d.args) - 1
            return ((s**n) * sympy.LaplaceTransform(d.args[0], t, s) - 
                    sum([s**(n-i) * sympy.diff(d.args[0], t, i-1).subs(t, 0)
                         for i in range(1, n+1)]))
        
    if isinstance(e, (sympy.Add, sympy.Mul)):
        t = type(e)
        return t(*[laplace_transform_derivatives(arg) for arg in e.args])
    
    return e

L_ode_2 = laplace_transform_derivatives(L_ode)
print (L_ode_2)
L_ode_3 = L_ode_2.subs(L_y, Y)
print (L_ode_3)
ics = {y(0): 1, y(t).diff(t).subs(t, 0): 0}
print (ics)
L_ode_4 = L_ode_3.subs(ics)
print (L_ode_4)
Y_sol = sympy.solve(L_ode_4, Y)
print (Y_sol)
sympy.apart(Y_sol[0])
y_sol = sympy.inverse_laplace_transform(Y_sol[0], s, t)
sympy.simplify(y_sol)
y_t = sympy.lambdify(t, y_sol, 'numpy')

fig, ax = plt.subplots(figsize=(8, 4))

tt = np.linspace(0, 10, 500)
ax.plot(tt, y_t(tt).real)
ax.set_xlabel(r"$t$", fontsize=18)
ax.set_ylabel(r"$y(t)$", fontsize=18)
fig.tight_layout()

os.system("pause")

