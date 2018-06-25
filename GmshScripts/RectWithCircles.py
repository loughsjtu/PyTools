#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 14:01:26 2018
Try to write a simple msh file for MOOSE
@author: Y. Bai
"""

#######################################################
### This script is applied for a rectangle domain   ###
### embeded several circles with different radius   ###
### Write all the information to .geo file          ###
### Since I have my own code to split the interface ###
### I don't do the interface things here            ###
#######################################################


import numpy as np


width=20.0;height=8.0 # for the width and height of rectangle domain

dx=1.0 # the mesh size
nCircles=9 # number of required circles which will be embedded in the domain

Rmax=np.min([width,height])/2.0
Rmin=1.5

filename='rectwithcircles.geo'
inp=open(filename,'w+')
### set title
inp.write('SetFactory("OpenCASCADE");\n\n')
### set parameter information
inp.write('dx=%.5f;\n'%(dx))
inp.write('w =%.5f;\n'%(width))
inp.write('h =%.5f;\n'%(height))

### For four corner nodes
inp.write('Point (1)={0.0,0.0,0.0,dx};\n')
inp.write('Point (2)={  w,0.0,0.0,dx};\n')
inp.write('Point (3)={  w,  h,0.0,dx};\n')
inp.write('Point (4)={0.0,  h,0.0,dx};\n\n')

inp.write('Line (1)={1,2};\n')
inp.write('Line (2)={2,3};\n')
inp.write('Line (3)={3,4};\n')
inp.write('Line (4)={4,1};\n\n')

##################################################
### define the function to generate circles    ###
##################################################
gap=0.5
def IsInList(xi,yi,ri,X,Y,R):
    IsIn=False
    if(len(X)<=0):
        return False
    for i in range(len(X)):
        dist=(xi-X[i])**2+(yi-Y[i])**2
        dist=np.sqrt(dist)
        if(dist<ri+R[i]+gap):
            IsIn=True
            return IsIn
    return IsIn

def IsInRect(xi,yi,ri,w,h):
    xmin=xi-ri;xmax=xi+ri 
    ymin=yi-ri;ymax=yi+ri 
    if (xmin>gap and xmax<w-gap) and (ymin>gap and ymax<h-gap):
        return True
    else:
        return False

def GenerateCircles(n):
    x=[];y=[];r=[]
    np.random.seed()
    for i in range(n):
        iTry=0;MaxTry=500000
        while iTry<=MaxTry:
            xi=(Rmin+gap)+(width -2.0*(Rmin+gap))*np.random.rand()
            yi=(Rmin+gap)+(height-2.0*(Rmin+gap))*np.random.rand()
            ri=Rmin+(Rmax-Rmin)*np.random.rand()
            iTry+=1
            if (not IsInList(xi,yi,ri,x,y,r)) and IsInRect(xi,yi,ri,width,height):
                x.append(xi)
                y.append(yi)
                r.append(ri)
                print('%2d-th circle: x=%12.4f, y=%12.4f, r=%12.4f-->iTry=%5d\n'%(i+1,xi,yi,ri,iTry))
                break
    
    print('Circle generation finished!\n')
    return x,y,r

X,Y,R=GenerateCircles(nCircles)

### Now we write circle's information to geo file
iStart=4 # there is already four lines before
for i in range(len(X)):
    inp.write('Circle (%2d)={%.5f,%.5f,0.0,%.5f,0.0,2*Pi};\n'%(i+1+iStart,X[i],Y[i],R[i]))

inp.write('\nLine Loop( 1)={1,2,3,4};\n')
inp.write('Plane Surface( 1)={1};\n')
for i in range(len(X)):
    inp.write('\nLine Loop(%2d)={%3d};\n'%(i+1+1,i+1+iStart))
    inp.write('Plane Surface(%2d)={%3d};\n'%(i+1+1,i+1+1))

### Now we do boolean operation to split the circles from rectangle
str='\nBooleanDifference(%d) = { Surface{1}; Delete;}{'%(i+1+1+1)
substr=''
for i in range(len(X)):
    substr+='Surface{%2d};'%(i+1+1)
str+=substr+'Delete; };\n'

inp.write(str)
inp.write('Physical Surface ("box")={%2d};\n\n'%(i+1+1+1))

iStart=i+1+1+1
### Create the deleted circles(after bool operation, they are removed!)
for i in range(len(X)):
    inp.write('Line Loop(%2d)={%2d};\n'%(i+1+iStart,4+i+1))
    inp.write('Plane Surface (%2d)={%2d};\n'%(i+1+iStart,i+1+iStart))
    inp.write('Physical Surface ("circle%-2d")={%2d};\n\n'%(i+1,i+1+iStart))

str='Physical Line("left") = {2};\n'+\
    'Physical Line("right") = {3};\n'+\
    'Physical Line("bottom") = {1};\n'+\
    'Physical Line("top") = {4};\n'

inp.write(str)

inp.close()