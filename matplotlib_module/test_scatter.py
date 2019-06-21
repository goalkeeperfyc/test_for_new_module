#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 23:23:33 2019

@author: fangyucheng
Email: 664947387@qq.com
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4,5,6,7,8])
y = x

plt.figure()
plt.scatter(x, y)

plt.title('test_title')
plt.xlabel('test xlabel')