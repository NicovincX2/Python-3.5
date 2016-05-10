# -*- coding: utf-8 -*-

import os
import numpy 
import math
from matplotlib import pyplot

# this gives the trajectories - the derivative of the state-space matrix
def dX_dt_damped(X, damping):
    #phi = X[0]
    #omega = X[1] = phi_dot
    #omega_dot = -(g/l)*math.sin(phi)
    #return phi_dot, omega_dot
    return numpy.array([ X[1], (-(g/l)*numpy.sin(X[0]))-(damping * X[1]) ]);

x = numpy.linspace(-1.25, 1.25, 21)
y = numpy.linspace(-2, 2, 20)

(X,Y) = numpy.meshgrid(x, y)
(DX, DY) = dX_dt_damped([X, Y], 0.5)

pyplot.figure(figsize=(10,5))
pyplot.xlabel(r'$\phi$', fontsize=14)
pyplot.ylabel(r'$\omega$', fontsize=14)
pyplot.quiver(X, Y, DX, DY)

coords = zip(omega_damped, phi_damped)
pyplot.hold(True)
pyplot.plot(phi_damped, omega_damped, label='b=0.5')
pyplot.legend()

os.system("pause")