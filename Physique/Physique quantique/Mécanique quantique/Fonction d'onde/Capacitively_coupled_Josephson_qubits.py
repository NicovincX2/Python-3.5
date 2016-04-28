# -*- coding: utf-8 -*-

import os
from scipy import *
from scipy import optimize
from wavefunction import *

h = 6.626e-34;
h_ = h/(2*pi);
e = 1.602e-19
Phi0 = h / (2 * e)
cf = h_

Ic = 1.7e-6
Cj = 700e-15
L = 0.72e-9


# discretization of X coordinate
N = 750
xmin = -0.7 * pi
xmax =  4 * pi
xvec = arange(xmin, xmax, (xmax - xmin)/N)

debug = False

def U_flux_biased(x, args):
    """
    Flux-biased phase qubit potential
    """
    Ej = args['Ej']
    beta = args['beta']
    gamma = args['gamma']
    
    u = -Ej * (cos(x) - 1 / (2 * beta) * x ** 2 + gamma * x)
    
    return u

def jjpq_flux_biased_me(ceta, Cj, cf_p, phi):
    
    mm = Cj * (1 + ceta) * (Phi0/(2*pi))**2 * cf;
    beta = 2*pi*L*Ic / Phi0;
    Ej = Phi0/(2*pi) * Ic / cf;
    
    gamma = phi / beta;
    
    U_args = {'Ej': Ej, 'beta': beta, 'gamma': gamma}
    S_param = array([h_, mm])

    # Calculate the eigenfunctions
    M = schrodinger_matrix(xmin, xmax, N, S_param, U_flux_biased, U_args)
    evals, evec = eigenvectors_sorted(M)
    
    # Find bound states
    dmin = optimize.fmin(U_flux_biased, [0.5], [U_args], disp=False)
    dmax = optimize.fmin(lambda x, args: -U_flux_biased(x, args), [2.5], [U_args], disp=False)
    delta = dmax-dmin
    
    Umin = U_flux_biased(dmin, U_args);
    Umax = U_flux_biased(dmax, U_args);
    dU = Umax - Umin;

    boundidx = []
    for i in range(0,N):
        if evals[i] > Umin-0.5*dU and evals[i] < Umax+0.5*dU:
            if inner(evec[:,i] * (dmin-delta < xvec) * (xvec < dmax), evec[:,i]) > 0.85:
                boundidx.append(i)
    
    if debug:
        print "Found bound states: ", boundidx
    
    # 
    # Evaluate matrix elements:
    #
    inner_prod = zeros((len(boundidx), len(boundidx)))
    expect_pos = zeros((len(boundidx), len(boundidx)))
    expect_kin = zeros((len(boundidx), len(boundidx)))
    energy_levels = zeros(len(boundidx))
    
    for i in range(0, len(boundidx)):
        l = boundidx[i]
        energy_levels[i] = evals[l]
    
        for j in range(0, len(boundidx)):
            k = boundidx[j]
    
            inner_prod[i,j] = inner(evec[:,k], evec[:,l])
            expect_pos[i,j] = inner(evec[:,k], evec[:,l] * xvec)
            expect_kin[i,j] = inner(evec[:,k], derivative(evec[:,l], xvec))

    return energy_levels, expect_pos, expect_kin

H  = 6.626e-34
H_ = H/(2*pi)

# Complication: When sweeping r or changing ceta -> very sensitive and the
# number of bound states changes.

ceta = 0.05
Cj = 700e-15 * (H_/h_)
phi1 = 5.15

E1, Ed1, Edd1 = jjpq_flux_biased_me(ceta, Cj, h_, phi1)
P1 = h_ /1j  * Edd1 

dphi = 0.001
PHI2 = arange(5.10, 5.18, dphi) 

eval_idx = 0
eval_store = zeros((len(PHI2),9)).astype(float)

for phi2 in PHI2:

    E2, Ed2, Edd2 = jjpq_flux_biased_me(ceta, Cj, h_, phi2);
    P2 = h_ / 1j * Edd2;

    H = zeros((9,9), dtype=complex)
    Hint = zeros((9,9), dtype=complex)
	
    for K1 in range(0,3):
        for K2 in range(0,3):
            for L1 in range(0,3):
                for L2 in range(0,3):
                    I1 = K1 + 3 * (L1)
                    I2 = K2 + 3 * (L2)
                    H[I1,I2] =            (E1[K1] - (1*E1[0]+1*E1[1])/2) * (K1 == K2) * (L1 == L2)
                    H[I1,I2] = H[I1,I2] + (E2[L1] - (1*E2[0]+1*E2[1])/2) * (K1 == K2) * (L1 == L2)
                    Hint[I1,I2] = (2*pi / Phi0)**2 * ceta / (Cj * ( 1 + ceta)) * P1[K1,K2] * P2[L1,L2] / cf


    H = H + Hint		
    H = H / (2*pi * 1e9)

    eval, e =  eigenvectors_sorted(H)
    eval_store[eval_idx, :] = eval
    eval_idx = eval_idx + 1

if debug:
    print "Eigenvalues vs :"
    print2DMatrix(eval_store)

fig, ax = subplots(1, 1, figsize=(12,6))
 
for n in range(6):
    ax.plot(PHI2, eval_store[:,n])
    
ax.axis('tight');
ax.set_xlabel(r'$\phi_2$')
ax.set_ylabel(r'$E_n$')
ax.set_title(r'Energy levels of a capacitively coupled phase qubits. $\phi_1 = %.2f$' % phi1)

fig, ax = subplots(1, 1, figsize=(12,6))
 
for n in [1,2]:
    ax.plot(PHI2, eval_store[:,n])
    
ax.axis('tight');
ax.set_xlabel(r'$\phi_2$')
ax.set_ylabel(r'$E_1, E_2$')
ax.set_title(r'Energy levels of a capacitively coupled phase qubits. $\phi_1 = %.2f$' % phi1)

os.system("pause")

