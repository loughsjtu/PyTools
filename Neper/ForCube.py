#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 14:01:26 2018
First use Neper to generate a geo file
then add physical groups(surface and volume) to
the geo file(append)
@author: Y. Bai
"""
import numpy as np 
import re

def SplitNum(str):
    return [float(s) for s in re.findall(r'-?\d+\.?\d*',str)]

filename='cube50.geo'

Xmax=-1.0e12;Xmin=1.0e12
Ymax=-1.0e12;Ymin=1.0e12
Zmax=-1.0e12;Zmin=1.0e12

nPoints=0;nGrains=0;nSurface=0;nLines=0;nVolume=0
nLineLoops=0
###################################################
### Read geo file to get geometry information   ###
###################################################
inp=open(filename,'r+')
line=inp.readline()
while len(line)>0:
    if 'Point (' in line:
        nPoints+=1
        numbers=SplitNum(line)
        if numbers[1]>Xmax:
            Xmax=numbers[1]
        if numbers[1]<Xmin:
            Xmin=numbers[1]

        if numbers[2]>Ymax:
            Ymax=numbers[2]
        if numbers[2]<Ymin:
            Ymin=numbers[2]

        if numbers[3]>Zmax:
            Zmax=numbers[3]
        if numbers[3]<Zmin:
            Zmin=numbers[3]
    elif 'Line (' in line:
        nLines+=1
    elif 'Line Loop (' in line:
        nLineLoops+=1
    elif 'Plane Surface (' in line:
        nSurface+=1
    elif 'Volume (' in line:
        nVolume+=1
    
    line=inp.readline()
inp.close()

print('nPoints=',nPoints)
print('nLines=',nLines)
print('nSurfaces=',nSurface)
print('nVolumes=',nVolume)

print('Xmin=%.5f, Xmax=%.5f\n'%(Xmin,Xmax))
print('Ymin=%.5f, Ymax=%.5f\n'%(Ymin,Ymax))
print('Zmin=%.5f, Zmax=%.5f\n'%(Zmin,Zmax))

################################
### Store points information


inp=open(filename,'r+')
line=inp.readline()

Points=np.zeros((nPoints,3))
npoints=0

Lines=np.zeros((nLines,2),dtype=np.int)
nlines=0

LineLoop=np.zeros((nLineLoops,20),dtype=np.int)
nlineloop=0

while len(line)>1:
    if 'Point (' in line:
        numbers=SplitNum(line)
        #t=re.findall('\d+',line)
        Points[npoints,0]=numbers[1]
        Points[npoints,1]=numbers[2]
        Points[npoints,2]=numbers[3]
        npoints+=1
    elif 'Line (' in line:
        numbers=SplitNum(line)
        Lines[nlines,0]=int(numbers[1])
        Lines[nlines,1]=int(numbers[2])
        nlines+=1
    elif 'Line Loop (' in line:
        numbers=SplitNum(line)
        size=len(numbers)-1
        LineLoop[nlineloop,0]=size 
        for i in range(size):
            LineLoop[nlineloop,1+i]=int(np.abs(numbers[1+i]))
        nlineloop+=1
    line=inp.readline()
inp.close()

#####################################
### check physical group information
#####################################
tol=1.0e-5
def IsLeftBCLine(node1,node2):
    Node1=False;Node2=False
    if np.abs(Points[node1-1,0]-Xmin)<tol:
        Node1=True
    if np.abs(Points[node2-1,0]-Xmin)<tol:
        Node2=True
    
    if Node1 and Node2:
        return True
    else:
        return False
def IsRightBCLine(node1,node2):
    Node1=False;Node2=False
    if np.abs(Points[node1-1,0]-Xmax)<tol:
        Node1=True
    if np.abs(Points[node2-1,0]-Xmax)<tol:
        Node2=True
    
    if Node1 and Node2:
        return True
    else:
        return False
######################################
def IsBottomBCLine(node1,node2):
    Node1=False;Node2=False
    if np.abs(Points[node1-1,1]-Ymin)<tol:
        Node1=True
    if np.abs(Points[node2-1,1]-Ymin)<tol:
        Node2=True
    
    if Node1 and Node2:
        return True
    else:
        return False
def IsTopBCLine(node1,node2):
    Node1=False;Node2=False
    if np.abs(Points[node1-1,0]-Ymax)<tol:
        Node1=True
    if np.abs(Points[node2-1,0]-Ymax)<tol:
        Node2=True
    
    if Node1 and Node2:
        return True
    else:
        return False
###############################
def IsBackBCLine(node1,node2):
    Node1=False;Node2=False
    if np.abs(Points[node1-1,0]-Zmin)<tol:
        Node1=True
    if np.abs(Points[node2-1,0]-Zmin)<tol:
        Node2=True
    
    if Node1 and Node2:
        return True
    else:
        return False
def IsFrontBCLine(node1,node2):
    Node1=False;Node2=False
    if np.abs(Points[node1-1,0]-Zmax)<tol:
        Node1=True
    if np.abs(Points[node2-1,0]-Zmax)<tol:
        Node2=True
    
    if Node1 and Node2:
        return True
    else:
        return False

Left=[];Right=[]
Bottom=[];Top=[]
Back=[];Front=[]
print(LineLoop)
for i in range(nLineLoops):
    IsOnLeftBC=True;IsOnRightBC=True
    IsOnBottomBC=True;IsOnTopBC=True
    IsOnBackBC=True;IsOnFrontBC=True

    for j in range(LineLoop[i,0]):
        i1=int(Lines[LineLoop[i,j+1]-1,0])
        i2=int(Lines[LineLoop[i,j+1]-1,1])
        if IsLeftBCLine(i1,i2):
            print('x1=%.5f, x2=%.5f\n'%(Points[i1-1,0],Points[i2-1,0]))
        if not IsLeftBCLine(i1,i2):
            IsOnLeftBC=False
        if not IsRightBCLine(i1,i2):
            IsOnRightBC=False
        if not IsBottomBCLine(i1,i2):
            IsOnBottomBC=False
        if not IsTopBCLine(i1,i2):
            IsOnTopBC=False
        if not IsBackBCLine(i1,i2):
            IsOnBackBC=False
        if not IsFrontBCLine(i1,i2):
            IsOnFrontBC=False
    
    if IsOnLeftBC:
        Left.append(i+1)
    if IsOnRightBC:
        Right.append(i+1)

    if IsOnBottomBC:
        Bottom.append(i+1)
    if IsOnTopBC:
        Top.append(i+1)

    if IsOnBackBC:
        Back.append(i+1)
    if IsOnFrontBC:
        Front.append(i+1)

print('Left=',Left)
print('Right=',Right)

print('Bottom=',Bottom)
print('Top=',Top)

print('Back=',Back)
print('Front=',Front)

inp=open(filename,'a')
inp.write('\n\n\n\n\n')

str='Physical Surface("Left")={'
for i in range(len(Left)-1):
    str+='%d,'%(Left[i])
str+='%d'%(Left[-1])
str+='};\n'
inp.write(str)
inp.write('\n')

str='Physical Surface("Right")={'
for i in range(len(Right)):
    str+='%d,'%(Right[i])
str+='%d'%(Right[-1])
str+='};\n'
inp.write(str)
inp.write('\n')

str='Physical Surface("Bottom")={'
for i in range(len(Bottom)-1):
    str+='%d,'%(Bottom[i])
str+='%d'%(Bottom[-1])
str+='};\n'
inp.write(str)
inp.write('\n')

str='Physical Surface("Top")={'
for i in range(len(Top)-1):
    str+='%d,'%(Top[i])
str+='%d'%(Top[-1])
str+='};\n'
inp.write(str)
inp.write('\n')

str='Physical Surface("Back")={'
for i in range(len(Back)-1):
    str+='%d,'%(Back[i])
str+='%d'%(Back[-1])
str+='};\n'
inp.write(str)
inp.write('\n')

str='Physical Surface("Front")={'
for i in range(len(Front)-1):
    str+='%d,'%(Front[i])
str+='%d'%(Front[-1])
str+='};\n'
inp.write(str)
inp.write('\n\n\n')


for i in range(nVolume):
    str='Physical Volume(%d)={%d};\n'%(i+1,i+1)
    inp.write(str)


inp.close()
        