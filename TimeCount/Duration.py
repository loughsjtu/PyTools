#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 09:25:19 2018

@author: Y. Bai
"""
import datetime

StartTime=datetime.datetime.strptime('2018-04-06T20:39:52Z', '%Y-%m-%dT%H:%M:%SZ')
EndTime=datetime.datetime.strptime('2018-04-06T23:13:21Z', '%Y-%m-%dT%H:%M:%SZ')

#a=time.mktime(StartTime)
#b=time.mktime(EndTime)

d=EndTime-StartTime
minutes=d.days*24.0*60.0+d.seconds/60.0

print('Using time=%g min'%(minutes))
