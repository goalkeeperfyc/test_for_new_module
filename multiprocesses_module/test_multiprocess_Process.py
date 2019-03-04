# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 09:27:59 2018

@author: fangyucheng
"""

import os
import time
from multiprocessing import Process

def process1():
    time.sleep(5)
    print("I am process 1, pid %s" % os.getpid())
    time.sleep(5)
    print("I am process 1 after sleeping %s" % os.getpid())


def process2():
    time.sleep(5)
    print("I am process 2, pid %s" % os.getpid())
    time.sleep(5)
    print("I am process 2 after sleeping, pid %s" % os.getpid())


if __name__ == "__main__":
    print("Process start, pid is %s" % os.getpid())
    P1 = Process(target=process1)
    P2 = Process(target=process2)
    print("this is a line after P1 and P2 initialized")
    P1.start()
    P2.start()
    P1.join()
    print("process ends")