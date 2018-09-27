# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 18:41:16 2018

@author: Balaji V
emailid: balaji36918@gmail.com
"""

from mpl_toolkits.mplot3d import Axes3D

import numpy
from matplotlib import pyplot, cm

#variable declarations
nx = 81
ny = 81
nt = 100
c = 1
dx = 2 / (nx - 1)
dy = 2 / (ny-1)
sigma = 0.2
dt = sigma * dx

#Creating arrays
x = numpy.linspace(0,2,nx)
y = numpy.linspace(0,2,ny)

#CREATING A ONE-DIMENSION VECTOR OF 1'S
u = numpy.ones((ny,nx))
un = numpy.ones((ny,nx))

#Assign initial conditions
#for both x & y
#0.5<=x<=1 use hat fn
u[int(0.5 / dx) : int(1/dx+1), int(0.5/dy) : int(1/dy+1)] = 2

#plot initial conditions
fig = pyplot.figure(figsize=(11,7),dpi=100)
ax = fig.gca(projection='3d')
X,Y = numpy.meshgrid(x,y)
surf = ax.plot_surface(X,Y, u[:], cmap=cm.viridis)

#Iterating to find the required : u
#v r doing this in 2d 1st time ,Cheers!

u = numpy.ones((ny,nx))
u[int(0.5 / dx) : int(1/dx+1), int(0.5/dy) : int(1/dy+1)] = 2

#loop across no.of time steps
for n in range(nt + 1):
    un = u.copy()
    row,col = u.shape
    for j in range(1,row):
        for i in range(1,col):
            u[j, i] = (un[j, i] - (c * dt / dx * (un[j, i] - un[j, i - 1])) -
             (c * dt / dy * (un[j, i] - un[j - 1, i])))
            u[0, :] = 1
            u[-1, :] = 1
            u[:, 0] = 1
            u[:, -1] = 1    
            

fig = pyplot.figure(figsize=(11,7), dpi=100)
ax = fig.gca(projection = '3d')
surf2 = ax.plot_surface(X,Y, u[:], cmap=cm.viridis)

















            




















