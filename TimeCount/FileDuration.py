#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 09:31:41 2018

@author: Y. Bai
This script get current folder's files create date and last modify date and
the duration
"""

import os
import time


currentdir=os.getcwd()# run the script in current folder
mod=0;o=0;f90=0
latex=0
for subdir,dirs,files in os.walk(currentdir):
    for file in files:
        ModifyTime=time.ctime(os.path.getmtime(file))
        CreateTime=time.ctime(os.path.getctime(file))
        StartTime=os.path.getctime(file)
        EndTime=os.path.getmtime(file)
        d=EndTime-StartTime
        minutes=d/60.0
        print('%s \n\t created:%s \n\t last modified:%s'%(file,ModifyTime,CreateTime))
        print('\t Duration time:%g mins'%(minutes))
        
