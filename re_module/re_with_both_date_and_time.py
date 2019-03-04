#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 18:45:31 2019

@author: fangyucheng
Email: 664947387@qq.com
"""

import re

month_list = ["january",
              "february",
              "march",
              "april",
              "may",
              "june",
              "july",
              "august",
              "september",
              "october",
              "november",
              "december"]

first_three_list = []

for line in month_list:
    line_first_three = line[:3]
    first_three_list.append(line_first_three)

upper_all_list = []

for line in month_list:
    line_upper = line.upper()
    upper_all_list.append(line_upper)

for line in first_three_list:
    line_upper = line.upper()
    upper_all_list.append(line_upper)

upper_first_letter = []

for line in month_list:
    line_upper = line.capitalize()
    upper_first_letter.append(line_upper)

for line in first_three_list:
    line_upper = line.capitalize()
    upper_first_letter.append(line_upper)

month_list.extend(first_three_list)
month_list.extend(upper_all_list)
month_list.extend(upper_first_letter)