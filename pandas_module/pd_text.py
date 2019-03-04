#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 10:21:28 2019

@author: fangyucheng
Email: 664947387@qq.com
"""

import pandas as pd
import numpy as np

doc = []
with open('dates.txt') as file:
    for line in file:
        doc.append(line)

df = pd.Series(doc)
df.head(10)
a1_1 =df.str.extractall(r'(\d{1,2})[/-](\d{1,2})[/-](\d{2})\b')
a1_2 =df.str.extractall(r'(\d{1,2})[/-](\d{1,2})[/-](\d{4})\b')
a1 = pd.concat([a1_1,a1_2])
a1.reset_index(inplace=True)
a1_index = a1['level_0']

a2 = df.str.extractall(r'((?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*[-.]* )((?:\d{1,2}[?:, -]*)\d{4})')
a2.reset_index(inplace=True)
a2_index = a2['level_0']

a3 = df.str.extractall(r'((?:\d{1,2} ))?((?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*[?:, -]* )(\d{4})')
a3.reset_index(inplace=True)
a3_index = a3['level_0']

a6 = df.str.extractall(r'(\d{1,2})[/](\d{4})')
a6.reset_index(inplace=True)
a6_index = a6['level_0']
save=[]
for i in a6_index:
    if not(i in a1_index.values):
        save.append(i)
save = np.asarray(save)
a6 = a6[a6['level_0'].isin(save)]


a7_1= df.str.extractall(r'[a-z]?[^0-9](\d{4})[^0-9]')
a7_2 = df.str.extractall(r'^(\d{4})[^0-9]')
a7 = pd.concat([a7_1,a7_2])
a7.reset_index(inplace=True)

a7_index = a7['level_0']
save=[]
for i in a7_index:
    if not((i in a2_index.values) | (i in a3_index.values) | (i in a6_index.values)):
        save.append(i)
save = np.asarray(save)
a7 = a7[a7['level_0'].isin(save)]

s = a1.level_0.values.tolist()+a2.level_0.values.tolist()+a3.level_0.values.tolist()+a6.level_0.values.tolist()+a7.level_0.values.tolist()
s = np.asarray(s)

a1.columns=['level_0','match','month','day','year']
a1['year']=a1['year'].apply(str)
a1['year']=a1['year'].apply(lambda x: '19'+x if len(x)<=2 else x)
   
a2[1] = a2[1].apply(lambda x: x.replace(',',''))
a2['day'] = a2[1].apply(lambda x:x.split(' ')[0])
a2['year'] = a2[1].apply(lambda x:x.split(' ')[1])
a2.columns=['level_0','match','month','day-year','day','year']
a2.drop('day-year',axis=1,inplace=True) 

a3.columns=['level_0','match','day','month','year']
a3['day'] = a3['day'].replace(np.nan,-99)
a3['day'] = a3['day'].apply(lambda x: 1 if int(x)==-99 else x)

a3['month'] = a3.month.apply(lambda x: x[:3])
a3['month'] = pd.to_datetime(a3.month, format='%b').dt.month

a6.columns=['level_0','match','month','year']
a6['day']=1
  
a7.columns=['level_0','match','year']
a7['day']=1
a7['month']=1
   
final = pd.concat([a1,a2,a3,a6,a7])
final['date'] =pd.to_datetime(final['month'].apply(str)+'/'+final['day'].apply(str)+'/'+final['year'].apply(str))
final = final.sort_values(by='level_0').set_index('level_0')

myList = final['date']
answer = pd.Series([i[0] for i in sorted(enumerate(myList), key=lambda x:x[1])],np.arange(500))