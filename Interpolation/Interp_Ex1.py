#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 09:44:30 2018

@author: Y. Bai
"""
import numpy as np
import matplotlib.pyplot as plt

from scipy.interpolate import InterpolatedUnivariateSpline


# Sample point or the original source point
x0=[  1.0,2.0, 3.0,4.0,5.0,6.0]
y0=[-10.0,1.0,-2.0,3.0,5.0,7.8]

# the point we want to do interpolation or extrapolation
nx=100
xi=np.linspace(1.0,6.0,nx)

p=1 # First order
s=InterpolatedUnivariateSpline(x0,y0,k=p)
y1=s(xi)

p=2 # Second order
s=InterpolatedUnivariateSpline(x0,y0,k=p)
y2=s(xi)

p=3 # Third order
s=InterpolatedUnivariateSpline(x0,y0,k=p)
y3=s(xi)

p=4 # Fourth order
s=InterpolatedUnivariateSpline(x0,y0,k=p)
y4=s(xi)

p=5 # Fifth order
s=InterpolatedUnivariateSpline(x0,y0,k=p)
y5=s(xi)


plt.plot(x0,y0,'-k',label='Origin')
plt.plot(xi,y1,':',label='P=1')
plt.plot(xi,y2,'--',label='P=2')
plt.plot(xi,y3,'-.',label='P=3')
plt.plot(xi,y4,'-+',label='P=4')
plt.plot(xi,y5,label='P=5')


plt.legend(loc=4,fontsize=12)
plt.xlabel('$x$',fontsize=12)
plt.ylabel('$y$',fontsize=12)
plt.xlim([1.0,6.0])
plt.ylim([-9.9,8.0])

plt.savefig('Interp_Ex1.png',dpi=500,bbox_inches='tight')
