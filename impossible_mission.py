#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 20:09:03 2018

@author: fangyucheng
"""

import copy

task_list = list(range(1,26))

#remove banned number
task_list.remove(2)

#remove ori number 1 6
#task_list.remove(1)
#task_list.remove(6)


#init ori list
ori_list = [[1, 6, 7], [1, 6, 11]]

count = 1
while count < 20:
    count += 1
    first_result = []
    
    for line in ori_list:
        temp_list = copy.deepcopy(task_list)
        for num in line:
            temp_list.remove(num)
        for num in temp_list:
            new_list = copy.deepcopy(line)
            new_list.append(num)
            first_result.append(new_list)
            continue
    
    ori_list = []
    
    for line in first_result:
        if abs(line[-1] - line[-2]) == 1 or abs(line[-1] - line[-2]) == 5:
            ori_list.append(line)
            print(line)