#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 22:44:18 2019

@author: fangyucheng
Email: 664947387@qq.com
"""

import pandas as pd

midx = pd.MultiIndex(levels=[['lama', 'cow', 'falcon'],
                              ['speed', 'weight', 'length']],
                     labels=[[0, 0, 0, 1, 1, 1, 2, 2, 2],
                            [0, 1, 2, 0, 1, 2, 0, 1, 2]])
s = pd.Series([45, 200, 1.2, 30, 250, 1.5, 320, 1, 0.3],
               index=midx)

print(s.index)