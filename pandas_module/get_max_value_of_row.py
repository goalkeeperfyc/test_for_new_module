#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 02:10:36 2019

@author: fangyucheng
Email: 664947387@qq.com
"""

import pandas as pd

df = pd.DataFrame({"A": [1, 2, 3, 4], "B": [-2, 8, 1, 9]})
df['max_value'] = df[["A", "B"]].max(axis=1)
