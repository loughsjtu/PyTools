#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 12:13:33 2018

@author: Y. Bai
"""

import os

currentdir=os.getcwd()# run the script in current folder
mod=0;o=0;f90=0
latex=0
for subdir,dirs,files in os.walk(currentdir):
    for file in files:
        if '.mod' in file:
            try:
                mod+=1
                removepath=subdir+'/'+file
                os.remove(removepath)
            except:
                print('%s is not here'%(file))
        elif '.f90' in file:
            try:
                f90+=1
                removepath=subdir+'/'+file
                os.remove(removepath)
            except:
                print('%s is not here'%(file))
        elif '.o' in file:
            try:
                o+=1
                removepath=subdir+'/'+file
                os.remove(removepath)
            except:
                print('%s is not here'%(file))
        elif '.aux' in file:
            try:
                latex+=1
                removepath=subdir+'/'+file
                os.remove(removepath)
            except:
                print('%s is not here'%(file))
        elif '.log' in file:
            try:
                latex+=1
                removepath=subdir+'/'+file
                os.remove(removepath)
            except:
                print('%s is not here'%(file))
        elif 'synctex.gz' in file:
            try:
                latex+=1
                removepath=subdir+'/'+file
                os.remove(removepath)
            except:
                print('%s is not here'%(file))
        elif '.cfg' in file:
            try:
                latex+=1
                removepath=subdir+'/'+file
                os.remove(removepath)
            except:
                print('%s is not here'%(file))
        elif '.def' in file:
            try:
                latex+=1
                removepath=subdir+'/'+file
                os.remove(removepath)
            except:
                print('%s is not here'%(file))
        elif '.bbl' in file:
            try:
                latex+=1
                removepath=subdir+'/'+file
                os.remove(removepath)
            except:
                print('%s is not here'%(file))
        elif '.toc' in file:
            try:
                latex+=1
                removepath=subdir+'/'+file
                os.remove(removepath)
            except:
                print('%s is not here'%(file))
        elif '.lot' in file:
            try:
                latex+=1
                removepath=subdir+'/'+file
                os.remove(removepath)
            except:
                print('%s is not here'%(file))
        elif '.lof' in file:
            try:
                latex+=1
                removepath=subdir+'/'+file
                os.remove(removepath)
            except:
                print('%s is not here'%(file))
        elif '.blg' in file:
            try:
                latex+=1
                removepath=subdir+'/'+file
                os.remove(removepath)
            except:
                print('%s is not here'%(file))
        elif '.out' in file:
            try:
                latex+=1
                removepath=subdir+'/'+file
                os.remove(removepath)
            except:
                print('%s is not here'%(file))



print('Cleaned %5d  .f90   files'%(f90))
print('Cleaned %5d  .mod   files'%(mod))
print('Cleaned %5d  .o     files'%(o))
print('Cleaned %5d  .latex files'%(latex))
