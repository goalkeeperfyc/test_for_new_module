#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 01:32:10 2019

@author: fangyucheng
Email: 664947387@qq.com
"""

people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

def split_title_and_name(person):
    return person.split('.')

print(list(map(split_title_and_name, people)))

result_map = map(split_title_and_name, people)

for line in result_map:
    print(line)