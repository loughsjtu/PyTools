#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 12:57:25 2018

@author: Y. Bai
""" 
import numpy as np
import matplotlib.pyplot as plt

nx=800
ny=nx
x=np.linspace(0.0,10.0,nx)
y=np.linspace(0.0,2.0,ny)
X,Y=np.meshgrid(x,y)
D0=2.0

D=D0*(1.0+np.abs(5.0*np.sin(X)*np.cos(Y)))

#plt.contourf(X,Y,D,cmap=plt.cm.jet,interpolation='bicubic')

#plt.imshow(D,extent=(min(x), max(x), max(y), min(y)),cmap=plt.cm.jet,origin='lower')
plt.pcolor(X,Y,D,cmap=plt.cm.jet)
plt.colorbar()
plt.title('$D=D_{0}(1+abs(5\sin(x)\cos(y)))$',fontsize=12)
plt.xlabel('X',fontsize=12)
plt.ylabel('Y',fontsize=12)
plt.savefig('D.png',dpi=800,bbox_inches='tight')

