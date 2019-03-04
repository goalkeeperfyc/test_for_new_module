# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 14:02:31 2018

@author: fangyucheng
"""

import asyncio

@asyncio.coroutine
def hello():
    print("Hello world!")
    r = yield from asyncio.sleep(1)
    print("Hello again!")

