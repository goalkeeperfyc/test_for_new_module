# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 19:38:48 2018

@author: fangyucheng
"""

from multiprocessing import Pool
from test_for_new_module.example_of_class import Test_Pool

function = Test_Pool().func1
pool = Pool(5)

for line in range(5):
    pool.apply_async(func=function, args=(line, ), kwds={'b': line})
pool.close()
pool.join()