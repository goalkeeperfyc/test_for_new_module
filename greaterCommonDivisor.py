#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 23:09:10 2020

author: yuchengfang
email: goalkeeperyucheng@gmail.com
"""

def gcd(a, b):
    if b == 0:
        return a
    else:
        # print("Running else")
        gcd(b, a % b)


print(gcd(14, 21))