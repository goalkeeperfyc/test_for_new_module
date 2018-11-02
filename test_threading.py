# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 13:51:10 2018

@author: fangyucheng
"""


import time
import threading


def run():

    time.sleep(2)

    print('当前线程名称是:%s\n' % threading.currentThread().name)

    time.sleep(2)

if __name__=="__main__":

    start_time=time.time()

    print('这是主线程:%s' % threading.current_thread().name)

    thread_list=[]

    for i in range(5):

        t=threading.Thread(target=run)

        thread_list.append(t)

    for t in thread_list:

        t.start()

    print('主线程结束:%s' % threading.current_thread().name)

print('一共用时:%f' % float(time.time()-start_time))