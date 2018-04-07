import os
import numpy as np
import matplotlib.pylab as plt
import sys


number=int(sys.argv[1])
step1 =int(sys.argv[2])

col = 0
file1=np.zeros((number,1000+1))
position1=np.zeros(1000+1)
r1=np.zeros((number,1000+1))

if(len(sys.argv)>3):
	step2 =int(sys.argv[3])
	file2=np.zeros((number,1000+1))
	r2=np.zeros((number,1000+1))
	name2=repr(step2).zfill(8)+'p.dat'

# ---------------------------------------------------------------------------------
for i in range(number):
	os.chdir('/home/jhzhai/jhzhai/Results/600K/'+'sim'+repr(i+1))
	name1=repr(step1).zfill(8)+'p.dat'
	file1[i]=np.loadtxt(name1,usecols=[col])
	if(len(sys.argv)>3):
		file2[i]=np.loadtxt(name2,usecols=[col])
	for d in range(0,1001,1):
		h1=np.zeros(len(position1)-d)
		if(len(sys.argv)>3):
			h2=np.zeros(len(position1)-d)
		for j in range(0,len(position1)-d):
			h1[j]=file1[i][j]-file1[i][j+d]
			if(len(sys.argv)>3):
				h2[j]=file2[i][j]-file2[i][j+d]
		r1[i][d]=np.mean(np.abs(h1))
		if(len(sys.argv)>3):
			r2[i][d]=np.mean(np.abs(h2))
	print(os.getcwd())
#----------------------------------------------------------------------------------
f1=np.zeros(1000+1)
f2=np.zeros(1000+1)
for i in range(0,number):
	f1=r1[i]+f1
	if(len(sys.argv)>3):
		f2=r2[i]+f2
f1=f1/number
if(len(sys.argv)>3):
	f2=f2/number

begin = 1
end = 999
x=[i for i in range(0,1001)]
plt.plot(np.log(x[begin:end]),np.log(f1[begin:end]),label='step1')
if(len(sys.argv)>3):
	plt.plot(np.log(x[begin:end]),np.log(f2[begin:end]),label='step2')

plt.legend()
plt.show()