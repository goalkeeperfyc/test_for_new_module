#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 18:32:33 2019

@author: fangyucheng
Email: 664947387@qq.com
"""

import numpy as np

x = np.array([[0], [1], [2]])

y = np.squeeze(x)

print("the shape of x is " + str(x.shape))
print("="*20)
print("the shape of y is " + str(y.shape))
print(y)
