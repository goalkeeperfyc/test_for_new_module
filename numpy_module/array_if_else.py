#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 13 11:22:35 2019

@author: fangyucheng
Email: 664947387@qq.com
"""

import numpy as np

task = [0.50154066, 0.49899566, 0.50213783]
task_array = np.array(task)
task_array = task_array.reshape(1,3)
new_array = task_array > 0.5

multiply = new_array * 2