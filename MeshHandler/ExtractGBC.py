#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 12:21:06 2018

@author: Y. Bai
"""
### Extract grain's id and grain bc's id
### In the original file each grain bc has an independent id
### now we want to let them use one same id

import re
import matplotlib.pyplot as plt
import numpy as np

w=2.0;h=2.0
filename='n5-id1.geo'
inp=open(filename,'r+')
x=[];y=[]
Conn=[]
line=inp.readline()
staticstr=''
while len(line)>1:
    if 'Point' in line:
        values=re.findall(r"[-+]?\d*\.\d+|\d+",line)
        print(values)
        x.append(float(values[2-1]))
        y.append(float(values[3-1]))
    if 'Line' in line and 'Loop' not in line and 'Physical' not in line:
        nodeid=[]
        values=re.findall(r"[-+]?\d*\.\d+|\d+",line)
        print(values)
        nodeid.append(int(values[2-1]))
        nodeid.append(int(values[3-1]))
        Conn.append(nodeid)
    if 'Line Loop' in line or 'Plane Surface' in line or 'Physical Surface' in line:
        staticstr+=line
    line=inp.readline()
inp.close()

tol=1.0e-9
def IsOnBoundary(x,y,w,h):
    # Left edge
    if np.abs(x[0]-0.0)<tol and np.abs(x[1]-0.0)<tol:
        return True
    # Bottom edge
    elif np.abs(y[0]-0.0)<tol and np.abs(y[1]-0.0)<tol:
        return True
    # Right edge
    elif np.abs(x[0]-w)<tol and np.abs(x[1]-w)<tol:
        return True
    # Top edge
    elif np.abs(y[0]-h)<tol and np.abs(y[1]-h)<tol:
        return True
    else:
        # non boundary case
        return False

plt.figure(1)
plt.hold
BCLineID=[]
GBCLineID=[]
for i in range(len(Conn)):
    xi=[x[Conn[i][0]-1],x[Conn[i][1]-1]]
    yi=[y[Conn[i][0]-1],y[Conn[i][1]-1]]
    if IsOnBoundary(xi,yi,w,h):
        BCLineID.append(i+1)
        plt.plot(xi,yi,'k')
    else:
        GBCLineID.append(i+1)
        plt.plot(xi,yi)
plt.savefig('Grains.png',dpi=800,bbox_inches='tight')
### Output new geo file
filename='newid.geo'
inp=open(filename,'w+')
dx=0.03
str='dx=%f;\n'%(dx)
inp.write(str)
for i in range(len(x)):
    str='Point (%d) = {%f,%f,%f,dx};\n'%(i+1,x[i],y[i],0.0)
    inp.write(str)
for i in range(len(Conn)):
    str='Line (%d)={%d,%d};\n'%(i+1,Conn[i][0],Conn[i][1])
    inp.write(str)

# Output static str
inp.write(staticstr)

# Now output all boundary edge id
for i in range(len(BCLineID)):
    str='Physical Line(%d)={%d};\n'%(len(Conn)+i+1,BCLineID[i])
    inp.write(str)
# For grain bc id
str=''
if len(GBCLineID)==1:
    str='%d'%(GBCLineID[i])
elif len(GBCLineID)>1:
    str='%d'%(GBCLineID[0])
    for i in range(1,len(GBCLineID)):
        str+=',%d'%(GBCLineID[i])
else:
    str=''

if len(str)>1:
    str1='Physical Line(%d)={'%(len(Conn)+len(BCLineID)+1)
    str=str1+str+'};\n'
    inp.write(str)

inp.close()
print('New geo file is finished!')

