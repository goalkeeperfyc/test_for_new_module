# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 14:59:34 2018

@author: fangyucheng
"""

import multiprocessing

def input_para(old_str1='old_str1',
               old_str2='old_str2'):
    print("This is %s" % old_str1)
    print("And this is %s" % old_str1)

KWARG = {'old_str1': 'i am new',
         'old_str2': 'i am new, too'}

def multi_process_input_para(para_dic):
    pool = multiprocessing.Pool(5)
    for line in range(5):
        pool.apply_async(func=input_para, kwds=para_dic)
    pool.close()
    pool.join()

P1 = multiprocessing.Process(target=multi_process_input_para, args=(KWARG,))
P1.start()