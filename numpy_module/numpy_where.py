#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 09:58:44 2019

@author: fangyucheng
Email: 664947387@qq.com
"""


import numpy as np

x = np.arange(9.).reshape(3, 3)

new_x = np.zeros_like(x)
x_id = np.where( x > 5 )
new_x[x_id] = 1

new_x2 = np.zeros_like(x)
x_id2 = np.where((x > 5) & (x < 2))
new_x2[x_id2] = 1

new_x3 = np.zeros_like(x)
x_id3 = np.where((x > 5) | (x < 2))
new_x3[x_id3] = 1