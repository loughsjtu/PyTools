#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 14:01:26 2018
Try to write a simple msh file for MOOSE
@author: Y. Bai
"""
import numpy as np
import matplotlib.pyplot as plt

x1=1.0;x2=2.0;h=1.0

# Define node's coordinates
X=np.array([0.0,x1,x2,0.0,x1,x2])
Y=np.array([0.0,0.0,0.0,h,h,h])

# Define element's connectivity
Conn=np.zeros((4,3),dtype=np.int32)
Conn[0][:]=np.array([1,2,5])
Conn[1][:]=np.array([2,3,5])
Conn[2][:]=np.array([1,5,4])
Conn[3][:]=np.array([5,3,6])
print(Conn)

inp=open('test.msh','w+')

# Header line for msh file
inp.write('$MeshFormat\n')
version_number=2.2;file_type=0;data_size=8
str='%.1f %d %d\n'%(version_number,file_type,data_size)
inp.write(str)
inp.write('$EndMeshFormat\n')

# For physical names
inp.write('$PhysicalNames\n')
nPhysics=4+4
inp.write('%d\n'%(nPhysics))
# for 4-boundary edges
inp.write('1 1 \"left\"\n')
inp.write('1 2 \"right\"\n')
inp.write('1 3 \"bottom\"\n')
inp.write('1 4 \"top\"\n')

inp.write('1 5 \"interface\"\n')

# for 4 blocks
inp.write('2 6  \"A\"\n')
inp.write('2 7  \"B\"\n')
inp.write('2 8  \"C\"\n')
inp.write('2 9  \"D\"\n')

inp.write('$EndPhysicalNames\n')

#######################################
### Write node's coordinates
#######################################
inp.write('$Nodes\n')
inp.write('%d\n'%(np.size(X)))
for i in range(np.size(X)):
    str='%-5d %14.6e %14.6e %14.6e\n'%(i+1,X[i],Y[i],0.0)
    inp.write(str)
inp.write('$EndNodes\n')

#######################################
### Write element information
#######################################
inp.write('$Elements\n')
elmt_numer=4+6
inp.write('%d\n'%elmt_numer)
# First print line element(only the boundary element)
elm_type=1
i=1
str='%-5d %d 2 %d %d %d %d\n'%(i,elm_type,3,1,1,2)
inp.write(str)
i=2
str='%-5d %d 2 %d %d %d %d\n'%(i,elm_type,3,1,2,3)
inp.write(str)
i=3
str='%-5d %d 2 %d %d %d %d\n'%(i,elm_type,2,1,3,6)
inp.write(str)
i=4
str='%-5d %d 2 %d %d %d %d\n'%(i,elm_type,4,1,6,5)
inp.write(str)
i=5
str='%-5d %d 2 %d %d %d %d\n'%(i,elm_type,4,1,5,4)
inp.write(str)
i=6
str='%-5d %d 2 %d %d %d %d\n'%(i,elm_type,1,1,4,1)
inp.write(str)


# Now for bulck element information
elm_type=2
i+=1
str='%-5d %d 2 %d %d %d %d %d\n'%(i,elm_type,4+1,elm_type,1,2,5)
inp.write(str)
i+=1
str='%-5d %d 2 %d %d %d %d %d\n'%(i,elm_type,4+2,elm_type,2,3,5)
inp.write(str)
i+=1
str='%-5d %d 2 %d %d %d %d %d\n'%(i,elm_type,4+3,elm_type,1,5,4)
inp.write(str)
i+=1
str='%-5d %d 2 %d %d %d %d %d\n'%(i,elm_type,4+4,elm_type,3,6,5)
inp.write(str)

inp.write('$EndElements\n')
inp.close()
