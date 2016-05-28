# -*- coding: utf-8 -*-

import os
import numpy
import math
from matplotlib import pyplot

# this gives the trajectories - the derivative of the state-space matrix


def dX_dt(X):
    #phi = X[0]
    #omega = X[1] = phi_dot
    #omega_dot = -(g/l)*math.sin(phi)
    # return phi_dot, omega_dot
    return numpy.array([X[1], -(g / l) * numpy.sin(X[0])])

x = numpy.linspace(-math.pi * 1.25, math.pi * 1.25, 21)
y = numpy.linspace(-8, 8, 20)

(X, Y) = numpy.meshgrid(x, y)
(DX, DY) = dX_dt([X, Y])

pyplot.figure(figsize=(10, 5))
pyplot.xlabel(r'$\phi$', fontsize=14)
pyplot.ylabel(r'$\omega$', fontsize=14)
pyplot.quiver(X, Y, DX, DY)

# simulate a second trajectory with a larger initial angle
(t2, phi_large, omega_large) = simulate_pendulum(math.pi * 0.99, 0, N, delta_t)

coords = zip(omega, phi)
pyplot.hold(True)
pyplot.plot(phi, omega, color='b', label='$\phi_0=\pi/6$')
pyplot.plot(phi_large, omega_large, color='g', label='$\phi_0=0.99\pi$')
pyplot.legend()

os.system("pause")
