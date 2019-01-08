#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 13:49:19 2019

@author: fangyucheng
Email: 664947387@qq.com
"""

people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

def split_title_and_name(person):
    return person.split()[0] + ' ' + person.split()[-1]

#option 1
for person in people:
    #my wrong answer
    print(split_title_and_name(person) == (lambda person: person.split()[0] + ' ' + person.split()[-1]))
    #my correct answer
    print(split_title_and_name(person) == (lambda person: person.split()[0] + ' ' + person.split()[-1])(person))    
    #the answer
    print(split_title_and_name(person) == (lambda x: x.split()[0] + ' ' + x.split()[-1])(person))
    #an interesting test
    print(split_title_and_name == (lambda x: x.split()[0] + ' ' + x.split()[-1]))
    print(split_title_and_name == (lambda person: person.split()[0] + ' ' + person.split()[-1]))
    print(split_title_and_name == (lambda split_title_and_name: split_title_and_name.split()[0] + ' ' + split_title_and_name.split()[-1]))