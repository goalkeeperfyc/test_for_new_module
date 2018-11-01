# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 15:08:48 2018

@author: fangyucheng
"""

import asyncio

async def main():
    print('Hello ...')
    await asyncio.sleep(1)
    print('... World!')

# Python 3.7+
asyncio.run(main())