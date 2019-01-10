#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 10:06:44 2019

@author: fangyucheng
Email: 664947387@qq.com
"""


import pandas as pd
import numpy as np

df = pd.DataFrame([[np.nan, 2, np.nan, 0],
                   [3, 4, np.nan, 1],
                   [np.nan, np.nan, np.nan, 5],
                   [np.nan, 3, np.nan, 4]],
                   columns=list('ABCD'))

df1 = df.fillna(0)

replace_dict = {"A": 111,
                "B": 222,
                "C": 333}
df2 = df.fillna(value=replace_dict)
