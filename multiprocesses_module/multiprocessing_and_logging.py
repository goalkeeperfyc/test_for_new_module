# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 19:38:48 2018

@author: fangyucheng
"""

import os
import time
from multiprocessing import Pool
from test_for_new_module import logging_output_to_different_files


class Test_Pool():
    
    def __init__(self):
        self.loggerinfo = logging_output_to_different_files.setup_logger('info', 'all.log')
        self.loggererror = logging_output_to_different_files.setup_logger('error', 'error.log')


    def func1(self, a, b=5):
        pid = os.getpid()
        c = a + b
        self.loggerinfo.info('this is process %s with %s' % (pid, c))
        time.sleep(5)
        self.loggererror.error('%s this is test for error' % pid)
        
    def func2(self, c, d):
        pass

if __name__ == '__main__':
    test = Test_Pool()
    pool = Pool(5)
    for num in range(5):
        pool.apply_async(func=test.func1, args=(num,))
    pool.close()
    pool.join()