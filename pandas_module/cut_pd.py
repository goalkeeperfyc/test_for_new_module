#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 16:42:08 2019

@author: fangyucheng
Email: 664947387@qq.com
"""

import pandas as pd

series = pd.Series([168, 180, 174, 190, 170, 185, 179, 181, 175, 169, 182, 177, 180, 171])

#cut with label
recode = pd.cut(series, 3, labels=['Small', 'Medium', 'Large'])

#cut without label
recode_without_label = pd.cut(series, 3)