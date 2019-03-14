#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 00:03:15 2019

@author: fangyucheng
Email: 664947387@qq.com
"""

import matplotlib.pyplot as plt
from random import randint

data_list = [randint(1,15) for x in range(10)] 

plt.bar(data_list)