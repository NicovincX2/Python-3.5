# -*- coding: utf-8 -*-

import os
import numpy
from numpy.polynomial.hermite import Hermite

def ho_evec(x,n,m,ohm):
    vec = [0]*9
    vec[n] = 1
    Hn = Hermite(vec)
    return (1/sqrt(2**n*factorial(n)))*pow(m*ohm/pi,0.25)*exp(-0.5*m*ohm*x**2)*Hn(x*sqrt(m*ohm))

plot(x,ho_evec(x,0,1,1),label="Analytic")
plot(x,-U[:,0]/sqrt(h),label="Numeric")
xlabel('x (bohr)')
ylabel(r'$\psi(x)$')
title("Comparison of numeric and analytic solutions to the Harmonic Oscillator")
legend()

phase_correction = [-1,1,1,-1,-1,1]
for i in range(6):
    subplot(2,3,i+1)
    plot(x,ho_evec(x,i,1,1),label="Analytic")
    plot(x,phase_correction[i]*U[:,i]/sqrt(h),label="Numeric")
    
os.system("pause")