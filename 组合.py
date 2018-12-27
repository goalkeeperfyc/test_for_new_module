# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 17:42:59 2018

@author: fangyucheng
"""

task_list = list(range(1,26))
task_list.remove(6)
task_list.remove(2)
task_list.remove(1)

final_list = []

for line in task_list:
    new_list = [1, 6]
    new_list.append(line)
    if abs(new_list[-2] - new_list[-1]) == 5 or abs(new_list[-2] - new_list[-1]) == 1:
        print(new_list)
        final_list.append(new_list)
    else:
        pass

for new_list in final_list:
    for line in task_list:
        new_list.append(line)
        if abs(new_list[-2] - new_list[-1]) == 5 or abs(new_list[-2] - new_list[-1]) == 1:
            print(new_list)
            final_list.append(new_list)
    else:
        pass

        

for line_lst in final_list:

    task_list.remove(line)
    