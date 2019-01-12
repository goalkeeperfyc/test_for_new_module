#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 12:01:43 2019

@author: fangyucheng
Email: 664947387@qq.com
"""

import pandas as pd

#this is a way to get max value. it returns with the max value without other information

d = {
'Name':['Alisa','Bobby','jodha','jack','raghu','Cathrine',
'Alisa','Bobby','kumar','Alisa','Alex','Cathrine'],
'Age':[26,24,23,22,23,24,26,24,22,23,24,24],
 
'Score':[85,63,55,74,31,77,85,63,42,62,89,77]}
 
df = pd.DataFrame(d,columns=['Name','Age','Score'])
df.max()
df['Age'].max()