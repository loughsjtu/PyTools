#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 09:44:30 2018

@author: Y. Bai
"""
import matplotlib.pyplot as plt
import numpy as np


def phi(x):
    return (x+5)*(x-2)*(x-5)
def dphi(x):
    return 3*x*x-4*x-25


from scipy.optimize import root

x0=np.array([-5.0,0.0,5.0])
sol=root(phi,x0,method='hybr')

x1,x2,x3=sol.x
y1=phi(x1)
y2=phi(x2)
y3=phi(x3)
print(sol)





x=np.linspace(-5.0,5.0,100)
y=phi(x)
dy=dphi(x)
plt.plot(x,y,label='y')
plt.plot(x,dy,label='dy')
plt.legend()

plt.plot(x1,y1,'-*',markersize=12)
str='$x_{1}$=%g'%(x1)
plt.text(x1,-9,str,fontsize=12)


plt.plot(x2,y2,'-+',markersize=12)
str='$x_{2}$=%g'%(x2)
plt.text(x2-1,-9,str,fontsize=12)


plt.plot(x3,y3,'bo',markersize=12)
str='$x_{3}$=%g'%(x3)
plt.text(x3,-9,str,fontsize=12)

plt.xlim([-5.2,5.2])
plt.ylim([-28,88])
str='$y=(x+5)(x-2)(x-5)$'
plt.title(str,fontsize=12)

plt.savefig('Eqs_Ex1.png',dpi=500,bbox_inches='tight')


