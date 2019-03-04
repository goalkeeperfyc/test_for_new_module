# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 09:55:24 2018

@author: fangyucheng
"""

import os
import time
from multiprocessing import Pool

def func(i):
    time.sleep(5)
    print("this is func %s" % i)
    print("pid is %s" % os.getpid())
    time.sleep(5)
    print("repeat this is func %s" % i)
    print("repeat pid is %s" % os.getpid())


if __name__ == "__main__":
    pool = Pool(5)
    for i in range(10):
        pool.apply_async(func, args=(i,))
    pool.close()
    pool.join()