# -*- coding: utf-8 -*-

import os
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(6,3))
plt.plot([0,2],[0,0],'k')
plt.plot([1,1],[0,1],'k')
plt.plot([0,1,2,1],[0,0,0,1],'ko',markersize=10)
plt.text(1.1,0.1,'T[n,j]')
plt.text(0.1,0.1,'T[n,j-1]')
plt.text(1.1,1.1,'T[n+1,j]')
plt.text(2.1,0.1,'T[n,j+1]')
plt.xlabel('space')
plt.ylabel('time')
plt.axis('equal')
plt.yticks([0.0,1.0],[])
plt.xticks([0.0,1.0],[])
plt.title('FTCS explicit scheme',fontsize=12)
plt.axis([-0.5,2.5,-0.5,1.5]);

dt = 0.0005 # grid size for time (s)
dy = 0.0005 # grid size for space (m)
viscosity = 2*10**(-4) # kinematic viscosity of oil (m2/s)
y_max = 0.04 # in m
t_max = 1 # total time in s
V0 = 10 # velocity in m/s

# function to calculate velocity profiles based on a finite difference approximation to the 1D diffusion equation and the 
# FTCS (forward-in-time, centered-in-space) scheme:
def diffusion_FTCS(dt,dy,t_max,y_max,viscosity,V0):
    # diffusion number (has to be less than 0.5 for the solution to be stable):
    s = viscosity*dt/dy**2 
    y = np.arange(0,y_max+dy,dy) 
    t = np.arange(0,t_max+dt,dt)
    r = len(t)
    c = len(y)
    V = np.zeros([r,c])
    V[:,0] = V0
    for n in range(0,r-1): # time
        for j in range(1,c-1): # space
            V[n+1,j] = V[n,j] + s*(V[n,j-1] - 2*V[n,j] + V[n,j+1]) 
    return y,V,r,s
# note that this can be written without the for-loop in space, but it is easier to read it this way


from scipy.special import erfc

# function to calculate velocity profiles using the analytic solution:
def diffusion_analytic(t,h,V0,dy,viscosity):
    y = np.arange(0,h+dy,dy)
    eta1 = h/(2*(t*viscosity)**0.5)
    eta = y/(2*(t*viscosity)**0.5)
    sum1 = 0
    sum2 = 0
    for n in range(0,1000):
        sum1 = sum1 + erfc(2*n*eta1+eta)
        sum2 = sum2 + erfc(2*(n+1)*eta1-eta)
    V_analytic = V0*(sum1-sum2)
    return V_analytic

y,V,r,s = diffusion_FTCS(dt,dy,t_max,y_max,viscosity,V0)

# plotting:
plt.figure(figsize=(7,5))
plot_times = np.arange(0.2,1.0,0.1)
for t in plot_times:
    plt.plot(y,V[t/dt,:],'Gray',label='numerical')
    V_analytic = diffusion_analytic(t,0.04,10,dy,viscosity)
    plt.plot(y,V_analytic,'ok',label='analytic',markersize=3)
    if t==0.2:
        plt.legend(fontsize=12)
plt.xlabel('distance from wall (m)',fontsize=12)
plt.ylabel('velocity (m/s)',fontsize=12)
plt.axis([0,y_max,0,V0])
plt.title('comparison between explicit numerical \n(FTCS scheme) and analytic solutions');

dt = 0.0005 # grid size for time (m)
dy = 0.0005 # grid size for space (s)
y,V,r,s = diffusion_FTCS(dt,dy,t_max,y_max,viscosity,V0)
V_analytic = diffusion_analytic(0.5,0.04,V0,dy,viscosity)
plt.figure(figsize=(7,5))
plt.plot(y,V_analytic-V[0.5/dt],'--k',label='small s')

dy = 0.0010
dt = 0.00254
y,V,r,s = diffusion_FTCS(dt,dy,t_max,y_max,viscosity,V0)
V_analytic = diffusion_analytic(0.5,0.04,V0,dy,viscosity)
V_numeric = V[r/2-1,:]

plt.plot(y,V_analytic-V_numeric,'k',label='large s')
plt.xlabel('distance from wall (m)',fontsize=12)
plt.ylabel('velocity difference (m/s)',fontsize=12)
plt.title('difference between numerical and analytic \n solutions for different \'s\' values',fontsize=14)
plt.axis([0,y_max,-4,4])
plt.legend();


os.system("pause")