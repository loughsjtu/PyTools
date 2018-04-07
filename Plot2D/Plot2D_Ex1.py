#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 09:44:30 2018

@author: Y. Bai
"""
import matplotlib.pyplot as plt
import numpy as np

nx=100
x=np.linspace(0.0,2.0*np.pi,nx)
y=np.sin(x)

plt.plot(x,y)
plt.xlabel('$x$',fontsize=12)
plt.ylabel('$\sin (x)$',fontsize=12)
y=[np.min(y),np.min(y),np.max(y),np.max(y)]
z=[1.,1.,1.,1.]
x=[0.0,np.pi,np.pi,0.0]
plt.tricontourf(x,y,z,colors='green',alpha=0.2)
x=[np.pi,2*np.pi,2*np.pi,np.pi]
plt.tricontourf(x,y,z,colors='blue',alpha=0.2)
plt.text(1.0,-0.75,'Left',fontsize=12)
plt.text(4.5,-0.75,'Right',fontsize=12)
plt.savefig('Plot2D_Ex1.png',dpi=500,bbox_inches='tight')
