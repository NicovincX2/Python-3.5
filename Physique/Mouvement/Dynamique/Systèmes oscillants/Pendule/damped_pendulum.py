# -*- coding: utf-8 -*-

import os
import numpy 
import math
from matplotlib import pyplot

def simulate_pendulum_damped(phi_init, omega_init, numSteps, deltaT, damping):
    t = numpy.zeros(numSteps)

    phi = numpy.zeros(numSteps)
    phi[0] = phi_init

    omega = numpy.zeros(numSteps)
    omega[0] = omega_init

    for n in range(1,numSteps):
        t[n] = deltaT * n # store the time for plotting.

        alpha_t = (-(g/l) * math.sin(phi[n-1])) - (damping * omega[n-1])
        omega_t = omega[n-1] + (delta_t * alpha_t)
        phi_t = phi[n-1] + (delta_t * omega_t)
        omega[n] = omega_t
        phi[n] = phi_t

    return (t, phi, omega)

damping = 0.5
(t_damped, phi_damped, omega_damped) = simulate_pendulum_damped(phi_0, omega_0, N, delta_t, damping)

pyplot.figure(figsize=(10,4))
pyplot.xlabel('t', fontsize=14)
pyplot.ylabel(r'$\phi$', fontsize=14)
pyplot.hold(True)
pyplot.plot(t_damped, phi_damped)

os.system("pause")