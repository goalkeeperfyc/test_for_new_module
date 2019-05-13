#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 13 10:16:58 2019

@author: fangyucheng
Email: 664947387@qq.com
"""

import numpy as np

x1 = range(6)
x1_power = np.power(x1, 3)
print(x1_power)

print("="*15)

x2 = [1, 2, 3, 3, 2, 1]
x1_x2_power = np.power(x1, x2)
print(x1_x2_power)

print("="*15)

x3 = np.array([[1, 2, 3, 3, 2, 1],
               [1, 2, 3, 3, 2, 1]])
x1_x3_power = np.power(x1, x3)
print(x1_x3_power)