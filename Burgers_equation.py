# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 16:06:20 2018

@author:Balaji.V
E-mail id:balaji36918@gmail.com 
"""
#import libraries
import numpy
import sympy
from matplotlib import pyplot


#using latex from sympy
from sympy import init_printing
init_printing(use_latex = True)

#use symbols
x,nu,t = sympy.symbols('x nu t')
phi = (sympy.exp(-(x - 4 * t)**2/(4 * nu *(t+1)))+
       sympy.exp(-x - 4 *t - 2 * sympy.pi)**2/(4 * nu * (t+1)))

#differentiate phi
phiprime = phi.diff(x)
print(phiprime)

#lambdify function in Python
from sympy.utilities.lambdify import lambdify
u = -2 * nu * (phiprime/phi) + 4
print(u)

ufunc = lambdify((t,x,nu),u)
print(ufunc(1,4,3))

#variable declarations
nx = 101
nt = 100
dx = 2 * numpy.pi/(nx-1)
nu = 0.07
dt = dx * nu
x = numpy.linspace(0,2 * numpy.pi,nx)
un = numpy.empty(nx)
t = 0
u = numpy.asarray([ufunc(t,x0,nu) for x0 in x])

#plotting
pyplot.figure(figsize = (11,7),dpi = 81)
pyplot.plot(x,u,marker = 'o',lw = 2)
pyplot.xlim([0,2 * numpy.pi])
pyplot.ylim([0,10]);

#back to BURGER'S EQUATION    
for n in range(nt):
    un = u.copy()
    for i in range(1, nx-1):
        u[i] = un[i] - un[i] * dt / dx *(un[i] - un[i-1]) + nu * dt / dx**2 *\
                (un[i+1] - 2 * un[i] + un[i-1])
    u[0] = un[0] - un[0] * dt / dx * (un[0] - un[-2]) + nu * dt / dx**2 *\
                (un[1] - 2 * un[0] + un[-2])
    u[-1] = u[0]
        
u_analytical = numpy.asarray([ufunc(nt * dt, xi, nu) for xi in x])

#results plotting
pyplot.figure(figsize=(11, 7), dpi=81)
pyplot.plot(x,u, marker='o', lw=2, label='Computational')
pyplot.plot(x, u_analytical, label='Analytical')
pyplot.xlim([0, 2 * numpy.pi])
pyplot.ylim([0, 10])
pyplot.legend();
    
