#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 08:35:41 2019

@author: fangyucheng
Email: 664947387@qq.com
"""

import pandas as pd

#example of group by function
#df.groupby('Category').apply(lambda df,a,b: sum(df[a] * df[b]), 'Weight (oz.)', 'Quantity'))


d = {
         'one': [1, 2, 3, 4, 5],
         'two': [9, 8, 7, 6, 5],
         'three': ['a', 'b', 'c', 'd', 'e']
    }
df = pd.DataFrame(d)

rename_dict = {'Unnamed: 2': 'Country',
               'Petajoules': 'Energy Supply',
               'Gigajoules': 'Energy Supply per Capita',
               '%': '% Renewable'}

#rename_list = ['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']

df = df.rename(columns=rename_dict)

# Unnamed: 2	Petajoules	Gigajoules	%
