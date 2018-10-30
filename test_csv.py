# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 20:02:08 2018

@author: fangyucheng
"""

import csv

get_header = t[0]

header = []



for key, value in get_header.items():
    header.append(key)


csv_file = open('D:/python_code/export_cgi/file3.csv','a')

output = csv.DictWriter(csv_file, delimiter=',', lineterminator='\n', fieldnames=header)

output.writeheader()
output.writerows(t)

csv_file.close()