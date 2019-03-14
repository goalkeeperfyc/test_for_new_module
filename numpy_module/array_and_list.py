#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 13:47:54 2019

@author: fangyucheng
Email: 664947387@qq.com
"""

import time
import numpy as np

test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
test_array = np.array(test_list)

#get single value
test_list[3]
test_array[3]

#get multi values
wanted_list = [1, 2, 6]
start = time.time()
result_list = [test_list[wanted] for wanted in wanted_list]
end1 = time.time() - start
print("run time for list is %s" % (time.time()-start))
start2 = time.time()
result_array = test_array[wanted_list]
end2 = time.time() - start2
print("run time for array is %s" % (time.time()-start2))

"""
the time cost for array is more than list, possible reason is the size of 
dataset is small
"""