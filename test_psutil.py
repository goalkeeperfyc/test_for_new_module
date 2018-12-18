# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 19:23:46 2018

@author: fangyucheng
"""

import psutil

psutil.cpu_count()
psutil.cpu_count(logical=False)
print(psutil.cpu_count())
print(psutil.cpu_count(logical=False))
psutil.cpu_times()
psutil.pid_exists()
psutil.pids()