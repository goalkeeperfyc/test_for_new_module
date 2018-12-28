# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 10:36:04 2018

@author: fangyucheng
"""

from multiprocessing import Pool

def cal(a, b):
    return a+b

if __name__ == "__main__":
    result_list =[]
    pool = Pool(10)
    for line in range(30):
        result = pool.apply_async(cal, args=(line, line))
        result_list.append(result)
    pool.close()
    pool.join()
    print(result_list)

