#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 01:07:25 2019

@author: fangyucheng
Email: 664947387@qq.com
"""

import numpy as np

a = np.array([[1, 2, 3], 
              [4, 5, 6],
              [7, 8, 9],
              [10, 11, 12]])



b = a.reshape(4, 3)
c = a.reshape(4, -1)
d = a.reshape(3, -1)
e = a.reshape(3, 4)

print("the shape of a is " + str(a.shape))
print("the shape of b is " + str(b.shape))
print("the shape of c is " + str(c.shape))
print("the shape of d is " + str(d.shape))
print("the shape of e is " + str(e.shape))

print(a)
print("="*10)
print(d)
print("="*10)
print(e)
print("="*10)