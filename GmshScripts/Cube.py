#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 14:01:26 2018
Try to write a simple msh file for MOOSE
@author: Y. Bai
"""
import numpy as np

class Cube:
    def __init__(self,cx,cy,cz,w,h,d,dx):
        self.cx=cx 
        self.cy=cy
        self.cz=cz
        self.dx=dx
        self.w=w
        self.h=h
        self.d=d
        self.xmin=cx-w 
        self.xmax=cx+w
        self.ymin=cy-h
        self.ymax=cy+h
        self.zmin=cz-d
        self.zmax=cz+d
        self.X=np.array([self.xmin,self.xmax,self.xmax,self.xmin,
                         self.xmin,self.xmax,self.xmax,self.xmin])
        self.Y=np.array([self.ymin,self.ymin,self.ymax,self.ymax,
                         self.ymin,self.ymin,self.ymax,self.ymax])
        self.Z=np.array([self.zmin,self.zmin,self.zmin,self.zmin,
                         self.zmax,self.zmax,self.zmax,self.zmax])  

    def SetPointStartIndex(self,i):
        self.PointStartIndex=i
        i+=8
        return i

    def SetLineStartIndex(self,i):
        self.LineStartIndex=i 
        i+=6 
        return i  

    def SetPlaneSurfaceStartIndex(self,i):
        self.PlaneSurfaceStartIndex=i
        i+=6
        return i
    
    def SetVolumeStartIndex(self,i):
        self.VolumeStartIndex=i
        i+=1
        return i

    def SetLineLoopStartIndex(self,i):
        self.LineLoopStartIndex=i
        i+=6 
        return i   

    def SetSurfaceLoopStartIndex(self,i):
        self.SurfaceLoopStartIndex=i
        i+=1
        return i

    def GenerateGEOinfo(self):
        #====> Define point information
        self.Point=''
        for i in range(8):
            str='Point(%5d)={%14.6f,%14.6f,%14.6f,%12.4f};\n'%(i+self.PointStartIndex,self.X[i],self.Y[i],self.Z[i],self.dx)
            self.Point+=str
        #=====> Define line information
        self.Line=''
        for i in range(8):
            if i==4-1:
                i1=1+self.LineStartIndex-1
            elif i==8-1:
                i1=5+self.LineStartIndex-1
            else:
                i1=i+1+self.LineLoopStartIndex
            str='Line(%5d)={%5d,%5d};\n'%(i+self.LineStartIndex,i+self.LineStartIndex,i1)
            self.Line+=str
        for i in range(4):
            i1=i+4+self.LineStartIndex
            str='Line(%5d)={%5d,%5d};\n'%(i+self.LineStartIndex+8,i+self.LineStartIndex,i1)
            self.Line+=str
        #====> For line loop and plane surface
        self.LineLoop=''
        self.PlaneSurface=''
        # bottom surface
        i=1+self.LineLoopStartIndex-1
        i1=1+self.LineStartIndex-1;i2=2+self.LineStartIndex-1
        i3=3+self.LineStartIndex-1;i4=4+self.LineStartIndex-1
        self.LineLoop+='Line Loop(%5d)={%5d,%5d,%5d,%5d};\n'%(i,i1,i2,i3,i4)
        self.PlaneSurface+='Plane Surface(%5d)={%5d};\n'%(i,i)
        # top surface
        i=2+self.LineLoopStartIndex-1
        i1=5+self.LineStartIndex-1;i2=6+self.LineStartIndex-1
        i3=7+self.LineStartIndex-1;i4=8+self.LineStartIndex-1
        self.LineLoop+='Line Loop(%5d)={%5d,%5d,%5d,%5d};\n'%(i,i1,i2,i3,i4)
        self.PlaneSurface+='Plane Surface(%5d)={%5d};\n'%(i,i)
        # left surface
        i=3+self.LineLoopStartIndex-1
        i1=4+self.LineStartIndex-1;i2=9+self.LineStartIndex-1
        i3=8+self.LineStartIndex-1;i4=12+self.LineStartIndex-1
        self.LineLoop+='Line Loop(%5d)={%5d,%5d,%5d,%5d};\n'%(i,i1,i2,-i3,-i4)
        self.PlaneSurface+='Plane Surface(%5d)={%5d};\n'%(i,i)
        # right surface
        i=4+self.LineLoopStartIndex-1
        i1=4+self.LineStartIndex-1;i2=9+self.LineStartIndex-1
        i3=8+self.LineStartIndex-1;i4=12+self.LineStartIndex-1
        self.LineLoop+='Line Loop(%5d)={%5d,%5d,%5d,%5d};\n'%(i,i1,i2,-i3,-i4)
        self.PlaneSurface+='Plane Surface(%5d)={%5d};\n'%(i,i)
        # front surface
        i=5+self.LineLoopStartIndex-1
        i1=1+self.LineStartIndex-1;i2=10+self.LineStartIndex-1
        i3=5+self.LineStartIndex-1;i4= 9+self.LineStartIndex-1
        self.LineLoop+='Line Loop(%5d)={%5d,%5d,%5d,%5d};\n'%(i,i1,i2,-i3,-i4)
        self.PlaneSurface+='Plane Surface(%5d)={%5d};\n'%(i,i)
        # back surface
        i=6+self.LineLoopStartIndex-1
        i1=3+self.LineStartIndex-1;i2=12+self.LineStartIndex-1
        i3=7+self.LineStartIndex-1;i4=11+self.LineStartIndex-1
        self.LineLoop+='Line Loop(%5d)={%5d,%5d,%5d,%5d};\n'%(i,i1,i2,-i3,-i4)
        self.PlaneSurface+='Plane Surface(%5d)={%5d};\n'%(i,i)
        #====> For surface loop
        i=1+self.SurfaceLoopStartIndex-1
        i1=1+self.PlaneSurfaceStartIndex-1;i2=2+self.PlaneSurfaceStartIndex-1
        i3=3+self.PlaneSurfaceStartIndex-1;i4=4+self.PlaneSurfaceStartIndex-1
        i5=5+self.PlaneSurfaceStartIndex-1;i6=6+self.PlaneSurfaceStartIndex-1
        self.SurfaceLoop='Surface Loop(%5d)={%5d,%5d,%5d,%5d,%5d,%5d};\n'%(i,i1,i2,i3,i4,i5,i6)
        #====> For volume
        k=1+self.VolumeStartIndex-1
        self.Volume='Volume(%5d)={%5d};\n'%(k,i)


        

    
    def Print(self):
        print('Cubic information:')
        print('   cx  =%12.4f,%12.4f,%12.4f'%(self.cx,self.cy,self.cz))
        print('   dx  =%14.6f'%(self.dx))
        print('   xmin=%12.4f, xmax=%12.4f'%(self.xmin,self.xmax))
        print('   ymin=%12.4f, ymax=%12.4f'%(self.ymin,self.ymax))
        print('   zmin=%12.4f, zmax=%12.4f'%(self.zmin,self.zmax))
        print('   the points\'s coordinates: ')
        for i in range(8):
            print('   %d-th node: x=%10.3f, y=%10.3f, z=%10.3f'%(i+1,self.X[i],self.Y[i],self.Z[i]))
    def PrintGEOinfo(self):
        print(self.Point)
        print(self.Line)
        print(self.LineLoop)
        print(self.PlaneSurface)
        print(self.SurfaceLoop)
        print(self.Volume)

    def WriteToGEOfile(self,inp):
        inp.write(self.Point)
        inp.write(self.Line)
        inp.write(self.LineLoop)
        inp.write(self.PlaneSurface)
        inp.write('\n\n')    



filename='cube.geo'
inp=open(filename,'w+')

PointIndex=1;LineIndex=1
LineLoopIndex=1;PlaneSurfaceIndex=1
SurfaceLoopIndex=1;VolumeIndex=1

Cubes=[]

cube1=Cube(1,1,1,1,1,1,0.05)
cube1.SetPointStartIndex(PointIndex)
cube1.SetLineStartIndex(LineIndex)
cube1.SetLineLoopStartIndex(LineLoopIndex)
cube1.SetPlaneSurfaceStartIndex(PlaneSurfaceIndex)
cube1.SetSurfaceLoopStartIndex(SurfaceLoopIndex)
cube1.SetVolumeStartIndex(VolumeIndex)

Cubes.append(cube1)


cube2=Cube(3,1,1,1,1,1,0.02)
cube2.SetPointStartIndex(PointIndex)
cube2.SetLineStartIndex(LineIndex)
cube2.SetLineLoopStartIndex(LineLoopIndex)
cube2.SetPlaneSurfaceStartIndex(PlaneSurfaceIndex)
cube2.SetSurfaceLoopStartIndex(SurfaceLoopIndex)
cube2.SetVolumeStartIndex(VolumeIndex)

Cubes.append(cube2)

for i in range(len(Cubes)):
    Cubes[i].GenerateGEOinfo()
    Cubes[i].WriteToGEOfile(inp)
    Cubes[i].PrintGEOinfo()