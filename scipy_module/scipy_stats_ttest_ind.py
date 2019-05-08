#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 22:33:24 2019

@author: fangyucheng
Email: 664947387@qq.com
"""


import numpy as np
from scipy import stats

rvs1 = stats.norm.rvs(loc=5,scale=10,size=500)
rvs2 = stats.norm.rvs(loc=5,scale=10,size=500)
result = stats.ttest_ind(rvs1,rvs2)

test_list = list(range(10))
test_list2 = list(range(13))
result2 = stats.ttest_ind(test_list, test_list2)

myarray = np.asarray(test_list)

print(type(rvs1))
print(type(myarray))