# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 10:48:52 2018

@author: Balaji.V
emailid: balaji36918@gmail.com
"""
#importing the libraries
import numpy
from matplotlib import pyplot
import time,sys

#for a notebook view
"""%matplotlib"""

#variables
nx = 21
dx = 2/(nx-1)
nt = 25
dt = 0.025
c = 1 #wavespeed


#Initial conditions
u=numpy.ones(nx)
u[int(0.5/dx) : int(1/dx+1)] = 2

#trying plotting
pyplot.plot(numpy.linspace(0,2,nx),u);

#extract_Solution
un=numpy.ones(nx) #initialize a temporary array

for n in range(nt):
    un=u.copy()
    for i in range(1,nx):
        u[i]=un[i] - c * dt/dx *(un[i] - un[i-1])

#plot the final results
pyplot.plot(numpy.linspace(0,2,nx),u)

