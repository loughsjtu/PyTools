#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 14:01:26 2018
For rank one tensor, the simple vector case
@author: Y. Bai
"""
import numpy as np
import sys

class RankOneTensor:
    def __init__(self,n=None,val=None):

        if n is None:
            self.N=3
        else:
            self.N=n
            
        if val is None:
            self.values=np.zeros(self.N)
        else:
            self.values=np.linspace(val,val,self.N)
        
    
    def PrintTensor(self,str=None):
        if not(str is None):
            print(str)
        print('RankOne Tensor:')
        str1=''
        for i in range(self.N):
            str1+='%14.6E '%(self.values[i])
        str1+='\n'
        print(str1)
    
    def Norm(self):
        return np.linalg.norm(self.values)
    
    def DotProduct(self,RankOneTensorB):
        # Do AiBi
        return np.dot(self.values,RankOneTensorB.values)
    
    def CrossProduct(self,RankOneTensorB):
        # Do AixBj=Cij
        sys.exit('No implementation!')

if __name__=='__main__':
    A=RankOneTensor(3,1.0)
    B=RankOneTensor(3,2.0)
    A.PrintTensor('A')
    B.PrintTensor('B')
    print(A.Norm())
    print(A.DotProduct(B))
    A.CrossProduct(B)
