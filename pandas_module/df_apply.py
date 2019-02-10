#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 13:44:54 2019

@author: fangyucheng
Email: 664947387@qq.com
"""

import pandas as pd
import numpy as np

df = pd.DataFrame(list(range(1,20)))

def function():
    if df[0] > 5:
        return 0
    else:
        return 1

#new_df = df[0].apply(lambda x: function())
new_df2 = df.apply(np.sum)
#
#if df[0] > 5:
#    df['new_column'] = 1
#else:
#    df['new_column'] = 0

df['bool'] = df[0] > 5
df['bool_to_binary'] = df['bool'].astype('int')