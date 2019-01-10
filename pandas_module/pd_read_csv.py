#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 08:42:36 2019

@author: fangyucheng
Email: 664947387@qq.com
"""

import pandas as pd
import os 

print(os.getcwd())

csv_name = '/Users/fangyucheng/Documents/code/python_code/test_for_new_module/read_csv.csv'

df = pd.read_csv(csv_name)

df2 = pd.read_csv(csv_name, index_col=2, skiprows=3)

df3 = pd.read_csv(csv_name, index_col=1, skiprows=2)

df4 = pd.read_csv(csv_name, index_col=0, skiprows=2)
df4.index
df4.columns
#index_col the column as index
#skiprows skip the number of rows(starting with 1 instead of 0)
#for computer science data starts with 0